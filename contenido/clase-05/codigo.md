# Codigo - Clases, Objetos y Atributos

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Primera Clase Completa

### Estructura basica de una clase

```python
# persona.py
class Persona:
    """Clase que representa una persona"""

    def __init__(self, nombre: str, edad: int, email: str = None):
        self.nombre = nombre
        self.edad = edad
        self.email = email if email else f"{nombre.lower()}@ejemplo.com"

    def saludar(self) -> str:
        """Retorna un saludo"""
        return f"Hola, soy {self.nombre}"

    def cumplir_anios(self):
        """Incrementa la edad en 1"""
        self.edad += 1

    def __str__(self) -> str:
        return f"Persona({self.nombre}, {self.edad} anos)"


# main.py
from persona import Persona

# Crear instancias
p1 = Persona("Ana Garcia", 25)
p2 = Persona("Carlos Lopez", 30)

# Usar metodos
print(p1.saludar())  # Hola, soy Ana Garcia
p1.cumplir_anios()
print(f"{p1.nombre} ahora tiene {p1.edad} anos")
print(p1)  # Persona(Ana Garcia, 26 anos)
```

---

## 2. Clase con Atributos de Clase

```python
# banco.py
class CuentaBancaria:
    # Atributos de clase (compartidos por todas las instancias)
    banco = "Banco Central"
    tasa_interes = 0.04
    total_cuentas = 0

    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo
        CuentaBancaria.total_cuentas += 1
        self.numero_cuenta = CuentaBancaria.total_cuentas

    def depositar(self, monto: float) -> bool:
        """Deposita dinero en la cuenta"""
        if monto > 0:
            self.saldo += monto
            return True
        return False

    def retirar(self, monto: float) -> bool:
        """Retira dinero de la cuenta si hay saldo suficiente"""
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    def aplicar_interes(self):
        """Aplica interes al saldo actual"""
        self.saldo *= (1 + self.tasa_interes)

    def __str__(self) -> str:
        return f"Cuenta #{self.numero_cuenta} - {self.titular}: ${self.saldo:.2f}"


# main.py
from banco import CuentaBancaria

# Crear cuentas
cuenta1 = CuentaBancaria("Ana Garcia", 1000)
cuenta2 = CuentaBancaria("Carlos Lopez", 500)

print(cuenta1)  # Cuenta #1 - Ana Garcia: $1000.00
print(cuenta2)  # Cuenta #2 - Carlos Lopez: $500.00
print(f"Total cuentas: {CuentaBancaria.total_cuentas}")  # 2
print(f"Banco: {cuenta1.banco}")  # Banco Central

# Operaciones
cuenta1.depositar(200)
cuenta1.aplicar_interes()
print(cuenta1)  # Saldo con interes aplicado
```

---

## 3. Clase Producto con Validacion

```python
# producto.py
class Producto:
    # Atributos de clase
    iva = 0.19
    productos_creados = 0

    def __init__(self, nombre: str, precio: float, categoria: str):
        self.codigo = Producto.productos_creados + 1
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        Producto.productos_creados += 1

    def precio_con_iva(self) -> float:
        """Retorna el precio con IVA incluido"""
        return self.precio * (1 + self.iva)

    def aplicar_descuento(self, porcentaje: float) -> bool:
        """Aplica un descuento al producto"""
        if 0 < porcentaje <= 100:
            self.precio *= (1 - porcentaje / 100)
            return True
        return False

    def __str__(self) -> str:
        return f"[{self.codigo}] {self.nombre} (${self.precio:.2f})"


# main.py
from producto import Producto

# Crear productos
p1 = Producto("Laptop", 1500000, "Electronica")
p2 = Producto("Mouse", 25000, "Electronica")
p3 = Producto("Libro", 45000, "Educacion")

print(p1)  # [1] Laptop ($1500000.00)
print(f"Con IVA: ${p1.precio_con_iva():.2f}")  # Con IVA: $1785000.00

p2.aplicar_descuento(10)
print(p2)  # [10% descuento aplicado]
print(f"Total productos: {Producto.productos_creados}")
```

