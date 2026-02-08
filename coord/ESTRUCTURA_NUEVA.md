# ESTRUCTURA NUEVA DEL CURSO IF0100

**Versión:** 1.0
**Fecha:** 2026-02-07
**Basado en:** memory-bank/ESTRATEGIA_REDISENIO.md

---

## 1. RESUMEN DE CAMBIOS ESTRUCTURALES

### Contenido Eliminado/Deprecado
- `clases/` → Archivos originales (archivar)
- `clases-html/` → Mantener como backup (clases-html-old/)

### Contenido Nuevo
- `notebooks/` → Jupyter Notebooks para aprendizaje interactivo
- `clases-html-v2/` → Nueva versión HTML con contenido Python
- `src/taskflow/` → Código del proyecto integrador
- `database/` → Scripts de base de datos
- `docs/` → Documentación del proyecto

---

## 2. ÁRBOL COMPLETO DE DIRECTORIOS

```
IF0100-POO-II/
│
├── README.md                                    # Actualizado con nueva estructura
├── CHANGELOG.md                                 # Historial de cambios
├── .gitignore                                   # Ignorar archivos sensibles
├── pyproject.toml                               # Configuración Python moderna
├── requirements.txt                             # Dependencias Python
├── pytest.ini                                   # Configuración pytest
├── .coveragerc                                  # Configuración coverage
│
├── planificacion/                               # DOCUMENTACIÓN PEDAGÓGICA
│   ├── syllabus.md                              # Syllabus oficial actualizado
│   ├── cronograma-actualizado-2026.md           # Cronograma semanal
│   ├── objetivos-por-clase.md                   # [NUEVO] Objetivos detallados
│   ├── progresion-tecnica.md                    # [NUEVO] Progresión notebooks→VSCode
│   ├── rubricas.md                              # [NUEVO] Rúbricas de evaluación
│   └── guias-taller.md                          # [NUEVO] Guías paso a paso
│
├── coord/                                       # COORDINACIÓN DEL REDISEÑO
│   ├── PLAN_TRABAJO.md                          # [NUEVO] Este archivo
│   ├── ESTRUCTURA_NUEVA.md                      # [NUEVO] Árbol de carpetas
│   ├── STATUS.md                                # Estado actual del curso
│   ├── STACK.md                                 # Stack tecnológico
│   ├── CLASS_STATUS.md                          # Estado de cada clase
│   ├── REVIEW_CHECKLIST.md                      # Checklist de revisión
│   ├── LOCKS/                                   # Locks de edición de archivos
│   ├── AGENTS.md                                # Definición de agentes
│   ├── WORK_INSTRUCTIONS.md                     # Instrucciones de trabajo
│   ├── SWARM_INSTRUCTIONS.md                    # Instrucciones para swarm
│   └── reportes/                                # [NUEVO] Reportes de agentes
│       ├── reporte-pep8.md                      # Reporte PEP 8 compliance
│       ├── reporte-types.md                     # Reporte type hints
│       ├── reporte-docs.md                      # Reporte docstrings
│       ├── reporte-html.md                      # Reporte validación HTML
│       ├── reporte-e2e.md                       # Reporte testing E2E
│       ├── reporte-links.md                     # Reporte enlaces rotos
│       ├── reporte-responsive.md                # Reporte responsive design
│       ├── reporte-qa-final.md                  # Reporte final QA
│       └── REPORTE_FINAL.md                     # Reporte final del proyecto
│
├── memory-bank/                                 # CONTEXTO DEL PROYECTO
│   ├── projectbrief.md                          # Descripción del curso
│   ├── productContext.md                        # Por qué existe el curso
│   ├── techContext.md                           # Stack tecnológico
│   ├── systemPatterns.md                        # Patrones de arquitectura
│   ├── activeContext.md                         # Estado actual
│   ├── progress.md                              # Progreso del proyecto
│   ├── ESTRATEGIA_REDISENIO.md                  # Estrategia completa
│   └── instructions/                            # [NUEVO] Instrucciones específicas
│       ├── python-patterns.md                   # Patrones Python
│       ├── fastapi-patterns.md                  # Patrones FastAPI
│       └── testing-patterns.md                  # Patrones de testing
│
├── notebooks/                                   # [NUEVO] JUPYTER NOTEBOOKS
│   ├── README.md                                # Guía de uso de notebooks
│   ├── unidad-00/                               # Fundamentos de Python
│   │   ├── 00-01-introduccion-python.ipynb      # Variables, tipos, operadores
│   │   ├── 00-02-estructuras-control.ipynb      # if/else, loops, break/continue
│   │   ├── 00-03-estructuras-datos.ipynb        # listas, diccionarios, conjuntos
│   │   └── 00-04-modulos-errores.ipynb          # imports, excepciones
│   │
│   ├── unidad-01/                               # POO Avanzada
│   │   ├── 01-01-clases-objetos.ipynb           # Clases, __init__, self
│   │   ├── 01-02-encapsulamiento.ipynb          # @property, dataclasses
│   │   ├── 01-03-herencia-composicion.ipynb     # Herencia, super(), composición
│   │   ├── 01-04-polimorfismo.ipynb             # Métodos mágicos, duck typing
│   │   └── 01-05-interfaces.ipynb               # ABC, @abstractmethod
│   │
│   ├── unidad-02/                               # Técnicas de Desarrollo
│   │   ├── 02-01-tdd-intro.ipynb                # Introducción a TDD
│   │   ├── 02-02-ciclo-red-green-refactor.ipynb # Ciclo TDD completo
│   │   ├── 02-03-mocks-fixtures.ipynb           # pytest fixtures y mocks
│   │   ├── 02-04-bdd-intro.ipynb                # BDD con behave
│   │   └── 02-05-ddd-intro.ipynb                # DDD: dominio rico
│   │
│   └── assets/                                  # Assets para notebooks
│       └── images/                              # Imágenes para notebooks
│
├── clases-html-v2/                              # [NUEVO] HTML ACTUALIZADO
│   ├── index.html                               # Índice de clases
│   ├── templates/                               # Plantillas base
│   │   ├── clase-template.html                  # Plantilla para nueva clase
│   │   └── unidad-template.html                 # Plantilla para unidad
│   │
│   ├── unidad-00/                               # Fundamentos Python
│   │   ├── clase-00-01-introduccion.html
│   │   ├── clase-00-02-control.html
│   │   ├── clase-00-03-datos.html
│   │   └── clase-00-04-modulos.html
│   │
│   ├── unidad-01/                               # POO Avanzada
│   │   ├── clase-01-01-clases-objetos.html
│   │   ├── clase-01-02-encapsulamiento.html
│   │   ├── clase-01-03-herencia.html
│   │   ├── clase-01-04-polimorfismo.html
│   │   ├── clase-01-05-interfaces.html
│   │   ├── clase-01-06-modelos-dtos.html
│   │   ├── clase-01-07-patrones.html
│   │   └── clase-01-08-evaluacion.html
│   │
│   ├── unidad-02/                               # Técnicas Desarrollo
│   │   ├── clase-02-01-tdd-intro.html
│   │   ├── clase-02-02-ciclo-tdd.html
│   │   ├── clase-02-03-mocks.html
│   │   ├── clase-02-04-bdd.html
│   │   ├── clase-02-05-ddd-entidades.html
│   │   ├── clase-02-06-ddd-repositorios.html
│   │   └── clase-02-07-evaluacion.html
│   │
│   ├── unidad-03/                               # Desarrollo Backend
│   │   ├── clase-03-01-fastapi-intro.html
│   │   ├── clase-03-02-pydantic.html
│   │   ├── clase-03-03-dependencias.html
│   │   ├── clase-03-04-postgresql.html
│   │   ├── clase-03-05-crud.html
│   │   ├── clase-03-06-jwt-auth.html
│   │   └── clase-03-07-evaluacion.html
│   │
│   ├── unidad-04/                               # Desarrollo Frontend
│   │   ├── clase-04-01-jinja2-intro.html
│   │   ├── clase-04-02-htmx.html
│   │   ├── clase-04-03-formularios.html
│   │   ├── clase-04-04-bootstrap.html
│   │   ├── clase-04-05-estado.html
│   │   ├── clase-04-06-dashboard.html
│   │   └── clase-04-07-evaluacion.html
│   │
│   └── unidad-05/                               # Proyecto Final
│       ├── clase-05-01-integracion.html
│       ├── clase-05-02-documentacion.html
│       ├── clase-05-03-sustentacion.html
│       └── clase-05-04-examen-final.html
│
├── clases-html-old/                             # [BACKUP] HTML ORIGINAL
│   └── (contenido anterior migrado aquí)
│
├── src/                                         # [NUEVO] CÓDIGO DEL PROYECTO
│   └── taskflow/                                # Paquete principal
│       ├── __init__.py                          # Init del paquete
│       ├── config.py                            # Configuración (settings)
│       ├── main.py                              # Entry point
│       │
│       ├── models/                              # Modelos de dominio
│       │   ├── __init__.py
│       │   ├── base.py                          # Clase base para modelos
│       │   ├── usuario.py                       # Modelo Usuario
│       │   ├── proyecto.py                      # Modelo Proyecto
│       │   ├── tarea.py                         # Modelo Tarea
│       │   └── comentario.py                    # Modelo Comentario
│       │
│       ├── schemas/                             # [NUEVO] Pydantic schemas
│       │   ├── __init__.py
│       │   ├── usuario.py                       # Schemas request/response
│       │   ├── proyecto.py
│       │   ├── tarea.py
│       │   └── auth.py                          # Login, register schemas
│       │
│       ├── services/                            # Lógica de negocio
│       │   ├── __init__.py
│       │   ├── base_service.py                  # Clase base
│       │   ├── usuario_service.py               # Servicio de usuarios
│       │   ├── proyecto_service.py              # Servicio de proyectos
│       │   ├── tarea_service.py                 # Servicio de tareas
│       │   └── auth_service.py                  # Autenticación
│       │
│       ├── repositories/                        # Acceso a datos
│       │   ├── __init__.py
│       │   ├── base.py                          # Repositorio base
│       │   ├── usuario_repository.py            # Repo usuarios
│       │   ├── proyecto_repository.py           # Repo proyectos
│       │   └── tarea_repository.py              # Repo tareas
│       │
│       ├── api/                                 # [NUEVO] API REST FastAPI
│       │   ├── __init__.py
│       │   ├── app.py                           # Aplicación FastAPI
│       │   ├── dependencies.py                  # Dependencias inyectables
│       │   ├── middleware.py                    # Middleware personalizado
│       │   ├── security.py                      # JWT, password hashing
│       │   ├── database.py                      # Conexión a BD
│       │   └── routes/                          # Endpoints
│       │       ├── __init__.py
│       │       ├── auth.py                      # /auth/* endpoints
│       │       ├── usuarios.py                  # /usuarios/* endpoints
│       │       ├── proyectos.py                 # /proyectos/* endpoints
│       │       └── tareas.py                    # /tareas/* endpoints
│       │
│       ├── templates/                           # [NUEVO] TEMPLATES JINJA2
│       │   ├── base.html                        # Layout principal
│       │   ├── index.html                       # Home page
│       │   ├── login.html                       # Login page
│       │   ├── registro.html                    # Registro page
│       │   ├── dashboard.html                   # Dashboard principal
│       │   │
│       │   ├── usuarios/                        # Templates usuarios
│       │   │   ├── list.html
│       │   │   ├── detail.html
│       │   │   └── form.html
│       │   │
│       │   ├── proyectos/                       # Templates proyectos
│       │   │   ├── list.html
│       │   │   ├── detail.html
│       │   │   └── form.html
│       │   │
│       │   ├── tareas/                          # Templates tareas
│       │   │   ├── list.html
│       │   │   ├── detail.html
│       │   │   └── form.html
│       │   │
│       │   └── componentes/                     # Parciales Jinja2
│       │       ├── navbar.html
│       │       ├── footer.html
│       │       ├── alert.html
│       │       └── pagination.html
│       │
│       └── static/                              # [NUEVO] ARCHIVOS ESTÁTICOS
│           ├── css/
│           │   └── styles.css                   # Estilos personalizados
│           ├── js/
│           │   └── main.js                      # JavaScript personalizado
│           └── img/                             # Imágenes del proyecto
│
├── tests/                                       # [NUEVO] PRUEBAS
│   ├── __init__.py
│   ├── conftest.py                              # Fixtures globales
│   ├── test_models.py                           # Tests de modelos
│   ├── test_services.py                         # Tests de servicios
│   ├── test_repositories.py                    # Tests de repos
│   ├── test_api.py                              # Tests de API
│   ├── test_e2e.py                              # Tests end-to-end
│   └── fixtures/                                # Datos de prueba
│       ├── usuarios.json
│       ├── proyectos.json
│       └── tareas.json
│
├── database/                                    # [NUEVO] BASE DE DATOS
│   ├── README.md                                # Guía de BD
│   ├── schema.sql                               # Schema completo
│   ├── setup.sql                                # Script de setup inicial
│   ├── teardown.sql                             # Script de limpieza
│   │
│   ├── migrations/                              # Migraciones
│   │   ├── 001_initial_schema.sql
│   │   ├── 002_add_constraints.sql
│   │   └── 003_add_indexes.sql
│   │
│   ├── seeds/                                   # Datos de prueba
│   │   ├── desarrollo.sql                       # Datos para desarrollo
│   │   └── pruebas.sql                          # Datos para tests
│   │
│   └── consultas.md                             # Consultas frecuentes
│
├── docs/                                        # [NUEVO] DOCUMENTACIÓN
│   ├── README.md                                # Índice de documentación
│   ├── instalacion.md                           # Guía de instalación
│   ├── arquitectura.md                          # Arquitectura del sistema
│   ├── api.md                                   # Documentación de API
│   ├── contribucion.md                          # Guía de contribución
│   ├── deployment.md                            # Guía de despliegue
│   └── diagrams/                                # Diagramas
│       ├── arquitectura.png
│       ├── modelo-datos.png
│       └── flujo-auth.png
│
├── evaluaciones/                                # EVALUACIONES (MANTENER)
│   ├── evaluacion-01-conceptos-poo.md           # Actualizada
│   ├── evaluacion-02-tecnicas-desarrollo.md     # Actualizada
│   ├── evaluacion-03-desarrollo-web.md          # Actualizada
│   ├── evaluacion-04-persistencia.md            # [NUEVA] PostgreSQL
│   ├── evaluacion-05-proyecto-integrador.md     # [NUEVA] TaskFlow
│   └── evaluacion-06-examen-final.md            # Actualizada
│
├── laboratorios/                                # LABORATORIOS (ACTUALIZAR)
│   ├── lab-01-python-basico/                    # Mantener
│   ├── lab-02-herencia-polimorfismo/            # Actualizar
│   ├── lab-03-tdd-testing/                      # Actualizar
│   ├── lab-04-fastapi-basico/                   # [NUEVO] Reemplazar Angular
│   ├── lab-05-postgresql/                       # [NUEVO] Reemplazar SQL Server
│   └── lab-06-proyecto-completo/                # [NUEVO] TaskFlow
│
├── proyectos/                                   # PROYECTOS DE ESTUDIANTES
│   └── .gitkeep
│
├── assets/                                      # ASSETS COMPARTIDOS
│   ├── css/                                     # Estilos compartidos
│   │   ├── codeblocks.css                       # Para HTML de clases
│   │   ├── print.css                            # Estilos de impresión
│   │   └── styles-v2.css                        # [NUEVO] Estilos actualizados
│   │
│   ├── js/                                      # JavaScript compartido
│   │   └── prism.js                             # Syntax highlighting
│   │
│   ├── svg/                                     # Diagramas SVG
│   │   ├── clase-01-*.svg
│   │   ├── clase-02-*.svg
│   │   └── ...
│   │
│   └── infografias/                             # Infografías (MANTENER)
│       ├── clase-01-*.png
│       ├── clase-02-*.png
│       └── ...
│
├── .venv/                                       # Virtual environment (gitignore)
├── .vscode/                                     # VS Code config
│   ├── settings.json
│   └── mcp.json
│
└── .git/                                        # Git repository
```

