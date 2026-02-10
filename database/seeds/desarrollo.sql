-- ============================================================================
-- Seed Data: Desarrollo
-- ============================================================================
-- TaskFlow Database Seed
-- Environment: Development
-- Date: 2026-02-07
-- Author: AGENTE_DB - Experto PostgreSQL
--
-- Description:
--   Datos de prueba para desarrollo del proyecto TaskFlow.
--   Incluye usuarios, proyectos, tareas y comentarios de ejemplo.
--
-- Usage:
--   psql -U username -d database -f seeds/desarrollo.sql
--
-- Notes:
--   - Todos los usuarios usan el mismo password: "password123"
--   - El hash fue generado con bcrypt (cost=12)
--   - Para generar nuevos hashes: python -c "import bcrypt; print(bcrypt.hashpw(b'password123', bcrypt.gensalt(12)).decode())"
-- ============================================================================

-- BEGIN;

-- ============================================================================
-- CLEAN EXISTING DATA (Optional)
-- ============================================================================
-- Uncomment if you want to clean before seeding
-- TRUNCATE comentarios CASCADE;
-- TRUNCATE tareas CASCADE;
-- TRUNCATE proyectos CASCADE;
-- TRUNCATE usuarios RESTART IDENTITY CASCADE;

-- ============================================================================
-- USUARIOS
-- ============================================================================
-- Password: "password123" for all users
-- Hash: $2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5N9M/t0ch9S1i

