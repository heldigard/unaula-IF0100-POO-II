# Codigo - SQLAlchemy y Persistencia de Datos

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Configuracion de Base de Datos

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

## 2. Modelos de Datos

```python
# src/models/user.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from src.db.database import Base
from datetime import datetime

class User(Base):
    """Modelo de usuario para base de datos"""
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    nombre_completo = Column(String(255))
    hashed_password = Column(String(255), nullable=False)
    activo = Column(Boolean, default=True)
    creado_en = Column(DateTime, default=datetime.utcnow)
    actualizado_en = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    proyectos = relationship("Project", back_populates="creador")
```

```python
# src/models/project.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from src.db.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Project(Base):
    """Modelo de proyecto"""
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)
    estado = Column(String(50), default="activo")
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    creado_en = Column(DateTime, default=datetime.utcnow)
    actualizado_en = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    creador = relationship("User", back_populates="proyectos")
    tareas = relationship("Task", back_populates="proyecto")
```

```python
# src/models/task.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric
from src.db.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Task(Base):
    """Modelo de tarea"""
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(Text)
    estado = Column(String(50), default="pendiente")
    prioridad = Column(String(20), default="media")
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_limite = Column(DateTime)
    nota_final = Column(Numeric(4, 2))
    creado_en = Column(DateTime, default=datetime.utcnow)
    actualizado_en = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    proyecto = relationship("Project", back_populates="tareas")
    usuario = relationship("User")
    comentarios = relationship("Comment", back_populates="tarea")
```

```python
# src/models/comment.py
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from src.db.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Comment(Base):
    """Modelo de comentario"""
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True)
    contenido = Column(Text, nullable=False)
    tarea_id = Column(Integer, ForeignKey("tareas.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    creado_en = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    tarea = relationship("Task", back_populates="comentarios")
    usuario = relationship("User")
```

---

## 3. Schemas Pydantic

```python
# src/schemas/user.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    """Schema base para usuario"""
    email: EmailStr
    nombre_completo: str

class UserCreate(UserBase):
    """Schema para crear usuario"""
    password: str

class UserUpdate(BaseModel):
    """Schema para actualizar usuario"""
    nombre_completo: Optional[str] = None
    email: Optional[EmailStr] = None
    activo: Optional[bool] = None

class UserResponse(UserBase):
    """Schema para respuesta de usuario"""
    id: int
    activo: bool
    creado_en: datetime

    class Config:
        from_attributes = True
```

```python
# src/schemas/task.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    """Schema base para tarea"""
    titulo: str
    descripcion: Optional[str] = None
    prioridad: Optional[str] = "media"

class TaskCreate(TaskBase):
    """Schema para crear tarea"""
    proyecto_id: int

class TaskUpdate(BaseModel):
    """Schema para actualizar tarea"""
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    prioridad: Optional[str] = None
    nota_final: Optional[float] = None

class TaskResponse(TaskBase):
    """Schema para respuesta de tarea"""
    id: int
    proyecto_id: int
    estado: str
    fecha_limite: Optional[datetime]
    creado_en: datetime

    class Config:
        from_attributes = True
```

---

## 4. Repositories

```python
# src/repositories/user_repository.py
from typing import Optional, List
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate

class UserRepository:
    """Repository para operaciones de usuario"""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[User]:
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

    def create(self, user_data: UserCreate) -> User:
        """Crear nuevo usuario"""
        db_user = User(
            email=user_data.email,
            nombre_completo=user_data.nombre_completo,
            hashed_password=user_data.password  # Hashear en produccion!
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Actualizar usuario"""
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None

        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int) -> bool:
        """Soft delete de usuario"""
        db_user = self.get_by_id(user_id)
        if not db_user:
            return False

        db_user.activo = False
        self.db.commit()
        return True
```

---

## 5. Migraciones con Alembic

```python
# alembic/versions/001_initial.py
"""Initial migration

Revision ID: 001
Revises:
Create Date: 2026-02-08

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Crear tablas
    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("nombre_completo", sa.String(255)),
        sa.Column("hashed_password", sa.String(255), nullable=False),
        sa.Column("activo", sa.Boolean(), default=True),
        sa.Column("creado_en", sa.DateTime(), default=sa.func.now()),
        sa.Column("actualizado_en", sa.DateTime(), default=sa.func.now()),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(op.f("ix_usuarios_id"), "usuarios", ["id"], unique=False)
    op.create_index(op.f("ix_usuarios_email"), "usuarios", ["email"], unique=True)

def downgrade():
    op.drop_index(op.f("ix_usuarios_email"), table_name="usuarios")
    op.drop_index(op.f("ix_usuarios_id"), table_name="usuarios")
    op.drop_table("usuarios")
```

---

**Ultima actualizacion:** 2026-02-08
