# Código - ASP.NET Core

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Primer Proyecto Razor Pages

### PageModel

```csharp
public class IndexModel : PageModel
{
    private readonly ILogger<IndexModel> _logger;

    public IndexModel(ILogger<IndexModel> logger)
    {
        _logger = logger;
    }

    public string Mensaje { get; set; } = "Hola ASP.NET Core!";

    public void OnGet()
    {
        _logger.LogInformation("Cargando página Index");
    }

    public IActionResult OnPost()
    {
        Mensaje = $"Formulario enviado: {Request.Form["nombre"]}";
        return Page();
    }
}
```

### Razor View

```cshtml
@page
@model IndexModel
@{
    ViewData["Title"] = "Home";
}

<h1>@Model.Mensaje</h1>

<form method="post">
    <input name="nombre" placeholder="Tu nombre" />
    <button type="submit">Enviar</button>
</form>
```

---

## 2. Middleware Personalizado

```csharp
public class LoggingMiddleware
{
    private readonly RequestDelegate _next;

    public LoggingMiddleware(RequestDelegate next)
    {
        _next = next;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        Console.WriteLine($"Request: {context.Request.Path}");
        await _next(context);
        Console.WriteLine($"Response: {context.Response.StatusCode}");
    }
}

// En Program.cs
app.UseMiddleware<LoggingMiddleware>();
```

---

**Última actualización:** 2026-02-01
