---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 1'
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

# Introducción a C# y .NET

**IF0100 - Lenguaje de Programación OO II**  
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Fecha:** Semana 1

---

## Objetivos y Agenda

| 🎯 Objetivos | 📋 Agenda (90 min) |
|-------------|-------------------|
| 1. Historia de C# y .NET | 15' ¿Qué es C#? |
| 2. Diferenciar .NET Framework/Core/8 | 15' Ecosistema .NET |
| 3. Configurar Visual Studio | 10' Instalación VS |
| 4. Crear primera app C# | 25' Estructura C# |
| 5. Estructura de programa | 25' Práctica |

---

## 1. ¿Qué es C#?

<div class="columns">
<div>

### 🚀 Por qué C# en 2026?

**Aplicaciones:** 🌐 Web APIs | 🖥️ Desktop | 📱 Mobile | ☁️ Cloud | 🎮 Gaming | 🤖 AI/ML

**Ventajas:**
- ✅ Multiplataforma (Win/Linux/Mac)
- ✅ Alto rendimiento
- ✅ Type-safe
- ✅ Gran demanda laboral

### 🔒 ¿Qué es Type-Safe?

**Type-safe** significa que el compilador verifica que los tipos de datos sean compatibles **antes** de ejecutar el código.

```csharp
// ✅ Type-safe: error en compilación, no en runtime
string nombre = "Juan";
int edad = nombre;  // ❌ Error CS0029: cannot convert string to int
```

**Beneficio:** Los errores se detectan mientras escribes, no cuando el programa ya está en producción.
- ✅ Multiplataforma (Win/Linux/Mac)
- ✅ Alto rendimiento
- ✅ Type-safe
- ✅ Gran demanda laboral

### 🏢 Quién usa C#

| Empresa | Uso |
|---------|-----|
| **Microsoft** | Azure, Office 365 |
| **Unity** | 2.5M+ juegos |
| **Stack Overflow** | Backend completo |

</div>
<div>

### ⚖️ C# vs Competidores

| C# (2000) | Java (1995) | Python (1991) |
|-----------|-------------|---------------|
| ✅ Type-safe | ✅ JVM portable | ✅ Sintaxis simple |
| ✅ **LINQ nativo** | ✅ Ecosistema grande | ✅ Líder en Data |
| ✅ **async/await** | | |

### 🔍 ¿Qué es LINQ?

**LINQ** (Language Integrated Query) permite consultar datos de forma declarativa, similar a SQL pero dentro de C#.

```csharp
// Consulta a una lista
var numeros = new List<int> { 5, 1, 9, 3, 7 };
var pares = numeros.Where(n => n % 2 == 0)
                  .OrderBy(n => n);
// Resultado: [] (sin pares en este ejemplo)
```

**Ventaja:** Misma sintaxis para bases de datos, XML, colecciones, JSON - lo veremos en detalle más adelante.

### ⚡ ¿Qué es async/await?

**async/await** es una forma de escribir código asíncrono de manera sincrónica, sin bloquear el hilo de ejecución. Es ideal para operaciones que toman tiempo (descargar archivos, consultar bases de datos, llamar APIs).

```csharp
// Código asíncrono que NO bloquea
async Task<string> DescargarDatosAsync()
{
    var cliente = new HttpClient();
    string resultado = await cliente.GetStringAsync("https://api.ejemplo.com");
    return resultado;
}
```

**Beneficio:** La aplicación permanece responsiva mientras espera - el hilo principal puede hacer otras cosas.

> ⚠️ **Error común:** Olvidar `await` antes de una llamada `async` - la operación se ejecuta en segundo plano y no obtienes el resultado.

**C# destaca en:** Empresas, Azure, Gaming

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

## Genéricos y su Arquitecto: Anders Hejlsberg

<div class="columns">
<div>

### ❌ ANTES: ArrayList

```csharp
ArrayList lista = new ArrayList();
lista.Add(42);        // ⚠️ boxing: int → object (en heap)
lista.Add("hola");    // ⚠️ puede mezclar tipos

int valor = (int)lista[0]; // ⚠️ unboxing: object → int
// Si lista[0] no es int, crash en runtime
```

