-- ============================================================================
-- TaskFlow Database Schema
-- ============================================================================
-- Project: TaskFlow - Sistema de Gestión de Proyectos y Tareas
-- Course: IF0100 - POO II - UNAULA
-- Semester: 2026-I
-- Version: 1.0
-- Date: 2026-02-07
--
-- Description:
--   Complete database schema for the TaskFlow project management system.
--   Includes users, projects, tasks, and comments tables with proper
--   constraints, indexes, and triggers.
--
-- Dependencies:
--   - PostgreSQL 14+
--   - Extension: uuid-ossp (optional, for future use)
-- ============================================================================

-- ============================================================================
-- EXTENSIONS
-- ============================================================================

-- Extension for UUID generation (optional, reserved for future use)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================================
-- DROP EXISTING TABLES
-- ============================================================================
-- Order matters: drop child tables before parent tables

DROP TABLE IF EXISTS comentarios CASCADE;
DROP TABLE IF EXISTS tareas CASCADE;
DROP TABLE IF EXISTS proyectos CASCADE;
DROP TABLE IF EXISTS usuarios CASCADE;

-- ============================================================================
-- ENUM TYPES
-- ============================================================================
-- Using VARCHAR with CHECK constraints for compatibility and simplicity
-- If using PostgreSQL 12+, consider using ENUM types for better performance

-- ============================================================================
-- TABLE: usuarios
-- ============================================================================

