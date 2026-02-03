# Instrucciones operativas para agentes (HTML->HTML)

Fuente: clases-html-old/**/*.html (solo lectura)
Destino: clases-html/**/*.html (edición)

Lock por clase:
- coord/LOCKS/<archivo>.lock
- Doble verificación: crear lock y re-leer para validar ownership
- Heartbeat: actualizar cada ~5 min
- Romper lock: solo si heartbeat > 45 min y output ausente/roto; registrar en coord/STATUS.md

Flujo:
1) CONVERT: tomar primera clase TODO/NEEDS_FIX sin lock, copiar HTML, convertir contenido a Python+Angular, marcar DONE.
2) REVIEW: R1 luego R2 luego R3 usando coord/REVIEW_CHECKLIST.md; marcar R1_OK/R2_OK/R3_OK o NEEDS_FIX.
3) Finalizar cuando todo esté R3_OK.

Prohibido:
- Editar clases en .md
- Modificar clases-html-old/
