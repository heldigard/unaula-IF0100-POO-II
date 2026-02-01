---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<style>
section {
  font-size: 16px;
  overflow: hidden;
}
img {
  max-width: 60% !important;
  max-height: 40vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
}
section h1 { font-size: 1.8em; color: #1e40af; }
section h2 { font-size: 1.2em; color: #1e3a8a; }
section h3 { font-size: 1em; color: #3b82f6; }
section ul, section ol { font-size: 0.8em; margin-left: 0.5em; }
section li { margin-bottom: 0.2em; }
section pre { font-size: 0.55em; max-height: 50vh; overflow-y: auto; }
section code { font-size: 0.7em; }
section p { margin: 0.3em 0; }
section table { width: 100%; font-size: 0.75em; border-collapse: collapse; margin: 0.2em auto; }
section th { background-color: #1e40af; color: white; padding: 0.25em 0.4em; text-align: left; font-size: 0.75em; border: 1px solid #ddd; }
section td { padding: 0.25em 0.4em; border: 1px solid #ddd; vertical-align: top; word-wrap: break-word; font-size: 0.7em; }
section tbody tr:nth-child(even) { background-color: #f8f9fa; }
section tbody tr:hover { background-color: #e9ecef; }
.highlight-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.8em; border-radius: 6px; margin: 0.3em 0; font-size: 0.85em; }
.info-box { background: #f0f9ff; border-left: 3px solid #3b82f6; padding: 0.6em; margin: 0.3em 0; font-size: 0.85em; }
.warning-box { background: #fffbeb; border-left: 3px solid #f59e0b; padding: 0.6em; margin: 0.3em 0; font-size: 0.85em; }
.success-box { background: #f0fdf4; border-left: 3px solid #22c55e; padding: 0.6em; margin: 0.3em 0; font-size: 0.85em; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; }
.three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.8em; }
.col-card { background: white; border: 1px solid #e5e7eb; border-radius: 6px; padding: 0.6em; font-size: 0.85em; }
.compact-list { display: grid; grid-template-columns: 1fr 1fr; gap: 0.5em; font-size: 0.85em; }
</style>

---

# Introducción a C# y .NET

<div class="info-box" style="text-align: center;">

**IF0100 - Lenguaje de Programación OO II**

*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Fecha:** Semana 1

</div>

---

## Objetivos y Agenda

<div class="two-col">

<div>

### 🎯 Objetivos

| # | Meta |
|---|------|
| 1 | Historia de C# y .NET |
| 2 | Diferenciar .NET Framework/Core/8 |
| 3 | Configurar Visual Studio |
| 4 | Crear primera app C# |
| 5 | Estructura de programa |

</div>

<div>

### 📋 Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 15' | ¿Qué es C#? |
| 15' | Ecosistema .NET |
| 10' | Instalación VS |
| 25' | Estructura C# |
| 25' | Práctica |

</div>

</div>

---

## 1. ¿Qué es C#?

<div class="two-col">

<div>

### 🚀 Por qué C# en 2026?

```
┌─────────────────────────────┐
│  🌐 Web      │  ☁️ Cloud   │
│  🖥️ Desktop  │  🎮 Gaming  │
│  📱 Mobile   │  🤖 AI/ML   │
└─────────────────────────────┘
```

**Ventajas:**
- ✅ Multiplataforma (Win/Linux/Mac)
- ✅ Alto rendimiento
- ✅ Type-safe
- ✅ Gran demanda laboral

</div>

<div>

### 💼 Quién usa C#

| Empresa | Uso |
|---------|-----|
| **Microsoft** | Azure, Office 365 |
| **Unity** | 2.5M+ juegos |
| **Stack Overflow** | Backend completo |
| **Siemens** | Sistemas industriales |

<div class="highlight-box" style="text-align: center; font-size: 0.9em;">

**C# = C Sharp**<br>
Lenguaje moderno, POO, type-safe

</div>

</div>

</div>

---

## C# vs Java vs Python

<div class="three-col">

<div class="col-card">

### 🟢 C# (2000)

```csharp
string nombre = "Juan";
int edad = 20;
Console.WriteLine($"Hola {nombre}, tienes {edad}");
```

**✅ Type-safe**<br>
**✅ LINQ nativo**<br>
**✅ async/await**

</div>

<div class="col-card">

### 🟠 Java (1995)

```java
String nombre = "Juan";
int edad = 20;
System.out.println("Hola " + nombre);
```

**✅ JVM portable**<br>
**✅ Ecosistema grande**

</div>

<div class="col-card">

### 🔵 Python (1991)

```python
nombre = "Juan"
edad = 20
print(f"Hola {nombre}, tienes {edad}")
```

**✅ Sintaxis simple**<br>
**✅ Líder en Data**

</div>

</div>

---

## Historia de C#: 24 Años de Innovación

```
2000        2005        2012        2020        2024
 │           │           │           │           │
 ▼           ▼           ▼           ▼           ▼
C# 1.0  →  C# 2.0  →  C# 5.0  →  C# 9.0  →  C# 12
NACE       GENERICS   ASYNC/     .NET      .NET 8
.NET       TYPE-SAFE  AWAIT      CORE      UNIF.
```

| Versión | Año | Innovación |
|---------|-----|------------|
| C# 1.0 | 2000 | Nace .NET Framework |
| C# 2.0 | 2005 | Generics (`List<T>`) |
| C# 3.0 | 2007 | LINQ, var |
| C# 5.0 | 2012 | async/await |
| C# 9.0 | 2020 | .NET 5 open-source |
| C# 12 | 2024 | Primary constructors |

---

## Genéricos: La Revolución de Type-Safety

<div class="two-col">

<div>

### ❌ ANTES: ArrayList

```csharp
ArrayList lista = new ArrayList();
lista.Add(42);        // ⚠️ boxing
lista.Add("hola");    // ⚠️ mezclado
lista.Add(3.14);

int valor = (int)lista[0]; // ⚠️ crash posible
```

**Problemas:**
- Sin verificación de tipos
- Boxing/unboxing lento
- Errores en runtime

</div>

<div>

### ✅ DESPUÉS: List&lt;T&gt;

```csharp
List<int> nums = new List<int>();
nums.Add(42);    // ✅ type-safe
// nums.Add("hola"); // ❌ error compile

int valor = nums[0]; // ✅ sin cast
```

**Ventajas:**
- Verificación en compilación
- Sin boxing overhead
- Código más rápido y seguro

</div>

</div>

---

## Anders Hejlsberg: El Arquitecto

<div class="two-col">

<div>

### 👤 Perfil

| Atributo | Info |
|----------|------|
| 🇩🇰 Nacionalidad | Danesa |
| 💼 Cargo | Chief Architect MS |
| 📅 Años | 1996-presente |

### 🏆 Creaciones

| Año | Tech |
|-----|------|
| 1995 | Delphi |
| 2000 | C# |
| 2002 | .NET |
| 2012 | TypeScript |

</div>

<div>

### 💡 Filosofía

> *"C# combina potencia de C++ con productividad de VB"*

### 🎯 Principios

| Principio | Ejemplo |
|-----------|---------|
| Productividad | `var`, `=>` |
| Type Safety | Generics |
| POO Pura | LINQ |
| Evolución | 24 años compatible |

</div>

</div>

---

## Ecosistema .NET: Todo en Uno Plataforma

```
┌─────────────────────────────────────────────────┐
│              .NET 8 UNIFICADO                    │
├─────────────────────────────────────────────────┤
│  🌐 ASP.NET Core  │  🖥️ Desktop  │  📱 MAUI   │
│  • APIs REST      │  • WPF       │  • iOS/Droid│
│  • MVC            │  • WinForms  │            │
│  • Blazor         │              │            │
├─────────────────────────────────────────────────┤
│  ☁️ Azure Cloud  │  🎮 Unity    │  🤖 ML.NET │
│  • Functions      │  • 2.5M+     │  • AI/ML    │
│  • SDK nativo     │  • C# main   │            │
└─────────────────────────────────────────────────┘
```

**Una plataforma para:** Web + Desktop + Mobile + Cloud + Gaming + AI

---

## Evolución .NET: De la Fragmentación a la Unificación

<div class="two-col">

<div>

### 🔴 ANTES (hasta 2016)

```
┌──────────┐  ┌──────────┐  ┌──────────┐
│ .NET     │  │ .NET     │  │ Xamarin  │
│ Framework│  │ Core     │  │          │
├──────────┤  ├──────────┤  ├──────────┤
│Windows   │  │Open-src  │  │Mobile    │
│Only      │  │Web/API   │  │Different │
└──────────┘  └──────────┘  └──────────┘
```

**Problema:** Código NO compartible

</div>

<div>

### 🟢 AHORA (.NET 8)

```
┌─────────────────────────────────┐
│        .NET 8 UNIFICADO          │
│  ┌───┬───┬───┬───┬───┬───┐      │
│  │Web│Desk│Mob│Cl│Gam│AI │      │
│  └───┴───┴───┴───┴───┴───┘      │
│      ↓ UN RUNTIME               │
│  Win  Linux  mac  iOS  Android  │
└─────────────────────────────────┘
```

**Ventaja:** 100% código compartible

</div>

</div>

---

## Arquitectura .NET: Capas

```
┌─────────────────────────────────────────┐
│      TU APLICACIÓN C#                   │
├─────────────────────────────────────────┤
│    BCL (Base Class Library)             │
│  System.String, Collections, IO, Data   │
├─────────────────────────────────────────┤
│    CLR (Common Language Runtime)        │
│  ┌─────┐ ┌──────┐ ┌─────────────────┐  │
│  │ JIT │ │  GC  │ │ Type Safety     │  │
│  └─────┘ └──────┘ │ Exception Hdlr   │  │
│  Memory Mgmt      │ Thread Mgmt      │  │
│  └───────────────────────────────────┘  │
├─────────────────────────────────────────┤
│    Windows / Linux / macOS              │
└─────────────────────────────────────────┘
```

---

## Visual Studio 2022

<div class="two-col">

<div>

### 🛠️ Ediciones

| Edición | Precio | Uso |
|---------|--------|-----|
| **Community** | Gratis | Estudiantes |
| **Professional** | $$ | Equipos |
| **Enterprise** | $$$ | Empresas |

<div class="success-box" style="text-align: center;">

**Usaremos Community** (GRATIS)

</div>

</div>

<div>

### 📦 Workloads

```
☑️ ASP.NET y desarrollo web
   ├─ ASP.NET Core
   └─ HTML/JavaScript

☑️ Almacenamiento de datos
   ├─ SQL Server Tools
   └─ Data connectivity

☑️ .NET 8 SDK + Git
```

**Descarga:** visualstudio.microsoft.com

</div>

</div>

---

## Estructura Programa C#: Anatomía

```csharp
using System;           // 1️⃣ Importar namespaces

namespace MiApp          // 2️⃣ Organización lógica
{
    class Program        // 3️⃣ Contenedor de código
    {
        static void Main(string[] args)  // 4️⃣ Punto entrada
        {
            Console.WriteLine("¡Hola!"); // 5️⃣ Código ejecutable
        }
    }
}
```

| Parte | Propósito |
|-------|-----------|
| `using` | Importar namespaces |
| `namespace` | Agrupar código relacionado |
| `class` | Definir tipo/objeto |
| `Main` | Método de entrada |
| `Console` | I/O estándar |

---

## Namespaces en C#

```
System                    ← Raíz
├── Console           → WriteLine()
├── String            → Cadena texto
├── Math              → Funciones matemáticas
├── Collections
│   └── Generic      → List<T>, Dictionary<K,V>
├── IO
│   ├── File         → Archivos
│   └── Directory    → Directorios
└── Data
    └── SqlClient    → SQL Server
```

<div class="info-box">

**💡 Tip:** `using System;` evita escribir `System.Console` cada vez

</div>

---

## Value Types vs Reference Types

<div class="two-col">

<div>

### 📦 VALUE TYPES

| Característica | Valor |
|----------------|-------|
| Ubicación | Stack |
| Contenido | Valor directo |
| Asignación | Copia valor |
| Ejemplos | `int`, `double`, `bool` |

```csharp
int edad = 25;
int edad2 = edad;   // Copia
edad2 = 30;

Console.WriteLine(edad);   // 25
Console.WriteLine(edad2);  // 30
```

</div>

<div>

### 🔗 REFERENCE TYPES

| Característica | Valor |
|----------------|-------|
| Ubicación | Heap |
| Contenido | Referencia |
| Asignación | Copia referencia |
| Ejemplos | `string`, `class`, `array` |

```csharp
string nombre = "Juan";
string nombre2 = nombre;  // Misma ref
nombre2 = "Maria";        // Nuevo obj

Console.WriteLine(nombre);   // "Juan"
Console.WriteLine(nombre2);  // "Maria"
```

</div>

</div>

---

## Stack vs Heap: Visualización

```
┌─────────────────────────────────────────┐
│  📦 STACK (Value Types)                 │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐           │
│  │edad│ │edad2│ │price│ │active│       │
│  │ 25 │ │ 30 │ │19.99│ │true │        │
│  └────┘ └────┘ └────┘ └────┘           │
│      ↓                              ↑   │
│   Valores independientes              │   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  🔗 HEAP (Reference Types)              │
│  ┌──────────┐        ┌──────────┐      │
│  │ "Juan"   │        │ "Maria"  │      │
│  │ @0x7F3A  │        │ @0x8B2C  │      │
│  └──────────┘        └──────────┘      │
│       ↑                    ↑           │
│  ┌────┴─────┐        ┌────┴─────┐     │
│  │nombre    │        │nombre2   │     │
│  │@0x7F3A   │        │@0x8B2C   │     │
│  └──────────┘        └──────────┘     │
└─────────────────────────────────────────┘
```

---

## Nullable Types

<div class="two-col">

<div>

### 🤔 ¿Por qué?

```csharp
int edad = null;  // ❌ Error
```

**Cuándo se necesita:**
- Bases de datos (NULL)
- Formularios (opcionales)
- Configuraciones (sin valor)

### ✅ Solución

```csharp
int? edad = null;        // Nullable<int>
double? precio = null;
bool? activo = null;
DateTime? fecha = null;
```

</div>

<div>

### 🛠️ Operadores

| Op | Sintaxis | Descripción |
|----|----------|-------------|
| **??** | `a ?? b` | Usa `b` si `a` es null |
| **??=** | `a ??= b` | Asigna si null |
| **?.** | `a?.Prop` | Acceso seguro |

```csharp
int? num = null;
int edad = num ?? 18;  // valor default

string s = null;
int? len = s?.Length;  // null (no crash)
```

</div>

</div>

---

## Strings en C#

<div class="two-col">

<div>

### 📝 Creación

```csharp
// Interpolación ⭐
string saludo = $"Hola {nombre}";

// Concatenación
string s2 = "Hola " + nombre;

// Verbatim
string ruta = @"C:\Docs\archivo.txt";

// Multilínea (C# 11+)
string texto = """
    Línea 1
    Línea 2
""";
```

</div>

<div>

### 🛠️ Métodos Útiles

| Método | Resultado |
|--------|-----------|
| `Trim()` | `" hola "` → `"hola"` |
| `ToUpper()` | `"hola"` → `"HOLA"` |
| `Contains()` | Busca texto |
| `Split()` | Divide en array |
| `Replace()` | Reemplaza |
| `Length` | Longitud |

<div class="warning-box">

**⚠️ Strings son INMUTABLES**

```csharp
texto.ToUpper();      // ❌ No modifica
texto = texto.ToUpper(); // ✅ Reasigna
```

</div>

</div>

</div>

---

## C# 12: Primary Constructors

<div class="two-col">

<div>

### ❌ ANTES (Verboso)

```csharp
public class Persona
{
    private readonly string _nombre;
    private readonly int _edad;

    public Persona(string n, int e)
    {
        _nombre = n;
        _edad = e;
    }

    public string Nombre => _nombre;
    public int Edad => _edad;
}
```

**16 líneas**

</div>

<div>

### ✅ AHORA (Conciso)

```csharp
public class Persona(
    string nombre, int edad)
{
    public void Saludar() =>
        Console.WriteLine($"Hola {nombre}");

    public string Info =>
        $"{nombre} ({edad} años)";
}

// Uso
var p = new Persona("Ana", 25);
p.Saludar();  // "Hola, Ana"
```

**8 líneas** • 50% menos código

</div>

</div>

---

## C# 12: Collection Expressions

<div class="two-col">

<div>

### ❌ ANTES

```csharp
// Array
int[] nums = new int[] {1,2,3};

// List
var list = new List<int> {1,2,3};

// Dictionary
var dict = new Dictionary<string,int>
{
    {"Ana", 25},
    {"Juan", 30}
};
```

</div>

<div>

### ✅ AHORA

```csharp
// Array
int[] nums = [1, 2, 3];

// List
List<string> names = ["Ana","Juan"];

// Dictionary
var dict = new Dictionary<string,int>()
{
    ["Ana"] = 25,
    ["Juan"] = 30
};

// Spread
int[] all = [..pares, ..impares];
```

</div>

</div>

---

## Pattern Matching

<div class="two-col">

<div>

### 🔢 Rangos

```csharp
string categoria = edad switch
{
    < 13 => "Niño",
    >= 13 and < 20 => "Adolescente",
    >= 20 and < 65 => "Adulto",
    _ => "Mayor"
};

string nota = promedio switch
{
    >= 4.5 => "Excelente ⭐",
    >= 3.5 => "Bueno 👍",
    >= 3.0 => "Aceptable",
    _ => "Reprobado ❌"
};
```

</div>

<div>

### 🎯 Tipos

```csharp
string desc = obj switch
{
    int i when i > 0 => $"Positivo: {i}",
    int i when i < 0 => $"Negativo: {i}",
    string s => $"Texto ({s.Length})",
    null => "Sin valor",
    _ => "Otro"
};

// List patterns
int[] nums = [1, 2, 3];
string patron = nums switch
{
    [1, 2, 3] => "Exacto",
    [1, _, _] => "Empieza con 1",
    _ => "Otro"
};
```

</div>

</div>

---

## Ejercicio: Calculadora de Área

<div class="two-col">

<div>

### 🎯 Objetivo

App de consola: área de rectángulo

### ✅ Conceptos

| # | Tema |
|---|------|
| 1 | Console I/O |
| 2 | Variables double |
| 3 | Parseo strings |
| 4 | Interpolación |
| 5 | Estructura C# |

### 🚀 Reto

Validar no negativos • Agregar círculo/triángulo • Usar métodos

</div>

<div>

### 💻 Código

```csharp
using System;

namespace CalculadoraArea
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== CALCULADORA ===");
            Console.Write("Base: ");
            double b = double.Parse(Console.ReadLine());
            Console.Write("Altura: ");
            double h = double.Parse(Console.ReadLine());
            double area = b * h;
            Console.WriteLine($"Área: {area:F2}");
        }
    }
}
```

</div>

</div>

---

## Ejercicio: Sistema de Calificaciones

<div class="two-col">

<div>

### 🎯 Desafío

Sistema que calcule promedios

### 📋 Requisitos

1. Nombre estudiante
2. 3 notas (0.0-5.0)
3. Calcular promedio
4. APROBADO/REPROBADO
5. Validar datos
6. Formatear salida

### 🚀 Niveles

| Nivel | Req |
|-------|-----|
| Básico | Calcular promedio |
| Intermedio | Validar 0-5 |
| Avanzado | Método reutilizable |

</div>

<div>

### 📊 Salida

```
================================
  SISTEMA DE CALIFICACIONES
================================
Estudiante: María López

Notas:
  Nota 1: 4.5
  Nota 2: 3.8
  Nota 3: 4.2
--------------------------------
Promedio: 4.17
Estado: ✅ APROBADO
================================
```

### 💡 Pistas

```csharp
double n1 = double.Parse(Console.ReadLine());
double promedio = (n1 + n2 + n3) / 3;
string estado = promedio >= 3.0 ?
    "APROBADO" : "REPROBADO";
```

</div>

</div>

---

## Validación de Entrada

<div class="two-col">

<div>

### 🎯 Por qué validar

- ❌ Letras en lugar de números
- ❌ Notas fuera de rango
- ❌ Crashes inesperados

### 🔑 Conceptos

| Método | Propósito |
|--------|-----------|
| `TryParse()` | Convierte sin excepción |
| `while(true)` | Repite hasta válido |
| `out nota` | Parámetro salida |

</div>

<div>

### 💻 Código

```csharp
static double PedirNota(string etiqueta)
{
    double nota;
    while (true)
    {
        Console.Write($"{etiqueta} (0-5): ");
        if (double.TryParse(
            Console.ReadLine(), out nota))
        {
            if (nota >= 0 && nota <= 5)
                return nota;
            Console.WriteLine("⚠️ Fuera de rango");
        }
        else
        {
            Console.WriteLine("⚠️ No es número");
        }
    }
}

// Uso
double n1 = PedirNota("Nota 1");
```

</div>

</div>

---

## Atajos Visual Studio

<div class="two-col">

<div>

### 🎯 Debugging

| Atajo | Acción |
|-------|--------|
| F5 | Iniciar debug |
| F9 | Toggle breakpoint |
| F10 | Step Over |
| F11 | Step Into |
| Shift+F11 | Step Out |
| Ctrl+. | Quick Actions |

</div>

<div>

### 🛠️ Edición

| Atajo | Acción |
|-------|--------|
| Ctrl+K,C | Comentar |
| Ctrl+K,U | Descomentar |
| Ctrl+Space | IntelliSense |
| F12 | Ir a definición |
| Ctrl+R,R | Renombrar |
| Ctrl+- | Navegar atrás |

</div>

</div>

---

## C# vs Otros Lenguajes (2024)

<div class="two-col">

<div>

### 🏆 Benchmark

| Operación | C# | Java | Python |
|-----------|-----|------|--------|
| Loop 1M | 15ms | 18ms | 980ms |
| Sort 100K | 180ms | 200ms | 450ms |
| JSON | 90ms | 100ms | 150ms |
| **Memoria** | **25MB** | **40MB** | **15MB** |

### 💼 Mercado Colombia 2026

- C#/.NET: ⭐⭐⭐⭐⭐
- Java: ⭐⭐⭐⭐⭐ (legacy)
- Python: ⭐⭐⭐⭐⭐ (Data/AI)
- JS: ⭐⭐⭐⭐⭐ (Universal)

</div>

<div>

### 🌟 Cuándo usar

```
┌─────────────────────────────┐
│ C#    → Empresas, Windows   │
│ Java  → Legacy, Android     │
│ Python→ Data Science, IA    │
│ JS    → Frontend, Node.js   │
│ Go    → Microservicios      │
│ Rust  → Bajo nivel, crítico │
└─────────────────────────────┘
```

**Fortalezas C#:**
- Rendimiento ≈ C++
- Menor memoria que Java
- Tipado estático (errores compile)

</div>

</div>

---

## Ciclo de Ejecución C#

```
1️⃣ ESCRITURA          2️⃣ COMPILACIÓN
┌──────────┐          ┌──────────┐
│ Código C# │  ──────>│ Compilador│
│ (.cs)    │          │   C#     │
└──────────┘          └─────┬────┘
                           │
                           ▼
                  3️⃣ CÓDIGO IL
                  ┌──────────┐
                  │ .exe/.dll│
                  │    IL    │
                  └─────┬────┘
                        │
                        ▼
           4️⃣ EJECUCIÓN (CLR - JIT)
           ┌─────────────────────────┐
           │  JIT → Código máquina   │
           │  (x64, ARM, etc.)       │
           │  (Windows/Linux/macOS)  │
           └─────────────────────────┘
```

---

## Convenciones de Código

<div class="two-col">

<div>

### ✅ Nomenclatura

| Elemento | Estilo | Ejemplo |
|----------|--------|---------|
| Clases | PascalCase | `StudentManager` |
| Métodos | PascalCase | `GetStudent()` |
| Propiedades | PascalCase | `Name { get; }` |
| Campos priv. | _camelCase | `_count` |
| Variables | camelCase | `studentName` |
| Constantes | PascalCase | `MaxCount` |

### 📜 Reglas de Oro

1. Nombres descriptivos
2. Sin abreviaturas
3. Código se explica solo
4. Líneas ≤ 100 chars
5. Un archivo por clase

</div>

<div>

### 💻 Ejemplo Correcto

```csharp
public class StudentManager
{
    private int _studentCount;

    public string Name { get; set; }

    public void AddStudent()
    {
        int localVar = 10;
    }
}
```

### 🚀 Herramientas

- **StyleCop** - Reglas estilo
- **Resharper** - Refactoring
- **Formatter** - Ctrl+K,D

</div>

</div>

---

## NuGet: Gestor de Paquetes

<div class="two-col">

<div>

### 📚 ¿Qué es?

Similar a npm o pip para .NET

### 💻 CLI

```bash
dotnet add package Newtonsoft.Json
dotnet add package Dapper --version 2.1.28
dotnet list package
```

### 🖥️ VS

Click derecho → Manage NuGet Packages → Install

</div>

<div>

### 🔥 Populares

| Paquete | Uso | Descargas |
|---------|-----|-----------|
| Newtonsoft.Json | JSON | 2.5B+ |
| Dapper | Micro ORM | 500M+ |
| Serilog | Logging | 300M+ |
| xUnit | Testing | 150M+ |

**🔗 https://www.nuget.org/**

</div>

</div>

---

## Resumen de la Clase

<div class="compact-list">

<div>

### 📚 Conceptos

| Tema | Descripción |
|------|-------------|
| **C#** | Lenguaje moderno, POO |
| **.NET 8** | Plataforma unificada |
| **CLR** | Máquina virtual |
| **Value Types** | Stack, valor |
| **Ref. Types** | Heap, referencias |

### 🎯 Habilidades

```
✅ Instalar VS 2022
✅ Crear app consola
✅ Variables y tipos
✅ I/O con Console
✅ Depurar código
```

</div>

<div>

### 🚀 Próximos Pasos

- **Clase 2:** Clases y Objetos
- Practicar ejercicios
- Completar tarea

### 💡 Recurso

[Microsoft Learn C#](https://learn.microsoft.com/es-es/dotnet/csharp/)

</div>

</div>

---

## Tarea para Casa

<div class="two-col">

<div>

### 🖥️ Instalación

1. Descargar VS Community
2. Workloads:
   - ☑️ ASP.NET web
   - ☑️ Datos
3. Componentes:
   - ☑️ .NET 8 SDK
   - ☑️ Git

</div>

<div>

### 💻 Proyecto

**Calculadora de Promedios**

```
1. Nombre estudiante
2. 3 notas (0.0-5.0)
3. Promedio
4. APROBADO/REPROBADO
5. Validar datos
```

**📦 Entrega:** Subir a GitHub

</div>

</div>

---

## 🎓 Próxima Clase: Clases y Objetos

### Temas

- POO en C#
- Clases y objetos
- Atributos y métodos
- Encapsulamiento
- Constructores

### 📝 Requisitos

- ✅ VS 2022 instalado
- ✅ Tarea completada
- ✅ Repo Git creado

### 🔗 Preparación

- **Clase** = Plantilla
- **Objeto** = Instancia
- **Atributo** = Propiedad
- **Método** = Comportamiento

---

# ¡Gracias!
## ¿Preguntas?

<div class="info-box" style="text-align: center;">

**Contacto:** [Tu correo]

**Repositorio:** [Enlace]

**UNAULA - Ingeniería Informática - 2026-I**

</div>
