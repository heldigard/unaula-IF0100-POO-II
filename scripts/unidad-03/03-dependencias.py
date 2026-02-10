"""
Script de Práctica - Clase 3.3: Dependencias en FastAPI

Este script demuestra el sistema de dependencias de FastAPI:
- Dependencias simples
- Dependencias con clases
- Dependencias con yield (setup/teardown)
- Dependencias anidadas
- Sobrescribir dependencias en tests

Autor: IF0100 - UNAULA
"""

from fastapi import Depends, FastAPI, HTTPException, Header, status
from pydantic import BaseModel
from typing import Optional
import time

app = FastAPI(title="Sistema de Dependencias")


# =====================================================
# MODELOS
# =====================================================

class Usuario(BaseModel):
    id: int
    username: str
    email: str


class Proyecto(BaseModel):
    id: int
    nombre: str
    usuario_id: int


# =====================================================
# DEPENDENCIAS SIMPLES
# =====================================================

# Base de datos simulada
fake_users_db = {
    1: {"id": 1, "username": "juan", "email": "juan@example.com"},
    2: {"id": 2, "username": "maria", "email": "maria@example.com"},
}

fake_projects_db = {
    1: {"id": 1, "nombre": "TaskFlow", "usuario_id": 1},
    2: {"id": 2, "nombre": "Mi Proyecto", "usuario_id": 1},
}


def get_usuario(usuario_id: int):
    """Dependencia simple: obtener usuario por ID"""
    if usuario_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return fake_users_db[usuario_id]


def get_proyecto(proyecto_id: int):
    """Dependencia simple: obtener proyecto por ID"""
    if proyecto_id not in fake_projects_db:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return fake_projects_db[proyecto_id]


@app.get("/usuarios/{usuario_id}")
def leer_usuario(usuario: dict = Depends(get_usuario)):
    """Obtener usuario usando dependencia"""
    return usuario


@app.get("/proyectos/{proyecto_id}")
def leer_proyecto(proyecto: dict = Depends(get_proyecto)):
    """Obtener proyecto usando dependencia"""
    return proyecto


# =====================================================
# DEPENDENCIAS CON CLASES
# =====================================================

class CommonQueryParams:
    """Clase para parámetros comunes de consulta"""

    def __init__(
        self,
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None
    ):
        self.skip = skip
        self.limit = limit
        self.search = search


@app.get("/usuarios")
def listar_usuarios(comunes: CommonQueryParams = Depends(CommonQueryParams)):
    """Listar usuarios con parámetros comunes"""
    usuarios = list(fake_users_db.values())

    # Aplicar búsqueda si se proporciona
    if comunes.search:
        usuarios = [u for u in usuarios if comunes.search.lower() in u["username"].lower()]

    # Aplicar paginación
    resultados = usuarios[comunes.skip : comunes.skip + comunes.limit]

    return {
        "total": len(usuarios),
        "skip": comunes.skip,
        "limit": comunes.limit,
        "items": resultados
    }


# =====================================================
# DEPENDENCIAS CON YIELD (Setup/Teardown)
# =====================================================

# Base de datos simulada con conexión
class DatabaseConnection:
    """Simula una conexión a base de datos"""

    def __init__(self):
        self.conectado = False

    def connect(self):
        print("Conectando a la base de datos...")
        time.sleep(0.1)  # Simular tiempo de conexión
        self.conectado = True
        print("Conectado!")

    def close(self):
        print("Cerrando conexión a la base de datos...")
        self.conectado = False
        print("Cerrado!")


def get_db():
    """Dependencia con yield para manejo de conexiones"""
    db = DatabaseConnection()
    db.connect()  # SETUP
    try:
        yield db  # SE USA EN EL ENDPOINT
    finally:
        db.close()  # TEARDOWN (siempre se ejecuta)


@app.get("/db-status")
def check_db(db: DatabaseConnection = Depends(get_db)):
    """Verificar estado de la BD usando dependencia con yield"""
    return {
        "conectado": db.conectado,
        "mensaje": "La conexión se cerrará automáticamente después de la respuesta"
    }


