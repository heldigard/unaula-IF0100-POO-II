# Teoría - Formularios, Validación y Sesiones

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Validaciones con Data Annotations

```csharp
public class RegistroViewModel
{
    [Required(ErrorMessage = "El nombre es requerido")]
    [StringLength(100, MinimumLength = 3)]
    public string Nombre { get; set; }

    [Required]
    [EmailAddress]
    public string Email { get; set; }

    [Required]
    [StringLength(100, MinimumLength = 6)]
    [DataType(DataType.Password)]
    public string Clave { get; set; }

    [Compare("Clave", ErrorMessage = "Las claves no coinciden")]
    [DataType(DataType.Password)]
    public string ConfirmarClave { get; set; }

    [Range(18, 120)]
    public int Edad { get; set; }
}
```

---

## 2. Estado y Sesiones

### TempData

```csharp
// Dura una redirección
TempData["Mensaje"] = "Operación exitosa";
```

### Session

```csharp
// Requiere: builder.Services.AddSession();
// Dura toda la sesión del usuario
HttpContext.Session.SetString("Usuario", "Juan");
var usuario = HttpContext.Session.GetString("Usuario");
```

### Cookies

```csharp
// Cookies persistentes
Response.Cookies.Append("UltimaVisita", DateTime.Now.ToString(),
    new CookieOptions { Expires = DateTime.Now.AddDays(30) });
```

---

**Última actualización:** 2026-02-01
