# Guías de Taller - IF0100 POO II

**Versión:** 1.0
**Fecha:** 2026-02-07
**Curso:** IF0100 - Lenguaje de Programación Orientado a Objetos II

---

## Índice

- [Taller 1.6: Modelos del Sistema con Pydantic](#taller-16-modelos-del-sistema-con-pydantic)
- [Taller 2.3: Repositorio en Memoria con Tests](#taller-23-repositorio-en-memoria-con-tests)
- [Taller 2.7: Servicios con TDD](#taller-27-servicios-con-tdd)
- [Taller 3.5: CRUD API con FastAPI](#taller-35-crud-api-con-fastapi)
- [Taller 4.3: Formularios con Jinja2 y HTMX](#taller-43-formularios-con-jinja2-y-htmx)
- [Taller 4.7: Interfaz Completa del Sistema](#taller-47-interfaz-completa-del-sistema)
- [Taller 5.3: Preparación para Sustentación](#taller-53-preparación-para-sustentación)

---

## Taller 1.6: Modelos del Sistema con Pydantic

**Unidad:** 1 - POO Avanzada con Python
**Clase:** 1.6 - Diseño de modelos y DTOs
**Duración:** 90 minutos
**Formato:** Parejas
**Entregable:** Modelos completos del sistema TaskFlow

### 1. Objetivos

Al finalizar este taller, usted será capaz de:
- [ ] Crear modelos con Pydantic BaseModel
- [ ] Definir schemas para request/response
- [ ] Implementar validaciones personalizadas
- [ ] Crear modelos anidados y complejos

### 2. Contexto

Estamos construyendo el sistema TaskFlow. Ya tenemos las entidades de dominio (Usuario, Proyecto, Tarea) usando dataclasses. Ahora necesitamos crear schemas Pydantic para:
- Validar datos de entrada (request)
- Formatear datos de salida (response)
- Serializar/deserializar para la API

### 3. Paso a Paso

#### Paso 1: Configuración (10 min)

```bash
# Crear estructura de carpetas
mkdir -p src/taskflow/schemas
touch src/taskflow/schemas/__init__.py
touch src/taskflow/schemas/usuario.py
touch src/taskflow/schemas/proyecto.py
touch src/taskflow/schemas/tarea.py
```

#### Paso 2: Schema de Usuario (20 min)

**Archivo:** `src/taskflow/schemas/usuario.py`

```python
"""
Schemas Pydantic para Usuario.
"""

from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime


class UsuarioBase(BaseModel):
    """Base fields para usuario."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    nombre_completo: Optional[str] = None


class UsuarioCreate(UsuarioBase):
    """Schema para crear usuario (incluye password)."""
    password: str = Field(..., min_length=8)

    @field_validator('password')
    @classmethod
    def password_strength(cls, v: str) -> str:
        """Valida que el password tenga mayúscula, minúscula y número."""
        if not any(c.isupper() for c in v):
            raise ValueError('Password debe tener al menos una mayúscula')
        if not any(c.islower() for c in v):
            raise ValueError('Password debe tener al menos una minúscula')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password debe tener al menos un número')
        return v


class UsuarioUpdate(BaseModel):
    """Schema para actualizar usuario."""
    nombre_completo: Optional[str] = None
    email: Optional[EmailStr] = None


class UsuarioResponse(UsuarioBase):
    """Schema para respuesta de usuario."""
    id: int
    creado_en: datetime

    class Config:
        from_attributes = True  # Pydantic v2


class UsuarioLogin(BaseModel):
    """Schema para login."""
    username: str
    password: str
```

**Validar:**
```python
# En tests/test_schemas/test_usuario.py

def test_usuario_create_valido():
    schema = UsuarioCreate(
        username="jdoe",
        email="john@example.com",
        password="SecurePass123"
    )
    assert schema.username == "jdoe"

def test_password_debil_falla():
    with pytest.raises(ValidationError):
        UsuarioCreate(
            username="test",
            email="test@example.com",
            password="debil"  # Sin mayúscula ni número
        )
```

#### Paso 3: Schema de Proyecto (15 min)

**Archivo:** `src/taskflow/schemas/proyecto.py`

```python
"""
Schemas Pydantic para Proyecto.
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime


class ProyectoBase(BaseModel):
    """Base fields para proyecto."""
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=1000)


class ProyectoCreate(ProyectoBase):
    """Schema para crear proyecto."""
    usuario_id: int


class ProyectoUpdate(BaseModel):
    """Schema para actualizar proyecto."""
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=1000)


class ProyectoResponse(ProyectoBase):
    """Schema para respuesta de proyecto."""
    id: int
    usuario_id: int
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True
```

#### Paso 4: Schema de Tarea con Enums (25 min)

**Archivo:** `src/taskflow/schemas/tarea.py`

```python
"""
Schemas Pydantic para Tarea.
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime, date
from enum import Enum


class EstadoTarea(str, Enum):
    """Estados posibles de una tarea."""
    PENDIENTE = "pendiente"
    EN_PROGRESO = "en_progreso"
    COMPLETADA = "completada"
    CANCELADA = "cancelada"


class PrioridadTarea(str, Enum):
    """Niveles de prioridad."""
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"
    URGENTE = "urgente"


class TareaBase(BaseModel):
    """Base fields para tarea."""
    titulo: str = Field(..., min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=2000)
    estado: EstadoTarea = EstadoTarea.PENDIENTE
    prioridad: PrioridadTarea = PrioridadTarea.MEDIA


class TareaCreate(TareaBase):
    """Schema para crear tarea."""
    proyecto_id: int
    asignado_a: Optional[int] = None
    fecha_limite: Optional[date] = None

    @field_validator('fecha_limite')
    @classmethod
    def fecha_limite_futura(cls, v: Optional[date]) -> Optional[date]:
        """Valida que la fecha límite sea futura."""
        if v and v < date.today():
            raise ValueError('Fecha límite debe ser futura')
        return v


class TareaUpdate(BaseModel):
    """Schema para actualizar tarea."""
    titulo: Optional[str] = Field(None, min_length=3, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=2000)
    estado: Optional[EstadoTarea] = None
    prioridad: Optional[PrioridadTarea] = None
    asignado_a: Optional[int] = None
    fecha_limite: Optional[date] = None


class TareaResponse(TareaBase):
    """Schema para respuesta de tarea."""
    id: int
    proyecto_id: int
    asignado_a: Optional[int] = None
    creada_por: int
    fecha_limite: Optional[date] = None
    completada_en: Optional[datetime] = None
    creada_en: datetime
    actualizada_en: datetime

    class Config:
        from_attributes = True


class TareaConProyecto(TareaResponse):
    """Schema de tarea con información del proyecto."""
    proyecto_nombre: str
    proyecto_usuario_id: int
```

#### Paso 5: Schemas Compuestos (15 min)

**Archivo:** `src/taskflow/schemas/__init__.py`

```python
"""
Schemas compuestos para respuestas complejas.
"""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from .usuario import UsuarioResponse
from .proyecto import ProyectoResponse
from .tarea import TareaResponse


class ProyectoConTareas(ProyectoResponse):
    """Proyecto con sus tareas."""
    tareas: List[TareaResponse] = []
    total_tareas: int
    tareas_completadas: int


class UsuarioConProyectos(UsuarioResponse):
    """Usuario con sus proyectos."""
    proyectos: List[ProyectoResponse] = []
    total_proyectos: int


class DashboardStats(BaseModel):
    """Estadísticas para el dashboard."""
    total_usuarios: int
    total_proyectos: int
    total_tareas: int
    tareas_pendientes: int
    tareas_en_progreso: int
    tareas_completadas: int
    proyectos_activos: int
```

### 4. Validación y Tests

**Archivo:** `tests/test_schemas/test_tarea.py`

```python
import pytest
from datetime import date, timedelta
from taskflow.schemas.tarea import (
    TareaCreate,
    EstadoTarea,
    PrioridadTarea
)


def test_tarea_create_valida():
    tarea = TareaCreate(
        titulo="Implementar login",
        descripcion="Crear endpoint de autenticación",
        proyecto_id=1,
        prioridad=PrioridadTarea.ALTA,
        fecha_limite=date.today() + timedelta(days=7)
    )
    assert tarea.titulo == "Implementar login"
    assert tarea.estado == EstadoTarea.PENDIENTE


def test_tarea_fecha_limite_pasada_falla():
    with pytest.raises(ValueError) as exc:
        TareaCreate(
            titulo="Tarea",
            proyecto_id=1,
            fecha_limite=date.today() - timedelta(days=1)
        )
    assert "futura" in str(exc.value).lower()
```

### 5. Reto Adicional (Opcional)

Agregar schemas para comentarios con:
- Validación de contenido no vacío
- Relación con tarea y usuario
- Timestamp automático

### 6. Entregables

- [ ] `src/taskflow/schemas/usuario.py` completo
- [ ] `src/taskflow/schemas/proyecto.py` completo
- [ ] `src/taskflow/schemas/tarea.py` completo
- [ ] `src/taskflow/schemas/__init__.py` con schemas compuestos
- [ ] Tests para todos los schemas
- [ ] Todos los tests pasando (`pytest`)

---

## Taller 2.3: Repositorio en Memoria con Tests

**Unidad:** 2 - Técnicas de Desarrollo
**Clase:** 2.3 - Mocks y Fixtures
**Duración:** 90 minutos
**Formato:** Parejas
**Entregable:** Repositorio en memoria con tests completos

### 1. Objetivos

- [ ] Implementar patrón Repository
- [ ] Usar fixtures de pytest
- [ ] Crear implementación en memoria para tests
- [ ] Escribir tests exhaustivos

### 2. Contexto

Necesitamos una capa de abstracción para la persistencia. El patrón Repository nos permite:
- Decoupling entre dominio e infraestructura
- Facilidad de testing (implementación en memoria)
- Posibilidad de cambiar la tecnología de persistencia

### 3. Paso a Paso

#### Paso 1: Interfaz Base (15 min)

**Archivo:** `src/taskflow/repositories/base.py`

```python
"""
Interfaz base para repositorios.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Type, Optional, List

T = TypeVar('T')


class Repository(ABC, Generic[T]):
    """
    Interfaz base para repositorios.

    Define operaciones CRUD genéricas.
    """

    @abstractmethod
    def guardar(self, entity: T) -> T:
        """Guarda o actualiza una entidad."""
        pass

    @abstractmethod
    def buscar_por_id(self, entity_id: int) -> Optional[T]:
        """Busca una entidad por ID."""
        pass

    @abstractmethod
    def listar_todos(self) -> List[T]:
        """Lista todas las entidades."""
        pass

    @abstractmethod
    def eliminar(self, entity_id: int) -> bool:
        """Elimina una entidad por ID."""
        pass

    @abstractmethod
    def contar(self) -> int:
        """Cuenta el total de entidades."""
        pass
```

#### Paso 2: Repositorio de Usuario en Memoria (30 min)

**Archivo:** `src/taskflow/repositories/usuario_repo.py`

```python
"""
Repositorio de Usuario en memoria para tests.
"""

from typing import Optional, List, Dict

from taskflow.repositories.base import Repository
from taskflow.models.usuario import Usuario


class UsuarioRepositoryInMemory(Repository[Usuario]):
    """
    Implementación en memoria del repositorio de usuarios.

    Útil para testing y prototipado rápido.

    Attributes:
        _usuarios: Diccionario interno de usuarios (id -> usuario)
        _next_id: Contador para generar IDs
    """

    def __init__(self):
        """Inicializa el repositorio vacío."""
        self._usuarios: Dict[int, Usuario] = {}
        self._next_id = 1

    def guardar(self, usuario: Usuario) -> Usuario:
        """
        Guarda un usuario (crea o actualiza).

        Args:
            usuario: Usuario a guardar

        Returns:
            El usuario guardado con ID asignado si es nuevo
        """
        if usuario.id is None:
            # Crear nuevo usuario
            usuario.id = self._next_id
            self._next_id += 1
            self._usuarios[usuario.id] = usuario
        else:
            # Actualizar usuario existente
            if usuario.id not in self._usuarios:
                raise ValueError(f"Usuario con ID {usuario.id} no existe")
            self._usuarios[usuario.id] = usuario

        return usuario

    def buscar_por_id(self, usuario_id: int) -> Optional[Usuario]:
        """
        Busca un usuario por ID.

        Args:
            usuario_id: ID del usuario a buscar

        Returns:
            El usuario encontrado o None
        """
        return self._usuarios.get(usuario_id)

    def buscar_por_username(self, username: str) -> Optional[Usuario]:
        """
        Busca un usuario por username.

        Args:
            username: Username único

        Returns:
            El usuario encontrado o None
        """
        for usuario in self._usuarios.values():
            if usuario.username == username:
                return usuario
        return None

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        """
        Busca un usuario por email.

        Args:
            email: Email único

        Returns:
            El usuario encontrado o None
        """
        for usuario in self._usuarios.values():
            if usuario.email == email:
                return usuario
        return None

    def listar_todos(self) -> List[Usuario]:
        """Retorna todos los usuarios."""
        return list(self._usuarios.values())

    def eliminar(self, usuario_id: int) -> bool:
        """
        Elimina un usuario por ID.

        Args:
            usuario_id: ID del usuario a eliminar

        Returns:
            True si se eliminó, False si no existía
        """
        if usuario_id in self._usuarios:
            del self._usuarios[usuario_id]
            return True
        return False

    def contar(self) -> int:
        """Retorna el total de usuarios."""
        return len(self._usuarios)

    def limpiar(self):
        """Elimina todos los usuarios (útil para tests)."""
        self._usuarios.clear()
        self._next_id = 1
```

#### Paso 3: Tests con Fixtures (30 min)

**Archivo:** `tests/conftest.py`

```python
"""
Fixtures compartidas para tests.
"""

import pytest
from taskflow.repositories.usuario_repo import UsuarioRepositoryInMemory
from taskflow.repositories.proyecto_repo import ProyectoRepositoryInMemory
from taskflow.repositories.tarea_repo import TareaRepositoryInMemory


@pytest.fixture
def usuario_repo_vacio():
    """Retorna un repositorio de usuarios vacío."""
    return UsuarioRepositoryInMemory()


@pytest.fixture
def proyecto_repo_vacio():
    """Retorna un repositorio de proyectos vacío."""
    return ProyectoRepositoryInMemory()


@pytest.fixture
def tarea_repo_vacio():
    """Retorna un repositorio de tareas vacío."""
    return TareaRepositoryInMemory()


@pytest.fixture
def usuario_repo_con_datos(usuario_repo_vacio):
    """Retorna un repositorio con 3 usuarios de prueba."""
    from datetime import datetime
    from taskflow.models.usuario import Usuario, EstadoUsuario

    usuarios = [
        Usuario(
            username="admin",
            email="admin@taskflow.local",
            password_hash="hash1",
            nombre_completo="Administrador",
            estado=EstadoUsuario.ACTIVO,
            creado_en=datetime.now()
        ),
        Usuario(
            username="jdoe",
            email="john@example.com",
            password_hash="hash2",
            nombre_completo="John Doe",
            estado=EstadoUsuario.ACTIVO,
            creado_en=datetime.now()
        ),
        Usuario(
            username="asmith",
            email="alice@example.com",
            password_hash="hash3",
            nombre_completo="Alice Smith",
            estado=EstadoUsuario.ACTIVO,
            creado_en=datetime.now()
        ),
    ]

    for usuario in usuarios:
        usuario_repo_vacio.guardar(usuario)

    return usuario_repo_vacio
```

**Archivo:** `tests/test_repositories/test_usuario_repo.py`

```python
"""
Tests del repositorio de usuarios en memoria.
"""

import pytest
from datetime import datetime
from taskflow.models.usuario import Usuario, EstadoUsuario
from taskflow.repositories.usuario_repo import UsuarioRepositoryInMemory


class TestUsuarioRepositoryCrear:
    """Tests para crear usuarios."""

    def test_crear_usuario_nuevo(self, usuario_repo_vacio):
        """Test crear nuevo usuario."""
        usuario = Usuario(
            username="jdoe",
            email="john@example.com",
            password_hash="hash123"
        )

        guardado = usuario_repo_vacio.guardar(usuario)

        assert guardado.id is not None
        assert guardado.id == 1
        assert guardado.username == "jdoe"
        assert usuario_repo_vacio.contar() == 1

    def test_crear_usuario_asigna_id_incremental(self, usuario_repo_vacio):
        """Test que IDs se asignan incrementalmente."""
        u1 = usuario_repo_vacio.guardar(Usuario(username="a", email="a@a.com", password_hash="h1"))
        u2 = usuario_repo_vacio.guardar(Usuario(username="b", email="b@b.com", password_hash="h2"))
        u3 = usuario_repo_vacio.guardar(Usuario(username="c", email="c@c.com", password_hash="h3"))

        assert u1.id == 1
        assert u2.id == 2
        assert u3.id == 3

    def test_actualizar_usuario_existente(self, usuario_repo_vacio):
        """Test actualizar usuario existente."""
        usuario = usuario_repo_vacio.guardar(
            Usuario(username="jdoe", email="john@example.com", password_hash="h1")
        )

        # Modificar y guardar
        usuario.nombre_completo = "John Doe"
        actualizado = usuario_repo_vacio.guardar(usuario)

        assert actualizado.nombre_completo == "John Doe"
        assert actualizado.id == 1  # ID no cambia
        assert usuario_repo_vacio.contar() == 1  # No crea nuevo

    def test_actualizar_usuario_inexistente_falla(self, usuario_repo_vacio):
        """Test error al actualizar usuario inexistente."""
        usuario = Usuario(
            id=999,  # ID no existe
            username="nobody",
            email="no@body.com",
            password_hash="hash"
        )

        with pytest.raises(ValueError) as exc:
            usuario_repo_vacio.guardar(usuario)

        assert "999" in str(exc.value)
        assert "no existe" in str(exc.value)


class TestUsuarioRepositoryBuscar:
    """Tests para buscar usuarios."""

    def test_buscar_por_id_existente(self, usuario_repo_con_datos):
        """Test buscar usuario por ID existente."""
        usuario = usuario_repo_con_datos.buscar_por_id(1)

        assert usuario is not None
        assert usuario.id == 1
        assert usuario.username == "admin"

    def test_buscar_por_id_inexistente(self, usuario_repo_con_datos):
        """Test buscar usuario por ID inexistente."""
        usuario = usuario_repo_con_datos.buscar_por_id(999)
        assert usuario is None

    def test_buscar_por_username_existente(self, usuario_repo_con_datos):
        """Test buscar usuario por username existente."""
        usuario = usuario_repo_con_datos.buscar_por_username("jdoe")

        assert usuario is not None
        assert usuario.username == "jdoe"
        assert usuario.email == "john@example.com"

    def test_buscar_por_username_inexistente(self, usuario_repo_con_datos):
        """Test buscar usuario por username inexistente."""
        usuario = usuario_repo_con_datos.buscar_por_username("nobody")
        assert usuario is None

    def test_buscar_por_email_existente(self, usuario_repo_con_datos):
        """Test buscar usuario por email existente."""
        usuario = usuario_repo_con_datos.buscar_por_email("alice@example.com")

        assert usuario is not None
        assert usuario.username == "asmith"

    def test_buscar_por_email_inexistente(self, usuario_repo_con_datos):
        """Test buscar usuario por email inexistente."""
        usuario = usuario_repo_con_datos.buscar_por_email("nobody@example.com")
        assert usuario is None


class TestUsuarioRepositoryListar:
    """Tests para listar usuarios."""

    def test_listar_todos(self, usuario_repo_con_datos):
        """Test listar todos los usuarios."""
        usuarios = usuario_repo_con_datos.listar_todos()

        assert len(usuarios) == 3
        usernames = [u.username for u in usuarios]
        assert "admin" in usernames
        assert "jdoe" in usernames
        assert "asmith" in usernames

    def test_listar_vacio(self, usuario_repo_vacio):
        """Test listar cuando no hay usuarios."""
        usuarios = usuario_repo_vacio.listar_todos()
        assert len(usuarios) == 0

    def test_contar(self, usuario_repo_con_datos):
        """Test contar usuarios."""
        assert usuario_repo_con_datos.contar() == 3


class TestUsuarioRepositoryEliminar:
    """Tests para eliminar usuarios."""

    def test_eliminar_existente(self, usuario_repo_con_datos):
        """Test eliminar usuario existente."""
        resultado = usuario_repo_con_datos.eliminar(2)

        assert resultado is True
        assert usuario_repo_con_datos.contar() == 2
        assert usuario_repo_con_datos.buscar_por_id(2) is None

    def test_eliminar_inexistente(self, usuario_repo_con_datos):
        """Test eliminar usuario inexistente."""
        resultado = usuario_repo_con_datos.eliminar(999)

        assert resultado is False
        assert usuario_repo_con_datos.contar() == 3  # No cambia
```

#### Paso 4: Reto - Tests Parametrizados (10 min)

Agregar tests parametrizados para validar diferentes escenarios:

```python
@pytest.mark.parametrize("username,email,esperado", [
    ("valid", "valid@example.com", True),
    ("ab", "valid@example.com", False),  # Username muy corto
    ("valid", "invalido", False),  # Email inválido
])
def test_validacion_usuario(usuario_repo_vacio, username, email, esperado):
    """Test validación de usuario con parámetros."""
    from taskflow.models.usuario import Usuario

    usuario = Usuario(username=username, email=email, password_hash="hash123")
    assert usuario.es_valido() == esperado
```

### 4. Entregables

- [ ] `src/taskflow/repositories/base.py` con interfaz genérica
- [ ] `src/taskflow/repositories/usuario_repo.py` con implementación
- [ ] `tests/conftest.py` con fixtures
- [ ] `tests/test_repositories/test_usuario_repo.py` con tests completos
- [ ] Todos los tests pasando
- [ ] Coverage > 90%

---

## Taller 2.7: Servicios con TDD

**Unidad:** 2 - Técnicas de Desarrollo
**Clase:** 2.7 - Evaluación 2
**Duración:** 120 minutos
**Formato:** Parejas + Sustentación
**Entregable:** Servicios del sistema con tests completos

### 1. Objetivos

- [ ] Aplicar TDD sistemáticamente
- [ ] Implementar servicios con lógica de negocio
- [ ] Usar mocks para aislar dependencias
- [ ] Escribir tests antes que código

### 2. Contexto

Los servicios contienen la lógica de negocio del dominio. Deben:
- Ser independientes de la infraestructura
- Usar repositorios para persistencia
- Manejar errores apropiadamente
- Ser testables en aislamiento

### 3. Paso a Paso (Ciclo R-G-R)

#### Iteración 1: Método crear_usuario

**RED (5 min):**

```python
# tests/test_services/test_usuario_service.py

def test_crear_usuario_exitoso(usuario_service):
    """Test crear usuario con datos válidos."""
    usuario = usuario_service.crear_usuario(
        username="jdoe",
        email="john@example.com",
        password="SecurePass123"
    )

    assert usuario.id is not None
    assert usuario.username == "jdoe"
    assert usuario.password_hash != "SecurePass123"  # Debe estar hasheado
```

**Ejecutar:** `pytest` → Debe fallar (no existe UsuarioService)

**GREEN (10 min):**

```python
# src/taskflow/services/usuario_service.py

class UsuarioService:
    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def crear_usuario(self, username: str, email: str, password: str):
        # Crear usuario con password hasheado
        import bcrypt
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode(), salt).decode()

        usuario = Usuario(
            username=username,
            email=email,
            password_hash=password_hash
        )

        return self.repo.guardar(usuario)
```

**Ejecutar:** `pytest` → Debe pasar

**REFACTOR (5 min):**

```python
# Extraer lógica de hasheo a método privado
def _hashear_password(self, password: str) -> str:
    import bcrypt
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def crear_usuario(self, username: str, email: str, password: str):
    password_hash = self._hashear_password(password)
    usuario = Usuario(username=username, email=email, password_hash=password_hash)
    return self.repo.guardar(usuario)
```

**Ejecutar:** `pytest` → Debe seguir pasando

#### Iteración 2: Validación de duplicados

**RED (5 min):**

```python
def test_crear_usuario_username_duplicado_falla(usuario_service):
    """Test error al crear usuario con username duplicado."""
    # Crear primer usuario
    usuario_service.crear_usuario(
        username="jdoe",
        email="john1@example.com",
        password="SecurePass123"
    )

    # Intentar crear con mismo username
    with pytest.raises(UsuarioExistenteError):
        usuario_service.crear_usuario(
            username="jdoe",
            email="john2@example.com",
            password="SecurePass456"
        )
```

**GREEN + REFACTOR (10 min):**

```python
def crear_usuario(self, username: str, email: str, password: str):
    # Verificar duplicados
    if self.repo.buscar_por_username(username):
        raise UsuarioExistenteError(f"Username '{username}' ya existe")

    if self.repo.buscar_por_email(email):
        raise UsuarioExistenteError(f"Email '{email}' ya existe")

    # Crear y guardar
    password_hash = self._hashear_password(password)
    usuario = Usuario(username=username, email=email, password_hash=password_hash)
    return self.repo.guardar(usuario)
```

#### Iteración 3: Autenticación

**RED (5 min):**

```python
def test_autenticar_usuario_exitoso(usuario_service, usuario_creado):
    """Test autenticación con credenciales correctas."""
    usuario = usuario_service.autenticar_usuario(
        username="jdoe",
        password="SecurePass123"
    )

    assert usuario is not None
    assert usuario.username == "jdoe"

def test_autenticar_password_incorrecto_falla(usuario_service, usuario_creado):
    """Test error con password incorrecto."""
    with pytest.raises(CredencialesInvalidasError):
        usuario_service.autenticar_usuario(
            username="jdoe",
            password="WrongPassword"
        )
```

**GREEN + REFACTOR (15 min):**

```python
def autenticar_usuario(self, username: str, password: str) -> Usuario:
    # Buscar usuario
    usuario = self.repo.buscar_por_username(username)

    if not usuario:
        raise CredencialesInvalidasError("Credenciales inválidas")

    # Verificar password
    if not self._verificar_password(password, usuario.password_hash):
        raise CredencialesInvalidasError("Credenciales inválidas")

    # Verificar estado
    if not usuario.esta_activo():
        raise UsuarioServiceError("Usuario no está activo")

    return usuario

def _verificar_password(self, password: str, password_hash: str) -> bool:
    import bcrypt
    return bcrypt.checkpw(password.encode(), password_hash.encode())
```

### 4. Tests con Mocks

```python
from unittest.mock import Mock

def test_usuario_service_usa_repo_correctamente():
    """Test que el servicio usa el repo apropiadamente."""
    # Crear mock del repo
    mock_repo = Mock()
    mock_repo.buscar_por_username.return_value = None
    mock_repo.buscar_por_email.return_value = None
    mock_repo.guardar.return_value = Usuario(id=1, username="test", email="test@example.com", password_hash="hash")

    # Crear servicio con mock
    service = UsuarioService(mock_repo)

    # Ejecutar
    service.crear_usuario("test", "test@example.com", "password123")

    # Verificar interacciones
    mock_repo.buscar_por_username.assert_called_once_with("test")
    mock_repo.buscar_por_email.assert_called_once_with("test@example.com")
    mock_repo.guardar.assert_called_once()

    # Verificar que el usuario guardado tiene password hasheado
    usuario_guardado = mock_repo.guardar.call_args[0][0]
    assert usuario_guardado.password_hash != "password123"
```

### 5. Entregables

- [ ] `src/taskflow/services/usuario_service.py` completo
- [ ] `src/taskflow/services/proyecto_service.py` completo
- [ ] `src/taskflow/services/tarea_service.py` completo
- [ ] `tests/test_services/` con tests completos
- [ ] Todos los tests pasando
- [ ] Coverage > 80%

### 6. Sustentación (10 min)

Preparar respuestas para:
- ¿Por qué separaron servicios de repositorios?
- ¿Cómo validaron que el servicio usa el repo correctamente?
- ¿Qué pasó si el repo falla?
- ¿Por qué usaron mocks en lugar del repo real?

---

## Taller 3.5: CRUD API con FastAPI

**Unidad:** 3 - Desarrollo Backend
**Clase:** 3.5 - CRUD completo
**Duración:** 120 minutos
**Formato:** Parejas
**Entregable:** API CRUD completa funcionando

### 1. Objetivos

- [ ] Crear endpoints CRUD completos
- [ ] Usar Pydantic para validación
- [ ] Retornar códigos de estado HTTP correctos
- [ ] Documentar con OpenAPI

### 2. Paso a Paso

#### Paso 1: Setup (10 min)

```bash
# Crear estructura
mkdir -p src/taskflow/api/routes
touch src/taskflow/api/routes/__init__.py
touch src/taskflow/api/routes/proyectos.py
touch src/taskflow/api/routes/tareas.py
```

#### Paso 2: Endpoint GET listar (15 min)

```python
# src/taskflow/api/routes/proyectos.py

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from taskflow.database import get_db
from taskflow.models.proyecto import Proyecto
from taskflow.schemas.proyecto import ProyectoCreate, ProyectoResponse

router = APIRouter(prefix="/proyectos", tags=["Proyectos"])


@router.get("/", response_model=List[ProyectoResponse])
def listar_proyectos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Lista todos los proyectos.

    Args:
        skip: Cantidad a saltar (paginación)
        limit: Cantidad máxima a retornar

    Returns:
        Lista de proyectos
    """
    proyectos = db.query(Proyecto).offset(skip).limit(limit).all()
    return proyectos


@router.get("/{proyecto_id}", response_model=ProyectoResponse)
def obtener_proyecto(
    proyecto_id: int,
    db: Session = Depends(get_db)
):
    """
    Obtiene un proyecto por ID.

    Args:
        proyecto_id: ID del proyecto

    Returns:
        El proyecto solicitado

    Raises:
        HTTPException 404 si no existe
    """
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()

    if not proyecto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proyecto con ID {proyecto_id} no encontrado"
        )

    return proyecto
```

#### Paso 3: Endpoint POST crear (20 min)

```python
@router.post(
    "/",
    response_model=ProyectoResponse,
    status_code=status.HTTP_201_CREATED
)
def crear_proyecto(
    proyecto_data: ProyectoCreate,
    db: Session = Depends(get_db)
):
    """
    Crea un nuevo proyecto.

    Args:
        proyecto_data: Datos del proyecto a crear

    Returns:
        El proyecto creado con ID asignado

    Raises:
        HTTPException 400 si datos inválidos
        HTTPException 404 si usuario no existe
    """
    # Verificar que existe el usuario
    from taskflow.models.usuario import Usuario
    usuario = db.query(Usuario).filter(Usuario.id == proyecto_data.usuario_id).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {proyecto_data.usuario_id} no encontrado"
        )

    # Crear proyecto
    proyecto = Proyecto(**proyecto_data.model_dump())
    db.add(proyecto)
    db.commit()
    db.refresh(proyecto)

    return proyecto
```

#### Paso 4: Endpoints PUT y DELETE (25 min)

```python
@router.put("/{proyecto_id}", response_model=ProyectoResponse)
def actualizar_proyecto(
    proyecto_id: int,
    proyecto_data: ProyectoUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza un proyecto existente.

    Args:
        proyecto_id: ID del proyecto a actualizar
        proyecto_data: Datos a actualizar

    Returns:
        El proyecto actualizado

    Raises:
        HTTPException 404 si no existe
    """
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()

    if not proyecto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proyecto con ID {proyecto_id} no encontrado"
        )

    # Actualizar campos
    update_data = proyecto_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(proyecto, field, value)

    db.commit()
    db.refresh(proyecto)

    return proyecto


@router.delete(
    "/{proyecto_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_proyecto(
    proyecto_id: int,
    db: Session = Depends(get_db)
):
    """
    Elimina un proyecto.

    Args:
        proyecto_id: ID del proyecto a eliminar

    Raises:
        HTTPException 404 si no existe
    """
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()

    if not proyecto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proyecto con ID {proyecto_id} no encontrado"
        )

    db.delete(proyecto)
    db.commit()

    return None  # FastAPI retorna 204 automáticamente
```

#### Paso 5: Tests de API (30 min)

```python
# tests/test_api/test_proyectos.py

import pytest
from fastapi.testclient import TestClient

from taskflow.api.app import create_app
from taskflow.database import get_db
from tests.conftest import TestingSession


@pytest.fixture
def client(db_session):
    """Cliente de prueba FastAPI."""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app = create_app()
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def test_listar_proyectos_vacio(client):
    """Test listar proyectos cuando no hay ninguno."""
    response = client.get("/api/proyectos/")

    assert response.status_code == 200
    assert response.json() == []


def test_crear_proyecto(client, usuario_creado):
    """Test crear un proyecto."""
    data = {
        "nombre": "TaskFlow",
        "descripcion": "Sistema de gestión",
        "usuario_id": usuario_creado.id
    }

    response = client.post("/api/proyectos/", json=data)

    assert response.status_code == 201
    json_resp = response.json()
    assert json_resp["nombre"] == "TaskFlow"
    assert json_resp["id"] is not None


def test_obtener_proyecto_existente(client, proyecto_creado):
    """Test obtener un proyecto existente."""
    response = client.get(f"/api/proyectos/{proyecto_creado.id}")

    assert response.status_code == 200
    json_resp = response.json()
    assert json_resp["id"] == proyecto_creado.id


def test_obtener_proyecto_inexistente(client):
    """Test obtener un proyecto inexistente."""
    response = client.get("/api/proyectos/999")

    assert response.status_code == 404
    assert "no encontrado" in response.json()["detail"]


def test_actualizar_proyecto(client, proyecto_creado):
    """Test actualizar un proyecto."""
    data = {
        "nombre": "TaskFlow v2",
        "descripcion": "Sistema mejorado"
    }

    response = client.put(f"/api/proyectos/{proyecto_creado.id}", json=data)

    assert response.status_code == 200
    json_resp = response.json()
    assert json_resp["nombre"] == "TaskFlow v2"


def test_eliminar_proyecto(client, proyecto_creado):
    """Test eliminar un proyecto."""
    response = client.delete(f"/api/proyectos/{proyecto_creado.id}")

    assert response.status_code == 204

    # Verificar que ya no existe
    response = client.get(f"/api/proyectos/{proyecto_creado.id}")
    assert response.status_code == 404
```

### 3. Reto - Filtros y Búsqueda

Agregar filtros a GET /proyectos/:
- ?estado=activo
- ?usuario_id=1
- ?nombre=TaskFlow (búsqueda parcial)

### 4. Entregables

- [ ] CRUD de proyectos completo
- [ ] CRUD de tareas completo
- [ ] Tests de todos los endpoints
- [ ] Documentación en Swagger (/docs)
- [ ] Todos los tests pasando

---

## Taller 4.3: Formularios con Jinja2 y HTMX

**Unidad:** 4 - Desarrollo Frontend
**Clase:** 4.3 - Formularios y validación
**Duración:** 90 minutos
**Formato:** Parejas
**Entregable:** Formularios funcionales con validación

### 1. Objetivos

- [ ] Crear formularios HTML con Jinja2
- [ ] Implementar validación cliente y servidor
- [ ] Usar HTMX para submit sin recarga
- [ ] Mostrar errores de forma clara

### 2. Paso a Paso

#### Paso 1: Template Base (15 min)

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}TaskFlow{% endblock %}</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
          rel="stylesheet">
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <link rel="stylesheet" href="/static/css/styles.css">

    {% block head %}{% endblock %}
</head>
<body>
    {% include "componentes/navbar.html" %}

    <main class="container my-4">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                <div class="alert alert-{{ category }} alert-dismissible fade show"
                     role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

#### Paso 2: Formulario de Crear Proyecto (25 min)

```html
<!-- templates/proyectos/crear.html -->
{% extends "base.html" %}

{% block title %}Crear Proyecto - TaskFlow{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h2>Crear Nuevo Proyecto</h2>
            </div>
            <div class="card-body">
                <form hx-post="/api/proyectos/"
                      hx-target="#form-container"
                      hx-swap="innerHTML">
                    {% csrf_token %}

                    <div class="mb-3">
                        <label for="nombre" class="form-label">Nombre *</label>
                        <input type="text"
                               class="form-control"
                               id="nombre"
                               name="nombre"
                               required
                               minlength="3"
                               maxlength="100"
                               placeholder="Ej: TaskFlow">
                        <div class="form-text">Mínimo 3 caracteres, máximo 100</div>
                        <div class="invalid-feedback" id="nombre-error"></div>
                    </div>

                    <div class="mb-3">
                        <label for="descripcion" class="form-label">Descripción</label>
                        <textarea class="form-control"
                                  id="descripcion"
                                  name="descripcion"
                                  rows="3"
                                  maxlength="1000"
                                  placeholder="Descripción del proyecto..."></textarea>
                        <div class="form-text">Máximo 1000 caracteres</div>
                        <div class="invalid-feedback" id="descripcion-error"></div>
                    </div>

                    <div class="d-flex justify-content-between">
                        <a href="/proyectos" class="btn btn-secondary">Cancelar</a>
                        <button type="submit" class="btn btn-primary">
                            Crear Proyecto
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<script>
// Validación en tiempo real con HTMX
document.body.addEventListener('htmx:responseError', function(evt) {
    const response = evt.detail.xhr.response;
    const errors = JSON.parse(response);

    // Limpiar errores anteriores
    document.querySelectorAll('.invalid-feedback').forEach(el => {
        el.textContent = '';
    });
    document.querySelectorAll('.is-invalid').forEach(el => {
        el.classList.remove('is-invalid');
    });

    // Mostrar nuevos errores
    for (const [field, message] of Object.entries(errors)) {
        const input = document.getElementById(field);
        const errorDiv = document.getElementById(`${field}-error`);

        if (input && errorDiv) {
            input.classList.add('is-invalid');
            errorDiv.textContent = message;
        }
    }
});

// Redirigir al crear exitosamente
document.body.addEventListener('htmx:afterRequest', function(evt) {
    if (evt.detail.xhr.status === 201) {
        const response = JSON.parse(evt.detail.xhr.response);
        window.location.href = `/proyectos/${response.id}`;
    }
});
</script>
{% endblock %}
```

#### Paso 3: Endpoint con Validación (20 min)

```python
# src/taskflow/api/routes/proyectos.py

from fastapi import HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse

@router.post("/api/proyectos/", response_class=JSONResponse)
async def crear_proyecto_htmx(
    request: Request,
    proyecto_data: ProyectoCreate,
    db: Session = Depends(get_db)
):
    """
    Crea un proyecto desde HTMX.

    Retorna JSON con detalles o errores.
    """
    # Validar usuario
    usuario = db.query(Usuario).filter(Usuario.id == proyecto_data.usuario_id).first()
    if not usuario:
        return JSONResponse(
            status_code=400,
            content={"usuario_id": "Usuario no encontrado"}
        )

    # Validar datos
    errores = {}
    if len(proyecto_data.nombre) < 3:
        errores["nombre"] = "Nombre debe tener al menos 3 caracteres"
    if len(proyecto_data.nombre) > 100:
        errores["nombre"] = "Nombre no puede exceder 100 caracteres"

    if errores:
        return JSONResponse(status_code=400, content=errores)

    # Crear proyecto
    proyecto = Proyecto(**proyecto_data.model_dump())
    db.add(proyecto)
    db.commit()
    db.refresh(proyecto)

    return JSONResponse(
        status_code=201,
        content={
            "id": proyecto.id,
            "nombre": proyecto.nombre,
            "descripcion": proyecto.descripcion
        }
    )
```

#### Paso 4: Formulario con Live Validation (15 min)

```html
<!-- Input con validación en tiempo real -->
<div class="mb-3">
    <label for="nombre" class="form-label">Nombre *</label>
    <input type="text"
           class="form-control"
           id="nombre"
           name="nombre"
           hx-post="/api/validar/nombre"
           hx-trigger="keyup changed delay:500ms"
           hx-target="#nombre-error"
           hx-swap="innerHTML"
           required>
    <div class="invalid-feedback" id="nombre-error"></div>
</div>
```

```python
# Endpoint de validación
@router.post("/api/validar/nombre")
async def validar_nombre(nombre: str = Form(...)):
    """Valida nombre de proyecto en tiempo real."""
    if len(nombre) < 3:
        return "<div class='invalid-feedback show'>Nombre muy corto</div>"
    return ""
```

### 3. Entregables

- [ ] Formulario de crear proyecto funcional
- [ ] Formulario de editar proyecto funcional
- [ ] Formulario de crear tarea funcional
- [ ] Validación cliente y servidor
- [ ] Errores mostrados claramente
- [ ] Submit con HTMX sin recarga

---

## Taller 4.7: Interfaz Completa del Sistema

**Unidad:** 4 - Desarrollo Frontend
**Clase:** 4.7 - Evaluación 4
**Duración:** 180 minutos
**Formato:** Parejas + Sustentación
**Entregable:** Interfaz web completa funcionando

### 1. Objetivos

- [ ] Integrar todos los componentes del frontend
- [ ] Implementar navegación completa
- [ ] Crear dashboard con estadísticas
- [ ] Asegurar experiencia de usuario fluida

### 2. Checklist de Funcionalidades

#### Autenticación
- [ ] Login con username/password
- [ ] Registro de nuevo usuario
- [ ] Logout
- [ ] Protección de rutas privadas

#### Proyectos
- [ ] Lista de proyectos
- [ ] Crear nuevo proyecto
- [ ] Ver detalles de proyecto
- [ ] Editar proyecto
- [ ] Eliminar proyecto
- [ ] Ver tareas del proyecto

#### Tareas
- [ ] Lista de tareas de un proyecto
- [ ] Crear nueva tarea
- [ ] Editar tarea
- [ ] Cambiar estado (pendiente → en progreso → completada)
- [ ] Asignar a usuario
- [ ] Agregar comentarios

#### Dashboard
- [ ] Estadísticas generales
- [ ] Proyectos recientes
- [ ] Mis tareas pendientes
- [ ] Gráficos de progreso

### 3. Estructura de Templates

```
templates/
├── base.html
├── index.html
├── auth/
│   ├── login.html
│   └── registro.html
├── dashboard.html
├── proyectos/
│   ├── lista.html
│   ├── crear.html
│   ├── detalle.html
│   └── editar.html
├── tareas/
│   ├── lista.html
│   ├── crear.html
│   └── editar.html
└── componentes/
    ├── navbar.html
    ├── footer.html
    ├── tarjeta_proyecto.html
    └── tarjeta_tarea.html
```

### 4. Ejemplos de Componentes

#### tarjeta_proyecto.html

```html
<!-- templates/componentes/tarjeta_proyecto.html -->
<div class="card proyecto-card mb-3" hx-target="#proyecto-{{ proyecto.id }}">
    <div class="card-header d-flex justify-content-between align-items-center">
        <h5 class="mb-0">{{ proyecto.nombre }}</h5>
        <span class="badge bg-{{ 'success' if proyecto.estado == 'activo' else 'secondary' }}">
            {{ proyecto.estado }}
        </span>
    </div>
    <div class="card-body">
        <p class="text-muted mb-2">{{ proyecto.descripcion[:100] }}...</p>

        <div class="d-flex justify-content-between align-items-center">
            <small class="text-muted">
                <i class="bi bi-calendar"></i> {{ proyecto.creado_en.strftime('%d/%m/%Y') }}
            </small>
            <div class="btn-group btn-group-sm">
                <a href="/proyectos/{{ proyecto.id }}"
                   class="btn btn-outline-primary">
                    Ver
                </a>
                <button class="btn btn-outline-secondary"
                        hx-get="/proyectos/{{ proyecto.id }}/editar"
                        hx-push-url="true">
                    Editar
                </button>
            </div>
        </div>
    </div>
</div>
```

### 5. Validación Final

**Test Manual de Usuario:**

1. **Login**
   - [ ] Puedo iniciar sesión con credenciales válidas
   - [ ] Muestro error con credenciales inválidas
   - [ ] Soy redirigido al dashboard después de login

2. **Crear Proyecto**
   - [ ] Puedo crear un proyecto con datos válidos
   - [ ] Muestro errores con datos inválidos
   - [ ] El proyecto aparece en la lista después de crear

3. **Ver Tareas**
   - [ ] Veo las tareas de un proyecto
   - [ ] Puedo crear una nueva tarea
   - [ ] Puedo cambiar el estado de una tarea

4. **Dashboard**
   - [ ] Veo estadísticas correctas
   - [ ] Veo mis proyectos recientes
   - [ ] Veo mis tareas pendientes

### 6. Entregables

- [ ] Todos los templates creados
- [ ] Navegación completa funcional
- [ ] Dashboard con estadísticas
- [ ] Validaciones en todos los formularios
- [ ] Feedback visual para todas las acciones
- [ ] Diseño responsivo (móvil, tablet, desktop)
- [ ] Sin errores de JavaScript en consola

### 7. Sustentación (15 min)

**Demo en vivo (8 min):**
1. Login al sistema
2. Crear un proyecto
3. Crear tareas
4. Cambiar estados
5. Ver dashboard
6. Mostrar algún detalle técnico

**Preguntas preparadas:**
- ¿Cómo manejan la validación de formularios?
- ¿Qué pasa si falla una petición HTMX?
- ¿Cómo aseguran que el usuario ve los datos actualizados?
- ¿Qué fue lo más difícil de implementar?
- ¿Cómo mejorarían la UX?

---

## Taller 5.3: Preparación para Sustentación

**Unidad:** 5 - Proyecto Final
**Clase:** 5.3 - Preparación para sustentación
**Duración:** 90 minutos
**Formato:** Individual
**Entregable:** Presentación lista

### 1. Objetivos

- [ ] Crear presentación profesional
- [ ] Preparar demo del sistema
- [ ] Anticipar preguntas del docente
- [ ] Ensayar presentación completa

### 2. Estructura de Presentación (10-15 min)

#### Slide 1: Título (30 seg)
```
TaskFlow - Sistema de Gestión de Proyectos y Tareas

[Nombre del Estudiante]
IF0100 - Lenguaje de Programación Orientado a Objetos II
UNAULA - 2026-I
```

#### Slide 2: Arquitectura (1-2 min)
```
ARQUITECTURA DEL SISTEMA

┌─────────────────────────────────────────┐
│           Frontend Layer                │
│  Jinja2 Templates + HTMX + Bootstrap 5  │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│            API Layer                    │
│         FastAPI + Pydantic              │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│         Service Layer                   │
│      Lógica de Negocio                  │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│      Repository Layer                   │
│    SQLAlchemy ORM + PostgreSQL          │
└─────────────────────────────────────────┘

TECNOLOGÍAS:
• Backend: Python 3.12, FastAPI, SQLAlchemy
• Frontend: Jinja2, HTMX, Bootstrap 5
• Base de Datos: PostgreSQL 15
• Testing: pytest, pytest-cov
```

#### Slide 3: Características Principales (1 min)
```
CARACTERÍSTICAS IMPLEMENTADAS

Autenticación y Autorización
✓ Login/Registro con JWT
✓ Gestión de sesiones
✓ Protección de rutas

Gestión de Proyectos
✓ CRUD completo
✓ Validaciones
✓ Estados (activo, archivado, completado)

Gestión de Tareas
✓ Creación dentro de proyectos
✓ Asignación a usuarios
✓ Cambio de estado
✓ Comentarios

Dashboard
✓ Estadísticas en tiempo real
✓ Proyectos recientes
✓ Tareas pendientes
```

#### Slide 4: Patrones Aplicados (1 min)
```
PATRONES DE DISEÑO APLICADOS

Domain-Driven Design (DDD)
• Entidades y Value Objects
• Servicios con lógica de negocio
• Repositorios para persistencia

Repository Pattern
• Abstracción de persistencia
• Implementación en memoria para tests
• SQLAlchemy para producción

Dependency Injection
• Inyección de repositorios en servicios
• Inyección de dependencias de FastAPI

Data Transfer Objects (DTO)
• Schemas Pydantic para request/response
• Validación automática
• Serialización/deserialización

Test-Driven Development (TDD)
• Ciclo Red-Green-Refactor
• Coverage > 80%
• Tests unitarios, integración, E2E
```

#### Slide 5: Código Destacado (2 min)
```
EJEMPLO: Servicio con TDD

[Mostrar código de UsuarioService]

Puntos clave:
• Validaciones completas
• Manejo de errores específicos
• Password hasheado con bcrypt
• Tests antes que implementación
```

#### Slide 6: Desafíos y Soluciones (1 min)
```
DESAFÍOS ENCONTRADOS

1. Transición Notebooks → VSCode
   Solución: Progresión gradual con guía del docente

2. TDD al principio
   Solución: Practicar con ejercicios simples primero

3. Validación HTMX
   Solución: Combinar validación cliente con servidor

4. Tests de API
   Solución: Usar TestClient y fixtures reutilizables
```

#### Slide 7: Métricas del Proyecto (1 min)
```
MÉTRICAS DE CALIDAD

Código
• ~2,000 líneas de código Python
• Type hints en 100% de funciones
• Docstrings en 90% de funciones
• PEP 8 compliance

Tests
• 150+ tests escritos
• 85% coverage
• Tests unitarios, integración, E2E
• Todos pasando ✓

Documentación
• README completo
• API documentada con OpenAPI
• Diagramas de arquitectura
• Guías de uso
```

#### Slide 8: Lo Más Proud (1 min)
```
LO MÁS PROUD DE MI PROYECTO

• [Mencionar 2-3 cosas destacadas]

Ejemplos:
- "La arquitectura limpia que logramos"
- "Los tests que nos salvaron varias veces"
- "La UX fluida con HTMX"
- "El dashboard con estadísticas en tiempo real"
```

#### Slide 9: Aprendizajes (1 min)
```
PRINCIPALES APRENDIZAJES

Técnicos
• POO aplicado a un proyecto real
• TDD como práctica diaria
• FastAPI y Python moderno
• Desarrollo frontend sin frameworks JS

Personales
• Persistencia frente a problemas difíciles
• Valor de escribir tests primero
• Importancia de arquitectura limpia
• Colaboración efectiva en parejas
```

#### Slide 10: Próximos Pasos (30 seg)
```
PRÓXIMOS PASOS

Corto Plazo
• [Mejora 1]
• [Mejora 2]

Largo Plazo
• [Característica futura 1]
• [Característica futura 2]

¡GRACIAS!
PREGUNTAS?
```

### 3. Preparación del Demo (5 min)

**Script de Demo:**

```
1. "Voy a mostrar el sistema funcionando..."
2. "Primero, inicio sesión..." [demostrar login]
3. "Ahora veo el dashboard..." [mostrar estadísticas]
4. "Voy a crear un nuevo proyecto..." [crear proyecto]
5. "Dentro del proyecto, creo una tarea..." [crear tarea]
6. "Puedo cambiar el estado de la tarea..." [cambiar estado]
7. "También puedo agregar comentarios..." [agregar comentario]
8. "Finalmente, muestro las estadísticas actualizadas..." [dashboard]
```

### 4. Preguntas Anticipadas

**Preparar respuestas para:**

| Pregunta | Respuesta Preparada |
|----------|---------------------|
| ¿Por qué HTMX en lugar de React? | [Razón: simplicidad, Python-only, curva de aprendizaje] |
| ¿Cómo manejan concurrencia? | [Explicar: PostgreSQL transacciones, SQLAlchemy] |
| ¿Qué pasaría si el repo falla? | [Explicar: excepciones, manejo de errores] |
| ¿Cómo escalaría esto? | [Explicar: cache, Redis, separación de servicios] |
| ¿Qué le cambiaría al código? | [Ser honesto: mencione 2-3 mejoras] |
| ¿Cuánto tiempo tardaron? | [Estimación realista por componente] |
| ¿Qué fue lo más difícil? | [Ser específico con un ejemplo] |

### 5. Checklist Final

**Antes de la sustentación:**
- [ ] Presentación lista y revisada
- [ ] Demo ensayado 3+ veces
- [ ] Sistema corriendo sin errores
- [ ] Datos de prueba preparados
- [ ] Backup del proyecto en Git
- [ ] README actualizado
- [ ] Documentación completa

**Día de la sustentación:**
- [ ] Llegar 10 min antes
- [ ] Tener sistema corriendo
- [ ] Tener presentación abierta
- [ ] Agua y respiración profunda
- [ ] ¡Confianza!

### 6. Consejos para la Sustentación

1. **Muestre orgullo:** Usted construyó un sistema completo
2. **Sea honesto:** Si no sabe algo, diga "no lo consideré"
3. **Muestre el código:** Tenga snippets preparados
4. **Demo fluida:** Ensaye el demo hasta que sea natural
5. **Respire:** Es una conversación, no un interrogatorio

---

## Anexo: Recursos Adicionales

### A. Comandos Útiles

```bash
# Ejecutar tests con coverage
pytest --cov=src/taskflow --cov-report=html

# Ejecutar tests de un archivo específico
pytest tests/test_services/test_usuario_service.py -v

# Ejecutar servidor FastAPI con reload
uvicorn taskflow.main:app --reload --port 8000

# Ver documentación de OpenAPI
# Ir a http://localhost:8000/docs

# Formatear código con black
black src/taskflow tests/

# Verificar PEP 8 con flake8
flake8 src/taskflow tests/
```

### B. Estructura de Tests

```python
"""
Plantilla para test file.
"""

import pytest
from taskflow.models import Modelo


class TestModeloCrear:
    """Tests para crear modelo."""

    def test_crear_exitoso(self):
        """Test crear con datos válidos."""
        # Arrange
        data = {...}

        # Act
        resultado = Modelo.crear(data)

        # Assert
        assert resultado.id is not None

    def test_crear_falla_con_datos_invalidos(self):
        """Test crear con datos inválidos."""
        with pytest.raises(ValueError):
            Modelo.crear({...})


class TestModeloActualizar:
    """Tests para actualizar modelo."""

    def test_actualizar_exitoso(self):
        """Test actualizar con datos válidos."""
        pass

    def test_actualizar_falla_con_datos_invalidos(self):
        """Test actualizar con datos inválidos."""
        pass
```

### C. Troubleshooting Común

| Problema | Solución |
|----------|----------|
| Tests fallan con ImportError | Verificar PYTHONPATH y __init__.py |
| FastAPI no encuentra templates | Verificar config de templates_dir |
| HTMX no actualiza DOM | Verificar hx-target y hx-swap |
| Base de datos no conecta | Verificar que PostgreSQL está corriendo |
| Coverage bajo | Agregar tests para branches faltantes |

---

**Fin de Documento**

**Próxima actualización:** Post-implementación de cada taller
