# Fix 4: Implementación de Rutas Frontend

**Fecha:** 2026-02-07
**Fase:** 10 de 10 - Integración Final y Fixes
**Estado:** COMPLETADO

---

## Problema Identificado

Los templates Jinja2/HTMX existían en `src/taskflow/templates/` pero faltaban las rutas en FastAPI para renderizarlos como HTML. La aplicación solo tenía endpoints API JSON (`/api/*`) sin forma de servir las páginas frontend.

### Síntomas
- Navegar a `/`, `/login`, `/dashboard` retornaba error 404
- Los templates no podían ser accedidos vía HTTP
- No había separación entre API JSON y frontend HTML

---

## Solución Implementada

### 1. Creación de `src/taskflow/api/routes/frontend.py`

Nuevo archivo que contiene todas las rutas frontend con separación clara:

**Rutas Públicas** (sin autenticación):
```
GET  /                  -> index.html (home)
GET  /login             -> login.html
GET  /registro          -> usuarios/registro.html
GET  /logout            -> Redirección a /login (elimina cookie)
```

**Rutas Privadas** (requieren autenticación):
```
GET  /dashboard         -> dashboard.html
GET  /proyectos         -> proyectos/lista.html
GET  /proyectos/nuevo   -> proyectos/form.html (crear)
GET  /proyectos/{id}    -> proyectos/detalle.html
GET  /proyectos/{id}/editar -> proyectos/form.html (editar)
GET  /tareas            -> tareas/lista.html
GET  /tareas/nueva      -> tareas/form.html (crear)
GET  /tareas/{id}       -> tareas/detalle.html
GET  /tareas/{id}/editar -> tareas/form.html (editar)
GET  /perfil            -> usuarios/perfil.html
```

### 2. Actualización de `src/taskflow/api/app.py`

```python
# Antes: Solo routers API JSON
app.include_router(auth.router, prefix="/api/auth", tags=["Autenticación"])
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(proyectos.router, prefix="/api/proyectos", tags=["Proyectos"])
app.include_router(tareas.router, prefix="/api/tareas", tags=["Tareas"])

# Después: Se agrega router Frontend HTML
app.include_router(frontend.router, tags=["Frontend"])

# Endpoint raíz movido a /api para evitar conflicto
@app.get("/api", tags=["API"])
def api_root():
    return {"nombre": settings.APP_NAME, "version": settings.APP_VERSION, "docs": "/docs"}
```

### 3. Actualización de `src/taskflow/api/routes/__init__.py`

```python
# Exportar router frontend
from .frontend import router as frontend_router

__all__ = [
    "auth_router",
    "usuarios_router",
    "proyectos_router",
    "tareas_router",
    "frontend_router",  # Nuevo
]
```

---

## Características Técnicas

### Manejo de Autenticación

Las rutas privadas usan la dependencia `get_current_active_user`:
```python
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    current_user: Usuario = Depends(get_current_active_user),
):
```

Las rutas públicas no requieren autenticación pero pueden mostrar datos del usuario si existe:
```python
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    current_user = _get_user_from_cookie(request)
    return templates.TemplateResponse("index.html", {...})
```

### Función Auxiliar `_get_user_from_cookie()`

Permite obtener el usuario desde la cookie de autenticación sin requerir token JWT en el header Authorization. Esto es necesario para:

1. Mostrar el nombre del usuario en la navegación
2. Mostrar contenido personalizado en páginas públicas
3. Redirigir automáticamente si ya está autenticado

