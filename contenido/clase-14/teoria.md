# Teoria - Pydantic y Validacion de Datos

**IF0100 - Lenguaje de Programacion OO II**

---

## ¿Que es Pydantic?

**Pydantic** es una libreria de Python para validacion de datos usando **type hints**. Es el corazon de FastAPI para:

- **Validar datos de entrada** (request body, query params, path params)
- **Convertir datos** (serializacion/deserializacion)
- **Documentar automaticamente** (OpenAPI se genera desde los modelos)
- **Proveer autocompletado** en editores

---

## Por que usar Pydantic

| Ventaja | Descripcion |
|---------|-------------|
| **Validacion Automatica** | Los datos se validan antes de ejecutar el codigo |
| **Documentacion Auto** | OpenAPI se genera desde los modelos |
| **Type Hints** | Usa tipos estandar de Python |
| **Serializacion** | Convierte objetos Python a JSON y viceversa |
| **Mensajes de Error** | Errores detallados y legibles |

---

## Schema Request vs Response

| Tipo | Proposito | Ejemplo |
|------|-----------|---------|
| **Request** | Validar datos de entrada | `UsuarioCreate` (con password) |
| **Response** | Definir datos de salida | `UsuarioResponse` (sin password) |

> **Importante:** Nunca incluyas passwords en schemas de response.

---

## Tipos de Validacion

### Validaciones Basicas con Field

```python
from pydantic import BaseModel, Field

class UsuarioCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_]+$"
    )
    email: str = Field(pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    password: str = Field(min_length=8)
```

### Tipos Especiales

| Tipo | Uso |
|------|-----|
| **EmailStr** | Validacion automatica de email |
| **HttpUrl** | Validacion de URL |
| **datetime** | Fechas y horas |
| **List[str]** | Lista de strings |
| **Optional[str]** | Campo opcional |

---

## Validadores Personalizados

```python
from pydantic import BaseModel, field_validator

class UsuarioCreate(BaseModel):
    username: str
    password: str
    password_confirm: str

    @field_validator('username')
    @classmethod
    def username_alphanumerico(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError('Username debe ser alfanumerico')
        return v

    @field_validator('password_confirm')
    @classmethod
    def passwords_coinciden(cls, v: str, info) -> str:
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Los passwords no coinciden')
        return v
```

---

## Patrones de Schemas Recomendados

```
1. Base: campos compartidos
   └── UsuarioBase: username, email

2. Create: para POST (agrega campos requeridos)
   └── UsuarioCreate: password

3. Update: para PUT/PATCH (todos opcionales)
   └── UsuarioUpdate: email?, password?

4. Response: para GET (sin datos sensibles)
   └── UsuarioResponse: id, username, email, creado_en
```

---

**Ultima actualizacion:** 2026-02-08
