# Progresión Técnica - IF0100 POO II

**Versión:** 1.0
**Fecha:** 2026-02-07
**Curso:** IF0100 - Lenguaje de Programación Orientado a Objetos II

---

## 1. Visión General

La progresión técnica del curso está diseñada para llevar a los estudiantes desde un nivel básico de Python hasta la construcción de un sistema completo en producción, siguiendo una curva de aprendizaje gradual:

```
Notebooks Interactivos → Python en VSCode → Backend FastAPI → Frontend Jinja2 → Sistema Completo
      (Semana 1-2)           (Semana 3-9)         (Semana 10-12)    (Semana 13-15)      (Semana 16-17)
```

---

## 2. Fase 1: Notebooks Interactivos (Semana 1-2)

### 2.1 Objetivo de la Fase

Introducir conceptos de Python en un ambiente de baja fricción donde los estudiantes pueden experimentar y recibir feedback inmediato.

### 2.2 Características

- **Ejecución celular:** Código en celdas individuales
- **Feedback visual:** Salidas inmediatas después de cada celda
- **Documentación integrada:** Markdown y código mezclados
- **Experimentación:** Fácil probar y modificar código
- **Baja ansiedad:** No hay "compilación" ni archivos que gestionar

### 2.3 Ejemplo de Notebook - Unidad 0.1

```python
# %% [markdown]
"""
# Clase 0.1 - Introducción a Python

## Objetivos
- [ ] Comprender variables y tipos
- [ ] Usar operadores aritméticos
- [ ] Aplicar input/output
"""

# %% [markdown]
"""
## 1. Variables y Tipos de Datos

En Python, las variables se crean asignando un valor. No necesitas declarar el tipo.

**Tipos básicos:**
- `int`: Números enteros (5, -10, 1000)
- `float`: Números decimales (3.14, -0.5, 2.0)
- `str`: Cadenas de texto ("Hola", 'Mundo')
- `bool`: Valores lógicos (True, False)
"""

# %% [markdown]
"""
### Ejemplo 1.1: Creación de Variables
"""

# Código ejecutable - El estudiante puede ejecutar y ver el resultado
nombre = "Juan"
edad = 25
altura = 1.75
estudiante = True

print(f"Nombre: {nombre}, tipo: {type(nombre)}")
print(f"Edad: {edad}, tipo: {type(edad)}")
print(f"Altura: {altura}, tipo: {type(altura)}")
print(f"Estudiante: {estudiante}, tipo: {type(estudiante)}")

# %% [markdown]
"""
### Ejercicio 1.1

Crea variables para:
- Tu nombre (str)
- Tu edad (int)
- Tu altura en metros (float)
- Si eres estudiante (bool)

Luego imprime todas las variables.
"""

# Espacio para el estudiante
tu_nombre = ""
tu_edad = 0
tu_altura = 0.0
tu_estudiante = False

# Escribe tu código aquí


# %% [markdown]
"""
### Validación Automática

Ejecuta esta celda para verificar tu solución:
"""

def validar_ejercicio_1():
    assert isinstance(tu_nombre, str) and len(tu_nombre) > 0, "tu_nombre debe ser un string no vacío"
    assert isinstance(tu_edad, int) and tu_edad > 0, "tu_edad debe ser un entero positivo"
    assert isinstance(tu_altura, float) and tu_altura > 0, "tu_altura debe ser un float positivo"
    assert isinstance(tu_estudiante, bool), "tu_estudiante debe ser un booleano"
    print("¡ Todos los tests pasaron!")

try:
    validar_ejercicio_1()
except AssertionError as e:
    print(f"Error: {e}")
```

### 2.4 Ejemplo de Notebook - Unidad 1.1 (POO)

