# Sprint 2: API Backend con FastAPI

## Informacion del Sprint

| Campo | Valor |
|-------|-------|
| Sprint | 2 |
| Duracion | 1 semana |
| Objetivo | Crear API REST completa con FastAPI |
| Peso en el Proyecto | 15% de la calificacion final |

Este sprint se enfoca en la construccion de una API RESTful robusta utilizando FastAPI como framework principal. Durante esta semana, los estudiantes implementaran todos los endpoints necesarios para operaciones CRUD (Create, Read, Update, Delete) sobre las tres entidades principales del sistema: Usuarios, Tareas y Proyectos. La API sera documentada automaticamente mediante Swagger/OpenAPI, permitiendo una interaccion visual con los endpoints y facilitando las pruebas durante el desarrollo.

## Entregables

### 1. Endpoints CRUD para User

El modulo de usuarios debe permitir la gestion completa de cuentas de usuario dentro del sistema. Esto incluye la capacidad de registrar nuevos usuarios, consultar la lista completa de usuarios registrados, buscar un usuario especifico por su identificador unico, actualizar la informacion de perfil y eliminar cuentas cuando sea necesario. Cada endpoint debe responder con los codigos de estado HTTP apropiados y manejar casos de error como usuarios no encontrados o datos invalidos.

### 2. Endpoints CRUD para Task

Las tareas representan las unidades de trabajo dentro de cada proyecto. Los endpoints de tareas deben soportar la creacion de nuevas tareas asociadas a proyectos especificos, la consulta de tareas individuales o filtradas por diferentes criterios, la actualizacion de estados, asignaciones y detalles de tareas, y la eliminacion de tareas completadas o canceladas. La estructura de datos debe incluir campos como titulo, descripcion, estado, prioridad, fecha de vencimiento y referencia al proyecto padre.

### 3. Endpoints CRUD para Project

Los proyectos actuan como contenedores logicos que agrupan tareas relacionadas. El API de proyectos debe permitir crear nuevos proyectos con su metadata correspondiente, listar todos los proyectos con soporte para paginacion, obtener detalles de un proyecto especifico incluyendo sus tareas asociadas, actualizar la informacion del proyecto y eliminar proyectos (con consideracion de integridad referencial con las tareas).

### 4. Documentacion Swagger/OpenAPI

FastAPI genera automaticamente documentacion interactiva gracias a su integracion nativa con OpenAPI. La documentacion debe ser accesible a traves de dos interfaces: Swagger UI en la ruta `/docs` y ReDoc en la ruta `/redoc`. Ambas interfaces deben mostrar todos los endpoints disponibles, los parametros requeridos y opcionales, los esquemas de peticion y respuesta, y los posibles codigos de error.

### 5. Validacion Pydantic

Todos los modelos de datos deben utilizar Pydantic para la validacion automatica deEntradas. Esto incluye validacion de tipos de datos, campos requeridos, longitudes maximas, formatos especiales (como emails y fechas) y restricciones personalizadas de negocio. Los errores de validacion deben retornar mensajes claros que indiquen exactamente que campo tiene problemas y cual es la restriccion violada.

## Criterios de Aceptacion

- [ ] **Endpoints GET para listar recursos**: Todos los modelos (User, Task, Project) deben tener un endpoint para obtener la coleccion completa de recursos. La respuesta debe incluir un array de objetos serializados apropiadamente.

- [ ] **Endpoints GET para obtener por ID**: Cada recurso debe ser recuperable individualmente mediante su identificador unico. El endpoint debe retornar 404 cuando el recurso no existe con un mensaje claro.

- [ ] **Endpoints POST para crear recursos**: La creacion de nuevos recursos debe validar todos los campos requeridos, aplicar valores por defecto cuando corresponda, y retornar el recurso creado con codigo 201 Created.

- [ ] **Endpoints PUT/PATCH para actualizar**: Se deben implementar dos estrategias de actualizacion: PUT para reemplazo completo del recurso y PATCH para actualizacion parcial de campos específicos.

- [ ] **Endpoints DELETE para eliminar**: La eliminacion de recursos debe retornar 204 No Content en caso de exito o 404 si el recurso no existe. Considerar si la eliminacion debe ser fisica o logica (soft delete).

