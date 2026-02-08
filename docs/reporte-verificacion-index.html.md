# Reporte de Verificación - clases-html/index.html

**Fecha:** 2026-02-08
**Versión:** 1.0
**Archivo Verificado:** `clases-html/index.html`

---

## Resumen Ejecutivo

El archivo `index.html` presenta múltiples inconsistencias con el cronograma y las rúbricas del curso. Se detectaron problemas en enlaces a clases, porcentajes de evaluación, definiciones CSS y contenido pendiente.

**Estado General:** ⚠️ REQUIERE CORRECCIONES

---

## 1. Verificación de Enlaces a Clases

### ✅ Unidad 0: Fundamentos de Python (4 clases)
Todos los enlaces funcionan correctamente:

| Enlace en index.html | Archivo Existente | Estado |
|---------------------|-------------------|--------|
| unidad-00/clase-00-introduccion.html | ✅ EXISTE | Correcto |
| unidad-00/clase-01-variables-tipos.html | ✅ EXISTE | Correcto |
| unidad-00/clase-02-estructuras-control.html | ✅ EXISTE | Correcto |
| unidad-00/clase-03-estructuras-datos.html | ✅ EXISTE | Correcto |

### ❌ Unidad 1: Programación Orientada a Objetos (4 clases)
**PROBLEMAS CRÍTICOS DETECTADOS:**

| Enlace en index.html | Archivo Existente | Estado |
|---------------------|-------------------|--------|
| unidad-01/clase-01-clases-objetos.html | ✅ EXISTE | Correcto |
| unidad-01/clase-02-encapsulamiento.html | ✅ EXISTE | Correcto |
| (Proximamente) clase-03-herencia-polimorfismo.html | ✅ EXISTE NO LISTADO | **INCORRECTO** |
| (Proximamente) clase-04-sobrecarga-sobreescritura.html | ❌ NO EXISTE | **ROTO** |

**Archivos EXISTENTES no listados:**
- `unidad-01/clase-03-herencia-polimorfismo.html` - ✅ Existe pero marcado como "Proximamente"
- `unidad-01/clase-04-clases-abstractas.html` - ✅ Existe pero no listado

**Corrección necesaria:**
1. Activar enlace a clase-03-herencia-polimorfismo.html (eliminar alert de "Proximamente")
2. Actualizar enlace de clase-04 para apuntar a clase-04-clases-abstractas.html (NO "sobrecarga-sobreescritura")

### ✅ Unidad 2: Técnicas de Desarrollo (4 clases)
Todos los enlaces funcionan correctamente:

| Enlace en index.html | Archivo Existente | Estado |
|---------------------|-------------------|--------|
| unidad-02/clase-01-tdd-intro.html | ✅ EXISTE | Correcto |
| unidad-02/clase-02-pytest-avanzado.html | ✅ EXISTE | Correcto |
| unidad-02/clase-03-bdd-intro.html | ✅ EXISTE | Correcto |
| unidad-02/clase-04-ddd-intro.html | ✅ EXISTE | Correcto |

### ⚠️ Unidad 3: Backend con FastAPI (3 clases listadas, 5 existentes)
**FALTAN CLASES EN INDEX.HTML:**

| Enlace en index.html | Archivo Existente | Estado |
|---------------------|-------------------|--------|
| unidad-03/clase-01-fastapi-intro.html | ✅ EXISTE | Correcto |
| unidad-03/clase-02-pydantic-validacion.html | ✅ EXISTE | Correcto |
| unidad-03/clase-03-dependencias.html | ✅ EXISTE | Correcto |
| - | unidad-03/clase-04-testing-fastapi.html | ⚠️ NO LISTADO |
| - | unidad-03/clase-05-persistencia-datos.html | ⚠️ NO LISTADO |

**Corrección necesaria:**
- Agregar clase-04-testing-fastapi.html y clase-05-persistencia-datos.html al index.html

---

## 2. Inconsistencia en Porcentajes de Evaluación

### ❌ CRÍTICO: Porcentajes Diferentes

**En index.html (líneas 474-501):**
```
Proyecto Integrador (TaskFlow): 35%
Parciales Teóricos: 30%
Laboratorios: 20%
Quiz y Talleres: 15%
TOTAL: 100%
```

**En rubricas.md (líneas 355-363) y cronograma.md (líneas 136-139):**
```
Laboratorio 1: Python Basics: 5%
Laboratorio 2: Clases POO: 5%
Parcial 1: 20%
Laboratorio 3: Tests Unitarios: 5%
Laboratorio 4: FastAPI: 5%
Parcial 2: 20%
Proyecto Final: TaskFlow: 30%
Seguimiento: 30%
TOTAL: 100%
```