```python
# %% [markdown]
"""
# Clase 1.1 - Clases y Objetos en Python

## Objetivos
- [ ] Definir clases usando dataclasses
- [ ] Crear instancias de objetos
- [ ] Implementar métodos de instancia
- [ ] Aplicar al proyecto TaskFlow
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

# %% [markdown]
"""
## 1. Definiendo Clases con Dataclasses

Python 3.7+ introduce `@dataclass`, que automáticamente genera:
- `__init__`: Constructor
- `__repr__`: Representación para debugging
- `__eq__`: Comparación de igualdad
"""

# %% [markdown]
"""
### Ejemplo 1.1: Clase Usuario (Proyecto TaskFlow)

Creamos la clase base para usuarios del sistema.
"""

@dataclass
class Usuario:
    """
    Representa un usuario en el sistema TaskFlow.

    Attributes:
        id: Identificador único (None para nuevos usuarios)
        username: Nombre de usuario único
        email: Correo electrónico único
        nombre_completo: Nombre completo del usuario
    """
    id: Optional[int] = None
    username: str = ""
    email: str = ""
    nombre_completo: Optional[str] = None
    creado_en: Optional[datetime] = None

    def es_valido(self) -> bool:
        """Verifica si el usuario es válido."""
        return len(self.validar()) == 0

    def validar(self) -> list[str]:
        """Retorna lista de errores de validación."""
        errores = []

        if not self.username or len(self.username) < 3:
            errores.append("Username debe tener al menos 3 caracteres")

        if not self.email or "@" not in self.email:
            errores.append("Email inválido")

        return errores

# %% [markdown]
"""
### Ejemplo 1.2: Creación de Instancias
"""

# Crear un nuevo usuario
usuario = Usuario(
    username="jdoe",
    email="john@example.com",
    nombre_completo="John Doe"
)

print(f"Usuario creado: {usuario}")
print(f"¿Es válido? {usuario.es_valido()}")
print(f"Errores: {usuario.validar()}")

# %% [markdown]
"""
### Ejercicio 1.1

Completa la clase `Proyecto` siguiendo el mismo patrón que `Usuario`.

Requisitos:
1. Campos: id, nombre, descripcion, usuario_id, creado_en
2. Método validar(): nombre debe tener al menos 3 caracteres
3. Método es_valido(): retorna True si validar() retorna lista vacía
"""

# Espacio para tu solución
@dataclass
class Proyecto:
    """Representa un proyecto en TaskFlow."""
    id: Optional[int] = None
    nombre: str = ""
    descripcion: str = ""
    usuario_id: Optional[int] = None
    creado_en: Optional[datetime] = None

    def es_valido(self) -> bool:
        # TODO: Implementar
        pass

    def validar(self) -> list[str]:
        # TODO: Implementar
        pass

# %% [markdown]
"""
### Validación
"""

def validar_proyecto():
    # Test 1: Proyecto válido
    p1 = Proyecto(nombre="TaskFlow", descripcion="Sistema de tareas", usuario_id=1)
    assert p1.es_valido(), "Test 1 falló: Proyecto válido marcado como inválido"

    # Test 2: Proyecto con nombre corto
    p2 = Proyecto(nombre="AB", descripcion="Descripción", usuario_id=1)
    assert not p2.es_valido(), "Test 2 falló: Proyecto con nombre corto marcado como válido"
    assert "al menos 3 caracteres" in p2.validar()[0], "Test 2 falló: Mensaje de error incorrecto"

    print("¡Todos los tests pasaron!")

try:
    validar_proyecto()
except AssertionError as e:
    print(f"Error: {e}")
```

### 2.5 Ventajas de esta Fase

| Aspecto | Beneficio |
|---------|-----------|
| **Baja fricción** | Los estudiantes no se preocupan por archivos, módulos, o configuración |
| **Feedback inmediato** | Ven el resultado de cada línea de código al instante |
| **Experimentación** | Pueden probar diferentes valores y ver qué pasa |
| **Seguridad psicológica** | El código "roto" no rompe nada, solo arroja un error en la celda |
| **Documentación viva** | La explicación está al lado del código |

