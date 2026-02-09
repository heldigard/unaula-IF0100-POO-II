# Codigo - Pydantic y Validacion de Datos

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Esquemas de Usuario Completos

```python
# schemas/usuario.py
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    """Campos base compartidos."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    nombre_completo: Optional[str] = Field(None, max_length=100)

class UsuarioCreate(UsuarioBase):
    """Schema para crear usuario (INCLUYE PASSWORD)."""
    password: str = Field(..., min_length=8)
    password_confirm: str

class UsuarioUpdate(BaseModel):
    """Schema para actualizar usuario (TODOS OPCIONALES)."""
    email: Optional[EmailStr] = None
    nombre_completo: Optional[str] = Field(None, max_length=100)
    password: Optional[str] = Field(None, min_length=8)

class UsuarioResponse(UsuarioBase):
    """Schema para respuesta (SIN PASSWORD, con ID)."""
    id: int
    activo: bool = True
    creado_en: datetime

    model_config = ConfigDict(from_attributes=True)
```

---

## 2. Esquemas con Relaciones

```python
# schemas/proyecto.py
from pydantic import BaseModel
from typing import List, Optional

class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    estado: str = "pendiente"
    prioridad: int = 2

class TareaCreate(TareaBase):
    """Schema para crear tarea."""
    proyecto_id: int

class TareaResponse(TareaBase):
    """Schema de respuesta de tarea."""
    id: int
    proyecto_id: int

class ProyectoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class ProyectoResponse(ProyectoBase):
    """Schema de respuesta de proyecto CON tareas anidadas."""
    id: int
    usuario_id: int
    activo: bool = True
    tareas: List[TareaResponse] = []
```

---

## 3. Validaciones Personalizadas

```python
# schemas/usuario.py
from pydantic import BaseModel, field_validator, ValidationInfo

class UsuarioCreate(BaseModel):
    username: str
    email: str
    password: str
    password_confirm: str

    @field_validator('username')
    @classmethod
    def username_alphanumerico(cls, v: str) -> str:
        """Valida que username sea alfanumerico."""
        if not v.isalnum():
            raise ValueError('Username debe ser alfanumerico')
        return v

    @field_validator('password_confirm')
    @classmethod
    def passwords_coinciden(cls, v: str, info: ValidationInfo) -> str:
        """Valida que passwords coincidan."""
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Los passwords no coinciden')
        return v

    @field_validator('password')
    @classmethod
    def password_fuerte(cls, v: str) -> str:
        """Valida que el password sea fuerte."""
        if len(v) < 8:
            raise ValueError('Password muy corto (minimo 8)')
        if not any(c.isupper() for c in v):
            raise ValueError('Password debe tener al menos una mayuscula')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password debe tener al menos un numero')
        return v
```

---

## 4. Uso en FastAPI

```python
# main.py
from fastapi import FastAPI, HTTPException, status
from typing import List
from schemas.usuario import UsuarioCreate, UsuarioResponse

app = FastAPI()

db_usuarios = []
next_id = 1

@app.post("/usuarios", response_model=UsuarioResponse, status_code=201)
def crear_usuario(usuario: UsuarioCreate):
    """
    Crea un nuevo usuario.

    - request body: UsuarioCreate (con password)
    - response: UsuarioResponse (sin password)
    """
    global next_id

    # Verificar duplicados
    for u in db_usuarios:
        if u["username"] == usuario.username:
            raise HTTPException(status_code=400, detail="Username ya existe")

    # Crear usuario
    nuevo_usuario = UsuarioResponse(
        id=next_id,
        username=usuario.username,
        email=usuario.email,
        nombre_completo=usuario.nombre_completo,
        activo=True,
        creado_en=datetime.now()
    )

    db_usuarios.append(nuevo_usuario.model_dump())
    next_id += 1

    return nuevo_usuario

@app.get("/usuarios", response_model=List[UsuarioResponse])
def listar_usuarios():
    """Retorna lista de usuarios SIN passwords."""
    return db_usuarios
```

---

## 5. Organizacion de Schemas

```
schemas/
├── __init__.py
├── usuario.py          # UsuarioBase, Create, Update, Response
├── proyecto.py         # ProyectoBase, Create, Update, Response
└── tarea.py            # TareaBase, Create, Update, Response
```

---

**Ultima actualizacion:** 2026-02-08
