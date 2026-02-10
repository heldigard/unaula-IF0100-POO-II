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
| **Version del Documento** | 2.0 |
| **Ultima Actualizacion** | Febrero 2026 |

---

## Introduccion

Este documento establece las rubricas de evaluacion para el curso de Programacion Orientada a Objetos II. Cada rubrica define los criterios, indicadores de logro y niveles de desempeno que se utilizaran para valorar el trabajo de los estudiantes. La evaluacion se realiza de manera integral, considerando tanto los aspectos tecnicos como la calidad del codigo y las buenas practicas de desarrollo.

Es fundamental que los estudiantes comprendan que la evaluacion no se limita a verificar que el codigo funcione, sino que tambien se valora la capacidad de escribir codigo mantenible, siguiendo estandares reconocidos y aplicando patrones de diseno apropiados. La escala de calificacion va desde el nivel Excelente (5.0) hasta Insuficiente (1.0-2.9), pasando por los niveles Bueno (4.0-4.9) y Suficiente (3.0-3.9).

---

## Resumen de Evaluaciones

### Distribucion por Seguimientos

| Seguimiento | Porcentaje Acumulado | Evaluaciones | Fecha Limite |
|-------------|---------------------|--------------|--------------|
| **Primer Seguimiento** | 50% | Quiz 1 (15%) + Taller 1 (15%) + Parcial 1 (20%) | 27 marzo 2026 |
| **Segundo Seguimiento** | 80% | Taller 2 (15%) + Proyecto Parcial (15%) | 15 mayo 2026 |
| **Tercer Seguimiento** | 100% | Proyecto Final (20%) | 28 mayo 2026 |

### Calendario de Evaluaciones

| # | Evaluacion | Peso | Fecha | Unidad | Seguimiento |
|---|------------|------|-------|--------|-------------|
| 1 | **Quiz 1** - Fundamentos Python | 15% | 19/02/2026 | U00 | 1er (50%) |
| 2 | **Taller 1** - Modelado OO | 15% | 03/03/2026 | U01 | 1er (50%) |
| 3 | **Parcial 1** - Python + POO | 20% | 12/03/2026 | U01 | 1er (50%) |
| 4 | **Taller 2** - TDD + Testing | 15% | 19/03/2026 | U02 | 2do (30%) |
| 5 | **Proyecto Parcial** - TaskFlow API | 15% | 16/04/2026 | U03 | 2do (30%) |
| 6 | **Proyecto Final** - TaskFlow Completo | 20% | 07/05/2026 | U03 | 3er (20%) |
| | **TOTAL** | **100%** | | | |

---

## 1. Quiz 1 - Fundamentos Python

**Porcentaje del Curso:** 15%
**Fecha:** 19 de febrero de 2026
**Duracion:** 45 minutos
**Unidad:** U00 - Fundamentos Python

### Descripcion

Este quiz evalua los conocimientos fundamentales de Python adquiridos en las primeras semanas del curso. Incluye preguntas teoricas y ejercicios practicos cortos sobre sintaxis, tipos de datos, estructuras de control, funciones y manejo de excepciones.

### Distribucion de Temas

| Tema | Porcentaje del Quiz |
|------|---------------------|
| Variables y tipos de datos | 20% |
| Estructuras de control (if, for, while) | 25% |
| Funciones y ambito | 25% |
| Estructuras de datos (listas, diccionarios) | 20% |
| Manejo de excepciones | 10% |

### Rubrica de Calificacion

| Nivel | Puntuacion | Descripcion |
|-------|------------|-------------|
| **Excelente** | 5.0 | 90-100% de respuestas correctas. Dominio completo de la sintaxis y conceptos. Codigo limpio y eficiente. |
| **Bueno** | 4.0 | 75-89% de respuestas correctas. Comprension solida con pequenos errores menores. |
| **Suficiente** | 3.0 | 60-74% de respuestas correctas. Comprension basica, errores que no impiden funcionamiento. |
| **Insuficiente** | 1.0-2.9 | Menos del 60% de respuestas correctas. Comprension insuficiente de los conceptos basicos. |

### Criterios de Evaluacion Practica

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Sintaxis Python** | Codigo 100% valido, uso correcto de indentacion, estructuras y convenciones | Pequenos errores de sintaxis que no afectan ejecucion | Errores de sintaxis que requieren correccion | Errores graves de sintaxis que impiden ejecucion |
| **Logica de Solucion** | Solucion optima, eficiente y bien estructurada | Solucion correcta con pequenas ineficiencias | Solucion funcional pero suboptima | Solucion incorrecta o incompleta |
| **Manejo de Errores** | Manejo apropiado de casos limite y excepciones | Manejo basico de errores presente | Manejo de errores parcial | Sin manejo de errores |

