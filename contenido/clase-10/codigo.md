# Código - MVC y Razor Pages

**IF0100 - Lenguaje de Programación OO II**

---

## 1. CRUD Completo con Razor Pages

### PageModel (Create.cshtml.cs)

```csharp
public class CreateModel : PageModel
{
    private readonly AppDbContext _context;

    public CreateModel(AppDbContext context)
    {
        _context = context;
    }

    [BindProperty]
    public Estudiante Estudiante { get; set; }

    public void OnGet() { }

    public async Task<IActionResult> OnPostAsync()
    {
        if (!ModelState.IsValid)
            return Page();

        _context.Estudiantes.Add(Estudiante);
        await _context.SaveChangesAsync();

        return RedirectToPage("./Index");
    }
}
```

### Razor View (Create.cshtml)

```cshtml
@page
@model CreateModel
@{
    ViewData["Title"] = "Nuevo Estudiante";
}

<h1>Nuevo Estudiante</h1>

<form method="post">
    <div asp-validation-summary="All" class="text-danger"></div>

    <div class="mb-3">
        <label asp-for="Estudiante.Nombre" class="form-label"></label>
        <input asp-for="Estudiante.Nombre" class="form-control" />
        <span asp-validation-for="Estudiante.Nombre" class="text-danger"></span>
    </div>

    <div class="mb-3">
        <label asp-for="Estudiante.Email" class="form-label"></label>
        <input asp-for="Estudiante.Email" class="form-control" />
        <span asp-validation-for="Estudiante.Email" class="text-danger"></span>
    </div>

    <button type="submit" class="btn btn-primary">Guardar</button>
    <a asp-page="./Index" class="btn btn-secondary">Cancelar</a>
</form>
```

---

## 2. MVC Controller

```csharp
public class ProductosController : Controller
{
    private readonly AppDbContext _context;

    public ProductosController(AppDbContext context)
    {
        _context = context;
    }

    // GET: Productos
    public async Task<IActionResult> Index()
    {
        return View(await _context.Productos.ToListAsync());
    }

    // GET: Productos/Details/5
    public async Task<IActionResult> Details(int? id)
    {
        if (id == null) return NotFound();

        var producto = await _context.Productos.FirstOrDefaultAsync(m => m.Id == id);
        if (producto == null) return NotFound();

        return View(producto);
    }

    // GET: Productos/Create
    public IActionResult Create() => View();

    // POST: Productos/Create
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Create([Bind("Id,Nombre,Precio")] Producto producto)
    {
        if (ModelState.IsValid)
        {
            _context.Add(producto);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }
        return View(producto);
    }
}
```

---

**Última actualización:** 2026-02-01
