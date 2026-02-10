# Código - BDD con Behave

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Feature de Registro con Behave

### features/registro.feature

```gherkin
Feature: Registro de Usuarios en TaskFlow
  Como usuario no registrado
  Quiero poder crear una cuenta
  Para poder usar TaskFlow

  Background:
    Given el sistema está configurado
    And la página de registro está accesible

  Scenario: Registro exitoso con datos válidos
    Given estoy en la página de registro
    When completo el formulario con:
      | campo           | valor            |
      | username        | newuser          |
      | email           | new@example.com  |
      | password        | pass123          |
      | confirm_password| pass123          |
    And hago clic en "Registrarse"
    Then veo "Registro exitoso"
    And soy redirigido al login

  Scenario: Registro falla con password corto
    Given estoy en la página de registro
    When completo el formulario con:
      | campo           | valor            |
      | username        | newuser         |
      | email           | new@example.com |
      | password        | abc             |
      | confirm_password| abc             |
    And hago clic en "Registrarse"
    Then veo "Password muy corto"
    And permanezco en la página de registro
```

---

## 2. Steps para Registro

### features/steps/registro_steps.py

```python
# features/steps/registro_steps.py

from behave import given, when, then


@given('estoy en la página de registro')
def step_pagina_registro(context):
    """Navega a la página de registro."""
    context.response = context.client.get('/registro')
    assert context.response.status_code == 200


@when('completo el formulario con:')
def step_completar_formulario(context):
    """Completa el formulario con los datos de la tabla."""
    tabla = context.table
    context.datos_form = {row['campo']: row['valor'] for row in tabla}


@when('hago clic en "{boton}"')
def step_hacer_clic(context, boton):
    """Envía el formulario."""
    context.response = context.client.post('/registro', json=context.datos_form)


@then('veo "{mensaje}"')
def step_ver_mensaje(context, mensaje):
    """Verifica que el mensaje esté en la respuesta."""
    assert mensaje in context.response.json()['mensaje']


@then('soy redirigido al login')
def step_redirigido_login(context):
    """Verifica redirección."""
    assert context.response.status_code == 302
    assert '/login' in context.response.headers['Location']


@then('permanezco en la página de registro')
def step_permanecer_registro(context):
    """Verifica que NO hubo redirección."""
    assert context.response.status_code == 200
```

---

## 3. Feature de Gestión de Tareas

### features/tareas.feature

```gherkin
Feature: Gestión de Tareas
  Como usuario de TaskFlow
  Quiero poder crear y gestionar tareas
  Para organizar mi trabajo

  Scenario: Crear tarea en proyecto existente
    Given soy usuario autenticado como "juan"
    And tengo un proyecto llamado "Mi Proyecto"
    When creo una tarea con:
      | campo      | valor               |
      | titulo     | Implementar login   |
      | descripcion| Crear endpoint POST |
      | prioridad  | alta                |
    Then la tarea se crea exitosamente
    And aparece en la lista de tareas del proyecto

  Scenario: Marcar tarea como completada
    Given soy usuario autenticado como "juan"
    And tengo una tarea "Implementar login" en estado "pendiente"
    When marco la tarea como completada
    Then la tarea cambia a estado "completada"
    And la fecha de completado se registra
```

---

## 4. Environment para behave

### features/environment.py

```python
# features/environment.py

from behave import fixture


@fixture
def browser(context):
    """Fixture que inicializa el navegador para UI tests."""
    from selenium import webdriver
    context.browser = webdriver.Chrome()
    yield context.browser
    context.browser.quit()


@fixture
def client(context):
    """Fixture que inicializa el cliente de API."""
    from fastapi.testclient import TestClient
    from taskflow.api.app import app
    context.client = TestClient(app)
    yield context.client
```

---

## 5. Tests BDD Completos

### tests/test_bdd/conftest.py

```python
# tests/test_bdd/conftest.py

import pytest
from pytest_bdd import pytest_genhook


def pytest_configure(config):
    """Configurar paths para behave."""
    pytest_genhook.pytest_configure(config)
    config.addinivalue_line(
        "markers", "scenario: mark test as scenario"
    )


@pytest.fixture
def app():
    """Fixture de la aplicación FastAPI."""
    from taskflow.api.app import app
    return app


@pytest.fixture
def client(app):
    """Cliente de test."""
    from fastapi.testclient import TestClient
    return TestClient(app)
```

---

**Última actualización:** 2026-02-08
