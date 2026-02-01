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

# Introducción a ASP.NET Core

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 3 - Clase 8**

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

| # | Objetivo |
|---|-----------|
| 1 | **Comprender** la arquitectura de ASP.NET Core |
| 2 | **Diferenciar** entre MVC, Razor Pages y Web API |
| 3 | **Crear** una aplicación web desde cero |
| 4 | **Configurar** el pipeline de middleware |
| 5 | **Implementar** inyección de dependencias básica |

---

## Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 15' | ¿Qué es ASP.NET Core? |
| 15' | Arquitectura y componentes |
| 20' | Crear primera aplicación |
| 15' | Middleware y Pipeline |
| 15' | Inyección de dependencias |
| 10' | Estructura de proyecto |

---

## 1. ¿Qué es ASP.NET Core?

### 📖 Definición

> **ASP.NET Core** es un framework open-source para construir aplicaciones web modernas, cloud-ready y multiplataforma, desarrollado por Microsoft.

### 🚀 Características Principales

| Característica | Descripción |
|----------------|-------------|
| **Alto rendimiento** | Más rápido que Node.js y Java |
| **Multiplataforma** | Windows, Linux, macOS |
| **Modular** | Solo incluyes lo que necesitas |
| **Cloud-ready** | Docker, Kubernetes, Azure |
| **Unificado** | MVC, Razor Pages, Web API, gRPC |
| **Full Stack** | Backend + Frontend integration |

### 📜 Historia

| Versión | Año | Novedad |
|---------|-----|---------|
| ASP.NET | 2002 | Framework original |
| ASP.NET MVC | 2009 | Patrón MVC |
| ASP.NET Core | 2016 | Multiplataforma |
| ASP.NET Core 8 | 2024 | LTS actual |

---

## Modelos de Programación ASP.NET Core

```
┌─────────────────────────────────────────────────────────────┐
│            MODELOS DE PROGRAMACIÓN ASP.NET CORE             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │      MVC        │  │   Razor Pages   │  │   Web API   │ │
│  │                 │  │                 │  │             │ │
│  │ Model-View-     │  │ Páginas con     │  │ Servicios   │ │
│  │ Controller      │  │ código C#       │  │ REST/gRPC   │ │
│  │                 │  │ embebido        │  │             │ │
│  │ • Aplicaciones  │  │ • Sitios        │  │ • SPAs      │ │
│  │   tradicionales │  │   contenido     │  │ • Mobile    │ │
│  │ • Separación    │  │ • Formularios   │  │ • APIs      │ │
│  │   de concerns   │  │   simples       │  │   públicas  │ │
│  │                 │  │ • Sitios        │  │             │ │
│  │                 │  │   pequeños      │  │             │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
│                                                             │
│  + Blazor (C# en el navegador con WebAssembly)             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## MVC vs Razor Pages

| Característica | MVC | Razor Pages |
|----------------|-----|-------------|
| **Estructura** | Controllers + Views | Páginas con modelo |
| **URL** | `/Controller/Action` | `/Page/Handler` |
| **Mejor para** | Apps complejas | Sitios con formularios |
| **Separación** | Más estricta | Más flexible |
| **Testing** | Más fácil | Un poco más difícil |

### Estructura de Archivos

```
MVC:                              Razor Pages:
Controllers/                      Pages/
├── HomeController.cs             ├── Index.cshtml
│   └── Action: Index()           │   └── @page
│       └── return View();        │       └── @model IndexModel
│                                 │           └── OnGet()
Views/                            ├── Privacy.cshtml
├── Home/                         │   └── @page
│   └── Index.cshtml              └── Contacto.cshtml
│       └── @model ViewModel          └── @page
```

> **En este curso usaremos MVC (más demandado laboralmente)**

---

## 2. Arquitectura ASP.NET Core

```
┌─────────────────────────────────────────────────────────────┐
│                ARQUITECTURA ASP.NET CORE                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │              APLICACIÓN WEB                           │ │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  │ │
│  │  │Controllers│ │  Views  │  │ Models  │  │Services│  │ │
│  │  │         │  │ (.cshtml)│  │         │  │        │  │ │
│  │  └────┬────┘  └─────────┘  └─────────┘  └────┬─────┘  │ │
│  │       │                                      │        │ │
│  │       └────────────────┬─────────────────────┘        │ │
│  │                        │                              │ │
│  │              ┌─────────▼──────────┐                   │ │
│  │              │   Routing System   │                   │ │
│  │              │   (enrutamiento)   │                   │ │
│  │              └─────────┬──────────┘                   │ │
│  └────────────────────────┼──────────────────────────────┘ │
│                           │                                 │
│  ┌────────────────────────▼──────────────────────────────┐ │
│  │              MIDDLEWARE PIPELINE                       │ │
│  │  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐         │ │
│  │  │Log│→│Aut│→│Rou│→│CORS│→│MVC│→│Sta│→│End│         │ │
│  │  │   │ │   │ │   │ │   │ │   │ │tic│ │   │         │ │
│  │  └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘         │ │
│  └────────────────────────────────────────────────────────┘ │
│                           │                                 │
│  ┌────────────────────────▼──────────────────────────────┐ │
│  │              HOST (Kestrel / IIS)                      │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Flujo de una Petición HTTP

