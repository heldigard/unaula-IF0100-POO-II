# Rúbricas de Evaluación - IF0100 POO II
## Semestre 2026-1 | Python/FastAPI

---

## Sistema de Evaluación Oficial

| # | Resultado de Aprendizaje | Tipo | Peso | Fecha |
|---|--------------------------|------|------|-------|
| **E1** | Conoce los conceptos fundamentales de objetos clases | Examen | 15% | 26/02/2026 |
| **E2** | Técnicas de Desarrollo de software | Taller | 15% | 12/03/2026 |
| **E3** | Desarrollo Web | Proyecto | 20% | 26/03/2026 |
| **E4** | Construye sistemas con persistencia de datos en archivos planos | Laboratorio | 15% | 23/04/2026 |
| **E5** | Desarrolla sistemas con persistencia en bases de datos | Proyecto | 15% | 07/05/2026 |
| **E6** | Conoce e implementa las arquitectura de datos desconectados | Proyecto | 20% | 26/05/2026 |

**Total: 100%**

---

## E1: Conceptos Fundamentales de Objetos y Clases
### Examen Teórico-Práctico | 15% | 26/02/2026

**Unidades:** U00 (Introducción Python) + U01 (POO)

#### Competencias Evaluadas
- Conocer y aplicar conceptos de Programación Orientada a Objetos
- Implementar clases, objetos, atributos y métodos en Python
- Aplicar encapsulamiento, herencia y polimorfismo

#### Rúbrica de Calificación (100 puntos)

| Criterio | Excelente (90-100) | Bueno (70-89) | Aceptable (60-69) | Insuficiente (0-59) |
|----------|-------------------|---------------|-------------------|---------------------|
| **Definición de Clases (25 pts)** | Clases bien estructuradas con `__init__`, type hints y docstrings | Clases correctas con `__init__`, faltan type hints o docstrings | Clases funcionales pero sin buenas prácticas | Errores en sintaxis de clases |
| **Atributos y Métodos (25 pts)** | Atributos públicos/privados correctos, métodos con `self` | Atributos y métodos correctos, faltan convenios | Métodos sin `self` o atributos mal definidos | Errores conceptuales graves |
| **Encapsulamiento (20 pts)** | Uso correcto de `_privado` y `@property` | Encapsulamiento básico funcional | Intenta encapsular sin éxito | No aplica encapsulamiento |
| **Herencia (15 pts)** | Herencia correcta con `super()` | Herencia funcional sin `super()` | Herencia con errores menores | No implementa herencia |
| **Polimorfismo (15 pts)** | Métodos sobrescritos correctamente | Polimorfismo básico | Intento de polimorfismo | No aplica polimorfismo |

#### Formato del Examen
- **Parte Teórica (30%):** Preguntas de selección múltiple y verdadero/falso
- **Parte Práctica (70%):** 2-3 ejercicios de código

---

## E2: Técnicas de Desarrollo de Software
### Taller Práctico | 15% | 12/03/2026

**Unidad:** U01 (POO Avanzada - Clases, Encapsulamiento, Herencia, Polimorfismo)

#### Competencias Evaluadas
- Diseñar jerarquías de clases con herencia
- Aplicar encapsulamiento con propiedades
- Implementar clases abstractas e interfaces
- Usar polimorfismo para comportamiento flexible

#### Rúbrica de Calificación (100 puntos)

| Criterio | Excelente (90-100) | Bueno (70-89) | Aceptable (60-69) | Insuficiente (0-59) |
|----------|-------------------|---------------|-------------------|---------------------|
| **Diseño de Clases (25 pts)** | Jerarquía bien diseñada con SRP | Diseño funcional con mejoras posibles | Diseño básico pero funcional | Diseño confuso o sin sentido |
| **Herencia (25 pts)** | Herencia correcta con super() y method overriding | Herencia funcional con errores menores | Herencia básica | No usa herencia correctamente |
| **Encapsulamiento (20 pts)** | Propiedades con @property, validación completa | Encapsulamiento parcial | Atributos públicos sin protección | Sin encapsulamiento |
| **Polimorfismo (15 pts)** | Métodos polimórficos bien implementados | Polimorfismo funcional | Polimorfismo básico | No aplica polimorfismo |
| **Clases Abstractas (15 pts)** | ABCs bien definidos con métodos abstractos | Clases abstractas funcionales | Uso básico de ABCs | No usa clases abstractas |