### 2.6 Desventajas y Mitigación

| Desventaja | Mitigación |
|------------|------------|
| No es código de producción | Transición gradual a VSCode desde semana 3 |
| Los estudiantes pueden ejecutar desordenadamente | Guías de ejecución ordenada de celdas |
| Difícil de versionar con Git | Explicar que notebooks son para aprendizaje, no para proyecto |

---

## 3. Fase 2: Transición Notebooks → VSCode (Semana 3-6)

### 3.1 Objetivo de la Fase

Mantener la familiaridad de los notebooks mientras introducen gradualmente conceptos de desarrollo profesional.

### 3.2 Estrategia de Transición

**Semana 3-4 (Clases 1.1 - 1.4):**
- 70% Notebook + 30% VSCode
- Aprenden concepto en notebook
- Copian código clave a módulos Python
- Comienzan a organizar en paquetes

**Semana 5-6 (Clases 1.5 - 1.7):**
- 40% Notebook + 60% VSCode
- Notebooks para exploración rápida
- VSCode para código del proyecto
- Tests con pytest en VSCode

### 3.3 Ejemplo de Transición - Clase 1.1

**Paso 1: Explorar en Notebook**

```python
# En notebook 01-01-clases-objetos.ipynb

# %% [markdown]
"""
## Exploración: Clases en Python

Primero, experimentamos con clases en el notebook.
"""

@dataclass
class Usuario:
    username: str
    email: str

    def saludar(self):
        return f"Hola, soy {self.username}"

# Experimentar
u = Usuario(username="test", email="test@example.com")
print(u.saludar())
```

**Paso 2: Copiar a Módulo Python**

```python
# En src/taskflow/models/usuario.py

"""
Módulo: Modelo de Usuario
Unidad: 1.1 - Clases y Objetos
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    """
    Representa un usuario en el sistema TaskFlow.

    Este modelo será usado en toda la aplicación.
    """

    id: Optional[int] = None
    username: str = ""
    email: str = ""
    nombre_completo: Optional[str] = None

    def saludar(self) -> str:
        """Retorna un saludo del usuario."""
        return f"Hola, soy {self.username}"

    def validar(self) -> list[str]:
        """Valida los campos del usuario."""
        errores = []

        if not self.username or len(self.username) < 3:
            errores.append("Username debe tener al menos 3 caracteres")

        if not self.email or "@" not in self.email:
            errores.append("Email inválido")

        return errores

    def es_valido(self) -> bool:
        """Verifica si el usuario es válido."""
        return len(self.validar()) == 0
```

**Paso 3: Usar el Módulo**

```python
# En tests/test_models.py

from taskflow.models.usuario import Usuario

def test_creacion_usuario():
    """Test crear usuario básico."""
    usuario = Usuario(username="jdoe", email="john@example.com")
    assert usuario.username == "jdoe"
    assert usuario.email == "john@example.com"
    assert usuario.saludar() == "Hola, soy jdoe"

def test_validacion_usuario():
    """Test validación de usuario."""
    usuario = Usuario(username="ab", email="invalido")
    assert not usuario.es_valido()
    assert len(usuario.validar()) == 2
```

### 3.4 Ejemplo de Progresión - Clases 1.1 a 1.6

| Clase | Notebook (Exploración) | VSCode (Producción) | Proporción |
|-------|------------------------|---------------------|-----------|
| **1.1** | Clases y objetos básicos | Crear `models/usuario.py` | 70/30 |
| **1.2** | Propiedades con @property | Agregar propiedades a modelos | 70/30 |
| **1.3** | Herencia simple | Crear `models/base.py` con Entity | 60/40 |
| **1.4** | Métodos mágicos | Implementar `__str__`, `__repr__` | 60/40 |
| **1.5** | ABCs y Protocolos | Crear `repositories/base.py` | 50/50 |
| **1.6** | Pydantic schemas | Crear schemas del proyecto | 40/60 |