---

## 3. EXPLICACIÓN DE DIRECTORIOS CLAVE

### notebooks/
**Propósito:** Material de aprendizaje interactivo con Jupyter Notebooks
**Contenido:**
- Unidad 0: Repaso de Python (4 notebooks)
- Unidad 1: POO Avanzada (5 notebooks)
- Unidad 2: Técnicas de Desarrollo (5 notebooks)

**Uso pedagógico:**
- Exploración interactiva de conceptos
- Ejercicios con validación automática
- Feedback inmediato

### clases-html-v2/
**Propósito:** Material teórico de referencia en HTML
**Contenido:**
- Unidades 0-5 completas
- 35+ clases HTML actualizadas
- Responsive, imprimible, con syntax highlighting

**Uso pedagógico:**
- Material de referencia teórica
- Lectura previa a clases
- Material de estudio para exámenes

### src/taskflow/
**Propósito:** Código del proyecto integrador TaskFlow
**Estructura:**
- `models/`: Modelos de dominio con dataclasses
- `services/`: Lógica de negocio
- `repositories/`: Acceso a datos (abstracción)
- `api/`: FastAPI REST API
- `templates/`: Jinja2 templates con HTMX
- `static/`: CSS, JS, imágenes

**Progresión:**
- Clase 1.1-1.5: Notebooks → Copiar a modelos
- Clase 1.6+: VSCode puro
- Clase 3.1+: API FastAPI
- Clase 4.1+: Templates Jinja2

