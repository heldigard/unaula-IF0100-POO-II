# Teoria - Clases, Objetos y Atributos

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Conceptos Fundamentales de POO

### 1.1 Que es una Clase?

Una **clase** es una plantilla o molde que define las caracteristicas y comportamientos que tendran los objetos creados a partir de ella. En Python, las clases son blueprint que combinan datos (atributos) y funciones (metodos).

### 1.2 Que es un Objeto?

Un **objeto** es una instancia especifica de una clase. Cada objeto tiene su propio conjunto de valores para los atributos definidos en la clase, pero comparten la misma estructura y comportamiento.

### Relacion Clase-Objeto

```
CLASE (Molde/Plantilla)          OBJETO (Instancia concreta)
+------------------+              +------------------+
|     Persona      |              | persona1         |
+------------------+              +------------------|
| atributos:       |              | nombre: "Ana"   |
| - nombre         | --------->   | edad: 25        |
| - edad           |              | email: "a@b.com"|
|------------------|              +------------------|
| metodos:         |
| - hablar()       |
| - caminar()      |
+------------------+
```

---

## 2. Definicion de Clases en Python

### Sintaxis Basica

```python
class Persona:
    """Clase que representa una persona"""
    pass
```

### Creacion de Objetos

```python
# Crear instancias de la clase Persona
persona1 = Persona()
persona2 = Persona()

print(type(persona1))  # <class '__main__.Persona'>
print(persona1 is persona2)  # False - son objetos diferentes
```

---

## 3. Atributos

### 3.1 Atributos de Instancia

Los atributos de instancia pertenecen a cada objeto individualmente. Se definen dentro del metodo `__init__`.

```python
class Persona:
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad

# Crear objetos
persona1 = Persona("Ana", 25)
persona2 = Persona("Carlos", 30)

print(persona1.nombre)  # Ana
print(persona2.nombre)  # Carlos
print(persona1.edad)    # 25

# Cada objeto tiene sus propios atributos
persona1.edad = 26  # Solo afecta a persona1
print(persona1.edad)  # 26
print(persona2.edad)  # 30
```

### 3.2 Atributos de Clase

Los atributos de clase son compartidos por todas las instancias de esa clase. Se definen directamente en el cuerpo de la clase.

```python
class Persona:
    # Atributo de clase (compartido por todas las instancias)
    especie = "Homo sapiens"

    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad

# Acceso al atributo de clase
print(Persona.especie)  # Homo sapiens

# Todas las instancias comparten el mismo atributo de clase
p1 = Persona("Ana", 25)
p2 = Persona("Carlos", 30)

print(p1.especie)  # Homo sapiens
print(p2.especie)  # Homo sapiens

# Si modificamos el atributo de clase, afecta a todas las instancias
Persona.especie = "Humano"
print(p1.especie)  # Humano
print(p2.especie)  # Humano
```

### 3.3 Atributos de Clase para Contadores

```python
class Contador:
    total_instancias = 0  # Atributo de clase compartido

    def __init__(self, nombre):
        self.nombre = nombre
        Contador.total_instancias += 1  # Incrementar contador

# Crear instancias
c1 = Contador("Primero")
c2 = Contador("Segundo")
c3 = Contador("Tercero")

print(f"Total instancias: {Contador.total_instancias}")  # 3
print(f"Instancia c1: {c1.nombre}, id: {c1.total_instancias}")  # 1
```

---

## 4. El Metodo __init__

El metodo `__init__` es el **constructor** de la clase. Se ejecuta automaticamente cuando se crea un nuevo objeto.

### Caracteristicas del __init__

```python
class Persona:
    def __init__(self, nombre, edad, email=None):
        # Atributos obligatorios
        self.nombre = nombre
        self.edad = edad
        # Atributo opcional con valor por defecto
        self.email = email if email else f"{nombre.lower()}@ejemplo.com"

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} anos"

# Crear objetos
p1 = Persona("Ana", 25)
p2 = Persona("Carlos", 30, "carlos@empresa.com")

print(p1.presentarse())  # Hola, soy Ana y tengo 25 anos
print(p2.presentarse())  # Hola, soy Carlos y tengo 30 anos
print(p1.email)  # ana@ejemplo.com (generado automaticamente)
print(p2.email)  # carlos@empresa.com (proporcionado)
```

### Atributos de Clase con Valor Mutable

**PELIGRO:** No usar listas o diccionarios como valores por defecto en `__init__`.

```python
# INCORRECTO - Todas las instancias comparten la misma lista
class Incorrecto:
    def __init__(self, valores=[]):  # PROBLEMA!
        self.valores = valores

# CORRECTO - Usar None y crear nueva lista
class Correcto:
    def __init__(self, valores=None):
        self.valores = valores if valores is not None else []
```

---

## 5. El Metodo __str__

El metodo `__str__` define la representacion legible del objeto para usuarios.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

p1 = Persona("Ana", 25)
print(p1)  # Persona(nombre='Ana', edad=25)
print(str(p1))  # Lo mismo
```

---

## 6. Convenciones de Nombres en Python

| Tipo | Convencion | Ejemplo |
|------|------------|---------|
| Clases | PascalCase | ` Persona`, `CalculadoraSimple` |
| Funciones/Metodos | snake_case | `calcular_total()`, `obtener_datos()` |
| Atributos | snake_case | `nombre_usuario`, `edad_maxima` |
| Constantes | UPPER_SNAKE_CASE | `MAXIMO_INTENTOS`, `TASA_POR_DEFECTO` |
| Atributos privados | underscore prefix | `_atributo_protegido` |
| Atributos muy privados | double underscore | `__atributo_privado` |

---

## 7. Ejemplo Integrador

```python
class Banco:
    # Atributo de clase
    tasa_interes = 0.05

    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    def calcular_interes(self):
        return self.saldo * self.tasa_interes

    def __str__(self):
        return f"Banco({self.nombre}, saldo=${self.saldo:.2f})"

# Uso
cuenta1 = Banco("Ana", 1000)
cuenta2 = Banco("Carlos", 500)

print(cuenta1)  # Banco(Ana, saldo=$1000.00)
cuenta1.depositar(200)
print(cuenta1)  # Banco(Ana, saldo=$1200.00)
print(f"Interes de Carlos: ${cuenta2.calcular_interes():.2f}")
```

---

**Ultima actualizacion:** 2026-02-08
