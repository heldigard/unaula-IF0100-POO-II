# Evaluación 3 - IF0100: Desarrollo Web con FastAPI

**Curso:** IF0100 - Lenguaje de Programación OO II
**Tipo:** Proyecto práctico (en parejas)
**Porcentaje:** 20%
**Fecha de entrega:** 2026-03-26 (Jueves)
**Sustentación:** Obligatoria

---

## 🎯 Objetivo

Desarrollar una aplicación web funcional usando FastAPI, HTML5, Jinja2, HTMX y Bootstrap, demostrando dominio de los conceptos de desarrollo web moderno.

---

## 📋 Descripción del Proyecto

### Tema: Sistema de Gestión de Biblioteca

Desarrollar un sistema web para gestionar una biblioteca con las siguientes funcionalidades:

---

## 🔧 Requerimientos Funcionales

### 1. Gestión de Libros (25 pts)
- Listar todos los libros
- Ver detalle de un libro
- Agregar nuevo libro
- Editar libro existente
- Eliminar libro (con confirmación)

**Campos del libro:**
- ISBN (único)
- Título
- Autor
- Editorial
- Año de publicación
- Género (dropdown)
- Cantidad disponible
- Imagen de portada (URL)

### 2. Gestión de Préstamos (20 pts)
- Registrar préstamo
- Ver préstamos activos
- Registrar devolución
- Historial de préstamos

### 3. Búsqueda y Filtros (10 pts)
- Buscar por título o autor
- Filtrar por género
- Ordenar resultados

### 4. Validaciones (15 pts)
- Validación de formularios (Pydantic)
- Mensajes de error claros
- Prevención de datos duplicados

---

## 🎨 Requerimientos de Diseño

### 5. Interfaz de Usuario (20 pts)

**Usar Bootstrap 5:**
- Navbar responsive
- Cards para mostrar libros
- Tablas estilizadas
- Formularios con validación visual
- Modales para confirmaciones
- Alertas para mensajes

**Layout:**
- Header con navegación
- Footer con información
- Diseño responsive (móvil, tablet, escritorio)

**Usar HTMX para interactividad:**
- Carga de contenido sin recargar página
- Actualización dinámica de listas
- Búsquedas en tiempo real

### 6. HTML5 Semántico (10 pts)
- Uso de `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`
- Formularios con tipos de input apropiados
- Atributos de accesibilidad

---

## 🏗️ Arquitectura del Proyecto FastAPI

```
biblioteca_web/
├── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── config.py           # Settings y configuración
│   ├── database.py         # Conexión SQLAlchemy
│   ├── models/
│   │   ├── __init__.py
│   │   ├── libro.py
│   │   └── prestamo.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── libro.py        # Pydantic schemas
│   │   └── prestamo.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── home.py
│   │   ├── libros.py
│   │   └── prestamos.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── biblioteca_service.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── layout.html
│       └── libros/
│           ├── index.html
│           ├── detail.html
│           ├── form.html
│           └── confirm_delete.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── htmx.min.js
├── tests/
│   ├── __init__.py
│   └── test_libros.py
├── alembic/
│   └── versions/
├── requirements.txt
└── pyproject.toml
```

---

## 💻 Requisitos Técnicos

1. **FastAPI** (.venv y Uvicorn)
2. **Jinja2** para templates
3. **HTMX** para interactividad sin JavaScript
4. **Bootstrap 5** para estilos
5. **Pydantic** para validación

### Código de Ejemplo Esperado:

**Modelo SQLAlchemy:**
```python
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String(13), unique=True, nullable=False)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(100), nullable=False)
    editorial = Column(String(100))
    anio_publicacion = Column(Integer)
    genero = Column(String(50))
    cantidad_disponible = Column(Integer, default=0)
    imagen_url = Column(String(500))

    prestamos = relationship("Prestamo", back_populates="libro")
```

