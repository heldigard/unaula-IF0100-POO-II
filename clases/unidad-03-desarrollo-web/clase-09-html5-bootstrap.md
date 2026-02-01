---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 3'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
style: |
  section {
    font-size: 22px;
  }
  h1 {
    color: #1e40af;
    font-size: 2em;
  }
  h2 {
    color: #1e3a8a;
    font-size: 1.5em;
  }
  h3 {
    color: #3b82f6;
    font-size: 1.2em;
  }
  table {
    font-size: 0.85em;
  }
  code {
    font-size: 0.8em;
  }
  pre {
    font-size: 0.7em;
  }
---

<!-- _class: lead -->

# HTML5 y Bootstrap

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 3 - Clase 9**

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

| # | Objetivo |
|---|-----------|
| 1 | **Utilizar** etiquetas semánticas de HTML5 |
| 2 | **Crear** formularios web modernos |
| 3 | **Aplicar** el sistema de grillas de Bootstrap |
| 4 | **Utilizar** componentes Bootstrap en vistas ASP.NET |
| 5 | **Desarrollar** interfaces responsivas (mobile-first) |

---

## Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 15' | HTML5: Estructura semántica |
| 15' | Formularios HTML5 |
| 20' | Bootstrap: Introducción y Grid |
| 20' | Componentes Bootstrap |
| 15' | Integración ASP.NET + Bootstrap |
| 5' | Responsive Design |

---

## 1. HTML5: Estructura Semántica

### 📝 Más allá de `<div>`

```html
<!-- ❌ HTML ANTIGUO (no semántico) -->
<div id="header">
    <div id="nav">...</div>
</div>
<div id="content">
    <div id="sidebar">...</div>
    <div id="main">...</div>
</div>
<div id="footer">...</div>

<!-- ✅ HTML5 SEMÁNTICO (significado claro) -->
<header>
    <nav>...</nav>
</header>

<main>
    <aside>...</aside>
    <section>
        <article>...</article>
        <article>...</article>
    </section>
</main>

<footer>...</footer>
```

---

## Etiquetas Semánticas HTML5

```
┌─────────────────────────────────────────────────────────────┐
│              ETIQUETAS SEMÁNTICAS HTML5                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ESTRUCTURA DE PÁGINA                                       │
│  ┌─────────┬─────────────────────────────────────────┐     │
│  │<header> │ Cabecera: logo, título, navegación      │     │
│  ├─────────┼─────────────────────────────────────────┤     │
│  │<nav>    │ Navegación: menú principal              │     │
│  ├─────────┼─────────────────────────────────────────┤     │
│  │<main>   │ Contenido principal (uno por página)    │     │
│  ├─────────┼─────────────────────────────────────────┤     │
│  │<section>│ Sección temática del contenido          │     │
│  ├─────────┼─────────────────────────────────────────┤     │
│  │<article>│ Contenido independiente y autocontenido │     │
│  ├─────────┼─────────────────────────────────────────┤     │
│  │<aside>  │ Contenido relacionado, sidebar          │     │
│  ├─────────┼─────────────────────────────────────────┤     │
│  │<footer> │ Pie: copyright, enlaces, contacto       │     │
│  └─────────┴─────────────────────────────────────────┘     │
│                                                             │
│  CONTENIDO                                                  │
│  • <figure> y <figcaption> - Imágenes con leyenda          │
│  • <time> - Fechas y horas                                 │
│  • <mark> - Texto resaltado                                │
│  • <details> y <summary> - Contenido colapsable            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Ejemplo: Estructura HTML5 Completa

### 📄 Página de Blog

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Blog - UNAULA</title>
</head>
<body>
    <header>
        <h1>🎓 Blog de Ingeniería Informática</h1>
        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/articulos">Artículos</a></li>
                <li><a href="/acerca">Acerca de</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>Últimos Artículos</h2>

            <article>
                <header>
                    <h3>Introducción a ASP.NET Core</h3>
                    <p>Publicado el <time datetime="2026-01-15">
                        15 de enero de 2026</time></p>
                </header>
                <p>ASP.NET Core es el framework moderno de Microsoft...</p>
                <footer>
                    <a href="/articulos/aspnet">Leer más</a>
                </footer>
            </article>

            <article>
                <h3>Patrones de Diseño en C#</h3>
                <p>Los patrones de diseño son soluciones...</p>
            </article>
        </section>

        <aside>
            <h3>Categorías</h3>
            <ul>
                <li>Programación</li>
                <li>Bases de Datos</li>
                <li>Web</li>
            </ul>
        </aside>
    </main>

    <footer>
        <p>&copy; 2026 UNAULA - Ingeniería Informática</p>
    </footer>
</body>
</html>
```

