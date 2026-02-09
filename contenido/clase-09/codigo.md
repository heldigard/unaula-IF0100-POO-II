# Codigo - TDD y pytest Basico

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Proyecto Base TDD

### Estructura del Proyecto

```
mi_proyecto/
├── src/
│   └── calculadora/
│       ├── __init__.py
│       └── calculadora.py
├── tests/
│   ├── __init__.py
│   └── test_calculadora.py
└── pytest.ini
```

### Archivo pytest.ini

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
python_classes = Test*
addopts = -v --tb=short
```

### __init__.py de tests

```python
# tests/__init__.py
# Paquete de pruebas
```

### __init__.py de src

```python
# src/__init__.py
# Paquete fuente
```

---

## 2. Calculadora con TDD

### Paso 1: Test que Falla (Rojo)

```python
# tests/test_calculadora.py
import pytest
from src.calculadora.calculadora import Calculadora


class TestCalculadora:
    """Tests para la clase Calculadora."""

    def setup_method(self):
        """Configuracion antes de cada test."""
        self.calc = Calculadora()

    def test_suma_dos_numeros_positivos(self):
        """Test suma de numeros positivos."""
        assert self.calc.sumar(2, 3) == 5

    def test_suma_numero_y_cero(self):
        """Test suma con cero."""
        assert self.calc.sumar(10, 0) == 10

    def test_suma_numeros_negativos(self):
        """Test suma de numeros negativos."""
        assert self.calc.sumar(-5, -3) == -8

    def test_suma_positivo_y_negativo(self):
        """Test suma de positivo y negativo."""
        assert self.calc.sumar(10, -3) == 7

    def test_resta_dos_numeros(self):
        """Test resta."""
        assert self.calc.restar(10, 4) == 6

    def test_multiplicacion_dos_numeros(self):
        """Test multiplicacion."""
        assert self.calc.multiplicar(4, 5) == 20

    def test_division_dos_numeros(self):
        """Test division."""
        assert self.calc.dividir(20, 4) == 5.0

    def test_division_por_cero_lanza_error(self):
        """Test division por cero lanza excepcion."""
        with pytest.raises(ZeroDivisionError):
            self.calc.dividir(10, 0)

    def test_multiplicacion_por_uno(self):
        """Test multiplicacion por uno."""
        assert self.calc.multiplicar(100, 1) == 100

    def test_multiplicacion_por_cero(self):
        """Test multiplicacion por cero."""
        assert self.calc.multiplicar(999, 0) == 0