### database/
**Propósito:** Scripts de base de datos PostgreSQL
**Contenido:**
- `schema.sql`: Schema completo con constraints
- `migrations/`: Migraciones versionadas
- `seeds/`: Datos de prueba
- `consultas.md`: Consultas frecuentes documentadas

### tests/
**Propósito:** Suite de pruebas completa
**Contenido:**
- `test_models.py`: Tests de modelos
- `test_services.py`: Tests de servicios
- `test_repositories.py`: Tests de repos
- `test_api.py`: Tests de endpoints
- `test_e2e.py`: Tests end-to-end

**Cobertura esperada:** > 80%

---

## 4. PATRONES DE ORGANIZACIÓN

### Patrones de Nomenclatura

**Archivos Python:**
- Módulos: `nombre_modulo.py` (snake_case)
- Clases: `NombreClase` (PascalCase)
- Funciones: `nombre_funcion()` (snake_case)
- Constantes: `NOMBRE_CONSTANTE` (UPPER_SNAKE_CASE)

**Archivos HTML:**
- Clases: `clase-XX-YY-titulo.html`
- Templates: `nombre-accion.html` (ej: `list.html`, `detail.html`)

**Notebooks:**
- Formato: `XX-YY-titulo.ipynb`
- XX: Número de unidad (00-05)
- YY: Número de clase (01-08)

