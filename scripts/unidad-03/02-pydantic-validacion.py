"""
Script de Práctica - Clase 3.2: Pydantic y Validación de Datos

Este script demuestra el uso de Pydantic para validación de datos:
- Definir modelos Pydantic
- Validar tipos de datos
- Validar restricciones (longitud, rangos, patrones)
- Valores por defecto y opcionales
- Manejo de errores de validación

Autor: IF0100 - UNAULA
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional, List
from datetime import datetime
import re

app = FastAPI(title="Validación con Pydantic")


# =====================================================
# MODELOS PYDANTIC
# =====================================================

class UsuarioBase(BaseModel):
    """Modelo base para usuario"""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    """Modelo para crear usuario (incluye password)"""
    password: str = Field(..., min_length=6, max_length=100)
    password_confirm: str

    @validator('password_confirm')
    def passwords_match(cls, v, values, **kwargs):
        """Valida que las contraseñas coincidan"""
        if 'password' in values and v != values['password']:
            raise ValueError('Las contraseñas no coinciden')
        return v


class UsuarioResponse(UsuarioBase):
    """Modelo para respuesta (no incluye password)"""
    id: int
    activo: bool = True
    creado_en: datetime


class ProyectoCreate(BaseModel):
    """Modelo para crear proyecto"""
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre del proyecto")
    descripcion: Optional[str] = Field(None, max_length=500)
    prioridad: int = Field(default=1, ge=1, le=5, description="Prioridad 1-5")

    @validator('nombre')
    def nombre_mayuscula(cls, v):
        """Convierte la primera letra a mayúscula"""
        return v.capitalize()


class TareaCreate(BaseModel):
    """Modelo para crear tarea"""
    titulo: str = Field(..., min_length=5, max_length=200)
    descripcion: Optional[str] = None
    prioridad: str = Field(default="media", regex="^(baja|media|alta)$")
    etiquetas: List[str] = Field(default_factory=list)


class TareaUpdate(BaseModel):
    """Modelo para actualizar tarea (todos los campos opcionales)"""
    titulo: Optional[str] = Field(None, min_length=5, max_length=200)
    descripcion: Optional[str] = None
    completada: Optional[bool] = None
    prioridad: Optional[str] = Field(None, regex="^(baja|media|alta)$")


# =====================================================
# BASE DE DATOS SIMULADA
# =====================================================

usuarios_db = {
    1: {"id": 1, "username": "juan", "email": "juan@example.com", "activo": True, "creado_en": datetime.now()}
}

proyectos_db = {
    1: {"id": 1, "usuario_id": 1, "nombre": "TaskFlow", "descripcion": "App de gestión", "prioridad": 5}
}

tareas_db = {
    1: {"id": 1, "proyecto_id": 1, "titulo": "Implementar login", "descripcion": "Crear endpoint POST", "completada": False, "prioridad": "alta", "etiquetas": ["backend", "auth"]}
}


# =====================================================
# ENDPOINTS - Crear Usuario
# =====================================================

@app.post("/usuarios", response_model=UsuarioResponse, status_code=201)
def create_usuario(usuario: UsuarioCreate):
    """
    Crear un nuevo usuario

    - **username**: Mínimo 3 caracteres, máximo 50
    - **email**: Debe ser un email válido
    - **password**: Mínimo 6 caracteres
    - **password_confirm**: Debe coincidir con password
    """
    # Verificar si el usuario ya existe
    for u in usuarios_db.values():
        if u["username"] == usuario.username or u["email"] == usuario.email:
            raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Crear usuario (simulado)
    nuevo_id = max(usuarios_db.keys()) + 1 if usuarios_db else 1
    usuario_db = {
        "id": nuevo_id,
        "username": usuario.username,
        "email": usuario.email,
        "activo": True,
        "creado_en": datetime.now()
    }
    usuarios_db[nuevo_id] = usuario_db

    return usuario_db


# =====================================================
# ENDPOINTS - Proyectos
# =====================================================

@app.post("/proyectos", status_code=201)
def create_proyecto(proyecto: ProyectoCreate, usuario_id: int = Query(..., gt=0)):
    """
    Crear un proyecto

    - **nombre**: Mínimo 3 caracteres, máximo 100
    - **descripcion**: Opcional, máximo 500 caracteres
    - **prioridad**: Entre 1 y 5 (default: 1)
    - **usuario_id**: Query parameter obligatorio, mayor que 0
    """
    # Verificar que el usuario existe
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    nuevo_id = max(proyectos_db.keys()) + 1 if proyectos_db else 1
    proyecto_db = {
        "id": nuevo_id,
        "usuario_id": usuario_id,
        "nombre": proyecto.nombre,
        "descripcion": proyecto.descripcion,
        "prioridad": proyecto.prioridad
    }
    proyectos_db[nuevo_id] = proyecto_db

    return proyecto_db


# =====================================================
# ENDPOINTS - Tareas
# =====================================================

@app.post("/tareas", status_code=201)
def create_tarea(tarea: TareaCreate, proyecto_id: int = Query(..., gt=0)):
    """
    Crear una tarea

    - **titulo**: Mínimo 5 caracteres, máximo 200
    - **descripcion**: Opcional
    - **prioridad**: Debe ser "baja", "media" o "alta"
    - **etiquetas**: Lista de strings (default: [])
    """
    # Verificar que el proyecto existe
    if proyecto_id not in proyectos_db:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    nuevo_id = max(tareas_db.keys()) + 1 if tareas_db else 1
    tarea_db = {
        "id": nuevo_id,
        "proyecto_id": proyecto_id,
        "titulo": tarea.titulo,
        "descripcion": tarea.descripcion,
        "completada": False,
        "prioridad": tarea.prioridad,
        "etiquetas": tarea.etiquetas
    }
    tareas_db[nuevo_id] = tarea_db

    return tarea_db


@app.patch("/tareas/{tarea_id}")
def update_tarea(tarea_id: int, tarea: TareaUpdate):
    """
    Actualizar una tarea (parcial)

    Solo se actualizan los campos proporcionados
    """
    if tarea_id not in tareas_db:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    tarea_db = tareas_db[tarea_id]

    # Actualizar solo los campos proporcionados
    update_data = tarea.dict(exclude_unset=True)
    for campo, valor in update_data.items():
        tarea_db[campo] = valor

    return tarea_db


# =====================================================
# EJEMPLOS DE VALIDACIÓN
# =====================================================

@app.get("/ejemplos/validacion")
def ejemplos_validacion():
    """
    Retorna ejemplos de requests válidos e inválidos
    """
    return {
        "usuario_valido": {
            "username": "juan123",
            "email": "juan@example.com",
            "password": "secreto123",
            "password_confirm": "secreto123"
        },
        "usuario_invalido_password_corto": {
            "username": "juan",
            "email": "juan@example.com",
            "password": "123",
            "password_confirm": "123"
        },
        "usuario_invalido_password_no_coincide": {
            "username": "juan",
            "email": "juan@example.com",
            "password": "secreto123",
            "password_confirm": "diferente"
        },
        "proyecto_valido": {
            "nombre": "Mi Proyecto",
            "descripcion": "Descripción del proyecto",
            "prioridad": 3
        },
        "proyecto_invalido_prioridad": {
            "nombre": "Mi Proyecto",
            "prioridad": 6  # Fuera de rango (1-5)
        },
        "tarea_valida": {
            "titulo": "Implementar endpoint de login",
            "descripcion": "Crear POST /auth/login",
            "prioridad": "alta",
            "etiquetas": ["backend", "auth"]
        },
        "tarea_invalida_prioridad": {
            "titulo": "Tarea",
            "prioridad": "urgente"  # No coincide con el regex
        }
    }


# =====================================================
# EJECUCIÓN
# =====================================================

if __name__ == "__main__":
    import uvicorn
    print("=" * 50)
    print("API de Validación con Pydantic")
    print("=" * 50)
    print("\nDocumentación: http://localhost:8000/docs")
    print("\nEjemplos de validación: http://localhost:8000/ejemplos/validacion")
    print("=" * 50)

    uvicorn.run(app, host="127.0.0.1", port=8001, reload=True)


"""
EJEMPLOS DE USO:

1. Crear usuario VÁLIDO:
POST http://localhost:8001/usuarios
{
  "username": "juan123",
  "email": "juan@example.com",
  "password": "secreto123",
  "password_confirm": "secreto123"
}

2. Crear usuario INVÁLIDO (password corto):
POST http://localhost:8001/usuarios
{
  "username": "juan",
  "email": "juan@example.com",
  "password": "123",
  "password_confirm": "123"
}
Response: 422 Validation Error

3. Crear proyecto:
POST http://localhost:8001/proyectos?usuario_id=1
{
  "nombre": "Mi Proyecto",
  "descripcion": "Descripción",
  "prioridad": 3
}

4. Crear tarea:
POST http://localhost:8001/tareas?proyecto_id=1
{
  "titulo": "Implementar login",
  "prioridad": "alta",
  "etiquetas": ["backend", "auth"]
}

5. Actualizar tarea (parcial):
PATCH http://localhost:8001/tareas/1
{
  "completada": true
}
"""
