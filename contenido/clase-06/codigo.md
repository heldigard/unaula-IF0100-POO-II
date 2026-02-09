# Codigo - Metodos y Encapsulamiento

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Sistema de Biblioteca

### modelo.py

```python
from datetime import datetime

class Libro:
    LIBROS_PRESTADOS = 0

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self._disponible = True
        self._prestamos = []

    # Propiedades
    @property
    def disponible(self):
        return self._disponible

    # Metodos
    def prestar(self):
        if self._disponible:
            self._disponible = False
            Libro.LIBROS_PRESTADOS += 1
            return True
        return False

    def devolver(self):
        if not self._disponible:
            self._disponible = True
            Libro.LIBROS_PRESTADOS -= 1
            return True
        return False

    @classmethod
    def libros_prestados(cls):
        return cls.LIBROS_PRESTADOS

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"


class Usuario:
    def __init__(self, nombre, email):
        self._nombre = nombre
        self.email = email
        self._libros_prestados = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor.strip().title()

    def recibir_libro(self, libro):
        if libro.disponible:
            libro.prestar()
            self._libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            libro.devolver()
            self._libros_prestados.remove(libro)
            return True
        return False

    def __str__(self):
        return f"{self.nombre} ({len(self._libros_prestados)} libros)"


# main.py
from modelo import Libro, Usuario

# Crear libros
libro1 = Libro("1984", "George Orwell", "978-0-452-28423-4")
libro2 = Libro("Cien anos de soledad", "Gabriel Garcia Marquez", "978-0-307-29162-2")

# Crear usuario
usuario1 = Usuario("Ana Garcia", "ana@email.com")

# Prestar libro
usuario1.recibir_libro(libro1)
print(libro1.disponible)  # False
print(f"Libros prestados globalmente: {Libro.libros_prestados()}")  # 1

# Devolver libro
usuario1.devolver_libro(libro1)
print(libro1.disponible)  # True
```

---

## 2. Clase MathUtils con Metodos Estaticos

```python
class MathUtils:
    @staticmethod
    def factorial(n):
        """Calcula el factorial de n"""
        if n < 0:
            raise ValueError("No existe factorial para numeros negativos")
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

    @staticmethod
    def es_primo(n):
        """Verifica si n es primo"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def fibonacci(n):
        """Retorna lista con primeros n numeros de Fibonacci"""
        if n <= 0:
            return []
        fib = [0, 1]
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]

    @staticmethod
    def mcd(a, b):
        """Maximo comun divisor"""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def mcm(a, b):
        """Minimo comun multiplo"""
        return abs(a * b) // MathUtils.mcd(a, b)


# main.py
from MathUtils import MathUtils

print(MathUtils.factorial(5))       # 120
print(MathUtils.es_primo(17))       # True
print(MathUtils.fibonacci(8))       # [0, 1, 1, 2, 3, 5, 8, 13]
print(MathUtils.mcd(48, 18))         # 6
print(MathUtils.mcm(4, 6))          # 12
```

---

## 3. Clase Vector con Metodos Magicos

```python
class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar, self.z * escalar)

    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    def __abs__(self):
        """Magnitud del vector"""
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __len__(self):
        """Dimension del vector"""
        return 3

    def __getitem__(self, indice):
        """Acceso por indice"""
        componentes = [self.x, self.y, self.z]
        return componentes[indice]

    def dot(self, other):
        """Producto punto"""
        return self.x * other.x + self.y * other.y + self.z * other.z


# main.py
from vector import Vector

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)           # Vector(1, 2, 3)
print(v1 + v2)      # Vector(5, 7, 9)
print(v1 - v2)      # Vector(-3, -3, -3)
print(v1 * 2)       # Vector(2, 4, 6)
print(abs(v1))      # 3.74165738677
print(v1.dot(v2))   # 32
print(v1[0])        # 1
```

---

## 4. Clase Rectangulo con Propiedades

```python
class Rectangulo:
    def __init__(self, ancho, alto):
        self._ancho = None
        self._alto = None
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser positivo")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser positivo")
        self._alto = valor

    @property
    def area(self):
        return self._ancho * self._alto

    @property
    def perimetro(self):
        return 2 * (self._ancho + self._alto)

    @property
    def diagonal(self):
        return (self._ancho ** 2 + self._alto ** 2) ** 0.5

    def __str__(self):
        return f"Rectangulo({self.ancho}x{self.alto})"

    def __eq__(self, other):
        if not isinstance(other, Rectangulo):
            return False
        return self.ancho == other.ancho and self.alto == other.alto


# main.py
from rectangulo import Rectangulo

r1 = Rectangulo(10, 5)
r2 = Rectangulo(10, 5)

print(r1)           # Rectangulo(10x5)
print(r1.area)      # 50
print(r1.perimetro) # 30
print(r1.diagonal)  # 11.1803...
print(r1 == r2)      # True
```

---

## 5. Sistema de Carrito con Encapsulamiento

```python
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = valor


class Carrito:
    def __init__(self):
        self._items = {}  # producto -> cantidad

    def agregar(self, producto, cantidad=1):
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser positiva")
        if producto.codigo in self._items:
            self._items[producto.codigo] += cantidad
        else:
            self._items[producto.codigo] = cantidad

    def eliminar(self, codigo, cantidad=None):
        if codigo not in self._items:
            raise ValueError("Producto no encontrado")
        if cantidad is None or cantidad >= self._items[codigo]:
            del self._items[codigo]
        else:
            self._items[codigo] -= cantidad

    def total(self):
        return sum(p.precio * qty for codigo, qty in self._items.items()
                   for p in [self._buscar_producto(codigo)])

    def _buscar_producto(self, codigo):
        """Metodo privado"""
        # Simulado - en la vida real consultaria una base de datos
        pass

    def __len__(self):
        return sum(self._items.values())

    def __str__(self):
        return f"Carrito({len(self)} items)"


# main.py
from producto import Producto
from carrito import Carrito

p1 = Producto("001", "Laptop", 1500000, 10)
p2 = Producto("002", "Mouse", 25000, 50)

carrito = Carrito()
carrito.agregar(p1, 1)
carrito.agregar(p2, 2)
print(carrito)       # Carrito(3 items)
print(carrito.total())  # $1,550,000
```

---

**Ultima actualizacion:** 2026-02-08
