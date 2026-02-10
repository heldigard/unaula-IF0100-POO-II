# Evaluación 2 - IF0100: Técnicas de Desarrollo de Software

**Curso:** IF0100 - Lenguaje de Programación OO II
**Tipo:** Examen práctico + Taller (en parejas)
**Porcentaje:** 15%
**Fecha:** 2026-03-12 (Jueves)
**Duración:** 1 hora (examen) + taller en casa
**Modalidad:** Mixta

---

## 🎯 Objetivo

Evaluar la comprensión y aplicación de técnicas modernas de desarrollo: Test Driven Development (TDD), Behavior Driven Development (BDD) y Domain Driven Design (DDD).

---

## 📝 Parte A: Examen en Clase (40 pts)

### Sección 1: Preguntas Conceptuales (20 pts)

1. **(5 pts)** Explique el ciclo Red-Green-Refactor de TDD y por qué es importante seguir este orden.

2. **(5 pts)** ¿Cuál es la diferencia principal entre TDD y BDD? ¿Cuándo usaría cada uno?

3. **(5 pts)** En DDD, explique qué son: Entity, Value Object, Aggregate y Repository.

4. **(5 pts)** ¿Qué es un test double (mock, stub, fake)? Proporcione un ejemplo de uso.

### Sección 2: Análisis de Código (20 pts)

Dado el siguiente código, identifique:

```python
import pytest
from unittest.mock import Mock, MagicMock

def test_calculadora_sumar_dos_numeros_retorna_suma():
    # Arrange
    calculadora = Calculadora()

    # Act
    resultado = calculadora.sumar(3, 5)

    # Assert
    assert resultado == 8
```

1. **(5 pts)** ¿Qué patrón de pruebas se está usando? Explique cada sección.

2. **(5 pts)** Escriba una prueba que falle primero (Red) para un método `dividir(a, b)` que lance excepción si b = 0.

3. **(5 pts)** Convierta esta prueba a estilo BDD con behave (Given-When-Then).

4. **(5 pts)** ¿Cómo haría mock de una dependencia de base de datos en esta calculadora?

---

## 💻 Parte B: Taller Práctico (60 pts)

**Trabajo en parejas - Entrega: 2026-03-14 (Sábado)**

### Proyecto: Sistema de Carrito de Compras con TDD

Desarrollar un sistema de carrito de compras siguiendo estrictamente TDD.

#### Requisitos Funcionales:

1. **Agregar productos al carrito**
2. **Eliminar productos del carrito**
3. **Calcular subtotal**
4. **Aplicar descuentos** (porcentaje o monto fijo)
5. **Calcular impuesto** (IVA 19%)
6. **Calcular total final**

#### Estructura del Proyecto:

```
carrito_compras/
├── src/
│   ├── core/
│   │   ├── entities/
│   │   │   ├── producto.py
│   │   │   ├── item_carrito.py
│   │   │   └── carrito.py
│   │   ├── services/
│   │   │   ├── calculador_precio.py
│   │   │   └── __init__.py
│   │   └── value_objects/
│   │       └── dinero.py
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_carrito.py
│   ├── test_calculador_precio.py
│   └── test_producto.py
└── pyproject.toml
```

#### Requisitos de Implementación:

**1. Pruebas Unitarias (25 pts)**

Escribir al menos 10 pruebas unitarias que cubran:

```python
import pytest
from src.core.entities.carrito import Carrito
from src.core.entities.producto import Producto
from src.core.value_objects.dinero import Dinero

class TestCarrito:
    def test_agregar_producto_carrito_vacio_tiene_un_item(self):
        """Test: agregar producto a carrito vacío"""
        pass

    def test_agregar_producto_mismo_producto_incrementa_cantidad(self):
        """Test: agregar mismo producto varias veces"""
        pass

    def test_eliminar_producto_producto_existe_se_elimina(self):
        """Test: eliminar producto existente"""
        pass

    def test_calcular_subtotal_varios_productos_suma_correcta(self):
        """Test: calcular subtotal con múltiples productos"""
        pass

    def test_aplicar_descuento_porcentaje_calcula_correcto(self):
        """Test: aplicar descuento porcentual"""
        pass

    # ... más pruebas
```

**2. Aplicación de DDD (15 pts)**

- Usar Value Objects para dinero (evitar problemas de decimales)
- Definir Aggregates correctamente
- Separar lógica de dominio de infraestructura

**3. Cobertura de Código (10 pts)**

- Mínimo 80% de cobertura
- Incluir reporte de cobertura en la entrega
- Usar `pytest-cov`

```bash
# Generar reporte de cobertura
pytest --cov=src --cov-report=html
```

**4. Documentación (10 pts)**

- README con instrucciones de ejecución
- type hints en todos los métodos
- docstrings en español
- Explicación de decisiones de diseño

---

## 📤 Entrega del Taller

1. **Repositorio Git** con commits que muestren el proceso TDD
2. **ZIP con:**
   - Código fuente completo
   - Reporte de cobertura (htmlcov/)
   - Documento PDF con:
     - Nombres de integrantes
     - Explicación del proceso TDD seguido
     - Capturas de pruebas pasando
     - Reflexión sobre dificultades encontradas

---

## 📏 Rúbrica

| Criterio | Excelente | Bueno | Regular | Insuficiente |
|----------|-----------|-------|---------|--------------|
| **Examen (40%)** | Todas correctas | 80% correctas | 60% correctas | <60% |
| **TDD aplicado** | Commits muestran Red-Green-Refactor | Mayoría TDD | Pruebas después | Sin TDD |
| **Cobertura** | >90% | 80-90% | 70-80% | <70% |
| **DDD** | Bien aplicado | Parcialmente | Básico | No aplica |
| **Documentación** | Completa | Buena | Básica | Falta |

---

## 💡 Recursos

- pytest: https://docs.pytest.org/
- pytest-mock: https://github.com/pytest-dev/pytest-mock
- pytest-cov: https://github.com/pytest-dev/pytest-cov
- behave (BDD): https://behave.readthedocs.io/
- SQLAlchemy (persistencia): https://docs.sqlalchemy.org/

---

**Examen:** Jueves 12 de marzo, 06:00-07:00 AM
**Taller:** Entrega sábado 14 de marzo, 23:59
**UNAULA - POO II - 2026-I**
