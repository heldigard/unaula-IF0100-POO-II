# Rubricas de Evaluacion - IF0100 POO-II

## Informacion del Curso

| Campo | Detalle |
|-------|---------|
| **Codigo del Curso** | IF0100-POO-II |
| **Nombre del Curso** | Programacion Orientada a Objetos II |
| **Programa** | Ingenieria de Sistemas |
| **Institucion** | UNAULA - Universidad Autonoma Latinoamericana |
| **Periodo Academico** | 2026-I |
| **Docente** | [Nombre del Docente] |
| **Correo** | [Correo Institucional] |
| **Version del Documento** | 1.0 |
| **Ultima Actualizacion** | Febrero 2026 |

---

## Introduccion

Este documento establece las rublicas de evaluacion para el curso de Programacion Orientada a Objetos II. Cada rublica define los criterios, indicadores de logro y niveles de desempeño que se utilizaran para valorar el trabajo de los estudiantes. La evaluacion se realiza de manera integral, considerando tanto los aspectos tecnicos como la calidad del codigo y las buenas practicas de desarrollo.

Es fundamental que los estudiantes comprendan que la evaluacion no se limita a verificar que el codigo funcione, sino que también se valora la capacidad de escribir codigo mantenible, siguiendo estandares reconocidos y aplicando patrones de diseño apropiados. La escala de calificacion va desde el nivel Excelente (5.0) hasta Insuficiente (1.0-2.9), pasando por los niveles Bueno (4.0-4.9) y Suficiente (3.0-3.9).

---

## 1. Laboratorio 1: Scripts Python Basics

**Porcentaje del Curso:** 5%
**Fecha de Entrega:** Semana 3

### Descripcion del Laboratorio

En este laboratorio, los estudiantes deben demostrar dominio de los conceptos fundamentales de Python, incluyendo variables, tipos de datos, estructuras de control, funciones y manejo de errores. El trabajo debe reflejar comprension de la sintaxis de Python y la capacidad de escribir codigo limpio y eficiente que resuelva problemas propuestos.

### Rublrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Funcionalidad** | El codigo resuelve todos los problemas correctamente, maneja casos limite y entradas inesperadas sin errores | El codigo resuelve la mayoria de problemas, puede tener pequenos bugs en casos limite | El codigo resuelve los problemas basicos pero presenta errores en casos especiales o entradas invalidas | El codigo no funciona correctamente o solo resuelve una parte menor de los problemas |
| **Estilo PEP 8** | Codigo 100% compatible con PEP 8, indentacion consistente, longitud de lineas adecuada, spacing correcto | Codigo mayormente compatible con PEP 8, pequenas violaciones que no afectan la legibilidad | Codigo con varias violaciones de PEP 8 que afectan parcialmente la legibilidad | Codigo con multiples violaciones graves de PEP 8, dificil de leer y mantener |
| **Variables y Tipos** | Uso correcto y consistente de tipos de datos, nombres descriptivos y significativos, conversiones apropiadas | Uso correcto de tipos con pequenos problemas en nomenclatura o conversiones | Uso basico de tipos con algunos errores o inconsistencias | Uso incorrecto de tipos de datos o nombres de variables confusos/inadecuados |
| **Comentarios y Documentacion** | Docstrings completos en todas las funciones, comentarios utiles que explican el por que, sin obviedades | Documentacion presente con pequenos vacios o comentarios redundantes | Documentacion minima o con errores, comentarios insuficientes o excesivos | Ausencia de documentacion o comentarios que no aportan valor |
| **Ejecucion y Manejo de Errores** | Ejecucion sin errores, manejo apropiado de excepciones con mensajes claros, trazabilidad completa | Ejecucion con pequenos warnings o manejo de errores basico pero funcional | Ejecucion con errores menores que no impiden el funcionamiento, manejo de errores basico | Ejecucion con errores criticos o ausencia total de manejo de excepciones |

### Pesos de los Criterios

| Criterio | Peso |
|----------|------|
| Funcionalidad | 35% |
| Estilo PEP 8 | 20% |
| Variables y Tipos | 20% |
| Comentarios y Documentacion | 15% |
| Ejecucion y Manejo de Errores | 10% |

---

## 2. Laboratorio 2: Clases POO

