# Teoria - Metodos y Encapsulamiento

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Tipos de Metodos

### 1.1 Metodos de Instancia

Los metodos de instancia son las funciones definidas dentro de una clase que operan sobre los atributos del objeto. Reciben `self` como primer parametro.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Metodo de instancia
    def saludar(self):
        return f"Hola, soy {self.nombre}"

    # Metodo que modifica atributos
    def cumplir_anios(self):
        self.edad += 1

p = Persona("Ana", 25)
print(p.saludar())  # Hola, soy Ana
p.cumplir_anios()
print(p.edad)  # 26
```

### 1.2 Metodos de Clase

Los metodos de clase reciben la clase como primer parametro (`cls`) y se decoran con `@classmethod`. Se usan para crear instancias alternative o acceder a atributos de clase.

```python
class Persona:
    total_personas = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.total_personas += 1

    # Metodo de clase
    @classmethod
    def obtener_total(cls):
        return cls.total_personas

    # Metodo de clase alternativo para crear instancias
    @classmethod
    def desde_tuple(cls, datos):
        return cls(datos[0], datos[1])

# Uso de metodo de clase
print(Persona.obtener_total())  # 0
p1 = Persona("Ana")
p2 = Persona("Carlos")
print(Persona.obtener_total())  # 2

# Crear instancia desde tuple
p3 = Persona.desde_tuple(("Maria", 30))
```

### 1.3 Metodos Estaticos

Los metodos estaticos no reciben `self` ni `cls`. Son funciones regulares dentro de la clase que no pueden modificar el estado de la clase o instancia.

```python
class Calculadora:
    @staticmethod
    def sumar(a, b):
        """Suma dos numeros"""
        return a + b

    @staticmethod
    def es_par(numero):
        """Verifica si un numero es par"""
        return numero % 2 == 0

# Uso - no necesitan instancia
print(Calculadora.sumar(5, 3))  # 8
print(Calculadora.es_par(10))   # True
```

---

## 2. Encapsulamiento

El **encapsulamiento** es el principio de ocultar los detalles internos de un objeto y exponer solo lo necesario.

### 2.1 Convenciones de Visibilidad en Python

Python usa convenciones con guiones bajos:

| Convention | Name | Meaning |
|------------|------|---------|
| `public` | Sin guion | Accesible desde cualquier lugar |
| `_protegido` | Un guion | "No tocar" - convencion, no restriction |
| `__privado` | Dos guiones | Name mangling - Python lo renombra |
| `__nombre__` | Doble guion ambos lados | Metodos magicos/reservados |

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # Publico
        self._saldo = saldo_inicial    # Protegido (convencion)
        self.__numero_cuenta = "CU-001" # Privado (name mangling)

    def get_saldo(self):
        """Metodo para acceder al saldo (getter implicito)"""
        return self._saldo

    def set_saldo(self, nuevo_saldo):
        """Metodo para modificar el saldo con validacion"""
        if nuevo_saldo >= 0:
            self._saldo = nuevo_saldo

# Name mangling: __numero_cuenta se convierte en _CuentaBancaria__numero_cuenta
cuenta = CuentaBancaria("Ana", 1000)
print(cuenta.titular)         # Ana
print(cuenta._saldo)          # 1000 (funciona, pero es convencion no usar)
print(cuenta._CuentaBancaria__numero_cuenta)  # CU-001 (acceso forzado)
```

---

## 3. Propiedades con @property

Las propiedades permiten usar getter/setter de forma pythonica, simulando atributos pero con logica detras.

### 3.1 Getter con @property

```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        """Getter para nombre"""
        return self._nombre

    @property
    def edad(self):
        """Getter para edad"""
        return self._edad

    @property
    def es_mayor_edad(self):
        """Propiedad calculada"""
        return self._edad >= 18

# Uso - parece un atributo pero es un metodo
p = Persona("Ana", 25)
print(p.nombre)          # Ana
print(p.es_mayor_edad)  # True
```

### 3.2 Setter con @nombre.setter

```python
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Validar antes de asignar
        if nuevo_nombre and len(nuevo_nombre.strip()) > 0:
            self._nombre = nuevo_nombre.strip()
        else:
            raise ValueError("El nombre no puede estar vacio")

# Uso - como si fuera un atributo
p = Persona("Ana")
p.nombre = "Ana Maria"  # Usa el setter
print(p.nombre)  # Ana Maria
```