---

## 2. Taller 1 - Modelado Orientado a Objetos

**Porcentaje del Curso:** 15%
**Fecha:** 03 de marzo de 2026
**Unidad:** U01 - Programacion Orientada a Objetos

### Descripcion

Este taller evalua la capacidad de los estudiantes para modelar soluciones utilizando los pilares de la programacion orientada a objetos: encapsulamiento, herencia y polimorfismo. Los estudiantes deben disenar e implementar un sistema de clases que resuelva un problema propuesto.

### Rubrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Diseno de Clases** (25%) | Clases bien disenadas con responsabilidades claras, uso apropiado de abstraccion, constructores y metodos correctamente implementados | Clases funcionales con pequenas inconsistencias en el diseno | Clases basicas que funcionan pero con responsabilidades poco claras | Clases mal definidas o con errores de implementacion |
| **Encapsulamiento** (20%) | Uso correcto de modificadores de acceso, propiedades con getters/setters cuando necesario, datos protegidos | Encapsulamiento basico con pequenos vacios | Encapsulamiento presente pero con inconsistencias | Ausencia de encapsulamiento |
| **Herencia** (20%) | Herencia correctamente implementada con jerarquia apropiada, uso de super() | Herencia funcional con pequenas inconsistencias | Herencia basica presente pero con problemas en la jerarquia | Herencia incorrecta o sin relacion logica |
| **Polimorfismo** (20%) | Polimorfismo implementado con metodos sobreescritos, duck typing cuando es apropiado | Polimorfismo funcional con pequenas limitaciones | Polimorfismo basico presente | Ausencia de polimorfismo |
| **Pruebas** (15%) | Tests unitarios completos con cobertura alta, asserts significativos | Tests funcionales con buena cobertura | Tests basicos presentes | Ausencia de tests |

### Pesos de los Criterios

| Criterio | Peso |
|----------|------|
| Diseno de Clases | 25% |
| Encapsulamiento | 20% |
| Herencia | 20% |
| Polimorfismo | 20% |
| Pruebas | 15% |

---

## 3. Parcial 1 - Python y Programacion Orientada a Objetos

**Porcentaje del Curso:** 20%
**Fecha:** 12 de marzo de 2026
**Duracion:** 90 minutos
**Unidad:** U00-U01

### Descripcion

El primer parcial evalua los conocimientos adquiridos en las primeras semanas del curso, abarcando fundamentos de Python y programacion orientada a objetos. La evaluacion combina preguntas teoricas con ejercicios practicos de programacion.

### Distribucion de Temas

| Tema | Porcentaje | Contenidos |
|------|------------|------------|
| Python Basics | 30% | Sintaxis, tipos de datos, estructuras de control, funciones, comprehensions |
| Programacion Orientada a Objetos | 40% | Clases, objetos, encapsulamiento, herencia, polimorfismo, metodos especiales |
| Testing Basico | 20% | pytest, assertions, fixtures basicos |
| Domain-Driven Design | 10% | Conceptos basicos de DDD, Entities, Value Objects |

### Rubrica de Calificacion Teorica

| Nivel | Puntuacion | Descripcion |
|-------|------------|-------------|
| Excelente | 5.0 | Respuestas completas y precisas, demuestra comprension profunda, ejemplos correctos |
| Bueno | 4.0 | Respuestas correctas con pequenos detalles faltantes |
| Suficiente | 3.0 | Comprension basica, respuestas incompletas o con algunos errores |
| Insuficiente | 1.0-2.9 | Comprension insuficiente, respuestas incorrectas o ausentes |

### Rubrica de Calificacion Practica

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Correctitud del Codigo** | Codigo funciona perfectamente para todos los casos | Codigo funciona para casos principales | Codigo funciona parcialmente | Codigo no funciona o solo para casos basicos |
| **Calidad del Codigo** | Codigo limpio, bien estructurado, sigue mejores practicas | Codigo legible con pequenas areas de mejora | Codigo funcional pero dificil de leer | Codigo confuso, mal estructurado |
| **Solucion Propuesta** | Solucion elegante, eficiente, buen uso de POO | Solucion funcional con pequena area de mejora | Solucion basica que funciona | Solucion ineficiente o incorrecta |
| **Manejo de Errores** | Manejo apropiado de excepciones, validaciones completas | Manejo basico de errores | Manejo de errores parcial | Ausencia de manejo de errores |