**Porcentaje del Curso:** 5%
**Fecha de Entrega:** Semana 5

### Descripcion del Laboratorio

Este laboratorio evalua la capacidad de los estudiantes para implementar programas utilizando los pilares de la programacion orientada a objetos: encapsulamiento, herencia y polimorfismo. Los estudiantes deben demostrar comprension de conceptos como clases, objetos, metodos, modificadores de acceso y relaciones entre clases.

### Rublrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Definicion de Clases** | Clases bien diseñadas con responsabilidades claras, uso apropiado de abstraccion, constructores y metodos correctamente implementados | Clases funcionales con pequenas inconsistencias en el diseño o organizacion | Clases basicas que funcionan pero con responsabilidades poco claras o diseño suboptimo | Clases mal definidas, con responsabilidades mezcladas o errores de implementacion |
| **Encapsulamiento** | Uso correcto de modificadores de acceso (public, protected, private), propiedades con getters/setters cuando necesario, datos protegidos apropiadamente | Encapsulamiento basico con pequenos vacios en la proteccion de datos | Encapsulamiento presente pero con inconsistencias o exposicion de datos internos | Ausencia de encapsulamiento o datos completamente expuestos sin proteccion |
| **Herencia** | Herencia correctamente implementada con clases base y derivadas apropiadas, uso de super(), herencia multiple manejada correctamente | Herencia funcional con pequenas inconsistencias en la jerarquia o uso de super() | Herencia basica presente pero con problemas en la jerarquia de clases o duplicacion de codigo | Herencia incorrecta, clases sin relacion logica o errores de implementacion |
| **Polimorfismo** | Polimorfismo implementado con metodos sobreescritos, uso de decoradores apropiados, duck typing cuando es apropiado | Polimorfismo funcional con pequenas limitaciones o uso suboptimo | Polimorfismo basico presente pero sin aprovechar completamente sus beneficios | Ausencia de polimorfismo o implementacion incorrecta que causa errores |
| **Pruebas (Tests)** | Tests unitarios completos con cobertura alta, casos de prueba diversos, asserts significativos, uso de pytest | Tests funcionales con buena cobertura pero pequenos vacios en casos de prueba | Tests basicos presentes pero con cobertura limitada o asserts insuficientes | Ausencia de tests o tests que no funcionan correctamente |

### Pesos de los Criterios

| Criterio | Peso |
|----------|------|
| Definicion de Clases | 25% |
| Encapsulamiento | 20% |
| Herencia | 20% |
| Polimorfismo | 20% |
| Pruebas (Tests) | 15% |

---

## 3. Parcial 1

**Porcentaje del Curso:** 20%
**Fecha:** Semana 7
**Duracion:** 90 minutos

### Estructura del Parcial

El parcial evalua los conocimientos adquiridos en las primeras seis semanas del curso, abarcando fundamentos de Python, programacion orientada a objetos y tecnicas de testing. La evaluacion combina preguntas teoricas con ejercicios praticos de programacion.

### Distrubucion de Temas

| Tema | Porcentaje | Contenidos |
|------|------------|------------|
| Python Basics | 25% | Sintaxis, tipos de datos, estructuras de control, funciones, manejo de archivos, comprehensions |
| Programacion Orientada a Objetos | 35% | Clases, objetos, encapsulamiento, herencia, polimorfismo, Composition vs Inheritance |
| Testing | 25% | pytest basico, assertions, fixtures, parametrizacion, Coverage |
| Domain-Driven Design | 15% | Conceptos basicos de DDD, Entities, Value Objects, Aggregates |

### Rublrica de Calificacion Teorica

| Nivel | Puntuacion | Descripcion |
|-------|------------|-------------|
| Excelente | 5.0 | Respuestas completas y precisas, demuestra comprension profunda, ejemplos correctos |
| Bueno | 4.0 | Respuestas correctas con pequenos detalles faltantes o imprecisiones menores |
| Suficiente | 3.0 | Comprension basica del concepto, respuestas incompletas o con algunos errores |
| Insuficiente | 1.0-2.9 | Comprension insuficiente, respuestas incorrectas o ausentes |

