"""
Script de Práctica - Clase 3.5: Persistencia de Datos

Este script demuestra patrones de persistencia:
- Base de datos en memoria (diccionarios)
- Conexión a base de datos real con SQLAlchemy
- CRUD (Create, Read, Update, Delete)
- Migraciones con Alembic
- Pydantic para validación
- Repositorios y servicios

Autor: IF0100 - UNAULA
"""

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import sqlite3

# =====================================================
# MODO 1: Base de datos en memoria (sin instaladores)
# =====================================================

app = FastAPI(title="Persistencia de Datos")


# Modelos Pydantic
class ProyectoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: Optional[str] = None


class ProyectoResponse(ProyectoCreate):
    id: int
    creado_en: datetime


class TareaCreate(BaseModel):
    titulo: str = Field(..., min_length=5, max_length=200)
    descripcion: Optional[str] = None
    proyecto_id: int
    prioridad: str = Field(default="media", regex="^(baja|media|alta)$")


class TareaResponse(TareaCreate):
    id: int
    completada: bool = False
    creado_en: datetime


# Base de datos en memoria (para desarrollo rápido)
proyectos_db: dict = {}
tareas_db: dict = {}
proyectos_counter = 1
tareas_counter = 1


# =====================================================
# REPOSITORIOS (Patrón Repository)
# =====================================================

class ProyectoRepository:
    """Repositorio para gestión de proyectos"""

    def __init__(self):
        self.db = proyectos_db
        self.counter = proyectos_counter

    def create(self, nombre: str, descripcion: str = None) -> dict:
        global proyectos_counter
        proyecto = {
            "id": proyectos_counter,
            "nombre": nombre,
            "descripcion": descripcion,
            "creado_en": datetime.now()
        }
        self.db[proyectos_counter] = proyecto
        proyectos_counter += 1
        return proyecto

    def get_all(self) -> List[dict]:
        return list(self.db.values())

    def get_by_id(self, proyecto_id: int) -> Optional[dict]:
        return self.db.get(proyecto_id)

    def update(self, proyecto_id: int, **kwargs) -> Optional[dict]:
        if proyecto_id not in self.db:
            return None
        self.db[proyecto_id].update(kwargs)
        return self.db[proyecto_id]

    def delete(self, proyecto_id: int) -> bool:
        if proyecto_id in self.db:
            del self.db[proyecto_id]
            return True
        return False


class TareaRepository:
    """Repositorio para gestión de tareas"""

    def __init__(self):
        self.db = tareas_db

    def create(self, titulo: str, proyecto_id: int, **kwargs) -> dict:
        global tareas_counter
        tarea = {
            "id": tareas_counter,
            "titulo": titulo,
            "proyecto_id": proyecto_id,
            "creado_en": datetime.now(),
            "completada": False,
            **kwargs
        }
        self.db[tareas_counter] = tarea
        tareas_counter += 1
        return tarea

    def get_by_project(self, proyecto_id: int) -> List[dict]:
        return [t for t in self.db.values() if t["proyecto_id"] == proyecto_id]

    def get_by_id(self, tarea_id: int) -> Optional[dict]:
        return self.db.get(tarea_id)

    def update(self, tarea_id: int, **kwargs) -> Optional[dict]:
        if tarea_id not in self.db:
            return None
        self.db[tarea_id].update(kwargs)
        return self.db[tarea_id]

    def delete(self, tarea_id: int) -> bool:
        if tarea_id in self.db:
            del self.db[tarea_id]
            return True
        return False


# Instancias de repositorios
proyecto_repo = ProyectoRepository()
tarea_repo = TareaRepository()


# =====================================================
# ENDPOINTS - Proyectos
# =====================================================

@app.post("/proyectos", response_model=ProyectoResponse, status_code=201)
def create_proyecto(proyecto: ProyectoCreate):
    """Crear un nuevo proyecto"""
    return proyecto_repo.create(proyecto.nombre, proyecto.descripcion)


@app.get("/proyectos", response_model=List[ProyectoResponse])
def get_proyectos():
    """Listar todos los proyectos"""
    return proyecto_repo.get_all()