---

## 2. Formularios HTML5

### 📋 Inputs Modernos y Validación

```html
<form action="/registro" method="post">

    <!-- Texto básico -->
    <label for="nombre">Nombre completo:</label>
    <input type="text" id="nombre" name="nombre"
           required minlength="3" maxlength="50"
           placeholder="Ej: María López">

    <!-- Email con validación automática -->
    <label for="email">Correo electrónico:</label>
    <input type="email" id="email" name="email"
           required placeholder="maria@ejemplo.com">

    <!-- Teléfono -->
    <label for="telefono">Teléfono:</label>
    <input type="tel" id="telefono" name="telefono"
           pattern="[0-9]{10}"
           placeholder="3001234567">

    <!-- Números con rango -->
    <label for="edad">Edad:</label>
    <input type="number" id="edad" name="edad"
           min="18" max="100" value="18">

    <!-- Fecha -->
    <label for="fechaNacimiento">Fecha de nacimiento:</label>
    <input type="date" id="fechaNacimiento" name="fechaNacimiento"
           min="1950-01-01" max="2006-12-31">

    <!-- Lista desplegable -->
    <label for="carrera">Carrera:</label>
    <select id="carrera" name="carrera" required>
        <option value="">Seleccione...</option>
        <option value="informatica">Ingeniería Informática</option>
        <option value="sistemas">Ingeniería de Sistemas</option>
        <option value="software">Ingeniería de Software</option>
    </select>

    <!-- Checkbox -->
    <label>
        <input type="checkbox" name="aceptaTerminos" required>
        Acepto los términos y condiciones
    </label>

    <!-- Radio buttons -->
    <fieldset>
        <legend>Género:</legend>
        <label><input type="radio" name="genero" value="F"> Femenino</label>
        <label><input type="radio" name="genero" value="M"> Masculino</label>
        <label><input type="radio" name="genero" value="O"> Otro</label>
    </fieldset>

    <button type="submit">Registrarse</button>
    <button type="reset">Limpiar</button>
</form>
```

---

### Nuevos Tipos de Input

```html
<!-- URL -->
<input type="url" placeholder="https://ejemplo.com">

<!-- Búsqueda -->
<input type="search" placeholder="Buscar...">

<!-- Color -->
<input type="color" value="#ff0000">

<!-- Rango (slider) -->
<input type="range" min="0" max="100" value="50">

<!-- Hora -->
<input type="time">

<!-- Fecha y hora local -->
<input type="datetime-local">

<!-- Mes -->
<input type="month">

<!-- Semana -->
<input type="week">

<!-- Archivo -->
<input type="file" accept=".pdf,.doc,.docx">

<!-- Área de texto -->
<textarea rows="4" cols="50" maxlength="500"
          placeholder="Escribe tu mensaje..."></textarea>
```

---

## 3. Bootstrap: Introducción

### 🎨 Framework CSS Más Popular

```
┌─────────────────────────────────────────────────────────────┐
│                    BOOTSTRAP 5                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ¿QUÉ ES?                                                   │
│  Framework CSS/JavaScript para desarrollo responsivo        │
│  y mobile-first de proyectos web                            │
│                                                             │
│  VENTAJAS:                                                  │
│  ✅ Ahorra tiempo (no reinventar la rueda)                 │
│  ✅ Diseño responsivo incluido                             │
│  ✅ Componentes listos para usar                           │
│  ✅ Compatible con todos los navegadores                   │
│  ✅ Documentación extensa                                  │
│  ✅ Personalizable                                         │
│                                                             │
│  VERSIÓN: Bootstrap 5.3                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Sistema de Grillas Bootstrap

### 📐 El Corazón de Bootstrap

```
┌─────────────────────────────────────────────────────────────┐
│              SISTEMA DE GRILLAS BOOTSTRAP                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  12 COLUMNAS POR FILA                                       │
│                                                             │
│  ├────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┤  │
│  │ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │10 │ 11 │ 12 │  │
│  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘  │
│                                                             │
│  CLASES DE TAMAÑO:                                          │
│  ┌─────────┬───────────────────┬──────────────────────────┐  │
│  │ Clase   │ Breakpoint        │ Típicamente              │  │
│  ├─────────┼───────────────────┼──────────────────────────┤  │
│  │ col-    │ Extra small       │ Móviles portrait         │  │
│  │ col-sm- │ Small (≥576px)    │ Móviles landscape        │  │
│  │ col-md- │ Medium (≥768px)   │ Tablets                  │  │
│  │ col-lg- │ Large (≥992px)    │ Laptops                  │  │
│  │ col-xl- │ Extra large       │ Desktops                 │  │
│  │ col-xxl │ Extra extra large │ Pantallas grandes        │  │
│  └─────────┴───────────────────┴──────────────────────────┘  │
│                                                             │
│  EJEMPLO: col-md-6 = En tablets ocupa 6/12 (50%)           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Grid Bootstrap en Práctica

