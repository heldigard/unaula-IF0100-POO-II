# Código - Formularios y Sesiones

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Formulario con Validación

### PageModel

```csharp
public class RegistroModel : PageModel
{
    [BindProperty]
    public RegistroViewModel Input { get; set; }

    public void OnGet() { }

    public IActionResult OnPost()
    {
        if (!ModelState.IsValid)
            return Page();

        // Procesar registro...
        TempData["Mensaje"] = "Registro exitoso";
        return RedirectToPage("./Confirmacion");
    }
}
```

### Razor View

```cshtml
@page
@model RegisterModel
<form method="post">
    <div class="mb-3">
        <label asp-for="Input.Nombre" class="form-label"></label>
        <input asp-for="Input.Nombre" class="form-control" />
        <span asp-validation-for="Input.Nombre" class="text-danger"></span>
    </div>

    <div class="mb-3">
        <label asp-for="Input.Email" class="form-label"></label>
        <input asp-for="Input.Email" class="form-control" />
        <span asp-validation-for="Input.Email" class="text-danger"></span>
    </div>

    <div class="mb-3">
        <label asp-for="Input.Clave" class="form-label"></label>
        <input asp-for="Input.Clave" class="form-control" type="password" />
        <span asp-validation-for="Input.Clave" class="text-danger"></span>
    </div>

    <button type="submit" class="btn btn-primary">Registrarse</button>
</form>

@section Scripts {
    <partial name="_ValidationScriptsPartial" />
}
```

---

## 2. Autenticación con Session

```csharp
public class LoginModel : PageModel
{
    public IActionResult OnPost(string email, string clave)
    {
        // Validar credenciales...
        if (ValidarCredenciales(email, clave))
        {
            HttpContext.Session.SetString("UsuarioEmail", email);
            HttpContext.Session.SetInt32("UsuarioId", usuarioId);

            return RedirectToPage("./Index");
        }

        ModelState.AddModelError("", "Credenciales inválidas");
        return Page();
    }

    public IActionResult OnPostLogout()
    {
        HttpContext.Session.Clear();
        return RedirectToPage("./Login");
    }
}
```

---

**Última actualización:** 2026-02-01
