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

### 🚀 Por qué C# en 2026?

**Aplicaciones:** 🌐 Web APIs | 🖥️ Desktop | 📱 Mobile | ☁️ Cloud | 🎮 Gaming | 🤖 AI/ML

**Ventajas:**
- ✅ Multiplataforma (Win/Linux/Mac)
- ✅ Alto rendimiento
- ✅ Type-safe
- ✅ Gran demanda laboral

---

## 💼 C# en el Mercado

<div class="columns">
<div>

### 🏢 Quién usa C#

| Empresa | Uso |
|---------|-----|
| **Microsoft** | Azure, Office 365 |
| **Unity** | 2.5M+ juegos |
| **Stack Overflow** | Backend completo |
| **Siemens** | Sistemas industriales |

</div>
<div>

### ⚖️ C# vs Competidores

| C# (2000) | Java (1995) | Python (1991) |
|-----------|-------------|---------------|
| ✅ Type-safe | ✅ JVM portable | ✅ Sintaxis simple |
| ✅ LINQ nativo | ✅ Ecosistema grande | ✅ Líder en Data |
| ✅ async/await | | |

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

## Genéricos: Type-Safety

### ❌ ANTES: ArrayList

```csharp
ArrayList lista = new ArrayList();
lista.Add(42);        // ⚠️ boxing
lista.Add("hola");    // ⚠️ mezclado

int valor = (int)lista[0]; // ⚠️ crash posible
```

**Problemas:** Sin verificación de tipos | Boxing/unboxing lento | Errores en runtime

### ✅ DESPUÉS: List&lt;T&gt;

```csharp
List<int> nums = new List<int>();
nums.Add(42);    // ✅ type-safe
// nums.Add("hola"); // ❌ error compile

int valor = nums[0]; // ✅ sin cast
```

**Ventajas:** Verificación en compilación | Sin boxing overhead | Código más rápido

---

## Anders Hejlsberg: El Arquitecto

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

> 💡 *"C# combina potencia de C++ con productividad de VB"*

---

## Ecosistema .NET: De Fragmentación a Unificación

<div class="columns">
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

**100% código compartible**

</div>
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
</div>

**Una plataforma para:** Web + Desktop + Mobile + Cloud + Gaming + AI

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

### 🛠️ Ediciones

| Edición | Precio | Uso |
|---------|--------|-----|
| **Community** | Gratis | Estudiantes |
| **Professional** | $$ | Equipos |
| **Enterprise** | $$$ | Empresas |

**✅ Usaremos Community (GRATIS)**

### 📦 Workloads necesarios

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

---

## Estructura Programa C#

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

</div>
<div>

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
</div>

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

**💡 Tip:** `using System;` evita escribir `System.Console` cada vez

---

## Value Types vs Reference Types

<div class="columns">
<div>

### 📦 VALUE TYPES (Stack)

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
Console.WriteLine(edad);   // 25 (independiente)
Console.WriteLine(edad2);  // 30
```

</div>
<div>

### 🔗 REFERENCE TYPES (Heap)

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

## Stack vs Heap: Visualización Comparativa

<div class="columns">
<div>

### 📦 STACK (Value Types)

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
```

**Características:**
- Almacena valores directos
- Cada variable es independiente
- Asignación = copia del valor

</div>
<div>

### 🔗 HEAP (Reference Types)

```
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

**Características:**
- Almacena referencias (direcciones)
- Múltiples variables pueden apuntar al mismo objeto
- Asignación = copia de la referencia

</div>
</div>

---

## Nullable Types (1/2)

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

---

## Nullable Types (2/2)

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

---

## Strings en C# - Creación

### 📝 Formas de Crear Strings

```csharp
// 1. Interpolación ⭐ RECOMENDADA
string nombre = "Juan";
int edad = 20;
string saludo = $"Hola {nombre}, tienes {edad} años";

// 2. Concatenación
string s2 = "Hola " + nombre;

// 3. Verbatim (@) - para rutas
string ruta = @"C:\Documents\archivo.txt";

// 4. Multilínea (C# 11+)
string texto = """
    Línea 1
    Línea 2
    Línea 3
""";
```

---

## Strings en C# - Métodos Útiles

### 🛠️ Métodos de Manipulación

| Método | Ejemplo | Resultado |
|--------|---------|-----------|
| `Trim()` | `" hola ".Trim()` | `"hola"` |
| `ToUpper()` | `"hola".ToUpper()` | `"HOLA"` |
| `ToLower()` | `"HOLA".ToLower()` | `"hola"` |
| `Contains()` | `"hola".Contains("la")` | `true` |
| `Split()` | `"a,b,c".Split(',')` | `["a","b","c"]` |
| `Replace()` | `"hola".Replace("o","0")` | `"h0la"` |
| `Length` | `"hola".Length` | `4` |

⚠️ **Strings son INMUTABLES:** `texto.ToUpper()` no modifica, debe reasignar: `texto = texto.ToUpper()`

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

## Ejercicio: Sistema de Calificaciones (1/2)

### 🎯 Desafío

Crear sistema que calcule promedios con validación

### 📋 Requisitos

1. Solicitar nombre del estudiante
2. Solicitar 3 notas (rango 0.0 - 5.0)
3. Calcular promedio
4. Mostrar APROBADO/REPROBADO
5. Validar datos de entrada

### 💡 Pistas de implementación

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

Notas:
  Nota 1: 4.5
  Nota 2: 3.8
  Nota 3: 4.2
--------------------------------
Promedio: 4.17
Estado: ✅ APROBADO
================================
```

---

## Validación de Entrada

<div class="columns">
<div>

### 🎯 ¿Por qué validar?

- ❌ Letras en lugar de números
- ❌ Notas fuera de rango
- ❌ Crashes inesperados

### 🔑 Conceptos Clave

| Método | Propósito |
|--------|-----------|
| `TryParse()` | Sin excepciones |
| `while(true)` | Repite hasta válido |
| `out nota` | Parámetro salida |

</div>
<div>

### 📝 Método de Validación

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

### 📚 ¿Qué es NuGet?

Repositorio de librerías para .NET (similar a npm para Node.js o pip para Python)

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

### 🔥 Paquetes Populares 2026

| Paquete | Uso | Descargas |
|---------|-----|-----------|
| **Newtonsoft.Json** | Serialización JSON | 2.5B+ |
| **Dapper** | Micro ORM para BD | 500M+ |
| **Serilog** | Logging estructurado | 300M+ |
| **xUnit** | Testing unitario | 150M+ |
| **AutoMapper** | Mapeo de objetos | 400M+ |

### 🔗 Recursos

- **Portal:** https://www.nuget.org/
- **En VS:** Click derecho proyecto → Manage NuGet Packages

---

## Resumen de la Clase

### 📚 Conceptos Clave Aprendidos

| Tema | Descripción |
|------|-------------|
| **C#** | Lenguaje moderno, orientado a objetos, type-safe |
| **.NET 8** | Plataforma unificada multiplataforma |
| **CLR** | Máquina virtual que ejecuta código IL |
| **Value Types** | Stack, almacenan valor directo (`int`, `double`) |
| **Reference Types** | Heap, almacenan referencia (`string`, clases) |
| **Nullable** | `int?` permite null en value types |
| **C# 12** | Primary constructors, collection expressions |

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