### 3.5 Estructura de Archivos (Semana 6)

```
taskflow/
├── notebooks/                      # Notebooks de aprendizaje
│   ├── unidad-01/
│   │   ├── 01-01-clases-objetos.ipynb
│   │   ├── 01-02-encapsulamiento.ipynb
│   │   └── ...
│   └── unidad-02/
│       └── (notebooks de TDD)
│
├── src/taskflow/                   # Código del proyecto
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py                 # Entity base (clase 1.3)
│   │   ├── usuario.py              # Usuario (clase 1.1)
│   │   ├── proyecto.py             # Proyecto (clase 1.1)
│   │   └── tarea.py                # Tarea (clase 1.3)
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── base.py                 # IRepository (clase 1.5)
│   │   └── usuario_repo.py         # Implementación (clase 1.6)
│   └── schemas/
│       ├── __init__.py
│       └── usuario.py              # Schemas Pydantic (clase 1.6)
│
├── tests/                          # Tests del proyecto
│   ├── __init__.py
│   ├── conftest.py                 # Fixtures (clase 2.3)
│   ├── test_models.py              # Tests de modelos
│   └── test_repositories.py        # Tests de repos
│
├── requirements.txt                # Dependencias
├── pytest.ini                      # Config de pytest
└── README.md                       # Documentación
```

---

## 4. Fase 3: VSCode Puro (Semana 7-15)

### 4.1 Objetivo de la Fase

Desarrollar habilidades profesionales de ingeniería de software usando herramientas de producción.

### 4.2 Transición Completa

**Semana 7-9 (Unidad 2):**
- 100% VSCode para código del proyecto
- Notebooks solo para demos rápidas
- pytest para todos los tests
- Git para control de versiones

**Semana 10-15 (Unidades 3-4):**
- 100% VSCode
- FastAPI para backend
- Jinja2/HTMX para frontend
- Docker para PostgreSQL

### 4.3 Ejemplo de Código - Semana 8 (Unidad 2)

**models/usuario.py (Producción)**

```python
"""
Módulo: Modelo de Usuario
Unidad: 1-2 - POO Avanzada
Actualizado: Clase 2.6 - Servicios y Repositorios
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum


class EstadoUsuario(Enum):
    """Estados posibles de un usuario."""
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    SUSPENDIDO = "suspendido"


@dataclass
class Usuario:
    """
    Representa un usuario en el sistema TaskFlow.

    Esta es la entidad de dominio principal para autenticación
    y gestión de usuarios. Contiene toda la lógica de negocio
    relacionada con usuarios.

    Attributes:
        id: Identificador único (None para nuevos usuarios)
        username: Nombre de usuario único, 3-50 caracteres
        email: Correo electrónico único y válido
        password_hash: Hash bcrypt del password (nunca texto plano)
        nombre_completo: Nombre completo del usuario
        estado: Estado actual del usuario (default: ACTIVO)
        creado_en: Fecha de creación (auto)
        actualizado_en: Fecha de última actualización (auto)

    Example:
        >>> usuario = Usuario(
        ...     username="jdoe",
        ...     email="john@example.com",
        ...     password_hash="$2b$12$..."
        ... )
        >>> usuario.es_valido()
        True
    """

    id: Optional[int] = None
    username: str = ""
    email: str = ""
    password_hash: str = ""
    nombre_completo: Optional[str] = None
    estado: EstadoUsuario = EstadoUsuario.ACTIVO
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    def validar(self) -> list[str]:
        """
        Valida todos los campos del usuario.

        Returns:
            Lista de mensajes de error. Vacía si es válido.

        Validation Rules:
            - Username: 3-50 caracteres, alfanuméricos y guiones
            - Email: Formato válido de email
            - Password: Debe tener hash (no vacío)
        """
        errores: list[str] = []

        # Validar username
        if not self.username:
            errores.append("Username es requerido")
        elif len(self.username) < 3:
            errores.append("Username debe tener al menos 3 caracteres")
        elif len(self.username) > 50:
            errores.append("Username no puede exceder 50 caracteres")
        elif not self.username.replace("-", "").replace("_", "").isalnum():
            errores.append("Username solo puede contener letras, números, guiones y guiones bajos")

        # Validar email
        if not self.email:
            errores.append("Email es requerido")
        elif "@" not in self.email or "." not in self.email.split("@")[1]:
            errores.append("Email inválido")

        # Validar password
        if not self.password_hash:
            errores.append("Password es requerido")

        return errores

    def es_valido(self) -> bool:
        """Verifica si el usuario pasa todas las validaciones."""
        return len(self.validar()) == 0

    def esta_activo(self) -> bool:
        """Verifica si el usuario está en estado ACTIVO."""
        return self.estado == EstadoUsuario.ACTIVO

    def puede_iniciar_sesion(self) -> bool:
        """Verifica si el usuario puede iniciar sesión."""
        return self.esta_activo() and self.es_valido()

    def __str__(self) -> str:
        """Representación string amigable."""
        nombre = self.nombre_completo or self.username
        return f"Usuario({nombre})"

    def __repr__(self) -> str:
        """Representación para debugging."""
        return (
            f"Usuario(id={self.id}, username='{self.username}', "
            f"email='{self.email}', estado={self.estado.value})"
        )

    def __eq__(self, other) -> bool:
        """Compara usuarios por ID."""
        if not isinstance(other, Usuario):
            return False
        return self.id == other.id if self.id and other.id else self.username == other.username
```

