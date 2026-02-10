# Ejercicios - Pydantic y Validacion de Datos

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Schemas Completos de Usuario

Crear schemas Pydantic para el modelo Usuario:

```python
# schemas/usuario.py
from pydantic import BaseModel, EmailStr, Field

# 1. UsuarioBase: username, email, nombre_completo
class UsuarioBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    nombre_completo: str | None = None

# 2. UsuarioCreate: agregar password con validaciones
class UsuarioCreate(BaseModel):
    pass

# 3. UsuarioUpdate: todos los campos opcionales
class UsuarioUpdate(BaseModel):
    pass

# 4. UsuarioResponse: con id y activo
class UsuarioResponse(BaseModel):
    pass
```

---

## Ejercicio 2: Validaciones Personalizadas

Agregar validadores al schema:

```python
from pydantic import BaseModel, field_validator

class UsuarioCreate(BaseModel):
    username: str
    email: str
    password: str
    password_confirm: str

    # Validador para username alfanumerico
    @field_validator('username')
    @classmethod
    def username_valido(cls, v):
        if not v.isalnum():
            raise ValueError('Solo caracteres alfanumericos')
        return v

    # Validador para passwords coincidentes
    @field_validator('password_confirm')
    @classmethod
    def passwords_coincidan(cls, v, info):
        pass  # Implementar

    # Validador para password fuerte
    @field_validator('password')
    @classmethod
    def password_seguro(cls, v):
        pass  # Implementar: min 8 chars, 1 mayus, 1 numero
```

---

## Ejercicio 3: Schemas Anidados

Crear schemas con relaciones:

```python
from pydantic import BaseModel
from typing import List

class Comentario(BaseModel):
    id: int
    texto: str
    autor: str

class Post(BaseModel):
    id: int
    titulo: str
    contenido: str
    comentarios: List[Comentario] = []

# Ejemplo de uso:
post = Post(
    id=1,
    titulo="Hola",
    contenido="Mundo",
    comentarios=[
        Comentario(id=1, texto="Comment 1", autor="User1")
    ]
)
```

---

## Ejercicio 4: Configuracion de Modelos

Usar ConfigDict para configurar comportamiento:

```python
from pydantic import BaseModel, ConfigDict

class Usuario(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(
        str_strip_whitespace=True,   # Limpiar espacios
        validate_assignment=True,     # Validar al asignar
        extra='forbid',              # Rechazar campos extra
        json_schema_extra={           # Metadata para OpenAPI
            "example": {
                "id": 1,
                "username": "juan",
                "email": "juan@example.com"
            }
        }
    )
```

---

**Ultima actualizacion:** 2026-02-08
