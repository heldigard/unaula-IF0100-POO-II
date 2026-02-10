-- ============================================================================
-- Migration: 001_initial
-- ============================================================================
-- TaskFlow Database Migration
-- Version: 001
-- Date: 2026-02-07
-- Author: AGENTE_DB - Experto PostgreSQL
-- Description: Initial schema creation for TaskFlow project
--
-- This migration creates:
--   - usuarios table (users)
--   - proyectos table (projects)
--   - tareas table (tasks)
--   - comentarios table (comments)
--   - Indexes for performance
--   - Triggers for timestamp management
--   - Views for common queries
--
-- To apply:   psql -U username -d database -f migrations/001_initial.sql
-- To rollback: Execute the DOWN section below
-- ============================================================================

-- ============================================================================
-- UP MIGRATION
-- ============================================================================

-- BEGIN;

-- ============================================================================
-- EXTENSIONS
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================================
-- TABLE: usuarios
-- ============================================================================

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT username_format CHECK (username ~ '^[a-zA-Z0-9_]{3,50}$'),
    CONSTRAINT email_format CHECK (email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'),
    CONSTRAINT nombre_no_vacio CHECK (nombre_completo IS NULL OR TRIM(nombre_completo) != '')
);

COMMENT ON TABLE usuarios IS 'Usuarios del sistema TaskFlow';
COMMENT ON COLUMN usuarios.password_hash IS 'Hash bcrypt del password';

CREATE INDEX idx_usuarios_username ON usuarios(username);
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_usuarios_activo ON usuarios(activo) WHERE activo = TRUE;

-- ============================================================================
-- TABLE: proyectos
-- ============================================================================

CREATE TABLE proyectos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    estado VARCHAR(20) DEFAULT 'activo',
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT nombre_no_vacio CHECK (TRIM(nombre) != ''),
    CONSTRAINT estado_proyecto CHECK (estado IN ('activo', 'archivado', 'completado', 'cancelado'))
);

COMMENT ON TABLE proyectos IS 'Proyectos de tareas';

CREATE INDEX idx_proyectos_usuario ON proyectos(usuario_id);
CREATE INDEX idx_proyectos_estado ON proyectos(estado);

-- ============================================================================
-- TABLE: tareas
-- ============================================================================

CREATE TABLE tareas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(20) DEFAULT 'pendiente',
    prioridad VARCHAR(20) DEFAULT 'media',
    proyecto_id INTEGER NOT NULL REFERENCES proyectos(id) ON DELETE CASCADE,
    asignado_a INTEGER REFERENCES usuarios(id) ON DELETE SET NULL,
    creada_por INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    fecha_limite DATE,
    completada_en TIMESTAMP,
    creada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT titulo_no_vacio CHECK (TRIM(titulo) != ''),
    CONSTRAINT estado_tarea CHECK (estado IN ('pendiente', 'en_progreso', 'completada', 'cancelada')),
    CONSTRAINT prioridad_tarea CHECK (prioridad IN ('baja', 'media', 'alta', 'urgente')),
    CONSTRAINT fecha_logica CHECK (
        completada_en IS NULL OR
        estado = 'completada' OR
        (estado != 'completada' AND completada_en IS NULL)
    )
);

COMMENT ON TABLE tareas IS 'Tareas individuales dentro de proyectos';

CREATE INDEX idx_tareas_proyecto ON tareas(proyecto_id);
CREATE INDEX idx_tareas_asignado ON tareas(asignado_a) WHERE asignado_a IS NOT NULL;
CREATE INDEX idx_tareas_estado ON tareas(estado);
CREATE INDEX idx_tareas_prioridad ON tareas(prioridad);
CREATE INDEX idx_tareas_fecha_limite ON tareas(fecha_limite) WHERE fecha_limite IS NOT NULL;
CREATE INDEX idx_tareas_estado_prioridad ON tareas(estado, prioridad);

-- ============================================================================
-- TABLE: comentarios
-- ============================================================================

CREATE TABLE comentarios (
    id SERIAL PRIMARY KEY,
    contenido TEXT NOT NULL,
    tarea_id INTEGER NOT NULL REFERENCES tareas(id) ON DELETE CASCADE,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT contenido_no_vacio CHECK (TRIM(contenido) != '')
);

