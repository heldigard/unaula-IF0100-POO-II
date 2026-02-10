# Codigo - Herencia y Polimorfismo

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Ejemplo Completo: Sistema de Figuras Geometricas

```python
from abc import ABC, abstractmethod
from math import pi
from typing import List


class Figura(ABC):
    """Clase abstracta base para todas las figuras"""

    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Figura {self.__class__.__name__} (color: {self._color})"


class Rectangulo(Figura):
    """Rectangulo con ancho y alto"""

    def __init__(self, ancho: float, alto: float, color: str = "azul"):
        super().__init__(color)
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self) -> float:
        return self._ancho

    @property
    def alto(self) -> float:
        return self._alto

    def area(self) -> float:
        return self._ancho * self._alto

    def perimetro(self) -> float:
        return 2 * (self._ancho + self._alto)


class Circulo(Figura):
    """Circulo con radio"""

    def __init__(self, radio: float, color: str = "rojo"):
        super().__init__(color)
        self._radio = radio

    @property
    def radio(self) -> float:
        return self._radio

    def area(self) -> float:
        return pi * self._radio ** 2

    def perimetro(self) -> float:
        return 2 * pi * self._radio


class Triangulo(Figura):
    """Triangulo equilatero"""

    def __init__(self, lado: float, color: str = "verde"):
        super().__init__(color)
        self._lado = lado

    @property
    def lado(self) -> float:
        return self._lado

    def area(self) -> float:
        return (self._lado ** 2 * (3 ** 0.5)) / 4

    def perimetro(self) -> float:
        return 3 * self._lado


# Uso del sistema de figuras
if __name__ == "__main__":
    figuras: List[Figura] = [
        Rectangulo(5, 3, "azul"),
        Circulo(4, "rojo"),
        Triangulo(6, "verde")
    ]

    print("=== SISTEMA DE FIGURAS ===\n")

    for figura in figuras:
        print(figura)
        print(f"  Area: {figura.area():.2f}")
        print(f"  Perimetro: {figura.perimetro():.2f}\n")

    # Calcular area total
    area_total = sum(f.area() for f in figuras)
    print(f"Area total de todas las figuras: {area_total:.2f}")
```

---

## 2. Sistema de Empleados con Polimorfismo

```python
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Empleado(ABC):
    """Clase abstracta base para empleados"""

    def __init__(self, nombre: str, identificacion: str):
        self._nombre = nombre
        self._id = identificacion
        self._fecha_ingreso = datetime.now()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def identificacion(self) -> str:
        return self._id

    @abstractmethod
    def calcular_salario(self) -> float:
        """Metodo abstracto que cada empleado implementa"""
        pass

    @abstractmethod
    def obtener_info(self) -> str:
        """Informacion del empleado"""
        pass

    def antiguedad(self) -> int:
        """Anios de antiguedad"""
        return datetime.now().year - self._fecha_ingreso.year


class EmpleadoTiempoCompleto(Empleado):
    """Empleado con salario fijo mensual"""

    def __init__(self, nombre: str, identificacion: str, salario_mensual: float):
        super().__init__(nombre, identificacion)
        self._salario_mensual = salario_mensual

    def calcular_salario(self) -> float:
        return self._salario_mensual

    def obtener_info(self) -> str:
        return f"Tiempo Completo - ${self._salario_mensual:,.0f}/mes"


class EmpleadoPorHoras(Empleado):
    """Empleado que cobra por horas trabajadas"""

    def __init__(self, nombre: str, identificacion: str, horas_trabajadas: float, tarifa_hora: float):
        super().__init__(nombre, identificacion)
        self._horas = horas_trabajadas
        self._tarifa = tarifa_hora

    def calcular_salario(self) -> float:
        return self._horas * self._tarifa

    def obtener_info(self) -> str:
        return f"Por Horas - ${self._tarifa:,.0f}/hora x {self._horas} horas"


class EmpleadoComisionista(Empleado):
    """Empleado con salario base + comision por ventas"""

    def __init__(self, nombre: str, identificacion: str, salario_base: float,
                 total_ventas: float, porcentaje_comision: float):
        super().__init__(nombre, identificacion)
        self._salario_base = salario_base
        self._ventas = total_ventas
        self._porcentaje = porcentaje_comision

    def calcular_salario(self) -> float:
        return self._salario_base + (self._ventas * self._porcentaje / 100)

    def obtener_info(self) -> str:
        comision = self._ventas * self._porcentaje / 100
        return f"Comision - Base: ${self._salario_base:,.0f} + {self._porcentaje}% de ${self._ventas:,.0f}"


def procesar_nomina(empleados: List[Empleado]) -> None:
    """Procesa la nomina de todos los empleados"""
    print("=== PROCESO DE NOMINA ===\n")

    total = 0
    for emp in empleados:
        salario = emp.calcular_salario()
        total += salario

        print(f"Empleado: {emp.nombre}")
        print(f"  ID: {emp.identificacion}")
        print(f"  Tipo: {emp.obtener_info()}")
        print(f"  Salario: ${salario:,.2f}\n")

    print(f"Total a pagar: ${total:,.2f}")


if __name__ == "__main__":
    empleados = [
        EmpleadoTiempoCompleto("Ana Garcia", "1001", 2500000),
        EmpleadoPorHoras("Carlos Rodriguez", "1002", 160, 25000),
        EmpleadoComisionista("Maria Lopez", "1003", 1500000, 50000000, 5)
    ]

    procesar_nomina(empleados)
```

---

## 3. Herencia Multiple: Dispositivos Electronicos

