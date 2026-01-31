---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 3'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<!--
IMÁGENES GENERADAS:
- clase-11-validacion-formularios.png: Validación de formularios en ASP.NET con Data Annotations
-->

# Clase 11: Formularios, Validación y Sesiones
## Validación de datos y estado en aplicaciones web

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Implementar** validación de datos con Data Annotations
2. **Configurar** validación en cliente y servidor
3. **Utilizar** TempData, ViewBag y ViewData
4. **Gestionar** sesiones y cookies
5. **Implementar** upload de archivos

**Duración:** 90 minutos

---

## Agenda

1. Validación con Data Annotations (20 min)
2. Validación cliente vs servidor (10 min)
3. TempData y mensajes flash (10 min)
4. Sesiones y Cookies (15 min)
5. Upload de archivos (15 min)
6. Ejercicio integrador (20 min)

---

## 1. Validación con Data Annotations

### Atributos de validación en .NET

```csharp
using System.ComponentModel.DataAnnotations;

public class EstudianteViewModel
{
    // VALIDACIÓN BÁSICA
    
    [Required(ErrorMessage = "El código es obligatorio")]
    [StringLength(10, MinimumLength = 5, 
        ErrorMessage = "El código debe tener entre 5 y 10 caracteres")]
    [Display(Name = "Código Estudiantil")]
    public string Codigo { get; set; }
    
    [Required]
    [StringLength(50)]
    public string Nombre { get; set; }
    
    [Required]
    [StringLength(50)]
    public string Apellido { get; set; }
    
    // VALIDACIÓN DE EMAIL
    [Required]
    [EmailAddress(ErrorMessage = "El formato del email no es válido")]
    [Display(Name = "Correo Electrónico")]
    public string Email { get; set; }
    
    // VALIDACIÓN NUMÉRICA
    [Range(18, 100, ErrorMessage = "La edad debe estar entre 18 y 100 años")]
    public int Edad { get; set; }
    
    [Range(0.0, 5.0, ErrorMessage = "El promedio debe estar entre 0.0 y 5.0")]
    [DisplayFormat(DataFormatString = "{0:F2}")]
    public double Promedio { get; set; }
    
    // VALIDACIÓN DE PATRÓN (Regex)
    [Required]
    [RegularExpression(@"^\d{10}$", 
        ErrorMessage = "El teléfono debe tener 10 dígitos numéricos")]
    [Display(Name = "Teléfono Celular")]
    public string Telefono { get; set; }
    
    // VALIDACIÓN DE FECHAS
    [DataType(DataType.Date)]
    [Display(Name = "Fecha de Nacimiento")]
    [FechaPasada(ErrorMessage = "La fecha debe ser en el pasado")]  // Custom
    public DateTime FechaNacimiento { get; set; }
    
    // COMPARACIÓN
    [Required]
    [DataType(DataType.Password)]
    public string Password { get; set; }
    
    [DataType(DataType.Password)]
    [Compare("Password", ErrorMessage = "Las contraseñas no coinciden")]
    [Display(Name = "Confirmar Contraseña")]
    public string ConfirmarPassword { get; set; }
}
```

---

## Data Annotations Disponibles

### Lista completa de atributos

