# Teoría - BDD y Behave

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es BDD?

**Behavior Driven Development (BDD)** evoluciona TDD enfocándose en **comportamiento** del sistema desde la perspectiva del usuario.

### Gherkin: Given-When-Then

```gherkin
Feature: Calculadora
  Scenario: Sumar dos números
    Given tengo una calculadora
    When ingreso 5 y 3
    Then el resultado debe ser 8
```

### Componentes

| Palabra Clave | Propósito |
|---------------|-----------|
| **Feature** | Historia de usuario |
| **Scenario** | Caso específico |
| **Given** | Contexto inicial |
| **When** | Acción |
| **Then** | Resultado esperado |
| **And** | Adicionales |

---

## 2. Behave en Python

### Instalación

```bash
pip install behave
```

### Estructura del Proyecto

```
features/
├── calculadora.feature      # Archivos Gherkin
├── steps/
│   └── calculadora_steps.py # Step definitions
└── environment.py           # Configuración inicial
```

### Ejemplo Completo

**Archivo: `features/calculadora.feature`**

```gherkin
Feature: Calculadora
  Como usuario
  Quiero realizar operaciones matemáticas
  Para facilitar mis cálculos

  Scenario: Sumar dos números
    Given tengo una calculadora
    When ingreso 5 y 3
    Then el resultado debe ser 8

  Scenario Outline: Sumar múltiples valores
    Given tengo una calculadora
    When ingreso <numero1> y <numero2>
    Then el resultado debe ser <resultado>

    Examples:
      | numero1 | numero2 | resultado |
      | 5       | 3       | 8         |
      | 10      | 20      | 30        |
      | -1      | 1       | 0         |
```

### Step Definitions

**Archivo: `features/steps/calculadora_steps.py`**

```python
from behave import given, when, then
from calculadora import Calculadora


@given('tengo una calculadora')
def step_tengo_calculadora(context):
    context.calculadora = Calculadora()


@when('ingreso {num1:d} y {num2:d}')
def step_ingreso_numeros(context, num1, num2):
    context.resultado = context.calculadora.sumar(num1, num2)


@then('el resultado debe ser {esperado:d}')
def step_verificar_resultado(context, esperado):
    assert context.resultado == esperado, \
        f"Esperado {esperado}, pero obtuve {context.resultado}"
```

### Ejemplo: Autenticación

**Archivo: `features/autenticacion.feature`**

```gherkin
Feature: Autenticación
  Como usuario
  Quiero iniciar sesión
  Para acceder al sistema

  Scenario: Login exitoso
    Given un usuario registrado con email "test@email.com" y clave "123456"
    When ingreso las credenciales correctas
    Then debo ser redirigido al dashboard
    And debo ver un mensaje de bienvenida
```

**Archivo: `features/steps/autenticacion_steps.py`**

```python
from behave import given, when, then
from servicios.autenticacion import AutenticacionService
from modelos.usuario import Usuario


@given('un usuario registrado con email "{email}" y clave "{clave}"')
def step_usuario_registrado(context, email, clave):
    context.usuario = Usuario(email=email, clave=clave)


@when('ingreso las credenciales correctas')
def step_ingreso_credenciales(context):
    servicio = AutenticacionService()
    context.resultado = servicio.login(
        context.usuario.email, 
        context.usuario.clave
    )


@then('debo ser redirigido al dashboard')
def step_redirigido_dashboard(context):
    assert context.resultado.redirect_url == "/dashboard", \
        f"URL esperada /dashboard, obtenida {context.resultado.redirect_url}"


@then('debo ver un mensaje de bienvenida')
def step_mensaje_bienvenida(context):
    assert "bienvenida" in context.resultado.mensaje.lower(), \
        "Mensaje de bienvenida no encontrado"
```

### Configuración con environment.py

```python
# features/environment.py

def before_all(context):
    """Ejecutado antes de todas las pruebas"""
    context.configuracion = {
        "base_url": "http://localhost:5000",
        "entorno": "pruebas"
    }


def before_scenario(context, scenario):
    """Ejecutado antes de cada escenario"""
    context.datos = {}


def after_scenario(context, scenario):
    """Ejecutado después de cada escenario"""
    if hasattr(context, 'db'):
        context.db.rollback()
```

---

## 3. Ejecutar Pruebas Behave

```bash
# Ejecutar todas las features
behave

# Ejecutar feature específica
behave features/calculadora.feature

# Ejecutar con formato detallado
behave --format=pretty

# Ejecutar escenarios específicos por tag
behave --tags=regression

# Generar reporte JSON
behave --format=json --outfile=resultados.json
```

---

**Última actualización:** 2026-02-01