**Análisis:**
- El proyecto en index.html dice **35%**, pero en rubricas/cronograma dice **30%**
- Los parciales en index.html dicen **30%**, pero en rubricas/cronograma son **40%** (20% + 20%)
- Los laboratorios en index.html dicen **20%**, pero en rubricas son **20%** (5% + 5% + 5% + 5%)
- Quiz y Talleres en index.html dicen **15%**, pero en rubricas "Seguimiento" es **30%**

**Recomendación:**
Actualizar index.html para coincidir con rubricas.md:
- Proyecto: 35% → 30%
- Parciales: 30% → 40% (o dividir en Parcial 1: 20%, Parcial 2: 20%)
- Laboratorios: 20% → mantener (pero dividir en 4 de 5% cada uno)
- Quiz y Talleres: 15% → 30% (renombrar a "Seguimiento")

---

## 3. Verificación de Descripciones de Tecnología

### ✅ Descripciones Python/FastAPI Correctas

| Línea | Contenido | Estado |
|-------|-----------|--------|
| 6 | "Curso de Programación Orientada a Objetos con Python y FastAPI" | ✅ Correcto |
| 331 | "Programación Orientada a Objetos con Python y FastAPI" | ✅ Correcto |
| 414 | "utilizando Python como lenguaje principal" | ✅ Correcto |
| 422 | "Desarrollar APIs RESTful con FastAPI" | ✅ Correcto |
| 477 | "Desarrollo progresivo de un sistema de gestión de tareas con FastAPI" | ✅ Correcto |

