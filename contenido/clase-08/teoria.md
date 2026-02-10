# Teoria - Clases Abstractas e Interfaces

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Conceptos Fundamentales

### Clases Abstractas

Una clase abstracta es una clase que no puede ser instanciada directamente y sirve como plantilla para otras clases. Contiene metodos abstractos (sin implementacion) que deben ser implementados por las clases derivadas.

```
         ┌─────────────────────┐
         │   FIGURA (Abstract) │
         ├─────────────────────┤
         │ + color             │
         ├─────────────────────┤
         │ + area() {abstract} │
         │ + perimetro()       │
         │   {abstract}        │
         └──────────┬──────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
   ┌────▼────┐ ┌────▼────┐ ┌────▼────┐
   │Rectangulo│ │ Circulo │ │Triangulo│
   └─────────┘ └─────────┘ └─────────┘
```

### Interfaces

Una interfaz define un contrato (conjunto de metodos) que una clase debe implementar. En Python, las interfaces se implementan usando clases abstractas con el modulo `abc`.

```python
from abc import ABC, abstractmethod
from typing import Protocol


# Interface (Protocolo en Python 3.8+)
class Volador(Protocol):
    def volar(self) -> str: ...


class Nadador(Protocol):
    def nadar(self) -> str: ...


# Clase abstracta como interfaz
class Conectable(ABC):
    @abstractmethod
    def conectar(self) -> None: ...

    @abstractmethod
    def desconectar(self) -> None: ...
```

---

## 2. Implementacion en Python

### Clase Abstracta Base

```python
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Figura(ABC):
    """Clase abstracta para figuras geometricas"""

    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @abstractmethod
    def area(self) -> float:
        """Metodo abstracto - debe ser implementado"""
        pass

    @abstractmethod
    def perimetro(self) -> float:
        """Metodo abstracto - debe ser implementado"""
        pass

    def __str__(self) -> str:
        return f"Figura {self.__class__.__name__} (color: {self._color})"


# Las clases concretas DEBEN implementar todos los metodos abstractos
class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float, color: str):
        super().__init__(color)
        self._ancho = ancho
        self._alto = alto

    def area(self) -> float:
        return self._ancho * self._alto

    def perimetro(self) -> float:
        return 2 * (self._ancho + self._alto)


class Circulo(Figura):
    def __init__(self, radio: float, color: str):
        super().__init__(color)
        self._radio = radio

    def area(self) -> float:
        return 3.14159 * self._radio ** 2

    def perimetro(self) -> float:
        return 2 * 3.14159 * self._radio
```

### Interfaces con Protocol (Python 3.8+)

```python
from typing import Protocol


class Repositorio(Protocol):
    """Interfaz para repositorios de datos"""

    def guardar(self, entidad) -> None: ...
    def buscar_por_id(self, id: int): ...
    def listar_todos(self) -> List: ...
    def eliminar(self, id: int) -> None: ...


class UsuarioRepositorio(Repositorio):
    """Implementacion concreta"""

    def __init__(self):
        self._usuarios = {}

    def guardar(self, usuario) -> None:
        self._usuarios[usuario.id] = usuario

    def buscar_por_id(self, id: int):
        return self._usuarios.get(id)

    def listar_todos(self) -> List:
        return list(self._usuarios.values())

    def eliminar(self, id: int) -> None:
        if id in self._usuarios:
            del self._usuarios[id]
```

### Metodos Concretos en Clases Abstractas

```python
from abc import ABC, abstractmethod


class Empleado(ABC):
    """Clase abstracta con metodos concretos y abstractos"""

    def __init__(self, nombre: str, salario_base: float):
        self._nombre = nombre
        self._salario_base = salario_base

    @property
    def nombre(self) -> str:
        return self._nombre

    @abstractmethod
    def calcular_salario(self) -> float:
        """Metodo abstracto - cada tipo lo implementa diferente"""
        pass

    def obtener_info(self) -> str:
        """Metodo concreto - coman a todas las subclases"""
        return f"{self._nombre}: ${self.calcular_salario():,.2f}"

    def __str__(self) -> str:
        return self.obtener_info()


class EmpleadoTiempoCompleto(Empleado):
    """Implementacion concreta"""

    def __init__(self, nombre: str, salario_base: float, bono: float):
        super().__init__(nombre, salario_base)
        self._bono = bono

    def calcular_salario(self) -> float:
        return self._salario_base + self._bono


class EmpleadoPorHoras(Empleado):
    """Otra implementacion concreta"""

    def __init__(self, nombre: str, horas: float, tarifa: float):
        super().__init__(nombre, 0)
        self._horas = horas
        self._tarifa = tarifa

    def calcular_salario(self) -> float:
        return self._horas * self._tarifa
```