```python
class Encendible:
    """Capacidad de ser encendido/apagado"""

    def __init__(self):
        self._encendido = False

    def encender(self) -> None:
        self._encendido = True
        print(f"{self.__class__.__name__}: Encendido")

    def apagar(self) -> None:
        self._encendido = False
        print(f"{self.__class__.__name__}: Apagado")

    def esta_encendido(self) -> bool:
        return self._encendido


class ConectableWifi:
    """Capacidad de conectarse a WiFi"""

    def __init__(self):
        self._wifi_conectado = False

    def conectar_wifi(self, red: str) -> None:
        self._wifi_conectado = True
        print(f"Conectado a WiFi: {red}")

    def desconectar_wifi(self) -> None:
        self._wifi_conectado = False
        print("Desconectado de WiFi")


class Reproducible:
    """Capacidad de reproducir contenido"""

    def __init__(self):
        self._reproduciendo = False

    def reproducir(self, contenido: str) -> None:
        self._reproduciendo = True
        print(f"Reproduciendo: {contenido}")

    def pausar(self) -> None:
        self._reproduciendo = False
        print("Pausado")


# Herencia multiple
class Smartphone(Encendible, ConectableWifi, Reproducible):
    """Smartphone con todas las capacidades"""

    def __init__(self, marca: str, modelo: str):
        Encendible.__init__(self)
        ConectableWifi.__init__(self)
        Reproducible.__init__(self)
        self._marca = marca
        self._modelo = modelo

    def __str__(self) -> str:
        estado = "encendido" if self._encendido else "apagado"
        return f"{self._marca} {self._modelo} ({estado})"


class Televisor(Encendible, ConectableWifi, Reproducible):
    """Televisor inteligente"""

    def __init__(self, marca: str, pulgadas: int):
        Encendible.__init__(self)
        ConectableWifi.__init__(self)
        Reproducible.__init__(self)
        self._marca = marca
        self._pulgadas = pulgadas

    def __str__(self) -> str:
        return f"TV {self._marca} {self._pulgadas}\""


def mostrar_dispositivos(dispositivo):
    """Demo de polimorfismo con diferentes dispositivos"""
    print(f"\n=== {dispositivo.__class__.__name__} ===")
    print(dispositivo)

    if hasattr(dispositivo, 'encender'):
        dispositivo.encender()

    if hasattr(dispositivo, 'conectar_wifi'):
        dispositivo.conectar_wifi("MiRed_WiFi")

    if hasattr(dispositivo, 'reproducir'):
        dispositivo.reproducir("Pelicula ejemplo")


if __name__ == "__main__":
    dispositivos = [
        Smartphone("Samsung", "Galaxy S24"),
        Televisor("LG", 55)
    ]

    for dispositivo in dispositivos:
        mostrar_dispositivos(dispositivo)
```

---

## 4. Ejercicio Guiado: Sistema de Animales

```python
from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    """Clase base abstracta para animales"""

    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def edad(self) -> int:
        return self._edad

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    @abstractmethod
    def mover(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self._nombre} ({self._edad} años)"


class Mamifero(Animal):
    """Clase intermedia para mamiferos"""

    @abstractmethod
    def amamantar(self) -> str:
        pass


class Ave(Animal):
    """Clase intermedia para aves"""

    def __init__(self, nombre: str, edad: int, envergadura: float):
        super().__init__(nombre, edad)
        self._envergadura = envergadura

    @abstractmethod
    def volar(self) -> str:
        pass


# Implementaciones concretas
class Perro(Mamifero):
    def __init__(self, nombre: str, edad: int, raza: str):
        super().__init__(nombre, edad)
        self._raza = raza

    def hacer_sonido(self) -> str:
        return "Guau Guau!"

    def mover(self) -> str:
        return "Caminando en 4 patas"

    def amamantar(self) -> str:
        return "Amamantando a sus crias"

    def __str__(self) -> str:
        return f"{super().__str__()} - Raza: {self._raza}"


class Gato(Mamifero):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)

    def hacer_sonido(self) -> str:
        return "Miau!"

    def mover(self) -> str:
        return "Saltando y caminando"

    def amamantar(self) -> str:
        return "Amamantando"


class Aguila(Ave):
    def __init__(self, nombre: str, edad: int, envergadura: float):
        super().__init__(nombre, edad, envergadura)

    def hacer_sonido(self) -> str:
        return "Chillido penetrante"

    def mover(self) -> str:
        return "Volando a gran altura"

    def volar(self) -> str:
        return f"Volando con envergadura de {self._envergadura}m"


class Pinguino(Ave):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad, 1.5)

    def hacer_sonido(self) -> str:
        return "Graznido"

    def mover(self) -> str:
        return "Caminando y nadando"

    def volar(self) -> str:
        return "No puede volar (alas pequenas)"


def hacer_concurso_sonidos(animales: List[Animal]) -> None:
    print("=== CONCURSO DE SONIDOS ===\n")
    for animal in animales:
        print(f"{animal.nombre}: {animal.hacer_sonido()}")


def zoo_virtual(animales: List[Animal]) -> None:
    print("\n=== RECORRIDO DEL ZOO ===\n")
    for animal in animales:
        print(animal)
        print(f"  Sonido: {animal.hacer_sonido()}")
        print(f"  Movimiento: {animal.mover()}")

        if isinstance(animal, Mamifero):
            print(f"  Lactancia: {animal.amamantar()}")
        elif isinstance(animal, Ave):
            print(f"  Vuelo: {animal.volar()}")

        print()


if __name__ == "__main__":
    animales = [
        Perro("Max", 5, "Golden Retriever"),
        Gato("Luna", 3),
        Aguila("AguilaReal", 10, 2.5),
        Pinguino("Pipo", 8)
    ]

    hacer_concurso_sonidos(animales)
    zoo_virtual(animales)
```

---

**Ultima actualizacion:** 2026-02-08