### 💻 Ejemplos de Uso

```html
<!-- ESTRUCTURA BÁSICA -->
<div class="container">
    <div class="row">
        <div class="col">Columna 1</div>
        <div class="col">Columna 2</div>
        <div class="col">Columna 3</div>
    </div>
</div>

<!-- TAMAÑOS RESPONSIVOS -->
<div class="container">
    <div class="row">
        <!-- Móvil: 100%, Tablet: 50%, Desktop: 33% -->
        <div class="col-12 col-md-6 col-lg-4">Card 1</div>
        <div class="col-12 col-md-6 col-lg-4">Card 2</div>
        <div class="col-12 col-md-6 col-lg-4">Card 3</div>
    </div>
</div>

<!-- SIDEBAR + CONTENIDO -->
<div class="container">
    <div class="row">
        <aside class="col-12 col-md-3">Menú lateral</aside>
        <main class="col-12 col-md-9">Contenido principal</main>
    </div>
</div>

<!-- OFFSET (margen para centrar) -->
<div class="row">
    <div class="col-md-6 offset-md-3">
        Contenido centrado (6 columnas + offset de 3)
    </div>
</div>
```

---

## 4. Componentes Bootstrap

### 🧩 Botones, Alertas, Cards

```html
<!-- BOTONES -->
<button class="btn btn-primary">Primario</button>
<button class="btn btn-secondary">Secundario</button>
<button class="btn btn-success">Éxito</button>
<button class="btn btn-danger">Peligro</button>
<button class="btn btn-warning">Advertencia</button>
<button class="btn btn-info">Información</button>

<!-- Tamaños -->
<button class="btn btn-primary btn-lg">Grande</button>
<button class="btn btn-primary">Normal</button>
<button class="btn btn-primary btn-sm">Pequeño</button>

<!-- Outline -->
<button class="btn btn-outline-primary">Outline</button>

<!-- ─────────────────────────────────────────────── -->

<!-- ALERTAS -->
<div class="alert alert-success" role="alert">
    ✅ Operación completada exitosamente
</div>
<div class="alert alert-danger" role="alert">
    ❌ Ha ocurrido un error
</div>
<div class="alert alert-warning alert-dismissible fade show">
    ⚠️ Atención: revise los datos
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>

<!-- ─────────────────────────────────────────────── -->

<!-- TARJETAS (CARDS) -->
<div class="card" style="width: 18rem;">
    <img src="estudiante.jpg" class="card-img-top" alt="Estudiante">
    <div class="card-body">
        <h5 class="card-title">María López</h5>
        <p class="card-text">Ingeniería Informática - 4° semestre</p>
        <a href="#" class="btn btn-primary">Ver perfil</a>
    </div>
</div>
```

---

## Más Componentes Bootstrap

### 🧩 Navbar, Tablas, Formularios

```html
<!-- NAVBAR (Menú de navegación) -->
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
        <a class="navbar-brand" href="#">UNAULA</a>
        <button class="navbar-toggler" type="button"
                data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" href="#">Inicio</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Estudiantes</a>
                </li>
            </ul>
        </div>
    </div>
</nav>

<!-- TABLA ESTILIZADA -->
<table class="table table-striped table-hover">
    <thead class="table-dark">
        <tr>
            <th>Código</th>
            <th>Nombre</th>
            <th>Promedio</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2024001</td>
            <td>María López</td>
            <td><span class="badge bg-success">4.5</span></td>
            <td>
                <button class="btn btn-sm btn-info">Editar</button>
                <button class="btn btn-sm btn-danger">Eliminar</button>
            </td>
        </tr>
    </tbody>
</table>

<!-- FORMULARIO ESTILIZADO -->
<form>
    <div class="mb-3">
        <label class="form-label">Email</label>
        <input type="email" class="form-control" placeholder="nombre@ejemplo.com">
    </div>
    <div class="mb-3">
        <label class="form-label">Contraseña</label>
        <input type="password" class="form-control">
    </div>
    <button type="submit" class="btn btn-primary">Ingresar</button>
</form>
```