#### Entregable
- Repositorio Git con modelo de dominio TaskFlow
- Mínimo 5 clases con relaciones de herencia
- Uso de @property para encapsulamiento
- Al menos 1 clase abstracta (ABC)

---

## E3: Desarrollo Web
### Proyecto API REST | 20% | 26/03/2026

**Unidad:** U03 (FastAPI, Pydantic, Jinja2, HTMX)

#### Competencias Evaluadas
- Crear APIs REST con FastAPI
- Validar datos con Pydantic
- Implementar operaciones CRUD
- Documentar API con OpenAPI

#### Rúbrica de Calificación (100 puntos)

| Criterio | Excelente (90-100) | Bueno (70-89) | Aceptable (60-69) | Insuficiente (0-59) |
|----------|-------------------|---------------|-------------------|---------------------|
| **Estructura API (20 pts)** | Routers organizados, separación de responsabilidades | Estructura clara pero mejorable | Todo en main.py pero funcional | Estructura confusa |
| **Endpoints CRUD (25 pts)** | GET, POST, PUT, DELETE implementados correctamente | CRUD funcional con errores menores | CRUD parcial | Endpoints incompletos |
| **Pydantic Models (20 pts)** | Schemas separados para request/response con validación | Modelos funcionales sin validación completa | Modelos básicos | Sin uso de Pydantic |
| **Manejo de Errores (15 pts)** | HTTPException con códigos correctos (404, 422, etc.) | Manejo básico de errores | Poco manejo de errores | Sin manejo de errores |
| **Documentación (10 pts)** | Docstrings en endpoints, descripción en FastAPI() | Documentación parcial | Poca documentación | Sin documentación |
| **Tests de API (10 pts)** | Tests con TestClient para endpoints | Tests básicos | Tests insuficientes | Sin tests |

#### Entregable
- API REST funcional con FastAPI
- Mínimo 3 recursos (ej: Usuarios, Proyectos, Tareas)
- Documentación en /docs funcional
- Colección de tests

---

## E4: Persistencia en Archivos Planos
### Laboratorio Práctico | 15% | 23/04/2026

**Unidad:** U04 (JSON, CSV, pickle, pathlib)

#### Competencias Evaluadas
- Leer y escribir archivos JSON y CSV
- Serializar objetos con pickle
- Manejar rutas con pathlib
- Implementar patrón Repository básico

#### Rúbrica de Calificación (100 puntos)

| Criterio | Excelente (90-100) | Bueno (70-89) | Aceptable (60-69) | Insuficiente (0-59) |
|----------|-------------------|---------------|-------------------|---------------------|
| **Lectura JSON/CSV (25 pts)** | Lectura robusta con manejo de errores | Lectura funcional | Lectura básica | Errores en lectura |
| **Escritura JSON/CSV (25 pts)** | Escritura con formato y validación | Escritura funcional | Escritura básica | Errores en escritura |
| **Uso de pathlib (20 pts)** | Path usado consistentemente, rutas cross-platform | Uso parcial de pathlib | Mezcla de pathlib y strings | Sin pathlib |
| **Manejo de Excepciones (15 pts)** | try/except para FileNotFoundError, JSONDecodeError | Manejo básico de excepciones | Poco manejo | Sin manejo |
| **Estructura de Código (15 pts)** | Funciones separadas, código limpio | Código organizado | Código funcional pero desordenado | Código desestructurado |

#### Entregable
- Módulo de persistencia con JSON
- Módulo de persistencia con CSV
- Ejemplos de uso funcionando
- Manejo de errores documentado

---

## E5: Persistencia en Bases de Datos
### Proyecto con SQLAlchemy | 15% | 07/05/2026

**Unidad:** U04 (SQLAlchemy ORM, Alembic, SQLite/PostgreSQL)

#### Competencias Evaluadas
- Definir modelos con SQLAlchemy ORM
- Crear relaciones (One-to-Many, Many-to-Many)
- Implementar CRUD con sesiones
- Usar migrations con Alembic

#### Rúbrica de Calificación (100 puntos)