```
┌─────────────────────────────────────────────────────────────┐
│              CICLO DE VIDA DE UNA PETICIÓN                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   NAVEGADOR                                                 │
│      │                                                      │
│      │ GET /Clientes/Index                                  │
│      ▼                                                      │
│   ┌─────────────────────────────────────────────────────┐   │
│   │              SERVIDOR WEB (Kestrel)                  │   │
│   │                                                     │   │
│   │  1. Middleware de Autenticación                     │   │
│   │     → ¿Usuario autenticado?                         │   │
│   │                                                     │   │
│   │  2. Routing                                         │   │
│   │     → /Clientes/Index → ClientesController.Index   │   │
│   │                                                     │   │
│   │  3. Model Binding                                   │   │
│   │     → Convertir parámetros URL a tipos C#          │   │
│   │                                                     │   │
│   │  4. Controller Action                               │   │
│   │     → ClientesController.Index()                    │   │
│   │     → Consultar servicio/repositorio                │   │
│   │     → Obtener lista de clientes                     │   │
│   │                                                     │   │
│   │  5. View Rendering                                  │   │
│   │     → Pasar modelo a View (lista de clientes)      │   │
│   │     → Renderizar HTML con Razor                    │   │
│   │                                                     │   │
│   │  6. Response                                        │   │
│   │     → HTML generado                                 │   │
│   └─────────────────────────────────────────────────────┘   │
│      │                                                      │
│      │ HTML                                                 │
│      ▼                                                      │
│   NAVEGADOR muestra página                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Crear Primera Aplicación

### 📦 Comandos CLI

```bash
# Crear nuevo proyecto MVC
dotnet new mvc -n MiPrimeraWeb

# Navegar al proyecto
cd MiPrimeraWeb

# Ejecutar la aplicación
dotnet run

# Abrir navegador en https://localhost:5001
```

### 📁 Estructura de Proyecto MVC

```
MiPrimeraWeb/
├── Controllers/           ← Controladores
│   └── HomeController.cs
├── Models/                ← Modelos de datos
│   └── ErrorViewModel.cs
├── Views/                 ← Vistas Razor
│   ├── Home/
│   │   ├── Index.cshtml
│   │   └── Privacy.cshtml
│   ├── Shared/
│   │   ├── _Layout.cshtml
│   │   └── _ValidationScriptsPartial.cshtml
│   ├── _ViewImports.cshtml
│   └── _ViewStart.cshtml
├── wwwroot/               ← Archivos estáticos
│   ├── css/
│   ├── js/
│   └── lib/               ← Bootstrap, jQuery
├── appsettings.json       ← Configuración
├── Program.cs             ← Punto de entrada
└── MiPrimeraWeb.csproj
```

---

## Program.cs Explicado

```csharp
// Program.cs - Configuración de la aplicación

