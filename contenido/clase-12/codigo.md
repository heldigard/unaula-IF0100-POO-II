# Código - Domain-Driven Design (DDD)

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Entidades con DDD

### src/domain/models/usuario.py

```python
# src/domain/models/usuario.py

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class Usuario:
    """Entidad Usuario del dominio TaskFlow."""
    id: Optional[int] = None
    username: str = ""
    email: str = ""
    password_hash: str = ""
    nombre_completo: Optional[str] = None
    activo: bool = True
    creado_en: Optional[datetime] = None

    def __eq__(self, other):
        if not isinstance(other, Usuario):
            return False
        return self.id is not None and self.id == other.id

    def __hash__(self):
        return hash(self.id) if self.id is not None else hash(id(self))

    def cambiar_email(self, nuevo_email: str):
        if "@" not in nuevo_email:
            raise ValueError("Email inválido")
        self.email = nuevo_email

    def puede_crear_proyectos(self) -> bool:
        return self.activo
```

---

## 2. Value Objects

### src/domain/value_objects/email.py

```python
# src/domain/value_objects/email.py

from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    """Value Object para representar un email."""
    valor: str

    def __post_init__(self):
        if "@" not in self.valor:
            raise ValueError(f"Email inválido: {self.valor}")

    def dominio(self) -> str:
        return self.valor.split("@")[1]

    def __str__(self):
        return self.valor


@dataclass(frozen=True)
class Prioridad:
    """Value Object para prioridad de tareas."""
    valor: str

    def __post_init__(self):
        prioridades_validas = ["baja", "media", "alta", "urgente"]
        if self.valor not in prioridades_validas:
            raise ValueError(f"Prioridad inválida: {self.valor}")
```

---

## 3. Patrón Repository

### src/domain/repositories/base.py

```python
# src/domain/repositories/base.py

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class Repository(ABC, Generic[T]):
    """Interfaz base para repositorios."""

    @abstractmethod
    def guardar(self, entidad: T) -> T:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[T]:
        pass

    @abstractmethod
    def eliminar(self, entidad: T) -> None:
        pass
```

### src/domain/repositories/usuario_repo.py

```python
# src/domain/repositories/usuario_repo.py

from src.domain.repositories.base import Repository
from src.domain.models.usuario import Usuario
from typing import Optional, List


class UsuarioRepository(Repository[Usuario]):
    """Repositorio para la entidad Usuario."""

    def guardar(self, usuario: Usuario) -> Usuario:
        pass

    def obtener_por_id(self, id: int) -> Optional[Usuario]:
        pass

    def obtener_por_username(self, username: str) -> Optional[Usuario]:
        pass

    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        pass

    def obtener_todos(self) -> List[Usuario]:
        pass

    def eliminar(self, usuario: Usuario) -> None:
        pass
```

---

## 4. Implementación con SQLite

### src/infrastructure/repositories/usuario_sqlite_repo.py

```python
# src/infrastructure/repositories/usuario_sqlite_repo.py

import sqlite3
from src.domain.repositories.usuario_repo import UsuarioRepository
from src.domain.models.usuario import Usuario
from typing import List, Optional


class UsuarioSQLiteRepository(UsuarioRepository):
    """Implementación con SQLite."""

    def __init__(self, db_path: str = "taskflow.db"):
        self.db_path = db_path

    def guardar(self, usuario: Usuario) -> Usuario:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        if usuario.id is None:
            cursor.execute(
                "INSERT INTO usuarios (username, email) VALUES (?, ?)",
                (usuario.username, usuario.email)
            )
            usuario.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE usuarios SET username=?, email=? WHERE id=?",
                (usuario.username, usuario.email, usuario.id)
            )

        conn.commit()
        conn.close()
        return usuario

    def obtener_por_id(self, id: int) -> Optional[Usuario]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Usuario(
                id=row[0],
                username=row[1],
                email=row[2],
                password_hash=row[3]
            )
        return None

    def obtener_todos(self) -> List[Usuario]:
        pass

    def eliminar(self, usuario: Usuario) -> None:
        pass
```

---

## 5. Servicios de Dominio

### src/domain/services/usuario_service.py

```python
# src/domain/services/usuario_service.py

from typing import Optional
from src.domain.models.usuario import Usuario
from src.domain.repositories.usuario_repo import UsuarioRepository


class UsuarioService:
    """Servicio de lógica de negocio para usuarios."""

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def crear_usuario(self, username: str, email: str, password: str) -> Usuario:
        """Crea un nuevo usuario."""
        if len(username) < 3:
            raise ValueError("Username muy corto")

        if self.repo.obtener_por_username(username):
            raise ValueError("Username ya existe")

        usuario = Usuario(
            id=None,
            username=username,
            email=email,
            password_hash=self._hashear_password(password)
        )

        return self.repo.guardar(usuario)

    def obtener_usuario(self, id: int) -> Optional[Usuario]:
        """Obtiene usuario por ID."""
        return self.repo.obtener_por_id(id)

    @staticmethod
    def _hashear_password(password: str) -> str:
        """Hashea el password (simplificado)."""
        # En producción usar bcrypt
        return hash(password)
```

---

**Última actualización:** 2026-02-08
