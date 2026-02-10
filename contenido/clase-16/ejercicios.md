# Ejercicios - Testing en APIs con pytest y httpx

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Test de Unidad

Escribir tests unitarios para el modelo `User`:

1. Crear archivo `tests/test_models.py`
2. Testear creacion de instancias
3. Testear validaciones de esquema
4. Verificar atributos por defecto

---

## Ejercicio 2: Tests CRUD Completos

Completar `tests/test_users.py` con:

```python
# Tests requeridos:
# - test_create_user
# - test_get_users_list
# - test_get_user_by_id
# - test_update_user
# - test_delete_user
# - test_create_duplicate_email
# - test_get_nonexistent_user
```

---

## Ejercicio 3: Tests de Proyectos

Crear archivo `tests/test_projects.py` con:

- Test de creacion de proyecto
- Test de lista de proyectos
- Test de proyecto no encontrado
- Test de actualizacion de proyecto

---

## Ejercicio 4: Tests Parametrizados

Crear tests parametizados para:

1. Validacion de email
2. Parametros de paginacion
3. Estados validos de tarea

---

## Ejercicio 5: Coverage > 80%

Objetivo: Alcanzar 80% de coverage:

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

Identificar codigo sin testear y agregar tests.

---

**Ultima actualizacion:** 2026-02-08
