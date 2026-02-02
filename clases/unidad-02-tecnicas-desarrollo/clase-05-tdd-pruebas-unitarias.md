---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 2'
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

# TDD - Test-Driven Development

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 2 - Clase 5**

---

## Objetivos y Agenda

| 🎯 Objetivos | 📋 Agenda (90 min) |
|-------------|-------------------|
| 1. Comprender filosofía y ciclo TDD | 10' ¿Por qué probar? |
| 2. Escribir pruebas con xUnit | 15' Fundamentos TDD |
| 3. Aplicar Red-Green-Refactor | 15' xUnit Framework |
| 4. Identificar casos de prueba | 15' Estructura de pruebas |
| 5. Medir cobertura de código | 20' Ciclo Red-Green-Refactor |
| | 15' Buenas prácticas |

---

## 1. ¿Por Qué Probar el Código?

### ❌ Desarrollo Sin TDD vs ✅ Beneficios TDD

| ❌ Sin TDD | ✅ Con TDD |
|------------|------------|
| Bugs en producción | Cambios sin miedo |
| Costo 100x mayor | Refactorización segura |
| Hotfixes urgentes | Detección temprana |
| Miedo a refactorizar | Código modular |
| Código frágil | Bajo acoplamiento |
| | APIs usables |
| | Documentación viva |

---

## Costo Exponencial de Errores

```
$1      $10     $100    $1,000   $10,000
 │       │       │        │         │
 ▼       ▼       ▼        ▼         ▼
Diseño  Código  Test   Integración  Producción
```

| Fase | Costo | Impacto |
|------|-------|---------|
| **Diseño** | $1 | Documentos |
| **Código** | $10 | Una clase |
| **Test** | $100 | Rompe otras pruebas |
| **Integración** | $1,000 | Múltiples módulos |
| **Producción** | $10,000+ | Daño reputacional |

> ⚠️ **IBM/NIST:** Corregir un error en producción cuesta **100x más**

---

## Pirámide de Pruebas

```
           ▲
          ╱ ╲
         ╱E2E╲         10% - Flujos completos
        ╱─────╲        Lentas, frágiles
       ╱       ╲
      ╱ INTEG. ╲      20% - Interacción componentes
     ╱──────────╲     Más lentas (BD/API)
    ╱            ╲
   ╱▆▆▆▆▆▆▆▆▆▆▆▆▆▆╲  70% - Unit Tests
 ╱  UNIT TESTS   ╲ Rápidas (ms), aisladas
╱─────────────────╲ Escribibles con TDD
```

### 📊 Distribución

| Tipo | % | Características |
|------|---|----------------|
| **Unit Tests** | 70% | Rápidas, aisladas, TDD |
| **Integration** | 20% | Interacción componentes, BD/API |
| **E2E** | 10% | Flujos completos, lentas |

---

## 2. Fundamentos de TDD

### Ciclo Red-Green-Refactor

```
┌─────────────────────────────────────────────────────────────┐
│                  CICLO TDD (MANTRA)                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   RED → Escribir prueba que falle (NO existe código aún)   │
│    ↓                                                       │
│ GREEN → Código mínimo para pasar                          │
│    ↓                                                       │
│ REFACTOR → Eliminar duplicación (tests verdes)             │
│    ↓                                                       │
│ REPEAT → Siguiente prueba, pequeños incrementos             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 📜 Las Tres Leyes de TDD (Uncle Bob)

| Ley | Principio |
|-----|-----------|
| 1️⃣ | No escribirás código de producción hasta haber escrito una prueba que falle |
| 2️⃣ | No escribirás más de una prueba suficiente para fallar |
| 3️⃣ | No escribirás más código del necesario para pasar la prueba |

---

## 3. xUnit: Framework para .NET

### Comparativa de Frameworks

| Framework | Características |
|-----------|----------------|
| **MSTest** | Microsoft, Visual Studio default |
| **NUnit** | Clásico, muy popular |
| **xUnit** | ⭐ Moderno, open source, usado por .NET team |

### ✅ Por qué xUnit

| Ventaja | Descripción |
|---------|-------------|
| Atributos `[Fact]` y `[Theory]` | Pruebas simples y parametrizadas |
| Inyección de dependencias nativa | Sin configuración extra |
| Paralelismo por defecto | Tests más rápidos |
| Constructor para setup | Sin `[SetUp]` atributo (usa constructor de clase) |
| Extensible con fixtures | Comunidad activa |

### 📖 Nota sobre Frameworks

**NUnit**: Framework alternativo clásico, usa `[SetUp]` atributo para método de configuración.
**MSTest**: Framework de Microsoft, incluido por defecto en Visual Studio.

> 💡 **Elegimos xUnit** por ser el framework usado por el equipo de .NET y tener mejor soporte moderno.

---

## Configuración de xUnit

### 📦 Crear Proyecto de Pruebas

```bash
# CLI de .NET
dotnet new xunit -n MiProyecto.Tests
cd MiProyecto.Tests
dotnet add reference ../MiProyecto/MiProyecto.csproj