**Schema Pydantic:**
```python
from pydantic import BaseModel, Field
from typing import Optional

class LibroCreate(BaseModel):
    isbn: str = Field(..., min_length=10, max_length=13)
    titulo: str = Field(..., min_length=1, max_length=200)
    autor: str = Field(..., min_length=1, max_length=100)
    editorial: Optional[str] = None
    anio_publicacion: int = Field(..., ge=1800, le=2026)
    genero: str
    cantidad_disponible: int = Field(..., ge=0)
    imagen_url: Optional[str] = None

    class Config:
        from_attributes = True
```

**Router FastAPI:**
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.libro import LibroCreate, LibroResponse
from src.services.biblioteca_service import BibliotecaService

router = APIRouter(prefix="/libros", tags=["libros"])

@router.get("/", response_model=list[LibroResponse])
def listar_libros(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    service = BibliotecaService(db)
    return service.listar_libros(skip=skip, limit=limit)

@router.get("/{libro_id}", response_model=LibroResponse)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    service = BibliotecaService(db)
    return service.obtener_libro(libro_id)

@router.post("/", response_model=LibroResponse, status_code=201)
def crear_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    service = BibliotecaService(db)
    return service.crear_libro(libro)

@router.delete("/{libro_id}", status_code=204)
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    service = BibliotecaService(db)
    service.eliminar_libro(libro_id)
```

**Template Jinja2 (con HTMX):**
```html
{% extends "base.html" %}

{% block content %}
<div class="container">
    <h1>Lista de Libros</h1>

    <!-- Búsqueda con HTMX -->
    <div class="mb-3">
        <input type="text"
               name="q"
               hx-get="/libros/buscar"
               hx-trigger="keyup changed delay:500ms"
               hx-target="#libros-list"
               placeholder="Buscar por título o autor..."
               class="form-control">
    </div>

    <!-- Lista de libros -->
    <div id="libros-list" hx-get="/libros" hx-trigger="load">
        {% include "libros/partials/lista.html" %}
    </div>

    <a href="/libros/nuevo" class="btn btn-primary">
        <i class="bi bi-plus-lg"></i> Agregar Libro
    </a>
</div>
{% endblock %}
```

---

## 📤 Entrega

1. **Repositorio GitHub** (público o compartido con profesor)
2. **ZIP con:**
   - Código fuente completo
   - README.md con instrucciones
   - Capturas de pantalla de todas las páginas
   - PDF con:
     - Nombres de integrantes
     - Descripción de funcionalidades
     - Dificultades encontradas
     - Distribución del trabajo

---

## 🎤 Sustentación

**Duración:** 15 minutos por pareja

1. **Demostración (8 min):**
   - Ejecutar la aplicación (`uvicorn main:app --reload`)
   - Mostrar todas las funcionalidades
   - Navegar en modo responsive
   - Demonstrar interactividad HTMX

2. **Preguntas técnicas (7 min):**
   - Explicar código específico de FastAPI
   - Justificar decisiones de diseño
   - Explicar uso de Pydantic para validación
   - Ambos miembros deben responder

---

## 📏 Rúbrica

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **CRUD Libros** | 25 | Todas las operaciones funcionan |
| **Préstamos** | 20 | Registro y devolución funcional |
| **Búsqueda** | 10 | Filtros y ordenamiento con HTMX |
| **Validaciones** | 15 | Pydantic, mensajes claros |
| **UI/Bootstrap** | 20 | Diseño profesional y responsive |
| **HTMX** | 10 | Interactividad sin recarga |
| **TOTAL** | **100** | |

**Sustentación:** Puede reducir hasta 30% si no demuestran dominio

---

## ⚠️ Notas Importantes

- **NO usar Scaffolding automático** (debe escribir el código)
- Puede usar SQLite o PostgreSQL
- El proyecto debe compilar y ejecutar sin errores
- Ambos integrantes deben entender todo el código
- Usar type hints en todo el código

---

**Fecha límite:** Jueves 26 de marzo de 2026, 23:59
**Sustentación:** En clase del jueves 26 de marzo
**UNAULA - POO II - 2026-I**
