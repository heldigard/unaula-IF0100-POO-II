# TaskFlow Database

**Proyecto:** TaskFlow - Sistema de Gestión de Proyectos y Tareas
**Curso:** IF0100 - POO II - UNAULA
**Semestre:** 2026-I
**Motor de Base de Datos:** PostgreSQL 14+

---

## Table of Contents

- [Overview](#overview)
- [Database Schema](#database-schema)
- [Setup Instructions](#setup-instructions)
- [Running Scripts](#running-scripts)
- [Database Schema Reference](#database-schema-reference)
- [Common Queries](#common-queries)
- [Troubleshooting](#troubleshooting)

---

## Overview

This directory contains all database scripts for the TaskFlow project management system:

```
database/
├── schema.sql           # Complete schema definition
├── migrations/
│   └── 001_initial.sql  # Initial migration (reversible)
├── seeds/
│   └── desarrollo.sql   # Development seed data
└── README.md            # This file
```

### Entity Relationship Diagram

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│  usuarios   │──────<│  proyectos  │──────<│   tareas    │
└─────────────┘       └─────────────┘       └─────────────┘
       │                     │                     │
       │                     │                     │
       │                     │                     v
       │                     │              ┌─────────────┐
       │                     │              │ comentarios │
       │                     │              └─────────────┘
       │                     │                     ^
       │                     └─────────────────────┘
       │
       └─────────────────────────────────────┘
```

---

## Database Schema

### Tables

| Table | Description | Key Columns |
|-------|-------------|-------------|
| `usuarios` | System users with authentication | id, username, email, password_hash |
| `proyectos` | Projects/Workspaces | id, nombre, usuario_id, estado |
| `tareas` | Tasks within projects | id, titulo, estado, prioridad, proyecto_id |
| `comentarios` | Comments on tasks | id, contenido, tarea_id, usuario_id |

### Enums (CHECK constraints)

**estados de proyecto:** `activo`, `archivado`, `completado`, `cancelado`

**estados de tarea:** `pendiente`, `en_progreso`, `completada`, `cancelada`

**prioridades:** `baja`, `media`, `alta`, `urgente`

---

## Setup Instructions

### Prerequisites

1. **PostgreSQL 14+** installed and running
2. **psql** command-line tool available
3. **Database user** with CREATE DATABASE privileges

### Installation

#### Windows (using installer)

```powershell
# Download from https://www.postgresql.org/download/windows/
# Run installer with default options
# Add PostgreSQL bin to PATH: C:\Program Files\PostgreSQL\15\bin
```

#### Windows (using Chocolatey)

```powershell
choco install postgresql
```

#### macOS (using Homebrew)

```bash
brew install postgresql@15
brew services start postgresql@15
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

---

## Running Scripts

### Step 1: Create the Database

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database and user
CREATE DATABASE taskflow;
CREATE USER taskflow_user WITH PASSWORD 'change_me_in_production';
GRANT ALL PRIVILEGES ON DATABASE taskflow TO taskflow_user;
\q
```

### Step 2: Run Schema

```bash
# Option 1: Using psql
psql -U postgres -d taskflow -f database/schema.sql

# Option 2: From Windows command prompt
psql -U postgres -d taskflow -f F:\UNAULA\IF0100-POO-II\database\schema.sql

# Option 3: Using connection string
psql "postgresql://postgres@localhost/taskflow" -f database/schema.sql
```

### Step 3: Load Seed Data (Optional)

```bash
psql -U postgres -d taskflow -f database/seeds/desarrollo.sql
```

### Step 4: Verify Installation

```bash
psql -U postgres -d taskflow -c "\dt"
psql -U postgres -d taskflow -c "SELECT COUNT(*) FROM usuarios;"
```

---

## Database Schema Reference

### Table: usuarios

```sql
CREATE TABLE usuarios (
    id                  SERIAL PRIMARY KEY,
    username            VARCHAR(50) UNIQUE NOT NULL,
    email               VARCHAR(100) UNIQUE NOT NULL,
    password_hash       VARCHAR(255) NOT NULL,
    nombre_completo     VARCHAR(100),
    activo              BOOLEAN DEFAULT TRUE,
    creado_en           TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizado_en      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Constraints:**
- `username`: 3-50 alphanumeric characters and underscores
- `email`: Valid email format
- `password_hash`: bcrypt hash (never plain text)

**Indexes:** username, email, activo, creado_en

---

### Table: proyectos

```sql
CREATE TABLE proyectos (
    id              SERIAL PRIMARY KEY,
    nombre          VARCHAR(100) NOT NULL,
    descripcion     TEXT,
    usuario_id      INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    estado          VARCHAR(20) DEFAULT 'activo',
    creado_en       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizado_en  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Constraints:**
- `estado`: 'activo', 'archivado', 'completado', 'cancelado'

**Indexes:** usuario_id, estado, creado_en

---

### Table: tareas

```sql
CREATE TABLE tareas (
    id              SERIAL PRIMARY KEY,
    titulo          VARCHAR(200) NOT NULL,
    descripcion     TEXT,
    estado          VARCHAR(20) DEFAULT 'pendiente',
    prioridad       VARCHAR(20) DEFAULT 'media',
    proyecto_id     INTEGER NOT NULL REFERENCES proyectos(id) ON DELETE CASCADE,
    asignado_a      INTEGER REFERENCES usuarios(id) ON DELETE SET NULL,
    creada_por      INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    fecha_limite    DATE,
    completada_en   TIMESTAMP,
    creada_en       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizada_en  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Constraints:**
- `estado`: 'pendiente', 'en_progreso', 'completada', 'cancelada'
- `prioridad`: 'baja', 'media', 'alta', 'urgente'

**Indexes:** proyecto_id, asignado_a, estado, prioridad, fecha_limite

---

### Table: comentarios

```sql
CREATE TABLE comentarios (
    id          SERIAL PRIMARY KEY,
    contenido   TEXT NOT NULL,
    tarea_id    INTEGER NOT NULL REFERENCES tareas(id) ON DELETE CASCADE,
    usuario_id  INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    creado_en   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Indexes:** tarea_id, usuario_id, creado_en

---

## Common Queries

### Get all projects with task counts

```sql
SELECT
    p.id,
    p.nombre,
    p.estado,
    COUNT(t.id) AS total_tareas,
    COUNT(t.id) FILTER (WHERE t.estado = 'pendiente') AS pendientes,
    COUNT(t.id) FILTER (WHERE t.estado = 'completada') AS completadas
FROM proyectos p
LEFT JOIN tareas t ON p.id = t.proyecto_id
GROUP BY p.id
ORDER BY p.creado_en DESC;
```

### Get user's tasks across all projects

```sql
SELECT
    t.id,
    t.titulo,
    t.estado,
    t.prioridad,
    t.fecha_limite,
    p.nombre AS proyecto
FROM tareas t
JOIN proyectos p ON t.proyecto_id = p.id
WHERE t.asignado_a = 2  -- user_id
ORDER BY t.prioridad DESC, t.fecha_limite ASC;
```

### Get overdue tasks

```sql
SELECT
    t.id,
    t.titulo,
    t.estado,
    t.fecha_limite,
    u.username AS asignado_a,
    p.nombre AS proyecto
FROM tareas t
JOIN proyectos p ON t.proyecto_id = p.id
LEFT JOIN usuarios u ON t.asignado_a = u.id
WHERE t.fecha_limite < CURRENT_DATE
  AND t.estado NOT IN ('completada', 'cancelada')
ORDER BY t.fecha_limite ASC;
```

### Get tasks with comments count

```sql
SELECT
    t.id,
    t.titulo,
    t.estado,
    COUNT(c.id) AS num_comentarios
FROM tareas t
LEFT JOIN comentarios c ON t.id = c.tarea_id
WHERE t.proyecto_id = 1
GROUP BY t.id
ORDER BY num_comentarios DESC;
```

### Search tasks by keyword

```sql
SELECT
    t.id,
    t.titulo,
    t.descripcion,
    p.nombre AS proyecto
FROM tareas t
JOIN proyectos p ON t.proyecto_id = p.id
WHERE t.titulo ILIKE '%api%'
   OR t.descripcion ILIKE '%api%'
ORDER BY t.creada_en DESC;
```

---

## Troubleshooting

### Issue: "FATAL: database "taskflow" does not exist"

**Solution:** Create the database first
```bash
psql -U postgres -c "CREATE DATABASE taskflow;"
```

### Issue: "FATAL: password authentication failed for user"

**Solution:** Check pg_hba.conf or use trust authentication for local development

**Windows:** `C:\Program Files\PostgreSQL\15\data\pg_hba.conf`

Change this line:
```
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
```

To:
```
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
```

Then restart PostgreSQL service:
```powershell
Restart-Service postgresql-x64-15
```

### Issue: "ERROR: must be owner of table usuarios"

**Solution:** Run scripts as postgres user or grant privileges
```bash
psql -U postgres -d taskflow -c "GRANT ALL ON ALL TABLES IN SCHEMA public TO taskflow_user;"
```

### Issue: "relation already exists"

**Solution:** Drop existing tables first
```bash
psql -U postgres -d taskflow -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
```

Or use the DROP statements in schema.sql before CREATE TABLE.

### Issue: Cannot connect to PostgreSQL server

**Check if PostgreSQL is running:**

Windows:
```powershell
Get-Service postgresql*
```

macOS/Linux:
```bash
# macOS
brew services list

# Linux
sudo systemctl status postgresql
```

**Start PostgreSQL if stopped:**

Windows:
```powershell
Start-Service postgresql-x64-15
```

macOS:
```bash
brew services start postgresql@15
```

Linux:
```bash
sudo systemctl start postgresql
```

---

## Additional Resources

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [psql Cheat Sheet](https://www.postgresql.org/docs/current/app-psql.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [FastAPI Database Tutorial](https://fastapi.tiangolo.com/tutorial/sql-databases/)

---

## Database Administration

### Backup Database

```bash
pg_dump -U postgres taskflow > taskflow_backup_$(date +%Y%m%d).sql
```

### Restore Database

```bash
psql -U postgres taskflow < taskflow_backup_20260207.sql
```

### Drop Database

```bash
psql -U postgres -c "DROP DATABASE IF EXISTS taskflow;"
```

### Reset Database (Drop + Recreate + Seed)

```bash
psql -U postgres -c "DROP DATABASE IF EXISTS taskflow;"
psql -U postgres -c "CREATE DATABASE taskflow;"
psql -U postgres -d taskflow -f database/schema.sql
psql -U postgres -d taskflow -f database/seeds/desarrollo.sql
```

---

**Version:** 1.0
**Last Updated:** 2026-02-07
**Maintainer:** AGENTE_DB - Experto PostgreSQL