```
┌─────────────────────────────────────────────────────────────┐
│           DATA ANNOTATIONS DE VALIDACIÓN                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  VALIDACIÓN DE REQUERIMIENTO                                │
│  • [Required]              - Campo obligatorio             │
│  • [Required(ErrorMessage="...")] - Con mensaje personal   │
│                                                             │
│  VALIDACIÓN DE LONGITUD                                     │
│  • [StringLength(50)]      - Máximo 50 caracteres          │
│  • [StringLength(50, MinimumLength=5)] - Min y max         │
│  • [MinLength(5)]          - Mínimo 5 caracteres           │
│  • [MaxLength(100)]        - Máximo 100 caracteres         │
│                                                             │
│  VALIDACIÓN NUMÉRICA                                        │
│  • [Range(0, 100)]         - Entre 0 y 100                 │
│  • [Range(0.0, 5.0)]       - Decimales                     │
│                                                             │
│  VALIDACIÓN DE FORMATO                                      │
│  • [EmailAddress]          - Formato email                 │
│  • [Phone]                 - Formato teléfono              │
│  • [Url]                   - Formato URL                   │
│  • [CreditCard]            - Formato tarjeta de crédito    │
│  • [RegularExpression(@"...")] - Patrón regex              │
│                                                             │
│  VALIDACIÓN DE COMPARACIÓN                                  │
│  • [Compare("OtraPropiedad")] - Debe coincidir con otra    │
│                                                             │
│  VALIDACIÓN PERSONALIZADA                                   │
│  • Crear clase que herede de ValidationAttribute           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Validación Personalizada

### Crear atributo custom

```csharp
// Validación personalizada: Fecha debe ser en el pasado
public class FechaPasadaAttribute : ValidationAttribute
{
    protected override ValidationResult IsValid(object value, 
        ValidationContext validationContext)
    {
        if (value is DateTime fecha)
        {
            if (fecha >= DateTime.Today)
            {
                return new ValidationResult(ErrorMessage ?? 
                    "La fecha debe ser en el pasado");
            }
        }
        return ValidationResult.Success;
    }
}

// Uso
public class EstudianteViewModel
{
    [FechaPasada(ErrorMessage = "La fecha de nacimiento debe ser en el pasado")]
    public DateTime FechaNacimiento { get; set; }
}

// Otra validación: Mayor de edad
public class MayorDeEdadAttribute : ValidationAttribute
{
    private readonly int _edadMinima;
    
    public MayorDeEdadAttribute(int edadMinima = 18)
    {
        _edadMinima = edadMinima;
    }
    
    protected override ValidationResult IsValid(object value, 
        ValidationContext validationContext)
    {
        if (value is DateTime fechaNacimiento)
        {
            var edad = DateTime.Today.Year - fechaNacimiento.Year;
            if (fechaNacimiento.Date > DateTime.Today.AddYears(-edad))
                edad--;
            
            if (edad < _edadMinima)
            {
                return new ValidationResult(
                    $"Debe tener al menos {_edadMinima} años");
            }
        }
        return ValidationResult.Success;
    }
}
```

---

## Validación en el Servidor

### ModelState.IsValid

```csharp
[HttpPost]
public async Task<IActionResult> Crear(EstudianteViewModel model)
{
    // Validación automática basada en Data Annotations
    if (!ModelState.IsValid)
    {
        // Si hay errores, retornar la vista con el modelo
        // Los errores se mostrarán automáticamente
        return View(model);
    }
    
    // Validación de negocio adicional
    var existe = await _service.ExisteCodigoAsync(model.Codigo);
    if (existe)
    {
        ModelState.AddModelError("Codigo", 
            "Ya existe un estudiante con este código");
        return View(model);
    }
    
    // Guardar
    await _service.CrearAsync(model);
    return RedirectToAction(nameof(Index));
}
```

---

## 2. Validación Cliente vs Servidor

### Doble validación

```
┌─────────────────────────────────────────────────────────────┐
│              VALIDACIÓN CLIENTE vs SERVIDOR                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   NAVEGADOR                    SERVIDOR                     │
│      │                            │                         │
│      │  1. Usuario escribe        │                         │
│      │     datos en formulario    │                         │
│      │                            │                         │
│      │  2. JavaScript valida      │                         │
│      │     (jQuery Validation)    │                         │
│      │                            │                         │
│      │◄─ 3. Si es inválido,       │                         │
│      │     muestra error sin      │                         │
│      │     enviar al servidor     │                         │
│      │                            │                         │
│      │  4. Si pasa validación     │                         │
│      │     cliente, envía POST    │                         │
│      ├────────────────────────────►                         │
│      │                            │ 5. ModelState valida    │
│      │                            │    (Data Annotations)   │
│      │                            │                         │
│      │◄─────────────────────────── 6. Si inválido, retorna  │
│      │                            │    vista con errores    │
│      │                            │                         │
│      │                            │ 7. Si válido, procesa   │
│      │                            │    y guarda             │
│      │                            │                         │
│                                                             │
│   ⚠️ IMPORTANTE:                                             │
│   • Validación cliente = UX mejor (rápida)                  │
│   • Validación servidor = Seguridad (obligatoria)           │
│   • Nunca confíe solo en validación cliente                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Configurar Validación Cliente

