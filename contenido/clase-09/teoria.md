# Teoria - TDD y pytest Basico

**IF0100 - Lenguaje de Programacion OO II**

---

## TDD (Test-Driven Development)

### Ciclo TDD

```
┌─────────────────────────────────────────────────────────────┐
│                    CICLO TDD                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   1. ROJO (Red)     ───── Escribe test que falla           │
│         │                                              │      │
│         ▼                                              │      │
│   2. VERDE (Green)  ──────── Haz que pase               │      │
│         │                                              │      │
│         ▼                                              ▼      │
│   3. REFACTORIZAR  ─── Mejora codigo manteniendo tests   │
│         │                                              │      │
│         └──────────────────────────────────────────────┘      │
│                           (repetir)                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Principios TDD

| Principio | Descripcion |
|-----------|-------------|
| **First, make it work** | Primero haz que funcione, despues hazlo bien |
| **Then, make it clean** | Refactoriza manteniendo los tests |
| **Baby steps** | Pequenos pasos incrementales |
| **YAGNI** | "You Ain't Gonna Need It" - no escribas codigo innecesario |

### Reglas TDD

1. **No escribir codigo de produccion sin un test fallando**
2. **Escribir el minimo codigo para que el test pase**
3. **Refactorizar continuamente**

---

## pytest Basico

### Instalacion

```bash
pip install pytest pytest-cov
```

### Estructura de un Test

```python
# test_modulo.py
import pytest
from mi_modulo import funciones

#Funcion de test
def test_suma_dos_numeros():
    resultado = funciones.suma(2, 3)
    assert resultado == 5

def test_resta_dos_numeros():
    resultado = funciones.resta(10, 4)
    assert resultado == 6

def test_suma_negativos():
    assert funciones.suma(-1, -1) == -2

def test_suma_cero():
    assert funciones.suma(5, 0) == 5
```

### Convenciones pytest

| Elemento | Convencion |
|----------|------------|
| Archivos de test | `test_*.py` o `*_test.py` |
| Funciones de test | `test_*()` |
| Clases de test | `Test*` |
| Fijaciones | `conftest.py` |

### Assertions Basicos

```python
# Comparaciones simples
assert resultado == valor_esperado
assert resultado != valor_inexperado

# Comparaciones numericas
assert resultado == pytest.approx(3.14, rel=1e-2)
assert numero > 0
assert numero >= 0
assert numero < 100
assert numero <= 99

# Verificaciones booleanas
assert condicion
assert not condicion

# Verificaciones de pertenencia
assert elemento in lista
assert clave in diccionario
assert "subcadena" in cadena

# Verificaciones de excepciones
with pytest.raises(ZeroDivisionError):
    resultado = 10 / 0
```

### Ejecutar pytest

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con verbosidad
pytest -v

# Ejecutar test especifico
pytest test_modulo.py::test_suma_dos_numeros -v

# Ejecutar por patron
pytest -k "test_suma"

# Mostrar print statements
pytest -s

# Detener en primer fracaso
pytest -x

# Mostrar diagnosticos
pytest --tb=short
pytest --tb=long
pytest --tb=line
```

---

## Ejemplo Completo TDD

### Paso 1: Escribir el test (Rojo)

```python
# test_calculadora.py
import pytest
from calculadora import Calculadora

def test_calculadora_puede_sumar():
    calc = Calculadora()
    resultado = calc.sumar(3, 5)
    assert resultado == 8

def test_calculadora_puede_restar():
    calc = Calculadora()
    assert calc.restar(10, 4) == 6

def test_calculadora_puede_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(3, 4) == 12

def test_calculadora_puede_dividir():
    calc = Calculadora()
    assert calc.dividir(15, 3) == 5

def test_calculadora_lanza_error_al_dividir_por_cero():
    calc = Calculadora()
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10, 0)
```

### Paso 2: Hacer pasar el test (Verde)

```python
# calculadora.py
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b
```

### Paso 3: Refactorizar

```python
# calculadora.py (refactorizada)
class Calculadora:
    """Calculadora basica con operaciones aritmeticas."""

    def sumar(self, a: float, b: float) -> float:
        """Suma dos numeros."""
        return a + b

    def restar(self, a: float, b: float) -> float:
        """Resta dos numeros."""
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """Multiplica dos numeros."""
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """Divide dos numeros.

        Raises:
            ZeroDivisionError: Si el divisor es cero.
        """
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b
```

---

## Organizacion de Tests

```
proyecto/
├── src/
│   └── mi_modulo/
│       ├── __init__.py
│       └── funciones.py
├── tests/
│   ├── __init__.py
│   ├── test_funciones.py
│   ├── conftest.py
│   └── unit/
│       └── ...
├── pytest.ini
└── setup.py
```

---

**Ultima actualizacion:** 2026-02-08