---

## 3. Herencia de Clases Abstractas

```python
from abc import ABC, abstractmethod
from typing import List


class Dispositivo(ABC):
    """Clase base abstracta"""

    def __init__(self, marca: str):
        self._marca = marca
        self._encendido = False

    @abstractmethod
    def encender(self) -> None:
        pass

    @abstractmethod
    def apagar(self) -> None:
        pass

    def esta_encendido(self) -> bool:
        return self._encendido


class Computadora(Dispositivo):
    """Clase intermedia"""

    def __init__(self, marca: str, procesador: str):
        super().__init__(marca)
        self._procesador = procesador
        self._sistema_operativo = None

    @abstractmethod
    def instalar_sistema(self, so: str) -> None:
        pass


class Laptop(Computadora):
    """Clase concreta"""

    def __init__(self, marca: str, procesador: str, autonomia: int):
        super().__init__(marca, procesador)
        self._autonomia = autonomia
        self._bateria = 100

    def encender(self) -> None:
        if self._bateria > 0:
            self._encendido = True
            print(f"Laptop {self._marca} encendida")

    def apagar(self) -> None:
        self._encendido = False
        print(f"Laptop {self._marca} apagada")

    def instalar_sistema(self, so: str) -> None:
        self._sistema_operativo = so
        print(f"Sistema {so} instalado en {self._marca}")

    def usar_bateria(self, porcentaje: int) -> None:
        self._bateria = max(0, self._bateria - porcentaje)
```

---

## 4. Mixins y Herencia Multiple

```python
from abc import ABC, abstractmethod


# Mixin: proporciona funcionalidad adicional
class Logueable:
    """Mixin para agregar capacidades de logging"""

    def loguear(self, mensaje: str) -> None:
        print(f"[LOG] {self.__class__.__name__}: {mensaje}")


class Serializable:
    """Mixin para serializacion"""

    def a_dict(self) -> dict:
        return self.__dict__.copy()


class Temporizable:
    """Mixin para medir tiempo"""

    def medir_tiempo(self, func):
        def wrapper(*args, **kwargs):
            inicio = datetime.now()
            resultado = func(*args, **kwargs)
            fin = datetime.now()
            print(f"Tiempo: {(fin - inicio).total_seconds()}s")
            return resultado
        return wrapper


# Clase que usa mixins
class Dispositivo(ABC, Logueable, Serializable):
    """Clase abstracta con mixins"""

    def __init__(self, marca: str):
        self._marca = marca
        self._encendido = False
        self.loguear(f"Dispositivo {marca} creado")

    @abstractmethod
    def encender(self) -> None: ...


class SmartPhone(Dispositivo):
    def __init__(self, marca: str, modelo: str):
        super().__init__(marca)
        self.modelo = modelo

    def encender(self) -> None:
        self._encendido = True
        self.loguear(f"{self._marca} {self.modelo} encendido")
```

---

## 5. Polimorfismo con Clases Abstractas

```python
from abc import ABC, abstractmethod
from typing import List


class Figura(ABC):
    """Interfaz comun para todas las figuras"""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimetro(self) -> float: ...

    @abstractmethod
    def escalar(self, factor: float) -> None: ...


class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float):
        self._ancho = ancho
        self._alto = alto

    def area(self) -> float:
        return self._ancho * self._alto

    def perimetro(self) -> float:
        return 2 * (self._ancho + self._alto)

    def escalar(self, factor: float) -> None:
        self._ancho *= factor
        self._alto *= factor


class Circulo(Figura):
    def __init__(self, radio: float):
        self._radio = radio

    def area(self) -> float:
        return 3.14159 * self._radio ** 2

    def perimetro(self) -> float:
        return 2 * 3.14159 * self._radio

    def escalar(self, factor: float) -> None:
        self._radio *= factor


# Polimorfismo: misma interfaz, diferentes implementaciones
def calcular_area_total(figuras: List[Figura]) -> float:
    return sum(f.area() for f in figuras)


def escalar_todas(figuras: List[Figura], factor: float) -> None:
    for figura in figuras:
        figura.escalar(factor)


# Uso
figuras: List[Figura] = [
    Rectangulo(5, 3),
    Circulo(4),
    Rectangulo(2, 2)
]

print(f"Area total: {calcular_area_total(figuras):.2f}")
escalar_todas(figuras, 2)
print(f"Area total (x2): {calcular_area_total(figuras):.2f}")
```