# Visual Studio:
# 1. Solución → Agregar → Nuevo
# 2. "xUnit Test Project"
# 3. Framework: .NET 8.0
```

### 📁 Estructura

```
MiProyecto/
├── src/
│   └── Calculadora/
│       └── Calculadora.cs
└── tests/
    └── Calculadora.Tests/
        └── CalculadoraTests.cs
```

---

## 4. Estructura de Pruebas xUnit

### Patrón AAA: Arrange, Act, Assert

```csharp
using Xunit;

public class CalculadoraTests
{
    [Fact]
    public void Sumar_DosNumeros_RetornaSuma()
    {
        // ARRANGE - Configurar escenario
        var calc = new Calculadora();
        int a = 5, b = 3;

        // ACT - Ejecutar acción
        int resultado = calc.Sumar(a, b);

        // ASSERT - Verificar resultado
        Assert.Equal(8, resultado);
    }
}
```

### 🔍 Convención de Nombres

```
Metodo_Escenario_Resultado

✅ Sumar_DosNumerosPositivos_RetornaSuma
✅ Dividir_DivisorCero_LanzaExcepcion
✅ Constructor_SinParametros_InicializaDefault

❌ Test1
❌ CalculadoraPrueba
```

---

## Verificaciones Fundamentales

| Tipo | Método | Ejemplo |
|------|--------|---------|
| **Igualdad** | `Assert.Equal/NotEqual` | `Assert.Equal(5, resultado)` |
| **Booleanos** | `Assert.True/False` | `Assert.True(condicion)` |
| **Nulos** | `Assert.Null/NotNull` | `Assert.Null(objeto)` |
| **Excepciones** | `Assert.Throws<T>` | `Assert.Throws<ArgumentException>(()=>...` |
| **Colecciones** | `Assert.Contains/Empty` | `Assert.Contains(item, list)` |
| **Tipos** | `Assert.IsType<T>` | `Assert.IsType<string>(obj)` |
| **Rangos** | `Assert.InRange` | `Assert.InRange(val, 1, 10)` |

---

## Pruebas Parametrizadas

### [Theory] para Múltiples Casos

```csharp
[Theory]
[InlineData(1, 1, 2)]      // a=1, b=1, esperado=2
[InlineData(5, 3, 8)]      // a=5, b=3, esperado=8
[InlineData(-1, 1, 0)]     // a=-1, b=1, esperado=0
[InlineData(0, 0, 0)]      // a=0, b=0, esperado=0
public void Sumar_VariosNumeros_RetornaSuma(
    int a, int b, int esperado)
{
    var calc = new Calculadora();
    int resultado = calc.Sumar(a, b);
    Assert.Equal(esperado, resultado);
}
```

---

## 5. Ciclo Red-Green-Refactor en Práctica

### 🔴🟢🔵 Ejemplo: Calculadora

| Fase | Código |
|-------|--------|
| **🔴 RED** | ```csharp<br>[Fact]<br>public void Sumar_DosNumeros_RetornaSuma()<br>{<br>&nbsp;&nbsp;var calc = new Calculadora();<br>&nbsp;&nbsp;int resultado = calc.Sumar(2, 3);<br>&nbsp;&nbsp;Assert.Equal(5, resultado);<br>}<br>// ❌ ERROR: No existe Calculadora<br>``` |
| **🟢 GREEN** | ```csharp<br>public class Calculadora<br>{<br>&nbsp;&nbsp;public int Sumar(int a, int b)<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;return 5; // Hardcoded<br>&nbsp;&nbsp;}<br>}<br>// ✅ TEST PASA<br>``` |
| **🔵 REFACTOR** | ```csharp<br>[Theory]<br>[InlineData(2, 3, 5)]<br>[InlineData(5, 5, 10)]<br>public void Sumar_Varios(int a, int b, int e)<br>{<br>&nbsp;&nbsp;Assert.Equal(e, calc.Sumar(a, b));<br>}<br>public class Calculadora<br>{<br>&nbsp;&nbsp;public int Sumar(int a, int b) => a + b;<br>}<br>``` |

---

## Buenas Prácticas de Pruebas

| Principio | Descripción |
|-----------|-------------|
| **📋 Independientes** | Cada prueba ejecuta sola, sin orden |
| **⚡ Rápidas** | Milisegundos, sin BD/red |
| **🎯 Focadas** | Una prueba = un concepto |
| **🔁 Repetibles** | Mismo resultado siempre |
| **📖 Legibles** | AAA claro, datos inline |

### ❌ Anti-Patrones

| Anti-Patrón | Problema |
|-------------|----------|
| **The Giant** | Arrange de 200 líneas |
| **The Sleeper** | Thread.Sleep en pruebas |
| **The Mockery** | Demasiados mocks, 0 código real |
| **The Sequencer** | Pruebas con orden de ejecución |

---

## Test Doubles: Tipología

```
┌─────────────────────────────────────────────────────────────┐
│                  TEST DOUBLES - TIPOLOGÍA                   │
├─────────────────────────────────────────────────────────────┤
│  DUMMY  │  STUB  │  FAKE  │  MOCK  │                      │
│ Solo   │Resp.   │Impl.   │Verif.  │                      │
│ llena  │prede-  │simpl.  │compor- │                      │
│ parám. │finida  │real    │tamiento│                      │
└─────────────────────────────────────────────────────────────┘
```

### 💡 Ejemplo: Stub vs Mock

| Tipo | Código |
|------|--------|
| **Stub** | ```csharp<br>public class StubRepo : IUsuarioRepo<br>{<br>&nbsp;&nbsp;public Usuario GetById(int id)<br>&nbsp;&nbsp;&nbsp;&nbsp;=> new Usuario { Id = id };<br>}<br>``` |
| **Mock** | ```csharp<br>var mock = new Mock<IUsuarioRepo>();<br>mock.Setup(r => r.GetById(1)).Returns(null);<br>mock.Verify(r => r.GetById(1), Times.Once);<br>``` |

### 📖 ¿Qué es una Interface?

**interface**: Contrato que define qué métodos DEBE tener una clase, sin implementarlos.

```csharp
// Contrato
public interface IUsuarioRepo
{
    Usuario GetById(int id);  // Solo define firma, no código
    void Save(Usuario usuario);
}

// Implementación real
public class UsuarioRepo : IUsuarioRepo
{
    public Usuario GetById(int id) { /* código real */ }
    public void Save(Usuario usuario) { /* código real */ }
}
```

> 💡 **En testing**: Las interfaces permiten crear **stubs y mocks** sin dependecer de la BD real.

---

## Pruebas Asíncronas

```csharp
// Prueba de método async
[Fact]
public async Task ObtenerUsuario_Existe_ReturnsUsuario()
{
    var repo = new UsuarioRepository();
    int usuarioId = 1;

    Usuario? usuario = await repo.ObtenerUsuarioAsync(usuarioId);

    Assert.NotNull(usuario);
    Assert.Equal(usuarioId, usuario.Id);
}

// Excepciones async
[Fact]
public async Task Eliminar_NoExist_LanzaExcepcion()
{
    var repo = new UsuarioRepository();

    await Assert.ThrowsAsync<KeyNotFoundException>(
        () => repo.EliminarUsuarioAsync(999)
    );
}

// Timeout
[Fact(Timeout = 5000)]
public async Task OperLenta_CompletaATiempo()
{
    var servicio = new ServicioExterno();
    await servicio.ProcesarAsync();
}
```

### 📖 Atributo Timeout

- **Timeout**: Tiempo máximo en milisegundos que la prueba puede ejecutarse
- Si excede el tiempo, la prueba **falla** con `TimeoutException`
- Útil para detectar operaciones lentas o bloqueos infinitos

⚠️ **No usar** `Thread.Sleep()` en pruebas - hace tests lentos y frágiles.

---

## Cobertura de Código

### 📊 Comandos

```bash
# Instalar herramienta
dotnet tool install -g dotnet-reportgenerator-globaltool

# Ejecutar con cobertura
dotnet test --collect:"XPlat Code Coverage"

# Generar reporte HTML
reportgenerator \
  -reports:"**/coverage.cobertura.xml" \
  -targetdir:"coveragereport"
```

### 📈 Métricas

```
Líneas:  85% ███████████████░░
Ramas:   70% ███████████░░░░░░
Métodos: 90% ███████████████░░

Meta: > 80% líneas

⚠️ 100% ≠ código sin bugs
⚠️ Cobertura mide QUÉ se ejecuta, no QUÉ se prueba
```

---

## Ejercicio Práctico: Billetera TDD

### 📋 Requisitos

1. Saldo inicial: 0
2. Agregar dinero (+)
3. Retirar si hay saldo
4. No retirar más del saldo
5. Consultar saldo

### 🔴🟢🔵 Ciclo TDD

| Fase | Código |
|-------|--------|
| **🔴 RED** | ```csharp<br>[Fact]<br>public void Saldo_Inicialmente_EsCero()<br>{<br>&nbsp;&nbsp;var billetera = new Billetera();<br>&nbsp;&nbsp;Assert.Equal(0, billetera.Saldo);<br>}<br>``` |
| **🟢 GREEN** | ```csharp<br>public class Billetera<br>{<br>&nbsp;&nbsp;public decimal Saldo => 0;<br>}<br>``` |
| **🔵 REFACTOR** | ```csharp<br>public class Billetera<br>{<br>&nbsp;&nbsp;private decimal _saldo;<br>&nbsp;&nbsp;public decimal Saldo => _saldo;<br>&nbsp;&nbsp;public void Agregar(decimal m)<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;if (m <= 0) throw new ArgumentException();<br>&nbsp;&nbsp;&nbsp;&nbsp;_saldo += m;<br>&nbsp;&nbsp;}<br>}<br>``` |

---

## Resumen de la Clase

### 📚 Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **TDD** | Pruebas ANTES del código |
| **R-G-R** | Red-Green-Refactor |
| **xUnit** | Framework .NET |
| **[Fact]** | Prueba sin params |
| **[Theory]** | Prueba parametrizada |
| **AAA** | Arrange-Act-Assert |

### 🔗 Recursos

- xUnit.net - Doc oficial
- Kent Beck - "TDD: By Example"
- `dotnet new xunit`
- `dotnet test`

### 💡 Mantra TDD

> **"Si no está probado, no funciona"**

---

## 🚀 Próxima Clase: BDD - Behavior Driven Development

### Temas Clase 6

| Tema | Descripción |
|------|-------------|
| **BDD** | Pruebas de comportamiento |
| **Gherkin** | Lenguaje Given-When-Then |
| **SpecFlow** | Framework BDD para .NET |
| **Historias** | User Stories |

### 📦 Instalación

```bash
dotnet add package SpecFlow.xUnit
dotnet add package SpecFlow.Tools.MsBuild.Generation
```

---

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