---

## 4. Taller 2 - TDD y Testing con pytest

**Porcentaje del Curso:** 15%
**Fecha:** 19 de marzo de 2026
**Unidad:** U02 - Tecnica de Desarrollo

### Descripcion

Este taller se centra en el desarrollo de pruebas unitarias utilizando pytest y la metodologia TDD (Test-Driven Development). Los estudiantes deben demostrar capacidad para escribir tests que verifiquen el comportamiento del codigo, utilizando fixtures, parametrizacion, mocks y asserts apropiados.

### Rubrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Cobertura de Tests** (25%) | Cobertura superior al 90%, todos los paths probados | Cobertura entre 75-90% | Cobertura entre 50-75% | Cobertura inferior al 50% |
| **Fixtures** (20%) | Fixtures bien disenados con alcance apropiado, reutilizables | Fixtures funcionales con pequenos problemas | Fixtures basicos presentes | Ausencia de fixtures |
| **Parametrizacion** (20%) | Parametrizacion maxima de tests, datos de prueba diversos | Parametrizacion presente | Parametrizacion basica | Sin parametrizacion |
| **Mocks y Patching** (20%) | Uso correcto de mocks para aislar unidades | Mocks funcionales | Mocks basicos presentes | Ausencia de mocks |
| **TDD** (15%) | Aplicacion correcta del ciclo red-green-refactor | TDD aplicado con pequenas inconsistencias | Intento de aplicar TDD | No aplica TDD |

### Pesos de los Criterios

| Criterio | Peso |
|----------|------|
| Cobertura de Tests | 25% |
| Fixtures | 20% |
| Parametrizacion | 20% |
| Mocks y Patching | 20% |
| TDD | 15% |

---

## 5. Proyecto Parcial - TaskFlow API

**Porcentaje del Curso:** 15%
**Fecha:** 16 de abril de 2026
**Unidad:** U03 - FastAPI y Persistencia

### Descripcion

El Proyecto Parcial consiste en desarrollar una API REST funcional utilizando FastAPI. El sistema TaskFlow debe incluir gestion de usuarios, proyectos y tareas con persistencia en base de datos, autenticacion JWT y documentacion automatica.

### Requisitos Minimos

- API REST con endpoints CRUD para usuarios, proyectos y tareas
- Autenticacion y autorizacion con JWT
- Validacion de datos con Pydantic
- Persistencia con SQLAlchemy
- Tests de integracion
- Documentacion Swagger/OpenAPI

### Rubrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Funcionalidad API** (30%) | API completa, todos los endpoints funcionan correctamente | API funcional con pequenas limitaciones | API basica con funcionalidad parcial | API incompleta o no funcional |
| **Modelos Pydantic** (20%) | Modelos completos con validaciones personalizadas | Modelos funcionales | Modelos basicos | Modelos incorrectos |
| **Autenticacion JWT** (20%) | Implementacion correcta de JWT, manejo de tokens | Autenticacion funcional | Autenticacion basica | Sin autenticacion |
| **Persistencia** (15%) | Uso correcto de SQLAlchemy, relaciones bien definidas | Persistencia funcional | Persistencia basica | Sin persistencia |
| **Testing API** (15%) | Tests de integracion completos, cobertura alta | Tests funcionales | Tests basicos | Sin tests |

### Pesos de los Criterios

| Criterio | Peso |
|----------|------|
| Funcionalidad API | 30% |
| Modelos Pydantic | 20% |
| Autenticacion JWT | 20% |
| Persistencia | 15% |
| Testing API | 15% |

---

## 6. Proyecto Final - TaskFlow Completo

**Porcentaje del Curso:** 20%
**Fecha:** 07 de mayo de 2026
**Unidad:** U03 - FastAPI y Persistencia

### Descripcion

El Proyecto Final TaskFlow es un sistema de gestion de tareas y proyectos que integra todos los conceptos aprendidos durante el curso. Los estudiantes deben desarrollar una aplicacion completa utilizando arquitectura Domain-Driven Design (DDD), API REST con FastAPI, pruebas unitarias comprehensivas y documentacion profesional.

### Requisitos del Proyecto

El sistema TaskFlow debe incluir:
- Gestion de usuarios con autenticacion
- Creacion y administracion de proyectos
- Gestion de tareas con estados y prioridades
- Comentarios en tareas
- Arquitectura DDD con separation of concerns
- Cobertura de tests > 70%

### Rubrica de Evaluacion

