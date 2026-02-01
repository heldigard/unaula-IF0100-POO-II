# Teoría - HTML5 y Bootstrap

**IF0100 - Lenguaje de Programación OO II**

---

## HTML5

### Estructura Básica

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página</title>
</head>
<body>
    <header>Encabezado</header>
    <nav>Navegación</nav>
    <main>Contenido principal</main>
    <footer>Pie de página</footer>
</body>
</html>
```

### Elementos Semánticos

| Elemento | Uso |
|----------|-----|
| `<header>` | Encabezado |
| `<nav>` | Navegación |
| `<main>` | Contenido principal |
| `<article>` | Artículo independiente |
| `<section>` | Sección temática |
| `<aside>` | Contenido lateral |
| `<footer>` | Pie de página |

---

## Bootstrap 5

### Sistema de Grillas

```
┌────────────────────────────────────┐
│ Container                          │
│ ┌─────┬─────┬─────┬─────┬─────┐  │
│ │ col │ col │ col │ col │ col │  │
│ │  -2 │ -2  │ -2  │ -2  │ -2  │  │
│ └─────┴─────┴─────┴─────┴─────┘  │
└────────────────────────────────────┘

<div class="container">
    <div class="row">
        <div class="col-2">1</div>
        <div class="col-2">2</div>
        <div class="col-2">3</div>
        <div class="col-2">4</div>
        <div class="col-2">5</div>
    </div>
</div>
```

### Componentes Principales

- **Botones**: `.btn`, `.btn-primary`, `.btn-outline-secondary`
- **Cards**: `.card`, `.card-body`, `.card-title`
- **Forms**: `.form-control`, `.form-label`, `.form-select`
- **Navbar**: `.navbar`, `.navbar-expand-lg`, `.navbar-light`
- **Modals**: `.modal`, `.modal-dialog`, `.modal-content`

---

**Última actualización:** 2026-02-01
