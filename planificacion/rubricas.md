# Rúbricas de Evaluación - IF0100 POO II

**Versión:** 1.0
**Fecha:** 2026-02-07
**Curso:** IF0100 - Lenguaje de Programación Orientado a Objetos II

---

## Índice

- [Rúbrica para Exámenes](#rúbrica-para-exámenes)
- [Rúbrica para Talleres](#rúbrica-para-talleres)
- [Rúbrica para Proyecto Final](#rúbrica-para-proyecto-final)
- [Rúbrica para Participación y Tareas](#rúbrica-para-participación-y-tareas)

---

## 1. Rúbrica para Entregas de Proyecto (Taller/Laboratorio/Software/Prototipo)

### 1.1 Rúbrica de Entregable Técnico (Unidades 1, 3 y 4)

**Propósito:** Evaluar la calidad técnica, funcionalidad y aplicación de conceptos en el código del proyecto.

**Peso Total:** 100 puntos
**Formato:** Entrega de Repositorio + Sustentación Corta

| Criterio | Excelente (25-20) | Bueno (19-15) | Satisfactorio (14-10) | Insuficiente (9-0) | Peso |
|----------|-------------------|---------------|----------------------|-------------------|------|
| **Funcionalidad e Integración** | El entregable cumple todos los requisitos; se integra perfectamente con la entrega anterior; maneja errores | Cumple requisitos principales; buena integración; funcionalidad estable | Funcionalidad parcial; integración con dificultades; algunos bugs | No funciona; no se integra; inestable | 30% |
| **Arquitectura POO/Lógica** | Uso excelente de clases, herencia o patrones; lógica de negocio clara y desacoplada | Buen uso de POO; lógica correcta; organización adecuada | Uso básico de POO; lógica algo mezclada con infra | No aplica POO; lógica confusa o inexistente | 25% |
| **Calidad de Código (PEP 8)** | Sigue PEP 8 perfectamente; nombres descriptivos; type hints completos; modular | Sigue PEP 8; buenos nombres; la mayoría con type hints; organizado | PEP 8 aceptable; nombres regulares; pocos type hints | No sigue estándares; difícil de leer; desorganizado | 20% |
| **Documentación y README** | README explica cómo ejecutar; docstrings Google style; diagramas incluidos | README claro; docstrings básicos; explicación suficiente | README mínimo; poca documentación interna | Sin documentación; imposible de entender sin el autor | 15% |
| **Sustentación Técnica** | Explica con claridad por qué tomó las decisiones de diseño; domina su código | Explica bien el funcionamiento; dominio adecuado del código | Explicación básica; dudas sobre partes del código | No sabe explicar su propio código | 10% |

**Tabla de Conversión a Nota:**

| Puntos | Nota | Calificación |
|--------|------|-------------|
| 90-100 | 5.0 | Superior |
| 80-89 | 4.5 | Alto |
| 70-79 | 4.0 | Bueno |
| 60-69 | 3.5 | Aceptable |
| 50-59 | 3.0 | Suficiente |
| 0-49 | 1.5-2.9 | Insuficiente |

### 1.2 Rúbrica Específica para Entrega de Testing (Unidad 2)

**Propósito:** Evaluar habilidad para escribir código Python limpio y funcional.

**Peso Total:** 100 puntos
**Tiempo:** 90-120 minutos

| Criterio | Excelente (25-20) | Bueno (19-15) | Satisfactorio (14-10) | Insuficiente (9-0) | Peso |
|----------|-------------------|---------------|----------------------|-------------------|------|
| **Funcionalidad** | Código funciona perfectamente; todos los requisitos cumplidos; edge cases manejados | Código funciona; requisitos principales cumplidos | Código funciona parcialmente; requisitos básicos cumplidos | Código no funciona; requisitos no cumplidos | 30% |
| **Calidad de Código (PEP 8)** | Sigue PEP 8 perfectamente; nombres descriptivos; formato impecable | Sigue PEP 8 mayormente; buenos nombres; buen formato | Algunas violaciones de PEP 8; nombres aceptables; formato regular | Muchas violaciones; nombres confusos; mal formato | 20% |
| **Type Hints** | Type hints completos y correctos; tipos precisos; Optional usado correctamente | Type hints en funciones principales; tipos correctos | Algunos type hints; tipos básicos | Sin type hints; tipos incorrectos | 15% |
| **Docstrings** | Docstrings completos (Google style); ejemplos de uso; parámetros documentados | Docstrings en funciones principales; buena documentación | Docstrings básicos; documentación mínima | Sin docstrings; sin documentación | 15% |
| **Manejo de Errores** | Manejo exhaustivo de excepciones; mensajes claros; validaciones completas | Manejo adecuado de excepciones; mensajes claros | Manejo básico de errores; validaciones simples | Sin manejo de errores | 10% |
| **Organización** | Código modular; funciones pequeñas y reutilizables; excelente separación de responsabilidades | Código organizado; funciones adecuadas; buena separación | Código algo desorganizado; funciones grandes; separación básica | Código desorganizado; funciones monolíticas | 10% |

**Rúbrica Específica por Tipo de Problema:**

#### Problema de POO (Unidad 1)

| Aspecto | Puntos | Criterio de Evaluación |
|---------|--------|------------------------|
| **Definición de Clase** | 0-10 | Uso correcto de @dataclass, __init__, atributos |
| **Encapsulamiento** | 0-10 | Uso de @property, convenciones _ y __ |
| **Herencia/Composición** | 0-10 | Uso apropiado de super(), composición vs herencia |
| **Métodos Mágicos** | 0-10 | Implementación de __str__, __repr__, __eq__, etc. |
| **Validaciones** | 0-10 | Método validar() con lógica completa |

#### Problema de TDD (Unidad 2)

| Aspecto | Puntos | Criterio de Evaluación |
|---------|--------|------------------------|
| **Tests Completos** | 0-15 | Cubre casos normales, edge cases, errores |
| **Organización de Tests** | 0-10 | Uso de fixtures, clases de test, nombres descriptivos |
| **Asserts Significativos** | 0-15 | Asserts que verifican comportamiento importante |
| **Mocks Apropiados** | 0-10 | Mocks donde necesario; no sobre-mocking |
| **Código Limpio** | 0-10 | Código que cumple con los tests, bien refactorizado |

#### Problema de FastAPI (Unidad 3)

| Aspecto | Puntos | Criterio de Evaluación |
|---------|--------|------------------------|
| **Endpoints Funcionales** | 0-20 | Todos los endpoints funcionan correctamente |
| **Validación Pydantic** | 0-15 | Schemas definidos, validaciones funcionando |
| **Status Codes** | 0-10 | Códigos HTTP correctos (200, 201, 404, etc.) |
| **Manejo de Errores** | 0-10 | Excepciones manejadas, respuestas de error consistentes |
| **Documentación** | 0-15 | Docstrings en endpoints, ejemplos en Swagger |

---

## 2. Rúbrica para Talleres

### 2.1 Rúbrica Taller con Sustentación (Unidades 2 y 4)

**Propósito:** Evaluar trabajo colaborativo y capacidad de sustentar decisiones técnicas.

**Peso Total:** 100 puntos
**Formato:** Trabajo en parejas + sustentación oral (10-15 min)

| Criterio | Excelente (25-20) | Bueno (19-15) | Satisfactorio (14-10) | Insuficiente (9-0) | Peso |
|----------|-------------------|---------------|----------------------|-------------------|------|
| **Código Funcional** | Código funciona perfectamente; todos los requisitos implementados; edge cases manejados | Código funciona; requisitos principales implementados | Código funciona parcialmente; requisitos básicos | Código no funciona | 25% |
| **Calidad de Código** | PEP 8 perfecto; type hints; docstrings; código modular | PEP 8 seguido; type hints principales; buenos docstrings | PEP 8 aceptable; algunos type hints; docstrings básicos | No sigue PEP 8; sin type hints; sin docstrings | 20% |
| **Tests Completos** | Coverage > 80%; tests unitarios y de integración; edge cases | Coverage 60-80%; tests adecuados; casos principales | Coverage 40-60%; tests básicos; casos normales | Coverage < 40%; pocos tests | 20% |
| **Colaboración** | Excelente trabajo en pareja; ambos contribuyen igual; código integrado | Buen trabajo en pareja; contribuciones equilibradas | Trabajo aceptable; contribuciones desiguales | Poca colaboración; uno hace todo | 10% |
| **Sustentación Oral** | Explicación clara y profesional; dominio del tema; responden preguntas bien | Buena explicación; buen dominio; responden mayoría de preguntas | Explicación básica; dominio aceptable; dificultades con preguntas | Explicación confusa; poco dominio; no responden preguntas | 15% |
| **Decisiones Técnicas** | Decisiones bien justificadas; consideran alternativas; argumentos sólidos | Decisiones justificadas; alternativas consideradas | Decisiones básicas; justificaciones simples | Decisiones no justificadas | 10% |

### 2.2 Guía de Sustentación Oral

**Duración:** 10-15 minutos por pareja
**Formato:** 5-7 min de presentación + 5-8 min de preguntas

**Estructura Recomendada:**

1. **Introducción (1-2 min)**
   - Nombres de los integrantes
   - Breve descripción del taller
   - Arquitectura general

2. **Demo del Funcionamiento (2-3 min)**
   - Mostrar el sistema funcionando
   - Demostrar características principales
   - Mostrar tests pasando

3. **Explicación Técnica (2-3 min)**
   - Arquitectura del código
   - Patrones aplicados
   - Decisiones técnicas importantes

4. **Código Destacado (1-2 min)**
   - Mostrar fragmento de código interesante
   - Explicar por qué lo hicieron así

5. **Desafíos y Aprendizajes (1 min)**
   - Qué les costó más
   - Qué aprendieron
   - Qué mejorarían

**Preguntas Comunes del Docente:**

- ¿Por qué eligieron este patrón de diseño?
- ¿Cómo manejan [edge case específico]?
- ¿Cómo verificarían que este código funciona?
- ¿Qué pasaría si [condición X] ocurre?
- ¿Cómo mejorarían este código?
- ¿Qué test agregarían?

### 2.3 Rúbrica Específica Taller Unidad 2 (TDD/DDD)

| Aspecto | Excelente (25-20) | Bueno (19-15) | Satisfactorio (14-10) | Insuficiente (9-0) | Peso |
|---------|-------------------|---------------|----------------------|-------------------|------|
| **Ciclo Red-Green-Refactor** | Aplican R-G-R sistemáticamente; tests primero; refactor claro | Aplican R-G-R; la mayoría de tests primero; refactor adecuado | Aplican R-G-R parcialmente; tests después de código; refactor básico | No aplican R-G-R; código sin tests | 30% |
| **Separación Dominio-Infraestructura** | Limpia separación; dominio puro; infraestructura aislada | Buena separación; dominio limpio; infraestructura adecuada | Separación básica; algo de acoplamiento | Sin separación; todo mezclado | 25% |
| **Servicios con Tests** | Servicios completos; tests exhaustivos; mocks apropiados | Servicios adecuados; tests buenos; mocks correctos | Servicios básicos; tests mínimos; pocos mocks | Servicios incompletos; sin tests | 25% |
| **Value Objects** | VOs inmutables; igualdad por valor; lógica de dominio | VOs correctamente implementados; buena lógica | VOs básicos; lógica simple | Sin VOs o incorrectos | 10% |
| **Repositorios** | Interfaces claras; implementaciones probadas; inyección de dependencias | Interfaces buenas; implementaciones correctas; DI básica | Interfaces básicas; implementaciones simples; sin DI | Sin interfaces o incorrectas | 10% |

### 2.4 Rúbrica Específica Software Unidad 4 (SQLAlchemy + Alembic)

| Aspecto | Excelente (25-20) | Bueno (19-15) | Satisfactorio (14-10) | Insuficiente (9-0) | Peso |
|---------|-------------------|---------------|----------------------|-------------------|------|
| **Modelos SQLAlchemy** | Modelos declarativos con Mapped[T]; relaciones 1-N correctas; índices y constraints | Modelos bien definidos; relaciones básicas correctas | Modelos funcionales; faltan relaciones o constraints | Modelos incorrectos o incompletos | 30% |
| **Migraciones Alembic** | Migraciones autogeneradas y versionadas; env.py configurado; upgrade/downgrade funcionan | Migraciones generadas correctamente; aplicadas sin errores | Migraciones básicas; algunos problemas de configuración | Sin migraciones o no funcionan | 20% |
| **Integración FastAPI** | CRUD funcional con SQLAlchemy; manejo de sesiones correcto; transacciones | CRUD básico funcional; buen manejo de sesiones | CRUD parcial; problemas con sesiones o commits | Sin integración o no funciona | 25% |
| **Calidad de Código** | PEP 8 impecable; type hints completos; separación clara de capas | Buena calidad; type hints en funciones principales | Calidad aceptable; algunos type hints faltantes | Código desorganizado; sin type hints | 15% |
| **Documentación** | README con instrucciones de ejecución; docstrings; diagrama de entidades | README claro; docstrings básicos | README mínimo; poca documentación | Sin documentación | 10% |

---

## 3. Rúbrica para Proyecto Final

### 3.1 Rúbrica General del Proyecto TaskFlow

**Propósito:** Evaluar el sistema completo entregado al final del curso.

**Peso Total:** 100 puntos (20% de la nota final)
**Entregables:**
- Código fuente completo
- Documentación (README, API docs, diagramas)
- Sistema desplegado y funcional
- **Sustentación oral (10-15 min) — 1 persona por grupo elegida aleatoriamente el día de la sustentación**

> **Requisitos técnicos obligatorios:** JWT para autenticación, SQLAlchemy como ORM (SQLite/PostgreSQL/MySQL), arquitectura limpia con separación de capas, y aplicación sólida de conceptos POO (herencia, polimorfismo, encapsulamiento).

| Criterio | Excelente (25-20) | Bueno (19-15) | Satisfactorio (14-10) | Insuficiente (9-0) | Peso |
|----------|-------------------|---------------|----------------------|-------------------|------|
| **Funcionalidad Completa** | Todos los requisitos implementados; JWT + SQLAlchemy funcionando; sistema estable; edge cases manejados | Requisitos principales; JWT y SQLAlchemy presentes; sistema funcional; algunos edge cases | Requisitos básicos; JWT o SQLAlchemy con deficiencias; funcionalidad limitada | Requisitos no cumplidos; falta JWT o SQLAlchemy; sistema inestable | 30% |
| **Arquitectura y Diseño POO** | Arquitectura limpia; excelente uso de herencia, polimorfismo, encapsulamiento; separación de capas clara; patrones aplicados correctamente | Buena arquitectura; uso adecuado de POO; separación de capas; patrones usados | Arquitectura básica; uso limitado de POO; algo de separación; patrones limitados | Mala arquitectura; no aplica POO; código monolítico | 20% |
| **Calidad de Código** | PEP 8 perfecto; type hints; docstrings; código modular; sin duplicación | PEP 8 seguido; type hints principales; buenos docstrings | PEP 8 aceptable; algunos type hints; docstrings básicos | No sigue PEP 8; sin type hints; sin docstrings | 15% |
| **Tests y Calidad** | Coverage > 80%; tests unitarios, integración, E2E; todos pasan | Coverage 60-80%; tests unitarios y integración; pasan | Coverage 40-60%; tests básicos; mayoría pasan | Coverage < 40%; pocos tests; algunos fallan | 15% |
| **Documentación** | README completo; API documentada; diagramas; guías de uso | README bueno; API documentada; algunos diagramas | README básico; documentación mínima | Sin documentación o muy pobre | 10% |
| **Sustentación** | Presentación profesional; demo fluida; dominio total; excelentes respuestas | Buena presentación; demo adecuada; buen dominio; respuestas buenas | Presentación básica; demo simple; dominio aceptable; respuestas limitadas | Presentación pobre; demo falla; poco dominio; no responde | 10% |

### 3.2 Rúbrica por Entregable del Proyecto

#### E1 — Dominio POO (Semana 4) - 15%

| Aspecto | Puntos | Criterio |
|---------|--------|----------|
| Modelo de Usuario | 0-20 | Dataclass/clase con validaciones y encapsulamiento |
| Modelo de Proyecto | 0-20 | Dataclass/clase con validaciones; uso de herencia/composición |
| Modelo de Tarea | 0-20 | Dataclass/clase con validaciones; polimorfismo en estados/tipos |
| Relaciones POO | 0-20 | Herencia, polimorfismo o mixins aplicados correctamente |
| Funcionalidad Básica | 0-20 | CRUD simple funciona en memoria |

#### E2 — Testing TDD/BDD (Semana 6) - 15%

| Aspecto | Puntos | Criterio |
|---------|--------|----------|
| Tests de Dominio | 0-30 | Tests unitarios con pytest; cubren casos normales y edge cases |
| Ciclo R-G-R | 0-20 | Evidencia de Red-Green-Refactor en commits |
| Separación Dominio-Infra | 0-20 | Dominio puro sin dependencias de framework/DB |
| Mocks/Fixtures | 0-20 | Uso apropiado de fixtures y mocks donde aplique |
| Cobertura | 0-10 | Coverage mínimo 60% |

#### E3 — Prototipo Web (Semana 8) - 20%

| Aspecto | Puntos | Criterio |
|---------|--------|----------|
| API REST FastAPI | 0-30 | Endpoints CRUD funcionales con Pydantic |
| Templates Jinja2 | 0-20 | Templates HTML con herencia y contexto |
| HTMX / Interactividad | 0-20 | Actualizaciones parciales sin recargas completas |
| Bootstrap / Responsive | 0-15 | Diseño responsivo y componentes UI |
| Documentación | 0-10 | README con instrucciones de ejecución |
| Arquitectura POO | 0-5 | Mantiene separación entre modelos de dominio y web |

#### E4 — SQLAlchemy + Migraciones (Semana 11) - 15%

| Aspecto | Puntos | Criterio |
|---------|--------|----------|
| Modelos SQLAlchemy | 0-30 | Modelos declarativos Usuario, Proyecto, Tarea con relaciones |
| Migraciones Alembic | 0-20 | Alembic configurado; migraciones generadas y aplicadas |
| Relaciones ORM | 0-20 | One-to-Many, Foreign Keys, cascadas correctas |
| Entidad-Relación | 0-15 | Diagrama ER incluido; normalización adecuada |
| Docker/Config DB | 0-10 | SQLite/PostgreSQL/MySQL configurado y funcional |
| POO en Modelos | 0-5 | Uso de properties, métodos de instancia, herencia si aplica |

#### E5 — CRUD + JWT + Arquitectura Básica (Semana 13) - 15%

| Aspecto | Puntos | Criterio |
|---------|--------|----------|
| JWT Authentication | 0-25 | Login/registro con JWT; protección de endpoints con `Depends` |
| CRUD SQLAlchemy | 0-25 | Create, Read, Update, Delete completos de todas las entidades |
| Arquitectura en Capas | 0-20 | Separación mínima Domain/Use Cases/Infrastructure |
| Manejo de Errores | 0-15 | HTTPException, validaciones de negocio, respuestas consistentes |
| Dependency Injection | 0-10 | Inyección de sesiones de DB en FastAPI |
| POO Avanzada | 0-5 | Repository pattern, clases abstractas o polimorfismo en servicios |

#### E6 — Sustentación Final (Semana 16) - 20%

| Aspecto | Puntos | Criterio |
|---------|--------|----------|
| Integración Completa | 0-25 | Backend + DB + JWT integrados y funcionando |
| Funcionalidad Extra | 0-15 | Filtros, búsqueda, paginación, ordenamiento dinámico |
| Calidad de Código POO | 0-20 | Herencia, polimorfismo, encapsulamiento, PEP 8, type hints |
| Tests de Integración | 0-15 | Pruebas de integración con DB de prueba; tests de autenticación JWT |
| Documentación | 0-10 | README completo; API docs; diagramas de arquitectura |
| Sustentación Aleatoria | 0-15 | **1 persona por grupo sorteada**; domina el código y responde preguntas |

### 3.3 Rúbrica de Sustentación Final

**Duración:** 15 minutos por grupo
**Formato:** 8-10 min de presentación + 5-7 min de preguntas
**Modalidad:** Se sortea aleatoriamente **1 persona por grupo** para defender el proyecto el día de la sustentación. Todos los integrantes deben estar preparados.

| Criterio | Excelente (10-8) | Bueno (7-5) | Satisfactorio (4-2) | Insuficiente (1-0) | Peso |
|----------|-------------------|---------------|----------------------|-------------------|------|
| **Organización** | Estructura clara; flujo lógico; tiempo bien manejado | Buena estructura; flujo adecuado | Estructura básica; flujo algo desorganizado | Sin estructura; desorganizado | 20% |
| **Demo en Vivo** | Demo fluida; sin errores; muestra características clave | Demo buena; pocos errores; muestra mayoría | Demo básica; algunos errores; muestra lo mínimo | Demo falla; no muestra funcionalidad | 25% |
| **Dominio Técnico** | Responde todas las preguntas; explica detalles; conoce el código | Responde mayoría; explica bien; conoce código | Responde algunas; explica básico; conoce algo | No responde; no explica; no conoce | 30% |
| **Calidad Visual** | Slides profesionales; código claro; demo visible | Buenas slides; código legible; demo OK | Slides básicas; código aceptable; demo regular | Pobres slides; código confuso; demo mala | 10% |
| **Reflexión** | Excelente autoevaluación; aprendizajes claros; mejoras propuestas | Buena reflexión; aprendizajes identificados | Reflexión básica; aprendizajes genéricos | Sin reflexión; sin aprendizajes | 15% |

**Estructura de Presentación Recomendada:**

1. **Introducción (1 min)**
   - Nombre y rol en el proyecto
   - Visión general del sistema

2. **Arquitectura (2 min)**
   - Diagrama de arquitectura
   - Explicación de capas
   - Tecnologías usadas

3. **Demo en Vivo (4-5 min)**
   - Login/Registro
   - Crear proyecto
   - Crear tarea
   - Dashboard/Estadísticas

4. **Código Destacado (2-3 min)**
   - Mostrar patrón interesante
   - Explicar decisión técnica
   - Destacar aprendizaje

5. **Desafíos y Soluciones (1-2 min)**
   - Qué fue difícil
   - Cómo lo resolvieron
   - Qué aprenderían

6. **Conclusiones (1 min)**
   - Lo más proud del
   - Lo que mejorarían
   - Próximos pasos

---

## 4. Rúbrica para Participación y Tareas

### 4.1 Rúbrica de Participación en Clase

**Peso:** 15% de la nota final
**Evaluación:** Continua durante el semestre

| Criterio | Excelente (25-20) | Bueno (19-15) | Satisfactorio (14-10) | Insuficiente (9-0) | Peso |
|----------|-------------------|---------------|----------------------|-------------------|------|
| **Asistencia y Puntualidad** | 100% asistencia; siempre puntual; nunca sale temprano | 90-99% asistencia; casi siempre puntual | 80-89% asistencia; algunas tardanzas | <80% asistencia; frecuente tardanza/salida | 20% |
| **Participación Activa** | Pregunta frecuente; responde preguntas; colabora con compañeros | Participa regularmente; responde cuando se le pide; colabora bien | Participa ocasionalmente; responde a veces; colaboración limitada | Rara vez participa; no responde; no colabora | 30% |
| **Preparación** | Siempre viene preparado; leyó el material; hizo ejercicios | Mayormente preparado; leyó material; ejercicios hechos | A veces preparado; leyó algo; ejercicios parciales | Rara vez preparado; no leyó; sin ejercicios | 25% |
| **Trabajo en Equipo** | Liderazgo positivo; ayuda a compañeros; facilita colaboración | Buen trabajo en equipo; ayuda cuando puede | Trabajo de equipo aceptable; ayuda limitada | Difícil trabajar con él/ella; no ayuda | 25% |

### 4.2 Rúbrica de Quizzes Rápidos

**Frecuencia:** Al inicio de cada clase teórica
**Duración:** 5 minutos
**Peso:** Acumulativo hacia participación

| Resultado | Puntos | Descripción |
|-----------|--------|-------------|
| 5/5 correctas | 10 | Excelente preparación |
| 4/5 correctas | 8 | Muy buena preparación |
| 3/5 correctas | 6 | Buena preparación |
| 2/5 correctas | 4 | Preparación básica |
| 1/5 correctas | 2 | Preparación insuficiente |
| 0/5 correctas | 0 | Sin preparación |

**Política de Quizzes:**
- Los 3 peores quizzes se eliminan del cálculo
- Los quizzes son de diagnóstico, no punitivos
- Sirven para identificar temas de refuerzo

### 4.3 Rúbrica de Tareas para Casa

**Frecuencia:** Después de cada clase práctica
**Entrega:** Próxima clase
**Formato:** Código en repositorio Git

| Criterio | Excelente | Bueno | Satisfactorio | Insuficiente |
|----------|-----------|--------|----------------|--------------|
| **Compleción** | Todos los ejercicios completos | La mayoría completos | Algunos completos | Pocos o ninguno |
| **Funcionalidad** | Todo funciona | La mayoría funciona | Algunos funcionan | Poco funciona |
| **Calidad** | PEP 8, type hints, docstrings | PEP 8 seguido, type hints | PEP 8 aceptable | No sigue PEP 8 |
| **Entrega a Tiempo** | Antes o en la fecha | En la fecha | 1 día tarde | >1 día tarde |

**Escalas de Puntos:**

- Excelente: 10 puntos
- Bueno: 8 puntos
- Satisfactorio: 6 puntos
- Insuficiente: 0-4 puntos

**Cálculo Final:**
- Promedio de todas las tareas
- Las 2 peores tareas se eliminan
- Peso: 30% de participación

### 4.4 Rúbrica de Trabajo en Parejas (Talleres)

| Aspecto | Excelente (4) | Bueno (3) | Satisfactorio (2) | Insuficiente (1) |
|---------|---------------|-----------|-------------------|------------------|
| **Contribución Equitativa** | Ambos contribuyen igual | Contribución mayormente equitativa | Uno contribuye más | Uno hace todo |
| **Colaboración** | Excelente comunicación; decisiones conjuntas | Buena comunicación; decisiones compartidas | Comunicación limitada; decisiones individuales | Poca comunicación; decisiones unilaterales |
| **Resolución de Conflictos** | Resuelven juntos; soluciones constructivas | Resuelven mayormente; soluciones adecuadas | Algunos conflictos sin resolver | Conflictos no resueltos |
| **Calidad del Producto** | Producto integrado; coherente | Producto con buena integración | Producto algo fragmentado | Producto desintegrado |

---

## 5. Cálculo de Nota Final

### 5.1 Distribución de Ponderación (Proyecto Incremental)

| Componente | Peso | Nota Base |
|------------|------|-----------|
| Evaluación 1 (Unidad 1) | 15% | Entrega 1: Dominio POO (Taller) |
| Evaluación 2 (Unidad 2) | 15% | Entrega 2: Testing TDD/BDD (Laboratorio) |
| Evaluación 3 (Unidad 3) | 20% | Entrega 3: Prototipo Web (Prototipo) |
| Evaluación 4 (Unidad 4) | 15% | Entrega 4: SQLAlchemy Modelos + Migraciones (Software) |
| Evaluación 5 (Unidad 4/5) | 15% | Entrega 5: CRUD + JWT + Arquitectura Básica (Software) |
| Evaluación Final (Unidad 5) | 20% | Sustentación Final — 1 persona/grupo sorteada (Proyecto) |
| **TOTAL** | **100%** | - |

### 5.2 Escala de Calificación

| Rango | Nota | Calificación |
|-------|------|-------------|
| 4.6 - 5.0 | 5.0 | Superior |
| 4.1 - 4.5 | 4.5 | Alto |
| 3.6 - 4.0 | 4.0 | Bueno |
| 3.0 - 3.5 | 3.5 | Aceptable |
| 2.5 - 2.9 | 3.0 | Suficiente |
| 0.0 - 2.4 | 1.5 - 2.9 | Insuficiente |

### 5.3 Política de Recuperación

**Caso 1: Nota Insuficiente (2.5 - 2.9)**
- Opción 1: Recuperar examen/práctica deficiente
- Opción 2: Entregar proyecto mejorado
- Nota máxima de recuperación: 3.5

**Caso 2: Nota Muy Insuficiente (<2.5)**
- Recuperación obligatoria de todas las evaluaciones
- Tutoría obligatoria
- Nota máxima de recuperación: 3.0

**Caso 3: Inasistencia > 20%**
- Pierde derecho a recuperación automática
- Debe solicitar recuperación especial
- Justificación requerida

---

## 6. Retroalimentación al Estudiante

### 6.1 Formato de Feedback en Exámenes

```
ESTUDIANTE: [Nombre]
EVALUACIÓN: [Nombre]
FECHA: [Fecha]
NOTA: [X]/100 → [X.X]

RESUMEN DE DESEMPEÑO
─────────────────────

Fortalezas:
• [Fortaleza 1]
• [Fortaleza 2]
• [Fortaleza 3]

Áreas de Mejora:
• [Área 1] - [Sugerencia específica]
• [Área 2] - [Sugerencia específica]
• [Área 3] - [Sugerencia específica]

COMENTARIOS ESPECÍFICOS
───────────────────────

[Comentarios constructivos detallados]

PRÓXIMOS PASOS
──────────────

• [Acción 1]
• [Acción 2]
• [Acción 3]

DOCENTE: [Nombre]
FECHA DE REVISIÓN: [Fecha]
```

### 6.2 Criterios de Feedback Constructivo

1. **Específico:** Referirse a aspectos concretos del trabajo
2. **Acccionable:** Sugerir acciones concretas de mejora
3. **Oportuno:** Entregar feedback dentro de la semana siguiente
4. **Equilibrado:** Incluir fortalezas y áreas de mejora
5. **Formativo:** Enfocado en aprendizaje, no solo en calificación

---

## 7. Uso de Rúbricas por el Docente

### 7.1 Antes de la Evaluación

1. **Compartir la rúbrica:** Mostrarla antes del examen/taller
2. **Ejemplificar:** Mostrar ejemplos de cada nivel
3. **Aclarar dudas:** Resolver preguntas sobre criterios
4. **Referencia:** Mantener rúbrica visible durante evaluación

### 7.2 Durante la Evaluación

1. **Usar consistentemente:** Aplicar los mismos criterios a todos
2. **Tomar notas:** Anotar observaciones específicas
3. **Ser justo:** Evitar sesgos conscientes o inconscientes
4. **Mantener objetividad:** Basar en evidencia, no en impresiones

### 7.3 Después de la Evaluación

1. **Calificar con rúbrica:** Usarla como guía sistemática
2. **Justificar puntaje:** Explicar por qué cada puntaje
3. **Preparar feedback:** Usar observaciones para feedback constructivo
4. **Revisar rúbrica:** Evaluar si fue adecuada y ajustar si es necesario

---

**Fin de Documento**

**Próxima revisión:** Post-primera evaluación (Unidad 1)
