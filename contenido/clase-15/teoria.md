# Teoria - Dependencias e Inyeccion de Dependencias

**IF0100 - Lenguaje de Programacion OO II**

---

## Inyeccion de Dependencias (DI)

### Concepto

La inyeccion de dependencias es un patron de diseno que permite que un objeto reciba sus dependencias desde外部 (en lugar de crearlas internamente).

```
SIN DI:   UserService crea su propia dependencia
          UserService ──► Database()

CON DI:   UserService recibe la dependencia externa
          UserService ◄── Database()
                        ^
                        |
                   Inyectada
```

### Ventajas

| Ventaja | Descripcion |
|---------|-------------|
| **Testabilidad** | Facilita tests con mocks |
| **Desacoplamiento** | Componentes no dependen de implementaciones concretas |
| **Flexibilidad** | Facilita cambiar implementaciones |
| **Reutilizacion** | Componentes mas reutilizables |

---

## Sistema de Dependencias de FastAPI

### Dependency Injection Basico

```python
from fastapi import FastAPI, Depends

app = FastAPI()

# Dependencia simple
def get_db():
    db = DatabaseConnection()
    try:
        yield db
    finally:
        db.close()

# Usar la dependencia
@app.get("/users/")
def get_users(db = Depends(get_db)):
    return db.query("SELECT * FROM users")
```

### Dependencias con Parametros

```python
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# Dependencia con parametros
def get pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def list_items(p: Annotated[dict, Depends(pagination)]):
    return {"items": [...], "pagination": p}
```

### Clases como Dependencias

```python
class PaginationParams:
    def __init__(
        self,
        skip: int = Query(0, ge=0),
        limit: int = Query(100, ge=1, le=1000)
    ):
        self.skip = skip
        self.limit = limit

@app.get("/items/")
def get_items(params: Annotated[PaginationParams, Depends()]):
    return {"skip": params.skip, "limit": params.limit}
```

---

## Patrones de Organizacion

### Capa de Servicios

```
API Routes
    │
    ▼
Services (Logica de negocio)
    │
    ▼
Repositories (Acceso a datos)
    │
    ▼
Database
```

### Ejemplo Estructura

```python
# src/api/dependencies.py
from typing import Annotated
from src.db.session import get_db
from src.services.user_service import UserService

async def get_user_service(
    db = Depends(get_db)
) -> UserService:
    return UserService(db)

# src/api/routes/users.py
from fastapi import APIRouter, Depends
from src.api.dependencies import get_user_service

router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(
    user_id: int,
    service: Annotated[UserService, Depends(get_user_service)]
):
    return service.get_by_id(user_id)
```

---

**Ultima actualizacion:** 2026-02-08