CREATE TABLE usuarios (
    -- Primary Key
    id SERIAL PRIMARY KEY,

    -- Authentication
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,

    -- Profile
    nombre_completo VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE,

    -- Timestamps
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Constraints
    CONSTRAINT username_format
        CHECK (username ~ '^[a-zA-Z0-9_]{3,50}$'),
    CONSTRAINT email_format
        CHECK (email ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'),
    CONSTRAINT nombre_no_vacio
        CHECK (nombre_completo IS NULL OR TRIM(nombre_completo) != '')
);

-- Table Comments
COMMENT ON TABLE usuarios IS 'Usuarios del sistema TaskFlow. Almacena información de autenticación y perfil.';
COMMENT ON COLUMN usuarios.id IS 'Identificador único auto-incremental';
COMMENT ON COLUMN usuarios.username IS 'Nombre de usuario único para login. 3-50 caracteres alfanuméricos y guiones bajos.';
COMMENT ON COLUMN usuarios.email IS 'Correo electrónico único para contacto y notificaciones';
COMMENT ON COLUMN usuarios.password_hash IS 'Hash bcrypt del password. NUNCA almacenar passwords en texto plano.';
COMMENT ON COLUMN usuarios.nombre_completo IS 'Nombre completo para mostrar en la interfaz';
COMMENT ON COLUMN usuarios.activo IS 'Indica si el usuario está activo. Soft delete';
COMMENT ON COLUMN usuarios.creado_en IS 'Fecha y hora de creación del registro';
COMMENT ON COLUMN usuarios.actualizado_en IS 'Fecha y hora de última actualización (mantenido por trigger)';

-- Indexes for usuarios
CREATE INDEX idx_usuarios_username ON usuarios(username);
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_usuarios_activo ON usuarios(activo) WHERE activo = TRUE;
CREATE INDEX idx_usuarios_creado_en ON usuarios(creado_en);

-- ============================================================================
-- TABLE: proyectos
-- ============================================================================

CREATE TABLE proyectos (
    -- Primary Key
    id SERIAL PRIMARY KEY,

    -- Project Info
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,

    -- Relationships
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,

    -- Status
    estado VARCHAR(20) DEFAULT 'activo',

    -- Timestamps
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Constraints
    CONSTRAINT nombre_no_vacio
        CHECK (TRIM(nombre) != ''),
    CONSTRAINT estado_proyecto
        CHECK (estado IN ('activo', 'archivado', 'completado', 'cancelado'))
);

-- Table Comments
COMMENT ON TABLE proyectos IS 'Proyectos de tareas. Cada proyecto agrupa tareas relacionadas.';
COMMENT ON COLUMN proyectos.id IS 'Identificador único auto-incremental';
COMMENT ON COLUMN proyectos.nombre IS 'Nombre del proyecto. Debe ser descriptivo pero conciso.';
COMMENT ON COLUMN proyectos.descripcion IS 'Descripción detallada del proyecto y sus objetivos';
COMMENT ON COLUMN proyectos.usuario_id IS 'ID del usuario creador/propietario del proyecto';
COMMENT ON COLUMN proyectos.estado IS 'Estado actual del proyecto: activo, archivado, completado, cancelado';
COMMENT ON COLUMN proyectos.creado_en IS 'Fecha y hora de creación del proyecto';
COMMENT ON COLUMN proyectos.actualizado_en IS 'Fecha y hora de última actualización (mantenido por trigger)';

-- Indexes for proyectos
CREATE INDEX idx_proyectos_usuario ON proyectos(usuario_id);
CREATE INDEX idx_proyectos_estado ON proyectos(estado);
CREATE INDEX idx_proyectos_creado_en ON proyectos(creado_en DESC);

-- ============================================================================
-- TABLE: tareas
-- ============================================================================

CREATE TABLE tareas (
    -- Primary Key
    id SERIAL PRIMARY KEY,

    -- Task Info
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT,

    -- Status & Priority
    estado VARCHAR(20) DEFAULT 'pendiente',
    prioridad VARCHAR(20) DEFAULT 'media',

    -- Relationships
    proyecto_id INTEGER NOT NULL REFERENCES proyectos(id) ON DELETE CASCADE,
    asignado_a INTEGER REFERENCES usuarios(id) ON DELETE SET NULL,
    creada_por INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,

    -- Dates
    fecha_limite DATE,
    completada_en TIMESTAMP,

    -- Timestamps
    creada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizada_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Constraints
    CONSTRAINT titulo_no_vacio
        CHECK (TRIM(titulo) != ''),
    CONSTRAINT estado_tarea
        CHECK (estado IN ('pendiente', 'en_progreso', 'completada', 'cancelada')),
    CONSTRAINT prioridad_tarea
        CHECK (prioridad IN ('baja', 'media', 'alta', 'urgente')),
    CONSTRAINT fecha_logica
        CHECK (
            completada_en IS NULL OR
            estado = 'completada' OR
            (estado != 'completada' AND completada_en IS NULL)
        )
);

-- Table Comments
COMMENT ON TABLE tareas IS 'Tareas individuales dentro de proyectos. Representa work items con asignación y seguimiento.';
COMMENT ON COLUMN tareas.id IS 'Identificador único auto-incremental';
COMMENT ON COLUMN tareas.titulo IS 'Título breve de la tarea';
COMMENT ON COLUMN tareas.descripcion IS 'Descripción detallada de la tarea y requisitos';
COMMENT ON COLUMN tareas.estado IS 'Estado actual: pendiente, en_progreso, completada, cancelada';
COMMENT ON COLUMN tareas.prioridad IS 'Nivel de prioridad: baja, media, alta, urgente';
COMMENT ON COLUMN tareas.proyecto_id IS 'ID del proyecto al que pertenece la tarea';
COMMENT ON COLUMN tareas.asignado_a IS 'ID del usuario asignado (puede ser NULL si no está asignada)';
COMMENT ON COLUMN tareas.creada_por IS 'ID del usuario que creó la tarea (traceability)';
COMMENT ON COLUMN tareas.fecha_limite IS 'Fecha límite para completar la tarea';
COMMENT ON COLUMN tareas.completada_en IS 'Fecha y hora cuando la tarea fue marcada como completada';
COMMENT ON COLUMN tareas.creada_en IS 'Fecha y hora de creación de la tarea';
COMMENT ON COLUMN tareas.actualizada_en IS 'Fecha y hora de última actualización (mantenido por trigger)';

-- Indexes for tareas
CREATE INDEX idx_tareas_proyecto ON tareas(proyecto_id);
CREATE INDEX idx_tareas_asignado ON tareas(asignado_a) WHERE asignado_a IS NOT NULL;
CREATE INDEX idx_tareas_creada_por ON tareas(creada_por);
CREATE INDEX idx_tareas_estado ON tareas(estado);
CREATE INDEX idx_tareas_prioridad ON tareas(prioridad);
CREATE INDEX idx_tareas_fecha_limite ON tareas(fecha_limite) WHERE fecha_limite IS NOT NULL;
CREATE INDEX idx_tareas_estado_prioridad ON tareas(estado, prioridad);

-- ============================================================================
-- TABLE: comentarios
-- ============================================================================

CREATE TABLE comentarios (
    -- Primary Key
    id SERIAL PRIMARY KEY,

    -- Content
    contenido TEXT NOT NULL,

    -- Relationships
    tarea_id INTEGER NOT NULL REFERENCES tareas(id) ON DELETE CASCADE,
    usuario_id INTEGER NOT NULL REFERENCES usuarios(id) ON DELETE CASCADE,

    -- Timestamps
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Constraints
    CONSTRAINT contenido_no_vacio
        CHECK (TRIM(contenido) != '')
);

-- Table Comments
COMMENT ON TABLE comentarios IS 'Comentarios y discusiones en tareas. Permite colaboración.';
COMMENT ON COLUMN comentarios.id IS 'Identificador único auto-incremental';
COMMENT ON COLUMN comentarios.contenido IS 'Texto del comentario. Markdown soportado en la aplicación.';
COMMENT ON COLUMN comentarios.tarea_id IS 'ID de la tarea comentada. Si se borra la tarea, se borran los comentarios (CASCADE)';
COMMENT ON COLUMN comentarios.usuario_id IS 'ID del autor del comentario';
COMMENT ON COLUMN comentarios.creado_en IS 'Fecha y hora de creación del comentario (inmutable)';

-- Indexes for comentarios
CREATE INDEX idx_comentarios_tarea ON comentarios(tarea_id);
CREATE INDEX idx_comentarios_usuario ON comentarios(usuario_id);
CREATE INDEX idx_comentarios_creado_en ON comentarios(creado_en DESC);

-- ============================================================================
-- TRIGGERS
-- ============================================================================
-- Automatic timestamp management for updated_at/actualizado_en columns

-- Trigger function: actualizar_timestamp
CREATE OR REPLACE FUNCTION actualizar_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.actualizado_en = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

COMMENT ON FUNCTION actualizar_timestamp() IS 'Trigger function que actualiza actualizado_en antes de cada UPDATE';

-- Trigger for: usuarios.actualizado_en
CREATE TRIGGER trigger_usuarios_actualizado
    BEFORE UPDATE ON usuarios
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_timestamp();

COMMENT ON TRIGGER trigger_usuarios_actualizado ON usuarios IS 'Actualiza usuarios.actualizado_en en cada UPDATE';

-- Trigger for: proyectos.actualizado_en
CREATE TRIGGER trigger_proyectos_actualizado
    BEFORE UPDATE ON proyectos
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_timestamp();

COMMENT ON TRIGGER trigger_proyectos_actualizado ON proyectos IS 'Actualiza proyectos.actualizado_en en cada UPDATE';

-- Trigger for: tareas.actualizada_en
CREATE TRIGGER trigger_tareas_actualizada
    BEFORE UPDATE ON tareas
    FOR EACH ROW
    EXECUTE FUNCTION actualizar_timestamp();

COMMENT ON TRIGGER trigger_tareas_actualizada ON tareas IS 'Actualiza tareas.actualizada_en en cada UPDATE';

-- ============================================================================
-- VIEWS (Optional, for common queries)
-- ============================================================================

-- View: tareas_con_detalle
-- Combina tareas con info de proyecto y usuarios asignados
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

COMMENT ON VIEW tareas_con_detalle IS 'Vista conveniente con toda la información de tareas incluyendo nombres de proyecto y usuarios';

-- View: resumen_proyectos
-- Resumen de cada proyecto con conteo de tareas
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

COMMENT ON VIEW resumen_proyectos IS 'Vista con resumen de proyectos y estadísticas de tareas';

-- ============================================================================
-- GRANT PERMISSIONS (Adjust based on your application user)
-- ============================================================================
-- Uncomment and adjust as needed for your setup
--
-- CREATE USER taskflow_app WITH PASSWORD 'change_me_in_production';
-- GRANT CONNECT ON DATABASE taskflow TO taskflow_app;
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO taskflow_app;
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO taskflow_app;
--
-- ALTER DEFAULT PRIVILEGES IN SCHEMA public
--     GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO taskflow_app;
-- ALTER DEFAULT PRIVILEGES IN SCHEMA public
--     GRANT USAGE, SELECT ON SEQUENCES TO taskflow_app;

-- ============================================================================
-- END OF SCHEMA
-- ============================================================================
