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
| **1.8** | 1 | **Evaluación 1** | 1. Demostrar comprensión de POO<br>2. Aplicar conceptos al proyecto<br>3. Escribir código limpio y documentado | - [ ] Diseñar clases de dominio<br>- [ ] Implementar lógica base<br>- [ ] Entregar repositorio Git | **Taller (15%)** | **Entrega 1:** Dominio del sistema |
...
| **3.7** | 3 | **Evaluación 3** | 1. Construir API funcional<br>2. Implementar autenticación<br>3. Documentar con OpenAPI | - [ ] Implementar rutas FastAPI<br>- [ ] Desplegar API funcional<br>- [ ] Demostrar endpoints en Swagger | **Prototipo (20%)** | **Entrega 3:** API funcionando |
...
| **5.4** | 5 | **Sustentación final** | 1. Presentar proyecto completo<br>2. Demostrar funcionalidad<br>3. Responder preguntas<br>4. Reflexionar sobre aprendizaje | - [ ] Presentar (10-15 min)<br>- [ ] Demostrar sistema completo<br>- [ ] Responder preguntas técnicas<br>- [ ] Autoevaluación | **Proyecto (20%)** | **Sustentación Final:** Sistema TaskFlow |

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