---

## Utilidades Bootstrap

### 🛠️ Spacing, Colores, Display

```html
<!-- SPACING: m = margin, p = padding -->
<!-- t = top, b = bottom, s = start, e = end, x = horizontal, y = vertical -->
<!-- 0-5: 0, 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem -->

<div class="m-3">Margin 3 en todos lados</div>
<div class="mt-2 mb-4">Margin top 2, bottom 4</div>
<div class="px-5 py-3">Padding horizontal 5, vertical 3</div>
<div class="mx-auto">Centrado horizontal (auto)</div>

<!-- COLORES DE TEXTO -->
<p class="text-primary">Texto primario (azul)</p>
<p class="text-success">Texto éxito (verde)</p>
<p class="text-danger">Texto peligro (rojo)</p>
<p class="text-warning">Texto advertencia (amarillo)</p>

<!-- COLORES DE FONDO -->
<div class="bg-primary text-white p-3">Fondo azul, texto blanco</div>
<div class="bg-light p-3">Fondo gris claro</div>

<!-- DISPLAY -->
<div class="d-none">Oculto (display: none)</div>
<div class="d-block">Block</div>
<div class="d-flex">Flexbox</div>

<!-- RESPONSIVO -->
<div class="d-none d-md-block">Solo visible en tablet+</div>
<div class="d-block d-md-none">Solo visible en móvil</div>

<!-- TEXTO -->
<p class="text-center">Centrado</p>
<p class="text-end">Alineado derecha</p>
<p class="fw-bold">Negrita</p>
<p class="text-uppercase">mayúsculas</p>
<p class="fs-1">Tamaño 1 (más grande)</p>
```

---

## 5. Integración ASP.NET + Bootstrap

### 🔗 Plantilla Razor (_Layout.cshtml)

```html
@* Views/Shared/_Layout.cshtml *@
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>@ViewData["Title"] - UNAULA</title>

    @* Bootstrap CSS *@
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
          rel="stylesheet">

    @* Estilos personalizados *@
    <link rel="stylesheet" href="~/css/site.css" />
</head>
<body>
    @* Navbar *@
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container">
                <a class="navbar-brand" asp-controller="Home" asp-action="Index">
                    🎓 UNAULA
                </a>
                <button class="navbar-toggler" data-bs-toggle="collapse"
                        data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto">
                        <li class="nav-item">
                            <a class="nav-link" asp-controller="Home" asp-action="Index">Inicio</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" asp-controller="Estudiantes" asp-action="Index">Estudiantes</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    @* Contenido *@
    <div class="container mt-4">
        <main role="main">
            @RenderBody()
        </main>
    </div>

    @* Footer *@
    <footer class="border-top footer text-muted mt-5 py-3">
        <div class="container">
            &copy; 2026 - UNAULA Ingeniería Informática
        </div>
    </footer>

    @* Bootstrap JS *@
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js">
    </script>
    @await RenderSectionAsync("Scripts", required: false)
</body>
</html>
```

---

## Vista con Bootstrap

### 📋 CRUD de Estudiantes