### 3.3 Ejemplo Completo de Encapsulamiento

```python
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Temperatura en grados Celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Setter con validacion"""
        if valor < -273.15:
            raise ValueError("Temperatura menor al cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        """Temperatura calculada en Fahrenheit"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Set desde Fahrenheit"""
        self._celsius = (valor - 32) * 5/9

# Uso
temp = Temperatura(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.fahrenheit = 32  # Set en Fahrenheit
print(temp.celsius)      # 0.0
```

---

## 4. Metodos Magicos

Los metodos magicos (o dunder methods) son metodos especiales que Python invoca automaticamente.

### 4.1 Metodos de Representacion

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        """Representacion legible para usuarios"""
        return f"Persona({self.nombre}, {self.edad})"

    def __repr__(self):
        """Representacion tecnica para desarrolladores"""
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

p = Persona("Ana", 25)
print(str(p))    # Persona(Ana, 25)
print(repr(p))   # Persona(nombre='Ana', edad=25)
```

### 4.2 Metodos de Comparacion

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        """=="""
        if not isinstance(other, Persona):
            return False
        return self.nombre == other.nombre and self.edad == other.edad

    def __lt__(self, other):
        """<"""
        return self.edad < other.edad

    def __le__(self, other):
        """<="""
        return self.edad <= other.edad

    def __gt__(self, other):
        """>"""
        return self.edad > other.edad

    def __ge__(self, other):
        """>="""
        return self.edad >= other.edad

p1 = Persona("Ana", 25)
p2 = Persona("Carlos", 30)
print(p1 < p2)   # True
print(p1 == p2)  # False
```

### 4.3 Metodos Aritmeticos

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """+"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """-"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, escalar):
        """*"""
        return Vector(self.x * escalar, self.y * escalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 1)
print(v1 + v2)  # (3, 4)
print(v1 * 2)   # (4, 6)
```

### 4.4 Otros Metodos Magicos Comunes

```python
class Coleccion:
    def __init__(self, datos):
        self.datos = datos

    def __len__(self):
        """len()"""
        return len(self.datos)

    def __getitem__(self, indice):
        """[]"""
        return self.datos[indice]

    def __contains__(self, item):
        """in"""
        return item in self.datos

    def __call__(self):
        """()"""
        return "Llamada al objeto"

c = Coleccion([1, 2, 3])
print(len(c))      # 3
print(c[0])        # 1
print(2 in c)      # True
print(c())         # "Llamada al objeto"
```

---

## 5. Ejemplo Integrador: Sistema de Empleados

```python
class Empleado:
    MINIMO_SALARIO = 1300000
    empleados_creados = 0

    def __init__(self, nombre, cargo, salario):
        self._nombre = nombre
        self._cargo = cargo
        self.salario = salario  # Usa el setter
        Empleado.empleados_creados += 1
        self.id = Empleado.empleados_creados

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor.strip().title()

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, valor):
        cargos_validos = ["Junior", "Senior", "Lead", "Manager"]
        if valor in cargos_validos:
            self._cargo = valor
        else:
            raise ValueError(f"Cargo debe ser uno de: {cargos_validos}")

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < self.MINIMO_SALARIO:
            raise ValueError(f"Salario menor al minimo: {self.MINIMO_SALARIO}")
        self._salario = valor

    @classmethod
    def empleados_totales(cls):
        return cls.empleados_creados

    def aumentar_salario(self, porcentaje):
        """Aumenta el salario por porcentaje"""
        nuevo = self._salario * (1 + porcentaje / 100)
        self.salario = nuevo

    def __str__(self):
        return f"{self.nombre} ({self.cargo}) - ${self.salario:,.0f}"

    def __repr__(self):
        return f"Empleado({self.id}: '{self.nombre}', {self.cargo})"


# Uso
e1 = Empleado("Ana Garcia", "Senior", 3500000)
e2 = Empleado("Carlos Lopez", "Lead", 5000000)

print(e1)  # Ana Garcia (Senior) - $3,500,000
e1.aumentar_salario(10)
print(e1)  # Ana Garcia (Senior) - $3,850,000
print(f"Total empleados: {Empleado.empleados_totales()}")
```

---

**Ultima actualizacion:** 2026-02-08