COMMENT ON TABLE comentarios IS 'Comentarios en tareas';

CREATE INDEX idx_comentarios_tarea ON comentarios(tarea_id);
CREATE INDEX idx_comentarios_usuario ON comentarios(usuario_id);
CREATE INDEX idx_comentarios_creado_en ON comentarios(creado_en DESC);

-- ============================================================================
-- TRIGGERS
-- ============================================================================

CREATE OR REPLACE FUNCTION actualizar_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.actualizado_en = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_usuarios_actualizado
    BEFORE UPDATE ON usuarios
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_timestamp();

CREATE TRIGGER trigger_proyectos_actualizado
    BEFORE UPDATE ON proyectos
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_timestamp();

CREATE TRIGGER trigger_tareas_actualizada
    BEFORE UPDATE ON tareas
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_timestamp();

-- ============================================================================
-- VIEWS
-- ============================================================================

CREATE OR REPLACE VIEW tareas_con_detalle AS
SELECT
    t.id,
    t.titulo,
    t.descripcion,
    t.estado,
    t.prioridad,
    t.fecha_limite,
    t.completada_en,
    t.creada_en,
    t.actualizada_en,
    p.id AS proyecto_id,
    p.nombre AS proyecto_nombre,
    creador.id AS creador_id,
    creador.username AS creador_username,
    creador.nombre_completo AS creador_nombre,
    asignado.id AS asignado_id,
    asignado.username AS asignado_username,
    asignado.nombre_completo AS asignado_nombre
FROM tareas t
JOIN proyectos p ON t.proyecto_id = p.id
JOIN usuarios creador ON t.creada_por = creador.id
LEFT JOIN usuarios asignado ON t.asignado_a = asignado.id;

CREATE OR REPLACE VIEW resumen_proyectos AS
SELECT
    p.id,
    p.nombre,
    p.descripcion,
    p.estado,
    p.usuario_id AS propietario_id,
    u.username AS propietario_username,
    COUNT(t.id) AS total_tareas,
    COUNT(t.id) FILTER (WHERE t.estado = 'pendiente') AS tareas_pendientes,
    COUNT(t.id) FILTER (WHERE t.estado = 'en_progreso') AS tareas_en_progreso,
    COUNT(t.id) FILTER (WHERE t.estado = 'completada') AS tareas_completadas,
    COUNT(t.id) FILTER (WHERE t.prioridad = 'urgente' AND t.estado != 'completada') AS tareas_urgentes,
    p.creado_en,
    p.actualizado_en
FROM proyectos p
JOIN usuarios u ON p.usuario_id = u.id
LEFT JOIN tareas t ON p.id = t.proyecto_id
GROUP BY p.id, p.nombre, p.descripcion, p.estado, p.usuario_id, u.username, p.creado_en, p.actualizado_en;

-- COMMIT;

-- ============================================================================
-- DOWN MIGRATION (Rollback)
-- ============================================================================
-- To rollback this migration, execute the following:
--
-- BEGIN;
--
-- DROP VIEW IF EXISTS resumen_proyectos CASCADE;
-- DROP VIEW IF EXISTS tareas_con_detalle CASCADE;
--
-- DROP TRIGGER IF EXISTS trigger_tareas_actualizada ON tareas;
-- DROP TRIGGER IF EXISTS trigger_proyectos_actualizado ON proyectos;
-- DROP TRIGGER IF EXISTS trigger_usuarios_actualizado ON usuarios;
-- DROP FUNCTION IF EXISTS actualizar_timestamp();
--
-- DROP TABLE IF EXISTS comentarios CASCADE;
-- DROP TABLE IF EXISTS tareas CASCADE;
-- DROP TABLE IF EXISTS proyectos CASCADE;
-- DROP TABLE IF EXISTS usuarios CASCADE;
--
-- DROP EXTENSION IF EXISTS "uuid-ossp";
--
-- COMMIT;
-- ============================================================================

-- ============================================================================
-- END OF MIGRATION 001_initial
-- ============================================================================