### Patrones de Estructura

**Módulos Python:**
```python
"""
Archivo: src/taskflow/models/usuario.py

Módulo: Modelos de dominio - Usuario
Unidad: 1.1 - Clases y Objetos
"""

from dataclasses import dataclass
# imports...
```

**Templates Jinja2:**
```jinja2
{# Archivo: src/taskflow/templates/proyectos/list.html #}
{% extends "base.html" %}
{% block title %}Proyectos - TaskFlow{% endblock %}
```

---

## 5. MIGRACIÓN DESDE ESTRUCTURA ANTIGUA

### Archivos a Migrar

| Desde | Hasta | Acción |
|-------|-------|--------|
| `clases-html/` | `clases-html-old/` | Mover como backup |
| `clases/` | `archivos/` | Archivar |
| `evaluaciones/*.md` | `evaluaciones/*.md` | Actualizar contenido |
| `laboratorios/*` | `laboratorios/*` | Actualizar referencias |

### Archivos a Crear

| Archivo | Propósito | Prioridad |
|---------|-----------|----------|
| `notebooks/unidad-00/*.ipynb` | Repaso Python | Alta |
| `notebooks/unidad-01/*.ipynb` | POO Avanzada | Alta |
| `src/taskflow/models/*.py` | Modelos TaskFlow | Alta |
| `database/schema.sql` | Schema BD | Alta |
| `clases-html-v2/**/*.html` | HTML actualizado | Media |
| `tests/*.py` | Suite de tests | Media |
| `docs/*.md` | Documentación | Baja |