---

## 6. Interfaces vs Clases Abstractas

| Caracteristica | Interfaz | Clase Abstracta |
|----------------|----------|-----------------|
| **Metodos abstractos** | Solo abstratos | Abstactos y concretos |
| **Atributos** | No tiene | Si tiene |
| **Herencia multiple** | Si | No (Python si) |
| **Proposito** | Definir contrato | Proporcionar plantilla parcial |
| **Instanciable** | No | No |

```python
from abc import ABC, abstractmethod


# Interfaz: solo define metodos (contrato)
class Volador(ABC):
    @abstractmethod
    def volar(self) -> str: ...


# Clase abstracta: combina abstraccion con implementacion parcial
class Ave(ABC):
    def __init__(self, nombre: str):
        self._nombre = nombre

    @abstractmethod
    def volar(self) -> str: ...

    @abstractmethod
    def obtener_nombre(self) -> str: ...

    def describir(self) -> str:
        """Metodo concreto - coman a todas las aves"""
        return f"Ave: {self.obtener_nombre()}, {self.volar()}"


class Aguila(Ave):
    def volar(self) -> str:
        return "Volando a gran altura"

    def obtener_nombre(self) -> str:
        return "Aguila Real"
```

---

## 7. Practico: Sistema de Gestion de Formas

```python
from abc import ABC, abstractmethod
from math import pi, sqrt
from typing import List


class Figura2D(ABC):
    """Interface base para todas las figuras 2D"""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimetro(self) -> float: ...

    @abstractmethod
    def mover(self, dx: float, dy: float) -> None: ...


class FiguraColoreada(Figura2D):
    """Mixin: adiciona color a cualquier figura"""

    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, valor: str) -> None:
        self._color = valor


class Rectangulo(FiguraColoreada):
    """Rectangulo con color"""

    def __init__(self, x: float, y: float, ancho: float, alto: float, color: str):
        super().__init__(color)
        self._x = x
        self._y = y
        self._ancho = ancho
        self._alto = alto

    def area(self) -> float:
        return self._ancho * self._alto

    def perimetro(self) -> float:
        return 2 * (self._ancho + self._alto)

    def mover(self, dx: float, dy: float) -> None:
        self._x += dx
        self._y += dy

    def __str__(self) -> str:
        return f"Rectangulo en ({self._x}, {self._y}), color: {self._color}"


class Circulo(FiguraColoreada):
    """Circulo con color"""

    def __init__(self, x: float, y: float, radio: float, color: str):
        super().__init__(color)
        self._x = x
        self._y = y
        self._radio = radio

    def area(self) -> float:
        return pi * self._radio ** 2

    def perimetro(self) -> float:
        return 2 * pi * self._radio

    def mover(self, dx: float, dy: float) -> None:
        self._x += dx
        self._y += dy

    def __str__(self) -> str:
        return f"Circulo en ({self._x}, {self._y}), radio: {self._radio}, color: {self._color}"


# Uso
def mostrar_figuras(figuras: List[Figura2D]) -> None:
    print("=== FIGURAS ===")
    for fig in figuras:
        print(f"{fig}: Area={fig.area():.2f}, Perimetro={fig.perimetro():.2f}")


if __name__ == "__main__":
    figuras: List[Figura2D] = [
        Rectangulo(0, 0, 5, 3, "rojo"),
        Circulo(2, 2, 4, "azul"),
        Rectangulo(1, 1, 2, 2, "verde")
    ]

    mostrar_figuras(figuras)
```

---

**Ultima actualizacion:** 2026-02-08