var builder = WebApplication.CreateBuilder(args);

// ═══════════════════════════════════════════════════════════════
//  SERVICES: Registrar servicios para Inyección de Dependencias
// ═══════════════════════════════════════════════════════════════

// Agregar soporte para Controllers y Views (MVC)
builder.Services.AddControllersWithViews();

// Otros servicios comunes:
// builder.Services.AddDbContext<AppDbContext>();      // Base de datos
// builder.Services.AddIdentity<Usuario, Rol>();       // Autenticación
// builder.Services.AddScoped<IClienteService, ClienteService>(); // Custom

var app = builder.Build();

// ═══════════════════════════════════════════════════════════════
//  MIDDLEWARE PIPELINE: Configurar el pipeline de procesamiento
// ═══════════════════════════════════════════════════════════════

// Configurar middleware según el ambiente
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();  // HTTP Strict Transport Security
}

app.UseHttpsRedirection();    // Redirigir HTTP a HTTPS
app.UseStaticFiles();         // Servir archivos de wwwroot
app.UseRouting();             // Habilitar routing

// Configurar rutas
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");
    // Ej: /Clientes/Detalle/5
    //     /Home/Index (default)

app.Run();  // Iniciar aplicación
```

---

## Mi Primer Controller

```csharp
using Microsoft.AspNetCore.Mvc;
using MiPrimeraWeb.Models;
using System.Diagnostics;

namespace MiPrimeraWeb.Controllers
{
    public class HomeController : Controller
    {
        // GET: /Home/Index (o simplemente /)
        public IActionResult Index()
        {
            return View();
        }

        // GET: /Home/Privacy
        public IActionResult Privacy()
        {
            return View();
        }

        // GET: /Home/Saludo?nombre=Juan
        public IActionResult Saludo(string nombre)
        {
            ViewBag.Nombre = nombre ?? "Visitante";
            ViewBag.Hora = DateTime.Now.ToString("HH:mm");
            return View();
        }

        // Manejo de errores
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel
            {
                RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier
            });
        }
    }
}
```

---

## Vista Razor: Saludo.cshtml

```html
@* Vista Razor para acción Saludo *@
@* Modelo no tipado, usamos ViewBag *@
@{
    ViewData["Title"] = "Saludo Personalizado";
    var mensaje = DateTime.Now.Hour < 12 ? "Buenos días" : "Buenas tardes";
}

<div class="text-center">
    <h1 class="display-4">@mensaje, @ViewBag.Nombre!</h1>
    <p class="lead">Son las @ViewBag.Hora</p>

    @if (DateTime.Now.Hour < 12)
    {
        <div class="alert alert-info">
            🌅 Es hora de empezar el día con energía
        </div>
    }
    else
    {
        <div class="alert alert-warning">
            ☀️ La tarde avanza, ¡sigue así!
        </div>
    }

    <a asp-controller="Home" asp-action="Index" class="btn btn-primary">
        Volver al Inicio
    </a>
</div>
```

---

## Sintaxis Razor

### 📝 C# en HTML

```html
@* RAZOR: Sintaxis para mezclar C# con HTML *@

@* 1. Expresiones implícitas *@
<h1>Hola @Model.Nombre</h1>
<p>Fecha: @DateTime.Now.ToShortDateString()</p>

@* 2. Bloques de código *@
@{
    var titulo = "Bienvenido";
    var hora = DateTime.Now.Hour;
}

@* 3. Estructuras de control *@
@if (hora < 12)
{
    <p>Buenos días</p>
}
else if (hora < 18)
{
    <p>Buenas tardes</p>
}
else
{
    <p>Buenas noches</p>
}

@* 4. Bucles *@
<ul>
@foreach (var item in Model.Lista)
{
    <li>@item.Nombre - @item.Precio.ToString("C")</li>
}
</ul>

@* 5. Comentarios Razor (no aparecen en HTML) *@
@* Este comentario no se ve en el navegador *@

