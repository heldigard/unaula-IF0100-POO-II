# Teoría - TDD y Pruebas Unitarias

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es TDD?

**Test-Driven Development (TDD)** es una práctica de desarrollo donde se escriben las pruebas ANTES del código de producción.

### Ciclo Red-Green-Refactor

```
🔴 RED   → Escribir prueba que falla
🟢 GREEN → Código mínimo para pasar
🔵 REFACTOR → Eliminar duplicación
🔁 REPEAT → Siguiente prueba
```

### Las Tres Leyes de TDD (Uncle Bob)

1. No escribirás código de producción hasta haber escrito una prueba que falle
2. No escribirás más de una prueba suficiente para fallar
3. No escribirás más código del necesario para pasar la prueba

---

## 2. pytest Framework

### Fixtures y Funciones de Prueba

| Decorador/Función | Uso |
|-------------------|-----|
| `def test_*()` | Prueba básica |
| `@pytest.fixture` | Configuración reutilizable |
| `@pytest.mark.parametrize` | Prueba parametrizada |

### Patrón AAA

```python
# test_calculadora.py
import pytest
from calculadora import Calculadora


def test_sumar_dos_numeros_retorna_suma():
    # Arrange - Configurar
    calc = Calculadora()

    # Act - Ejecutar
    resultado = calc.sumar(5, 3)

    # Assert - Verificar
    assert resultado == 8


# Versión con fixture
@pytest.fixture
def calculadora():
    return Calculadora()


def test_sumar_con_fixture(calculadora):
    # Act
    resultado = calculadora.sumar(5, 3)
    
    # Assert
    assert resultado == 8


# Versión parametrizada
@pytest.mark.parametrize("a, b, esperado", [
    (5, 3, 8),
    (10, 20, 30),
    (-1, 1, 0),
])
def test_sumar_parametrizado(calculadora, a, b, esperado):
    assert calculadora.sumar(a, b) == esperado
```

### Clase de Ejemplo

```python
# calculadora.py
class Calculadora:
    def sumar(self, a: int, b: int) -> int:
        return a + b

    def restar(self, a: int, b: int) -> int:
        return a - b

    def dividir(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
```

---

## 3. Test Doubles

| Tipo | Propósito |
|------|-----------|
| **Dummy** | Llena parámetros, sin uso |
| **Stub** | Respuestas predefinidas |
| **Fake** | Implementación simplificada |
| **Mock** | Verifica comportamiento |

### Ejemplo con Mock (unittest.mock)

```python
# test_con_mock.py
from unittest.mock import Mock, patch
import pytest


def test_enviar_notificacion():
    # Arrange
    servicio_mock = Mock()
    servicio_mock.enviar.return_value = True
    
    notificador = Notificador(servicio_mock)
    
    # Act
    resultado = notificador.notificar("Hola")
    
    # Assert
    assert resultado is True
    servicio_mock.enviar.assert_called_once_with("Hola")


# Usando patch
@patch("modulo.ServicioEmail")
def test_procesar_pedido(mock_email_class):
    mock_email = Mock()
    mock_email_class.return_value = mock_email
    
    procesador = ProcesadorPedidos()
    procesador.procesar("cliente@email.com")
    
    mock_email.enviar_confirmacion.assert_called_once()
```

---

**Última actualización:** 2026-02-01