### Rublrica de Calificacion Practica

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Correctitud del Codigo** | Codigo funciona perfectamente para todos los casos, incluyendo casos limite | Codigo funciona para casos principales, pequenos bugs en casos limite | Codigo funciona parcialmente, errores en algunos casos de prueba | Codigo no funciona o solo funciona para casos basicos |
| **Calidad del Codigo** | Codigo limpio, bien estructurado, sigue mejores practicas, nombres descriptivos | Codigo legible con pequenas areas de mejora | Codigo funcional pero dificil de leer o mantener | Codigo confuso, mal estructurado, dificil de entender |
| **Solucion Propuesta** | Solucion elegante, eficiente, con buen uso de estructuras de datos y algoritmos | Solucion funcional con pequena area de mejora en eficiencia | Solucion basica que funciona pero sin optimizacion | Solucion ineficiente o que no resuelve el problema adecuadamente |
| **Manejo de Errores** | Manejo apropiado de excepciones, validaciones completas | Manejo basico de errores con pequenas inconsistencias | Manejo de errores parcial o incorrecto | Ausencia de manejo de errores o errores no capturados |

---

## 4. Laboratorio 3: Tests Unitarios

**Porcentaje del Curso:** 5%
**Fecha de Entrega:** Semana 9

### Descripcion del Laboratorio

Este laboratorio se centra en el desarrollo de pruebas unitarias utilizando pytest. Los estudiantes deben demostrar capacidad para escribir tests que verifiquen el comportamiento del codigo, utilizando fixtures, parametros, mocks y asserts apropiados para lograr alta cobertura y tests mantenibles.

### Rublrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Cobertura de Tests** | Cobertura superior al 90%, todos los paths de ejecution probados, casos limite incluidos | Cobertura entre 75-90%, mayoria de paths probados | Cobertura entre 50-75%, paths basicos probados | Cobertura inferior al 50%, pocos paths probados |
| **Fixtures** | Fixtures bien diseñados con alcance apropiado, reusable, documentados, uso de autouse cuando apropiado | Fixtures funcionales con pequenos problemas de diseño o documentacion | Fixtures basicos presentes pero con problemas de scope o reusabilidad | Ausencia de fixtures o fixtures mal implementados |
| **Parametrizacion** | Parametrizacion maxima de tests, datos de prueba diversos y significativos, ev duplicacion | Parametrizacion presente con pequenos espacios de mejora | Parametrizacion basica con algunas repeticiones de codigo | Sin parametrizacion o tests duplicados innecesariamente |
| **Mocks y Patching** | Uso correcto de mocks para aislar unidades, verifica llamadas, parametros y tiempos, mocking de APIs externas | Mocks funcionales con pequenas inconsistencias en la verificacion | Mocks basicos presentes pero sin verificacion completa | Ausencia de mocks o mocks incorrectos que no aíslan las unidades |
| **Assertions** | Asserts claros y especificos, mensajes de error utiles, verifica valores esperados y tipos, uso de assertRaises | Assertions correctos con pequenos espacios de mejora en mensajes de error | Assertions basicos presentes pero limitados o poco especificos | Assertions insuficientes, incorrectos o ausentes |

### Pesos de los Criterios

| Criterio | Peso |
|----------|------|
| Cobertura de Tests | 25% |
| Fixtures | 20% |
| Parametrizacion | 20% |
| Mocks y Patching | 20% |
| Assertions | 15% |

---

## 5. Laboratorio 4: API con FastAPI

**Porcentaje del Curso:** 5%
**Fecha de Entrega:** Semana 11

### Descripcion del Laboratorio

En este laboratorio, los estudiantes deben desarrollar una API REST completa utilizando FastAPI. La evaluacion se centra en la correcta implementacion de endpoints CRUD, validacion de datos con Pydantic, manejo apropiado de codigos de estado HTTP, documentacion automatica con Swagger UI y pruebas de la API.

### Rublrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Endpoints CRUD** | API completa con todos los endpoints CRUD funcionando perfectamente, rutas bien diseñadas, RESTful API correctamente implementada | Endpoints funcionales con pequenas inconsistencias en el diseño REST | Endpoints basicos presentes pero con problemas de diseño o funcionalidad parcial | Endpoints incompletos, no funcionales o mal diseñados |
| **Validacion Pydantic** | Modelos Pydantic completos con validaciones personalizadas, mensajes de error claros, restricciones apropiadas | Validacion funcional con pequenas areas de mejora en mensajes o restricciones | Validacion basica presente pero limitada o con mensajes de error confusos | Ausencia de validacion o validacion incorrecta que permite datos invalidos |
| **Status Codes** | Uso correcto de todos los codigos de estado HTTP (200, 201, 204, 400, 404, 500), respuestas apropiadas para cada situacion | Codigos de estado correctos con pequenas inconsistencias en respuestas | Uso basico de status codes con algunos errores o respuestas inadecuadas | Status codes incorrectos o ausentes, respuestas inadecuadas |
| **Documentacion** | Documentacion completa con Swagger UI y ReDoc, ejemplos de peticion/respuesta, descripciones claras de endpoints y modelos | Documentacion funcional con pequenas areas de mejora en ejemplos o descripciones | Documentacion basica presente pero incompleta o con descripciones insuficientes | Ausencia de documentacion o documentacion inutilizable |
| **Testing de API** | Tests de integracion completos para todos los endpoints, cobertura alta, uso de TestClient, pruebas de errores | Tests funcionales con buena cobertura pero pequenos vacios | Tests basicos presentes pero con cobertura limitada o pruebas superficiales | Ausencia de tests de API o tests que no funcionan correctamente |

### Pesos de los Criterios

| Criterio | Peso |
|----------|------|
| Endpoints CRUD | 30% |
| Validacion Pydantic | 20% |
| Status Codes | 15% |
| Documentacion | 15% |
| Testing de API | 20% |

---

## 6. Parcial 2

**Porcentaje del Curso:** 20%
**Fecha:** Semana 13
**Duracion:** 90 minutos

### Estructura del Parcial

El segundo parcial evalua los conocimientos relacionados con el desarrollo de APIs con FastAPI, validacion de datos, manejo de dependencias y pruebas de APIs. La evaluacion combina preguntas teoricas con ejercicios praticos de desarrollo.

### Distribucion de Temas

| Tema | Porcentaje | Contenidos |
|------|------------|------------|
| FastAPI | 35% | Routing, dependencies, middleware, background tasks, WebSocket (basico) |
| Pydantic | 25% | Modelos de datos, validaciones personalizadas, serializacion, opciones de campo |
| Dependencias | 20% | Dependency injection, Depends, bases de datos, autenticacion |
| pytest con FastAPI | 20% | TestClient, fixtures, testing asincrono, mocks en API |

### Rublrica de Calificacion Teorica

| Nivel | Puntuacion | Descripcion |
|-------|------------|-------------|
| Excelente | 5.0 | Respuestas completas y precisas, demuestra comprension profunda, ejemplos correctos incluyendo casos edge |
| Bueno | 4.0 | Respuestas correctas con pequenos detalles faltantes o imprecisiones menores |
| Suficiente | 3.0 | Comprension basica del concepto, respuestas incompletas o con algunos errores conceptuales |
| Insuficiente | 1.0-2.9 | Comprension insuficiente, respuestas incorrectas o ausentes |

### Rublrica de Calificacion Practica

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Implementacion API** | API completa y funcional, endpoints bien diseñados, manejo correcto de parametros y cuerpos de peticion | API funcional con pequenas inconsistencias en el diseño o manejo de parametros | API basica con problemas de diseño o funcionalidad parcial | API incompleta, no funcional o con errores criticos |
| **Modelos Pydantic** | Modelos completos con validaciones personalizadas, uso de Field, configuracion de serializacion | Modelos funcionales con pequenas areas de mejora | Modelos basicos con validaciones limitadas o problemas de definicion | Modelos ausentes, incorrectos o sin validacion apropiada |
| **Dependencies** | Sistema de dependencias bien diseñado, injection correcta, manejo de recursos (DB, auth) | Dependencias funcionales con pequenos problemas de diseño | Dependencias basicas presentes pero con problemas de scope o manejo de recursos | Ausencia de dependencias o dependencias mal implementadas |
| **Testing** | Tests completos de API con TestClient, coverage alto, pruebas de casos de exito y error | Tests funcionales con buena cobertura pero pequenos vacios | Tests basicos presentes pero con cobertura limitada | Ausencia de tests o tests que no funcionan |

---

## 7. Proyecto Final: TaskFlow

**Porcentaje del Curso:** 30%
**Fecha de Entrega:** Semana 17

