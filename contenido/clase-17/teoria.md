# Teoria - SQLAlchemy y Persistencia de Datos

**IF0100 - Lenguaje de Programacion OO II**

---

## SQLAlchemy

### Que es SQLAlchemy?

SQLAlchemy es el kit de herramientas SQL de Python y Object-Relational Mapper (ORM). Proporciona:

| Componente | Descripcion |
|------------|-------------|
| **Core** | Abstracciones de base de datos de bajo nivel |
| **ORM** | Mapeo objeto-relacional para alto nivel |

```
┌─────────────────────────────────────────┐
│            Aplicacion Python            │
├─────────────────────────────────────────┤
│  Pydantic (Schemas)                     │
│       │                                 │
│       ▼                                 │
│  SQLAlchemy ORM                         │
│       │                                 │
│       ▼                                 │
│  SQLAlchemy Core (SQL Expression)        │
│       │                                 │
│       ▼                                 │
│  Database Driver (psycopg2, asyncpg)     │
├─────────────────────────────────────────┤
│         PostgreSQL / MySQL / SQLite      │
└─────────────────────────────────────────┘
```

---

## Modelos vs Schemas

### Modelos (Base de Datos)

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
```

### Schemas (API)

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

class UserResponse(UserBase):
    """Schema para respuesta de usuario"""
    id: int
    activo: bool
    creado_en: datetime

    class Config:
        from_attributes = True
```

---

## Sesiones y Transacciones

### Configuracion de Sesion

```python
# src/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import user, project, task  # Importar todos los modelos

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/taskflow"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency para obtener sesion
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Patrones de Sesion

```python
# Buena practica: Context Manager
from contextlib import contextmanager
from sqlalchemy.orm import Session

@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

# Uso
with get_db_session() as session:
    user = session.query(User).first()
```

---

## Relaciones en SQLAlchemy

### Relacion Uno a Muchos

```python
# src/models/project.py
class Project(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    descripcion = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    # Relacion 1:N
    tareas = relationship("Task", back_populates="proyecto")
    usuario = relationship("User", back_populates="proyectos")

# src/models/task.py
class Task(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255))
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))

    # Relacion N:1
    proyecto = relationship("Project", back_populates="tareas")
```

### Relacion Muchos a Muchos

```python
# src/models/user.py
from sqlalchemy import Table, Column, Integer, ForeignKey

# Tabla de asociacion
user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("usuarios.id")),
    Column("role_id", Integer, ForeignKey("roles.id"))
)

class User(Base):
    # Relacion N:M
    roles = relationship("Role", secondary=user_roles, back_populates="users")
```

---

## Consultas con SQLAlchemy

### CRUD Basico

```python
# Crear
def create_user(db: Session, user_data: UserCreate):
    db_user = User(
        email=user_data.email,
        nombre_completo=user_data.nombre_completo,
        hashed_password=hash_password(user_data.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Leer todos
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Leer por ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Actualizar
def update_user(db: Session, user_id: int, user_data: UserUpdate):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    for field, value in user_data.model_dump(exclude_unset=True).items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user

# Eliminar (soft delete)
def deactivate_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return False

    db_user.activo = False
    db.commit()
    return True
```

### Consultas Avanzadas

```python
from sqlalchemy import or_, and_, desc, func

# Filtros complejos
def search_users(db: Session, query: str, activo: bool = None):
    users = db.query(User)

    if query:
        users = users.filter(
            or_(
                User.email.ilike(f"%{query}%"),
                User.nombre_completo.ilike(f"%{query}%")
            )
        )

    if activo is not None:
        users = users.filter(User.activo == activo)

    return users.order_by(desc(User.creado_en)).all()

# Agregaciones
def count_users_by_status(db: Session):
    return (
        db.query(User.activo, func.count(User.id))
        .group_by(User.activo)
        .all()
    )
```

---

**Ultima actualizacion:** 2026-02-08