**services/usuario_service.py (Unidad 2)**

```python
"""
Módulo: Servicio de Usuarios
Unidad: 2.6 - DDD: Servicios y Repositorios

Este servicio contiene la lógica de negocio relacionada con usuarios.
Separa el dominio de la infraestructura.
"""

from typing import Optional, List
from datetime import datetime

from taskflow.models.usuario import Usuario, EstadoUsuario
from taskflow.repositories.usuario_repo import UsuarioRepository
from taskflow.repositories.base import RepositoryError


class UsuarioServiceError(Exception):
    """Excepción base para errores del servicio."""
    pass


class UsuarioExistenteError(UsuarioServiceError):
    """Error cuando el usuario ya existe."""
    pass


class CredencialesInvalidasError(UsuarioServiceError):
    """Error cuando las credenciales son inválidas."""
    pass


class UsuarioService:
    """
    Servicio para gestión de usuarios.

    Este servicio implementa la lógica de negocio del dominio,
    utilizando repositorios para la persistencia.

    Attributes:
        repo: Repositorio de usuarios a utilizar

    Example:
        >>> repo = UsuarioRepository(db_session)
        >>> service = UsuarioService(repo)
        >>> usuario = service.crear_usuario(
        ...     username="jdoe",
        ...     email="john@example.com",
        ...     password="securepass123"
        ... )
    """

    def __init__(self, repo: UsuarioRepository):
        """
        Inicializa el servicio con un repositorio.

        Args:
            repo: Repositorio de usuarios a utilizar
        """
        self.repo = repo

    def crear_usuario(
        self,
        username: str,
        email: str,
        password: str,
        nombre_completo: Optional[str] = None
    ) -> Usuario:
        """
        Crea un nuevo usuario en el sistema.

        Args:
            username: Nombre de usuario único
            email: Correo electrónico único
            password: Password en texto plano (será hasheado)
            nombre_completo: Nombre completo (opcional)

        Returns:
            El usuario creado con ID asignado

        Raises:
            UsuarioExistenteError: Si username o email ya existen
            UsuarioServiceError: Si hay error de validación
        """
        # Verificar si ya existe
        existente = self.repo.buscar_por_username(username)
        if existente:
            raise UsuarioExistenteError(f"Username '{username}' ya existe")

        existente = self.repo.buscar_por_email(email)
        if existente:
            raise UsuarioExistenteError(f"Email '{email}' ya existe")

        # Crear usuario
        password_hash = self._hashear_password(password)
        usuario = Usuario(
            username=username,
            email=email,
            password_hash=password_hash,
            nombre_completo=nombre_completo,
            estado=EstadoUsuario.ACTIVO,
            creado_en=datetime.now()
        )

        # Validar
        if not usuario.es_valido():
            errores = ", ".join(usuario.validar())
            raise UsuarioServiceError(f"Usuario inválido: {errores}")

        # Guardar
        try:
            return self.repo.guardar(usuario)
        except RepositoryError as e:
            raise UsuarioServiceError(f"Error al guardar usuario: {e}")

    def autenticar_usuario(self, username: str, password: str) -> Usuario:
        """
        Autentica un usuario con credenciales.

        Args:
            username: Nombre de usuario
            password: Password en texto plano

        Returns:
            El usuario autenticado

        Raises:
            CredencialesInvalidasError: Si las credenciales son incorrectas
            UsuarioServiceError: Si el usuario no puede iniciar sesión
        """
        usuario = self.repo.buscar_por_username(username)

        if not usuario:
            raise CredencialesInvalidasError("Credenciales inválidas")

        if not self._verificar_password(password, usuario.password_hash):
            raise CredencialesInvalidasError("Credenciales inválidas")

        if not usuario.puede_iniciar_sesion():
            raise UsuarioServiceError(
                f"Usuario no puede iniciar sesión (estado: {usuario.estado.value})"
            )

        return usuario

    def obtener_usuario(self, usuario_id: int) -> Optional[Usuario]:
        """
        Obtiene un usuario por ID.

        Args:
            usuario_id: ID del usuario

        Returns:
            El usuario o None si no existe
        """
        return self.repo.buscar_por_id(usuario_id)

    def listar_usuarios(self, solo_activos: bool = True) -> List[Usuario]:
        """
        Lista usuarios del sistema.

        Args:
            solo_activos: Si True, solo retorna usuarios activos

        Returns:
            Lista de usuarios
        """
        usuarios = self.repo.listar_todos()
        if solo_activos:
            usuarios = [u for u in usuarios if u.esta_activo()]
        return usuarios

    def _hashear_password(self, password: str) -> str:
        """Hashea un password usando bcrypt."""
        import bcrypt
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def _verificar_password(self, password: str, password_hash: str) -> bool:
        """Verifica un password contra su hash."""
        import bcrypt
        return bcrypt.checkpw(
            password.encode('utf-8'),
            password_hash.encode('utf-8')
        )
```