### jQuery Validation

```html
<!-- Views/Shared/_ValidationScriptsPartial.cshtml -->

<script src="~/lib/jquery/dist/jquery.min.js"></script>
<script src="~/lib/jquery-validation/dist/jquery.validate.min.js"></script>
<script src="~/lib/jquery-validation-unobtrusive/jquery.validate.unobtrusive.min.js">
</script>

<!-- En la vista -->
<form asp-action="Crear" method="post">
    <div class="form-group">
        <label asp-for="Email"></label>
        <input asp-for="Email" class="form-control" />
        <span asp-validation-for="Email" class="text-danger"></span>
    </div>
    
    <button type="submit" class="btn btn-primary">Guardar</button>
</form>

@section Scripts {
    @{await Html.RenderPartialAsync("_ValidationScriptsPartial");}
}
```

```javascript
// jQuery Validation genera automáticamente:
// - Validación de campos required
// - Validación de email con regex
// - Validación de rango numérico
// - Mensajes de error en español (con configuración)
```

---

## 3. TempData y Mensajes Flash

### Pasar datos entre acciones

```
┌─────────────────────────────────────────────────────────────┐
│              FORMAS DE PASAR DATOS EN MVC                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ViewData / ViewBag                                        │
│   ─────────────────                                         │
│   • Alcance: Una sola petición (request)                   │
│   • Uso: Controller → View                                  │
│   • Ejemplo: ViewBag.Mensaje = "Hola"                       │
│                                                             │
│   TempData                                                  │
│   ────────                                                  │
│   • Alcance: Persiste hasta la siguiente petición          │
│   • Uso: Controller → Redirect → Controller/View           │
│   • Ejemplo: TempData["Mensaje"] = "Guardado"               │
│                                                             │
│   Sesión (Session)                                          │
│   ─────────────────                                         │
│   • Alcance: Múltiples peticiones del mismo usuario        │
│   • Uso: Datos persistentes durante la sesión              │
│   • Ejemplo: Session["UsuarioId"] = 123                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Usando TempData

### Mensajes de confirmación

```csharp
[HttpPost]
public async Task<IActionResult> Crear(EstudianteViewModel model)
{
    if (!ModelState.IsValid)
        return View(model);
    
    await _service.CrearAsync(model);
    
    // Mensaje que persistirá después del Redirect
    TempData["MensajeExito"] = "Estudiante creado exitosamente";
    TempData["TipoMensaje"] = "success";  // Para Bootstrap alert
    
    return RedirectToAction(nameof(Index));
}

[HttpPost]
public async Task<IActionResult> Eliminar(int id)
{
    try
    {
        await _service.EliminarAsync(id);
        TempData["MensajeExito"] = "Estudiante eliminado correctamente";
        TempData["TipoMensaje"] = "success";
    }
    catch (Exception ex)
    {
        TempData["MensajeError"] = "No se pudo eliminar el estudiante";
        TempData["TipoMensaje"] = "danger";
    }
    
    return RedirectToAction(nameof(Index));
}
```

```html
<!-- Views/Estudiantes/Index.cshtml - Mostrar mensajes -->
@{
    var mensaje = TempData["MensajeExito"] ?? TempData["MensajeError"];
    var tipo = TempData["TipoMensaje"] ?? "info";
}

@if (mensaje != null)
{
    <div class="alert alert-@tipo alert-dismissible fade show" role="alert">
        @mensaje
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
}

<!-- O usando Partial View -->
<partial name="_Mensajes" />
```

---

## 4. Sesiones y Cookies

### Configuración de sesiones

```csharp
// Program.cs - Configurar servicio de sesiones

// Agregar servicio de sesiones
builder.Services.AddDistributedMemoryCache();  // Almacenamiento en memoria
builder.Services.AddSession(options =>
{
    options.IdleTimeout = TimeSpan.FromMinutes(30);  // Tiempo de expiración
    options.Cookie.HttpOnly = true;  // Solo accesible por HTTP
    options.Cookie.IsEssential = true;  // Necesaria para GDPR
});

var app = builder.Build();

