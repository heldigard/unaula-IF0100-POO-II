# Teoría - MVC y Razor Pages

**IF0100 - Lenguaje de Programación OO II**

---

## MVC vs Razor Pages

| Aspecto | MVC | Razor Pages |
|---------|-----|-------------|
| **Organización** | Controllers + Views | Pages |
| **Complejidad** | Mayor | Menor |
| **Uso ideal** | APIs, apps complejas | CRUD simple, páginas enfocadas |

---

## MVC Pattern

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Browser  │────▶│ Controller│────▶│  Model   │
└──────────┘     └────┬─────┘     └──────────┘
                      │
                      ▼
                 ┌──────────┐
                 │  View    │
                 └────┬─────┘
                      │
                      ▼
                 ┌──────────┐
                 │ Browser  │
                 └──────────┘
```

### Controller

```csharp
public class ProductosController : Controller
{
    public IActionResult Index() => View();
    public IActionResult Details(int id) => View();
    [HttpGet]
    public IActionResult Create() => View();
    [HttpPost]
    public IActionResult Create(Producto producto) { ... }
}
```

---

## Razor Pages

```
Producto.cshtml + Producto.cshtml.cs
├─ OnGet()    ← GET /Producto
├─ OnPost()   ← POST /Producto
└─ Modelo de página
```

### PageModel

```csharp
public class CreateModel : PageModel
{
    [BindProperty]
    public Producto Producto { get; set; }

    public void OnGet() { }

    public IActionResult OnPost()
    {
        if (!ModelState.IsValid) return Page();
        // Guardar...
        return RedirectToPage("./Index");
    }
}
```

---

**Última actualización:** 2026-02-01