---

## 6. SCRIPTS DE UTILIDAD

### Script para crear estructura

```bash
#!/bin/bash
# setup-estructura.sh

# Directorios principales
mkdir -p notebooks/{unidad-00,unidad-01,unidad-02}
mkdir -p clases-html-v2/{unidad-00,unidad-01,unidad-02,unidad-03,unidad-04,unidad-05}/templates
mkdir -p src/taskflow/{models,schemas,services,repositories,api/routes,templates,static/{css,js,img}}
mkdir -p tests/fixtures
mkdir -p database/{migrations,seeds}
mkdir -p docs/diagrams
mkdir -p coord/reportes

# Archivos vacíos con __init__.py
touch src/taskflow/__init__.py
touch src/taskflow/{models,schemas,services,repositories,api,api/routes}/__init__.py
touch tests/__init__.py

echo "Estructura creada exitosamente"
```

### Script para validar estructura

```bash
#!/bin/bash
# validate-estructura.sh

# Verificar directorios clave
dirs=(
    "notebooks/unidad-00"
    "notebooks/unidad-01"
    "src/taskflow/models"
    "src/taskflow/api"
    "database"
    "tests"
)

for dir in "${dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "✓ $dir existe"
    else
        echo "✗ $dir NO existe"
    fi
done
```

