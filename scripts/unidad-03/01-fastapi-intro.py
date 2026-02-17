"""
Script de Práctica - Clase 3.1: Introducción a FastAPI

Este script demuestra los conceptos básicos de FastAPI:
- Crear una aplicación FastAPI
- Definir rutas y operaciones HTTP
- Usar path parameters y query parameters
- Retornar JSON
- Ejecutar el servidor de desarrollo

Autor: IF0100 - UNAULA
"""

from fastapi import FastAPI, HTTPException
from typing import Optional, List
import uvicorn

# Crear la aplicación FastAPI
app = FastAPI(
    title="TaskFlow API",
    description="API para gestión de proyectos y tareas",
    version="1.0.0"
)

# Datos en memoria (simulando una base de datos)
proyectos_db = [
    {"id": 1, "nombre": "TaskFlow", "descripcion": "App de gestión de tareas"},
    {"id": 2, "nombre": "Mi Proyecto", "descripcion": "Proyecto personal"},
]

# =====================================================
# RUTAS BASICAS
# =====================================================

@app.get("/")
def read_root():
    """
    Ruta raíz - Retorna información de la API
    GET http://localhost:8000/
    """
    return {
        "mensaje": "Bienvenido a TaskFlow API",
        "version": "1.0.0",
        "documentacion": "/docs"
    }


@app.get("/health")
def health_check():
    """
    Health check - Para verificar que la API funciona
    GET http://localhost:8000/health
    """
    return {"status": "ok"}


# =====================================================
# PATH PARAMETERS
# =====================================================

@app.get("/proyectos/{proyecto_id}")
def get_proyecto(proyecto_id: int):
    """
    Obtener un proyecto por ID
    GET http://localhost:8000/proyectos/1

    - proyecto_id: Path parameter (obligatorio, tipo int)
    """
    # Buscar proyecto
    for proyecto in proyectos_db:
        if proyecto["id"] == proyecto_id:
            return proyecto

    # Si no existe, retornar 404
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")


@app.get("/proyectos/{proyecto_id}/tareas/{tarea_id}")
def get_tarea(proyecto_id: int, tarea_id: int):
    """
    Obtener una tarea específica de un proyecto
    GET http://localhost:8000/proyectos/1/tareas/5

    Múltiples path parameters
    """
    return {
        "proyecto_id": proyecto_id,
        "tarea_id": tarea_id,
        "titulo": f"Tarea {tarea_id} del proyecto {proyecto_id}"
    }


# =====================================================
# QUERY PARAMETERS
# =====================================================

@app.get("/proyectos")
def get_proyectos(skip: int = 0, limit: int = 10):
    """
    Listar proyectos con paginación
    GET http://localhost:8000/proyectos?skip=0&limit=10

    - skip: Query parameter (opcional, default 0)
    - limit: Query parameter (opcional, default 10)
    """
    return {
        "total": len(proyectos_db),
        "skip": skip,
        "limit": limit,
        "items": proyectos_db[skip : skip + limit]
    }


@app.get("/proyectos/search")
def search_proyectos(q: Optional[str] = None):
    """
    Buscar proyectos por nombre
    GET http://localhost:8000/proyectos/search?q=task
    GET http://localhost:8000/proyectos/search

    - q: Query parameter opcional (puede ser None)
    """
    if not q:
        return {"mensaje": "Proporciona un término de búsqueda", "ejemplo": "/proyectos/search?q=task"}

    resultados = [p for p in proyectos_db if q.lower() in p["nombre"].lower()]
    return {"resultados": resultados, "cantidad": len(resultados)}


# =====================================================
# POST - Crear recursos
# =====================================================

@app.post("/proyectos")
def create_proyecto(proyecto: dict):
    """
    Crear un nuevo proyecto
    POST http://localhost:8000/proyectos
    Body: {"nombre": "Nuevo Proyecto", "descripcion": "Descripción"}
    """
    # Generar ID
    nuevo_id = max([p["id"] for p in proyectos_db]) + 1 if proyectos_db else 1

    nuevo_proyecto = {
        "id": nuevo_id,
        "nombre": proyecto.get("nombre"),
        "descripcion": proyecto.get("descripcion")
    }

    proyectos_db.append(nuevo_proyecto)
    return nuevo_proyecto


# =====================================================
# PUT - Actualizar recursos
# =====================================================

@app.put("/proyectos/{proyecto_id}")
def update_proyecto(proyecto_id: int, proyecto: dict):
    """
    Actualizar un proyecto existente
    PUT http://localhost:8000/proyectos/1
    Body: {"nombre": "Nombre Actualizado", "descripcion": "Nueva descripción"}
    """
    for p in proyectos_db:
        if p["id"] == proyecto_id:
            p["nombre"] = proyecto.get("nombre", p["nombre"])
            p["descripcion"] = proyecto.get("descripcion", p["descripcion"])
            return p

    raise HTTPException(status_code=404, detail="Proyecto no encontrado")


# =====================================================
# DELETE - Eliminar recursos
# =====================================================

@app.delete("/proyectos/{proyecto_id}")
def delete_proyecto(proyecto_id: int):
    """
    Eliminar un proyecto
    DELETE http://localhost:8000/proyectos/1
    """
    for i, p in enumerate(proyectos_db):
        if p["id"] == proyecto_id:
            proyectos_db.pop(i)
            return {"mensaje": f"Proyecto {proyecto_id} eliminado"}

    raise HTTPException(status_code=404, detail="Proyecto no encontrado")


# =====================================================
# EJECUCIÓN DEL SERVIDOR
# =====================================================

if __name__ == "__main__":
    print("=" * 50)
    print("TaskFlow API - FastAPI")
    print("=" * 50)
    print("\nServidor disponible en:")
    print("  - http://localhost:8000")
    print("  - Documentación: http://localhost:8000/docs")
    print("  - Redocly: http://localhost:8000/redoc")
    print("\nPresiona Ctrl+C para detener")
    print("=" * 50)

    # Ejecutar servidor
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


# =====================================================
# INSTRUCCIONES DE USO
# =====================================================

"""
Para ejecutar este script:

1. Instalar dependencias:
   pip install fastapi uvicorn

2. Ejecutar el script:
   python scripts/unidad-03/01-fastapi-intro.py

3. Probar la API:
   - Visitar http://localhost:8000/docs para la documentación interactiva
   - O usar curl:
     curl http://localhost:8000/
     curl http://localhost:8000/proyectos
     curl http://localhost:8000/proyectos/1

4. Ejemplos de requests:

   # Listar proyectos
   GET http://localhost:8000/proyectos

   # Buscar proyecto
   GET http://localhost:8000/proyectos/1

   # Crear proyecto
   POST http://localhost:8000/proyectos
   Content-Type: application/json
   {
     "nombre": "Mi Proyecto",
     "descripcion": "Descripción del proyecto"
   }

   # Actualizar proyecto
   PUT http://localhost:8000/proyectos/1
   Content-Type: application/json
   {
     "nombre": "Proyecto Actualizado",
     "descripcion": "Nueva descripción"
   }

   # Eliminar proyecto
   DELETE http://localhost:8000/proyectos/1
"""
