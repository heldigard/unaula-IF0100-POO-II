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
- [Unidad 3: Desarrollo Web con FastAPI](#unidad-3-desarrollo-web-con-fastapi)
- [Unidad 4: Persistencia Relacional en el Proyecto](#unidad-4-persistencia-relacional-en-el-proyecto)
- [Unidad 5: Proyecto Final y Sustentación](#unidad-5-proyecto-final-y-sustentación)

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
| **1.8** | 1 | **Evaluación 1** | 1. Demostrar comprensión de POO<br>2. Aplicar conceptos al proyecto<br>3. Escribir código limpio y documentado | - [ ] Diseñar clases de dominio<br>- [ ] Implementar lógica base<br>- [ ] Entregar repositorio Git | **Taller (15%)** | **Entrega 1:** Dominio del sistema |
...
| **3.7** | 3 | **Evaluación 3** | 1. Construir API funcional<br>2. Implementar autenticación<br>3. Documentar con OpenAPI | - [ ] Implementar rutas FastAPI<br>- [ ] Desplegar API funcional<br>- [ ] Demostrar endpoints en Swagger | **Prototipo (20%)** | **Entrega 3:** API funcionando |
| **4.1** | 4 | SQLAlchemy ORM / Modelos | 1. Configurar SQLAlchemy 2.0 con modelos declarativos<br>2. Diseñar entidades con tipos de columna y constraints<br>3. Aplicar herencia con DeclarativeBase<br>4. Modelar Usuario, Proyecto y Tarea | - [ ] Crear Base y engine SQLite<br>- [ ] Definir modelos con Mapped[T]<br>- [ ] Implementar __repr__ y métodos de dominio<br>- [ ] Crear tablas con create_all | - | TaskFlow: Modelos de persistencia |
| **4.2** | 4 | Alembic / Migraciones | 1. Configurar Alembic en el proyecto<br>2. Generar migraciones automáticas<br>3. Aplicar y revertir migraciones<br>4. Versionar esquema en equipo | - [ ] Inicializar Alembic<br>- [ ] Configurar env.py con Base.metadata<br>- [ ] Generar primera migración autogenerada<br>- [ ] Aplicar con upgrade head | **Software (15%)** | **E4:** SQLAlchemy + Alembic (23/04) |
| **4.3** | 4 | SQLAlchemy Relaciones | 1. Implementar relaciones One-to-Many<br>2. Usar ForeignKey y relationship<br>3. Aplicar cascadas y lazy/eager loading<br>4. Validar integridad referencial | - [ ] Relacionar Usuario → Proyectos → Tareas<br>- [ ] Usar back_populates en relaciones<br>- [ ] Definir Enum para estados<br>- [ ] Consultar con joins | - | TaskFlow: Jerarquía completa |
| **4.4** | 4 | CRUD con SQLAlchemy | 1. Crear, leer, actualizar y eliminar entidades<br>2. Filtrar, ordenar y paginar queries<br>3. Manejar transacciones y commits<br>4. Validar datos antes de persistir | - [ ] Implementar CRUD completo<br>- [ ] Usar Session con context manager<br>- [ ] Crear queries con filtros<br>- [ ] Manejar rollback en errores | - | TaskFlow: Operaciones de datos |
| **5.1** | 5 | Repository Pattern | 1. Abstraer acceso a datos con Repository<br>2. Crear interfaces genéricas<br>3. Implementar repositories con SQLAlchemy<br>4. Aplicar inversión de dependencias | - [ ] Definir ABC Repository<br>- [ ] Implementar UserRepository, ProjectRepository<br>- [ ] Inyectar repositories en servicios<br>- [ ] Desacoplar capas | - | TaskFlow: Capa de persistencia |
| **5.2** | 5 | Clean Architecture + JWT | 1. Separar capas: Domain, Use Cases, Infrastructure<br>2. Implementar JWT Authentication en FastAPI<br>3. Proteger endpoints con OAuth2PasswordBearer<br>4. Organizar código por responsabilidades | - [ ] Crear capas domain/application/infrastructure/api<br>- [ ] Implementar login con JWT<br>- [ ] Proteger rutas con Depends(get_current_user)<br>- [ ] Aplicar inyección de dependencias | **Software (15%)** | **E5:** CRUD + JWT + Arquitectura (07/05) |
| **5.3** | 5 | DTOs y Serialización | 1. Validar entrada/salida con Pydantic v2<br>2. Serializar relaciones anidadas<br>3. Manejar passwords con hash seguro<br>4. Documentar schemas en OpenAPI | - [ ] Crear schemas anidados<br>- [ ] Serializar listas de tareas<br>- [ ] Integrar passlib para hashing<br>- [ ] Validar con Field constraints | - | TaskFlow: API type-safe |
| **5.4** | 5 | API REST Avanzada | 1. Implementar paginación en listados<br>2. Crear endpoints anidados (/proyectos/{id}/tareas)<br>3. Aplicar filtrado y búsqueda<br>4. Optimizar queries con eager loading | - [ ] Paginar resultados con limit/offset<br>- [ ] Crear rutas anidadas<br>- [ ] Filtrar por estado y usuario<br>- [ ] Usar joinedload para N+1 | - | TaskFlow: Endpoints avanzados |
| **5.5** | 5 | Testing de Integración | 1. Escribir tests con base de datos de prueba<br>2. Testear autenticación JWT<br>3. Alcanzar cobertura mínima 60%<br>4. Usar fixtures y dependency overrides | - [ ] Configurar DB de test con SQLite<br>- [ ] Testear login y rutas protegidas<br>- [ ] Medir cobertura con pytest-cov<br>- [ ] Mockear servicios externos | - | TaskFlow: Calidad asegurada |
| **5.6** | 5 | Pulido del Proyecto | 1. Pulir manejo de errores de la API<br>2. Corregir bugs y edge cases<br>3. Optimizar performance de queries<br>4. Revisar documentación técnica | - [ ] Documentar schemas en OpenAPI<br>- [ ] Optimizar queries lentas<br>- [ ] Revisar manejo de errores<br>- [ ] Actualizar README | - | TaskFlow: Versión pulida |
| **5.7** | 5 | Preparación Sustentación | 1. Revisar funcionalidad completa<br>2. Preparar demo en vivo<br>3. Ensayar preguntas técnicas<br>4. Organizar repositorio para entrega | - [ ] Checklist de features<br>- [ ] Script de demo<br>- [ ] Revisar código en parejas<br>- [ ] Preparar ambiente de presentación | - | TaskFlow: Listo para demo |
| **5.8** | 5 | **Sustentación Final** | 1. Presentar proyecto completo<br>2. Demostrar funcionalidad<br>3. Responder preguntas<br>4. Reflexionar sobre aprendizaje | - [ ] Presentar (10-15 min)<br>- [ ] Demostrar sistema completo<br>- [ ] Responder preguntas técnicas<br>- [ ] Autoevaluación | **Proyecto (20%)** | **Sustentación Final:** Sistema TaskFlow (28/05) |

---

## Resumen de Evaluaciones

| Evaluación | Unidad | Peso | Formato | Semana |
|------------|--------|------|---------|--------|
| Evaluación 1 | 1.8 | 15% | Examen teórico-práctico + modelos | 6 |
| Evaluación 2 | 2.7 | 15% | Taller práctico + sustentación | 9 |
| Evaluación 3 | 3.7 | 20% | Examen práctico + API funcionando | 12 |
| Evaluación 4 | 4.2 | 15% | Software: SQLAlchemy modelos + migraciones | 11 |
| Evaluación 5 | 5.2 | 15% | Software: CRUD + JWT + Arquitectura | 13 |
| Evaluación Final | 5.8 | 20% | Sustentación del proyecto completo | 16 |
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

### Unidad 4: Persistencia Relacional en el Proyecto (Semana 11-12)

**Objetivo General:** Modelar el dominio en base de datos relacional con SQLAlchemy 2.0 y Alembic.

**Objetivos Específicos:**
- Configurar SQLAlchemy con modelos declarativos
- Diseñar entidades con tipos de columna, constraints y claves primarias
- Implementar relaciones One-to-Many entre entidades
- Aplicar herencia con DeclarativeBase para reutilizar comportamiento
- Crear y ejecutar migraciones con Alembic
- Implementar CRUD completo con SQLAlchemy
- Integrar autenticación JWT con base de datos relacional

### Unidad 5: Proyecto Final y Sustentación (Semana 13-16)

**Objetivo General:** Integrar, probar, documentar y presentar el sistema completo TaskFlow.

**Objetivos Específicos:**
- Aplicar patrón Repository y Clean Architecture
- Crear DTOs y serialización con Pydantic v2
- Implementar APIs REST avanzadas con paginación y filtros
- Escribir pruebas de integración con base de datos
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
7. **API REST:** Construir APIs type-safe con FastAPI, Pydantic y OpenAPI
8. **DevOps:** Usar Git, ambientes virtuales, y configuración
9. **Documentación:** Escribir documentación técnica clara
10. **Colaboración:** Trabajar en parejas y sustentar trabajo

---

**Fin de Documento**

**Próxima actualización:** Post-implementación de primeras 4 clases