# =====================================================
# DEPENDENCIAS ANIDADAS
# =====================================================

def get_current_user(x_token: str = Header(...)):
    """Obtener usuario desde token en header"""
    if x_token != "secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"id": 1, "username": "auth_user"}


def get_authenticated_user(
    current_user: dict = Depends(get_current_user),
    usuarios_db: dict = Depends(lambda: fake_users_db)
):
    """Dependencia que usa otra dependencia"""
    user_id = current_user["id"]
    if user_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarios_db[user_id]


@app.get("/me")
def leer_mi_usuario(usuario: dict = Depends(get_authenticated_user)):
    """Obtener usuario autenticado usando dependencias anidadas"""
    return usuario


# =====================================================
# SOBREESCRIBIR DEPENDENCIAS (Testing)
# =====================================================

def get_usuario_auth_override(usuario_id: int):
    """Versión override para testing"""
    return {"id": 999, "username": "test_user", "email": "test@example.com"}


@app.get("/usuarios-override/{usuario_id}", dependencies=[Depends(get_usuario_auth_override)])
def leer_usuario_override(usuario_id: int):
    """
    Este endpoint usa la versión override de la dependencia
    Útil para testing
    """
    return {"mensaje": "Este endpoint usa dependencias override", "usuario_id": usuario_id}


# =====================================================
# DEPENDENCIAS OPCIONALES
# =====================================================

from typing import Generator


def pagination(skip: int = 0, limit: int = 100) -> Generator:
    """Dependencia para paginación"""
    yield {"skip": skip, "limit": limit}


@app.get("/items")
def listar_items(pag: dict = Depends(pagination)):
    """Listar items con paginación opcional"""
    items = [{"id": i, "nombre": f"Item {i}"} for i in range(1, 101)]
    return {
        "skip": pag["skip"],
        "limit": pag["limit"],
        "items": items[pag["skip"] : pag["skip"] + pag["limit"]]
    }


# =====================================================
# EJEMPLOS DE USO
# =====================================================

@app.get("/")
def home():
    """Página principal con explicación de dependencias"""
    return {
        "titulo": "Sistema de Dependencias FastAPI",
        "endpoints": {
            "/usuarios/{id}": "Dependencia simple",
            "/proyectos/{id}": "Dependencia simple",
            "/usuarios": "Dependencia con clase (CommonQueryParams)",
            "/db-status": "Dependencia con yield (setup/teardown)",
            "/me": "Dependencias anidadas (requiere header X-Token)",
            "/items": "Dependencia opcional"
        },
        "ejemplo_header_auth": {
            "header": "X-Token: secret-token",
            "curl": 'curl -H "X-Token: secret-token" http://localhost:8002/me'
        }
    }


# =====================================================
# EJECUCIÓN
# =====================================================

if __name__ == "__main__":
    import uvicorn
    print("=" * 50)
    print("API de Dependencias FastAPI")
    print("=" * 50)
    print("\nDocumentación: http://localhost:8002/docs")
    print("\nEndpoints:")
    print("  - GET /usuarios/{id}")
    print("  - GET /usuarios?skip=0&limit=10&search=juan")
    print("  - GET /db-status")
    print("  - GET /me (requiere header X-Token)")
    print("=" * 50)

    uvicorn.run(app, host="127.0.0.1", port=8002, reload=True)


"""
EJEMPLOS DE USO:

1. Dependencia simple:
GET http://localhost:8002/usuarios/1

2. Dependencia con clase:
GET http://localhost:8002/usuarios?skip=0&limit=10&search=juan

3. Dependencia con yield:
GET http://localhost:8002/db-status

4. Dependencias anidadas (con auth):
GET http://localhost:8002/me
Header: X-Token: secret-token

5. Sin auth (debería fallar):
GET http://localhost:8002/me
(Sin header o con header incorrecto)
"""