**¿Qué es Boxing/Unboxing?**
- **Boxing:** Convertir un value type (stack) a reference type (heap) → costo de copia
- **Unboxing:** Operación inversa → costo de verificación de tipo + copia

**Problemas:** Sin verificación de tipos | Boxing/unboxing lento | Errores en runtime

### 🧩 ¿Qué son los Generics?

**Generics** permiten crear clases, interfaces y métodos que trabajan con cualquier tipo de datos, manteniendo type-safety. El `<T>` es un "parámetro de tipo" que se reemplaza por el tipo real que uses.

```csharp
// T puede ser int, string, Persona, lo que sea
List<T> lista = new List<T>();

// Ejemplos concretos:
List<int> numeros = new List<int>();      // T = int
List<string> nombres = new List<string>(); // T = string
List<Estudiante> estudiantes = new List<Estudiante>(); // T = Estudiante
```

**Beneficio:** Código reutilizable + type-safe + sin boxing overhead.

### ✅ DESPUÉS: List&lt;T&gt;

```csharp
List<int> nums = new List<int>();
nums.Add(42);    // ✅ type-safe
// nums.Add("hola"); // ❌ error compile

int valor = nums[0]; // ✅ sin cast
```

**Ventajas:** Verificación en compilación | Sin boxing overhead | Código más rápido

</div>
<div>

### 👤 Anders Hejlsberg

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

> 💡 *"C# combina potencia de C++ con productividad de VB"*

</div>
</div>

---

## Ecosistema .NET: De Fragmentación a Unificación

<div class="columns">
<div>

### 🟢 AHORA (.NET 10 / .NET 8 LTS)