---

## 7. GUÍA DE MIGRACIÓN PASO A PASO

### Paso 1: Backup
1. Copiar `clases-html/` a `clases-html-old/`
2. Crear commit de seguridad en Git

### Paso 2: Crear estructura nueva
1. Ejecutar script `setup-estructura.sh`
2. Validar con `validate-estructura.sh`

### Paso 3: Migrar contenido
1. Actualizar referencias C# → Python en evaluaciones
2. Crear notebooks Unidad 0 (repaso Python)
3. Crear modelos del proyecto TaskFlow

### Paso 4: Validar
1. Ejecutar tests de validación
2. Probar notebooks
3. Verificar enlaces en HTML

---

## 8. CRITERIOS DE VALIDACIÓN

Una vez creada la estructura, verificar:

### Estructura de Directorios
- [ ] Todos los directorios creados
- [ ] `__init__.py` en todos los paquetes Python
- [ ] `.gitignore` configurado correctamente
- [ ] `requirements.txt` creado

### Archivos de Configuración
- [ ] `pytest.ini` configurado
- [ ] `.coveragerc` configurado
- [ ] `pyproject.toml` creado

### Git
- [ ] Estructura commiteada
- [ ] Tag de versión creado
- [ ] README.md actualizado

---

**FIN DEL DOCUMENTO DE ESTRUCTURA**

**Próximo paso:** Ejecutar script de creación de estructura
**Validación:** Verificar todos los directorios creados