@app.get("/proyectos/{proyecto_id}", response_model=ProyectoResponse)
def get_proyecto(proyecto_id: int):
    """Obtener un proyecto por ID"""
    proyecto = proyecto_repo.get_by_id(proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


@app.put("/proyectos/{proyecto_id}", response_model=ProyectoResponse)
def update_proyecto(proyecto_id: int, proyecto: ProyectoCreate):
    """Actualizar un proyecto"""
    actualizado = proyecto_repo.update(
        proyecto_id,
        nombre=proyecto.nombre,
        descripcion=proyecto.descripcion
    )
    if not actualizado:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return actualizado


@app.delete("/proyectos/{proyecto_id}")
def delete_proyecto(proyecto_id: int):
    """Eliminar un proyecto"""
    if not proyecto_repo.delete(proyecto_id):
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return {"mensaje": "Proyecto eliminado"}


# =====================================================
# ENDPOINTS - Tareas
# =====================================================

@app.post("/tareas", response_model=TareaResponse, status_code=201)
def create_tarea(tarea: TareaCreate):
    """Crear una nueva tarea"""
    # Verificar que el proyecto existe
    if not proyecto_repo.get_by_id(tarea.proyecto_id):
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")

    return tarea_repo.create(
        titulo=tarea.titulo,
        proyecto_id=tarea.proyecto_id,
        descripcion=tarea.descripcion,
        prioridad=tarea.prioridad
    )


@app.get("/proyectos/{proyecto_id}/tareas", response_model=List[TareaResponse])
def get_tareas_por_proyecto(proyecto_id: int):
    """Listar tareas de un proyecto"""
    if not proyecto_repo.get_by_id(proyecto_id):
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return tarea_repo.get_by_project(proyecto_id)


@app.get("/tareas/{tarea_id}", response_model=TareaResponse)
def get_tarea(tarea_id: int):
    """Obtener una tarea por ID"""
    tarea = tarea_repo.get_by_id(tarea_id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@app.patch("/tareas/{tarea_id}/completar")
def completar_tarea(tarea_id: int):
    """Marcar una tarea como completada"""
    actualizado = tarea_repo.update(tarea_id, completada=True)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea marcada como completada"}


@app.delete("/tareas/{tarea_id}")
def delete_tarea(tarea_id: int):
    """Eliminar una tarea"""
    if not tarea_repo.delete(tarea_id):
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"mensaje": "Tarea eliminada"}


# =====================================================
# DEMO - Datos iniciales
# =====================================================

@app.post("/demo/seed")
def seed_demo_data():
    """Crear datos de demostración"""
    global proyectos_counter, tareas_counter

    # Crear proyectos demo
    p1 = proyecto_repo.create("TaskFlow", "App de gestión de tareas")
    p2 = proyecto_repo.create("Mi Proyecto Personal", "Proyecto de aprendizaje")

    # Crear tareas demo
    tarea_repo.create("Implementar login", p1["id"], descripcion="POST /auth/login", prioridad="alta")
    tarea_repo.create("Diseñar base de datos", p1["id"], descripcion="Modelo ER", prioridad="media")
    tarea_repo.create("Aprender FastAPI", p2["id"], descripcion="Tutorial oficial", prioridad="baja")

    return {"mensaje": "Datos demo creados", "proyectos": len(proyectos_db), "tareas": len(tareas_db)}


# =====================================================
# EJECUCIÓN
# =====================================================

if __name__ == "__main__":
    import uvicorn
    print("=" * 50)
    print("API de Persistencia de Datos")
    print("=" * 50)
    print("\nCaracterísticas:")
    print("  - Base de datos en memoria")
    print("  - Patrones CRUD completos")
    print("  - Repositorios para separar lógica")
    print("  - Relaciones 1:N (proyecto -> tareas)")
    print("\nEndpoints:")
    print("  - POST /demo/seed  -> Crear datos demo")
    print("  - GET  /proyectos  -> Listar proyectos")
    print("  - POST /proyectos  -> Crear proyecto")
    print("  - GET  /proyectos/{id}/tareas -> Tareas del proyecto")
    print("\nDocumentación: http://localhost:8004/docs")
    print("=" * 50)

    uvicorn.run(app, host="127.0.0.1", port=8004, reload=True)


"""
=====================================================
MODO 2: Conexión a Base de Datos Real (SQLAlchemy)
=====================================================

Para usar base de datos real, necesitas instalar:

pip install sqlalchemy

Modelo con SQLAlchemy:

```python
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Configurar BD
DATABASE_URL = "sqlite:///./taskflow.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos SQLAlchemy
class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500))
    creado_en = Column(DateTime, default=datetime.utcnow)

    tareas = relationship("Tarea", back_populates="proyecto")


class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(String(500))
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"))
    completada = Column(Boolean, default=False)
    prioridad = Column(String(20))
    creado_en = Column(DateTime, default=datetime.utcnow)

    proyecto = relationship("Proyecto", back_populates="tareas")

# Crear tablas
Base.metadata.create_all(bind=engine)

# Dependencia para obtener sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint con BD real
@app.post("/proyectos-db")
def create_proyecto_db(proyecto: ProyectoCreate, db: Session = Depends(get_db)):
    db_proyecto = Proyecto(
        nombre=proyecto.nombre,
        descripcion=proyecto.descripcion
    )
    db.add(db_proyecto)
    db.commit()
    db.refresh(db_proyecto)
    return db_proyecto
```

=====================================================
MODO 3: Migraciones con Alembic
=====================================================

Para gestionar cambios en la BD:

pip install alembic
alembic init alembic

# Configurar alembic.ini
# sqlalchemy.url = sqlite:///./taskflow.db

# Crear migración
alembic revision --autogenerate -m "Crear tablas iniciales"

# Ejecutar migración
alembic upgrade head

=====================================================
PATRONES DE DISEÑO
=====================================================

1. Repository Pattern:
   - Separa lógica de acceso a datos
   - Facilita testing con mocks
   - Permite cambiar BD sin afectar endpoints

2. Service Layer (Opcional):
   - Lógica de negocio compleja
   - Coordina múltiples repositorios
   - Maneja transacciones

3. Unit of Work:
   - Agrupa operaciones en transacciones
   - Commit/rollback atómicos

=====================================================
EJEMPLOS DE USO
=====================================================

1. Crear datos demo:
   POST http://localhost:8004/demo/seed

2. Crear proyecto:
   POST http://localhost:8004/proyectos
   {
     "nombre": "Mi Proyecto",
     "descripcion": "Descripción"
   }

3. Crear tarea:
   POST http://localhost:8004/tareas
   {
     "titulo": "Nueva tarea",
     "proyecto_id": 1,
     "prioridad": "alta"
   }

4. Listar tareas del proyecto:
   GET http://localhost:8004/proyectos/1/tareas

5. Completar tarea:
   PATCH http://localhost:8004/tareas/1/completar
"""