- [ ] **Validacion Pydantic en todos los modelos**: Cada modelo de peticion y respuesta debe definir validaciones explicitas para todos los campos, incluyendo mensajes de error personalizados cuando sea necesario.

- [ ] **Documentacion Swagger accesible**: La ruta `/docs` debe mostrar una interfaz interactiva funcional con todos los endpoints documentados y probables.

- [ ] **Status codes correctos**: Implementar uso apropiado de codigos HTTP: 200 para operaciones exitosas, 201 para recursos creados, 204 para eliminaciones exitosas, 400 para bad requests, 404 para recursos no encontrados, 422 para errores de validacion.

## Requisitos Tecnicos

### Framework y Librerias

| Tecnologia | Version Minima | Proposito |
|------------|----------------|-----------|
| FastAPI | 0.100.0 | Framework web asincrono |
| Pydantic | 2.0.0 | Validacion de datos y serializacion |
| Uvicorn | 0.23.0 | Servidor ASGI para produccion |
| Python | 3.9 | Runtime requerido |

### Routing con Path y Query Parameters

FastAPI soporta multiple tipos de parametros que deben utilizarse apropiadamente segun el contexto. Los **path parameters** se utilizan para identificar un recurso especifico dentro de la URL, como el identificador de un usuario (`/users/{user_id}`). Los **query parameters** se utilizan para filtros, paginacion y opciones opcionales (`/tasks?status=pending&priority=high`). Los **request body parameters** se utilizan para enviar datos en operaciones POST y PUT, validandolos automaticamente contra modelos Pydantic.

### HTTP Status Codes Apropiados

| Codigo | Significado | Uso en la API |
|--------|-------------|---------------|
| 200 | OK | Respuestas exitosas en GET y PUT |
| 201 | Created | Respuesta exitosa a POST |
| 204 | No Content | Respuesta exitosa a DELETE |
| 400 | Bad Request | Datos de peticion invalidos |
| 404 | Not Found | Recurso solicitado no existe |
| 422 | Unprocessable Entity | Error de validacion de datos |

## Guia de Implementacion

### Paso 1: Configurar FastAPI App

El primer paso consiste en inicializar la aplicacion FastAPI con la configuracion basica necesaria. Esto incluye definir el titulo de la API, la version inicial, y la configuracion de documentos OpenAPI. La aplicacion debe estar lista para ejecutar con Uvicorn en un servidor de desarrollo y poder reiniciarse automaticamente cuando se detectan cambios en el codigo (debug mode).

```python
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="TaskFlow API",
    description="API RESTful para gestion de tareas y proyectos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```

### Paso 2: Crear Modelos Pydantic

Los modelos Pydantic se dividen en dos categorias principales: modelos de peticion (Request Models) que definen la estructura esperada para crear o actualizar recursos, y modelos de respuesta (Response Models) que definen la estructura de los datos retornados al cliente. Los modelos deben incluir validaciones apropiadas como campos requeridos, maximos y minimos para strings, y formatos especificos para emails y fechas.

```python
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List

# Modelos base
class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=100)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    priority: int = Field(default=1, ge=1, le=5)

class TaskCreate(TaskBase):
    project_id: int

class TaskResponse(TaskBase):
    id: int
    status: str
    user_id: Optional[int]
    created_at: datetime
    due_date: Optional[datetime]

    class Config:
        from_attributes = True
```

### Paso 3: Implementar Rutas User

Las rutas de usuario deben seguir un patron REST consistente a lo largo de toda la API. Para operaciones de lectura, se implementan dos endpoints: uno para listar todos los usuarios con soporte opcional para paginacion y filtros, y otro para obtener un usuario especifico por su identificador. Las operaciones de escritura incluyen creacion de nuevos usuarios con validacion de email unico, actualizacion parcial de campos, y eliminacion logica o fisica del registro.