### 4.4 Ejemplo de Tests - Semana 8

```python
"""
tests/test_services/test_usuario_service.py

Tests del servicio de usuarios.
"""

import pytest
from datetime import datetime

from taskflow.models.usuario import Usuario, EstadoUsuario
from taskflow.services.usuario_service import (
    UsuarioService,
    UsuarioExistenteError,
    CredencialesInvalidasError
)
from taskflow.repositories.usuario_repo import UsuarioRepositoryInMemory


@pytest.fixture
def repo_vacio():
    """Retorna un repositorio vacío."""
    return UsuarioRepositoryInMemory()


@pytest.fixture
def service(repo_vacio):
    """Retorna un servicio con repositorio vacío."""
    return UsuarioService(repo_vacio)


class TestUsuarioServiceCrear:
    """Tests para crear_usuario."""

    def test_crear_usuario_exitoso(self, service):
        """Test crear usuario con datos válidos."""
        usuario = service.crear_usuario(
            username="jdoe",
            email="john@example.com",
            password="securepass123",
            nombre_completo="John Doe"
        )

        assert usuario.id is not None
        assert usuario.username == "jdoe"
        assert usuario.email == "john@example.com"
        assert usuario.password_hash != "securepass123"  # Debe estar hasheado
        assert usuario.estado == EstadoUsuario.ACTIVO
        assert usuario.creado_en is not None

    def test_crear_usuario_username_existente(self, service):
        """Test error al crear usuario con username duplicado."""
        service.crear_usuario(
            username="jdoe",
            email="john1@example.com",
            password="pass123"
        )

        with pytest.raises(UsuarioExistenteError) as exc:
            service.crear_usuario(
                username="jdoe",
                email="john2@example.com",
                password="pass456"
            )

        assert "jdoe" in str(exc.value)
        assert "ya existe" in str(exc.value)

    def test_crear_usuario_email_existente(self, service):
        """Test error al crear usuario con email duplicado."""
        service.crear_usuario(
            username="jdoe1",
            email="john@example.com",
            password="pass123"
        )

        with pytest.raises(UsuarioExistenteError) as exc:
            service.crear_usuario(
                username="jdoe2",
                email="john@example.com",
                password="pass456"
            )

        assert "john@example.com" in str(exc.value)

    def test_crear_usuario_datos_invalidos(self, service):
        """Test error al crear usuario con datos inválidos."""
        with pytest.raises(UsuarioServiceError) as exc:
            service.crear_usuario(
                username="ab",  # Muy corto
                email="invalido",  # Email inválido
                password="123"  # Muy corto
            )

        errores = str(exc.value)
        assert "inválido" in errores.lower()


class TestUsuarioServiceAutenticar:
    """Tests para autenticar_usuario."""

    def test_autenticar_exitoso(self, service):
        """Test autenticación con credenciales correctas."""
        service.crear_usuario(
            username="jdoe",
            email="john@example.com",
            password="correctpass"
        )

        usuario = service.autenticar_usuario("jdoe", "correctpass")
        assert usuario.username == "jdoe"

    def test_autenticar_password_incorrecto(self, service):
        """Test error con password incorrecto."""
        service.crear_usuario(
            username="jdoe",
            email="john@example.com",
            password="correctpass"
        )

        with pytest.raises(CredencialesInvalidasError):
            service.autenticar_usuario("jdoe", "wrongpass")

    def test_autenticar_usuario_inexistente(self, service):
        """Test error con usuario inexistente."""
        with pytest.raises(CredencialesInvalidasError):
            service.autenticar_usuario("nobody", "anypass")

    def test_autenticar_usuario_inactivo(self, service, repo_vacio):
        """Test error con usuario inactivo."""
        usuario = service.crear_usuario(
            username="jdoe",
            email="john@example.com",
            password="pass123"
        )
        usuario.estado = EstadoUsuario.INACTIVO
        repo_vacio.guardar(usuario)

        with pytest.raises(UsuarioServiceError) as exc:
            service.autenticar_usuario("jdoe", "pass123")

        assert "no puede iniciar sesión" in str(exc.value)
```

