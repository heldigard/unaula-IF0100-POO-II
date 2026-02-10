# Teoría - Domain-Driven Design (DDD)

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es DDD?

**Domain-Driven Design** es un enfoque de desarrollo de software que se centra en el dominio del problema y en la lógica de negocio, más que en detalles técnicos de implementación.

### Principios Fundamentales

| Principio | Descripción |
|-----------|-------------|
| **Ubiquitous Language** | Lenguaje compartido entre expertos del dominio y desarrolladores |
| **Bounded Contexts** | Delimitar fronteras claras entre diferentes contextos del dominio |
| **Modelo Rico** | El modelo no es solo datos, incluye comportamiento y reglas de negocio |
| **Separación de Capas** | Dominio, Aplicación, Infraestructura e Interfaz |

### Arquitectura en Capas DDD

```
┌─────────────────────────────────────┐
│     UI / Presentación               │
│   (Controllers, Templates)         │
├─────────────────────────────────────┤
│     Aplicación                      │
│   (Servicios, Casos de uso)        │
├─────────────────────────────────────┤
│     Dominio                         │
│   (Entidades, VOs, Servicios)      │
├─────────────────────────────────────┤
│     Infraestructura                  │
│   (Repositorios, BD, APIs)         │
└─────────────────────────────────────┘
```

---

## 2. Entidades

Una **Entidad** es un objeto definido por su **identidad**, no por sus atributos. Dos entidades son iguales si tienen el mismo ID.

### Características

- Identidad única (ID)
- Ciclo de vida (puede cambiar)
- Continuidad (mantiene identidad aunque atributos cambien)
- Comportamiento encapsulado

### Ejemplo: Entidad Usuario

```python
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Usuario:
    """
    Entidad Usuario en el dominio TaskFlow.

    La identidad de un usuario está dada por su ID,
    no por su username o email que pueden cambiar.
    """
    id: Optional[int]
    username: str
    email: str
    password_hash: str
    nombre_completo: Optional[str] = None
    activo: bool = True

    def cambiar_email(self, nuevo_email: str):
        """Cambia el email del usuario."""
        if "@" not in nuevo_email:
            raise ValueError("Email inválido")
        self.email = nuevo_email

    def desactivar(self):
        """Desactiva el usuario."""
        self.activo = False

    def puede_crear_proyectos(self) -> bool:
        """Verifica si el usuario puede crear proyectos."""
        return self.activo
```

---

## 3. Value Objects

Un **Value Object** es un objeto definido por sus atributos, no por su identidad. Son **inmutables**.

### Características

- Sin identidad
- Inmutables
- Compartibles
- Validados al crearse

### Ejemplo: Value Object Email

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    """Value Object que representa un email."""
    valor: str

    def __post_init__(self):
        """Valida el email después de la creación."""
        if "@" not in self.valor:
            raise ValueError(f"Email inválido: {self.valor}")

    def dominio(self) -> str:
        """Retorna el dominio del email."""
        return self.valor.split("@")[1]
```

### Comparación Entidad vs Value Object

| Aspecto | Entidad | Value Object |
|---------|---------|--------------|
| Identidad | Definida por ID | Definida por atributos |
| Mutable | Sí | No (inmutable) |
| Comparación | Por ID | Por todos los atributos |
| Ciclo de vida | Largo, con cambios | Corto, se reemplaza |
| Ejemplos | Usuario, Tarea, Proyecto | Email, Fecha, Dinero |

---

## 4. Patrón Repository

Un **Repository** es una abstracción que simula una colección de objetos del dominio, ocultando los detalles de persistencia.

### Propósito

- Abstraer persistencia
- Centrar lógica de acceso
- Facilitar testing
- Separar responsabilidades

### Interfaz de Repository

```python
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

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


# Implementación para Usuario
class UsuarioRepository(Repository[Usuario]):
    """Repositorio para la entidad Usuario."""

    def guardar(self, usuario: Usuario) -> Usuario:
        if usuario.id is None:
            return self._crear(usuario)
        else:
            return self._actualizar(usuario)

    def obtener_por_id(self, id: int) -> Optional[Usuario]:
        pass

    def obtener_todos(self) -> List[Usuario]:
        pass

    def eliminar(self, usuario: Usuario) -> None:
        pass
```

---

## 5. Servicios de Dominio

Lógica de negocio que no pertenece naturalmente a una Entidad o Value Object específico.

### Características

- Stateless (no mantienen estado)
- Operaciones del dominio
- No CRUD simple

### Ejemplo: Servicio de Autenticación

```python
class AuthService:
    """Servicio de dominio para autenticación."""

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def login(self, username: str, password: str) -> dict:
        """Autentica un usuario."""
        usuario = self.repo.obtener_por_username(username)

        if not usuario:
            return {"exitoso": False, "mensaje": "Usuario no encontrado"}

        if usuario.password_hash != self._hashear(password):
            return {"exitoso": False, "mensaje": "Password incorrecto"}

        if not usuario.activo:
            return {"exitoso": False, "mensaje": "Usuario desactivado"}

        return {"exitoso": True, "usuario": usuario}
```

---

## 6. Buenas Prácticas

### DO's

- Pon lógica en entidades (no modelos anémicos)
- Usa Value Objects para conceptos sin identidad
- Abstrae con repositorios (dominio no sabe sobre BD)
- Servicios stateless
- Usa el lenguaje del dominio

### DON'T's

- No modelos anémicos (solo getters/setters)
- No lógica de infraestructura en dominio
- No servicios con todo
- No bases de datos en entidades

---

**Última actualización:** 2026-02-08