// Usar sesiones (antes de MapControllers)
app.UseSession();
app.MapControllers();
```

---

## Usando Sesiones

### Almacenar y recuperar datos

```csharp
public class AccountController : Controller
{
    // Guardar en sesión
    public IActionResult Login(LoginViewModel model)
    {
        // Validar credenciales...
        
        // Guardar en sesión
        HttpContext.Session.SetInt32("UsuarioId", usuario.Id);
        HttpContext.Session.SetString("UsuarioNombre", usuario.Nombre);
        HttpContext.Session.SetString("UsuarioEmail", usuario.Email);
        
        // Guardar objeto completo (serializado)
        var usuarioJson = JsonSerializer.Serialize(usuario);
        HttpContext.Session.SetString("UsuarioCompleto", usuarioJson);
        
        return RedirectToAction("Index", "Home");
    }
    
    // Leer de sesión
    public IActionResult Perfil()
    {
        var usuarioId = HttpContext.Session.GetInt32("UsuarioId");
        var usuarioNombre = HttpContext.Session.GetString("UsuarioNombre");
        
        if (usuarioId == null)
        {
            return RedirectToAction("Login");
        }
        
        // Recuperar objeto
        var usuarioJson = HttpContext.Session.GetString("UsuarioCompleto");
        var usuario = JsonSerializer.Deserialize<Usuario>(usuarioJson);
        
        return View(usuario);
    }
    
    // Cerrar sesión
    public IActionResult Logout()
    {
        HttpContext.Session.Clear();  // Limpiar toda la sesión
        return RedirectToAction("Index", "Home");
    }
}
```

---

## Cookies

### Manipulación directa

```csharp
public class PreferenciasController : Controller
{
    // Establecer cookie
    public IActionResult SetTema(string tema)
    {
        // Cookie simple
        Response.Cookies.Append("Tema", tema, new CookieOptions
        {
            Expires = DateTime.Now.AddDays(30),  // Expira en 30 días
            HttpOnly = false,  // Accesible por JavaScript
            Secure = true,     // Solo HTTPS
            SameSite = SameSiteMode.Strict
        });
        
        return RedirectToAction("Index");
    }
    
    // Leer cookie
    public IActionResult Index()
    {
        var tema = Request.Cookies["Tema"] ?? "claro";
        ViewBag.Tema = tema;
        return View();
    }
    
    // Eliminar cookie
    public IActionResult EliminarTema()
    {
        Response.Cookies.Delete("Tema");
        return RedirectToAction("Index");
    }
}
```

---

## 5. Upload de Archivos

### IFormFile

```html
<!-- Vista con formulario para subir archivo -->
<form asp-action="SubirFoto" method="post" enctype="multipart/form-data">
    <div class="mb-3">
        <label class="form-label">Foto del Estudiante</label>
        <input type="file" name="archivo" class="form-control" 
               accept=".jpg,.jpeg,.png" />
        <div class="form-text">Formatos permitidos: JPG, PNG (máx. 2MB)</div>
    </div>
    <button type="submit" class="btn btn-primary">Subir</button>
</form>
```

```csharp
[HttpPost]
public async Task<IActionResult> SubirFoto(IFormFile archivo, int estudianteId)
{
    if (archivo == null || archivo.Length == 0)
    {
        ModelState.AddModelError("", "No se seleccionó ningún archivo");
        return View();
    }
    
    // Validaciones
    var extensionesPermitidas = new[] { ".jpg", ".jpeg", ".png" };
    var extension = Path.GetExtension(archivo.FileName).ToLowerInvariant();
    
    if (!extensionesPermitidas.Contains(extension))
    {
        ModelState.AddModelError("", "Formato de archivo no válido");
        return View();
    }
    
    if (archivo.Length > 2 * 1024 * 1024)  // 2MB
    {
        ModelState.AddModelError("", "El archivo es demasiado grande (máx. 2MB)");
        return View();
    }
    
    // Generar nombre único
    var nombreArchivo = $"{estudianteId}_{Guid.NewGuid()}{extension}";
    var rutaCarpeta = Path.Combine(_environment.WebRootPath, "uploads", "fotos");
    var rutaCompleta = Path.Combine(rutaCarpeta, nombreArchivo);
    
    // Crear carpeta si no existe
    if (!Directory.Exists(rutaCarpeta))
        Directory.CreateDirectory(rutaCarpeta);
    
    // Guardar archivo
    using (var stream = new FileStream(rutaCompleta, FileMode.Create))
    {
        await archivo.CopyToAsync(stream);
    }
    
    // Guardar ruta en base de datos
    await _service.ActualizarFotoAsync(estudianteId, $"/uploads/fotos/{nombreArchivo}");
    
    TempData["Mensaje"] = "Foto subida correctamente";
    return RedirectToAction("Detalles", new { id = estudianteId });
}
```

---

## Múltiples Archivos

### Subir varios archivos

```html
<form asp-action="SubirDocumentos" method="post" enctype="multipart/form-data">
    <input type="file" name="archivos" multiple class="form-control" />
    <button type="submit" class="btn btn-primary">Subir Documentos</button>
