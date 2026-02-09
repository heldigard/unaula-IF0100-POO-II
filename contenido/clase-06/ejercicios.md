# Ejercicios - Metodos y Encapsulamiento

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Clase con Propiedades

Crear una clase `Rectangulo` con:
- Atributos privados `_ancho`, `_alto`
- Propiedades `ancho`, `alto` con validacion (valores positivos)
- Propiedad calculada `area`
- Metodo magico `__str__`

**Plantilla:**
```python
class Rectangulo:
    def __init__(self, ancho, alto):
        # Completar con propiedades

    @property
    def ancho(self):
        # Completar

    @ancho.setter
    def ancho(self, valor):
        # Completar con validacion

    @property
    def area(self):
        # Completar
```

---

## Ejercicio 2: Clase con Metodos de Clase

Crear una clase `Tienda` que:
- Tenga un atributo de clase `ventas_totales`
- Use `@classmethod` para registrar ventas
- Use `@staticmethod` para calcular impuestos

```python
class Tienda:
    iva = 0.19
    ventas_totales = 0

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def registrar_venta(cls, monto):
        # Completar

    @staticmethod
    def calcular_precio_con_iva(precio):
        # Completar
```

---

## Ejercicio 3: Metodos Magicos

Crear una clase `Fraccion` que soporte operaciones aritmeticas:

| Operacion | Metodo Magico |
|-----------|---------------|
| `f1 + f2` | `__add__` |
| `f1 - f2` | `__sub__` |
| `f1 * f2` | `__mul__` |
| `f1 / f2` | `__truediv__` |
| `f1 == f2` | `__eq__` |

**Requisitos:**
- Simplificar fracciones automaticamente
- Validar division por cero

---

## Ejercicio 4: Sistema de Cuenta Bancaria

Crear una clase `CuentaBancaria` con encapsulamiento completo:

| Atributo | Tipo | Visibilidad |
|----------|------|-------------|
| `titular` | str | public |
| `_saldo` | float | protegido |
| `_numero_cuenta` | str | privado |

| Metodo | Descripcion |
|--------|-------------|
| `depositar(monto)` | Valida monto positivo |
| `retirar(monto)` | Valida saldo suficiente |
| `get_saldo()` | Getter |
| `__str__()` | Representacion |

---

## Ejercicio 5: Coleccion Personalizada (Opcional)

Crear una clase `Coleccion` con:

| Metodo Magico | Comportamiento |
|---------------|----------------|
| `__len__` | Cantidad de elementos |
| `__getitem__` | Acceso por indice |
| `__setitem__` | Modificacion por indice |
| `__contains__` | `item in coleccion` |
| `__add__` | `col1 + col2` concatenar |
| `__iter__` | Iterar sobre elementos |

---

**Ultima actualizacion:** 2026-02-08