```html
@* Views/Estudiantes/Index.cshtml *@
@model IEnumerable<Estudiante>

@{
    ViewData["Title"] = "Lista de Estudiantes";
}

<div class="d-flex justify-content-between align-items-center mb-4">
    <h1>📚 Estudiantes</h1>
    <a asp-action="Crear" class="btn btn-primary">
        ➕ Nuevo Estudiante
    </a>
</div>

<div class="card shadow">
    <div class="card-body">
        <table class="table table-striped table-hover">
            <thead class="table-dark">
                <tr>
                    <th>@Html.DisplayNameFor(m => m.Codigo)</th>
                    <th>@Html.DisplayNameFor(m => m.Nombre)</th>
                    <th>@Html.DisplayNameFor(m => m.Carrera)</th>
                    <th>Promedio</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                @foreach (var item in Model)
                {
                    <tr>
                        <td>@item.Codigo</td>
                        <td>@item.Nombre</td>
                        <td>@item.Carrera</td>
                        <td>
                            @if (item.Promedio >= 3.5)
                            {
                                <span class="badge bg-success">@item.Promedio</span>
                            }
                            else if (item.Promedio >= 3.0)
                            {
                                <span class="badge bg-warning">@item.Promedio</span>
                            }
                            else
                            {
                                <span class="badge bg-danger">@item.Promedio</span>
                            }
                        </td>
                        <td>
                            <a asp-action="Editar" asp-route-id="@item.Id"
                               class="btn btn-sm btn-warning">✏️ Editar</a>
                            <a asp-action="Detalles" asp-route-id="@item.Id"
                               class="btn btn-sm btn-info">👁️ Detalles</a>
                            <a asp-action="Eliminar" asp-route-id="@item.Id"
                               class="btn btn-sm btn-danger">🗑️ Eliminar</a>
                        </td>
                    </tr>
                }
            </tbody>
        </table>
    </div>
</div>
```

---

## Formulario con Bootstrap

### ➕ Crear/Editar Estudiante

```html
@* Views/Estudiantes/Crear.cshtml *@
@model Estudiante

@{
    ViewData["Title"] = "Nuevo Estudiante";
}

<div class="row justify-content-center">
    <div class="col-md-8 col-lg-6">
        <div class="card shadow">
            <div class="card-header bg-primary text-white">
                <h4 class="mb-0">➕ Nuevo Estudiante</h4>
            </div>
            <div class="card-body">
                <form asp-action="Crear" method="post">
                    <div asp-validation-summary="ModelOnly" class="text-danger"></div>

                    <div class="mb-3">
                        <label asp-for="Codigo" class="form-label"></label>
                        <input asp-for="Codigo" class="form-control"
                               placeholder="Ej: 2024001">
                        <span asp-validation-for="Codigo" class="text-danger"></span>
                    </div>

                    <div class="mb-3">
                        <label asp-for="Nombre" class="form-label"></label>
                        <input asp-for="Nombre" class="form-control">
                        <span asp-validation-for="Nombre" class="text-danger"></span>
                    </div>

                    <div class="mb-3">
                        <label asp-for="Carrera" class="form-label"></label>
                        <select asp-for="Carrera" class="form-select">
                            <option value="">Seleccione...</option>
                            <option>Ingeniería Informática</option>
                            <option>Ingeniería de Software</option>
                            <option>Ingeniería de Sistemas</option>
                        </select>
                    </div>

                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a asp-action="Index" class="btn btn-secondary">Cancelar</a>
                        <button type="submit" class="btn btn-primary">Guardar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

@section Scripts {
    @{await Html.RenderPartialAsync("_ValidationScriptsPartial");}
}
```

---

## 6. Responsive Design

### 📱 Mobile-First Approach

```
┌─────────────────────────────────────────────────────────────┐
│              MOBILE-FIRST APPROACH                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PRINCIPIO: Diseñar primero para móvil, luego escalar      │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  MÓVIL (< 576px)         TABLET    DESKTOP          │   │
│  │  ┌──────┐               ┌────┬───┐ ┌───┬───┬───┐   │   │
│  │  │      │               │    │   │ │   │   │   │   │   │
│  │  │ 100% │               │50% │50%│ │33%│33%│33%│   │   │
│  │  │      │               │    │   │ │   │   │   │   │   │
│  │  └──────┘               └────┴───┘ └───┴───┴───┘   │   │
│  │   col-12               col-md-6   col-lg-4         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  EJEMPLO:                                                   │
│  <div class="col-12 col-md-6 col-lg-4">                   │
│    → Móvil:  12/12 = 100%                                  │
│    → Tablet:  6/12 = 50%                                   │
│    → Desktop: 4/12 = 33%                                   │
│  </div>                                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Accesibilidad en HTML5

### ♿ ARIA Labels

```html
@* ACCESIBILIDAD: Importante para usuarios con discapacidades *@
@* ARIA = Accessible Rich Internet Applications *@

<!-- 1. ARIA-LABEL - Descripción para elementos sin texto -->
<input type="search" aria-label="Buscar estudiantes">
<button aria-label="Cerrar ventana">&times;</button>