@* 6. Escapar @ *@
<p>Email: usuario@@dominio.com</p>
```

---

## 4. Middleware Pipeline

### 🔧 Configuración del Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                MIDDLEWARE PIPELINE                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   El orden de los middleware es CRÍTICO                     │
│                                                             │
│   ❌ ORDEN INCORRECTO:                                      │
│   app.UseAuthentication();  // Primero intenta autenticar   │
│   app.UseRouting();         // Pero aún no hay routing!     │
│                                                             │
│   ✅ ORDEN CORRECTO:                                        │
│   app.UseExceptionHandler();  // 1. Capturar errores        │
│   app.UseHttpsRedirection();  // 2. Redirigir a HTTPS       │
│   app.UseCors();              // 3. CORS antes de auth      │
│   app.UseStaticFiles();       // 4. Archivos estáticos      │
│   app.UseRouting();           // 5. Routing                 │
│   app.UseAuthentication();    // 6. Quién eres?            │
│   app.UseAuthorization();     // 7. Qué puedes hacer?      │
│   app.MapControllers();       // 8. Endpoints               │
│                                                             │
│   REQUEST → Middleware1 → Middleware2 → ... → Endpoint     │
│                ↓               ↓                           │
│   RESPONSE ← ... ← Middleware2 ← Middleware1               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Middleware Personalizado

```csharp
public class RequestTimingMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<RequestTimingMiddleware> _logger;

    public RequestTimingMiddleware(
        RequestDelegate next,
        ILogger<RequestTimingMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        var stopwatch = Stopwatch.StartNew();
        _logger.LogInformation(
            "→ Request {Method} {Path} started",
            context.Request.Method,
            context.Request.Path);

        await _next(context);  // Pasar al siguiente middleware

        stopwatch.Stop();
        _logger.LogInformation(
            "← Request {Method} {Path} completed in {ElapsedMs}ms - Status {StatusCode}",
            context.Request.Method,
            context.Request.Path,
            stopwatch.ElapsedMilliseconds,
            context.Response.StatusCode);
    }
}

// Registro en Program.cs
app.UseMiddleware<RequestTimingMiddleware>();
```

---

## 5. Inyección de Dependencias

### 🎯 Principio Fundamental

```
┌─────────────────────────────────────────────────────────────┐
│           INYECCIÓN DE DEPENDENCIAS (DI)                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PROBLEMA: Acoplamiento directo                             │
│  ════════════════════════════                                │
│  public class PedidoController : Controller                 │
│  {                                                          │
│      private PedidoRepository _repo = new PedidoRepository();│
│      // ❌ Acoplado a implementación concreta               │
│      // ❌ Difícil de probar                                │
│      // ❌ No se puede cambiar implementación               │
│  }                                                          │
│                                                             │
│  SOLUCIÓN: Inyección de dependencias                        │
│  ═════════════════════════════════                           │
│  public class PedidoController : Controller                 │
│  {                                                          │
│      private readonly IPedidoRepository _repo;              │
│                                                             │
│      public PedidoController(IPedidoRepository repo)        │
│      {                                                      │
│          _repo = repo;  // ← Inyectado por el framework     │
│      }                                                      │
│      // ✅ Desacoplado                                      │
│      // ✅ Fácil de probar (mocks)                          │
│      // ✅ Configurable en un solo lugar                    │
│  }                                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Ciclos de Vida DI

```csharp
// Registro de servicios en Program.cs

// TRANSIENT: Nueva instancia cada vez que se solicita
// Útil para: Servicios ligeros, stateless
builder.Services.AddTransient<IEmailService, EmailService>();

// SCOPED: Una instancia por petición HTTP
// Útil para: DbContext, Unit of Work, repositorios
builder.Services.AddScoped<IClienteRepository, ClienteRepository>();
builder.Services.AddScoped<IClienteService, ClienteService>();

// SINGLETON: Una instancia para toda la aplicación
// Útil para: Configuración, caché, logging
builder.Services.AddSingleton<ICacheService, CacheService>();
```