```python
from fastapi import APIRouter, HTTPException, status

users_router = APIRouter(prefix="/users", tags=["Users"])

# Almacenamiento en memoria (temporal)
users_db = {}
user_id_counter = 1

@users_router.get("", response_model=List[UserResponse])
async def list_users(skip: int = 0, limit: int = 100):
    """Lista todos los usuarios con paginacion"""
    users = list(users_db.values())
    return users[skip : skip + limit]

@users_router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """Obtiene un usuario por su ID"""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {user_id} no encontrado"
        )
    return users_db[user_id]

@users_router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Crea un nuevo usuario"""
    global user_id_counter

    # Verificar email unico
    for existing_user in users_db.values():
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya esta registrado"
            )

    user_id = user_id_counter
    user_id_counter += 1

    new_user = UserResponse(
        id=user_id,
        email=user.email,
        full_name=user.full_name,
        created_at=datetime.now(),
        is_active=True
    )

    users_db[user_id] = new_user
    return new_user

@users_router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserCreate):
    """Actualiza un usuario existente"""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {user_id} no encontrado"
        )

    users_db[user_id].email = user_update.email
    users_db[user_id].full_name = user_update.full_name

    return users_db[user_id]

@users_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """Elimina un usuario"""
    if user_id not in users_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {user_id} no encontrado"
        )
    del users_db[user_id]
```

### Paso 4: Implementar Rutas Task

Las rutas de tareas siguen una estructura similar a las de usuarios pero加入了 conceptos adicionales como la asociacion con proyectos y usuarios asignados. La implementacion debe manejar casos especiales como la consulta de tareas por proyecto, tareas asignadas a un usuario especifico, y filtrado por estado y prioridad. Los endpoints deben validar que el proyecto referenciado exista antes de crear una tarea.

```python
tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks_db = {}
task_id_counter = 1

@tasks_router.get("", response_model=List[TaskResponse])
async def list_tasks(
    project_id: Optional[int] = None,
    user_id: Optional[int] = None,
    status: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
):
    """Lista tareas con filtros opcionales"""
    tasks = list(tasks_db.values())

    if project_id:
        tasks = [t for t in tasks if t.project_id == project_id]
    if user_id:
        tasks = [t for t in tasks if t.user_id == user_id]
    if status:
        tasks = [t for t in tasks if t.status == status]

    return tasks[skip : skip + limit]

@tasks_router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    """Obtiene una tarea por su ID"""
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con ID {task_id} no encontrada"
        )
    return tasks_db[task_id]

@tasks_router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskCreate):
    """Crea una nueva tarea"""
    global task_id_counter

    task_id = task_id_counter
    task_id_counter += 1

    new_task = TaskResponse(
        id=task_id,
        title=task.title,
        description=task.description,
        priority=task.priority,
        project_id=task.project_id,
        status="pending",
        user_id=None,
        created_at=datetime.now(),
        due_date=None
    )

    tasks_db[task_id] = new_task
    return new_task

@tasks_router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Actualiza parcialmente una tarea"""
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con ID {task_id} no encontrada"
        )

    task_data = task_update.model_dump(exclude_unset=True)
    for field, value in task_data.items():
        setattr(tasks_db[task_id], field, value)

    return tasks_db[task_id]

@tasks_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    """Elimina una tarea"""
    if task_id not in tasks_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarea con ID {task_id} no encontrada"
        )
    del tasks_db[task_id]
```

### Paso 5: Implementar Rutas Project

Los proyectos son las entidades de nivel superior en la jerarquia del sistema. Cada proyecto puede contener multiples tareas, y opcionalmente puede tener un usuario responsable asignado. Los endpoints de proyectos deben permitir no solo la gestion del proyecto sino tambi�n operaciones como listar las tareas asociadas a un proyecto especifico, lo cual requiere JOIN logicos o consultas filtradas sobre la coleccion de tareas.