### Descripcion del Proyecto

El Proyecto Final TaskFlow es un sistema de gestion de tareas y proyectos que integra todos los conceptos aprendidos durante el curso. Los estudiantes deben desarrollar una aplicacion completa utilizando arquitectura Domain-Driven Design (DDD), API REST con FastAPI, pruebas unitarias comprehensivas y documentacion profesional.

### Requisitos del Proyecto

El sistema TaskFlow debe incluir las siguientes funcionalidades principales: gestion de usuarios con autenticacion, creacion y administracion de proyectos, gestion de tareas dentro de proyectos con diferentes estados y prioridades, comentarios en tareas para colaboracion, y un sistema de notificaciones. La arquitectura debe seguir los principios de DDD con separation of concerns clara entre capas de dominio, aplicacion, infraestructura y presentacion.

### Rublrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Funcionalidad** (30%) | Sistema completamente funcional, todas las caracteristicas implementadas, casos limite manejados, experiencia de usuario fluida | Sistema funcional con pequenas limitaciones menores en caracteristicas secundarias | Sistema basico funcional pero con caracteristicas faltantes o bugs en flujos principales | Sistema no funcional o con caracteristicas criticas faltantes |
| **Arquitectura DDD** (20%) | Arquitectura DDD completa y correcta, bounded contexts claramente definidos, Entities, Value Objects, Aggregates bien definidos, repositories correctamente implementados | Arquitectura DDD funcional con pequenas inconsistencias en la separacion de capas o diseño de agregados | Arquitectura basica presente pero con confusion en las capas o diseño de dominio deficiente | Ausencia de arquitectura DDD o mal implementada sin separation of concerns |
| **API REST** (20%) | API REST completa y bien diseñada, endpoints intuitivos, versionamiento, pagination, filtering, HATEOAS basico | API funcional con pequenas inconsistencias en el diseño REST o falta de algunas caracteristicas | API basica presente pero con problemas de diseño o endpoints mal estructurados | API mal diseñada, no RESTful, o con problemas criticos de implementacion |
| **Testing** (15%) | Cobertura superior al 85%, tests unitarios, de integracion y e2e, mocks apropiados, tests parametrizados | Buena cobertura (70-85%) con la mayoria de scenarios probados | Tests basicos presentes pero con cobertura limitada (50-70%) o calidad de tests suboptima | Cobertura inferior al 50%, tests ausentes o que no funcionan correctamente |
| **Calidad del Codigo** (10%) | Codigo limpio, DRY, SRP, naming consistente, typing completo, sin code smells, refactorizado | Codigo legible con pequenas areas de mejora en calidad o consistencia | Codigo funcional pero con algunos code smells o inconsistencias | Codigo con multiples code smells, dificil de mantener, sin atencion a calidad |
| **Documentacion** (5%) | Documentacion completa: README, API docs, arquitectura, guia de instalacion, ejemplos de uso | Documentacion funcional con pequenos vacios en alguna seccion | Documentacion basica presente pero incompleta o con secciones faltantes | Documentacion minima o ausentes secciones criticas |

### Desglose de Pesos del Proyecto Final

| Criterio | Peso |
|----------|------|
| Funcionalidad | 30% |
| Arquitectura DDD | 20% |
| API REST | 20% |
| Testing | 15% |
| Calidad del Codigo | 10% |
| Documentacion | 5% |

### Requisitos Minimos para Aprobar

Para que el proyecto sea considerado para calificacion, debe cumplir con los siguientes requisitos minimos: el codigo debe ejecutarse sin errores criticos, la API debe responder a las peticiones basicas, y al menos el 50% de coverage en pruebas unitarias. Proyectos que no cumplan estos requisitos seran calificados como Insuficientes (1.0-2.9).

---

## 8. Seguimiento

**Porcentaje del Curso:** 30%
**Distribuido a lo largo del semestre**

### Descripcion

La componente de seguimiento evalua el progreso continuo del estudiante a traves de diversas actividades que demuestran comprension y aplicacion de los conceptos del curso. Esta componente es fundamental porque refleja el compromiso y la consistencia del estudiante durante el semestre.

### Desglose de Actividades