---

## 4. Clase Estudiante

```python
# estudiante.py
class Estudiante:
    universidad = "Universidad UNAULA"
    estudiantes_activos = 0

    def __init__(self, nombre: str, codigo: str, carrera: str):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.materias = []
        self.notas = {}
        Estudiante.estudiantes_activos += 1

    def matricular(self, materia: str):
        """Matricula al estudiante en una materia"""
        if materia not in self.materias:
            self.materias.append(materia)
            self.notas[materia] = None

    def asignar_nota(self, materia: str, nota: float):
        """Asigna una nota a una materia"""
        if materia in self.materias and 0 <= nota <= 5.0:
            self.notas[materia] = nota

    def promedio(self) -> float:
        """Calcula el promedio de notas"""
        notas_validas = [n for n in self.notas.values() if n is not None]
        if not notas_validas:
            return 0
        return sum(notas_validas) / len(notas_validas)

    def ha_aprobado(self, materia: str) -> bool:
        """Verifica si aprobo una materia"""
        return self.notas.get(materia, 0) >= 3.0

    def __str__(self) -> str:
        return f"{self.nombre} ({self.codigo}) - {self.carrera}"


# main.py
from estudiante import Estudiante

# Crear estudiante
e1 = Estudiante("Ana Garcia", "20241001", "Ingenieria de Sistemas")

# Matricular en materias
e1.matricular("POO II")
e1.matricular("Bases de Datos")
e1.matricular("Algoritmos")

# Asignar notas
e1.asignar_nota("POO II", 4.5)
e1.asignar_nota("Bases de Datos", 3.8)
e1.asignar_nota("Algoritmos", 2.5)

print(e1)
print(f"Promedio: {e1.promedio():.2f}")
print(f"POO II aprobado: {e1.ha_aprobado('POO II')}")  # True
print(f"Algoritmos aprobado: {e1.ha_aprobado('Algoritmos')}")  # False
```

---

## 5. Sistema de Inventario

```python
# inventario.py
class Inventario:
    producto_creado = 0

    def __init__(self, nombre_tienda: str):
        self.nombre = nombre_tienda
        self.productos = {}
        Inventario.producto_creado = 0

    def agregar_producto(self, nombre: str, precio: float, cantidad: int):
        """Agrega un producto al inventario"""
        codigo = len(self.productos) + 1
        self.productos[codigo] = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        return codigo

    def actualizar_stock(self, codigo: int, cantidad: int):
        """Actualiza la cantidad de un producto"""
        if codigo in self.productos:
            self.productos[codigo]["cantidad"] += cantidad
            return True
        return False

    def valor_total_inventario(self) -> float:
        """Calcula el valor total del inventario"""
        total = 0
        for producto in self.productos.values():
            total += producto["precio"] * producto["cantidad"]
        return total

    def buscar_producto(self, nombre: str):
        """Busca productos por nombre"""
        resultados = []
        for codigo, producto in self.productos.items():
            if nombre.lower() in producto["nombre"].lower():
                resultados.append((codigo, producto["nombre"]))
        return resultados

    def __str__(self) -> str:
        return f"Inventario: {self.nombre} ({len(self.productos)} productos)"


# main.py
from inventario import Inventario

# Crear inventario
tienda = Inventario("Tecnologia Plus")

# Agregar productos
tienda.agregar_producto("Laptop", 1500000, 5)
tienda.agregar_producto("Mouse", 25000, 20)
tienda.agregar_producto("Teclado", 45000, 15)

print(tienda)
print(f"Valor total: ${tienda.valor_total_inventario():,.0f}")

tienda.actualizar_stock(1, -1)  # Vender una laptop
resultados = tienda.buscar_producto("mouse")
print(f"Buscar 'mouse': {resultados}")
```

---

**Ultima actualizacion:** 2026-02-08