<!-- 2. ARIA-LABELEDBY - Relacionar con otro elemento -->
<input type="text" id="nombre" aria-labelledby="lbl-nombre">
<label id="lbl-nombre">Nombre completo:</label>

<!-- 3. ARIA-DESCRIBEDBY - Descripción adicional -->
<input type="password" aria-describedby="pwd-help">
<small id="pwd-help">Mínimo 8 caracteres, una mayúscula y un número</small>

<!-- 4. ARIA-HIDDEN - Ocultar a lectores de pantalla -->
<span aria-hidden="true">🎓</span>

<!-- 5. ROLES ARIA - Semántica adicional -->
<nav role="navigation" aria-label="Menú principal">...</nav>
<main role="main">...</main>
<div role="alert" class="alert alert-danger">
    Operación fallida
</div>

<!-- 6. ESTADOS ARIA -->
<button aria-pressed="false">Me gusta</button>
<input aria-invalid="true" aria-describedby="error-msg">
<div id="error-msg" role="alert">El email es inválido</div>
```

---

## Más Componentes Bootstrap

### 🧩 Modals, Collapse, Progress

```html
<!-- MODAL (Ventana emergente) -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal"
        data-bs-target="#exampleModal">
    Abrir Modal
</button>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Confirmar eliminación</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"
                        aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>¿Está seguro que desea eliminar este estudiante?</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary"
                        data-bs-dismiss="modal">Cancelar</button>
                <button type="button" class="btn btn-danger">Eliminar</button>
            </div>
        </div>
    </div>
</div>

<!-- ACCORDION -->
<div class="accordion" id="accordionPreguntas">
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button"
                    data-bs-toggle="collapse" data-bs-target="#collapseUno">
                ¿Qué es ASP.NET Core?
            </button>
        </h2>
        <div id="collapseUno" class="accordion-collapse collapse show"
             data-bs-parent="#accordionPreguntas">
            <div class="accordion-body">
                ASP.NET Core es un framework web de código abierto...
            </div>
        </div>
    </div>
</div>

<!-- PROGRESS BAR -->
<div class="progress" style="height: 25px;">
    <div class="progress-bar" role="progressbar" style="width: 65%;"
         aria-valuenow="65" aria-valuemin="0" aria-valuemax="100">
        65%
    </div>
</div>
```

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **HTML5 semántico** | `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` |
| **Formularios HTML5** | Nuevos tipos: email, tel, date, number, range |
| **Bootstrap Grid** | 12 columnas, clases: `col-`, `col-sm-`, `col-md-`, `col-lg-` |
| **Componentes** | Botones, alertas, cards, navbar, tablas, formularios, modals |
| **Utilidades** | Spacing (`m-`, `p-`), colores (`text-`, `bg-`), display |
| **Responsive** | Mobile-first, breakpoints |
| **Tag Helpers** | `asp-controller`, `asp-action`, `asp-for` |
| **Accesibilidad** | ARIA labels, roles, estados |

---

## Recursos Bootstrap

### 📚 Documentación y Herramientas

- **Documentación oficial:** https://getbootstrap.com/docs/5.3/
- **Iconos:** https://icons.getbootstrap.com/
- **Temas:** https://themes.getbootstrap.com/
- **Builder online:** https://bootstrap.build/
- **Grid generator:** https://grid.layoutit.com/

---

## Ejercicio Práctico

### 📋 Diseñar Página de Estudiantes

**Crear vista "ListaEstudiantes" con:**

1. **Layout responsivo:**
   - Header con navegación
   - Contenido principal con cards de estudiantes
   - 1 columna en móvil, 2 en tablet, 3 en desktop

2. **Card de estudiante con:**
   - Foto (placeholder)
   - Nombre
   - Carrera (badge)
   - Promedio (badge color según valor)
   - Botón "Ver detalle"

3. **Tabla alternativa para desktop**

4. **Formulario de búsqueda arriba**

---

## 🚀 Próxima Clase: MVC y Razor Pages

| Tema | Descripción |
|------|-------------|
| **MVC profundo** | Routing avanzado, Model Binding, Validación |
| **Razor Pages** | Page Models, Handlers (OnGet, OnPost) |
| **Tag Helpers** | Form, Anchor, Custom tag helpers |
| **Partial Views** | ViewComponents |

---

# ¡Gracias!
## ¿Preguntas?

**"Bootstrap: Haz más, escribe menos"**

**UNAULA - Ingeniería Informática - 2026-I**