INSERT INTO usuarios (username, email, password_hash, nombre_completo, activo) VALUES
('admin', 'admin@taskflow.local', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5N9M/t0ch9S1i', 'Administrador del Sistema', TRUE),
('jdoe', 'john.doe@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5N9M/t0ch9S1i', 'John Doe', TRUE),
('asmith', 'alice.smith@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5N9M/t0ch9S1i', 'Alice Smith', TRUE),
('bjones', 'bob.jones@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5N9M/t0ch9S1i', 'Bob Jones', TRUE),
('cwhite', 'carol.white@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5N9M/t0ch9S1i', 'Carol White', FALSE);

-- ============================================================================
-- PROYECTOS
-- ============================================================================

INSERT INTO proyectos (nombre, descripcion, usuario_id, estado) VALUES
('TaskFlow - Sistema de Gestión', 'Sistema completo de gestión de proyectos y tareas para el curso POO II', 1, 'activo'),
('Curso POO II', 'Proyecto integrador del curso - Desarrollo de TaskFlow', 2, 'activo'),
('App Móvil TaskFlow', 'Aplicación móvil nativa para Android y iOS', 3, 'activo'),
('Website Corporativo', 'Rediseño del sitio web corporativo de la empresa', 4, 'activo'),
('Sistema de Facturación', 'Módulo de facturación electrónica con integración fiscal', 2, 'archivado');

-- ============================================================================
-- TAREAS
-- ============================================================================

-- Tareas para proyecto 1: TaskFlow
INSERT INTO tareas (titulo, descripcion, estado, prioridad, proyecto_id, asignado_a, creada_por, fecha_limite, completada_en) VALUES
('Configurar entorno de desarrollo', 'Instalar Python 3.11+, PostgreSQL, configurar virtualenv y dependencias base', 'completada', 'alta', 1, 2, 1, '2026-02-10', '2026-02-08 14:30:00'),
('Diseñar modelo de datos', 'Crear diagrama ER y definir todas las entidades, relaciones y atributos', 'completada', 'alta', 1, 2, 1, '2026-02-12', '2026-02-09 16:45:00'),
('Implementar modelos SQLAlchemy', 'Crear modelos de SQLAlchemy para Usuario, Proyecto, Tarea y Comentario', 'en_progreso', 'alta', 1, 2, 1, '2026-02-15', NULL),
('Crear API REST con FastAPI', 'Implementar endpoints CRUD para todas las entidades', 'pendiente', 'alta', 1, 3, 1, '2026-02-20', NULL),
('Implementar autenticación JWT', 'Login, logout, refresh tokens y middleware de autenticación', 'pendiente', 'alta', 1, 3, 1, '2026-02-22', NULL),
('Diseñar interfaz con Jinja2', 'Templates base, layouts y componentes reutilizables', 'pendiente', 'media', 1, 4, 1, '2026-02-25', NULL),
('Implementar HTMX', 'Interactividad dinámica sin JavaScript complejo', 'pendiente', 'media', 1, 4, 1, '2026-02-28', NULL),
('Escribir tests unitarios', 'Cobertura >80% con pytest para todos los módulos', 'pendiente', 'alta', 1, 2, 1, '2026-03-05', NULL),
('Documentar API', 'Documentación OpenAPI/Swagger automática', 'pendiente', 'baja', 1, 2, 1, '2026-03-08', NULL),
('Deploy en producción', 'Configurar servidor, Docker, nginx y SSL', 'pendiente', 'urgente', 1, 2, 1, '2026-03-15', NULL);

-- Tareas para proyecto 2: Curso POO II
INSERT INTO tareas (titulo, descripcion, estado, prioridad, proyecto_id, asignado_a, creada_por, fecha_limite, completada_en) VALUES
('Completar Unidad 0', 'Notebooks de repaso de Python fundamentals', 'completada', 'alta', 2, 2, 2, '2026-02-05', '2026-02-03 10:00:00'),
('Estudiar clases y objetos', 'Unidad 1 - Clases, herencia, polimorfismo en Python', 'en_progreso', 'alta', 2, 2, 2, '2026-02-12', NULL),
('Implementar modelos del proyecto', 'Crear clases Usuario, Proyecto, Tarea con dataclasses', 'pendiente', 'alta', 2, 2, '2026-02-15', NULL),
('Taller de TDD', 'Práctica de Test Driven Development con pytest', 'pendiente', 'media', 2, 2, 2, '2026-02-19', NULL),
('Examen parcial', 'Evaluación de unidades 0 y 1', 'pendiente', 'urgente', 2, 2, 2, '2026-02-22', NULL);

-- Tareas para proyecto 3: App Móvil
INSERT INTO tareas (titulo, descripcion, estado, prioridad, proyecto_id, asignado_a, creada_por, fecha_limite, completada_en) VALUES
('Requerimientos funcionales', 'Documentar todos los requerimientos de la app móvil', 'completada', 'alta', 3, 3, 3, '2026-02-01', '2026-01-28 15:00:00'),
('UI/UX Design', 'Diseñar pantallas y flujos de usuario en Figma', 'en_progreso', 'alta', 3, 3, 3, '2026-02-10', NULL),
('Prototipo interactivo', 'Crear prototipo navegable para validación con stakeholders', 'pendiente', 'media', 3, 4, 3, '2026-02-15', NULL),
('Setup React Native', 'Inicializar proyecto con Expo o React Native CLI', 'pendiente', 'alta', 3, 3, 3, '2026-02-18', NULL),
('Integración API', 'Conectar con backend REST de TaskFlow', 'pendiente', 'alta', 3, 3, 3, '2026-03-01', NULL),
('Autenticación móvil', 'Implementar login, logout y persistencia de sesión', 'pendiente', 'alta', 3, 3, 3, '2026-03-05', NULL),
('Publicación Play Store', 'Build release y publicar en Google Play', 'pendiente', 'urgente', 3, 3, 3, '2026-03-20', NULL),
('Publicación App Store', 'Build release y publicar en Apple App Store', 'pendiente', 'urgente', 3, 3, 3, '2026-03-22', NULL);

-- Tareas para proyecto 4: Website Corporativo
INSERT INTO tareas (titulo, descripcion, estado, prioridad, proyecto_id, asignado_a, creada_por, fecha_limite, completada_en) VALUES
('Audit SEO actual', 'Analizar sitio existente y crear reporte SEO', 'completada', 'media', 4, 4, 4, '2026-02-02', '2026-01-30 11:00:00'),
('Nuevo diseño visual', 'Rediseñar homepage y páginas principales', 'en_progreso', 'alta', 4, 4, 4, '2026-02-12', NULL),
('Migración de contenido', 'Transferir contenido desde CMS antiguo al nuevo sistema', 'pendiente', 'media', 4, 4, 4, '2026-02-18', NULL),
('Optimización de performance', 'Mejorar Core Web Vitals y tiempo de carga', 'pendiente', 'alta', 4, 2, 4, '2026-02-20', NULL),
('Testing cross-browser', 'Verificar compatibilidad con Chrome, Firefox, Safari, Edge', 'pendiente', 'media', 4, 2, 4, '2026-02-22', NULL),
('Responsive design', 'Asegurar correcta visualización en móvil y tablet', 'pendiente', 'alta', 4, 4, 4, '2026-02-25', NULL),
('Accessibility audit', 'Verificar WCAG 2.1 AA compliance', 'pendiente', 'baja', 4, 4, 4, '2026-02-28', NULL);

-- Tareas para proyecto 5: Sistema de Facturación (archivado)
INSERT INTO tareas (titulo, descripcion, estado, prioridad, proyecto_id, asignado_a, creada_por, fecha_limite, completada_en) VALUES
('Diseñar schema fiscal', 'Definir estructura para facturas electrónicas locales', 'cancelada', 'alta', 5, 2, 2, '2025-12-15', NULL),
('Integración DIAN', 'Conectar con API de la DIAN para facturación electrónica', 'cancelada', 'urgente', 5, 2, 2, '2025-12-20', NULL);

-- ============================================================================
-- COMENTARIOS
-- ============================================================================

-- Comentarios para tarea 1 (Configurar entorno)
INSERT INTO comentarios (contenido, tarea_id, usuario_id, creado_en) VALUES
('He instalado Python 3.11 y PostgreSQL 15. Virtualenv creado en venv/', 1, 2, '2026-02-07 09:00:00'),
('Recuerda agregar requirements.txt con las dependencias base: fastapi, uvicorn, sqlalchemy, pydantic, passlib[bcrypt], python-jose[cryptography]', 1, 1, '2026-02-07 10:30:00'),
('Requirements actualizado. Ya tengo el entorno funcionando.', 1, 2, '2026-02-07 14:00:00');

-- Comentarios para tarea 3 (Modelos SQLAlchemy)
INSERT INTO comentarios (contenido, tarea_id, usuario_id, creado_en) VALUES
('Usar SQLAlchemy 2.0 con async/await para mejor performance', 3, 1, '2026-02-08 11:00:00'),
('Considerar usar Alembic para migraciones de base de datos', 3, 1, '2026-02-08 11:05:00'),
('Buena idea. Agrego Alembic al requirements.txt', 3, 2, '2026-02-08 15:30:00');

-- Comentarios para tarea 4 (API REST)
INSERT INTO comentarios (contenido, tarea_id, usuario_id, creado_en) VALUES
('FastAPI auto-genera documentación con OpenAPI. Solo falta configurar los meta datos', 4, 3, '2026-02-09 10:00:00'),
('Recordar implementar paginación en endpoints que retornan listas', 4, 1, '2026-02-09 11:30:00');

-- Comentarios para tarea 5 (Autenticación JWT)
INSERT INTO comentarios (contenido, tarea_id, usuario_id, creado_en) VALUES
('Usar passlib con bcrypt para hashear passwords. Nunca almacenar en texto plano', 5, 1, '2026-02-09 14:00:00'),
('Implementar refresh tokens para mejor UX. Access token de 15min, refresh token de 7 dias', 5, 1, '2026-02-09 14:05:00');

-- Comentarios para tarea 9 (Examen parcial)
INSERT INTO comentarios (contenido, tarea_id, usuario_id, creado_en) VALUES
('¿Qué temas entran en el examen?', 23, 2, '2026-02-07 16:00:00'),
('Unidades 0 y 1 completas. Enfócate en: clases, herencia, polimorfismo, dataclasses, y patrones de diseño', 23, 1, '2026-02-07 16:30:00'),
('¿Viene algo de pytest?', 23, 2, '2026-02-07 17:00:00'),
('Sí, conceptos básicos de TDD y fixtures', 1, 23, '2026-02-07 17:15:00');

-- Comentarios para tarea 11 (UI/UX Design)
INSERT INTO comentarios (contenido, tarea_id, usuario_id, creado_en) VALUES
('Compartí el link de Figma en el chat del equipo', 26, 3, '2026-02-06 10:00:00'),
('El diseño se ve muy bien. Solo considerar dark mode', 26, 4, '2026-02-06 14:30:00');

-- ============================================================================
-- OUTPUT SUMMARY
-- ============================================================================

DO $$
BEGIN
    RAISE NOTICE '============================================================================';
    RAISE NOTICE 'Seed Data Loaded Successfully';
    RAISE NOTICE '============================================================================';
    RAISE NOTICE 'Usuarios: %', (SELECT COUNT(*) FROM usuarios);
    RAISE NOTICE 'Proyectos: %', (SELECT COUNT(*) FROM proyectos);
    RAISE NOTICE 'Tareas: %', (SELECT COUNT(*) FROM tareas);
    RAISE NOTICE 'Comentarios: %', (SELECT COUNT(*) FROM comentarios);
    RAISE NOTICE '';
    RAISE NOTICE 'Login credentials:';
    RAISE NOTICE '  Username: admin      | Password: password123';
    RAISE NOTICE '  Username: jdoe       | Password: password123';
    RAISE NOTICE '  Username: asmith     | Password: password123';
    RAISE NOTICE '  Username: bjones     | Password: password123';
    RAISE NOTICE '  Username: cwhite     | Password: password123 (inactive)';
    RAISE NOTICE '============================================================================';
END $$;

-- COMMIT;

-- ============================================================================
-- END OF SEED DATA
-- ============================================================================
