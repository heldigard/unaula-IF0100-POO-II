# Ejercicios - Dependencias e Inyeccion de Dependencias

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Dependency Basica

Crear un sistema de dependencias para TaskFlow:

1. Crear archivo `src/db/dependencies.py`
2. Definir dependencia `get_db()` que yield una sesion
3. Verificar que la sesion se cierra automaticamente

```python
# Estructura esperada
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## Ejercicio 2: Service Factory

Implementar un factory de dependencias para los servicios:

1. Crear dependencia `get_project_service(db)`
2. Crear dependencia `get_task_service(db)`
3. Usar `Annotated` para integrar con Depends

---

## Ejercicio 3: Pagination Dependency

Crear dependencia de paginacion reutilizable:

```python
class PaginationParams:
    def __init__(self, skip: int = 0, limit: int = 100):
        self.skip = skip
        self.limit = limit
```

Usarla en al menos 2 endpoints diferentes.

---

## Ejercicio 4: Dependency Overrides

Configurar overrides para testing:

```python
# En test conftest.py
def override_get_db():
    # Return test database session

app.dependency_overrides[get_db] = override_get_db
```

---

**Ultima actualizacion:** 2026-02-08
