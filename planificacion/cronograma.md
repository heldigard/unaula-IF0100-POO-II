# IF0100 - Lenguaje de Programación OO II
## Cronograma Detallado 2026-I (Python/FastAPI)

---

## Información General

| Campo | Valor |
|-------|-------|
| **Curso** | IF0100 - Lenguaje de Programación OO II |
| **Pensum** | 302 Pensum 2023-2 |
| **Créditos** | 3 (48 horas presenciales) |
| **Semestre** | 2026-I |
| **Horario** | **Martes 06:00-08:00** (2h) + **Jueves 06:00-07:00** (1h) |
| **Aula** | TU301 |
| **Total Sesiones** | 16 martes (2h) + 16 jueves (1h) = 32 sesiones = 48 horas |
| **Stack** | Python 3.11+ / FastAPI / SQLAlchemy |

---

## Calendario Completo de Clases 2026-I

### Formato: Martes (M) 2 horas | Jueves (J) 1 hora

**IMPORTANTE: Distribución 50% Teoría / 50% Práctica en todas las sesiones**

| Semana | Martes (2h) | Jueves (1h) | Unidad | Temas | Eval |
|--------|-------------|-------------|--------|-------|------|
| **1** | M1: 2026-02-03 | J1: 2026-02-05 | U0 | Intro Python / Variables / Tipos | - |
| **2** | M2: 2026-02-10 | J2: 2026-02-12 | U0 | Estructuras Control / Estructuras Datos | - |
| **3** | M3: 2026-02-17 | J3: 2026-02-19 | U1 | Clases y Objetos / Encapsulamiento | - |
| **4** | M4: 2026-02-24 | J4: 2026-02-26 | U1 | Herencia / Polimorfismo / Clases Abstractas | **Eval 1 (15% Taller)** |
| **5** | M5: 2026-03-03 | J5: 2026-03-05 | U2 | Intro TDD / pytest / Ciclo Red-Green-Refactor | - |
| **6** | M6: 2026-03-10 | J6: 2026-03-12 | U2 | BDD / DDD / Repository Pattern | **Eval 2 (15% Lab)** |
| **7** | M7: 2026-03-17 | J7: 2026-03-19 | U2 | Práctica TDD/BDD / Proyecto | - |
| **8** | M8: 2026-03-24 | J8: 2026-03-26 | U3 | Intro FastAPI / Rutas / Pydantic | **Eval 3 (20% Prototipo)** |
| **-** | **M: 2026-03-31 SEMANA SANTA** | **J: 2026-04-02 SEMANA SANTA** | **-** | **Receso (29 mar - 5 abr)** | **-** |
| **9** | M9: 2026-04-07 | J9: 2026-04-09 | U3 | Dependency Injection / SQLAlchemy | - |
| **10** | M10: 2026-04-14 | J10: 2026-04-16 | U3 | CRUD / JWT Authentication / Práctica | - |
| **11** | M11: 2026-04-21 | J11: 2026-04-23 | U4 | Persistencia Archivos / JSON / CSV | **Eval 4 (15% Software)** |
| **12** | M12: 2026-04-28 | J12: 2026-04-30 | U4 | SQLAlchemy ORM / Modelos / Relaciones | - |
| **13** | M13: 2026-05-05 | J13: 2026-05-07 | U4 | CRUD SQLAlchemy / Alembic | **Eval 5 (15% Software)** |
| **14** | M14: 2026-05-12 | J14: 2026-05-14 | U5 | Repository Pattern / Clean Architecture | - |
| **15** | M15: 2026-05-19 | J15: 2026-05-21 | U5 | API REST Avanzada / Caché | - |
| **16** | M16: 2026-05-26 | J16: 2026-05-28 | U5 | **Proyecto integrador / SUSTENTACIÓN FINAL** | **Final (20% Proyecto)** |

---

## Estrategia Didáctica: 50% Teoría - 50% Práctica

### Distribución por Día

#### Martes (2 horas): Teoría + Práctica Guiada
| Tiempo | Actividad | Porcentaje |
|--------|-----------|------------|
| 0:00-0:40 | **Teoría**: Exposición conceptual con ejemplos | 33% |
| 0:40-1:30 | **Práctica**: Desarrollo en vivo de código | 42% |
| 1:30-2:00 | **Ejercicio**: Estudiantes practican + Dudas | 25% |
| **Total** | | **100% (≈50/50 teoría-práctica)** |

#### Jueves (1 hora): Práctica Intensiva + Refuerzo
| Tiempo | Actividad | Porcentaje |
|--------|-----------|------------|
| 0:00-0:20 | **Repaso**: Conceptos clave del martes | 33% |
| 0:20-0:50 | **Taller**: Ejercicio práctico guiado | 50% |
| 0:50-1:00 | **Cierre**: Asignación tarea + Preguntas | 17% |
| **Total** | | **100% (≈50/50 teoría-práctica)** |

---

## Distribución de Contenido por Unidad

### Unidad 0: Fundamentos de Python (3 clases)
**M1-M2 + J1-J2: Feb 03 - Feb 12**
- Introducción a Python y configuración del entorno
- Variables, tipos de datos y operadores
- Estructuras de control (if, for, while)
- Estructuras de datos (listas, diccionarios, tuplas, sets)

**Sin evaluación - Preparación para POO**

---

### Unidad 1: Conceptos Fundamentales de POO (5 clases)
**M3-M4 + J3-J4: Feb 17 - Feb 26**
- Clases, objetos, __init__, self
- Encapsulamiento con @property
- Herencia y super()
- Polimorfismo y sobreescritura
- Clases abstractas con ABC

