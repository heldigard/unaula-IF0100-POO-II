# Teoría - BDD y SpecFlow

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es BDD?

**Behavior Driven Development (BDD)** evoluciona TDD enfocándose en **comportamiento** del sistema desde la perspectiva del usuario.

### Gherkin: Given-When-Then

```gherkin
Feature: Calculadora
  Scenario: Sumar dos números
    Given tengo una calculadora
    When ingreso 5 y 3
    Then el resultado debe ser 8
```

### Componentes

| Palabra Clave | Propósito |
|---------------|-----------|
| **Feature** | Historia de usuario |
| **Scenario** | Caso específico |
| **Given** | Contexto inicial |
| **When** | Acción |
| **Then** | Resultado esperado |
| **And** | Adicionales |

---

## 2. SpecFlow en .NET

### Instalación

```bash
dotnet add package SpecFlow.xUnit
dotnet add package SpecFlow.Tools.MsBuild.Generation
```

### Ejemplo Completo

```gherkin
Feature: Autenticación
  Como usuario
  Quiero iniciar sesión
  Para acceder al sistema

  Scenario: Login exitoso
    Given un usuario registrado con email "test@email.com" y clave "123456"
    When ingreso las credenciales correctas
    Then debo ser redirigido al dashboard
    And debo ver un mensaje de bienvenida
```

### Step Definitions

```csharp
[Binding]
public class AutenticacionSteps
{
    private Usuario _usuario;
    private LoginResult _resultado;

    [Given(@"un usuario registrado con email ""(.*)"" y clave ""(.*)""")]
    public void GivenUsuarioRegistrado(string email, string clave)
    {
        _usuario = new Usuario { Email = email, Clave = clave };
    }

    [When(@"ingreso las credenciales correctas")]
    public void WhenIngresoCredenciales()
    {
        var servicio = new AutenticacionService();
        _resultado = servicio.Login(_usuario.Email, _usuario.Clave);
    }

    [Then(@"debo ser redirigido al dashboard")]
    public void ThenRedirigidoDashboard()
    {
        Assert.Equal("/dashboard", _resultado.RedirectUrl);
    }
}
```

---

**Última actualización:** 2026-02-01
