# Teoria - FastAPI y APIs REST

**IF0100 - Lenguaje de Programacion OO II**

---

## ¿Que es FastAPI?

**FastAPI** es un framework web moderno y rapido para construir APIs con Python 3.7+ basado en:
- **Type hints** de Python
- **Pydantic** para validacion
- **Starlette** para el servidor async
- **OpenAPI** para documentacion automatica

### Caracteristicas Principales

| Caracteristica | Descripcion |
|---------------|-------------|
| **Rendimiento** | Comparable a NodeJS y Go |
| **Velocidad de desarrollo** | 2-3x mas rapido |
| **Menos bugs** | ~40% menos errores |
| **Documentacion automatica** | Swagger UI y ReDoc |
| **Type safety** | Validacion automatica con type hints |

---

## API REST

Una **API REST** es una interfaz que permite a diferentes sistemas comunicarse usando HTTP:

| Metodo HTTP | Operacion | Descripcion |
|-------------|-----------|-------------|
| **GET** | Leer/Obtener | Recupera recursos |
| **POST** | Crear | Crea nuevos recursos |
| **PUT/PATCH** | Actualizar | Modifica recursos existentes |
| **DELETE** | Eliminar | Remueve recursos |

### Endpoints de Ejemplo (TaskFlow)

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| GET | `/proyectos` | Lista todos los proyectos |
| POST | `/proyectos` | Crea un nuevo proyecto |
| GET | `/proyectos/{id}` | Obtiene un proyecto por ID |
| PUT | `/proyectos/{id}` | Actualiza un proyecto |
| DELETE | `/proyectos/{id}` | Elimina un proyecto |

---

## Conceptos Clave

### Path Parameters

Son parte de la URL y se definen entre llaves `{}`:

```python
@app.get("/proyectos/{proyecto_id}")
def obtener_proyecto(proyecto_id: int):
    return {"id": proyecto_id, "nombre": "Proyecto Ejemplo"}
```

### Query Parameters

Son opcionales y van despues del `?` en la URL:

```python
@app.get("/proyectos")
def listar_proyectos(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### Request Body

Datos enviados en el cuerpo de la peticion (POST/PUT):

```python
from pydantic import BaseModel

class ProyectoCreate(BaseModel):
    nombre: str
    descripcion: str | None = None

@app.post("/proyectos")
def crear_proyecto(proyecto: ProyectoCreate):
    return proyecto
```

---

## Ecosistema FastAPI

| Componente | Proposito |
|-----------|-----------|
| **FastAPI** | Framework principal |
| **Uvicorn** | Servidor ASGI |
| **Starlette** | Componentes web |
| **Pydantic** | Validacion de datos |
| **OpenAPI** | Documentacion |

---

**Ultima actualizacion:** 2026-02-08