**Evaluación 1 (15% Taller - Entrega 1):** Jueves 26 de febrero

---

### Unidad 2: Técnicas de Desarrollo de Software (5 clases)
**M5-M7 + J5-J7: Mar 03 - Mar 19**
- Test Driven Development (TDD)
- pytest: fixtures, parametrize, markers
- Behavior Driven Development (BDD) con behave
- Domain Driven Design (DDD)
- Patrón Repository

**Evaluación 2 (15% Taller):** Jueves 12 de marzo

---

### Unidad 3: Desarrollo Web con FastAPI (5 clases)
**M8-M11 + J8-J11: Mar 24 - Abr 23 (con receso Semana Santa)**
- Introducción a FastAPI
- Pydantic y validación
- Dependency Injection
- SQLAlchemy ORM
- JWT Authentication

**Evaluación 3 (20% Proyecto):** Jueves 26 de marzo
**⚠️ NOTA:** Proyecto asignado desde semana 7 (17 marzo). Receso completo Semana Santa (31 mar - 2 abr).

---

### Unidad 4: Manejo de Persistencia (5 clases)
**M11-M13 + J11-J13: Abr 21 - May 07**
- Persistencia en archivos planos (JSON, CSV)
- SQLAlchemy: modelos y relaciones
- CRUD con SQLAlchemy
- Migraciones con Alembic
- Integración con FastAPI

**Evaluación 4 (15% Laboratorio):** Jueves 23 de abril
**Evaluación 5 (15% Proyecto):** Jueves 07 de mayo

---

### Unidad 5: Arquitectura de Datos Desconectados (5 clases)
**M14-M16 + J14-J16: May 12 - May 28**
- Patrón Repository con SQLAlchemy
- Clean Architecture
- DTOs y serialización
- APIs REST avanzadas
- Proyecto integrador

**Examen Final (20%):** Jueves 28 de mayo

---

## Seguimientos y Fechas Límite

### Primer Seguimiento (50%) - Límite: 2026-03-27
**Evaluaciones:**
- Eval 1 (15%): Taller - Entrega 1 Dominio (Feb 26)
- Eval 2 (15%): Taller - TDD/BDD (Mar 12)
- Eval 3 (20%): Proyecto - FastAPI (Mar 26)

**✅ CUMPLE:** Todas antes del 27 de marzo

### Segundo Seguimiento (80%) - Límite: 2026-05-15
**Evaluaciones:**
- Eval 4 (15%): Laboratorio - Persistencia archivos (Abr 23)
- Eval 5 (15%): Proyecto - SQLAlchemy (May 07)

**✅ CUMPLE:** Todas antes del 15 de mayo

### Tercer Seguimiento (100%) - Límite: 2026-05-28
**Evaluación:**
- Entrega Final (20%): Arquitectura y Sustentación (May 28)

---

## Estrategia de Clases

### Martes (2 horas): Teoría + Práctica
- **40 min:** Exposición teórica del tema
- **50 min:** Desarrollo práctico con código
- **30 min:** Ejercicio guiado y resolución de dudas

### Jueves (1 hora): Refuerzo + Taller
- **20 min:** Repaso de conceptos del martes
- **30 min:** Taller práctico individual/parejas
- **10 min:** Cierre y asignación de tarea

---

## Evaluaciones según Syllabus

| Eval | % | Tipo | Resultado de Aprendizaje | Fecha |
|------|---|------|--------------------------|-------|
| 1 | 15% | **Taller** | Conceptos fundamentales POO (Entrega 1) | J4: Feb 26 |
| 2 | 15% | **Laboratorio** | Técnicas de desarrollo TDD/BDD (Entrega 2) | J6: Mar 12 |
| 3 | **20%** | **Prototipo** | Desarrollo Web: FastAPI + Jinja2 (Entrega 3) | J8: Mar 26 |
| 4 | 15% | **Software** | Persistencia en archivos JSON/CSV (Entrega 4) | J11: Abr 23 |
| 5 | 15% | **Software** | SQLAlchemy ORM: CRUD completo (Entrega 5) | J13: May 07 |
| Final | **20%** | **Proyecto** | Arquitectura Limpia (Sustentación Final) | J16: May 28 |

---

## Tecnologías y Herramientas

### Software Requerido:
- **Python 3.11+** (lenguaje principal)
- **VS Code** con extensiones Python
- **Git** para control de versiones
- **PostgreSQL** (base de datos)

### Frameworks y Librerías:
- **FastAPI** (framework web)
- **SQLAlchemy 2.0** (ORM)
- **Pydantic 2.5+** (validación)
- **pytest** (testing)
- **Alembic** (migraciones)
- **Jinja2** (templates)
- **HTMX** (frontend interactivo)

---

## Notas Importantes

1. **Semana Santa:** No hay clases del 29 de marzo al 5 de abril (Semana completa)
2. **Formato mixto:** Martes (teoría extensa) + Jueves (práctica intensiva)
3. **Proyecto TaskFlow:** Sistema de gestión de tareas que se desarrolla durante todo el curso
4. **Talleres:** En parejas con sustentación para prevenir uso indebido de IA
5. **Proyecto integrador:** API REST con arquitectura limpia

---

**Última actualización:** 2026-02-14 (Actualizado a stack Python/FastAPI)
**Basado en:** Syllabus actualizado + Cálculo real de fechas 2026-I
