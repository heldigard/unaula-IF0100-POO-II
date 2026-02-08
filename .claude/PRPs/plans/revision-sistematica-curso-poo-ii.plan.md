# Plan: Revisión Sistemática del Curso POO II - 2026-I

## Summary

Revisión y corrección completa del contenido del curso IF0100 POO II para garantizar coherencia cronológica, actualización tecnológica (Python + FastAPI en lugar de C# + ASP.NET), correcta alineación con días festivos de Colombia 2026, y estructura consistente entre teoría (clases HTML), práctica (notebooks), evaluaciones (rúbricas) y proyecto integrador (TaskFlow).

## User Story

As a docente del curso POO II
I want to have all course content systematically reviewed, corrected, and aligned
So that students have a coherent learning experience with accurate dates, consistent technology stack (Python + FastAPI), and clear evaluation criteria

## Problem Statement

El curso actual tiene múltiples inconsistencias críticas:
1. **Días de clase incorrectos**: El cronograma indica "Lunes y Miércoles" pero la clase 3 es el martes 10 de febrero
2. **Fechas de Semana Santa erróneas**: El cronograma dice 24-27 marzo pero Semana Santa 2026 es 29 marzo - 5 abril
3. **Contenido desactualizado**: cronograma.md describe C#/ASP.NET en lugar de Python/FastAPI
4. **Falta coherencia**: Entre index.html, cronograma.md y rubricas.md
5. **Proyecto TaskFlow sin implementación**: Documentación existe pero no hay código en src/
6. **Links rotos**: Repositorio GitHub no configurado

## Solution Statement

Realizar una revisión sistemática en 4 fases:
1. **Phase 1**: Corregir cronograma con fechas y días correctos
2. **Phase 2**: Actualizar documentación para coherencia Python/FastAPI
3. **Phase 3**: Verificar y completar clases HTML
4. **Phase 4**: Estructurar proyecto TaskFlow con rúbricas de evaluación

## Metadata

| Field            | Value                                         |
| ---------------- | --------------------------------------------- |
| Type             | REFACTOR                                      |
| Complexity       | HIGH                                          |
| Systems Affected | docs/, clases-html/, proyecto/, memory-bank/  |
| Dependencies     | Días festivos Colombia 2026, Semana Santa 2026 |
| Estimated Tasks  | 24                                            |

---

## UX Design

### Before State
```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                  ESTADO ACTUAL DEL CURSO POO II                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ┌─────────────┐         ┌─────────────┐         ┌─────────────┐            ║
║   │   index.html│ ──────► │cronograma.md│ ──────► │ rubricas.md │            ║
║   │ Python/FastAPI│       │  C#/ASP.NET │         │   Mixto     │            ║
║   └─────────────┘         └─────────────┘         └─────────────┘            ║
║         │                       │                       │                     ║
║         ▼                       ▼                       ▼                     ║
║   ┌─────────────┐         ┌─────────────┐         ┌─────────────┐            ║
║   │  Confusión  │         │ Fechas mal  │         │Proyecto sin │            ║
║   │  estudiantes│         │  (Lun/Mie   │         │implementación│           ║
║   └─────────────┘         └─────────────┘         └─────────────┘            ║
║                                                                               ║
║   PAIN_POINTS:                                                                ║
║   - Estudiantes no saben qué tecnología usar                                 ║
║   - Días de clase incorrectos (martes vs lun/mie)                            ║
║   - Semana Santa mal fechada (24-27 marzo vs 29 mar-5 abr)                  ║
║   - Proyecto TaskFlow sin código                                            ║
║   - Rúbricas mezclan tecnologías                                             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### After State
```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                  ESTADO CORREGIDO DEL CURSO POO II                            ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║   ┌─────────────┐         ┌─────────────┐         ┌─────────────┐            ║
║   │   index.html│ ──────► │cronograma.md│ ──────► │ rubricas.md │            ║
║   │ Python/FastAPI│       │Python/FastAPI│       │Python/FastAPI│            ║
║   │   Martes     │         │   Martes     │         │  Alineado   │            ║
║   └─────────────┘         └─────────────┘         └─────────────┘            ║
║         │                       │                       │                     ║
║         ▼                       ▼                       ▼                     ║
║   ┌─────────────┐         ┌─────────────┐         ┌─────────────┐            ║
║   │ Coherencia  │         │ Fechas      │         │Proyecto    │            ║
║   │ completa    │         │ correctas   │         │TaskFlow OK │            ║
║   └─────────────┘         └─────────────┘         └─────────────┘            ║
║                                   │                                           ║
║                                   ▼                                           ║
║                          ┌─────────────┐                                      ║
║                          │ Clases HTML │                                      ║
║                          │ coherentes  │  ◄── Cronología correcta              ║
║                          └─────────────┘                                      ║
║                                                                               ║
║   VALUE ADD:                                                                   ║
║   - Estudiantes con claridad tecnológica                                      ║
║   - Días correctos (Martes 10 feb = clase 3)                                  ║
║   - Semana Santa correcta (29 mar-5 abr)                                     ║
║   - Proyecto TaskFlow implementado                                           ║
║   - Rúbricas alineadas con Python/FastAPI                                    ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Interaction Changes
| Location | Before | After | User Impact |
|----------|--------|-------|-------------|
| `docs/cronograma.md` | Dice Lunes/Miércoles, C#/ASP.NET | Martes, Python/FastAPI | Estudiantes saben cuándo asistir y qué estudiar |
| `index.html` | Mezcla tecnologías | Coherente Python/FastAPI | Sin confusión tecnológica |
| `proyecto/README.md` | Solo documentación | Código implementado en src/ | Proyecto funcional para evaluar |
| `docs/rubricas.md` | Mezcla C# y Python | Solo Python/FastAPI | Evaluación justa y consistente |

---

## Mandatory Reading

**CRITICAL: Implementation agent MUST read these files before starting any task:**

| Priority | File | Lines | Why Read This |
|----------|------|-------|---------------|
| P0 | `docs/cronograma.md` | all | Contiene fechas y estructura a corregir |
| P0 | `docs/rubricas.md` | all | Contiene rúbricas a actualizar |
| P0 | `clases-html/index.html` | 1-968 | Índice principal del curso |
| P0 | `docs/FestivosColombia2026.txt` | all | Días festivos oficiales |
| P0 | `docs/SemanaSanta2026.txt` | all | Fechas Semana Santa correctas |
| P1 | `proyecto/README.md` | all | Estructura del proyecto TaskFlow |
| P2 | `clases-html/templates/clase-template.html` | all | Plantilla para nuevas clases |

**External Documentation:**
| Source | Section | Why Needed |
|--------|---------|------------|
| [UNAULA Calendario](https://www.unaula.edu.co/calendario-academico) | Calendario 2026-I | Verificar fechas del semestre |
| [FastAPI Docs](https://fastapi.tiangolo.com/tutorial/) | Tutorial | Referencia para proyecto |

---

## Patterns to Mirror

**ESTRUCTURA DE CLASE HTML:**

```html
<!-- SOURCE: clases-html/templates/clase-template.html -->
<!-- COPY THIS PATTERN: -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Clase X: Título - IF0100 POO II</title>
    <!-- Bootstrap 5, Prism.js, Bootstrap Icons -->
</head>
<body>
    <header>...</header>
    <main>
        <section id="objetivos">...</section>
        <section id="contenido">...</section>
        <section id="ejercicios">...</section>
        <section id="recursos">...</section>
    </main>
    <footer>...</footer>
</body>
</html>
```

**FORMATO DE CRONOGRAMA:**

```markdown
<!-- SOURCE: docs/cronograma.md -->
<!-- COPY THIS PATTERN: -->
## Unidad X: Nombre Unidad (Semanas Y-Z)

| Semana | Fecha | Clase | Tema |
|--------|-------|-------|------|
| Y | DD/MM/AAAA | Clase XX | Descripción |
```

**ESTRUCTURA DE RÚBRICA:**

```markdown
<!-- SOURCE: docs/rubricas.md -->
<!-- COPY THIS PATTERN: -->
## X. [Nombre Evaluación]

**Porcentaje del Curso:** X%
**Fecha de Entrega:** Semana X

### Descripción

[Descripción detallada]

### Rúbrica de Evaluación

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
```

---

## Files to Change

| File                                    | Action  | Justification                                    |
| --------------------------------------- | ------- | ------------------------------------------------ |
| `docs/cronograma.md`                    | UPDATE  | Corregir días (Martes), fechas Semana Santa      |
| `docs/rubricas.md`                      | UPDATE  | Alinear a Python/FastAPI                         |
| `clases-html/index.html`                | UPDATE  | Verificar coherencia con cronograma corregido    |
| `memory-bank/activeContext.md`          | CREATE  | Documentar estado actual de la revisión          |
| `memory-bank/tasks/revision-sistematica.md` | CREATE | Tarea principal de revisión                      |
| `proyecto/README.md`                    | UPDATE  | Agregar enlace a repositorio correcto            |
| `.claude/PRPs/plans/cronograma-fases.plan.md` | CREATE | Sub-plan para corrección de cronograma            |
| `docs/compromisos-docentes-2026-1.md`   | CREATE  | Extraer fechas de entrega de notas del PDF        |

---

## NOT Building (Scope Limits)

Exclusiones explícitas para evitar scope creep:

- **NO crear nuevas clases HTML** - solo verificar coherencia de las existentes
- **NO reescribir notebooks** - ya están completos y funcionales
- **NO cambiar la tecnología base** - mantener Python + FastAPI
- **NO modificar el pensum oficial** - documento PDF de la universidad
- **NO crear contenido para Unidades 4 y 5** - fueron eliminadas del rediseño

---

## Step-by-Step Tasks

Execute in order. Each task is atomic and independently verifiable.

### Task 1: ANALIZAR PDF Compromisos Docentes

- **ACTION**: Extraer fechas críticas del PDF "FTGCU010 Compromisos Docentes 2026-1.pdf"
- **IMPLEMENT**: Leer el PDF y crear un markdown con las fechas de:
  - Inicio del semestre
  - Fin del semestre
  - Fechas de corte para notas (50%, 80%, 100%)
  - Días festivos que afectan el calendario
- **OUTPUT**: `docs/compromisos-docentes-2026-1.md`
- **VALIDATE**: El archivo contiene todas las fechas críticas extraídas del PDF

### Task 2: CALCULAR Cronograma Correcto (MARTES)

- **ACTION**: Crear cronograma CORREGIDO para días MARTES
- **INPUT**:
  - Inicio semestre: 3 de febrero 2026 (primer martes)
  - Semana Santa: 29 marzo - 5 abril 2026
  - Días festivos: 1 ene, 9 ene, 21 mar, 13-14 abr, 1 may, 22 may, 12 jun, 19 jun
  - Fin semestre: ~junio 2026
- **IMPLEMENT**:
  ```
  Clase 1: 03 feb (martes)
  Clase 2: 10 feb (martes) ← TERCERA CLASE SEGÚN USUARIO
  Clase 3: 17 feb (martes)
  ...
  Ajustar por Semana Santa (sin clases 31 mar, 7 abr)
  ...
  Última clase: junio 2026
  ```
- **OUTPUT**: `docs/cronograma-corregido-2026-1-tuesday.md`
- **GOTCHA**: El usuario dice "martes 10 de febrero es la tercera clase" - esto implica:
  - Clase 1: 27 enero (martes ANTES de 3 feb)
  - Clase 2: 3 febrero (martes)
  - Clase 3: 10 febrero (martes) ✓
  - **VERIFICAR**: ¿Empezó el curso el 27 de enero?
- **VALIDATE**: El cronograma tiene 16-17 semanas, respusa días festivos

### Task 3: VERIFICAR Coherencia de Clases HTML

- **ACTION**: Revisar TODAS las clases HTML para coherencia cronológica
- **IMPLEMENT**:
  1. Leer cada clase HTML en orden
  2. Verificar que el contenido sigue una secuencia lógica
  3. Verificar que los enlaces a notebooks funcionen
  4. Verificar que los enlaces a recursos externos funcionen
  5. Identificar clases "Proximamente" que deberían estar completas
- **CHECKLIST**:
  - [ ] unidad-00/clase-00-introduccion.html → Introducción a Python
  - [ ] unidad-00/clase-01-variables-tipos.html → Variables y tipos
  - [ ] unidad-00/clase-02-estructuras-control.html → if/for/while
  - [ ] unidad-00/clase-03-estructuras-datos.html → listas/diccionarios
  - [ ] unidad-01/clase-01-clases-objetos.html → Clases y objetos
  - [ ] unidad-01/clase-02-encapsulamiento.html → Encapsulamiento
  - [ ] unidad-01/clase-03-herencia-polimorfismo.html → Herencia
  - [ ] unidad-01/clase-04-clases-abstractas.html → Clases abstractas
  - [ ] unidad-02/clase-01-tdd-intro.html → TDD intro
  - [ ] unidad-02/clase-02-pytest-avanzado.html → pytest avanzado
  - [ ] unidad-02/clase-03-bdd-intro.html → BDD intro
  - [ ] unidad-02/clase-04-ddd-intro.html → DDD intro
  - [ ] unidad-03/clase-01-fastapi-intro.html → FastAPI intro
  - [ ] unidad-03/clase-02-pydantic-validacion.html → Pydantic
  - [ ] unidad-03/clase-03-dependencias.html → Dependencias
  - [ ] unidad-03/clase-04-testing-fastapi.html → Testing FastAPI
  - [ ] unidad-03/clase-05-persistencia-datos.html → Persistencia
- **OUTPUT**: `docs/reporte-coherencia-clases.md` con:
  - Lista de clases verificadas
  - Inconsistencias encontradas
  - Clases faltantes o con errores
- **VALIDATE**: El reporte está completo con todas las clases revisadas

### Task 4: CORREGIR cronograma.md

- **ACTION**: Actualizar `docs/cronograma.md` con:
  1. Días correctos (MARTES, no Lunes/Miércoles)
  2. Fechas de Semana Santa correctas (29 mar-5 abr, no 24-27 mar)
  3. Contenido Python/FastAPI (no C#/ASP.NET)
- **MIRROR**: Mantener estructura del archivo pero corregir contenido
- **CHANGES**:
  ```markdown
  ## 1. Información General
  | **Días de Clase** | MARTES (corregido) |
  | **Tecnologías** | Python 3.12+, FastAPI, pytest |

  ## 2. Resumen Estadístico
  - Actualizar número de clases según calendario martes

  ## 3. Calendario por Unidad
  - Recalcular todas las fechas para martes
  - Respetar Semana Santa 29 mar-5 abr

  ## 5. Fechas Críticas
  - Alinear con PDF de compromisos docentes
  ```
- **GOTCHA**: Preservar toda la estructura good del archivo, solo cambiar datos incorrectos
- **VALIDATE**: `grep -i "C#\|ASP\.NET\|Lunes.*Miércoles" docs/cronograma.md` no retorna resultados

### Task 5: ACTUALIZAR rubricas.md

- **ACTION**: Alinear `docs/rubricas.md` a Python/FastAPI
- **CHANGES**:
  1. Eliminar referencias a C#, ASP.NET, ADO.NET
  2. Mantener estructura de rúbricas (4 niveles)
  3. Actualizar porcentajes según proyecto TaskFlow
  4. Verificar que todas las evaluaciones tengan:
     - Descripción clara
     - Rúbrica con 4 niveles
     - Pesos porcentuales
     - Fecha de entrega
- **MIRROR**: Mantener formato de rúbricas existente
- **GOTCHA**: El proyecto TaskFlow es 35% de la nota final - verificar coherencia
- **VALIDATE**: `grep -i "C#\|ASP\|ADO\|\.NET" docs/rubricas.md` no retorna resultados positivos

### Task 6: VERIFICAR index.html

- **ACTION**: Revisar `clases-html/index.html` para coherencia
- **CHECK**:
  - [ ] Enlaces a clases funcionan
  - [ ] Descripciones de tecnología correctas (Python/FastAPI)
  - [ ] Porcentajes de evaluación coherentes
  - [ ] Links a recursos externos funcionan
  - [ ] Clases "Proximamente" identificadas
- **FIX**: Si hay enlaces rotos o descripciones incorrectas
- **VALIDATE**: Abrir index.html en navegador y verificar todos los links

### Task 7: CREAR Estructura del Proyecto TaskFlow

- **ACTION**: Crear estructura base en `src/taskflow/`
- **IMPLEMENT**:
  ```
  src/taskflow/
  ├── __init__.py
  ├── core/
  │   ├── __init__.py
  │   ├── config.py
  │   └── exceptions.py
  ├── domain/
  │   ├── __init__.py
  │   ├── entities.py
  │   └── value_objects.py
  ├── application/
  │   ├── __init__.py
  │   └── services.py
  ├── infrastructure/
  │   ├── __init__.py
  │   ├── database.py
  │   └── repositories.py
  └── api/
      ├── __init__.py
      ├── main.py
      ├── dependencies.py
      └── routes/
  ```
- **MIRROR**: `proyecto/README.md` estructura documentada
- **VALIDATE**: `python -m py_compile src/taskflow/**/*.py` - todos los archivos compilan

### Task 8: ACTUALIZAR proyecto/README.md

- **ACTION**: Actualizar README con:
  1. Enlace correcto al repositorio (cuando exista)
  2. Instrucciones de instalación
  3. Instrucciones de ejecución
  4. Estructura del proyecto
  5. Criterios de evaluación por Sprint
- **MIRROR**: Mantener estructura good existente
- **ADD**:
  ```markdown
  ## Configuración del Entorno

  \`\`\`bash
  # Crear entorno virtual
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows

  # Instalar dependencias
  pip install -r requirements.txt
  \`\`\`

  ## Ejecución

  \`\`\`bash
  # Ejecutar tests
  pytest

  # Ejecutar API
  uvicorn src.taskflow.api.main:app --reload
  \`\`\`
  ```
- **VALIDATE**: Todos los comandos del README funcionan

### Task 9: CREAR requirements.txt

- **ACTION**: Crear `requirements.txt` con todas las dependencias
- **CONTENT**:
  ```
  fastapi==0.115.0
  uvicorn[standard]==0.32.0
  pydantic==2.10.0
  sqlalchemy==2.0.36
  pytest==8.3.3
  pytest-asyncio==0.24.0
  pytest-cov==6.0.0
  behave==1.2.7
  python-dotenv==1.0.1
  python-jose[cryptography]==3.3.0
  passlib[bcrypt]==1.7.4
  ```
- **VALIDATE**: `pip install -r requirements.txt` - todas las dependencias instalan

### Task 10: ACTUALIZAR memory-bank

- **ACTION**: Crear/actualizar archivos en memory-bank
- **CREATE**: `memory-bank/activeContext.md` con:
  ```markdown
  # Active Context - POO II Revisión

  ## Fecha de Última Actualización
  2026-02-08

  ## Estado Actual de la Revisión
  - [X] Estructura del curso analizada
  - [X] Inconsistencias identificadas
  - [ ] Cronograma corregido
  - [ ] Clases HTML verificadas
  - [ ] Rubricas actualizadas
  - [ ] Proyecto TaskFlow estructurado

  ## Decisiones Tomadas
  1. Mantener stack Python + FastAPI
  2. Días de clase: MARTES
  3. Semana Santa: 29 marzo - 5 abril 2026

  ## Próximos Pasos
  1. Corregir cronograma.md
  2. Verificar coherencia de clases HTML
  3. Actualizar rubricas.md
  ```
- **VALIDATE**: El archivo existe y tiene el formato correcto

### Task 11: CREAR Checklist de Validación

- **ACTION**: Crear `docs/checklist-revision.md`
- **CONTENT**:
  ```markdown
  # Checklist de Revisión - Curso POO II

  ## Cronograma
  - [ ] Días correctos (Martes)
  - [ ] Semana Santa correcta (29 mar-5 abr)
  - [ ] Tecnologías correctas (Python/FastAPI)
  - [ ] Fechas de evaluación alineadas con PDF

  ## Clases HTML
  - [ ] Todas las clases accesibles desde index.html
  - [ ] Contenido coherente cronológicamente
  - [ ] Enlaces a notebooks funcionan
  - [ ] No hay clases "Proximamente" que deban estar completas

  ## Rubricas
  - [ ] Sin referencias a C#/ASP.NET
  - [ ] Porcentajes coherentes (suman 100%)
  - [ ] Todas las evaluaciones tienen rúbrica
  - [ ] Fechas de entrega alineadas con cronograma

  ## Proyecto TaskFlow
  - [ ] Estructura de directorios creada
  - [ ] requirements.txt completo
  - [ ] README con instrucciones
  - [ ] Criterios de evaluación claros
  ```
- **VALIDATE**: El archivo existe con formato markdown válido

### Task 12: GENERAR Reporte Final

- **ACTION**: Crear `docs/reporte-revision-2026-1.md`
- **CONTENT**:
  ```markdown
  # Reporte de Revisión - Curso POO II 2026-I

  ## Resumen Ejecutivo
  - Fecha de revisión: 2026-02-08
  - Revisor: Claude AI Agent
  - Estado: COMPLETADO

  ## Cambios Realizados
  1. Cronograma corregido para días MARTES
  2. Semana Santa actualizada (29 mar-5 abr)
  3. Contenido actualizado a Python/FastAPI
  4. Clases HTML verificadas
  5. Rubricas alineadas

  ## Métricas
  - Archivos modificados: X
  - Archivos creados: Y
  - Inconsistencias corregidas: Z

  ## Recomendaciones
  1. Configurar repositorio GitHub
  2. Implementar código base de TaskFlow
  3. Realizar validación con estudiantes
  ```
- **VALIDATE**: El reporte está completo y formateado correctamente

---

## Testing Strategy

### Validaciones Manuales

| Check | Método | Esperado |
|-------|--------|----------|
| Días correctos | Leer cronograma | Todas las clases son en MARTES |
| Semana Santa | Verificar fechas | 29 marzo - 5 abril (no 24-27 marzo) |
| Tecnologías | grep C#/ASP.NET | No hay resultados |
| Links funcionan | Abrir index.html | Todos los links funcionan |
| Proyecto | ls src/taskflow/ | Estructura creada |

### Edge Cases Checklist

- [ ] Clases caen en días festivos (reprogramar)
- [ ] Semana Santa no interrumpe evaluaciones
- [ ] Fechas de entrega respetan compromisos docentes
- [ ] Porcentajes de evaluación suman 100%
- [ ] Todos los notebooks tienen enlace correspondiente

---

## Validation Commands

### Level 1: CONSISTENCIA DE CONTENIDO

```bash
# Verificar que no hay referencias a tecnologías antiguas
grep -r "C#\|ASP\.NET\|ADO\.NET" docs/ clases-html/ || echo "✓ No referencias a .NET"

# Verificar que cronograma usa martes
grep "Martes\|Tuesday" docs/cronograma.md || echo "✗ Días incorrectos"

# Verificar que Semana Santa es correcta
grep "29.*marzo\|5.*abril" docs/cronograma.md || echo "✗ Semana Santa incorrecta"
```

**EXPECT**: ✓ para todas las verificaciones

### Level 2: ENLACES FUNCIONALES

```bash
# Verificar que todos los HTML existen
for file in $(grep -o 'href="[^"]*\.html"' clases-html/index.html | cut -d'"' -f2); do
  test -f "clases-html/$file" && echo "✓ $file" || echo "✗ $file missing"
done
```

**EXPECT**: Todos los HTML existen

### Level 3: ESTRUCTURA DEL PROYECTO

```bash
# Verificar estructura de TaskFlow
ls -la src/taskflow/{core,domain,application,infrastructure,api} || echo "✗ Estructura incompleta"
```

**EXPECT**: Todos los directorios existen

### Level 4: DEPENDENCIAS

```bash
# Verificar que requirements.txt es válido
pip install --dry-run -r requirements.txt || echo "✗ Dependencias inválidas"
```

**EXPECT**: Todas las dependencias son válidas

### Level 5: COHERENCIA DE RÚBRICAS

```bash
# Sumar porcentajes
# (manual) Verificar que todos los componentes suman 100%
```

**EXPECT**: Suma = 100%

---

## Acceptance Criteria

- [ ] Cronograma corregido con días MARTES
- [ ] Semana Santa con fechas correctas (29 mar-5 abr)
- [ ] Sin referencias a C#/ASP.NET en docs/
- [ ] Todas las clases HTML verificadas y coherentes
- [ ] Rubricas alineadas con Python/FastAPI
- [ ] Proyecto TaskFlow con estructura base
- [ ] requirements.txt creado y funcional
- [ ] memory-bank actualizado
- [ ] Reporte final generado

---

## Completion Checklist

- [ ] Task 1: PDF analizado y extraído
- [ ] Task 2: Cronograma MARTES creado
- [ ] Task 3: Clases HTML verificadas
- [ ] Task 4: cronograma.md corregido
- [ ] Task 5: rubricas.md actualizado
- [ ] Task 6: index.html verificado
- [ ] Task 7: Estructura TaskFlow creada
- [ ] Task 8: README.md actualizado
- [ ] Task 9: requirements.txt creado
- [ ] Task 10: memory-bank actualizado
- [ ] Task 11: Checklist creado
- [ ] Task 12: Reporte final generado
- [ ] Level 1-5 validaciones pasan
- [ ] Todos los criterios de aceptación cumplidos

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Fecha de inicio incorrecta | MED | HIGH | Verificar con usuario: ¿empezó 27 ene o 3 feb? |
| Días festivos adicionales | LOW | MED | Revisar calendario UNAULA 2026-I |
| Cambio en tecnologías | LOW | CRITICAL | Mantener Python/FastAPI - confirmado con usuario |
| Links a notebooks rotos | MED | MED | Verificar cada enlace manualmente |
| Semana Santa afecta evaluaciones | HIGH | HIGH | Reprogramar evaluaciones si es necesario |

---

## Notes

### Fechas Críticas Confirmadas

**Días Festivos 2026 que afectan MARTES:**
- 6 enero (Lunes) - no afecta
- 9 enero (Jueves) - no afecta
- 24 marzo (Martes) - **CLASE CANCELADA**
- 31 marzo (Martes) - **CLASE CANCELADA** (Semana Santa)
- 7 abril (Martes) - **CLASE CANCELADA** (Semana Santa)
- 1 mayo (Viernes) - no afecta
- ...resto no afectan martes

**Conflicto a resolver:**
- Usuario dice: "martes 10 de febrero es la tercera clase"
- Esto implica:
  - Clase 1: 27 enero (martes)
  - Clase 2: 3 febrero (martes)
  - Clase 3: 10 febrero (martes) ✓

**VERIFICAR CON USUARIO:** ¿El curso comenzó el 27 de enero de 2026?

### Stack Tecnológico Confirmado

- **Backend:** Python 3.12+, FastAPI
- **Testing:** pytest, behave (BDD)
- **Base de datos:** SQLite (desarrollo), PostgreSQL (producción)
- **Calidad:** Black, Ruff, mypy

### Proyecto Integrador

**TaskFlow** - Sistema de gestión de tareas:
- 5 Sprints con entregas progresivas
- 35% de la nota final
- Debe incluir:
  - API REST completa
  - Tests unitarios y de integración
  - Cobertura >80%
  - Documentación completa

---

## Confidence Score

**8/10** para implementación en un solo paso

**Rationale:**
- (+) Estructura del proyecto bien entendida
- (+) Tareas claramente definidas
- (+) Patrones a seguir identificados
- (-) Incertidumbre sobre fecha de inicio (27 ene vs 3 feb)
- (-) Posible cambio en días de clase (confirmar MARTES)

**Recomendación:** Ejecutar Task 2 primero y verificar fechas con usuario antes de continuar.
