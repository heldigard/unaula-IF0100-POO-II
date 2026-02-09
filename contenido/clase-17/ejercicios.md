# Ejercicios - SQLAlchemy y Persistencia de Datos

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Definir Modelos

Completar los modelos en `src/models/`:

1. **User**: Completo (dado)
2. **Project**: Completar con relaciones
3. **Task**: Completar con relaciones
4. **Comment**: Crear desde cero

Verificar que las foreign keys apunten correctamente.

---

## Ejercicio 2: Crear Schemas Pydantic

Crear schemas para el modelo `Project`:

```python
# src/schemas/project.py
class ProjectBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None

class ProjectResponse(ProjectBase):
    id: int
    estado: str
    usuario_id: int
    creado_en: datetime

    class Config:
        from_attributes = True
```

---

## Ejercicio 3: Implementar Repository

Completar `src/repositories/task_repository.py`:

- `get_all()`
- `get_by_id()`
- `get_by_proyecto()`
- `create()`
- `update()`
- `delete()`

---

## Ejercicio 4: Relaciones y Joins

Escribir consultas que usen:

1. **Inner Join**: Obtener tareas con nombre de proyecto
2. **Left Join**: Obtener usuarios con sus proyectos
3. **Filter**: Tareas por estado y prioridad

---

## Ejercicio 5: Migraciones Alembic

Crear migracion para la tabla `tareas`:

```bash
# Generar migracion
alembic revision -m "Add tareas table"

# Aplicar migracion
alembic upgrade head
```

---

**Ultima actualizacion:** 2026-02-08
