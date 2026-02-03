# Checklist de revisión (HTML->HTML)

Estructura / visual:
- No se rompió el layout HTML (diapositivas/secciones siguen igual).
- No hay tags rotos evidentes (cierre de <div>, <section>, <pre><code>, etc.).
- No aparece HTML “crudo” como texto (regresión del problema histórico de layouts). 

Conversión técnica:
- No quedan instrucciones activas de ASP.NET/ADO.NET salvo una sección de equivalencia comparativa.
- C#/.NET -> Python coherente (POO, sintaxis, excepciones).
- Web: se reorientó a Angular (componentes, servicios, routing, forms) donde aplique.
- TDD/BDD/DDD: pytest (+ behave/pytest-bdd opcional) donde aplique.
- Datos: SQL Server + acceso desde Python consistente con STACK.md.
- Clases 12–16: incluye “Equivalencia con ADO.NET / DataSet / DataAdapter” explicada en bullets.

Didáctica:
- Actividades/retos siguen presentes y ejecutables.
- “Entrega con Git” está incluida (branch + 3 commits + tag) sin inflar demasiado.

Salida:
- El archivo final está en `clases-html/<archivo>.html`.
- SOURCE `clases-html-old/` no fue modificado.