### Ejemplo Completo

```csharp
public interface IClienteService
{
    Task<List<Cliente>> ObtenerTodos();
    Task<Cliente> ObtenerPorId(int id);
}

public class ClienteService : IClienteService
{
    private readonly IClienteRepository _repository;

    public ClienteService(IClienteRepository repository)
    {
        _repository = repository;
    }

    public Task<List<Cliente>> ObtenerTodos() => _repository.GetAll();
    public Task<Cliente> ObtenerPorId(int id) => _repository.GetById(id);
}

// Registro
builder.Services.AddScoped<IClienteRepository, ClienteRepository>();
builder.Services.AddScoped<IClienteService, ClienteService>();
```

---

## 6. Estructura de Proyecto Recomendada

```
MiAplicacionWeb/
│
├── Controllers/              ← Controladores MVC
│   ├── HomeController.cs
│   ├── ClientesController.cs
│   └── ProductosController.cs
│
├── Models/                   ← Modelos de dominio y ViewModels
│   ├── Entities/             ← Entidades del dominio
│   │   ├── Cliente.cs
│   │   └── Producto.cs
│   └── ViewModels/           ← Modelos para vistas
│       ├── ClienteViewModel.cs
│       └── ProductoViewModel.cs
│
├── Views/                    ← Vistas Razor
│   ├── Clientes/
│   │   ├── Index.cshtml
│   │   ├── Crear.cshtml
│   │   └── Editar.cshtml
│   ├── Productos/
│   └── Shared/
│       └── _Layout.cshtml
│
├── Services/                 ← Lógica de negocio
│   ├── Interfaces/
│   │   └── IClienteService.cs
│   └── Implementations/
│       └── ClienteService.cs
│
├── Data/                     ← Acceso a datos
│   ├── AppDbContext.cs
│   └── Repositories/
│
├── wwwroot/                  ← Archivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
│
├── Program.cs
└── appsettings.json
```

---

## HTTP Methods y Status Codes

### 📡 Métodos HTTP Principales

| Método | Propósito | Ejemplo |
|--------|-----------|---------|
| **GET** | Obtener datos (seguro, idempotente) | `GET /api/productos` |
| **POST** | Crear recurso (no idempotente) | `POST /api/pedidos` |
| **PUT** | Actualizar completo (idempotente) | `PUT /api/clientes/5` |
| **PATCH** | Modificación parcial | `PATCH /api/clientes/5` |
| **DELETE** | Eliminar recurso (idempotente) | `DELETE /api/pedidos/5` |

### 📊 Códigos de Estado HTTP

| Código | Significado |
|--------|-------------|
| **2xx - Éxito** | |
| 200 OK | Petición exitosa |
| 201 Created | Recurso creado |
| 204 No Content | Sin contenido (DELETE exitoso) |
| **3xx - Redirección** | |
| 301 Moved | Redirección permanente |
| 302 Found | Redirección temporal |
| **4xx - Error Cliente** | |
| 400 Bad Request | Petición mal formada |
| 401 Unauthorized | No autenticado |
| 403 Forbidden | Autenticado pero sin permiso |
| 404 Not Found | Recurso no encontrado |
| **5xx - Error Servidor** | |
| 500 Error | Error interno del servidor |

---

## Tipos de Action Results

