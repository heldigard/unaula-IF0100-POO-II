# Objetivos por Clase - IF0100 POO II

**Versión:** 1.0
**Fecha:** 2026-02-07
**Curso:** IF0100 - Lenguaje de Programación Orientado a Objetos II
**Semestre:** 2026-I

---

## Índice

- [Unidad 0: Fundamentos de Python](#unidad-0-fundamentos-de-python)
- [Unidad 1: POO Avanzada con Python](#unidad-1-poo-avanzada-con-python)
- [Unidad 2: Técnicas de Desarrollo](#unidad-2-técnicas-de-desarrollo)
- [Unidad 3: Desarrollo Backend](#unidad-3-desarrollo-backend)
- [Unidad 4: Desarrollo Frontend](#unidad-4-desarrollo-frontend)
- [Unidad 5: Proyecto Final](#unidad-5-proyecto-final)

---

## Tabla de Objetivos por Clase

| Clase | Unidad | Tema | Objetivos de Aprendizaje | Skills Prácticas | Evaluación | Conexión Proyecto |
|-------|--------|------|-------------------------|------------------|------------|-------------------|
| **0.1** | 0 | Introducción a Python y configuración | 1. Configurar entorno de desarrollo Python<br>2. Comprender tipos de datos básicos<br>3. Usar operadores aritméticos y de comparación<br>4. Aplicar input/output básico | - [ ] Instalar Python y VSCode<br>- [ ] Crear variables y tipos<br>- [ ] Usar print() e input()<br>- [ ] Crear script básico | Quiz diagnóstico (no calificado) | Base para todo el proyecto |
| **0.2** | 0 | Estructuras de control y funciones | 1. Usar condicionales if/elif/else<br>2. Implementar loops for y while<br>3. Aplicar break y continue<br>4. Definir funciones básicas | - [ ] Escribir condicionales<br>- [ ] Crear loops<br>- [ ] Definir funciones con parámetros<br>- [ ] Retornar valores | Quiz rápido (5 min) | Lógica de negocio del sistema |
| **0.3** | 0 | Listas, diccionarios y conjuntos | 1. Manipular listas y sus métodos<br>2. Usar diccionarios clave-valor<br>3. Aplicar tuplas y conjuntos<br>4. Usar comprensiones de lista | - [ ] Crear y modificar listas<br>- [ ] Usar métodos de diccionario<br>- [ ] Aplicar set para eliminar duplicados<br>- [ ] Escribir list comprehensions | Ejercicio práctico (30 min) | Estructuras de datos del sistema |
| **0.4** | 0 | Módulos, paquetes y manejo de errores | 1. Importar módulos y paquetes<br>2. Manejar excepciones con try/except<br>3. Crear excepciones personalizadas<br>4. Organizar código en módulos | - [ ] Importar desde módulos<br>- [ ] Manejar excepciones comunes<br>- [ ] Crear excepción personalizada<br>- [ ] Organizar código en paquetes | Quiz rápido + ejercicio | Manejo de errores en el sistema |
| **1.1** | 1 | Conceptos de POO en Python | 1. Definir clases usando dataclasses<br>2. Crear instancias de objetos<br>3. Implementar métodos de instancia<br>4. Comprender el concepto de self | - [ ] Crear clase Usuario con dataclass<br>- [ ] Instanciar objetos<br>- [ ] Implementar método __init__<br>- [ ] Usar atributos de instancia | Quiz (5 min) + Ejercicio (40 min) | Modelo Usuario del sistema |
| **1.2** | 1 | Encapsulamiento y propiedades | 1. Aplicar convenciones _ y __<br>2. Usar @property para getters<br>3. Implementar setters pythonicos<br>4. Aplicar encapsulamiento adecuado | - [ ] Crear propiedades con @property<br>- [ ] Implementar setters<br>- [ ] Usar _ para atributos protegidos<br>- [ ] Validar en setters | Quiz + código en clase | Propiedades de modelos |
| **1.3** | 1 | Herencia y composición | 1. Implementar herencia simple<br>2. Usar super() correctamente<br>3. Aplicar composición vs herencia<br>4. Diseñar jerarquías de clases | - [ ] Crear clase base Entity<br>- [ ] Heredar de clase base<br>- [ ] Usar super().__init__()<br>- [ ] Aplicar composición | Ejercicio práctico (45 min) | Jerarquía de modelos del sistema |
| **1.4** | 1 | Polimorfismo y métodos mágicos | 1. Sobrecargar operadores<br>2. Implementar __str__ y __repr__<br>3. Aplicar duck typing<br>4. Usar métodos mágicos comunes | - [ ] Implementar __str__ y __repr__<br>- [ ] Sobrecargar __eq__<br>- [ ] Usar __len__ y __bool__<br>- [ ] Aplicar duck typing | Quiz + reto en clase | Representación de modelos |
| **1.5** | 1 | Interfaces y ABCs | 1. Usar Abstract Base Classes<br>2. Aplicar @abstractmethod<br>3. Crear interfaces con Protocol<br>4. Implementar repositorios abstractos | - [ ] Crear ABC con métodos abstractos<br>- [ ] Implementar interface concreta<br>- [ ] Crear Protocol para type checking<br>- [ ] Definir interfaz Repository | Ejercicio (40 min) | Interfaces de repositorios |
| **1.6** | 1 | Diseño de modelos y DTOs | 1. Usar dataclasses del módulo dataclasses<br>2. Crear modelos con Pydantic<br>3. Implementar DTOs para transferencia<br>4. Validar datos con Pydantic | - [ ] Crear dataclass con validaciones<br>- [ ] Usar BaseModel de Pydantic<br>- [ ] Crear schemas request/response<br>- [ ] Validar datos de entrada | Quiz + código (VSCode) | Modelos completos del sistema |
| **1.7** | 1 | Patrones de diseño (Singleton, Factory) | 1. Implementar Singleton en Python<br>2. Crear Factory Method<br>3. Aplicar patrones al proyecto<br>4. Reconocer cuándo usar cada patrón | - [ ] Implementar Singleton con __new__<br>- [ ] Crear factory para conexiones<br>- [ ] Usar patrón Repository<br>- [ ] Documentar decisión de patrón | Ejercicio práctico (40 min) | Connection factory, Repository factory |
| **1.8** | 1 | **Evaluación 1** | 1. Demostrar comprensión de POO<br>2. Aplicar conceptos al proyecto<br>3. Escribir código limpio y documentado | - [ ] Escribir examen teórico<br>- [ ] Completar código práctico<br>- [ ] Entregar modelos del sistema | **Examen (15%)** | Entrega de modelos del sistema |
| **2.1** | 2 | Introducción a TDD | 1. Comprender el ciclo Red-Green-Refactor<br>2. Instalar y configurar pytest<br>3. Escribir primer test unitario<br>4. Ejecutar tests desde terminal | - [ ] Instalar pytest<br>- [ ] Escribir test con assert<br>- [ ] Ejecutar pytest<br>- [ ] Usar flags de pytest | Quiz (5 min) + práctica | Tests de modelos del sistema |
| **2.2** | 2 | Ciclo Red-Green-Refactor | 1. Aplicar TDD paso a paso<br>2. Escribir test antes que código<br>3. Hacer pasar el test<br>4. Refactorizar código | - [ ] Seguir ciclo R-G-R<br>- [ ] Escribir test que falla<br>- [ ] Hacer código mínimo para pasar<br>- [ ] Refactorizar manteniendo tests verdes | Taller en parejas (40 min) | Repositorio en memoria con tests |
| **2.3** | 2 | Mocks y Fixtures | 1. Crear fixtures con pytest<br>2. Usar mocks para aislar código<br>3. Aplicar parametrización de tests<br>4. Organizar tests con fixtures | - [ ] Crear @pytest.fixture<br>- [ ] Usar unittest.mock<br>- [ ] Parametrizar tests<br>- [ ] Organizar tests en clases | Ejercicio práctico (45 min) | Tests con repos de archivos |
| **2.4** | 2 | BDD con behave | 1. Escribir escenarios Gherkin<br>2. Implementar pasos en Python<br>3. Conectar escenarios con código<br>4. Ejecutar tests BDD | - [ ] Escribir feature Gherkin<br>- [ ] Implementar pasos<br>- [ ] Usar context.pickle<br>- [ ] Ejecutar behave | Quiz + práctica | Escenarios de usuario del sistema |
| **2.5** | 2 | DDD: Entidades y Value Objects | 1. Distinguir entre Entidad y Value Object<br>2. Implementar Value Objects inmutables<br>3. Aplicar lógica de dominio<br>4. Diseñar modelo rico | - [ ] Crear Value Object<br>- [ ] Implementar igualdad por valor<br>- [ ] Agregar lógica a entidades<br>- [ ] Validar invariantes | Ejercicio (40 min) | Lógica de dominio del sistema |
| **2.6** | 2 | DDD: Repositorios y Servicios | 1. Separar dominio de infraestructura<br>2. Implementar patrón Repository<br>3. Crear Services con lógica de negocio<br>4. Inyectar dependencias | - [ ] Crear interfaz Repository<br>- [ ] Implementar repo en archivos<br>- [ ] Crear Service con lógica<br>- [ ] Inyectar repo en service | Código en clase | Servicios con tests |
| **2.7** | 2 | **Evaluación 2** | 1. Demostrar habilidad con TDD<br>2. Escribir tests completos<br>3. Aplicar DDD correctamente | - [ ] Completar taller práctico<br>- [ ] Sustentar decisiones de diseño<br>- [ ] Mostrar tests pasando | **Taller (15%)** | Entrega de servicios con tests |
| **3.1** | 3 | Introducción a FastAPI | 1. Crear aplicación FastAPI básica<br>2. Definir rutas y operaciones HTTP<br>3. Usar Pydantic para validación<br>4. Ejecutar servidor de desarrollo | - [ ] Instalar FastAPI y uvicorn<br>- [ ] Crear primera ruta<br>- [ ] Definir operaciones CRUD<br>- [ ] Probar con Swagger UI | Quiz + práctica (40 min) | API básica del sistema |
| **3.2** | 3 | Pydantic y validación | 1. Crear modelos con BaseModel<br>2. Validar entrada de datos<br>3. Personalizar mensajes de error<br>4. Usar tipos complejos de Pydantic | - [ ] Crear schemas Pydantic<br>- [ ] Validar emails, passwords<br>- [ ] Personalizar validadores<br>- [ ] Usar List, Optional, etc. | Ejercicio práctico (40 min) | Schemas Pydantic del sistema |
| **3.3** | 3 | Inyección de dependencias | 1. Comprender inyección de dependencias<br>2. Usar Depends de FastAPI<br>3. Crear funciones de dependencia<br>4. Manejar ciclo de vida de dependencias | - [ ] Crear dependency function<br>- [ ] Usar Depends en rutas<br>- [ ] Inyectar sesión de BD<br>- [ ] Crear dependencias con yield | Quiz + código en clase | Config y DB del sistema |
| **3.4** | 3 | PostgreSQL y SQLAlchemy | 1. Conectar FastAPI con PostgreSQL<br>2. Definir modelos SQLAlchemy<br>3. Crear tablas con Alembic<br>4. Usar sesión de base de datos | - [ ] Configurar conexión<br>- [ ] Definir modelo ORM<br>- [ ] Crear migración<br>- [ ] Consultar con ORM | Ejercicio (45 min) | Base de datos del sistema |
| **3.5** | 3 | CRUD completo | 1. Implementar endpoints CRUD<br>2. Manejar códigos de estado HTTP<br>3. Retornar respuestas consistentes<br>4. Documentar endpoints con OpenAPI | - [ ] Crear POST, GET, PUT, DELETE<br>- [ ] Usar status codes correctos<br>- [ ] Retornar JSON consistente<br>- [ ] Documentar con docstrings | Taller en parejas (50 min) | API de tareas completa |
| **3.6** | 3 | Autenticación JWT | 1. Comprender JWT y tokens<br>2. Implementar login con JWT<br>3. Crear middleware de autenticación<br>4. Proteger rutas con dependencias | - [ ] Generar token JWT<br>- [ ] Validar token en rutas<br>- [ ] Crear Depends get_current_user<br>- [ ] Manejar refresh tokens | Ejercicio (45 min) | Auth completo del sistema |
| **3.7** | 3 | **Evaluación 3** | 1. Construir API funcional<br>2. Implementar autenticación<br>3. Documentar con OpenAPI | - [ ] Completar examen práctico<br>- [ ] Desplegar API funcional<br>- [ ] Demostrar endpoints en Swagger | **Examen (20%)** | API funcionando del sistema |
| **4.1** | 4 | Introducción a Jinja2 | 1. Comprender sistema de templates<br>2. Usar variables y filtros<br>3. Crear herencia de templates<br>4. Renderizar templates desde FastAPI | - [ ] Crear template base<br>- [ ] Usar bloques y extends<br>- [ ] Iterar con for<br>- [ ] Usar filtros comunes | Quiz + práctica (40 min) | Base de templates del sistema |
| **4.2** | 4 | HTMX: Interactividad sin JS | 1. Comprender atributos HTMX<br>2. Usar hx-get, hx-post<br>3. Actualizar DOM dinámicamente<br>4. Integrar HTMX con FastAPI | - [ ] Usar hx-trigger y hx-swap<br>- [ ] Crear endpoints HTMX<br>- [ ] Actualizar parcialmente la página<br>- [ ] Usar hx-vals para datos | Ejercicio (45 min) | Endpoints HTMX del sistema |
| **4.3** | 4 | Formularios y validación | 1. Crear formularios HTML<br>2. Validar con Pydantic<br>3. Mostrar errores de validación<br>4. Procesar form data | - [ ] Crear formulario HTML<br>- [ ] Validar en servidor<br>- [ ] Mostrar errores en UI<br>- [ ] Usar flash messages | Taller en parejas (50 min) | Formularios funcionales |
| **4.4** | 4 | Bootstrap 5 y diseño responsivo | 1. Usar sistema de grilla Bootstrap<br>2. Aplicar componentes UI<br>3. Crear diseño responsivo<br>4. Personalizar estilos | - [ ] Usar container, row, col<br>- [ ] Aplicar cards, modals<br>- [ ] Usar breakpoints<br>- [ ] Crear tema personalizado | Quiz + práctica (40 min) | UI completa del sistema |
| **4.5** | 4 | Estado y componentes dinámicos | 1. Gestionar estado en frontend<br>2. Usar hx-boost para navegación<br>3. Implementar actualización en tiempo real<br>4. Crear componentes reutilizables | - [ ] Crear componentes dinámicos<br>- [ ] Usar hx-swap-oob<br>- [ ] Implementar polling<br>- [ ] Crear partials reutilizables | Ejercicio (45 min) | Interfaz reactiva del sistema |
| **4.6** | 4 | Dashboard y reportes | 1. Crear dashboard con métricas<br>2. Usar Plotly para gráficos<br>3. Implementar filtros y búsqueda<br>4. Exportar datos | - [ ] Crear layout dashboard<br>- [ ] Integrar gráficos Plotly<br>- [ ] Implementar búsqueda<br>- [ ] Exportar a CSV/PDF | Taller en parejas (50 min) | Dashboard completo del sistema |
| **4.7** | 4 | **Evaluación 4** | 1. Integrar frontend con backend<br>2. Implementar UI completa<br>3. Demostrar flujo de usuario | - [ ] Completar taller práctico<br>- [ ] Sustentar UX/UI<br>- [ ] Demostrar sistema funcional | **Taller (15%)** | Interfaz completa del sistema |
| **5.1** | 5 | Integración y pruebas E2E | 1. Integrar todos los componentes<br>2. Escribir pruebas end-to-end<br>3. Resolver bugs de integración<br>4. Optimizar performance | - [ ] Ejecutar pruebas E2E<br>- [ ] Corregir errores<br>- [ ] Optimizar queries<br>- [ ] Documentar fixes | Código en clase + pruebas | Sistema probado |
| **5.2** | 5 | Documentación y README | 1. Escribir README completo<br>2. Documentar API con OpenAPI<br>3. Crear diagramas de arquitectura<br>4. Documentar instalación y uso | - [ ] Crear README.md<br>- [ ] Documentar endpoints<br>- [ ] Crear diagramas<br>- [ ] Escribir guías de uso | Taller documentación (40 min) | README completo |
| **5.3** | 5 | Preparación para sustentación | 1. Preparar presentación<br>2. Ensayar demo del sistema<br>3. Preparar respuestas a preguntas<br>4. Revisar código y documentación | - [ ] Crear slides de presentación<br>- [ ] Ensayar demo<br>- [ ] Preparar Q&A<br>- [ ] Revisar todo el proyecto | Trabajo en clase (50 min) | Presentación lista |
| **5.4** | 5 | **Sustentaciones finales** | 1. Presentar proyecto completo<br>2. Demostrar funcionalidad<br>3. Responder preguntas<br>4. Reflexionar sobre aprendizaje | - [ ] Presentar (10-15 min)<br>- [ ] Demostrar sistema<br>- [ ] Responder preguntas<br>- [ ] Autoevaluación | **Examen Final (20%)** | **Entrega final del sistema** |

---

## Resumen de Evaluaciones

| Evaluación | Unidad | Peso | Formato | Semana |
|------------|--------|------|---------|--------|
| Evaluación 1 | 1.8 | 15% | Examen teórico-práctico + modelos | 6 |
| Evaluación 2 | 2.7 | 15% | Taller práctico + sustentación | 9 |
| Evaluación 3 | 3.7 | 20% | Examen práctico + API funcionando | 12 |
| Evaluación 4 | 4.7 | 15% | Taller práctico + sustentación | 15 |
| Evaluación Final | 5.4 | 20% | Sustentación del proyecto completo | 17 |
| **Participación y tareas** | - | 15% | Quizzes, ejercicios, tareas | Todo el curso |
| **TOTAL** | - | **100%** | - | - |

---

## Mapa de Objetivos por Unidad

### Unidad 0: Fundamentos de Python (Semana 1-2)

**Objetivo General:** Reforzar conocimientos básicos de Python para preparar a los estudiantes en el desarrollo del proyecto.

**Objetivos Específicos:**
- Configurar entorno de desarrollo Python
- Comprender tipos de datos y operadores
- Dominar estructuras de control
- Manipular estructuras de datos (listas, diccionarios, conjuntos)
- Organizar código en módulos y paquetes
- Manejar excepciones adecuadamente

### Unidad 1: POO Avanzada con Python (Semana 3-6)

**Objetivo General:** Dominar programación orientada a objetos aplicándola al diseño de modelos del sistema TaskFlow.

**Objetivos Específicos:**
- Definir clases y objetos usando dataclasses
- Aplicar encapsulamiento con propiedades
- Implementar herencia y composición
- Sobrecargar operadores y métodos mágicos
- Crear interfaces con ABCs y Protocols
- Diseñar modelos y DTOs con Pydantic
- Aplicar patrones de diseño (Singleton, Factory)

### Unidad 2: Técnicas de Desarrollo (Semana 7-9)

**Objetivo General:** Aplicar TDD, BDD y DDD para construir software de calidad con pruebas automatizadas.

**Objetivos Específicos:**
- Comprender y aplicar el ciclo Red-Green-Refactor
- Escribir tests unitarios con pytest
- Usar mocks y fixtures para aislar código
- Implementar escenarios BDD con Gherkin
- Distinguir entre Entidades y Value Objects
- Implementar patrón Repository y Services
- Inyectar dependencias apropiadamente

### Unidad 3: Desarrollo Backend (Semana 10-12)

**Objetivo General:** Construir una API REST completa con FastAPI y PostgreSQL.

**Objetivos Específicos:**
- Crear aplicación FastAPI con rutas
- Validar datos con Pydantic
- Inyectar dependencias en FastAPI
- Conectar con PostgreSQL usando SQLAlchemy
- Implementar endpoints CRUD completos
- Autenticar usuarios con JWT
- Documentar API con OpenAPI

### Unidad 4: Desarrollo Frontend (Semana 13-15)

**Objetivo General:** Crear una interfaz web moderna con Jinja2 y HTMX.

**Objetivos Específicos:**
- Usar sistema de templates Jinja2
- Aplicar herencia de templates
- Implementar interactividad con HTMX
- Crear formularios con validación
- Diseñar UI responsiva con Bootstrap 5
- Gestionar estado en el frontend
- Crear dashboard con métricas y gráficos

### Unidad 5: Proyecto Final (Semana 16-17)

**Objetivo General:** Integrar, probar, documentar y presentar el sistema completo TaskFlow.

**Objetivos Específicos:**
- Integrar todos los componentes del sistema
- Escribir pruebas end-to-end
- Optimizar performance y corregir bugs
- Documentar el proyecto completamente
- Preparar y ejecutar presentación
- Reflexionar sobre el aprendizaje

---

## Skills Generales del Curso

Al finalizar el curso, el estudiante será capaz de:

1. **Python Avanzado:** Escribir código Python limpio siguiendo PEP 8
2. **POO:** Diseñar sistemas usando principios orientados a objetos
3. **Testing:** Escribir tests unitarios y de integración con pytest
4. **TDD:** Aplicar desarrollo guiado por pruebas
5. **API REST:** Construir APIs con FastAPI y OpenAPI
6. **Base de Datos:** Diseñar y consultar bases de datos PostgreSQL
7. **Frontend:** Crear interfaces web con Jinja2 y HTMX
8. **DevOps:** Usar Git, ambientes virtuales, y configuración
9. **Documentación:** Escribir documentación técnica clara
10. **Colaboración:** Trabajar en parejas y sustentar trabajo

---

**Fin de Documento**

**Próxima actualización:** Post-implementación de primeras 4 clases