---

## 5. Fase 4: Producción (Semana 16-17)

### 5.1 Objetivo de la Fase

Integrar todos los componentes en un sistema completo y funcional listo para presentación.

### 5.2 Estructura Final del Proyecto

```
taskflow/
├── src/taskflow/
│   ├── __init__.py
│   ├── main.py                     # Entry point FastAPI
│   ├── config.py                   # Configuración
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── usuario.py
│   │   ├── proyecto.py
│   │   ├── tarea.py
│   │   └── comentario.py
│   ├── schemas/                    # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── usuario.py
│   │   ├── proyecto.py
│   │   └── tarea.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── ...
│   ├── services/
│   │   ├── __init__.py
│   │   └── ...
│   ├── api/
│   │   ├── __init__.py
│   │   ├── app.py                  # FastAPI app
│   │   ├── dependencies.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── usuarios.py
│   │   │   ├── proyectos.py
│   │   │   └── tareas.py
│   │   └── middleware.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── dashboard.html
│       └── componentes/
│           ├── navbar.html
│           └── footer.html
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models/
│   ├── test_services/
│   ├── test_api/
│   └── test_e2e/
├── database/
│   ├── schema.sql
│   ├── migrations/
│   └── seeds/
├── notebooks/                      # Material de aprendizaje
├── docs/                           # Documentación
│   ├── arquitectura.md
│   ├── api.md
│   └── deployment.md
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

### 5.3 Ejemplo de Código de Producción

**main.py (Entry Point)**

```python
"""
TaskFlow - Sistema de Gestión de Proyectos y Tareas

Entry point de la aplicación FastAPI.
"""