```

### Paso 2: Implementacion Minima (Verde)

```python
# src/calculadora/calculadora.py
class Calculadora:
    """Clase Calculadora para operaciones basicas."""

    def sumar(self, a, b):
        """Suma dos numeros."""
        return a + b

    def restar(self, a, b):
        """Resta dos numeros."""
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos numeros."""
        return a * b

    def dividir(self, a, b):
        """Divide dos numeros."""
        if b == 0:
            raise ZeroDivisionError()
        return a / b
```

### Paso 3: Implementacion Final (Refactorizado)

```python
# src/calculadora/calculadora.py
from typing import Union


class Calculadora:
    """Calculadora basica con operaciones aritmeticas.

    Attributes:
        resultado: Almacena el resultado de la ultima operacion.
    """

    def __init__(self):
        """Inicializa la calculadora con resultado cero."""
        self.resultado = 0

    def sumar(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Suma dos numeros.

        Args:
            a: Primer operando.
            b: Segundo operando.

        Returns:
            La suma de los dos operandos.
        """
        self.resultado = a + b
        return self.resultado

    def restar(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Resta dos numeros.

        Args:
            a: Minuendo.
            b: Sustraendo.

        Returns:
            La diferencia entre los dos operandos.
        """
        self.resultado = a - b
        return self.resultado

    def multiplicar(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiplica dos numeros.

        Args:
            a: Primer factor.
            b: Segundo factor.

        Returns:
            El producto de los dos factores.
        """
        self.resultado = a * b
        return self.resultado

    def dividir(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide dos numeros.

        Args:
            a: Dividendo.
            b: Divisor.

        Raises:
            ZeroDivisionError: Si el divisor es cero.

        Returns:
            El cociente de la division.
        """
        if b == 0:
            raise ZeroDivisionError(f"No se puede dividir {a} por cero")
        self.resultado = a / b
        return self.resultado

    def limpiar(self):
        """Limpia el resultado actual."""
        self.resultado = 0
```

---

## 3. Funciones de Strings con TDD

### Test para Funciones de String

```python
# tests/test_string_utils.py
import pytest
from src.string_utils.string_utils import StringUtils


class TestStringUtils:
    """Tests para funciones de strings."""

    def setup_method(self):
        """Configuracion antes de cada test."""
        self.utils = StringUtils()

    def test_contar_palabras_cadena_simple(self):
        """Test conteo de palabras basico."""
        assert self.utils.contar_palabras("Hola mundo") == 2

    def test_contar_palabras_cadena_vacia(self):
        """Test cadena vacia."""
        assert self.utils.contar_palabras("") == 0

    def test_contar_palabras_con_espacios(self):
        """Test con espacios multiples."""
        assert self.utils.contar_palabras("Hola   mundo") == 2

    def test_invertir_cadena_simple(self):
        """Test inversion de cadena."""
        assert self.utils.invertir("python") == "nohtyp"

    def test_invertir_cadena_vacia(self):
        """Test inversion de cadena vacia."""
        assert self.utils.invertir("") == ""

    def test_es_palindromo_palabra_valida(self):
        """Test palindromo valido."""
        assert self.utils.es_palindromo("radar") is True

    def test_es_palindromo_palabra_invalida(self):
        """Test palindromo invalido."""
        assert self.utils.es_palindromo("python") is False

    def test_es_palindromo_con_mayusculas(self):
        """Test palindromo insensitive case."""
        assert self.utils.es_palindromo("Radar") is True

    def test_a_mayusculas(self):
        """Test conversion a mayusculas."""
        assert self.utils.a_mayusculas("hola") == "HOLA"

    def test_a_minusculas(self):
        """Test conversion a minusculas."""
        assert self.utils.a_minusculas("HOLA") == "hola"
```

### Implementacion de StringUtils

```python
# src/string_utils/string_utils.py
class StringUtils:
    """Utilidades para manipulacion de strings."""

    def contar_palabras(self, texto: str) -> int:
        """Cuenta el numero de palabras en un texto.

        Args:
            texto: Texto a analizar.

        Returns:
            Numero de palabras.
        """
        if not texto:
            return 0
        return len(texto.split())

    def invertir(self, texto: str) -> str:
        """Invierte una cadena.

        Args:
            texto: Texto a invertir.

        Returns:
            Texto invertido.
        """
        return texto[::-1]

    def es_palindromo(self, texto: str) -> bool:
        """Verifica si un texto es palindromo.

        Args:
            texto: Texto a verificar.

        Returns:
            True si es palindromo, False en caso contrario.
        """
        texto_limpio = texto.lower().replace(" ", "")
        return texto_limpio == texto_limpio[::-1]

    def a_mayusculas(self, texto: str) -> str:
        """Convierte texto a mayusculas.

        Args:
            texto: Texto a convertir.

        Returns:
            Texto en mayusculas.
        """
        return texto.upper()

    def a_minusculas(self, texto: str) -> str:
        """Convierte texto a minusculas.

        Args:
            texto: Texto a convertir.

        Returns:
            Texto en minusculas.
        """
        return texto.lower()
```

---

## 4. Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con coverage
pytest --cov=src --cov-report=html

# Ejecutar tests de un modulo especifico
pytest tests/test_calculadora.py -v

# Ver resultado detallado
pytest -v --tb=short

# Detener en primer fallo
pytest -x
```

---

**Ultima actualizacion:** 2026-02-08
