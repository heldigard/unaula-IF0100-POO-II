# Codigo - FastAPI y APIs REST

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Primera Aplicacion FastAPI

```python
# main.py
from fastapi import FastAPI

app = FastAPI(
    title="TaskFlow API",
    description="API del sistema de gestion de tareas",
    version="0.1.0"
)

@app.get("/")
def read_root():
    """Endpoint raiz de la API."""
    return {
        "mensaje": "Bienvenido a TaskFlow API",
        "version": "0.1.0",
        "documentacion": "/docs"
    }

@app.get("/api/hola-mundo")
def hola_mundo():
    """Endpoint simple que retorna un saludo."""
    return {
        "mensaje": "Hola, Mundo!",
        "api": "TaskFlow API",
        "status": "funcionando"
    }
```

### Ejecutar el Servidor

```bash
uvicorn main:app --reload
```

---

## 2. CRUD Basico de Proyectos

```python
# main.py
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="TaskFlow API")

# Modelos Pydantic
class ProyectoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class ProyectoCreate(ProyectoBase):
    pass

class ProyectoResponse(ProyectoBase):
    id: int
    activo: bool = True

# Base de datos simulada
db_proyectos = []
next_id = 1

# GET - Listar proyectos
@app.get("/proyectos", response_model=List[ProyectoResponse])
def listar_proyectos(skip: int = 0, limit: int = 10):
    """Lista proyectos con paginacion."""
    return db_proyectos[skip : skip + limit]

# GET - Obtener por ID
@app.get("/proyectos/{proyecto_id}", response_model=ProyectoResponse)
def obtener_proyecto(proyecto_id: int):
    """Obtiene un proyecto por su ID."""
    for proyecto in db_proyectos:
        if proyecto["id"] == proyecto_id:
            return proyecto
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

# POST - Crear proyecto
@app.post("/proyectos", response_model=ProyectoResponse, status_code=201)
def crear_proyecto(proyecto: ProyectoCreate):
    """Crea un nuevo proyecto."""
    global next_id
    nuevo_proyecto = {
        "id": next_id,
        **proyecto.model_dump(),
        "activo": True
    }
    db_proyectos.append(nuevo_proyecto)
    next_id += 1
    return nuevo_proyecto

# PUT - Actualizar proyecto
@app.put("/proyectos/{proyecto_id}", response_model=ProyectoResponse)
def actualizar_proyecto(proyecto_id: int, proyecto_update: ProyectoBase):
    """Actualiza un proyecto existente."""
    for i, proyecto in enumerate(db_proyectos):
        if proyecto["id"] == proyecto_id:
            db_proyectos[i] = {
                **proyecto,
                **proyecto_update.model_dump()
            }
            return db_proyectos[i]
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

# DELETE - Eliminar proyecto
@app.delete("/proyectos/{proyecto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_proyecto(proyecto_id: int):
    """Elimina un proyecto."""
    for i, proyecto in enumerate(db_proyectos):
        if proyecto["id"] == proyecto_id:
            db_proyectos.pop(i)
            return None
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")
```

---

## 3. Organizacion con Routers

```python
# routers/proyectos.py
from fastapi import APIRouter

router = APIRouter(
    prefix="/proyectos",
    tags=["proyectos"]
)

@router.get("/")
def listar_proyectos():
    return []

@router.post("/")
def crear_proyecto():
    return {"mensaje": "Proyecto creado"}

# main.py
from fastapi import FastAPI
from routers import proyectos

app = FastAPI()
app.include_router(proyectos.router)
```

---

## 4. Manejo de Errores

```python
from fastapi import HTTPException, status

@app.get("/proyectos/{proyecto_id}")
def obtener_proyecto(proyecto_id: int):
    """Obtiene un proyecto con manejo de errores."""
    proyecto = buscar_proyecto(proyecto_id)

    if not proyecto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "Proyecto no encontrado",
                "proyecto_id": proyecto_id
            },
            headers={"X-Error": "Proyecto no existe"}
        )

    return proyecto
```

---

## 5. Estructura de Proyecto Recomendada

```
taskflow-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicacion FastAPI
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── proyectos.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── proyecto.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── proyecto.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   └── db/
│       ├── __init__.py
│       └── database.py
├── tests/
├── requirements.txt
└── README.md
```

---

**Ultima actualizacion:** 2026-02-08
