# Teoría - Herencia y Polimorfismo

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Conceptos Fundamentales

### Herencia

La herencia es un mecanismo que permite crear nuevas clases basadas en clases existentes, heredando sus atributos y comportamientos.

```
    ANIMAL (Clase Base)
    ├── nombre
    ├── edad
    ├── comer()
    └── dormir()

    PERRO (Hereda de Animal)
    ├── raza
    └── ladrar()

    GATO (Hereda de Animal)
    └── maullar()
```

### Tipos de Herencia

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Simple** | Una clase hereda de una sola clase base | Perro -> Animal |
| **Multiple** | Una clase hereda de varias clases base | class A(B, C) |
| **Multinivel** | Herencia en cadena | A -> B -> C |
| **Jerarquica** | Multiple clases heredan de una base | Animal -> Perro, Gato |

---

## 2. Implementacion en Python

### Herencia Simple

```python
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Persona:
    """Clase base para personas"""

    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, valor: int):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor

    def presentarse(self) -> str:
        return f"Soy {self._nombre} y tengo {self._edad} años"


class Estudiante(Persona):
    """Estudiante hereda de Persona"""

    def __init__(self, nombre: str, edad: int, codigo: str, carrera: str):
        super().__init__(nombre, edad)
        self._codigo = codigo
        self._carrera = carrera
        self._notas: List[float] = []

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def carrera(self) -> str:
        return self._carrera

    def agregar_nota(self, nota: float) -> None:
        if 0 <= nota <= 5:
            self._notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 5")

    def calcular_promedio(self) -> float:
        if not self._notas:
            return 0.0
        return sum(self._notas) / len(self._notas)

    def presentarse(self) -> str:
        base = super().presentarse()
        return f"{base}, estudio {self._carrera} (código: {self._codigo})"


# Uso
estudiante = Estudiante("Maria", 20, "2024001", "Ingeniería")
estudiante.agregar_nota(4.5)
estudiante.agregar_nota(3.8)
print(estudiante.presentarse())  # Soy Maria y tengo 20 años...
print(f"Promedio: {estudiante.calcular_promedio():.2f}")
```

### Herencia Multinivel

```python
class DispositivoElectronico:
    """Clase base"""

    def __init__(self, marca: str):
        self._marca = marca

    def encender(self) -> str:
        return f"Dispositivo {self._marca} encendido"


class Computadora(DispositivoElectronico):
    """Hereda de DispositivoElectronico"""

    def __init__(self, marca: str, procesador: str):
        super().__init__(marca)
        self._procesador = procesador

    def ejecutar_programa(self, programa: str) -> str:
        return f"Ejecutando {programa} en {self._marca} con {self._procesador}"


class Laptop(Computadora):
    """Hereda de Computadora"""

    def __init__(self, marca: str, procesador: str, autonomia: int):
        super().__init__(marca, procesador)
        self._autonomia = autonomia
        self._bateria = 100

    def usar_bateria(self, porcentaje: int) -> str:
        self._bateria = max(0, self._bateria - porcentaje)
        return f"Batería al {self._bateria}%"


# Uso
laptop = Laptop("Dell", "Intel i7", 8)
print(laptop.encender())  # Dispositivo Dell encendido
print(laptop.ejecutar_programa("VS Code"))
print(laptop.usar_bateria(20))
```

### Herencia Multiple

```python
class Volador:
    def volar(self) -> str:
        return "Volando..."


class Nadador:
    def nadar(self) -> str:
        return "Nadando..."


class Pato(Volador, Nadador):
    """Pato hereda de Volador y Nadador"""

    def graznar(self) -> str:
        return "Cuac Cuac!"


# Uso
pato = Pato()
print(pato.volar())      # Volando...
print(pato.nadar())       # Nadando...
print(pato.graznar())     # Cuac Cuac!

# Method Resolution Order (MRO)
print(Pato.__mro__)  # (<class '__main__.Pato'>, <class '__main__.Volador'>, ...)
```

---

## 3. Polimorfismo

El polimorfismo permite que objetos de diferentes clases respondan al mismo mensaje de formas diferentes.

### Polimorfismo con Metodos

```python
class Figura:
    """Clase abstracta para figuras geometricas"""

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass


class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float):
        self._ancho = ancho
        self._alto = alto

    def area(self) -> float:
        return self._ancho * self._alto

    def perimetro(self) -> float:
        return 2 * (self._ancho + self._alto)


class Circulo(Figura):
    def __init__(self, radio: float):
        self._radio = radio
        self._pi = 3.14159

    def area(self) -> float:
        return self._pi * self._radio ** 2

    def perimetro(self) -> float:
        return 2 * self._pi * self._radio


class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        self._base = base
        self._altura = altura

    def area(self) -> float:
        return (self._base * self._altura) / 2

    def perimetro(self) -> float:
        return 3 * self._base  # Equilatero


# Polimorfismo: misma interfaz, diferentes implementaciones
def mostrar_info(figura: Figura) -> None:
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}")


figuras: List[Figura] = [
    Rectangulo(5, 3),
    Circulo(4),
    Triangulo(6, 4)
]

for figura in figuras:
    mostrar_info(figura)
    print("-" * 20)
```

### Polimorfismo con Funciones

