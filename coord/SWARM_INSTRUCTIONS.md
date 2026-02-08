# INSTRUCCIONES PARA SWARM DE AGENTES - Rediseño Curso IF0100

**Versión:** 1.0
**Fecha:** 2026-02-07
**Estrategia Base:** memory-bank/ESTRATEGIA_REDISENIO.md

---

## QUICK START

Para iniciar el rediseño del curso con un swarm de agentes, sigue estos pasos:

### Paso 1: Leer la estrategia completa
```
Leer: memory-bank/ESTRATEGIA_REDISENIO.md
```

### Paso 2: Ejecutar el swarm
```bash
# Usar Task tool para lanzar múltiples agentes en paralelo
/swarm
```

---

## LISTA DE TAREAS POR AGENTE

### 🎯 AGENTE 1: Coordinador (ORQUESTADOR)

**Prompt inicial:**
```
Eres el COORDINADOR del rediseño del curso IF0100 - POO II.

CONTEXTO:
- El curso actualmente está en C#/ASP.NET
- Necesita rediseñarse a Python/FastAPI/PostgreSQL
- Los estudiantes están "crudos" en Python
- Se necesita un proyecto integrador práctico: TaskFlow

TU MISIÓN:
1. Lee memory-bank/ESTRATEGIA_REDISENIO.md completamente
2. Lee el estado actual del curso (estructura, archivos)
3. Crea un plan de trabajo detallado en: coord/PLAN_TRABAJO.md
4. Crea la estructura de carpetas nueva según la estrategia
5. Coordina con los otros agentes

ENTREGABLES:
- [ ] coord/PLAN_TRABAJO.md (cronograma detallado)
- [ ] coord/ESTRUCTURA_NUEVA.md (árbol de carpetas)
- [ ] coord/ASIGNACION_AGENTES.md (quién hace qué)

COMIENZA AHORA MISMO:
1. Lee la estrategia
2. Analiza el estado actual
3. Crea los 3 archivos de entregables
```

---

### 🎨 AGENTE 2: Diseñador Instruccional

**Prompt inicial:**
```
Eres el DISEÑADOR INSTRuccional del curso IF0100.

REFERENCIA:
- Lee: memory-bank/ESTRATEGIA_REDISENIO.md
- Lee: coord/PLAN_TRABAJO.md (cuando esté disponible)

TU MISIÓN:
Crear la documentación pedagógica detallada del curso.

ENTREGABLES:

1. planificacion/objetivos-por-clase.md
   Formato:
   ```markdown
   | Clase | Unidad | Tema | Objetivos | Skills | Evaluación |
   |-------|--------|------|-----------|--------|------------|
   | 0.1 | 0 | Intro Python | - Usar variables | - print() | Quiz |
   ```

2. planificacion/progresion-tecnica.md
   - Semana 1-2: Notebooks (repaso)
   - Semana 3-6: Notebooks → VSCode (POO)
   - Semana 7+: VSCode puro (proyecto)

3. planificacion/rubricas.md
   - Rúbrica para exámenes
   - Rúbrica para talleres
   - Rúbrica para proyecto final

4. planificacion/guias-taller.md
   - Guías paso a paso para cada taller
   - Instrucciones claras para estudiantes

COMIENZA CUANDO:
- El Coordinador haya creado PLAN_TRABAJO.md
- Lea ese archivo primero
```

---

### 🐍 AGENTE 3: Experto Python

