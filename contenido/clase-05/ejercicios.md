# Ejercicios - Clases, Objetos y Atributos

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Clase Persona Basica

Crear una clase `Persona` con:
- Atributos: nombre, edad, email
- Metodo `presentarse()` que retorne una cadena con la informacion
- Metodo `cumplir_anios()` que incremente la edad

**Plantilla:**
```python
class Persona:
    def __init__(self, nombre, edad, email=None):
        # Completar

    def presentarse(self):
        # Completar

    def cumplir_anios(self):
        # Completar

# Prueba
p = Persona("Maria", 30)
print(p.presentarse())
p.cumplir_anios()
print(f"Ahora tiene {p.edad} anos")
```

---

## Ejercicio 2: Clase Banco

Crear una clase `CuentaBancaria` con:
- Atributos de clase: `banco`, `tasa_interes`
- Atributos de instancia: `titular`, `saldo`, `numero_cuenta`
- Metodos: `depositar()`, `retirar()`, `aplicar_interes()`

**Requisitos:**
- No permitir depositos negativos
- No permitir retiros mayores al saldo
- Contador de cuentas creadas

---

## Ejercicio 3: Inventario de Tienda

Crear una clase `Inventario` para gestionar productos:

| Metodo | Descripcion |
|--------|-------------|
| `agregar_producto(nombre, precio, cantidad)` | Agrega producto nuevo |
| `actualizar_stock(codigo, cantidad)` | Modifica stock |
| `valor_total()` | Calcula valor del inventario |
| `buscar_producto(nombre)` | Busca por nombre parcial |

| Atributo | Descripcion |
|----------|-------------|
| `nombre_tienda` | Nombre del establecimiento |
| `productos` | Diccionario con codigo -> datos |

---

## Ejercicio 4: Sistema de Empleados

Crear un sistema con:

```python
class Empleado:
    # Atributos de clase
    empresa = "TechCorp"
    empleados_totales = 0

    def __init__(self, nombre, cargo, salario):
        # Completar

    def aumentar_salario(self, porcentaje):
        # Completar (validar 0-100%)

    def __str__(self):
        # Completar
```

**Puntos extra:**
- Contador de empleados por cargo
- Verificar que el salario no baje del minimo

---

## Ejercicio 5: Carrito de Compras (Opcional)

Crear un `Carrito` con productos:

| Metodo | Descripcion |
|--------|-------------|
| `agregar_producto(producto, cantidad)` | Agrega item |
| `eliminar_producto(codigo)` | Remueve item |
| `calcular_total()` | Suma precios |
| `vaciar()` | Limpia el carrito |

| Atributo | Descripcion |
|----------|-------------|
| `items` | Diccionario producto -> cantidad |

---

**Ultima actualizacion:** 2026-02-08