```python
class Animal:
    def hacer_sonido(self) -> str:
        return "Sonido generico"


class Perro(Animal):
    def hacer_sonido(self) -> str:
        return "Guau Guau!"


class Gato(Animal):
    def hacer_sonido(self) -> str:
        return "Miau!"


class Vaca(Animal):
    def hacer_sonido(self) -> str:
        return "Muuu!"


def sonidos_granero(animales: List[Animal]) -> None:
    """Funcion que no sabe que tipo de animal es"""
    for animal in animales:
        print(f"{animal.__class__.__name__}: {animal.hacer_sonido()}")


# Uso
animales = [Perro(), Gato(), Vaca(), Animal()]
sonidos_granero(animales)
```

### Duck Typing

Python usa "duck typing": si camina como un pato y grazna como un pato, es un pato.

```python
class PatoReal:
    def graznar(self) -> str:
        return "Cuac!"


class Persona:
    def graznar(self) -> str:
        return "Hola!"


def hacer_graznar(objeto):
    """No importa el tipo, solo que tenga el metodo graznar"""
    print(objeto.graznar())


hacer_graznar(PatoReal())  # Cuac!
hacer_graznar(Persona())   # Hola!
```

---

## 4. Metodos Especiales

```python
class Persona:
    def __init__(self, nombre: str):
        self._nombre = nombre

    def __str__(self) -> str:
        """Representacion legible para usuarios"""
        return f"Persona: {self._nombre}"

    def __repr__(self) -> str:
        """Representacion tecnica para desarrolladores"""
        return f"Persona(nombre='{self._nombre}')"

    def __eq__(self, other) -> bool:
        """Comparacion por igualdad"""
        if not isinstance(other, Persona):
            return False
        return self._nombre == other._nombre

    def __lt__(self, other) -> bool:
        """Menor que para ordenamiento"""
        if not isinstance(other, Persona):
            return NotImplemented
        return self._nombre < other._nombre

    def __hash__(self) -> int:
        """Hash para usar en diccionarios/conjuntos"""
        return hash(self._nombre)


# Uso
p1 = Persona("Ana")
p2 = Persona("Ana")
p3 = Persona("Carlos")

print(p1)              # Persona: Ana
print(repr(p1))        # Persona(nombre='Ana')
print(p1 == p2)        # True
print(p1 < p3)         # True (orden alfabetico)
print(hash(p1))        # Entero hash
```

---

## 5. Composicion vs Herencia

### Herencia (Es-un)

```python
class Motor:
    def arrancar(self) -> str:
        return "Motor arrancado"


class Auto(Motor):  # Auto ES-UN Motor (incorrecto conceptualmente)
    def conducir(self) -> str:
        return self.arrancar() + " Auto en movimiento"
```

### Composicion (Tiene-un)

```python
class Motor:
    def arrancar(self) -> str:
        return "Motor arrancado"


class Auto:
    """Auto TIENE-UN Motor (mejor diseno)"""

    def __init__(self, marca: str):
        self._marca = marca
        self._motor = Motor()

    def conducir(self) -> str:
        return f"{self._marca}: {self._motor.arrancar()} Auto en movimiento"


# Uso
auto = Auto("Toyota")
print(auto.conducir())
```

### Cuando Usar Cada Uno

| Herencia | Composicion |
|----------|-------------|
| Relacion "es-un" clara | Relacion "tiene-un" |
| Comportamiento compartido | Reutilizacion modular |
| Polimorfismo necesario | Flexibilidad maxima |
| Jerarquia estable | Cambios dinamicos |

---

## 6. Practico: Sistema de Empleados

```python
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Empleado(ABC):
    """Clase base abstracta"""

    def __init__(self, nombre: str, salario_base: float):
        self._nombre = nombre
        self._salario_base = salario_base

    @property
    def nombre(self) -> str:
        return self._nombre

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self._nombre} - {self.__class__.__name__}"


class EmpleadoTiempoCompleto(Empleado):
    """Empleado de tiempo completo"""

    def __init__(self, nombre: str, salario_base: float, bono: float):
        super().__init__(nombre, salario_base)
        self._bono = bono

    def calcular_salario(self) -> float:
        return self._salario_base + self._bono


class EmpleadoPorHoras(Empleado):
    """Empleado por horas"""

    def __init__(self, nombre: str, horas: int, tarifa: float):
        super().__init__(nombre, 0)
        self._horas = horas
        self._tarifa = tarifa

    def calcular_salario(self) -> float:
        return self._horas * self._tarifa


class EmpleadoComisionista(Empleado):
    """Empleado con comision por ventas"""

    def __init__(self, nombre: str, salario_base: float, ventas: float, tasa: float):
        super().__init__(nombre, salario_base)
        self._ventas = ventas
        self._tasa_comision = tasa

    def calcular_salario(self) -> float:
        return self._salario_base + (self._ventas * self._tasa_comision)


def calcular_nomina(empleados: List[Empleado]) -> float:
    """Calcula nomina total (polimorfismo en accion)"""
    total = 0
    print("=== NOMINA ===")
    for emp in empleados:
        salario = emp.calcular_salario()
        total += salario
        print(f"{emp.nombre}: ${salario:,.2f}")
    print(f"Total: ${total:,.2f}")
    return total


# Uso
nomina = [
    EmpleadoTiempoCompleto("Juan", 2000000, 300000),
    EmpleadoPorHoras("Maria", 160, 25000),
    EmpleadoComisionista("Pedro", 1500000, 5000000, 0.05)
]

calcular_nomina(nomina)
```

---

**Ultima actualizacion:** 2026-02-08