| Actividad | Porcentaje | Frecuencia | Descripcion |
|-----------|------------|------------|-------------|
| Quices | 10% | Semanal | Evaluaciones cortas de conocimiento teorico y practico |
| Talleres | 10% | Quincenal | Ejercicios praticos en clase con supervision del docente |
| Actividades Swarm | 5% | Mensual | Colaboracion en equipos para resolucion de problemas complejos |
| Participacion | 5% | Continua | Aportes en clase, preguntas, discusiones tecnicas |

### Rublrica de Quices

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Respuestas Correctas** | 90-100% de respuestas correctas | 75-89% de respuestas correctas | 60-74% de respuestas correctas | Menos del 60% de respuestas correctas |
| **Tiempo de Respuesta** | Respuestas rapidas y precisas | Respuestas dentro del tiempo limite con pequenas demoras | Respuestas entregadas con algunas demoras | Respuestas incompletas o no entregadas |
| **Comprension Conceptual** | Demuestra comprension profunda, puede explicar el razonamiento | Comprension solida con pequenas imprecisiones | Comprension basica del tema | Comprension insuficiente del tema |

### Rublrica de Talleres

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Completitud** | Todos los ejercicios resueltos correctamente | Mayoria de ejercicios resueltos correctamente | Ejercicios basicos resueltos, avanzados incompletos | Pocos ejercicios resueltos o con errores graves |
| **Calidad de Solucion** | Soluciones optimas, eficientes y bien explicadas | Soluciones correctas con pequenas areas de mejora | Soluciones funcionales pero suboptimas | Soluciones incorrectas o mal estructuradas |
| **Participacion Activa** | Participacion activa, ayuda a compañeros, formula preguntas pertinentes | Participacion regular con pequenos aportes | Participacion minima requerida | Ausencia de participacion o participacion pasiva |

### Rublrica de Actividades Swarm

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Colaboracion** | Contribucion significativa al equipo, comparticion de conocimientos, liderazgo | Colaboracion activa con pequenas limitaciones | Colaboracion basica presente | Colaboracion minima o nula |
| **Calidad de Aporte** | Aportes tecnicos de alto valor que mejoran la solucion colectiva | Aportes utiles que contribuyen al objetivo | Aportes basicos que cumplen el minimo | Aportes insuficientes o que no agregan valor |
| **Integracion** | Trabajo sincronizado con el equipo, comunicacion efectiva | Buena integracion con pequenas descoordinaciones | Integracion basica con algunos problemas de comunicacion | Falta de integracion con el equipo |

### Rublrica de Participacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Calidad de Preguntas** | Preguntas profundas que demuestran comprension avanzada, genera discusiones tecnicas | Preguntas pertinentes que muestran interes genuino | Preguntas basicas sobre el contenido | Ausencia de preguntas o preguntas superficiales |
| **Aportes en Clase** | Aportes que enriquecen la discusion, aporta ejemplos relevantes y perspectivas nuevas | Aportes utiles que contribuyen positivamente | Aportes minimos que cumplen las expectativas | Ausencia de aportes o aportes irrelevantes |
| **Actitud** | Actitud positiva, respetuosa, promueve el aprendizaje colectivo | Actitud adecuada con pequenas areas de mejora | Actitud aceptable sin problemas | Actitud que afecta negativamente el ambiente de aprendizaje |

---

## 9. Politica de Entregas Tardias

### Aplicacion de Penalizaciones

Todas las entregas de laboratorios, proyecto final y trabajos tienen una politica de penalizacion por entrega tardia que busca promover la responsabilidad y la gestion adecuada del tiempo. Las penalizaciones se aplican de manera progresiva segun el tiempo de demora en la entrega.

| Tiempo de Demora | Penalizacion |
|------------------|--------------|
| Hasta 24 horas | 10% de la nota |
| 24-48 horas | 20% de la nota |
| 48-72 horas | 30% de la nota |
| Mas de 72 horas | 50% de la nota o no aceptado |

### Consideraciones Especiales

Existen circunstancias que pueden例外 de la politica de entregas tardias. Los estudiantes deben comunicarse con el docente lo antes posible cuando enfrenten situaciones extraordinarias como problemas de salud documentados con certificado medico, emergencias familiares, problemas tecnicos graves con el equipo de computo que impidan el trabajo, o situaciones fuera del control del estudiante que afecten significativamente su capacidad de entrega. Las solicitudes de excepcion deben ser presentadas por escrito con la documentacion de soporte correspondiente.