| Criterio | Excelente (5.0) | Bueno (4.0) | Suficiente (3.0) | Insuficiente (1.0-2.9) |
|----------|-----------------|-------------|------------------|------------------------|
| **Funcionalidad** (30%) | Sistema completamente funcional, todas las caracteristicas implementadas | Sistema funcional con pequenas limitaciones | Sistema basico funcional | Sistema no funcional o con caracteristicas criticas faltantes |
| **Arquitectura DDD** (20%) | Arquitectura DDD completa, Entities, Value Objects, Repositories bien definidos | Arquitectura DDD funcional con pequenas inconsistencias | Arquitectura basica presente | Ausencia de arquitectura DDD |
| **API REST** (20%) | API REST completa y bien disenada, endpoints intuitivos | API funcional con pequenas inconsistencias | API basica presente | API mal disenada |
| **Testing** (15%) | Cobertura superior al 85%, tests unitarios e integracion | Buena cobertura (70-85%) | Tests basicos (50-70%) | Cobertura inferior al 50% |
| **Calidad del Codigo** (10%) | Codigo limpio, DRY, SRP, typing completo | Codigo legible con pequenas areas de mejora | Codigo funcional pero con code smells | Codigo dificil de mantener |
| **Documentacion** (5%) | Documentacion completa: README, API docs, guia de instalacion | Documentacion funcional | Documentacion basica | Documentacion minima |

### Pesos de los Criterios

| Criterio | Peso |
|----------|------|
| Funcionalidad | 30% |
| Arquitectura DDD | 20% |
| API REST | 20% |
| Testing | 15% |
| Calidad del Codigo | 10% |
| Documentacion | 5% |

### Requisitos Minimos para Aprobar

Para que el proyecto sea considerado para calificacion, debe cumplir con:
- Codigo que ejecute sin errores criticos
- API que responda a peticiones basicas
- Al menos 50% de coverage en pruebas unitarias

Proyectos que no cumplan estos requisitos seran calificados como Insuficientes (1.0-2.9).

---

## Politica de Entregas Tardias

### Aplicacion de Penalizaciones

Todas las entregas tienen una politica de penalizacion progresiva:

| Tiempo de Demora | Penalizacion |
|------------------|--------------|
| Hasta 24 horas | 10% de la nota |
| 24-48 horas | 20% de la nota |
| 48-72 horas | 30% de la nota |
| Mas de 72 horas | 50% de la nota o no aceptado |

### Entregas Tardias en Parciales

Los parciales tienen tolerancia de 15 minutos para el inicio. Despues de este tiempo, el estudiante debera justificar su ausencia para presentar en fecha alternativa.

---

## Escala de Calificacion Final

| Rango | Nota | Descriptor |
|-------|------|------------|
| 4.6 - 5.0 | Sobresaliente | Dominio completo de los objetivos, trabajo de alta calidad |
| 4.0 - 4.5 | Bueno | Cumplimiento satisfactorio de los objetivos |
| 3.0 - 3.9 | Aprobado | Cumplimiento minimo de los objetivos |
| 1.0 - 2.9 | No Aprobado | No cumplimiento de los objetivos |

### Requisitos para Aprobar el Curso

- Nota definitiva igual o superior a 3.0
- Haber presentado todas las evaluaciones
- Haber presentado ambos parciales

---

## Anexos

### Anexo A: Formato de Entrega

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

- [ ] Codigo en repositorio Git con commits descriptivos
- [ ] Todos los tests pasan correctamente (pytest)
- [ ] Coverage es el esperado segun la rubrica
- [ ] requirements.txt incluye todas las dependencias
- [ ] README.md tiene instrucciones claras
- [ ] No hay archivos de cache ni datos sensibles
- [ ] Documentacion completa y actualizada

### Anexo C: Recursos de Apoyo

- **Python**: Documentacion oficial, PEP 8, Fluent Python (Luciano Ramalho)
- **POO**: Design Patterns (Gang of Four)
- **pytest**: Python Testing with pytest (Brian Okken)
- **FastAPI**: Documentacion oficial de FastAPI
- **DDD**: Domain-Driven Design (Eric Evans)

---

## Informacion del Documento

| Campo | Valor |
|-------|-------|
| **Version** | 2.0 |
| **Autor** | [Nombre del Docente] |
| **Fecha de Creacion** | Febrero 2026 |
| **Ultima Revision** | 08 de febrero 2026 |
| **Aprobado por** | [Nombre del coordinador] |

---

*Este documento esta sujeto a modificaciones. Cualquier cambio sera comunicado con al menos dos semanas de anticipacion.*