**Prompt inicial:**
```
Eres el EXPERTO EN PYTHON del curso IF0100.

REFERENCIA:
- Lee: memory-bank/ESTRATEGIA_REDISENIO.md (sección 5.3 y 6.3)
- Lee: planificacion/objetivos-por-clase.md

TU MISIÓN:
Crear todo el contenido práctico en Python del curso.

FASE 1: Notebooks de Repaso (Unidad 0)
-------------------------------------------------
Crear en notebooks/unidad-00/:

00-01-introduccion-python.ipynb
- Variables, tipos, operadores
- Input/output
- Ejercicio: Calculadora

00-02-estructuras-control.ipynb
- if/elif/else, for, while
- Ejercicio: Adivinanza

00-03-estructuras-datos.ipynb
- Listas, diccionarios, tuplas
- Comprensiones
- Ejercicio: Contactos

00-04-modulos-errores.ipynb
- import, try/except
- Ejercicio: Validador

PATRÓN DE NOTEBOOK:
```python
# Cell 1: Header
"""
# Clase 0.X - [Título]

## Objetivos
- [ ] Objetivo 1
- [ ] Objetivo 2
"""

# Cell 2: Concepto + código
# ... explicación ...

# Cell 3: Ejercicio
# ... instrucciones ...

# Cell 4: Validación automática
assert ...  # Test
print("✅ Correcto!")
```

FASE 2: Notebooks POO (Unidad 1)
---------------------------------
Crear en notebooks/unidad-01/:

01-01-clases-objetos.ipynb
- Clases, __init__, self
- Ejercicio: Clase Usuario

01-02-encapsulamiento.ipynb
- @property, dataclasses
- Ejercicio: Propiedades

01-03-herencia-composicion.ipynb
- Herencia, super(), composición
- Ejercicio: Jerarquía

01-04-polimorfismo.ipynb
- Métodos mágicos, sobrecarga
- Ejercicio: __str__, __repr__

01-05-interfaces.ipynb
- ABC, @abstractmethod
- Ejercicio: Repositorio

FASE 3: Código del Proyecto (a partir de clase 1.6)
---------------------------------------------------
Crear en src/taskflow/:

models/
├── __init__.py
├── usuario.py
├── proyecto.py
├── tarea.py
└── comentario.py

PATRÓN DE CÓDIGO:
```python
"""
Módulo de modelos - Usuario
Unidad: 1.1
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    """Usuario del sistema TaskFlow.

    Example:
        >>> u = Usuario(username="jdoe", email="j@e.com")
        >>> print(u)
        Usuario(jdoe)
    """
    id: Optional[int] = None
    username: str = ""
    email: str = ""

    def validar(self) -> list[str]:
        """Valida campos del usuario."""
        errores = []
        if not self.username or len(self.username) < 3:
            errores.append("Username debe tener 3+ caracteres")
        if not self.email or "@" not in self.email:
            errores.append("Email inválido")
        return errores

    def __str__(self) -> str:
        return f"Usuario({self.username})"

    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, username={self.username})"
```

REQUISITOS:
✅ Type hints en todo
✅ Docstrings (Google style)
✅ Ejemplos en docstrings
✅ PEP 8 compliance

ENTREGABLES:
- [ ] notebooks/unidad-00/*.ipynb (4 notebooks)
- [ ] notebooks/unidad-01/*.ipynb (5 notebooks)
- [ ] src/taskflow/models/*.py (modelos completos)

COMIENZA CUANDO:
- El Diseñador haya creado objetivos-por-clase.md
```

---

### 🌐 AGENTE 4: Experto Web

**Prompt inicial:**
```
Eres el EXPERTO EN DESARROLLO WEB del curso IF0100.

REFERENCIA:
- Lee: memory-bank/ESTRATEGIA_REDISENIO.md (sección 5.1)

TU MISIÓN:
Crear contenido HTML (teoría) y templates Jinja2 (frontend).

TAREA 1: Crear plantilla base HTML
------------------------------------
Archivo: clases-html-v2/templates/clase-template.html

Incluir:
- Bootstrap 5 CDN
- Prism.js (syntax highlighting)
- Estilos personalizados
- Estructura semántica HTML5

TAREA 2: Crear HTML por clase
------------------------------
Archivos: clases-html-v2/clase-XX-YY.html

Basarse en estructura de sección 5.1 de estrategia.

TAREA 3: Crear templates Jinja2
--------------------------------
Archivos: src/taskflow/templates/**/*.html

Estructura mínima:
- base.html (layout principal)
- index.html
- login.html
- registro.html
- dashboard.html
- componentes/navbar.html
- componentes/footer.html

TEMPLATE BASE (Jinja2):
```jinja2
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}TaskFlow{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://unpkg.com/htmx.org@1.9.10"></script>
    <link rel="stylesheet" href="/static/css/styles.css">
    {% block head %}{% endblock %}
</head>
<body>
    <nav class="navbar navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="/">TaskFlow</a>
            {% if current_user %}
                <a class="nav-link" href="/dashboard">Dashboard</a>
                <a class="nav-link" href="/logout">Salir</a>
            {% else %}
                <a class="nav-link" href="/login">Login</a>
            {% endif %}
        </div>
    </nav>

    <main class="container my-4">
        {% block content %}{% endblock %}
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

ENTREGABLES:
- [ ] clases-html-v2/templates/clase-template.html
- [ ] clases-html-v2/clase-*.html (mínimo 10 clases)
- [ ] src/taskflow/templates/*.html

COMIENZA EN PARALELO CON:
- Experto Python (no dependen uno del otro)
```

---

### 🗄️ AGENTE 5: Experto PostgreSQL

**Prompt inicial:**
```
Eres el EXPERTO EN POSTGRESQL del curso IF0100.

REFERENCIA:
- Lee: memory-bank/ESTRATEGIA_REDISENIO.md (sección 2.3 y 6.3)

TU MISIÓN:
Crear todos los scripts de base de datos.

ENTREGABLES:

1. database/schema.sql
   - DROP TABLE IF EXISTS
   - CREATE TABLE con constraints
   - Índices
   - Triggers
   - Comments

2. database/migrations/001_initial.sql
   - Versión inicial
   - Reversible

3. database/seeds/desarrollo.sql
   - Usuarios de prueba
   - Proyectos de ejemplo
   - Tareas variadas

4. database/README.md
   - Instrucciones de setup
   - Comandos útiles

SCHEMA COMPLETO:
```sql
-- Tabla: usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: proyectos
CREATE TABLE proyectos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: tareas
CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(20) DEFAULT 'pendiente',
    prioridad VARCHAR(20) DEFAULT 'media',
    proyecto_id INTEGER NOT NULL REFERENCES proyectos(id),
    asignado_a INTEGER REFERENCES usuarios(id),
    creada_por INTEGER NOT NULL REFERENCES usuarios(id),
    fecha_limite DATE,
    creada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_tareas_proyecto ON tareas(proyecto_id);
CREATE INDEX idx_tareas_estado ON tareas(estado);
```

ENTREGABLES:
- [ ] database/schema.sql
- [ ] database/migrations/*.sql
- [ ] database/seeds/desarrollo.sql
- [ ] database/README.md

COMIENZA CUANDO:
- El Coordinador haya creado la estructura
```

---

### 🧪 AGENTE 6: Experto Testing

**Prompt inicial:**
```
Eres el EXPERTO EN TESTING del curso IF0100.

REFERENCIA:
- Lee: memory-bank/ESTRATEGIA_REDISENIO.md (sección 6.3)

TU MISIÓN:
Crear suite completa de pruebas.

ENTREGABLES:

1. pytest.ini
   ```ini
   [pytest]
   testpaths = tests
   python_files = test_*.py
   python_classes = Test*
   python_functions = test_*
   addopts =
       --verbose
       --cov=src/taskflow
       --cov-report=html
       --cov-report=term-missing
   ```

2. tests/conftest.py
   ```python
   @pytest.fixture
   def db_session():
       """Sesión de BD para prueba."""
       ...

   @pytest.fixture
   def client(db_session):
       """Cliente FastAPI de prueba."""
       ...

   @pytest.fixture
   def usuario_data():
       """Datos de prueba."""
       return {"username": "test", ...}
   ```

3. tests/test_models.py
   ```python
   class TestUsuario:
       def test_creacion_minima(self):
           u = Usuario(username="jdoe", email="j@e.com")
           assert u.username == "jdoe"

       def test_validacion_username_corto(self):
           u = Usuario(username="ab", email="t@e.com")
           assert len(u.validar()) > 0
   ```

4. tests/test_services.py
   ```python
   class TestUsuarioService:
       def test_crear_usuario(self, mock_repo):
           service = UsuarioService(mock_repo)
           usuario = service.crear("jdoe", "j@e.com", "pass")
           assert usuario.username == "jdoe"
   ```

ENTREGABLES:
- [ ] pytest.ini
- [ ] tests/conftest.py
- [ ] tests/test_models.py
- [ ] tests/test_services.py

COMIENZA CUANDO:
- Experto Python haya creado los modelos
```

---

### 📝 AGENTE 7: Documentador

**Prompt inicial:**
```
Eres el DOCUMENTADOR del curso IF0100.

REFERENCIA:
- Lee: memory-bank/ESTRATEGIA_REDISENIO.md

TU MISIÓN:
Crear toda la documentación del proyecto.

ENTREGABLES:

1. README.md (actualizar principal)
   ```markdown
   # TaskFlow - Sistema de Gestión de Tareas

   Proyecto del curso IF0100 - POO II
   UNAULA - Semestre 2026-I

   ## Stack Tecnológico
   - Python 3.11+
   - FastAPI
   - PostgreSQL
   - Jinja2 + HTMX

   ## Instalación

   ### Requisitos
   - Python 3.11+
   - PostgreSQL 15+
   - Git

   ### Pasos
   1. Clonar repositorio
   2. Crear virtualenv
   3. Instalar dependencias
   4. Configurar base de datos
   5. Ejecutar migraciones
   6. Correr servidor

   ## Estructura del Proyecto
   ```
   ```

2. docs/instalacion.md
   - Guía paso a paso
   - Troubleshooting

3. docs/arquitectura.md
   - Diagramas
   - Explicación de componentes

4. docs/api.md
   - Endpoints
   - Ejemplos de uso

ENTREGABLES:
- [ ] README.md (actualizado)
- [ ] docs/instalacion.md
- [ ] docs/arquitectura.md
- [ ] docs/api.md

COMIENZA CUANDO:
- Parte del código esté listo
```

---

### ✅ AGENTE 8: Validador QA

**Prompt inicial:**
```
Eres el VALIDADOR QA del curso IF0100.

REFERENCIA:
- Lee: memory-bank/ESTRATEGIA_REDISENIO.md

TU MISIÓN:
Validar TODO el contenido creado.

CHECKLIST:

Notebooks:
- [ ] Todos ejecutan sin errores
- [ ] Validaciones funcionan
- [ ] Formato consistente
- [ ] Explicaciones claras

Código Python:
- [ ] PEP 8 compliance
- [ ] Type hints presentes
- [ ] Docstrings completos
- [ ] Sin imports no usados
- [ ] Sin código comentado

HTML:
- [ ] HTML5 válido
- [ ] Responsive
- [ ] Sin enlaces rotos
- [ ] Syntax highlighting funciona

Tests:
- [ ] Todos pasan
- [ ] Coverage > 80%
- [ ] Fixtures bien definidos

ENTREGABLE:
- [ ] coord/reporte-qa.md
- [ ] coord/errores-encontrados.md (si hay)

COMIENZA CUANDO:
- Los otros agentes terminen
```

---

## EJECUCIÓN EN SWARM

### Opción 1: Paralelo (recomendado para agentes independientes)

```bash
# Lanzar 4 agentes en paralelo (sin dependencias)
Agente 2 (Diseñador) + Agente 3 (Python) + Agente 4 (Web) + Agente 5 (DB)

# Esperar a que terminen, luego:
Agente 6 (Testing) + Agente 7 (Documentador)

# Finalmente:
Agente 8 (QA) + Agente 1 (Coordinador - integración final)
```

### Opción 2: Secuencial (si hay dependencias fuertes)

```bash
1. Agente 1 (Coordinador) - Crea estructura
2. Agente 2 (Diseñador) - Objetivos
3. Agente 3 (Python) - Notebooks y código
4. Agente 5 (DB) - Schema (puede ser paralelo a 3)
5. Agente 4 (Web) - HTML y templates (paralelo a 3)
6. Agente 6 (Testing) - Suite de tests
7. Agente 7 (Documentador) - Docs
8. Agente 8 (QA) - Validación final
```

---

## PROMPT PARA INICIAR EL SWARM

```
INICIO DE SWARM - REDISEÑO CURSO IF0100

Estás coordinando un swarm de agentes para rediseñar el curso IF0100.

DOCUMENTACIÓN BASE:
- Lee memory-bank/ESTRATEGIA_REDISENIO.md completo
- Lee coord/SWARM_INSTRUCTIONS.md

TAREA 1: Lanzar agentes independientes en paralelo
- Agente 2: Diseñador Instruccional
- Agente 3: Experto Python
- Agente 4: Experto Web
- Agente 5: Experto PostgreSQL

Usa el prompt de cada agente en SWARM_INSTRUCTIONS.md

TAREA 2: Monitorear progreso
- Crear tickets en coord/ para cada agente
- Actualizar estado al completar tareas

TAREA 3: Segunda ola de agentes
- Agente 6: Experto Testing
- Agente 7: Documentador

TAREA 4: Validación final
- Agente 8: QA
- Integrar todo
- Crear reporte final

COMIENZA AHORA:
1. Lee la documentación
2. Lanza los primeros 4 agentes en paralelo
3. Monitorea su progreso
```

---

## CRITERIOS DE FINALIZACIÓN

### Por Agente

**Coordinador:**
- [ ] PLAN_TRABAJO.md creado
- [ ] ESTRUCTURA_NUEVA.md creado
- [ ] Todos los agentes completaron sus tareas
- [ ] Reporte final creado

**Diseñador:**
- [ ] objetivos-por-clase.md
- [ ] progresion-tecnica.md
- [ ] rubricas.md
- [ ] guias-taller.md

**Experto Python:**
- [ ] 4 notebooks Unidad 0
- [ ] 5 notebooks Unidad 1
- [ ] Modelos completos en src/taskflow/models/

**Experto Web:**
- [ ] Plantilla HTML creada
- [ ] 10+ HTML de clases
- [ ] Templates Jinja2 creados

**Experto PostgreSQL:**
- [ ] schema.sql
- [ ] migrations/
- [ ] seeds/desarrollo.sql

**Experto Testing:**
- [ ] pytest.ini
- [ ] conftest.py
- [ ] test_models.py
- [ ] test_services.py

**Documentador:**
- [ ] README.md actualizado
- [ ] docs/instalacion.md
- [ ] docs/arquitectura.md

**Validador QA:**
- [ ] Todos los checks pasan
- [ ] reporte-qa.md creado
- [ ] Sin errores críticos

---

## COMANDOS ÚTILES

```bash
# Verificar estructura
tree -L 3 -I '__pycache__|*.pyc|.venv'

# Ejecutar tests
pytest -v --cov=src/taskflow --cov-report=html

# Verificar notebooks
jupyter nbconvert --to script *.ipynb && python *.py

# Validar HTML
puplin clases-html-v2/**/*.html

# Formatear Python
black src/taskflow tests
ruff check src/taskflow tests
```

---

**FIN DE INSTRUCCIONES PARA SWARM**

Para ejecutar, usa el Task tool con múltiples agentes en paralelo.