```python
projects_router = APIRouter(prefix="/projects", tags=["Projects"])

projects_db = {}
project_id_counter = 1

@projects_router.get("", response_model=List[ProjectResponse])
async def list_projects(skip: int = 0, limit: int = 100):
    """Lista todos los proyectos"""
    projects = list(projects_db.values())
    return projects[skip : skip + limit]

@projects_router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: int):
    """Obtiene un proyecto por su ID"""
    if project_id not in projects_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proyecto con ID {project_id} no encontrado"
        )
    return projects_db[project_id]

@projects_router.get("/{project_id}/tasks", response_model=List[TaskResponse])
async def get_project_tasks(project_id: int):
    """Obtiene todas las tareas de un proyecto"""
    if project_id not in projects_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proyecto con ID {project_id} no encontrado"
        )

    project_tasks = [t for t in tasks_db.values() if t.project_id == project_id]
    return project_tasks

@projects_router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate):
    """Crea un nuevo proyecto"""
    global project_id_counter

    project_id = project_id_counter
    project_id_counter += 1

    new_project = ProjectResponse(
        id=project_id,
        name=project.name,
        description=project.description,
        owner_id=project.owner_id,
        created_at=datetime.now(),
        status="active"
    )

    projects_db[project_id] = new_project
    return new_project

@projects_router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(project_id: int, project_update: ProjectUpdate):
    """Actualiza un proyecto existente"""
    if project_id not in projects_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proyecto con ID {project_id} no encontrado"
        )

    project_data = project_update.model_dump(exclude_unset=True)
    for field, value in project_data.items():
        setattr(projects_db[project_id], field, value)

    return projects_db[project_id]

@projects_router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int):
    """Elimina un proyecto y sus tareas asociadas"""
    if project_id not in projects_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proyecto con ID {project_id} no encontrado"
        )

    # Eliminar tareas asociadas
    tasks_to_delete = [t.id for t in tasks_db.values() if t.project_id == project_id]
    for task_id in tasks_to_delete:
        del tasks_db[task_id]

    del projects_db[project_id]
```

### Paso 6: Probar en Navegador

Una vez implementados todos los endpoints, la API debe probarse exhaustivamente utilizando la interfaz Swagger UI disponible en `/docs`. Esta interfaz permite ejecutar requests directamente desde el navegador sin necesidad de herramientas externas como Postman. Se recomienda probar cada endpoint con casos de exito y con casos de error para validar tanto el funcionamiento correcto como el manejo apropiado de excepciones.

**Rutas de acceso:**

| Ruta | Descripcion |
|------|-------------|
| `http://localhost:8000/docs` | Swagger UI - Interfaz interactiva |
| `http://localhost:8000/redoc` | ReDoc - Documentacion alternativa |
| `http://localhost:8000/openapi.json` | Especificacion OpenAPI en JSON |
| `http://localhost:8000/` | Pagina de inicio de la API |

**Flujo de prueba recomendado:**

1. Crear un usuario mediante POST a `/users`
2. Verificar la creacion con GET a `/users/{id}`
3. Listar usuarios con GET a `/users`
4. Crear un proyecto mediante POST a `/projects`
5. Crear una tarea asociada al proyecto con POST a `/tasks`
6. Actualizar el estado de la tarea con PATCH a `/tasks/{id}`
7. Ver las tareas del proyecto con GET a `/projects/{id}/tasks`
8. Eliminar recursos para validar DELETE

## Conexion con Clases del Curso

Este sprint integra directamente los conceptos vistos en las tres ultimas clases de la Unidad 03 del curso de Programacion Orientada a Objetos II, estableciendo la conexion entre la teoria de desarrollo web y la implementacion practica de APIs modernas con Python.

### Unidad 03 - FastAPI Intro (Clase 01)

La primera clase sobre FastAPI establecio los fundamentos del framework, incluyendo la creacion de instancias de aplicacion, el sistema de routing mediante decoradores, y el concepto de operaciones asincronas con `async` y `await`. Durante este sprint, estos conceptos se aplican directamente en la creacion de la estructura de la API, donde cada endpoint se define como una funcion asincrona decorada con el metodo HTTP correspondiente (`@app.get()`, `@app.post()`, etc.). La comprension de como FastAPI maneja las solicitudes HTTP y genera respuestas automaticamente es crucial para implementar endpoints funcionales y eficientes.

### Unidad 03 - Pydantic y Validacion (Clase 02)

La segunda clase se enfoco en Pydantic como sistema de validacion de datos y serializacion. Los estudiantes aprendieron a definir modelos que automaticamente validan los datos de entrada, convierten tipos cuando es posible, y generan mensajes de error claros cuando la validacion falla. En este sprint, cada modelo Pydantic (`UserCreate`, `TaskResponse`, `ProjectUpdate`) representa la aplicacion practica de estos conceptos, donde las validaciones como `Field(..., min_length=3)` o `EmailStr` garantizan la integridad de los datos desde el momento en que son recibidos por la API.