import uvicorn
from contextlib import asynccontextmanager

from taskflow.api.app import create_app
from taskflow.config import settings


@asynccontextmanager
async def lifespan(app):
    """Maneja el ciclo de vida de la aplicación."""
    # Startup
    print("TaskFlow iniciando...")
    print(f"Modo: {settings.ENV}")
    print(f"DB: {settings.DATABASE_URL}")

    yield

    # Shutdown
    print("TaskFlow deteniéndose...")


# Crear aplicación FastAPI
app = create_app(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(
        "taskflow.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
```

**api/app.py**

```python
"""
Aplicación FastAPI principal.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from taskflow.api.routes import auth, usuarios, proyectos, tareas
from taskflow.templates import templates


def create_app(lifespan=None):
    """Crea y configura la aplicación FastAPI."""
    app = FastAPI(
        title="TaskFlow API",
        description="Sistema de Gestión de Proyectos y Tareas",
        version="1.0.0",
        lifespan=lifespan
    )

    # Registrar rutas
    app.include_router(auth.router, prefix="/api/auth", tags=["Autenticación"])
    app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])
    app.include_router(proyectos.router, prefix="/api/proyectos", tags=["Proyectos"])
    app.include_router(tareas.router, prefix="/api/tareas", tags=["Tareas"])

    # Rutas de templates
    @app.get("/", response_class=HTMLResponse)
    async def root():
        return templates.TemplateResponse("index.html", {"request": {}})

    @app.get("/login", response_class=HTMLResponse)
    async def login_page():
        return templates.TemplateResponse("login.html", {"request": {}})

    @app.get("/dashboard", response_class=HTMLResponse)
    async def dashboard():
        return templates.TemplateResponse("dashboard.html", {"request": {}})

    # Static files
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app
```

---

## 6. Resumen de Progresión

| Semana | Fase | Herramienta Principal | Proporción Notebooks/VSCode | Entregable |
|--------|------|----------------------|----------------------------|------------|
| 1-2 | Notebooks | Jupyter Lab | 100/0 | Notebooks completados |
| 3-4 | Transición | Jupyter + VSCode | 70/30 | Modelos básicos |
| 5-6 | Transición | Jupyter + VSCode | 40/60 | Modelos completos |
| 7-9 | VSCode | VSCode + pytest | 0/100 | Servicios con tests |
| 10-12 | Backend | VSCode + FastAPI | 0/100 | API funcional |
| 13-15 | Frontend | VSCode + Jinja2 | 0/100 | UI completa |
| 16-17 | Producción | VSCode + Docker | 0/100 | Sistema completo |

---

## 7. Consejos para la Transición

### Para el Docente

1. **Sea explícito sobre el cambio:** Anuncie la transición de notebooks a VSCode con anticipación
2. **Muestre el camino:** Demuestre cómo copiar código de notebook a módulo
3. **Valide el progreso:** Verifique que los estudiantes están organizando código correctamente
4. **Use checkpoints:** Tenga hitos claros (ej: "Hoy todos deben tener models/usuario.py creado")

### Para el Estudiante

1. **Notebooks para aprender:** Úselos para experimentar y comprender conceptos
2. **VSCode para construir:** El código del proyecto va en módulos Python
3. **Git es su amigo:** Commitee frecuentemente el código de VSCode
4. **Pregunte:** Si está confundido sobre qué va dónde, pregunte

---

**Fin de Documento**

**Próxima actualización:** Post-implementación de Unidad 1