No se encontraron referencias a tecnologías obsoletas (.NET, C#, ADOPython).

---

## 4. Verificación de Links a Recursos Externos

### ✅ Quick Links (líneas 378-403)
| Link | Destino | Estado |
|------|---------|--------|
| docs/cronograma.md | ✅ Existe | Correcto |
| docs/rubricas.md | ✅ Existe | Correcto |
| https://colab.research.google.com | Google Colab | ✅ Funciona |
| https://code.visualstudio.com | VSCode | ✅ Funciona |

### ✅ Bibliografía y Documentación (líneas 864-891)
| Link | Destino | Estado |
|------|---------|--------|
| https://docs.python.org/es/3/ | Python Docs | ✅ Funciona |
| https://fastapi.tiangolo.com/ | FastAPI Docs | ✅ Funciona |
| https://docs.pytest.org/ | pytest Docs | ✅ Funciona |
| https://behave.readthedocs.io/ | Behave Docs | ✅ Funciona |
| https://realpython.com/ | Real Python | ✅ Funciona |
| https://www.w3schools.com/python/ | W3Schools | ✅ Funciona |
| https://exercism.org/tracks/python | Exercism | ✅ Funciona |
| https://peps.python.org/ | PEPs | ✅ Funciona |

### ✅ Herramientas (líneas 779-809)
| Link | Destino | Estado |
|------|---------|--------|
| https://python.org/downloads | Python Downloads | ✅ Funciona |
| https://code.visualstudio.com | VSCode | ✅ Funciona |
| https://git-scm.com | Git | ✅ Funciona |
| https://github.com | GitHub | ✅ Funciona |

---

## 5. Clases "Proximamente" Identificadas

### Marcadas como "Proximamente" en index.html:

| Clase | Unidad | Estado Real | Acción Necesaria |
|-------|--------|-------------|------------------|
| Clase 03: Herencia y Polimorfismo | Unidad 1 | ✅ **EXISTE** | Activar enlace |
| Clase 04: Sobrecarga y Sobre-escritura | Unidad 1 | ❌ Nombre incorrecto | Cambiar a "Clases Abstractas" |

**Nota:** Las clases marcadas como "Proximamente" en realidad existen (con diferente nombre para la clase 04).

---

## 6. Problemas de CSS

### ❌ Clases CSS No Definidas

Las siguientes clases CSS se usan en el HTML pero NO están definidas en el `<style>`:

| Clase | Usada en | Línea | Efecto |
|-------|----------|-------|--------|
| `.text-purple` | Badge Unidad 2 | 621 | Color no aplicado |
| `.bg-purple` | Badge Unidad 2 | 623, 629, 641, 648 | Fondo no aplicado |
| `.text-orange` | Badge Unidad 3 | 669, 676, 687 | Color no aplicado |
| `.bg-orange` | Badge Unidad 3 | 671, 678, 689 | Fondo no aplicado |

**Corrección necesaria:** Agregar al `<style>`:
```css
.text-purple { color: #6f42c1; }
.bg-purple { background-color: #6f42c1; color: white; }
.text-orange { color: #fd7e14; }
.bg-orange { background-color: #fd7e14; color: white; }
```

---

## 7. Contenido Pendiente (Placeholders)

### Información del Docente (líneas 900-903)
```html
<p><strong>Nombre:</strong> [Nombre del Docente]</p>
<p><strong>Correo:</strong> [correo@univ.edu]</p>
<p><strong>Oficina:</strong> [Ubicación]</p>
<p><strong>Horario de atención:</strong> [Días y horas]</p>
```

### Repositorio del Proyecto (línea 716)
```html
<a href="https://github.com/your-username/taskflow" target="_blank">
```

### Footer Contacto (líneas 937-938)
```html
<p>Correo: [correo@univ.edu]</p>
<p>GitHub: <a href="https://github.com/your-username/taskflow">
```

**Recomendación:** Crear placeholders más genéricos o instrucciones para personalización.

---

## 8. Coherencia con Cronograma

### ✅ Fechas y Estructura
- El cronograma indica 30 clases efectivas
- El index.html lista 15 clases (4 + 4 + 4 + 3)
- **Inconsistencia:** El cronograma tiene más clases que las listadas en index.html

**Cronograma resumido:**
- Unidad 0: 4 clases ✅ (coincide)
- Unidad 1: 4 clases ✅ (coincide)
- Unidad 2: 4 clases ✅ (coincide)
- Unidad 3: 8 clases (clases 13-20) ❌ (index.html solo lista 3)
- Proyecto: 4 clases (clases 21-24) ❌ (no listadas en unidades)

**Recomendación:** Actualizar index.html para incluir todas las clases del cronograma.

---

## 9. Resumen de Acciones Recomendadas

### 🔴 Prioridad ALTA (Corregir inmediatamente)

1. **Actualizar porcentajes de evaluación** en index.html para coincidir con rubricas.md
2. **Activar clase-03-herencia-polimorfismo.html** (eliminar marcador "Proximamente")
3. **Corregir enlace clase-04** para apuntar a clase-04-clases-abstractas.html
4. **Definir clases CSS faltantes** (.text-purple, .bg-purple, .text-orange, .bg-orange)

### 🟡 Prioridad MEDIA (Corregir pronto)

5. **Agregar clases faltantes de Unidad 3:**
   - clase-04-testing-fastapi.html
   - clase-05-persistencia-datos.html
6. **Actualizar contador de clases** en headers de unidades (3 → 5 para Unidad 3)

### 🟢 Prioridad BAJA (Mejoras)

7. **Reemplazar placeholders** con información genérica o instrucciones
8. **Agregar nota** sobre actualización de información del docente
9. **Revisar coherencia** entre número de clases en cronograma vs. index.html

---

## 10. Tabla de Errores Detectados

| # | Tipo | Severidad | Ubicación | Descripción |
|---|------|-----------|-----------|-------------|
| 1 | Enlace roto | 🔴 Alta | Unidad 1, Clase 04 | Apunta a archivo inexistente |
| 2 | Enlace desactivado | 🟡 Media | Unidad 1, Clase 03 | Marcado como "Proximamente" pero existe |
| 3 | Clases faltantes | 🟡 Media | Unidad 3 | Faltan 2 clases en listado |
| 4 | Porcentajes inconsistentes | 🔴 Alta | Sección Evaluación | No coinciden con rubricas.md |
| 5 | CSS no definido | 🟡 Media | Badges Unidad 2 y 3 | Clases .text-purple, .bg-purple, etc. |
| 6 | Placeholder genérico | 🟢 Baja | Sección Docente | [Nombre del Docente] |
| 7 | Placeholder genérico | 🟢 Baja | Repo TaskFlow | your-username/taskflow |

---

## 11. Verificación de Tecnologías

### ✅ Tecnologías Correctas
- Python (mencionado 10+ veces)
- FastAPI (mencionado 8+ veces)
- pytest (mencionado en contexto de testing)
- Pydantic (mencionado en contexto de validación)

### ❌ Tecnologías Obsoletas
No se encontraron referencias a:
- .NET Framework
- C#
- ADOPython
- SpecFlow
- Visual Studio (solo VSCode)

---

## Conclusión

El archivo `index.html` requiere correcciones importantes para ser coherente con el cronograma y las rúbricas del curso. Los problemas más críticos son:

1. **Porcentajes de evaluación incorrectos** (35% vs 30% para proyecto)
2. **Enlaces a clases rotos o desactivados** (clase-04 incorrecta, clase-03 desactivada)
3. **Clases faltantes en el listado** (Unidad 3 incompleta)
4. **CSS no definido** (badges sin estilo)

Se recomienda realizar las correcciones de prioridad ALTA antes de publicar o distribuir el material del curso.

---

**Reporte generado:** 2026-02-08
**Verificado por:** Claude Code (Task 5)
**Archivos de referencia:** cronograma.md, rubricas.md