### Unidad 03 - Dependencias (Clase 03)

La tercera clase cubrio el sistema de dependencias de FastAPI, que permite inyectar funcionalidad comun a multiples endpoints de manera reutilizable. Aunque la implementacion basica de este sprint puede no utilizar dependencias avanzadas, el concepto se aplica implicitamente en la estructura del codigo donde logica compartida (como validacion de existencia de recursos o verificacion de permisos) puede factorizarse en funciones reutilizables. Para implementaciones mas avanzadas, se podrian usar `Depends()` para autenticacion, verificacion de tokens, y gestion de sesiones de usuario.

## Recursos

### Documentacion Oficial

| Recurso | URL | Descripcion |
|---------|-----|-------------|
| FastAPI Tutorial | https://fastapi.tiangolo.com/tutorial/ | Guia oficial paso a paso |
| Pydantic Docs | https://docs.pydantic.dev/ | Referencia completa de validacion |
| OpenAPI Specification | https://spec.openapis.org/oas/v3.1.0 | Estandar de documentacion API |
| Uvicorn Server | https://www.uvicorn.org/ | Servidor ASGI de produccion |

### Recursos de Aprendizaje

| Recurso | URL | Descripcion |
|---------|-----|-------------|
| FastAPI from Scratch | https://fastapi.tiangolo.com/tutorial/first-steps/ | Primeros pasos con FastAPI |
| Path Parameters | https://fastapi.tiangolo.com/tutorial/path-params/ | Parametros en la URL |
| Query Parameters | https://fastapi.tiangolo.com/tutorial/query-params/ | Filtros y opciones |
| Request Body | https://fastapi.tiangolo.com/tutorial/body/ | Datos en peticion |
| Validation Errors | https://fastapi.tiangolo.com/tutorial/handling-errors/ | Manejo de errores |

### Herramientas de Testing

| Herramienta | Proposito |
|------------|-----------|
| Swagger UI | Testing visual desde el navegador |
| HTTPie | Cliente HTTP desde linea de comandos |
| Postman | Testing completo de APIs |
| curl | Requests HTTP basicos |

## Evaluacion

### Rubrica de Calificacion

| Criterio | Peso | Descripcion |
|----------|------|-------------|
| **Endpoints Funcionales** | 40% | Todos los endpoints CRUD funcionan correctamente, responden con datos precisos y manejan casos de borde apropiadamente |
| **Validacion Correcta** | 25% | Los modelos Pydantic validan correctamente todos los campos, mostrando mensajes de error claros y precisos |
| **Documentacion** | 20% | La documentacion Swagger/OpenAPI es completa, precisa y accesible, con descripciones claras de cada endpoint |
| **Calidad del Codigo** | 15% | El codigo sigue buenas practicas de programacion, esta bien estructurado, es legible y esta documentado apropiadamente |

### Puntos Adicionales (Opcional)

| Mejora | Puntos Extra | Descripcion |
|--------|--------------|-------------|
| Autenticacion JWT | +5% | Implementar login y proteccion de endpoints |
| Paginacion Completa | +3% | Soporte para next/previous en listados |
| Rate Limiting | +2% | Proteccion contra abuso de la API |
| Tests Unitarios | +5% | Cobertura minima del 70% |

### Penalizaciones

| Problema | Penalizacion | Descripcion |
|----------|--------------|-------------|
| Endpoints no funcionales | -10% por endpoint | Endpoint que falla en ejecucion basica |
| Codigo no的可读性 | -5% | Codigo sin formato o estructura clara |
| Sin documentacion | -10% | Endpoints sin descripcion o ejemplos |
| Manejo de errores inadecuado | -5% | Errores que causan caidas o mensajes confusos |

---

**Nota importante:** Este sprint establece la base para el Sprint 3 donde se implementara la persistencia de datos con SQLite. Asegurese de que la estructura de la API este bien diseñada ya que sera reutilizada y extendida en las siguientes iteraciones del proyecto.