<figure>
<svg width="100%" viewBox="0 0 800 180" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="dotnet10Title">
  <title id="dotnet10Title">Ecosistema .NET unificado</title>
  <style>
    .box { fill:#0b2d6b; stroke:#e6eefc; rx:10; }
    .label { fill:#fff; font-size:14px; font-family:Arial, sans-serif; font-weight:600; }
    .small { fill:#0b2d6b; font-size:12px; font-family:Arial, sans-serif; }
  </style>
  <rect x="30" y="12" width="740" height="56" rx="10" fill="#0b2d6b"/>
  <text x="400" y="48" text-anchor="middle" class="label">.NET 10 (2025) • .NET 8 LTS</text>
  <g transform="translate(70,80)">
    <rect x="0" y="0" width="660" height="36" rx="8" fill="#e5f0ff" stroke="#cfe2ff"/>
    <g fill="#0b2d6b" font-size="12" font-family="Arial, sans-serif" font-weight="600">
      <text x="20" y="24">Web</text>
      <text x="110" y="24">Desktop</text>
      <text x="220" y="24">Mobile</text>
      <text x="330" y="24">Cloud</text>
      <text x="440" y="24">Gaming</text>
      <text x="560" y="24">AI</text>
    </g>
  </g>
  <text x="400" y="150" text-anchor="middle" class="small">Un runtime compartido → Windows • Linux • macOS • iOS • Android</text>
</svg>
<figcaption>Diagrama simplificado del ecosistema .NET unificado (servicios: Web, Desktop, Mobile, Cloud, Gaming, AI) sobre un runtime común.</figcaption>
</figure>

**100% código compartible** • **Una plataforma para todo**

</div>
<div>

### 🔴 ANTES (hasta 2016)

<figure>
<svg width="100%" viewBox="0 0 800 140" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="dotnetAntes">
  <title id="dotnetAntes">Ecosistema .NET fragmentado antes de la unificación</title>
  <style>
    .card{fill:#f8fafc;stroke:#d9e2ec;rx:8}
    .h{font:600 13px/1.2 Arial, sans-serif;fill:#0b2d6b}
    .s{font:12px Arial, sans-serif;fill:#475569}
  </style>
  <g transform="translate(30,20)">
    <rect x="0" y="0" width="220" height="90" rx="8" class="card"/>
    <text x="110" y="28" text-anchor="middle" class="h">.NET Framework</text>
    <text x="110" y="52" text-anchor="middle" class="s">Windows only</text>
  </g>
  <g transform="translate(290,20)">
    <rect x="0" y="0" width="220" height="90" rx="8" class="card"/>
    <text x="110" y="28" text-anchor="middle" class="h">.NET Core</text>
    <text x="110" y="52" text-anchor="middle" class="s">Open-source • Web/API</text>
  </g>
  <g transform="translate(550,20)">
    <rect x="0" y="0" width="220" height="90" rx="8" class="card"/>
    <text x="110" y="28" text-anchor="middle" class="h">Xamarin</text>
    <text x="110" y="52" text-anchor="middle" class="s">Mobile • Diferente</text>
  </g>
</svg>
<figcaption>Antes de la unificación, existían plataformas separadas (.NET Framework, .NET Core, Xamarin) con compatibilidades y objetivos distintos.</figcaption>
</figure>

**Problema:** Código NO compartible

</div>
</div>

**Una plataforma para:** Web + Desktop + Mobile + Cloud + Gaming + AI

---

## Arquitectura .NET: Capas

<figure>
<svg width="100%" viewBox="0 0 760 320" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="arquTitle">
  <title id="arquTitle">Arquitectura en capas de .NET</title>
  <style>
    .layer{fill:#0b2d6b;rx:10}
    .layerText{fill:#fff;font:600 14px Arial, sans-serif}
    .sub{fill:#fff;font:500 12px Arial, sans-serif}
    .box{fill:#f4f8ff;stroke:#dbeafe;rx:6}
    .small{fill:#0b2d6b;font:12px Arial, sans-serif}
  </style>
  <!-- Top: App -->
  <rect x="60" y="12" width="640" height="56" rx="10" fill="#0b2d6b"/>
  <text x="380" y="48" text-anchor="middle" class="layerText">TU APLICACIÓN C#</text>
  <!-- BCL -->
  <rect x="80" y="84" width="600" height="64" rx="8" fill="#2563eb"/>
  <text x="380" y="122" text-anchor="middle" class="sub">BCL — System.String, Collections, IO, Data</text>
  <!-- CLR -->
  <rect x="100" y="164" width="560" height="84" rx="8" fill="#0b3a91"/>
  <text x="380" y="190" text-anchor="middle" class="sub">CLR — Common Language Runtime</text>
  <!-- JIT & GC boxes -->
  <g>
    <rect x="220" y="204" width="80" height="28" rx="6" class="box"/>
    <text x="260" y="222" text-anchor="middle" class="small">JIT</text>
    <rect x="320" y="204" width="100" height="28" rx="6" class="box"/>
    <text x="370" y="222" text-anchor="middle" class="small">GC</text>
    <rect x="440" y="204" width="160" height="28" rx="6" class="box"/>
    <text x="520" y="222" text-anchor="middle" class="small">Type Safety • Exceptions</text>
  </g>
  <!-- OS -->
  <rect x="120" y="260" width="520" height="36" rx="8" fill="#eef2ff"/>
  <text x="380" y="286" text-anchor="middle" class="small">Windows • Linux • macOS</text>
</svg>
<figcaption>Arquitectura por capas: aplicación → BCL (librerías) → CLR (runtime con JIT, GC, seguridad) → sistema operativo.</figcaption>
</figure>

### 📚 Componentes Clave

| Componente | Qué es | Por qué importa |
|-----------|--------|-----------------|
| **BCL** | Base Class Library - colección de clases predefinidas | No reinventas la rueda: String, List, File, etc. ya existen |
| **CLR** | Common Language Runtime - máquina virtual de .NET | Ejecuta código IL, maneja memoria, provee seguridad |
| **JIT** | Just-In-Time Compiler | Convierte IL a código máquina nativo en tiempo de ejecución |
| **GC** | Garbage Collector | Recupera memoria automática - no necesitas `free()`/`delete` |

> 💡 **Analogía:** .NET es como un restaurante:
> - **BCL** = La cocina ya equipada (no llevas tus propios utensilios)
> - **CLR** = El gerente que coordina todo
> - **JIT** = El chef que prepara cada plato al momento
> - **GC** = El personal de limpieza que recoge los platos sucios
```

---

## Visual Studio 2022 (v17.14)

### 🛠️ Ediciones

| Edición | Precio | Uso | Soporte hasta |
|---------|--------|-----|--------------|
| **Community** | Gratis | Estudiantes | Ene 2032 |
| **Professional** | $$ | Equipos | Ene 2032 |
| **Enterprise** | $$$ | Empresas | Ene 2032 |

**✅ Usaremos Community (GRATIS) - Versión actual: 17.14**

### 📦 Workloads necesarios

```
☑️ ASP.NET y desarrollo web
   ├─ ASP.NET Core
   └─ HTML/JavaScript

☑️ Almacenamiento de datos
   ├─ SQL Server Tools
   └─ Data connectivity

☑️ .NET 8 SDK (incluye .NET 10)
☑️ Git para Windows
```

**Descarga:** visualstudio.microsoft.com

---

## Estructura Programa C# y Namespaces

<div class="columns">
<div>

### 📋 Partes Esenciales

| # | Elemento | Propósito |
|---|----------|-----------|
| 1️⃣ | `using` | Importar namespaces |
| 2️⃣ | `namespace` | Organización lógica |
| 3️⃣ | `class` | Contenedor de código |
| 4️⃣ | `Main` | Punto de entrada |
| 5️⃣ | Código | Lógica ejecutable |

### 📖 Definiciones Clave

- **Namespace**: Espacio de nombres que agrupa clases relacionadas. Evita conflictos de nombres (como `System.Console` vs `MiApp.Console`).
- **Main**: Método especial donde comienza la ejecución del programa. Solo puede haber uno por aplicación. Puede retornar `void` o `int` (código de salida al sistema operativo).

> 💡 **Analogía:** El namespace es como el apellido de una persona - ayuda a distinguir entre "Juan Pérez" y "Juan García". El método Main es como la puerta principal de una casa - es por donde entra el programa cuando empieza a ejecutarse.

### 💻 Estructura Básica

```csharp
using System;

namespace MiApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("¡Hola!");
        }
    }
}
```

</div>
<div>

### 🌳 Namespaces Comunes

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

**💡 Tip:** `using System;` evita escribir `System.Console` cada vez

</div>
</div>

---

## Value Types vs Reference Types

<div class="columns">
<div>

### 📦 VALUE TYPES (Stack)

| Característica | Valor |
|----------------|-------|
| Ubicación | Stack (memoria rápida, limitada) |
| Contenido | Valor directo |
| Asignación | Copia valor |
| Ejemplos | `int`, `double`, `bool`, `struct` |

```csharp
int edad = 25;
int edad2 = edad;   // Copia
edad2 = 30;
Console.WriteLine(edad);   // 25 (independiente)
Console.WriteLine(edad2);  // 30
```

### 🎯 ¿Por qué Stack vs Heap?

**Stack:** Rápido, memoria secuencial, ideal para valores pequeños.
**Heap:** Más lento, memoria dinámica, para objetos de tamaño variable.

### 📦 STACK Visual

```
Valores independientes → Asignación = copia
```

> 💡 **Regla práctica:** Tipos "pequeños y fijos" → Stack. Tipos "grandes o variables" → Heap.

</div>
<div>

### 🔗 REFERENCE TYPES (Heap)

| Característica | Valor |
|----------------|-------|
| Ubicación | Heap (memoria dinámica, abundante) |
| Contenido | Referencia (puntero al objeto) |
| Asignación | Copia referencia |
| Ejemplos | `string`, `class`, `array`, `interface` |

```csharp
string nombre = "Juan";
string nombre2 = nombre;  // Misma ref
nombre2 = "Maria";        // Nuevo obj
Console.WriteLine(nombre);   // "Juan"
Console.WriteLine(nombre2);  // "Maria"
```

### 🔗 HEAP Visual

```
Referencias a objetos → Asignación = copia ref
```

> ⚠️ **Error común:** Al asignar un reference type, NO estás copiando el objeto, solo la referencia. Si modificas el objeto a través de la nueva variable, el cambio se refleja en ambas (para tipos mutables).

</div>
</div>

---

## Nullable Types

<div class="columns">
<div>

### 🤔 ¿Por qué?

```csharp
int edad = null;  // ❌ Error! Value types no aceptan null
```

**Cuándo se necesita:**
- Bases de datos (campos NULL)
- Formularios opcionales
- Configuraciones sin valor

### ✅ Solución: Nullable&lt;T&gt;

```csharp
int? edad = null;           // Nullable<int>
double? precio = null;      // Nullable<double>
bool? activo = null;        // Nullable<bool>
DateTime? fecha = null;     // Nullable<DateTime>
```

</div>
<div>

### 🛠️ Operadores

| Operador | Sintaxis | Descripción |
|----------|----------|-------------|
| **??** | `a ?? b` | Usa `b` si `a` es null |
| **??=** | `a ??= b` | Asigna `b` si `a` es null |
| **?.** | `a?.Prop` | Acceso seguro (no crash) |

```csharp
int? num = null;
int edad = num ?? 18;      // 18 (valor default)

string s = null;
int? len = s?.Length;      // null (no crash)
```

</div>
</div>

---

## Strings en C#

<div class="columns">
<div>

### 📝 Creación

```csharp
// 1. Interpolación ⭐
string nombre = "Juan";
string saludo = $"Hola {nombre}";

// 2. Verbatim (@)
string ruta = @"C:\Docs\file.txt";

// 3. Multilínea (C# 11+)
string texto = """
    Línea 1
    Línea 2
""";
```

### 🛠️ Métodos Clave

| Método | Resultado |
|--------|-----------|
| `Trim()` | `" hola "` → `"hola"` |
| `ToUpper()` | `"hola"` → `"HOLA"` |
| `Contains()` | `"hola".Contains("la")` → `true` |
| `Split()` | `"a,b".Split(',')` → `["a","b"]` |

</div>
<div>

### ⚠️ INMUTABILIDAD

```csharp
string s = "hola";
s.ToUpper();      // ❌ No modifica
s = s.ToUpper();  // ✅ Reasigna
```

### 💡 Conceptos Clave

- **Inmutables:** Cada operación crea un nuevo string
- **Verbatim (@):** Para rutas Windows
- **Interpolación ($):** Forma preferida
- **Multilínea:** C# 11+

</div>
</div>

---

## C# 12: Primary Constructors

<div class="columns">
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

</div>
<div>

### ✅ AHORA (Conciso)

```csharp
public class Persona(string nombre, int edad)
{
    public void Saludar() =>
        Console.WriteLine($"Hola {nombre}");

    public string Info =>
        $"{nombre} ({edad} años)";
}

// Uso
var p = new Persona("Ana", 25);
p.Saludar();  // "Hola Ana"
```

**50% menos código** • Más legible

</div>
</div>

---

## C# 12: Collection Expressions

<div class="columns">
<div>

### ❌ ANTES (Verboso)

```csharp
// Array
int[] nums = new int[] {1, 2, 3};

// List
var list = new List<int> {1, 2, 3};

// Dictionary
var dict = new Dictionary<string,int>
{
    {"Ana", 25},
    {"Juan", 30}
};
```

</div>
<div>

### ✅ AHORA (Sintaxis `[ ]`)

```csharp
// Array
int[] nums = [1, 2, 3];

// List
List<string> names = ["Ana", "Juan"];

// Spread operator
int[] pares = [2, 4, 6];
int[] impares = [1, 3, 5];
int[] all = [..pares, ..impares];
```

### 🎯 ¿Qué es el Spread Operator?

El operador `..` (spread) "desempaqueta" los elementos de una colección dentro de otra. Es como vaciar el contenido de una caja dentro de otra más grande.

```csharp
// Sin spread: crea array anidado
int[] combinado = [pares, impares];  // [[2,4,6], [1,3,5]]

// Con spread: combina elementos
int[] combinado = [..pares, ..impares];  // [2,4,6,1,3,5]
```

> ⚠️ **Error común:** Olvidar el `..` - obtienes un array anidado en lugar de una combinación plana de elementos.

</div>
</div>

---

## Pattern Matching (C# 8+)

<div class="columns">
<div>

### 🔢 Rangos con `switch`

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
    >= 4.5 => "Excelente",
    >= 3.5 => "Bueno",
    >= 3.0 => "Aceptable",
    _ => "Reprobado"
};
```

### 🎯 Por Tipo

```csharp
string desc = obj switch
{
    int i when i > 0 => $"Positivo: {i}",
    int i when i < 0 => $"Negativo: {i}",
    string s => $"Texto ({s.Length} chars)",
    null => "Sin valor",
    _ => "Otro tipo"
};
```

</div>
<div>

### 📋 List Patterns (C# 11+)

```csharp
int[] nums = [1, 2, 3];
string patron = nums switch
{
    [1, 2, 3] => "Exacto",
    [1, _, _] => "Empieza con 1",
    [_, _, 5] => "Termina con 5",
    _ => "Otro patrón"
};
```

**Beneficios:**
- ✅ Código más limpio
- ✅ Menos `if-else` anidados
- ✅ Expresivo y legible

</div>
</div>

---

## Ejercicio: Calculadora de Área

<div class="columns">
<div>

### 🎯 Objetivo
Crear app de consola que calcule área de rectángulo

### ✅ Conceptos a practicar
1. Console I/O (ReadLine/WriteLine)
2. Variables double
3. Parseo de strings
4. Interpolación de strings
5. Estructura básica C#

</div>
<div>

### 💻 Código base

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

### 🚀 Retos adicionales
- Validar que no sean negativos
- Agregar círculo y triángulo

</div>
</div>

---

## Ejercicio: Sistema de Calificaciones

<div class="columns">
<div>

### 🎯 Desafío

Crear sistema que calcule promedios con validación

### 📋 Requisitos

1. Solicitar nombre del estudiante
2. Solicitar 3 notas (rango 0.0 - 5.0)
3. Calcular promedio
4. Mostrar APROBADO/REPROBADO
5. Validar datos de entrada

### 💡 Pistas

```csharp
// Parseo
double n1 = double.Parse(Console.ReadLine());

// Promedio
double promedio = (n1 + n2 + n3) / 3;

// Condicional
string estado = promedio >= 3.0 ?
    "APROBADO" : "REPROBADO";
```

### 📊 Salida Esperada

```
================================
  SISTEMA DE CALIFICACIONES
================================
Estudiante: María López
Promedio: 4.17
Estado: ✅ APROBADO
================================
```

</div>
<div>

### 🔑 Conceptos Clave

| Método | Propósito |
|--------|-----------|
| `Parse()` | Convierte string a tipo, lanza excepción si falla |
| `TryParse()` | Retorna true/false sin excepciones |
| `while(true)` | Repite hasta válido |
| `out nota` | Parámetro salida |

### 📌 Parse vs TryParse: ¿Cuál usar?

```csharp
// ❌ Parse: puede fallar en runtime
string input = "abc";
int valor = int.Parse(input);  // 💥 FormatException

// ✅ TryParse: maneja errores gracefully
string input = "abc";
if (int.TryParse(input, out int valor))
{
    Console.WriteLine($"Valor: {valor}");
}
else
{
    Console.WriteLine("⚠️ No es un número válido");
}
```

**Regla:** Usa `TryParse` para entrada de usuario. Usa `Parse` solo cuando estás seguro del formato.

### 📝 Validación

```csharp
static double PedirNota(string etiqueta)
{
    double nota;
    while (true)
    {
        Console.Write($"{etiqueta} (0-5): ");
        if (double.TryParse(Console.ReadLine(), out nota))
        {
            if (nota >= 0 && nota <= 5)
                return nota;
            Console.WriteLine("⚠️ Fuera de rango");
        }
        else
        {
            Console.WriteLine("⚠️ No válido");
        }
    }
}
```

**✅ Ventajas:** Previene crashes • Mejora UX • Código robusto

</div>
</div>

---

## Atajos Visual Studio

<div class="columns">
<div>

### 🎯 Debugging

| Atajo | Acción |
|-------|--------|
| **F5** | Iniciar debug |
| **F9** | Toggle breakpoint |
| **F10** | Step Over |
| **F11** | Step Into |
| **Shift+F11** | Step Out |
| **Ctrl+.** | Quick Actions |

</div>
<div>

### 🛠️ Edición

| Atajo | Acción |
|-------|--------|
| **Ctrl+K,C** | Comentar |
| **Ctrl+K,U** | Descomentar |
| **Ctrl+Space** | IntelliSense |
| **F12** | Ir a definición |
| **Ctrl+R,R** | Renombrar |
| **Ctrl+-** | Navegar atrás |

</div>
</div>

---

## C# vs Otros Lenguajes (2026)

<div class="columns">
<div>

### 🏆 Rendimiento

| Operación | C# | Java | Python |
|-----------|-----|------|--------|
| Loop 1M | 15ms | 18ms | 980ms |
| Parse JSON | 90ms | 100ms | 150ms |
| Memoria | 25MB | 40MB | 15MB |

### 🌟 Casos de Uso

| Lenguaje | Mejor para |
|----------|-----------|
| **C#** | Empresas, Azure, Gaming |
| **Java** | Android, Grandes empresas |
| **Python** | Data Science, IA |
| **JS** | Frontend, Full-stack |

</div>
<div>

### 💼 Mercado Laboral Colombia 2026

| Tecnología | Demanda | Salario Junior |
|------------|---------|----------------|
| C#/.NET | ⭐⭐⭐⭐⭐ | $3M - $5M COP |
| Java | ⭐⭐⭐⭐⭐ | $3M - $5M COP |
| Python | ⭐⭐⭐⭐⭐ | $3.5M - $6M COP |
| JavaScript | ⭐⭐⭐⭐⭐ | $3M - $5M COP |

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

**IL** = Intermediate Language (MSIL)  
**JIT** = Just-In-Time Compiler  
**CLR** = Common Language Runtime

---

## Convenciones de Código

<div class="columns">
<div>

### ✅ Nomenclatura

| Elemento | Estilo | Ejemplo |
|----------|--------|---------|
| Clases | PascalCase | `StudentManager` |
| Métodos | PascalCase | `GetStudent()` |
| Propiedades | PascalCase | `Name { get; }` |
| Campos privados | _camelCase | `_count` |
| Variables | camelCase | `studentName` |
| Constantes | UPPER_SNAKE | `MAX_SIZE` |

### 📜 Reglas de Oro

- Nombres descriptivos (`CalculateTotal` > `Calc`)
- Sin abreviaturas (`customer` > `cust`)
- 4 espacios indentación

</div>
<div>

### 💻 Ejemplo Correcto

```csharp
public class StudentManager
{
    private int _studentCount;
    private const int MAX_STUDENTS = 100;
    
    public string Name { get; set; }

    public void AddStudent(string studentName)
    {
        if (_studentCount < MAX_STUDENTS)
        {
            _studentCount++;
        }
    }
}
```

</div>
</div>

---

## NuGet: Gestor de Paquetes

<div class="columns">
<div>

### 📚 ¿Qué es NuGet?

Repositorio de librerías para .NET (similar a npm para Node.js o pip para Python)

### 📖 Términos Clave de Paquetes

- **ORM (Object-Relational Mapper)**: Herramienta que mapea tablas de base de datos a objetos C#, permitiendo trabajar con BD sin escribir SQL directamente.
- **Serialización JSON**: Convertir objetos C# a texto JSON (y viceversa) para transmisión por API o almacenamiento.
- **Logging estructurado**: Registrar eventos de la aplicación con formato consistente (texto + propiedades) para facilitar análisis y debugging.

### 💻 Comandos CLI

```bash
# Agregar paquete
dotnet add package Newtonsoft.Json

# Agregar versión específica
dotnet add package Dapper --version 2.1.28

# Listar paquetes instalados
dotnet list package

# Restaurar paquetes
dotnet restore
```

### 🔗 Recursos

- **Portal:** https://www.nuget.org/
- **En VS:** Click derecho proyecto → Manage NuGet Packages

</div>
<div>

### 🔥 Paquetes Populares 2026

| Paquete | Uso | Descargas |
|---------|-----|-----------|
| **Newtonsoft.Json** | Serialización JSON | 7.5B+ |
| **Dapper** | Micro ORM para BD | 500M+ |
| **Serilog** | Logging estructurado | 300M+ |
| **xUnit** | Testing unitario | 150M+ |
| **AutoMapper** | Mapeo de objetos | 400M+ |

</div>
</div>

---

## Resumen de la Clase (1/2)

### 📚 Conceptos Clave Aprendidos

| Tema | Descripción |
|------|-------------|
| **C#** | Lenguaje moderno, orientado a objetos, type-safe |
| **.NET 8/10** | Plataforma unificada multiplataforma (LTS hasta 2026) |
| **BCL** | Base Class Library - clases predefinidas reutilizables |
| **CLR** | Máquina virtual que ejecuta código IL |
| **JIT** | Just-In-Time Compiler - IL a código máquina |
| **GC** | Garbage Collector - gestión automática de memoria |
| **Value Types** | Stack, almacenan valor directo (`int`, `double`) |
| **Reference Types** | Heap, almacenan referencia (`string`, clases) |
| **Nullable** | `int?` permite null en value types |
| **LINQ** | Consultas integradas al lenguaje |
| **C# 12** | Primary constructors, collection expressions |

---

## Resumen de la Clase (2/2)

### 🎯 Habilidades Adquiridas

- ✅ Instalar Visual Studio 2022
- ✅ Crear aplicación de consola
- ✅ Declarar variables y usar tipos
- ✅ Entrada/salida con Console
- ✅ Depurar código con breakpoints

### 🚀 Próximos Pasos

- **Clase 2:** Clases y Objetos en C#
- Completar ejercicios de práctica
- Realizar tarea asignada

---

## Tarea para Casa

<div class="columns">
<div>

### 🖥️ Instalación Obligatoria

1. Descargar **Visual Studio Community 2022**
2. Seleccionar Workloads:
   - ☑️ ASP.NET y desarrollo web
   - ☑️ Almacenamiento de datos
3. Incluir:
   - ☑️ .NET 8 SDK
   - ☑️ Git para Windows

### 💻 Proyecto: Calculadora de Promedios

Crear aplicación de consola que:
- Solicite nombre y 3 notas
- Valide rango (0.0 - 5.0)
- Calcule promedio
- Muestre APROBADO/REPROBADO

</div>
<div>

### 📋 Checklist de Entrega

- [ ] Código funcional sin errores
- [ ] Validación de datos
- [ ] Formato de salida claro
- [ ] README.md con instrucciones
- [ ] Repositorio público en GitHub

</div>
</div>

---

## 🎓 Próxima Clase: Clases y Objetos

<div class="columns">
<div>

### 📚 Temas a ver

- Programación Orientada a Objetos
- Definición de clases y objetos
- Atributos y métodos
- Encapsulamiento
- Constructores y propiedades

### 📝 Requisitos

- ✅ VS 2022 instalado
- ✅ Tarea completada
- ✅ Cuenta GitHub creada

</div>
<div>

### 🔗 Conceptos Clave

| Concepto | Definición |
|----------|------------|
| **Clase** | Plantilla de objeto |
| **Objeto** | Instancia de clase |
| **Atributo** | Características |
| **Método** | Comportamientos |

### 💡 Preparación

Repasar: ¿Qué es una clase? ¿Qué es un objeto? ¿Qué es encapsulamiento?

</div>
</div>

---

<!-- _class: lead -->

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**

📧 Contacto: [correo del docente]
🔗 Repositorio: [enlace del curso]

---

## 📚 Referencias y Fuentes

**Datos validados para 2026:**

- [.NET Support Policy](https://dotnet.microsoft.com/en-us/platform/support/policy) - Políticas oficiales de soporte .NET
- [.NET 10 Release Notes](https://github.com/dotnet/core/blob/main/release-notes/10.0/README.md) - Notas de versión .NET 10 (LTS hasta noviembre 2028)
- [Visual Studio 2022 v17.14 Release Notes](https://learn.microsoft.com/en-us/visualstudio/releases/2022/release-notes) - Notas de versión VS 2022 v17.14
- [C# 12 - What's New](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-12) - Novedades de C# 12 (noviembre 2023)