| Criterio | Excelente (90-100) | Bueno (70-89) | Aceptable (60-69) | Insuficiente (0-59) |
|----------|-------------------|---------------|-------------------|---------------------|
| **Modelos SQLAlchemy (25 pts)** | Modelos con relaciones, constraints y tipos correctos | Modelos funcionales con relaciones básicas | Modelos sin relaciones | Modelos incorrectos |
| **Relaciones (25 pts)** | One-to-Many y Many-to-Many implementadas | Una relación implementada correctamente | Relaciones con errores | Sin relaciones |
| **CRUD con Sesiones (20 pts)** | Operaciones con commit/rollback correctos | CRUD funcional | CRUD con errores | CRUD incompleto |
| **Alembic Migrations (15 pts)** | Migrations creadas y aplicadas | Migration inicial creada | Intento de migrations | Sin migrations |
| **Integración API (15 pts)** | API conectada a BD, endpoints funcionales | Integración parcial | Integración con errores | Sin integración |

#### Entregable
- Modelos SQLAlchemy completos
- Base de datos SQLite con datos de prueba
- Migrations de Alembic
- API conectada a la base de datos

---

## E6: Arquitectura de Datos Desconectados
### Proyecto Integrador Final | 20% | 26/05/2026

**Unidad:** U05 (Repository Pattern, Clean Architecture, Caché)

#### Competencias Evaluadas
- Implementar patrón Repository
- Aplicar arquitectura limpia
- Usar DTOs con Pydantic
- Implementar caché básico

#### Rúbrica de Calificación (100 puntos)

| Criterio | Excelente (90-100) | Bueno (70-89) | Aceptable (60-69) | Insuficiente (0-59) |
|----------|-------------------|---------------|-------------------|---------------------|
| **Patrón Repository (25 pts)** | Repository completo con interfaz y implementación | Repository funcional | Repository básico | Sin Repository |
| **Arquitectura en Capas (25 pts)** | Separación clara: models/repositories/services/api | Alguna separación de capas | Capas mezcladas | Sin arquitectura |
| **DTOs Pydantic (20 pts)** | DTOs separados para cada operación | DTOs básicos | Un solo modelo para todo | Sin DTOs |
| **Caché (15 pts)** | Caché implementado con cachetools o similar | Intento de caché | Caché conceptual | Sin caché |
| **Documentación y Tests (15 pts)** | README completo, tests de integración | Documentación básica, algunos tests | Poca documentación | Sin documentación |

#### Entregable
- Proyecto TaskFlow completo
- Arquitectura limpia implementada
- Patrón Repository funcional
- Caché implementado
- README con instrucciones

---

## Seguimientos Académicos

### Primer Seguimiento (50%) - 27/03/2026
| Evaluación | % | Fecha |
|------------|---|-------|
| E1 - Conceptos fundamentales | 15% | 26/02/2026 |
| E2 - Técnicas de desarrollo | 15% | 12/03/2026 |
| E3 - Desarrollo Web | 20% | 26/03/2026 |

### Segundo Seguimiento (80%) - 15/05/2026
| Evaluación | % | Fecha |
|------------|---|-------|
| E4 - Persistencia archivos | 15% | 23/04/2026 |
| E5 - Persistencia BD | 15% | 07/05/2026 |

### Tercer Seguimiento (100%) - 28/05/2026
| Evaluación | % | Fecha |
|------------|---|-------|
| E6 - Datos desconectados | 20% | 26/05/2026 |

---

## Criterios Generales de Calificación

### Escala de Calificación
| Rango | Calificación | Descripción |
|-------|-------------|-------------|
| 90-100 | Excelente | Supera expectativas, trabajo de calidad profesional |
| 80-89 | Muy Bueno | Cumple todos los requisitos con calidad |
| 70-79 | Bueno | Cumple requisitos básicos |
| 60-69 | Aceptable | Cumple mínimamente, necesita mejoras |
| 0-59 | Insuficiente | No cumple requisitos mínimos |

### Políticas de Entrega
- **Entrega puntual:** 100% de la calificación
- **Entrega tardía (24h):** -10% de la calificación
- **Entrega tardía (48h):** -20% de la calificación
- **Sin entrega:** 0%

### Detección de Plagio
- Todo código será revisado con herramientas de detección de similitud
- Plagio resultará en calificación de 0 y reporte a coordinación
- Se permite y fomenta la colaboración, pero el código debe ser original

---

*Documento actualizado: 14 de febrero de 2026*
*Universidad Autónoma Latinoamericana - UNAULA*
