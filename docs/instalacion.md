# Guia de Instalacion - TaskFlow

**Curso:** IF0100 - POO II
**Institucion:** UNAULA
**Semestre:** 2026-I

---

## Tabla de Contenidos

1. [Prerrequisitos](#prerrequisitos)
2. [Instalacion de Herramientas](#instalacion-de-herramientas)
3. [Configuracion del Proyecto](#configuracion-del-proyecto)
4. [Base de Datos](#base-de-datos)
5. [Ejecucion](#ejecucion)
6. [Verificacion](#verificacion)
7. [Solucion de Problemas](#solucion-de-problemas)

---

## Prerrequisitos

### Hardware Minimo

- **Procesador:** Intel Core i3 o equivalente
- **RAM:** 4 GB minimo, 8 GB recomendado
- **Espacio en Disco:** 2 GB libres

### Software Requerido

| Herramienta | Version Minima | Descripcion |
|-------------|----------------|-------------|
| Python | 3.11+ | Lenguaje de programacion |
| PostgreSQL | 15+ | Base de datos |
| Git | 2.30+ | Control de versiones |
| VS Code | 1.80+ | Editor de codigo (recomendado) |
| Navegador | Chrome/Firefox | Para acceder a la aplicacion |

### Sistema Operativo

- Windows 10/11
- macOS 12+ (Monterey)
- Ubuntu 20.04+ o distribucion Linux equivalente

---

## Instalacion de Herramientas

### Windows

#### 1. Instalar Python 3.11+

1. Descargar desde [python.org](https://www.python.org/downloads/)
2. Ejecutar el instalador
3. **IMPORTANTE:** Marcar "Add Python to PATH"
4. Verificar instalacion:

```cmd
python --version
# Output esperado: Python 3.11.x o superior
```

#### 2. Instalar PostgreSQL 15+

1. Descargar desde [postgresql.org](https://www.postgresql.org/download/windows/)
2. Ejecutar el instalador
3. Anotar la password que ingreses (la necesitaras despues)
4. Asegurarte de que pgAdmin 4 tambien se instale
5. Verificar instalacion:

```cmd
psql --version
# Output esperado: psql (PostgreSQL) 15.x o superior
```

#### 3. Instalar Git

1. Descargar desde [git-scm.com](https://git-scm.com/download/win)
2. Ejecutar el instalador con opciones por defecto
3. Verificar instalacion:

```cmd
git --version
# Output esperado: git version 2.30.x o superior
```

#### 4. Instalar Visual Studio Code (Opcional pero Recomendado)

1. Descargar desde [code.visualstudio.com](https://code.visualstudio.com/)
2. Instalar extensiones recomendadas:
   - Python
   - Pylance
   - Jupyter
   - PostgreSQL

---

### macOS

#### 1. Instalar Python 3.11+

**Opcion A: Usar Homebrew (Recomendado)**

```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python@3.11

# Verificar instalacion
python3.11 --version
```

**Opcion B: Instalador Oficial**

1. Descargar desde [python.org](https://www.python.org/downloads/macos/)
2. Ejecutar el instalador pkg
3. Verificar instalacion:

```bash
python3 --version
```

#### 2. Instalar PostgreSQL 15+

**Opcion A: Usar Homebrew (Recomendado)**

```bash
# Instalar PostgreSQL
brew install postgresql@15

# Iniciar servicio
brew services start postgresql@15

# Crear usuario y base de datos
createdb

# Verificar instalacion
psql --version
```

**Opcion B: Postgres.app**

1. Descargar desde [postgresapp.com](https://postgresapp.com/)
2. Arrastrar a Applications
3. Abrir Postgres.app
4. Inicializar la base de datos

#### 3. Instalar Git

```bash
# Usar Homebrew
brew install git

# Verificar instalacion
git --version
```

---

### Linux (Ubuntu/Debian)

```bash
# Actualizar repositorios
sudo apt update

# Instalar Python 3.11+
sudo apt install python3.11 python3.11-venv python3-pip

# Instalar PostgreSQL 15+
sudo apt install postgresql-15 postgresql-contrib-15

# Instalar Git
sudo apt install git

# Instalar VS Code (opcional)
sudo snap install code --classic

# Verificar instalaciones
python3.11 --version
psql --version
git --version
```

---

## Configuracion del Proyecto

### 1. Clonar el Repositorio

```bash
# Clonar el repositorio
git clone https://github.com/heldigard/unaula-IF0100-POO-II.git

# Entrar al directorio
cd IF0100-POO-II
```

### 2. Crear Entorno Virtual

**Windows (PowerShell o CMD):**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**Windows (Git Bash):**

```bash
python -m venv .venv
source .venv/Scripts/activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Verificar activacion:**

Deberias ver `(.venv)` al inicio de tu prompt.

### 3. Actualizar pip y herramientas

```bash
pip install --upgrade pip setuptools wheel
```

### 4. Instalar Dependencias

```bash
# Instalar todas las dependencias
pip install -r requirements.txt
```

**Tiempo estimado:** 2-5 minutos dependiendo de tu conexion.

---

## Base de Datos

### 1. Crear Base de Datos

**Windows:**

```cmd
psql -U postgres
```

**macOS/Linux:**

```bash
sudo -u postgres psql
```

**Dentro de psql:**

```sql
-- Crear base de datos
CREATE DATABASE taskflow;

-- Verificar que se creo
\l

-- Salir
\q
```

### 2. Ejecutar Esquema de Base de Datos

**Windows:**

```cmd
psql -U postgres -d taskflow -f database/schema.sql
```

**macOS/Linux:**

```bash
psql -U postgres -d taskflow -f database/schema.sql
```

**Salida esperada:**

```
CREATE EXTENSION
DROP TABLE
DROP TABLE
DROP TABLE
DROP TABLE
CREATE TABLE
COMMENT
CREATE INDEX
...
```

### 3. Cargar Datos de Prueba (Opcional)

**Windows:**

```cmd
psql -U postgres -d taskflow -f database/seeds/desarrollo.sql
```

**macOS/Linux:**

```bash
psql -U postgres -d taskflow -f database/seeds/desarrollo.sql
```

**Datos de prueba incluidos:**

- 4 usuarios (password: `password123`)
- 4 proyectos
- 5 tareas de ejemplo

### 4. Verificar Instalacion

```sql
-- Conectarse a la base de datos
psql -U postgres -d taskflow

-- Verificar tablas
\dt

-- Deberias ver:
--     Schema     |     Name      | Type  |   Owner
-- ---------------+---------------+-------+----------
--  public        | comentarios   | table | postgres
--  public        | proyectos     | table | postgres
--  public        | tareas        | table | postgres
--  public        | usuarios      | table | postgres

-- Verificar datos de prueba
SELECT COUNT(*) FROM usuarios;
-- Output: 4

-- Salir
\q
```

---

## Configuracion de Variables de Entorno

### 1. Crear Archivo .env

**Copiar el archivo de ejemplo:**

**Windows:**

```cmd
copy .env.example .env
```

**macOS/Linux:**

```bash
cp .env.example .env
```

### 2. Editar .env

Crear el archivo `.env` en la raiz del proyecto:

```bash
# Database
DATABASE_URL=postgresql://taskflow:taskpass@localhost:5432/taskflow

# API
APP_NAME=TaskFlow API
APP_VERSION=0.1.0
DEBUG=true

# Security
SECRET_KEY=cambia-esto-en-produccion-usa-al-menos-32-caracteres
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS (origins permitidos, separados por coma)
CORS_ORIGINS=http://localhost:3000,http://localhost:8000
```

**Generar SECRET_KEY seguro:**

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## Ejecucion

### 1. Ejecutar Servidor de Desarrollo

```bash
uvicorn src.taskflow.api.app:app --reload
```

**Opciones adicionales:**

```bash
# Puerto personalizado
uvicorn src.taskflow.api.app:app --reload --port 8080

# Host especifico (accesible desde red local)
uvicorn src.taskflow.api.app:app --reload --host 0.0.0.0

# Modo produccion (no usar reload)
uvicorn src.taskflow.api.app:app --host 0.0.0.0 --port 8000
```

**Salida esperada:**

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 2. Acceder a la Aplicacion

Abre tu navegador y accede a:

- **Aplicacion:** http://localhost:8000
- **Documentacion API (Swagger):** http://localhost:8000/docs
- **Documentacion API (ReDoc):** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/health

---

## Verificacion

### 1. Verificar API

```bash
# Health check
curl http://localhost:8000/health

# Output esperado:
# {"status":"healthy"}
```

### 2. Verificar Base de Datos

```bash
# Conectarse
psql -U postgres -d taskflow

# Consultar
SELECT COUNT(*) FROM usuarios;
SELECT COUNT(*) FROM proyectos;
SELECT COUNT(*) FROM tareas;

# Salir
\q
```

### 3. Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Output esperado:
# tests/test_models.py::TestUsuario::test_creacion_usuario_minimo PASSED
# tests/test_models.py::TestUsuario::test_creacion_usuario_completo PASSED
# ...
# ==================== X passed in Y seconds ====================
```

---

## Solucion de Problemas

### Problema: "python no se reconoce como comando"

**Windows:**

1. Reinstalar Python marcando "Add Python to PATH"
2. O agregar manualmente al PATH:

```cmd
setx PATH "%PATH%;C:\Users\TuUsuario\AppData\Local\Programs\Python\Python311\Scripts"
```

### Problema: "psql: connection refused"

**Soluciones:**

1. Verificar que PostgreSQL este corriendo:

**Windows:**
- Abrir Services.msc
- Buscar "postgresql-x64-15"
- Iniciar servicio

**macOS:**
```bash
brew services start postgresql@15
```

**Linux:**
```bash
sudo systemctl start postgresql
```

2. Verificar que el puerto 5432 este disponible:

```bash
# Windows (PowerShell)
netstat -an | findstr 5432

# macOS/Linux
lsof -i :5432
```

### Problema: "ImportError: No module named 'fastapi'"

**Solucion:**

```bash
# Asegurarte de estar en el entorno virtual
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Reinstalar dependencias
pip install -r requirements.txt
```

### Problema: "database is locked" o "database exists"

**Solucion:**

```bash
# Conectarse a PostgreSQL
psql -U postgres

# Eliminar y recrear base de datos
DROP DATABASE IF EXISTS taskflow;
CREATE DATABASE taskflow;

-- Salir
\q

-- Reejecutar scripts
psql -U postgres -d taskflow -f database/schema.sql
psql -U postgres -d taskflow -f database/seeds/desarrollo.sql
```

### Problema: Puerto 8000 ya en uso

**Solucion 1: Cambiar puerto**

```bash
uvicorn src.taskflow.api.app:app --reload --port 8080
```

**Solucion 2: Matar proceso que usa el puerto**

**Windows:**
```cmd
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**macOS/Linux:**
```bash
lsof -ti :8000 | xargs kill -9
```

### Problema: "permission denied" en Linux/macOS

**Solucion:**

```bash
# Dar permisos de ejecucion a scripts
chmod +x scripts/*.sh

# O usar sudo (no recomendado para desarrollo)
sudo pip install -r requirements.txt
```

---

## Instalacion con Docker (Opcional)

Si prefieres usar Docker y Docker Compose:

### 1. Crear docker-compose.yml

```yaml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: taskflow
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  app:
    build: .
    command: uvicorn src.taskflow.api.app:app --host 0.0.0.0 --port 8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/taskflow

volumes:
  postgres_data:
```

### 2. Ejecutar

```bash
# Construir y ejecutar
docker-compose up --build

# Ejecutar en background
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener
docker-compose down
```

---

## Siguiente Paso

Una vez completada la instalacion:

1. Revisa la [arquitectura del sistema](docs/arquitectura.md)
2. Explora la [documentacion de la API](docs/api.md)
3. Revisa los [notebooks de aprendizaje](notebooks/)
4. Comienza a desarrollar!

---

**UNAULA - IF0100 - POO II - 2026-I**
