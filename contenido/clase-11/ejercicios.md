# Ejercicios - BDD con Behave

**IF0100 - Lenguaje de Programación OO II**

---

## Ejercicio 1: Feature de Login

Crear un escenario BDD completo para el flujo de login en TaskFlow.

### Instrucciones

1. **Crear estructura de directorios:**
   ```bash
   mkdir -p features/steps
   touch features/__init__.py
   touch features/steps/__init__.py
   ```

2. **Escribir el feature** (`features/login.feature`):
   ```gherkin
   Feature: Login de Usuarios en TaskFlow
     Como usuario registrado
     Quiero poder iniciar sesión
     Para acceder a mis proyectos y tareas

     Scenario: Login exitoso
       Given un usuario registrado con username "testuser" y password "pass123"
       When ingresa username "testuser" y password "pass123"
       Then el login es exitoso
       And recibe un token de autenticación

     Scenario: Login fallido con password incorrecto
       Given un usuario registrado con username "testuser" y password "pass123"
       When ingresa username "testuser" y password "incorrecto"
       Then el login falla
       And ve el error "Credenciales inválidas"
   ```

3. **Implementar los steps** (`features/steps/login_steps.py`).

4. **Ejecutar:**
   ```bash
   behave features/login.feature
   ```

---

## Ejercicio 2: Scenario Outline

Crear un Scenario Outline para validar el registro de usuarios.

```gherkin
Scenario Outline: Validación de registro de usuario
  Given un usuario con email "<email>"
  When intenta registrarse con username "<username>" y password "<password>"
  Then el sistema responde "<resultado>"

  Examples:
    | email             | username | password | resultado           |
    | user@example.com  | valid    | pass123  | Registro exitoso     |
    | invalid           | user     | pass123  | Email no válido     |
    | user@example.com  |          | pass123  | Username requerido  |
    | user@example.com  | user     | 123      | Password muy corto  |
```

---

## Ejercicio 3: Feature de Tareas

Crear un feature completo para gestión de tareas.

### Requirements

- Crear tarea con título, descripción y prioridad
- Marcar tarea como completada
- Listar tareas por proyecto
- Verificar que no se puedan agregar tareas a proyectos completados

---

## Ejercicio 4: Integración con pytest-bdd

Convertir los escenarios behave a pytest-bdd.

### Pasos

1. Crear `tests/test_bdd/test_login.py`
2. Definir el scenario decorator
3. Implementar los steps como funciones pytest

---

**Última actualización:** 2026-02-08
