# Codigo - Dependencias e Inyeccion de Dependencias

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Configuracion de Dependencias Basica

```python
# src/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/taskflow"
)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependencia para obtener sesion de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 2. Dependency Class

```python
# src/services/pagination.py
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")

class PaginationParams(BaseModel):
    """Parametros de paginacion"""
    skip: int = 0
    limit: int = 100

class PaginatedResponse(GenericModel, Generic[T]):
    """Respuesta paginada generica"""
    data: list[T]
    total: int
    skip: int
    limit: int

def get_pagination(
    skip: int = 0,
    limit: int = 100
) -> dict:
    """Dependencia que retorna parametros de paginacion validados"""
    return {
        "skip": min(max(skip, 0), 1000),
        "limit": min(max(limit, 1), 100)
    }
```

---

## 3. Repository Pattern con Dependencias

```python
# src/repositories/user_repository.py
from typing import Optional
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate

class UserRepository:
    """Repository para operaciones de usuario"""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        """Obtener todos los usuarios con paginacion"""
        return (
            self.db.query(User)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Obtener usuario por ID"""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email: str) -> Optional[User]:
        """Obtener usuario por email"""
        return self.db.query(User).filter(User.email == email).first()

    def create(self, user: UserCreate) -> User:
        """Crear nuevo usuario"""
        db_user = User(
            email=user.email,
            nombre_completo=user.nombre_completo,
            hashed_password=user.password  # En produccion, hashear!
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        """Actualizar usuario"""
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None

        update_data = user_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int) -> bool:
        """Eliminar usuario (soft delete)"""
        db_user = self.get_by_id(user_id)
        if not db_user:
            return False

        db_user.activo = False
        self.db.commit()
        return True
```

---

## 4. Service Layer con Dependencias

```python
# src/services/user_service.py
from typing import Optional
from sqlalchemy.orm import Session
from src.repositories.user_repository import UserRepository
from src.schemas.user import UserCreate, UserUpdate, UserResponse
from src.models.user import User

class UserService:
    """Servicio con logica de negocio"""

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_users(
        self,
        skip: int = 0,
        limit: int = 100
    ) -> dict:
        """Obtener usuarios paginados"""
        users = self.repository.get_all(skip, limit)
        total = self.repository.count()
        return {
            "data": users,
            "total": total,
            "skip": skip,
            "limit": limit
        }

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Obtener usuario por ID"""
        return self.repository.get_by_id(user_id)

    def create_user(self, user_data: UserCreate) -> User:
        """Crear usuario con validaciones"""
        # Verificar email unico
        existing = self.repository.get_by_email(user_data.email)
        if existing:
            raise ValueError("Email ya registrado")

        return self.repository.create(user_data)

    def update_user(
        self,
        user_id: int,
        user_data: UserUpdate
    ) -> Optional[User]:
        """Actualizar usuario"""
        return self.repository.update(user_id, user_data)

    def deactivate_user(self, user_id: int) -> bool:
        """Desactivar usuario"""
        return self.repository.delete(user_id)
```

---

## 5. API Routes con Depends

```python
# src/api/routes/users.py
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.services.user_service import UserService
from src.schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/api/usuarios", tags=["Usuarios"])

def get_user_service(db: Annotated[Session, Depends(get_db)]) -> UserService:
    """Factory dependency para UserService"""
    return UserService(db)

@router.get("/")
async def listar_usuarios(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    service: Annotated[UserService, Depends(get_user_service)]
):
    """Listar usuarios con paginacion"""
    return service.get_users(skip, limit)

@router.get("/{user_id}")
async def obtener_usuario(
    user_id: int,
    service: Annotated[UserService, Depends(get_user_service)]
):
    """Obtener usuario por ID"""
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return user

@router.post("/")
async def crear_usuario(
    user_data: UserCreate,
    service: Annotated[UserService, Depends(get_user_service)]
):
    """Crear nuevo usuario"""
    try:
        return service.create_user(user_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{user_id}")
async def actualizar_usuario(
    user_id: int,
    user_data: UserUpdate,
    service: Annotated[UserService, Depends(get_user_service)]
):
    """Actualizar usuario"""
    user = service.update_user(user_id, user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return user

@router.delete("/{user_id}")
async def eliminar_usuario(
    user_id: int,
    service: Annotated[UserService, Depends(get_user_service)]
):
    """Eliminar usuario (soft delete)"""
    if not service.deactivate_user(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return {"message": "Usuario eliminado"}
```

---

**Ultima actualizacion:** 2026-02-08