</form>
```

```csharp
[HttpPost]
public async Task<IActionResult> SubirDocumentos(List<IFormFile> archivos)
{
    foreach (var archivo in archivos)
    {
        if (archivo.Length > 0)
        {
            var nombre = Path.GetFileName(archivo.FileName);
            var ruta = Path.Combine(_environment.WebRootPath, "uploads", nombre);
            
            using (var stream = new FileStream(ruta, FileMode.Create))
            {
                await archivo.CopyToAsync(stream);
            }
        }
    }
    
    TempData["Mensaje"] = $"{archivos.Count} archivos subidos";
    return RedirectToAction("Index");
}
```

---

## 6. Ejercicio Integrador

### Sistema de registro completo

```
EJERCICIO: Formulario de Inscripción

Crear sistema de inscripción de estudiantes con:

1. ViewModel con validaciones:
   - Código: requerido, 5-10 caracteres, único
   - Nombre: requerido, máx 50 caracteres
   - Email: requerido, formato válido
   - FechaNacimiento: requerido, mayor de 15 años
   - Carrera: seleccionar de dropdown
   - Foto: opcional, solo JPG/PNG, máx 1MB

2. Controller con:
   - GET: mostrar formulario
   - POST: validar, guardar, mostrar mensaje éxito
   - Validación de código único

3. Vista con:
   - Formulario Bootstrap estilizado
   - Validación cliente activada
   - Vista previa de foto seleccionada (JS)
   - Mensajes de error específicos por campo

4. Sesión:
   - Guardar último estudiante registrado
   - Mostrar en barra superior "Último registro: [Nombre]"

5. Funcionalidades extra:
   - Exportar lista a Excel (simulado)
   - Filtrar por carrera (session)
```

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **Data Annotations** | Atributos para validación de modelos |
| **ModelState** | Estado de validación en servidor |
| **jQuery Validation** | Validación en cliente |
| **TempData** | Datos persistentes hasta siguiente petición |
| **Session** | Datos persistentes durante sesión de usuario |
| **Cookies** | Almacenamiento en navegador |
| **IFormFile** | Manejo de archivos subidos |

---

## Unidad 3 Completada ✅

### Resumen Unidad 3: Desarrollo Web

```
CLASES CREADAS:

Clase 8: Introducción a ASP.NET Core
  • Arquitectura, middleware, DI
  
Clase 9: HTML5 y Bootstrap
  • Semántica HTML5, componentes Bootstrap
  
Clase 10: MVC y Razor Pages
  • Patrón MVC, Routing, Tag Helpers
  
Clase 11: Formularios, Validación y Sesiones
  • Data Annotations, TempData, Session, Upload
```

---

## Próxima Unidad

### Unidad 4: Manejo de Persistencia

```
CLASES 12-14: ADO.NET Y PERSISTENCIA

• Clase 12: Introducción a ADO.NET
  - SqlConnection, SqlCommand, SqlDataReader
  - CRUD básico
  
• Clase 13: Entity Framework Core
  - DbContext, DbSet
  - Migrations
  - LINQ to Entities
  
• Clase 14: Persistencia en archivos
  - Lectura/escritura de archivos
  - JSON, XML
  - CSV
```

---

# ¡Gracias!
## ¿Preguntas?

**Unidad 3 completada: 4/4 clases ✅**

**UNAULA - Ingeniería Informática - 2026-I**
