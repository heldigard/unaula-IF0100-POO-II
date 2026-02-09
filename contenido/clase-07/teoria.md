# Teoría - Domain Driven Design

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es DDD?

**Domain Driven Design** es una metodología que centra el desarrollo en el **dominio del negocio**, usando su lenguaje y conceptos.

### Estrategia vs Dominio

```
ESTRATEGIA           DOMINIO
├─ Visión            ├─ Entidades
├─ Objetivos         ├─ Value Objects
└─ Planes            ├─ Agregados
                     ├─ Repositorios
                     └─ Servicios de Dominio
```

---

## 2. Patrones Fundamentales

### Entidad (Entity)

| Característica | Descripción |
|----------------|-------------|
| **Identidad única** | Tiene ID que la distingue |
| **Ciclo de vida** | Persiste en el tiempo |
| **Igualdad** | Por ID, no por atributos |

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


class Estudiante:  # Entidad
    def __init__(self, codigo: str, nombre: str):
        self._codigo = codigo  # Identidad
        self._nombre = nombre

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        self._nombre = valor

    # Igualdad por identidad
    def __eq__(self, other) -> bool:
        if not isinstance(other, Estudiante):
            return False
        return self._codigo == other._codigo

    def __hash__(self) -> int:
        return hash(self._codigo)

    def __repr__(self) -> str:
        return f"Estudiante(codigo='{self._codigo}', nombre='{self._nombre}')"
```

### Value Object

| Característica | Descripción |
|----------------|-------------|
| **Sin identidad** | No tiene ID |
| **Inmutable** | No cambia después de crear |
| **Igualdad** | Por todos sus atributos |

```python
from dataclasses import dataclass


@dataclass(frozen=True)  # Value Object - Inmutable
class Dinero:
    monto: float
    moneda: str

    def __post_init__(self):
        if self.monto < 0:
            raise ValueError("El monto no puede ser negativo")

    def sumar(self, otro: 'Dinero') -> 'Dinero':
        if self.moneda != otro.moneda:
            raise ValueError("No se pueden sumar montos de diferentes monedas")
        return Dinero(self.monto + otro.monto, self.moneda)


@dataclass(frozen=True)
class Direccion:
    calle: str
    ciudad: str
    codigo_postal: str
    pais: str
```

### Agregado (Aggregate)

```
┌──────────────────────┐
│      PEDIDO          │ ← Agregado Root
│  ├── Id              │
│  ├── Fecha           │
│  └── LineasPedido[]  │ ← Entidades internas
│      ├── Producto
│      ├── Cantidad
│      └── Precio
└──────────────────────┘
```

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import uuid


@dataclass(frozen=True)
class ProductoId:
    valor: str


@dataclass(frozen=True)
class LineaPedido:  # Value Object
    producto_id: ProductoId
    cantidad: int
    precio_unitario: Dinero

    def calcular_subtotal(self) -> Dinero:
        return Dinero(
            self.precio_unitario.monto * self.cantidad,
            self.precio_unitario.moneda
        )


class Pedido:  # Agregado Root
    def __init__(self, cliente_id: str):
        self._id = str(uuid.uuid4())
        self._cliente_id = cliente_id
        self._fecha = datetime.now()
        self._lineas: List[LineaPedido] = []
        self._estado = "PENDIENTE"

    @property
    def id(self) -> str:
        return self._id

    @property
    def estado(self) -> str:
        return self._estado

    def agregar_linea(self, producto_id: str, cantidad: int, 
                      precio: Dinero) -> None:
        if self._estado != "PENDIENTE":
            raise ValueError("No se pueden modificar pedidos confirmados")
        
        linea = LineaPedido(
            ProductoId(producto_id),
            cantidad,
            precio
        )
        self._lineas.append(linea)

    def calcular_total(self) -> Dinero:
        if not self._lineas:
            return Dinero(0, "USD")
        
        total = self._lineas[0].calcular_subtotal()
        for linea in self._lineas[1:]:
            total = total.sumar(linea.calcular_subtotal())
        return total

    def confirmar(self) -> None:
        if not self._lineas:
            raise ValueError("No se puede confirmar un pedido vacío")
        self._estado = "CONFIRMADO"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pedido):
            return False
        return self._id == other._id
```

---

## 3. Bounded Contexts

Dividir el dominio en contexts con límites claros:

```
VENTAS          INVENTARIO        CONTABILIDAD
├─ Pedido       ├─ Producto       ├─ Factura
├─ Cliente      ├─ Stock         ├─ Asiento
└─ Descuento    └─ Almacén        └─ Cuenta
```

```python
# Contexto: Ventas
class PedidoService:
    """Servicio de dominio para gestionar pedidos"""
    
    def __init__(self, repositorio_pedidos, servicio_inventario):
        self._repo_pedidos = repositorio_pedidos
        self._servicio_inventario = servicio_inventario

    def crear_pedido(self, cliente_id: str) -> Pedido:
        pedido = Pedido(cliente_id)
        self._repo_pedidos.guardar(pedido)
        return pedido

    def agregar_producto(self, pedido_id: str, producto_id: str, 
                         cantidad: int) -> None:
        # Verificar disponibilidad en inventario
        if not self._servicio_inventario.verificar_disponibilidad(
            producto_id, cantidad):
            raise ValueError("Producto no disponible")
        
        pedido = self._repo_pedidos.obtener(pedido_id)
        precio = self._servicio_inventario.obtener_precio(producto_id)
        
        pedido.agregar_linea(producto_id, cantidad, precio)
        self._repo_pedidos.guardar(pedido)


# Repositorio (Interfaz)
from abc import ABC, abstractmethod


class RepositorioPedidos(ABC):
    @abstractmethod
    def guardar(self, pedido: Pedido) -> None:
        pass

    @abstractmethod
    def obtener(self, pedido_id: str) -> Optional[Pedido]:
        pass

    @abstractmethod
    def listar_por_cliente(self, cliente_id: str) -> List[Pedido]:
        pass
```

---

**Última actualización:** 2026-02-01