### Configuración de Jinja2Templates

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/taskflow/templates")
```

El directorio de templates es relativo a la raíz del proyecto.

### Inyección de Contexto en Templates

Cada ruta inyecta variables necesarias en el template:
```python
{
    "request": request,           # Requerido por Jinja2Templates
    "current_user": current_user, # Usuario autenticado (opcional)
    "stats": stats,               # Datos específicos del endpoint
    "proyecto": proyecto,         # Entidad específica
    # ... otras variables
}
```

---

## Separación API vs Frontend

### API JSON (`/api/*`)
- Return types: Pydantic models, dict, list
- Content-Type: `application/json`
- Authentication: Bearer token en header Authorization
- Used by: HTMX, fetch(), clientes API

### Frontend HTML (`/`, `/proyectos`, etc.)
- Return types: `HTMLResponse`
- Content-Type: `text/html`
- Authentication: Cookie access_token
- Used by: Navegador del usuario

---

## Compatibilidad con Templates Existentes

Los templates creados anteriormente ya usaban las variables correctas:
- `{{ current_user }}` - Usuario autenticado
- `{{ stats }}` - Estadísticas del dashboard
- `{{ proyecto }}` - Proyecto actual
- `{{ tarea }}` - Tarea actual

No se requirieron modificaciones en los templates.

---

## Testing Manual

### Verificar Rutas Públicas
```bash
curl http://localhost:8000/
curl http://localhost:8000/login
curl http://localhost:8000/registro
```

### Verificar Rutas Privadas (requiere token)
```bash
# Primero obtener token
TOKEN=$(curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test123"}' \
  | jq -r '.access_token')

# Usar cookie para acceder a frontend
curl http://localhost:8000/dashboard \
  --cookie "access_token=$TOKEN"
```

---

## Próximos Pasos (Opcionales)

1. **CSRF Protection**: Implementar tokens CSRF para formularios POST
2. **Flash Messages**: Reemplazar `get_flashed_messages()` de Flask con alternativo FastAPI
3. **Static Files**: Configurar serving de archivos estáticos (CSS, JS custom)
4. **Session Management**: Implementar refresh de tokens en cookie
5. **Error Pages**: Crear templates para 404, 500, etc.

---

## Archivos Modificados

```
src/taskflow/api/
├── app.py                          (Actualizado: incluye router frontend)
└── routes/
    ├── __init__.py                 (Actualizado: exporta frontend_router)
    └── frontend.py                 (NUEVO: rutas frontend HTML)

docs/
└── fix-frontend.md                 (NUEVO: este documento)
```

---

## Referencias

- [FastAPI: Templating](https://fastapi.tiangolo.com/advanced/templates/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Unidad 3.7: Servicios HTML con FastAPI](../clases-html-v2/unidad-03/clase-03-fastapi-intro.html)

---

## Apéndice: Detalles Técnicos de Implementación

### Importaciones Relativas

Para mantener consistencia con el resto del código base, se usaron importaciones relativas:

```python
from ...models import Usuario
from ...repositories import UsuarioRepository, ProyectoRepository, TareaRepository
from ..dependencies import get_current_user, get_current_active_user
from ..config import settings
```

Patrón:
- `...models` → 3 niveles hacia arriba desde `api/routes/frontend.py`
- `..dependencies` → 2 niveles hacia arriba desde `api/routes/frontend.py`

### Métodos de Repositorio Utilizados

| Operación | Repositorio | Método |
|-----------|-------------|--------|
| Obtener proyecto por ID | ProyectoRepository | `get_by_id(id)` |
| Proyectos de usuario | ProyectoRepository | `get_by_usuario(usuario_id)` |
| Obtener tarea por ID | TareaRepository | `get_by_id(id)` |
| Tareas asignadas | TareaRepository | `get_by_asignado(usuario_id)` |
| Usuario por username | UsuarioRepository | `get_by_username(username)` |

### Atributos de Modelos

| Modelo | Atributo Propietario | Atributo Estado |
|--------|---------------------|-----------------|
| Proyecto | `usuario_id` | `estado` (Enum: EstadoProyecto) |
| Tarea | `asignado_a` | `estado` (Enum: EstadoTarea) |

### Estado Final de la Implementación

```
Total de rutas en la aplicación: 41
├── Rutas API JSON: 27 (/api/*)
│   ├── /api/auth/*: 3
│   ├── /api/usuarios/*: 6
│   ├── /api/proyectos/*: 8
│   └── /api/tareas/*: 10
└── Rutas Frontend HTML: 14
    ├── Públicas: 4 (/, /login, /registro, /logout)
    └── Privadas: 10 (/dashboard, /proyectos/*, /tareas/*, /perfil)
```

### Compilación Verificada

```bash
$ python -m py_compile src/taskflow/api/routes/frontend.py
# Sin errores

$ python -c "from src.taskflow.api.app import create_app; app = create_app(); print('Routes:', len(app.routes))"
# App OK
# Routes: 41
```
