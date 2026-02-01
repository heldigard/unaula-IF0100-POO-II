---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 2'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<style>
section { font-size: 16px; overflow: hidden; }
img { max-width: 70% !important; max-height: 45vh !important; object-fit: contain !important; height: auto !important; display: block !important; margin: 0 auto !important; }
section h1 { font-size: 1.8em; color: #1e40af; }
section h2 { font-size: 1.2em; color: #1e3a8a; margin-top: 0.5em; }
section h3 { font-size: 1.05em; color: #1e3a8a; }
section ul, section ol { font-size: 0.85em; margin-left: 1em; }
section li { margin-bottom: 0.25em; }
section pre { font-size: 0.55em; max-height: 50vh; overflow-y: auto; background: #1e293b; color: #e2e8f0; padding: 0.8em; border-radius: 6px; }
section code { font-size: 0.8em; background: #f1f5f9; padding: 0.1em 0.3em; border-radius: 3px; }
section p { margin: 0.4em 0; font-size: 0.9em; }
section table { width: 100%; font-size: 0.75em; border-collapse: collapse; margin: 0.5em auto; }
section th { background-color: #1e40af; color: white; padding: 0.3em 0.5em; text-align: left; font-size: 0.85em; border: 1px solid #ddd; }
section td { padding: 0.3em 0.5em; border: 1px solid #ddd; vertical-align: top; word-wrap: break-word; font-size: 0.8em; }
section tbody tr:nth-child(even) { background-color: #f8f9fa; }
section tbody tr:hover { background-color: #e9ecef; }

.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; }
.three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.8em; }
.highlight-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.8em 1em; border-radius: 8px; margin: 0.5em 0; }
.info-box { background: #f0f9ff; border-left: 3px solid #3b82f6; padding: 0.6em 0.8em; margin: 0.4em 0; }
.warning-box { background: #fefce8; border-left: 3px solid #eab308; padding: 0.6em 0.8em; margin: 0.4em 0; }
.success-box { background: #f0fdf4; border-left: 3px solid #22c55e; padding: 0.6em 0.8em; margin: 0.4em 0; }
.error-box { background: #fef2f2; border-left: 3px solid #ef4444; padding: 0.6em 0.8em; margin: 0.4em 0; }
</style>

---

# TDD - Test-Driven Development

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos y Agenda

<div class="two-col">

<div>

### 🎯 Objetivos

| # | Meta |
|---|------|
| 1 | Comprender filosofía y ciclo TDD |
| 2 | Escribir pruebas con xUnit |
| 3 | Aplicar Red-Green-Refactor |
| 4 | Identificar casos de prueba |
| 5 | Medir cobertura de código |

</div>

<div>

### 📋 Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 10' | ¿Por qué probar? |
| 15' | Fundamentos TDD |
| 15' | xUnit Framework |
| 15' | Estructura de pruebas |
| 20' | Ciclo Red-Green-Refactor |
| 15' | Buenas prácticas |

</div>

</div>

---

## 1. ¿Por Qué Probar el Código?

<div class="two-col">

<div>

### ❌ Desarrollo Sin TDD

```
1. Escribir código
2. Más código...
3. Probar manual
4. Deploy 🚀
5. 💥 ERROR
6. Debuggear 😱
7. Hotfix 3AM
```

### Problemas

**Pruebas Tardías**
- Bugs en producción
- Costo 100x mayor
- Hotfixes urgentes

**Sin Confianza**
- Miedo a refactorizar
- Código frágil

</div>

<div>

### ✅ Beneficios TDD

**Seguridad**
- Cambios sin miedo
- Refactorización segura
- Detección temprana

**Diseño**
- Código modular
- Bajo acoplamiento
- APIs usables

**Documentación Viva**
- Pruebas documentan comportamiento
- Ejemplos reales
- Siempre actualizada

**Menos Debugging**
- Problemas inmediatos
- Flujo continuo

</div>

</div>

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

<div class="error-box">

**⚠️ Conclusión IBM/NIST:** Corregir un error en producción cuesta **100x más** que en desarrollo.

</div>

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
   ╱▆▆▆▆▆▆▆▆▆▆▆▆▆╲  70% - Unit Tests
  ╱  UNIT TESTS   ╲ Rápidas (ms), aisladas
 ╱─────────────────╲ Escribibles con TDD
```

<div class="two-col">

<div>

**Unit Tests (70%)**
- Prueban clases/métodos
- Rápidas (milisegundos)
- Aisladas (sin BD/red)
- Escribibles con TDD

</div>

<div>

**Integration (20%)**
- Interacción componentes
- Requieren BD/API
- Verifican integración

**E2E (10%)**
- Flujo completo usuario
- Lentas y frágiles
- Solo flujos críticos

</div>

</div>

---

## 2. Fundamentos de TDD

### Ciclo Red-Green-Refactor

```
┌─────────────────────────────────────────────────────────────┐
│                  CICLO TDD (MANTRA)                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│              ┌─────────────┐                                │
│              │    RED     │ Escribir prueba que falle      │
│              │  (falla)   │ NO existe código aún            │
│              └──────┬──────┘                                │
│                     │                                       │
│                     ▼                                       │
│  ┌─────────────┐    Código     ┌─────────────┐             │
│  │   GREEN    │ ←── mínimo ───│ Escribe     │             │
│  │  (pasa)    │    para pasar │ prueba      │             │
│  └──────┬──────┘               └─────────────┘             │
│         │                                                       │
│         │ Mejora código                                       │
│         ▼                                                     │
│  ┌─────────────┐                                            │
│  │  REFACTOR  │ Eliminar duplicación                        │
│  │ (mejora)   │ Mantener tests verdes                       │
│  └──────┬──────┘                                            │
│         │                                                   │
│         └───────────────────────────────────┐               │
│                                             │               │
│                                             ▼               │
│              ┌─────────────┐                                │
│              │   REPEAT   │ Siguiente prueba                │
│              │  (ciclo)   │ Pequeños incrementos            │
│              └─────────────┘                                │
│                                                             │
│         RED → GREEN → REFACTOR → REPEAT                    │
└─────────────────────────────────────────────────────────────┘
```

---

### Las Tres Leyes de TDD (Uncle Bob)

<div class="highlight-box">

**1️⃣ Primera Ley**
> "No escribirás código de producción hasta haber escrito una prueba unitaria que falle"

**2️⃣ Segunda Ley**
> "No escribirás más de una prueba unitaria suficiente para fallar, y no compilar es fallar"

**3️⃣ Tercera Ley**
> "No escribirás más código de producción del necesario para pasar la prueba actual"

</div>

### Resultado

✅ Pruebas muy pequeñas
✅ Incrementos pequeños
✅ Código siempre probado
✅ Diseño emergente

---

## 3. xUnit: Framework para .NET

### Comparativa de Frameworks

```
┌─────────────────────────────────────────────────────────────┐
│                  FRAMEWORKS DE PRUEBA .NET                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   MSTest   │  │    NUnit   │  │    xUnit   │         │
│  │(Microsoft) │  │ (Clásico)  │  │ (Moderno)  │         │
│  └─────────────┘  └─────────────┘  └──────┬──────┘         │
│                                           │                 │
│                                           ▼                 │
│              USAREMOS: xUnit                                       │
│                                                             │
│  • Atributos [Fact] y [Theory]                              │
│  • Inyección de dependencias nativa                         │
│  • Paralelismo por defecto                                  │
│  • Constructor para setup (sin [Setup])                     │
│  • Extensible con fixtures                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Configuración de xUnit

### Crear Proyecto de Pruebas

<div class="two-col">

<div>

```bash
# CLI de .NET
dotnet new xunit -n MiProyecto.Tests
cd MiProyecto.Tests
dotnet add reference \
  ../MiProyecto/MiProyecto.csproj

# Visual Studio:
# 1. Solución → Agregar → Nuevo
# 2. "xUnit Test Project"
# 3. Framework: .NET 8.0
```

### Estructura

```
MiProyecto/
├── src/
│   └── Calculadora/
│       └── Calculadora.cs
└── tests/
    └── Calculadora.Tests/
        └── CalculadoraTests.cs
```

</div>

<div>

```xml
<!-- .csproj -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <IsPackable>false</IsPackable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="xunit"
      Version="2.6.2" />
    <PackageReference Include="xunit.runner.visualstudio"
      Version="2.5.4" />
    <PackageReference Include="coverlet.collector"
      Version="6.0.0" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\..\src\Proyecto\Proyecto.csproj" />
  </ItemGroup>
</Project>
```

</div>

</div>

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
        // ╔══════════════════════════════════════╗
        // ║ ARRANGE - Configurar escenario       ║
        // ╚══════════════════════════════════════╝
        var calc = new Calculadora();
        int a = 5, b = 3;

        // ╔══════════════════════════════════════╗
        // ║ ACT - Ejecutar acción               ║
        // ╚══════════════════════════════════════╝
        int resultado = calc.Sumar(a, b);

        // ╔══════════════════════════════════════╗
        // ║ ASSERT - Verificar resultado        ║
        // ╚══════════════════════════════════════╝
        Assert.Equal(8, resultado);
    }
}
```

---

### Verificaciones Fundamentales

<div class="two-col">

<div>

```csharp
// IGUALDAD
Assert.Equal(expected, actual);
Assert.NotEqual(unexpected, actual);

// BOOLEANOS
Assert.True(condicion);
Assert.False(condicion);

// NULOS
Assert.Null(objeto);
Assert.NotNull(objeto);

// EXCEPCIONES
Assert.Throws<TipoException>(() => codigo);
```

</div>

<div>

```csharp
// COLECCIONES
Assert.Contains(elemento, coleccion);
Assert.Empty(coleccion);
Assert.NotEmpty(coleccion);

// TIPOS
Assert.IsType<Tipo>(objeto);
Assert.IsAssignableFrom<Base>(objeto);

// RANGOS
Assert.InRange(valor, min, max);

// STRINGS
Assert.StartsWith("inicio", texto);
Assert.EndsWith("fin", texto);
Assert.Matches(@"regex", texto);
```

</div>

</div>

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
    // Arrange
    var calc = new Calculadora();

    // Act
    int resultado = calc.Sumar(a, b);

    // Assert
    Assert.Equal(esperado, resultado);
}

// [ClassData] o [MemberData] para datos complejos
```

---

## 5. Ciclo Red-Green-Refactor en Práctica

### Ejemplo: Calculadora

<div class="two-col">

<div>

**🔴 PASO 1: RED**

```csharp
[Fact]
public void Sumar_DosNumeros_RetornaSuma()
{
    var calc = new Calculadora();
    int resultado = calc.Sumar(2, 3);
    Assert.Equal(5, resultado);
}

// ❌ ERROR: No existe Calculadora
```

</div>

<div>

**🟢 PASO 2: GREEN**

```csharp
public class Calculadora
{
    public int Sumar(int a, int b)
    {
        return 5; // Hardcoded
    }
}

// ✅ TEST PASA
```

**🔵 PASO 3: REFACTOR**

```csharp
[Theory]
[InlineData(2, 3, 5)]
[InlineData(5, 5, 10)]
public void Sumar_Varios(int a, int b, int e)
{
    Assert.Equal(e, calc.Sumar(a, b));
}

public class Calculadora
{
    public int Sumar(int a, int b)
        => a + b; // Implementación real
}
```

</div>

</div>

---

## Ejemplo Completo: Estudiante

<div class="two-col">

<div>

### Prueba 1: Aprobado

```csharp
[Fact]
public void Aprobo_PromedioMayor3_RetornaTrue()
{
    var est = new Estudiante
        { Promedio = 3.5 };
    bool aprobo = est.Aprobo();
    Assert.True(aprobo);
}

// Código mínimo
public class Estudiante
{
    public double Promedio { get; set; }
    public bool Aprobo() => true;
}
```

### Prueba 2: Reprobado

```csharp
[Fact]
public void Aprobo_PromedioMenor3_RetornaFalse()
{
    var est = new Estudiante
        { Promedio = 2.5 };
    Assert.False(est.Aprobo());
}

// ❌ FALLA (siempre true)
```

</div>

<div>

### Implementación Real

```csharp
public class Estudiante
{
    public double Promedio { get; set; }

    public bool Aprobo()
        => Promedio >= 3.0;
}

// ✅ AMBOS TESTS PASAN
```

### Convención de Nombres

```
Metodo_Escenario_Resultado

✅ Sumar_DosNumerosPositivos_RetornaSuma
✅ Dividir_DivisorCero_LanzaExcepcion
✅ Constructor_SinParametros_InicializaDefault

❌ Test1
❌ CalculadoraPrueba
```

</div>

</div>

---

## Buenas Prácticas de Pruebas

```
┌─────────────────────────────────────────────────────────────┐
│                BUENAS PRÁCTICAS DE PRUEBAS                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📋 INDEPENDIENTES                                          │
│     • Cada prueba ejecuta sola                              │
│     • Sin dependencia del orden                             │
│     • Sin estado compartido                                 │
│                                                             │
│  ⚡ RÁPIDAS                                                 │
│     • Milisegundos, no segundos                             │
│     • Sin BD, red, archivos                                 │
│     • Usar mocks/stubs                                      │
│                                                             │
│  🎯 FOCUSDAS                                                │
│     • Una prueba = un concepto                              │
│     • Nombre: Metodo_Escenario_Resultado                    │
│                                                             │
│  🔁 REPETIBLES                                              │
│     • Mismo resultado siempre                               │
│     • Sin valores aleatorios                                │
│     • Sin dependencia de fecha/hora                         │
│                                                             │
│  📖 LEGIBLES                                                │
│     • AAA claro                                             │
│     • Sin lógica compleja                                   │
│     • Datos inline                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Test Doubles: Tipología

```
┌─────────────────────────────────────────────────────────────┐
│                  TEST DOUBLES - TIPOLOGÍA                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Cuando una clase tiene dependencias (BD, API),             │
│  usamos "dobles" para aislar la prueba                      │
│                                                             │
│  ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐      │
│  │  DUMMY │    │  STUB  │    │  FAKE  │    │  MOCK  │      │
│  │        │    │        │    │        │    │        │      │
│  │ Solo   │    │ Resp.  │    │ Impl.  │    │ Verif. │      │
│  │ llena  │    │ prede- │    │ simpl. │    │ compor-│      │
│  │ parám. │    │ finida │    │ real   │    │ tamiento│      │
│  └────────┘    └────────┘    └────────┘    └────────┘      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Ejemplo: Stub vs Mock

<div class="two-col">

<div>

```csharp
// STUB: Respuestas predefinidas
public class StubRepo
    : IUsuarioRepository
{
    public Usuario GetById(int id)
        => new Usuario { Id = id };
}

[Fact]
public void Auth_Valid_ReturnsTrue()
{
    var stub = new StubRepo();
    var auth = new Autenticador(stub);
    Assert.True(auth.Autenticar(1));
}
```

</div>

<div>

```csharp
// MOCK: Verifica interacciones
[Fact]
public void Auth_Invalid_CallsRepo()
{
    var mock = new Mock<IUsuarioRepo>();
    mock.Setup(r => r.GetById(1))
        .Returns((Usuario)null);
    var auth = new Autenticador(mock.Object);

    auth.Autenticar(1, "pass");

    // Verify: Verifica llamada
    mock.Verify(r => r.GetById(1),
        Times.Once);
}
```

</div>

</div>

---

## Anti-Patrones de Pruebas

```
┌─────────────────────────────────────────────────────────────┐
│              ANTI-PATRONES DE PRUEBAS                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ❌ THE LOADER                                              │
│     "Prueba que carga TODO el sistema"                     │
│     • Integración disfrazada de unitaria                    │
│     • Lenta, frágil, difícil de debug                       │
│                                                             │
│  ❌ THE GIANT                                               │
│     "Prueba de 200 líneas con Arrange gigante"              │
│     • Difícil saber qué se prueba                           │
│     • Muchas cosas pueden fallar                            │
│                                                             │
│  ❌ THE MOCKERY                                             │
│     "Demasiados mocks, 0 código real"                      │
│     • Prueba que solo prueba los mocks                      │
│                                                             │
│  ❌ THE SLEEPER                                             │
│     "Thread.Sleep(5000) en la prueba"                       │
│     • Pruebas lentas, dependen del tiempo                   │
│                                                             │
│  ❌ THE SEQUENCER                                           │
│     "Pruebas con orden de ejecución"                        │
│     • Comparten estado entre pruebas                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Pruebas Asíncronas

```csharp
// Prueba de método async
[Fact]
public async Task ObtenerUsuario_Existe_ReturnsUsuario()
{
    var repo = new UsuarioRepository();
    int usuarioId = 1;

    Usuario? usuario =
        await repo.ObtenerUsuarioAsync(usuarioId);

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

---

## Cobertura de Código

<div class="two-col">

<div>

```bash
# Instalar herramienta
dotnet tool install -g \
  dotnet-reportgenerator-globaltool

# Ejecutar con cobertura
dotnet test --collect:"XPlat Code Coverage"

# Generar reporte HTML
reportgenerator \
  -reports:"**/coverage.cobertura.xml" \
  -targetdir:"coveragereport"
```

</div>

<div>

### Métricas de Cobertura

```
Líneas:  85% ███████████████░░
Ramas:   70% ███████████░░░░░░
Métodos: 90% ███████████████░░

Meta: > 80% líneas

⚠️ 100% ≠ código sin bugs
⚠️ Cobertura mide QUÉ se ejecuta,
   no QUÉ se prueba
```

### Ejecutar Pruebas

```bash
dotnet test                           # Todas
dotnet test --verbosity normal       # Detallado
dotnet test --filter "Calculadora"   # Por nombre
dotnet test --stop-on-failure        # Hasta fallo
dotnet test --parallel               # Paralelo
```

</div>

</div>

---

## Ejercicio Práctico: Billetera TDD

<div class="two-col">

<div>

### Requisitos

1. Saldo inicial: 0
2. Agregar dinero (+)
3. Retirar si hay saldo
4. No retirar más del saldo
5. Consultar saldo

### RED: Prueba 1

```csharp
[Fact]
public void Saldo_Inicialmente_EsCero()
{
    var billetera = new Billetera();
    Assert.Equal(0, billetera.Saldo);
}

// GREEN
public class Billetera
{
    public decimal Saldo => 0;
}
```

### RED: Prueba 2

```csharp
[Fact]
public void Agregar_Pos_AumentaSaldo()
{
    var b = new Billetera();
    b.Agregar(100);
    Assert.Equal(100, b.Saldo);
}
```

</div>

<div>

### GREEN: Implementación

```csharp
public class Billetera
{
    private decimal _saldo;
    public decimal Saldo => _saldo;

    public void Agregar(decimal m)
    {
        if (m <= 0)
            throw new ArgumentException();
        _saldo += m;
    }

    public void Retirar(decimal m)
    {
        if (m > _saldo)
            throw new InvalidOperationException();
        _saldo -= m;
    }
}
```

### REFACTOR: Tests completos

```csharp
[Theory]
[InlineData(100)]
[InlineData(50)]
public void Agregar_Varios_AumentaSaldo(decimal m)
{
    var b = new Billetera();
    b.Agregar(m);
    Assert.Equal(m, b.Saldo);
}

[Fact]
public void Retirar_Suficiente_DescuentaSaldo()
{
    var b = new Billetera();
    b.Agregar(100);
    b.Retirar(30);
    Assert.Equal(70, b.Saldo);
}
```

</div>

</div>

---

## Resumen y Próxima Clase

<div class="two-col">

<div>

### 📚 Resumen

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

### ⚠️ Anti-Patrones

- ❌ The Giant (Arrange grande)
- ❌ The Sleeper (Thread.Sleep)
- ❌ The Mockery (Demasiados mocks)
- ❌ The Sequencer (Dependientes)

</div>

<div>

### 🚀 Próxima Clase: BDD

- Historias de usuario
- Lenguaje Gherkin
- Given-When-Then
- SpecFlow para .NET
- Pruebas de comportamiento

```bash
dotnet add package SpecFlow.xUnit
dotnet add package SpecFlow.Tools.MsBuild.Generation
```

### 💡 Mantra TDD

> **"Si no está probado, no funciona"**

### 📝 Próxima Evaluación

- **Semana 4:** Quiz + Práctico
- **Tema:** POO completo + TDD

</div>

</div>

---

# ¡Gracias!

## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