### Procedimiento de Solicitud

Para solicitar una exception a la politica de entregas tardias, el estudiante debe enviar un correo electronico al docente con el asunto «Solicitud de Excepcion - [Nombre del Estudiante] - [Codigo del Curso]» dentro de las 48 horas siguientes al vencimiento del plazo. El correo debe incluir una descripcion detallada de la situacion, la documentacion de soporte necesaria, y la nueva fecha de entrega propuesta si es applicable.

### Entregas Tardias en Parciales

Los parciales tienen tolerancia de 15 minutos para el inicio. Despues de este tiempo, el estudiante no podra presentar el examen y debera justificar su ausencia para poder presentarlo en una fecha alternativa. Las justificaciones deben entregarse dentro de las 48 horas siguientes al parcial y estaran sujetas a verificacion.

---

## 10. Resumen de Calificaciones

### Distribucion Final del Curso

| Componente | Porcentaje |
|------------|------------|
| Laboratorio 1: Python Basics | 5% |
| Laboratorio 2: Clases POO | 5% |
| Parcial 1 | 20% |
| Laboratorio 3: Tests Unitarios | 5% |
| Laboratorio 4: FastAPI | 5% |
| Parcial 2 | 20% |
| Proyecto Final: TaskFlow | 30% |
| Seguimiento | 30% |
| **Total** | **100%** |

### Escala de Calificacion Final

| Rango | Nota | Descriptor |
|-------|------|------------|
| 4.6 - 5.0 | Sobresaliente | Dominio completo de los objetivos, trabajo de alta calidad |
| 4.0 - 4.5 | Bueno | Cumplimiento satisfactorio de los objetivos |
| 3.0 - 3.9 | Aprobado | Cumplimiento minimo de los objetivos |
| 1.0 - 2.9 | No Aprobado | No cumplimiento de los objetivos |

### Requisitos para Aprobar el Curso

Para aprobar el curso, el estudiante debe cumplir con los siguientes requisitos: obtener una nota definitiva igual o superior a 3.0, haber presentado todos los laboratorios y el proyecto final, y haber presentado ambos parciales. El incumplimiento de cualquiera de estos requisitos resultara en la reprobacion del curso independientemente del promedio ponderado.

---

## 11. Anexos

### Anexo A: Formato de Entrega de Codigo

Todo el codigo fuente debe entregarse en un repositorio Git con la siguiente estructura:

```
proyecto/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   └── repositories/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   └── integration/
├── docs/
├── requirements.txt
├── pytest.ini
└── README.md
```

### Anexo B: Checklist de Entrega

Antes de cada entrega, verifique que ha completado los siguientes items:

- El codigo esta en un repositorio Git con commits descriptivos
- Todos los tests pasan correctamente (pytest)
- El coverage es el esperado segun la rublrica
- El archivo requirements.txt incluye todas las dependencias
- El README.md tiene instrucciones claras de instalacion y ejecucion
- No hay archivos de cache, archivos temporales ni datos sensibles en el repositorio
- La documentacion requerida esta completa y actualizada

### Anexo C: Recursos de Apoyo

Para profundizar en los temas del curso, se recomiendan los siguientes recursos:

- **Python**: Documentacion oficial de Python, PEP 8 Style Guide, Fluent Python de Luciano Ramalho
- **POO**: Design Patterns: Elements of Reusable Object-Oriented Software de Gang of Four
- **pytest**: Documentacion oficial de pytest, Python Testing with pytest de Brian Okken
- **FastAPI**: Documentacion oficial de FastAPI, Building Microservices with Python de Harwal
- **DDD**: Domain-Driven Design de Eric Evans, Implementing Domain-Driven Design de Vaughn Vernon

---

## Informacion del Documento

| Campo | Valor |
|-------|-------|
| **Version** | 1.0 |
| **Autor** | [Nombre del Docente] |
| **Fecha de Creacion** | Febrero 2026 |
| **Ultima Revision** | [Fecha de ultima revision] |
| **Aprobado por** | [Nombre del coordinador] |

---

*Este documento esta sujeto a modificaciones. Cualquier cambio sera comunicado con al menos dos semanas de anticipacion a los estudiantes afectados.*