```csharp
public class ProductosController : Controller
{
    // 1. ViewResult - Renderiza vista HTML
    public IActionResult Index()
    {
        var productos = _servicio.ObtenerTodos();
        return View(productos);
    }

    // 2. RedirectToActionResult - Redirección
    [HttpPost]
    public IActionResult Crear(ProductoViewModel model)
    {
        if (!ModelState.IsValid)
            return View(model);

        _servicio.Crear(model);
        return RedirectToAction("Index");
    }

    // 3. JsonResult - Retorna JSON (para APIs)
    [HttpGet("api/productos")]
    public IActionResult ObtenerJson()
    {
        return Json(_servicio.ObtenerTodos());
    }

    // 4. ContentResult - Texto plano
    public IActionResult Texto()
    {
        return Content("Hola desde el servidor", "text/plain");
    }

    // 5. FileResult - Descarga de archivo
    public IActionResult Descargar()
    {
        byte[] fileBytes = System.IO.File.ReadAllBytes(@"ruta\archivo.pdf");
        return File(fileBytes, "application/pdf", "reporte.pdf");
    }

    // 6. NotFoundResult - 404
    public IActionResult Detalle(int id)
    {
        var producto = _servicio.ObtenerPorId(id);
        if (producto == null)
            return NotFound();
        return View(producto);
    }

    // 7. StatusCodeResult - Código personalizado
    public IActionResult NoAutorizado()
    {
        return StatusCode(403);
    }
}
```

---

## Tag Helpers

### 🏷️ HTML con Inteligencia de Razor

```html
@* Tag Helpers: atributos especiales que se procesan en el servidor *@

@* 1. ANCHOR TAG HELPER *@
<a asp-controller="Productos" asp-action="Detalle" asp-route-id="5">
    Ver producto
</a>

@* 2. FORM TAG HELPER *@
<form asp-controller="Productos" asp-action="Crear" method="post">
</form>

@* 3. INPUT TAG HELPER *@
<input asp-for="Nombre" class="form-control" />

@* 4. LABEL TAG HELPER *@
<label asp-for="Nombre"></label>

@* 5. VALIDATION MESSAGE *@
<span asp-validation-for="Nombre" class="text-danger"></span>

@* 6. SELECT TAG HELPER *@
<select asp-for="CategoriaId" asp-items="Model.Categorias"></select>

@* 7. TEXTAREA TAG HELPER *@
<textarea asp-for="Descripcion" rows="4"></textarea>
```

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **ASP.NET Core** | Framework web multiplataforma de Microsoft |
| **MVC** | Model-View-Controller, patrón de diseño |
| **Controller** | Recibe peticiones, orquesta lógica |
| **View** | Presentación con sintaxis Razor |
| **Middleware** | Pipeline de procesamiento de peticiones |
| **DI** | Inyección de dependencias para desacoplamiento |
| **Transient** | Nueva instancia cada vez |
| **Scoped** | Una instancia por petición HTTP |
| **Singleton** | Una instancia global |
| **HTTP Methods** | GET, POST, PUT, PATCH, DELETE |
| **Status Codes** | 2xx (éxito), 3xx (redirección), 4xx (cliente), 5xx (servidor) |
| **Tag Helpers** | Atributos Razor que generan HTML dinámico |

---

## Ejercicio Práctico

### 📋 Crear página de información

**Tareas:**

1. Crear nuevo Controller "InformacionController"
   - Acción "HoraActual" que muestre hora del servidor
   - Acción "DatosServidor" que muestre:
     - Nombre del servidor
     - Framework (.NET 8)
     - Ambiente (Development/Production)

2. Crear las vistas correspondientes
   - Usar Razor para mostrar datos dinámicos
   - Aplicar clases de Bootstrap para estilos

3. Configurar enlace en el menú de navegación
   - Editar Views/Shared/_Layout.cshtml
   - Agregar enlace al menú

4. Probar inyección de dependencias
   - Crear interfaz IServicioHora
   - Implementar ServicioHoraReal
   - Inyectar en el controller

---

## 🚀 Próxima Clase: HTML5 y Bootstrap

| Tema | Descripción |
|------|-------------|
| **HTML5 semántico** | Estructura: header, nav, main, section, footer |
| **Formularios modernos** | Inputs, validación HTML5 |
| **Bootstrap 5** | Grid, componentes, utilidades |
| **Responsive Design** | Mobile-first, breakpoints |
| **Layouts** | Shared layouts, partial views |

---

# ¡Gracias!
## ¿Preguntas?

**"ASP.NET Core: Un framework, infinitas posibilidades"**

**UNAULA - Ingeniería Informática - 2026-I**
