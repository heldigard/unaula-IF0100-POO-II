# Ejercicios - FastAPI y APIs REST

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: API de Usuarios

Implementar CRUD completo para usuarios:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class UsuarioCreate(BaseModel):
    username: str
    email: str
    password: str

# Endpoints requeridos:
# - GET /usuarios (lista todos)
# - GET /usuarios/{id} (obtiene por ID)
# - POST /usuarios (crea usuario)
# - PUT /usuarios/{id} (actualiza usuario)
# - DELETE /usuarios/{id} (elimina usuario)
```

---

## Ejercicio 2: Endpoint con Filtros

Agregar filtros de query al listado de proyectos:

```python
@app.get("/proyectos")
def listar_proyectos(
    skip: int = 0,
    limit: int = 10,
    activo: Optional[bool] = None,
    nombre: Optional[str] = None
):
    """
    Lista proyectos con filtros opcionales.
    """
    # Implementar logica de filtrado
    pass
```

---

## Ejercicio 3: Validacion de Datos

Agregar validaciones con Pydantic:

```python
from pydantic import BaseModel, Field, EmailStr

class UsuarioCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_]+$"
    )
    email: EmailStr
    password: str = Field(..., min_length=8)

    @Field.validator('username')
    def username_alphanumerico(cls, v):
        if not v.isalnum():
            raise ValueError('Debe ser alfanumerico')
        return v
```

---

## Ejercicio 4: Respuestas con Codigos de Estado

Implementar endpoints con codigos HTTP apropiados:

```python
@app.post("/usuarios", status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: UsuarioCreate):
    """Retorna 201 Created al crear."""
    pass

@app.delete("/proyectos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_proyecto(id: int):
    """Retorna 204 No Content (sin cuerpo de respuesta)."""
    pass
```

---

**Ultima actualizacion:** 2026-02-08
