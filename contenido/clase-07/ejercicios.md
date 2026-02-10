# Ejercicios - Herencia y Polimorfismo

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Sistema de Vehiculos

**Objetivo:** Practicar herencia y polimorfismo

Modelar un sistema de vehiculos con:

### Clases requeridas:
- `Vehiculo` (clase base abstracta)
  - `marca`, `modelo`, `año`
  - `abstract acelerar()`
  - `abstract frenar()`
  - `__str__()`

- `Automovil(Vehiculo)`
  - `num_puertas`
  - `tipo_combustible`
  - Implementacion concreta

- `Motocicleta(Vehiculo)`
  - `cilindrada`
  - `tiene_parabrisas`
  - Implementacion concreta

- `Camion(Vehiculo)`
  - `capacidad_carga`
  - `num_ejes`
  - Implementacion concreta

### Requisitos:
1. Crear vehiculos de cada tipo
2. Usar polimorfismo para mostrar informacion
3. Crear una flota y calcular promedio de año

### Codigo de inicio:

```python
from abc import ABC, abstractmethod
from typing import List


class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, año: int):
        # Completar
        pass

    @abstractmethod
    def acelerar(self) -> str:
        pass

    @abstractmethod
    def frenar(self) -> str:
        pass


# Completar las demas clases...
```

---

## Ejercicio 2: Tienda de electronicos

**Objetivo:** Implementar herencia multiple y composicion

### Sistema de productos electronicos:

```
Producto Electronico
├── Dispositivo
│   ├── Telefono (encendible, recargable)
│   ├── Laptop (encendible, recargable)
│   └── Television (encendible)
└── Accesorio
    ├── Cargador (recargable)
    └── Auricular
```

### Interfaces (traits):
- `Encendible`: `encender()`, `apagar()`
- `Recargable`: `cargar()`, `nivel_bateria()`

### Requisitos:
1. Implementar con herencia multiple o composicion
2. Mostrar polimorfismo con metodo `mostrar_info()`
3. Crear inventario mixto

---

## Ejercicio 3: Universidad (Herencia jerarquica)

**Objetivo:** Practicar herencia multinivel y polimorfismo

### Estructura:
```
Persona
└── Empleado
    ├── Docente
    │   ├── TiempoCompleto
    │   └── Catedra
    └── Administrativo
```

### Cada clase debe tener:
- Atributos propios
- Metodo `calcular_salario()` polimorfico
- `__str__()` con informacion completa

### Datos de ejemplo:
- Docente Tiempo Completo: salario base + bono antigüedad
- Docente Catedra: horas trabajadas × tarifa hora
- Administrativo: salario fijo + gratificación

---

## Ejercicio 4: Juego de estrategia

**Objetivo:** Polimorfismo avanzado con unidades de juego

### Unidades:
```
Unidad (abstracta)
├── Milicia
│   ├── Guerrero
│   ├── Arquero
│   └── Caballero
└── Especial
    ├── Mago
    └── Curandero
```

### Metodos:
- `atacar(objetivo: Unidad) -> float`
- `recibir_daño(cantidad: float) -> None`
- `esta_vivo() -> bool`

### Requisitos:
1. Cada tipo de unidad calcula dano diferente
2. Mago tiene ataque magico (ignora armadura)
3. Curandero puede curar aliados

---

## Ejercicio 5: Sistema de archivos (Composicion vs Herencia)

**Objetivo:** Comparar composicion y herencia

### Opcion A - Herencia:
```python
class Archivo
class Carpeta(Archivo)
class EnlaceSimbolico(Archivo)
```

### Opcion B - Composicion:
```python
class Nodo:
    tipo: "archivo" | "carpeta"
    contenido: str | List[Nodo]
```

### Tarea:
1. Implementar ambas opciones
2. Comparar ventajas y desventajas
3. ¿Cual es mejor para un sistema de archivos real?

---

## Solucion Ejercicio 1 (Referencia)

```python
from abc import ABC, abstractmethod
from typing import List


class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, año: int):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    @property
    def marca(self) -> str:
        return self._marca

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def año(self) -> int:
        return self._año

    @abstractmethod
    def acelerar(self) -> str:
        pass

    @abstractmethod
    def frenar(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self._marca} {self._modelo} ({self._año})"


class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, año: int,
                 num_puertas: int, tipo_combustible: str):
        super().__init__(marca, modelo, año)
        self._num_puertas = num_puertas
        self._tipo_combustible = tipo_combustible

    def acelerar(self) -> str:
        return f"{self._modelo}: Motor ronroneando..."

    def frenar(self) -> str:
        return f"{self._modelo}: Frenos activados"

    def __str__(self) -> str:
        return f"{super().__str__()} - {self._num_puertas} puertas, {self._tipo_combustible}"


# Continuara...
```

---

**Ultima actualizacion:** 2026-02-08
