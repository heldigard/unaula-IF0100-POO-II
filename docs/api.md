# API Documentation - TaskFlow

**Version:** 1.0.0
**Base URL:** `http://localhost:8000`
**Documentation:** `/docs` (Swagger UI) or `/redoc` (ReDoc)

---

## Table of Contents

1. [Authentication](#authentication)
2. [Users](#users)
3. [Projects](#projects)
4. [Tasks](#tasks)
5. [Error Responses](#error-responses)
6. [Rate Limiting](#rate-limiting)

---

## Authentication

### Overview

TaskFlow uses JWT (JSON Web Token) based authentication. Most endpoints require a valid JWT token in the Authorization header.

```
Authorization: Bearer <token>
```

### Endpoints

#### Register User

Register a new user account.

**Endpoint:** `POST /api/auth/register`

**Request Body:**

```json
{
  "username": "jdoe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "nombre_completo": "John Doe"
}
```

**Response (201 Created):**

```json
{
  "id": 1,
  "username": "jdoe",
  "email": "john@example.com",
  "nombre_completo": "John Doe",
  "activo": true,
  "creado_en": "2026-02-07T10:30:00Z"
}
```

**Validation Errors (400 Bad Request):**

```json
{
  "detail": "Username ya existe"
}
```

#### Login

Authenticate and receive a JWT token.

**Endpoint:** `POST /api/auth/login`

**Request Body (form-data):**

```
username: jdoe
password: SecurePass123!
```

**Or (JSON):**

```json
{
  "username": "jdoe",
  "password": "SecurePass123!"
}
```

**Response (200 OK):**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### Get Current User

Get information about the authenticated user.

**Endpoint:** `GET /api/auth/me`

**Headers:**

```
Authorization: Bearer <token>
```

**Response (200 OK):**

```json
{
  "id": 1,
  "username": "jdoe",
  "email": "john@example.com",
  "nombre_completo": "John Doe",
  "activo": true
}
```

---

> **NOTA:** El endpoint `POST /api/auth/refresh` no está implementado actualmente.
> Para obtener un nuevo token, usa el endpoint `POST /api/auth/login`.

---

## Users

### List Users

Get a list of all users (requires authentication).

**Endpoint:** `GET /api/usuarios`

**Headers:**

```
Authorization: Bearer <token>
```

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| skip | int | 0 | Number of records to skip |
| limit | int | 100 | Maximum number of records to return |
| activo | bool | null | Filter by active status |

**Response (200 OK):**

```json
{
  "total": 4,
  "items": [
    {
      "id": 1,
      "username": "jdoe",
      "email": "john@example.com",
      "nombre_completo": "John Doe",
      "activo": true,
      "creado_en": "2026-02-07T10:30:00Z"
    }
  ]
}
```

### Get User by ID

Get a specific user by ID.

**Endpoint:** `GET /api/usuarios/{id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | User ID |

**Response (200 OK):**

```json
{
  "id": 1,
  "username": "jdoe",
  "email": "john@example.com",
  "nombre_completo": "John Doe",
  "activo": true,
  "creado_en": "2026-02-07T10:30:00Z",
  "actualizado_en": "2026-02-07T10:30:00Z"
}
```

**Error (404 Not Found):**

```json
{
  "detail": "Usuario no encontrado"
}
```

### Update User

Update user information.

**Endpoint:** `PATCH /api/usuarios/{id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | User ID |

**Request Body:**

```json
{
  "nombre_completo": "John Updated Doe",
  "email": "john.updated@example.com"
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "username": "jdoe",
  "email": "john.updated@example.com",
  "nombre_completo": "John Updated Doe",
  "activo": true,
  "actualizado_en": "2026-02-07T12:00:00Z"
}
```

### Delete User

Delete (soft delete) a user account.

**Endpoint:** `DELETE /api/usuarios/{id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | User ID |

**Response (204 No Content):**

```
(no content)
```

---

## Projects

### List Projects

Get a list of all projects.

**Endpoint:** `GET /api/proyectos`

**Headers:**

```
Authorization: Bearer <token>
```

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| skip | int | 0 | Number of records to skip |
| limit | int | 100 | Maximum number of records to return |
| estado | str | null | Filter by state (activo, archivado, completado) |
| usuario_id | int | null | Filter by owner user ID |

**Response (200 OK):**

```json
{
  "total": 3,
  "items": [
    {
      "id": 1,
      "nombre": "TaskFlow",
      "descripcion": "Sistema de gestion de tareas",
      "usuario_id": 1,
      "estado": "activo",
      "creado_en": "2026-02-07T10:30:00Z",
      "actualizado_en": "2026-02-07T10:30:00Z"
    }
  ]
}
```

### Create Project

Create a new project.

**Endpoint:** `POST /api/proyectos`

**Headers:**

```
Authorization: Bearer <token>
```

**Request Body:**

```json
{
  "nombre": "Nuevo Proyecto",
  "descripcion": "Descripcion del proyecto"
}
```

**Response (201 Created):**

```json
{
  "id": 2,
  "nombre": "Nuevo Proyecto",
  "descripcion": "Descripcion del proyecto",
  "usuario_id": 1,
  "estado": "activo",
  "creado_en": "2026-02-07T12:00:00Z",
  "actualizado_en": "2026-02-07T12:00:00Z"
}
```

### Get Project by ID

Get a specific project by ID.

**Endpoint:** `GET /api/proyectos/{id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | Project ID |

**Response (200 OK):**

```json
{
  "id": 1,
  "nombre": "TaskFlow",
  "descripcion": "Sistema de gestion de tareas",
  "usuario_id": 1,
  "estado": "activo",
  "creado_en": "2026-02-07T10:30:00Z",
  "actualizado_en": "2026-02-07T10:30:00Z"
}
```

### Update Project

Update project information.

**Endpoint:** `PATCH /api/proyectos/{id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | Project ID |

**Request Body:**

```json
{
  "nombre": "Proyecto Actualizado",
  "descripcion": "Nueva descripcion",
  "estado": "completado"
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "nombre": "Proyecto Actualizado",
  "descripcion": "Nueva descripcion",
  "estado": "completado",
  "actualizado_en": "2026-02-07T14:00:00Z"
}
```

### Delete Project

Delete a project and all its tasks (cascade delete).

**Endpoint:** `DELETE /api/proyectos/{id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | Project ID |

**Response (204 No Content):**

```
(no content)
```

### Get Project Tasks

Get all tasks for a specific project.

**Endpoint:** `GET /api/proyectos/{id}/tareas`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | Project ID |

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| estado | str | null | Filter by task state |
| prioridad | str | null | Filter by priority |

**Response (200 OK):**

```json
{
  "proyecto_id": 1,
  "proyecto_nombre": "TaskFlow",
  "total": 5,
  "items": [
    {
      "id": 1,
      "titulo": "Configurar proyecto",
      "estado": "completada",
      "prioridad": "alta",
      "asignado_a": 1,
      "creada_en": "2026-02-07T10:30:00Z"
    }
  ]
}
```

---

## Tasks

### List Tasks

Get a list of all tasks with optional filtering.

**Endpoint:** `GET /api/tareas`

**Headers:**

```
Authorization: Bearer <token>
```

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| skip | int | 0 | Number of records to skip |
| limit | int | 100 | Maximum number of records to return |
| proyecto_id | int | null | Filter by project ID |
| estado | str | null | Filter by state (pendiente, en_progreso, completada, cancelada) |
| prioridad | str | null | Filter by priority (baja, media, alta, urgente) |
| asignado_a | int | null | Filter by assigned user ID |
| creada_por | int | null | Filter by creator user ID |

**Response (200 OK):**

```json
{
  "total": 10,
  "items": [
    {
      "id": 1,
      "titulo": "Configurar proyecto",
      "descripcion": "Crear estructura de carpetas y virtualenv",
      "estado": "completada",
      "prioridad": "alta",
      "proyecto_id": 1,
      "proyecto_nombre": "TaskFlow",
      "asignado_a": 1,
      "asignado_a_username": "jdoe",
      "creada_por": 1,
      "creada_por_username": "admin",
      "fecha_limite": "2026-02-10",
      "completada_en": "2026-02-07T15:00:00Z",
      "creada_en": "2026-02-07T10:00:00Z",
      "actualizada_en": "2026-02-07T15:00:00Z"
    }
  ]
}
```

### Create Task

Create a new task.

**Endpoint:** `POST /api/tareas`

**Headers:**

```
Authorization: Bearer <token>
```

**Request Body:**

```json
{
  "titulo": "Nueva tarea",
  "descripcion": "Descripcion de la tarea",
  "proyecto_id": 1,
  "prioridad": "media",
  "fecha_limite": "2026-03-01"
}
```

**Response (201 Created):**

```json
{
  "id": 6,
  "titulo": "Nueva tarea",
  "descripcion": "Descripcion de la tarea",
  "estado": "pendiente",
  "prioridad": "media",
  "proyecto_id": 1,
  "asignado_a": null,
  "creada_por": 1,
  "fecha_limite": "2026-03-01",
  "completada_en": null,
  "creada_en": "2026-02-07T16:00:00Z",
  "actualizada_en": "2026-02-07T16:00:00Z"
}
```

### Get Task by ID

Get a specific task by ID.

**Endpoint:** `GET /api/tareas/{id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | Task ID |

**Response (200 OK):**

```json
{
  "id": 1,
  "titulo": "Configurar proyecto",
  "descripcion": "Crear estructura de carpetas y virtualenv",
  "estado": "completada",
  "prioridad": "alta",
  "proyecto_id": 1,
  "proyecto_nombre": "TaskFlow",
  "asignado_a": 1,
  "asignado_a_username": "jdoe",
  "asignado_a_nombre": "John Doe",
  "creada_por": 1,
  "creada_por_username": "admin",
  "creada_por_nombre": "Administrador",
  "fecha_limite": "2026-02-10",
  "completada_en": "2026-02-07T15:00:00Z",
  "creada_en": "2026-02-07T10:00:00Z",
  "actualizada_en": "2026-02-07T15:00:00Z"
}
```

### Update Task

Update task information.

**Endpoint:** `PATCH /api/tareas/{id}`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | Task ID |

**Request Body:**

```json
{
  "titulo": "Titulo actualizado",
  "descripcion": "Nueva descripcion",
  "prioridad": "alta",
  "asignado_a": 2,
  "fecha_limite": "2026-03-15"
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "titulo": "Titulo actualizado",
  "descripcion": "Nueva descripcion",
  "prioridad": "alta",
  "asignado_a": 2,
  "fecha_limite": "2026-03-15",
  "actualizada_en": "2026-02-07T17:00:00Z"
}
```

### Complete Task

Marks a task as completed.

**Endpoint:** `POST /api/tareas/{id}/completar`

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| id | int | Task ID |

**Response (200 OK):**

```json
{
  "id": 1,
  "titulo": "Configurar proyecto",
  "descripcion": "Crear estructura de carpetas y virtualenv",
  "estado": "completada",
  "prioridad": "alta",
  "proyecto_id": 1,
  "asignado_a": 1,
  "creada_por": 1,
  "fecha_limite": "2026-02-10",
  "completada_en": "2026-02-07T17:30:00Z",
  "creada_en": "2026-02-07T10:00:00Z",
  "actualizada_en": "2026-02-07T17:30:00Z"
}
```

> **NOTA:** Los endpoints de comentarios (`GET /api/tareas/{id}/comentarios`, `POST /api/tareas/{id}/comentarios`, `GET /api/comentarios/{id}`, `PUT /api/comentarios/{id}`, `DELETE /api/comentarios/{id}`) NO están implementados actualmente.

---

---

## Error Responses

### Error Response Format

All errors follow this format:

```json
{
  "detail": "Error message description"
}
```

### Common HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 204 | No Content - Request successful, no content returned |
| 400 | Bad Request - Invalid request data |
| 401 | Unauthorized - Authentication required or failed |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource not found |
| 422 | Unprocessable Entity - Validation error |
| 500 | Internal Server Error - Server error |

### Error Examples

**400 Bad Request:**

```json
{
  "detail": "Username debe tener al menos 3 caracteres"
}
```

**401 Unauthorized:**

```json
{
  "detail": "Credenciales invalidas"
}
```

**404 Not Found:**

```json
{
  "detail": "Usuario no encontrado"
}
```

**422 Validation Error:**

```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

**500 Internal Server Error:**

```json
{
  "detail": "Error interno del servidor"
}
```

---

## Rate Limiting

Currently, the API does not enforce rate limiting. This may be added in future versions.

---

## Examples Using curl

### Register and Login

```bash
# Register a new user
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123!",
    "nombre_completo": "Test User"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=TestPass123!"

# Save the token for subsequent requests
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### Create a Project

```bash
curl -X POST http://localhost:8000/api/proyectos \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "My Project",
    "descripcion": "A test project"
  }'
```

### Create a Task

```bash
curl -X POST http://localhost:8000/api/tareas \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "My First Task",
    "descripcion": "Task description",
    "proyecto_id": 1,
    "prioridad": "alta"
  }'
```

### List Tasks

```bash
# List all tasks
curl -X GET http://localhost:8000/api/tareas \
  -H "Authorization: Bearer $TOKEN"

# Filter by state
curl -X GET "http://localhost:8000/api/tareas?estado=pendiente" \
  -H "Authorization: Bearer $TOKEN"

# Filter by priority
curl -X GET "http://localhost:8000/api/tareas?prioridad=urgente" \
  -H "Authorization: Bearer $TOKEN"
```

### Complete Task

```bash
curl -X POST http://localhost:8000/api/tareas/1/completar \
  -H "Authorization: Bearer $TOKEN"
```

---

## Examples Using Python (requests)

```python
import requests

BASE_URL = "http://localhost:8000"

# Register
response = requests.post(f"{BASE_URL}/api/auth/register", json={
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123!",
    "nombre_completo": "Test User"
})
user = response.json()
print(f"User created: {user}")

# Login
response = requests.post(f"{BASE_URL}/api/auth/login", data={
    "username": "testuser",
    "password": "TestPass123!"
})
token_data = response.json()
token = token_data["access_token"]

# Set up headers
headers = {"Authorization": f"Bearer {token}"}

# Create project
response = requests.post(
    f"{BASE_URL}/api/proyectos",
    headers=headers,
    json={
        "nombre": "My Project",
        "descripcion": "Test project"
    }
)
project = response.json()
print(f"Project created: {project}")

# Create task
response = requests.post(
    f"{BASE_URL}/api/tareas",
    headers=headers,
    json={
        "titulo": "My Task",
        "proyecto_id": project["id"],
        "prioridad": "media"
    }
)
task = response.json()
print(f"Task created: {task}")

# List tasks
response = requests.get(
    f"{BASE_URL}/api/tareas",
    headers=headers
)
tasks = response.json()
print(f"Tasks: {tasks}")
```

---

## Interactive Documentation

FastAPI provides interactive API documentation:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

These interfaces allow you to:

- Browse all available endpoints
- See request/response schemas
- Test endpoints directly from the browser
- Download OpenAPI specification

---

## OpenAPI Specification

The complete OpenAPI 3.0 specification is available at:

```
http://localhost:8000/openapi.json
```

---

**UNAULA - IF0100 - POO II - 2026-I**
