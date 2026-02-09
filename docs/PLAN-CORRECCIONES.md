# Plan de Correcciones - IF0100-POO-II

**Fecha:** 2026-02-09
**Basado en:** ANALISIS-CURSO.md
**Estado:** Listo para implementación

---

## Cambios Necesarios por Prioridad

### PRIORIDAD ALTA: Críticos

#### 1. Corregir Evaluación 2 - Técnicas de Desarrollo

**Archivo:** `evaluaciones/evaluacion-02-tecnicas-desarrollo.md`

**Cambios:**
- [ ] Convertir ejemplos de C# NUnit a Python pytest
- [ ] Cambiar estructura de proyecto de `.cs` a `.py`
- [ ] Reemplazar NUnit/Moq con pytest/mocker
- [ ] Actualizar recursos a documentación de Python

**Antes (C#):**
```csharp
[TestFixture]
public class CarritoTests
{
    [Test]
    public void AgregarProducto_CarritoVacio_TieneUnItem() { }
}
```

**Después (Python):**
```python
import pytest

class TestCarrito:
    def test_agregar_producto_carrito_vacio_tiene_un_item(self):
        pass
```

**Archivos afectados:** 1
**Tiempo estimado:** 2 horas

---

#### 2. Corregir Evaluación 3 - Desarrollo Web

**Archivo:** `evaluaciones/evaluacion-03-desarrollo-web.md`

**Cambios:**
- [ ] Cambiar título de "ASP.NET" a "FastAPI"
- [ ] Convertir estructura MVC C# a estructura FastAPI
- [ ] Cambiar Razor (.cshtml) a Jinja2 (.html.j2)
- [ ] Reemplazar Controllers/.cs por APIRouter de FastAPI
- [ ] Actualizar ejemplos de código a Python

**Antes (ASP.NET):**
```
BibliotecaWeb/
├── Controllers/
│   ├── HomeController.cs
│   └── LibrosController.cs
├── Views/
│   └── Libros/
│       └── Index.cshtml
```

**Después (FastAPI):**
```
biblioteca_web/
├── routers/
│   ├── __init__.py
│   ├── home.py
│   └── libros.py
├── templates/
│   ├── base.html
│   └── libros/
│       ├── index.html
│       └── detail.html
```

**Archivos afectados:** 1
**Tiempo estimado:** 3 horas

---

#### 3. Corregir Evaluación 4 - Persistencia de Datos

**Archivo:** `evaluaciones/evaluacion-04-persistencia-adonet.md`

**Cambios:**
- [ ] Cambiar título de "ADO.NET" a "SQLAlchemy"
- [ ] Convertir SqlConnection a SQLAlchemy Engine
- [ ] Cambiar SQL Server (IDENTITY) a PostgreSQL (SERIAL)
- [ ] Reemplazar SqlCommand con SQLAlchemy ORM
- [ ] Actualizar ejemplos a Python

**Antes (ADO.NET):**
```csharp
using (var conn = new SqlConnection(connectionString))
{
    using (var cmd = new SqlCommand("SELECT * FROM Productos", conn))
    {
        conn.Open();
        // ...
    }
}
```

**Después (SQLAlchemy):**
```python
from sqlalchemy import create_engine, text

engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM productos"))
```

**Archivos afectados:** 1
**Tiempo estimado:** 2.5 horas

---

#### 4. Corregir Evaluación 5 - CRUD Completo

**Archivo:** `evaluaciones/evaluacion-05-crud-adonet.md`

**Cambios:**
- [ ] Cambiar título de "ADO.NET" a "SQLAlchemy + FastAPI"
- [ ] Convertir estructura .NET a estructura Python
- [ ] Cambiar Windows Forms a API REST + Jinja2
- [ ] Actualizar diagramas y arquitectura

**Antes (C# + Windows Forms):**
```
SistemaInventario.Data/
├── Connection/
│   └── DatabaseConnection.cs
└── Repositories/
    └── ProductoRepository.cs
```

**Después (Python + FastAPI):**
```
sistema_inventario/
├── src/
│   ├── models/
│   │   └── producto.py
│   ├── repositories/
│   │   └── producto_repository.py
│   └── services/
│       └── inventario_service.py
```

**Archivos afectados:** 1
**Tiempo estimado:** 3 horas

---

### PRIORIDAD MEDIA: Mejoras Visuales

#### 5. Crear Directorio de Infografías

**Acción:** Crear `clases-html/assets/infografias/`

**Archivos a crear:**
- [ ] `clase-01-ecosistema-python.svg` (copia de existente o placeholder)

**Verificar:**
- [ ] Ruta en `clase-00-introduccion.html` línea 383

---

#### 6. Crear Diagrama: Herencia Múltiple y MRO

**Archivo nuevo:** `clases-html/assets/diagramas/herencia-multiple-mro.svg`

**Contenido del diagrama:**
- Visualización del Method Resolution Order
- Ejemplo de herencia diamond
- Orden de búsqueda de métodos
- Función `super()` en herencia múltiple

**Tiempo estimado:** 1.5 horas

---

#### 7. Crear Diagrama: Flujo Request/Response FastAPI

**Archivo nuevo:** `clases-html/assets/diagramas/fastapi-request-flow.svg`

**Contenido del diagrama:**
- Cliente → Uvicorn/ASGI
- Routing (Path Parameters)
- Dependency Injection
- Pydantic Validation
- Response (JSON/HTML)

**Tiempo estimado:** 2 horas

---

### PRIORIDAD BAJA: Enriquecimiento

#### 8. Crear Diagrama: Decoradores en Python

**Archivo nuevo:** `clases-html/assets/diagramas/decoradores-python.svg`

**Contenido:**
- Concepto de decorator
- Sintaxis con @decorator
- Decoradores comunes (@property, @staticmethod)
- Decoradores personalizados

#### 9. Crear Diagrama: Repository vs Service Layer

**Archivo nuevo:** `clases-html/assets/diagramas/repository-service-layer.svg`

**Contenido:**
- Separación de responsabilidades
- Flujo de datos
- Patrón de arquitectura

#### 10. Crear Diagrama: Arquitectura TaskFlow

**Archivo nuevo:** `clases-html/assets/diagramas/taskflow-arquitectura.svg`

**Contenido:**
- Estructura del proyecto integrador
- Componentes principales
- Flujo de datos

---

## Resumen de Cambios

| Prioridad | Tarea | Archivos | Tiempo |
|-----------|-------|----------|--------|
| ALTA | Eval 2 → Python/pytest | 1 | 2h |
| ALTA | Eval 3 → FastAPI | 1 | 3h |
| ALTA | Eval 4 → SQLAlchemy | 1 | 2.5h |
| ALTA | Eval 5 → Python stack | 1 | 3h |
| MEDIA | Directorio infografías | 1 | 0.5h |
| MEDIA | Diagrama MRO | 1 | 1.5h |
| MEDIA | Diagrama FastAPI flow | 1 | 2h |
| BAJA | Diagrama decoradores | 1 | 1h |
| BAJA | Diagrama Repository | 1 | 1h |
| BAJA | Diagrama TaskFlow | 1 | 1h |

**Total:**
- Archivos a modificar: 6
- Archivos a crear: 7
- Tiempo total estimado: 17.5 horas

---

## Orden de Implementación Recomendado

```
Fase 1: Evaluaciones Críticas (Día 1-2)
├── 1. Eval 2: Técnicas de Desarrollo (pytest)
├── 2. Eval 3: Desarrollo Web (FastAPI)
├── 3. Eval 4: Persistencia (SQLAlchemy)
└── 4. Eval 5: CRUD Completo (FastAPI + SQLAlchemy)

Fase 2: Recursos Visuales (Día 3)
├── 5. Directorio de infografías
├── 6. Diagrama MRO
└── 7. Diagrama FastAPI flow

Fase 3: Enriquecimiento (Día 4)
├── 8. Diagrama decoradores
├── 9. Diagrama Repository
└── 10. Diagrama TaskFlow

Fase 4: Validación (Día 5)
├── Revisión cruzada
├── Verificar enlaces
└── Commit y push
```

---

## Comandos de Validación

```bash
# Verificar que todos los HTML existen
ls clases-html/unidad-00/*.html
ls clases-html/unidad-01/*.html
ls clases-html/unidad-02/*.html
ls clases-html/unidad-03/*.html

# Verificar estructura de evaluaciones
ls evaluaciones/*.md

# Verificar diagramas existentes
ls clases-html/assets/diagramas/

# Verificar enlaces en HTML (simple check)
grep -r "href=" clases-html/*.html | head -20
```

---

## Criterios de Éxito

1. ✅ Todas las evaluaciones usan Python/FastAPI
2. ✅ Todos los ejemplos de código son funcionales en Python 3.11+
3. ✅ Los diagramas SVG se renderizan correctamente
4. ✅ Los enlaces internos funcionan
5. ✅ El proyecto TaskFlow es el eje integrador

---

**Creado:** 2026-02-09
**Versión:** 1.0
**Estado:** Listo para implementación
