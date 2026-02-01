# Teoría - ASP.NET Core

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es ASP.NET Core?

Framework web **cross-platform**, moderno y de alto rendimiento.

### Arquitectura

```
┌─────────────────────────────────┐
│       ASP.NET CORE APP          │
├─────────────────────────────────┤
│  Middleware Pipeline            │
│  ┌─────────────────────────────┐│
│  │ Exception Handler           ││
│  │ HTTPS Redirection           ││
│  │ Static Files                ││
│  │ Routing                     ││
│  │ Authentication              ││
│  │ Authorization               ││
│  │ Custom Middleware           ││
│  │ Endpoints (MVC/Razor/API)   ││
│  └─────────────────────────────┘│
├─────────────────────────────────┤
│  Kestrel Web Server            │
└─────────────────────────────────┘
```

### Middleware Pipeline

```csharp
app.UseExceptionHandler("/Error");
app.UseHsts();
app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();
app.MapRazorPages();
app.Run();
```

---

## 2. Crear Proyecto

```bash
# Razor Pages
dotnet new webapp -n MiAppWeb

# MVC
dotnet new mvc -n MiMvcApp

# Web API
dotnet new webapi -n MiApi
```

---

**Última actualización:** 2026-02-01
