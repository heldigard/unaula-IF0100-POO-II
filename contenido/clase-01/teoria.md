# Clase 01 - Teoría Profunda
## Introducción a C# y .NET

**IF0100 - Lenguaje de Programación OO II** | Unidad 1

---

## Tabla de Contenidos

- [Historia de C#](#historia-de-c)
- [Ecosistema .NET](#ecosistema-net)
- [Arquitectura .NET](#arquitectura-net)
- [Value vs Reference Types](#value-vs-reference-types)
- [Nullable Types](#nullable-types)
- [Strings y StringBuilder](#strings-y-stringbuilder)
- [Convenciones de Código](#convenciones-de-codigo)

---

## Historia de C#

### El Problema que C# Resolvió (2000)

**Contexto pre-C#:**
- **C++**: Poderoso pero complejo, sin garbage collection, propenso a memory leaks
- **Java**: "Write Once, Run Anywhere" pero limitado a la JVM, sin integración nativa con Windows
- **VB6**: Productivo pero no orientado a objetos, limitado para sistemas enterprise

**C# nació para:**
1. Combinar la potencia de C++ con la productividad de Visual Basic
2. Aprovechar al máximo la plataforma Windows
3. Introducir características modernas (generics, LINQ, async/await) antes que otros lenguajes

### Evolución por Versión

| Versión | Año | Innovación Clave | Impacto en la Industria |
|---------|-----|------------------|-------------------------|
| **C# 1.0** | 2000 | Lanzamiento con .NET Framework | Primer lenguaje moderno para Windows |
| **C# 2.0** | 2005 | **Generics** (`List<T>`) | Type-safe sin overhead de boxing |
| **C# 3.0** | 2007 | **LINQ**, `var`, lambdas | Revolución en consultas de datos |
| **C# 4.0** | 2010 | `dynamic`, DLR | Interoperabilidad con Python/JS |
| **C# 5.0** | 2012 | **async/await** | Programación asíncrona accesible |
| **C# 6.0** | 2015 | `$` string interpolation, null-conditional | Código más limpio y seguro |
| **C# 7.0** | 2017 | `out var`, pattern matching básico, tuples | Reducción de código boilerplate |
| **C# 8.0** | 2019 | Nullable reference types, streams | Seguridad contra null references |
| **C# 9.0** | 2020 | Records, init-only setters | Programación más funcional |
| **C# 10** | 2021 | Global usings, file-scoped namespaces | Menos repetición |
| **C# 11** | 2022 | Raw string literals, list patterns | Manejo mejorado de strings |
| **C# 12** | 2024 | **Primary constructors**, collection expressions | Sintaxis más concisa |

### El Arquitecto: Anders Hejlsberg

Anders Hejlsberg es una leyenda en el mundo de los lenguajes de programación:

| Creación | Año | Aporte |
|----------|-----|--------|
| **Turbo Pascal** | 1983 | Compilador extremadamente rápido |
| **Delphi** | 1995 | RAD (Rapid Application Development) para Windows |
| **C#** | 2000 | Lenguaje orientado a objetos moderno |
| **TypeScript** | 2012 | JavaScript con tipos para aplicaciones escalables |

> *"C# fue diseñado para ser un lenguaje simple, moderno, orientado a objetos y type-safe."* — Anders Hejlsberg

---

## Ecosistema .NET

### La Fragmentación (hasta 2016)

Antes de .NET Core (2016), existían tres plataformas separadas:

```
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   .NET Framework│  │   .NET Core     │  │    Xamarin      │
├─────────────────┤  ├─────────────────┤  ├─────────────────┤
│ Solo Windows    │  │ Open-source     │  │ iOS/Android     │
│ Web + Desktop   │  │ Cross-platform  │  │ Diferente runtime│
│ IIS hosting     │  │ Self-contained  │  │ Mono runtime     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

**Problema:** Código escrito para .NET Framework no funcionaba en .NET Core o Xamarin.

### La Unificación (.NET 5 en adelante)

A partir de .NET 5 (2020), Microsoft unificó todo:

```
┌─────────────────────────────────────────────────────────┐
│                  .NET 8 UNIFICADO                       │
│  ┌────┬────┬────┬────┬────┬────┬────┬────┬────────┐   │
│  │Web │API │MVC │Razor│Blazor│Desktop│Mobile│Cloud │   │
│  └────┴────┴────┴────┴────┴────┴────┴────┴────────┘   │
│                      ↓ UN RUNTIME                       │
│  ┌─────────────────────────────────────────────────┐   │
│  │    Win  │  Linux  │  macOS  │ iOS │ Android  │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

**Ventajas:**
- **100% de código compartible** entre plataformas
- **Un solo SDK** para todo
- **Un solo BCL** (Base Class Library)
- **Versiones sincronizadas** (no más .NET Framework 4.8 vs .NET Core 3.1)

### .NET Framework vs .NET Core vs .NET 5+

| Característica | .NET Framework | .NET Core | .NET 5+ (incluye .NET 8) |
|----------------|----------------|-----------|--------------------------|
| **Plataformas** | Solo Windows | Win/Linux/mac | Win/Linux/mac/iOS/Android |
| **Open Source** | Parcialmente | Sí | Sí |
| **Instalación** | Dependiente del sistema | Self-contained | Opción self-contained |
| **Performance** | Bueno | Mejor | Óptimo |
| **Soporte** | Maintenance solo (LTS hasta 2029) | - | Activo |
| **Usar en:** | Sistemas legacy existentes | - | NUEVOS proyectos |

**Recomendación 2026:** Usar **.NET 8 LTS** (Long Term Support hasta 2026-11-10).

---

## Arquitectura .NET

### Componentes Principales

```
┌─────────────────────────────────────────────────────────┐
│                  TU APLICACIÓN C#                       │
│           (Console, Web, Desktop, Mobile)              │
├─────────────────────────────────────────────────────────┤
│             BCL - Base Class Library                   │
│  ┌─────────┬─────────┬─────────┬─────────┬─────────┐  │
│  │ System  │Collections│  IO   │  Data  │  Net   │  │
│  │ .String │ .Generic │.File  │.SqlClient│.Http │  │
│  └─────────┴─────────┴─────────┴─────────┴─────────┘  │
├─────────────────────────────────────────────────────────┤
│             CLR - Common Language Runtime              │
│  ┌─────────┬─────────┬─────────┬─────────┬─────────┐  │
│  │   JIT   │   GC    │Exception│ Thread  │ Type   │  │
│  │Compiler │Memory   │ Handler │ Manager │ Safety │  │
│  └─────────┴─────────┴─────────┴─────────┴─────────┘  │
├─────────────────────────────────────────────────────────┤
│            Sistema Operativo (OS)                       │
│       Windows   │   Linux   │   macOS   │  iOS/Android │
└─────────────────────────────────────────────────────────┘
```

### CLR: Common Language Runtime

El CLR es la máquina virtual de .NET (similar a JVM para Java):

| Componente | Función |
|------------|---------|
| **JIT (Just-In-Time Compiler)** | Compila IL → código máquina nativo en tiempo de ejecución |
| **GC (Garbage Collector)** | Maneja automáticamente la memoria (previene memory leaks) |
| **CTS (Common Type System)** | Define tipos comunes entre todos los lenguajes .NET |
| **CLS (Common Language Specification)** | Estándar de interoperabilidad entre lenguajes |

### Flujo de Ejecución

```
1️⃣ CÓDIGO FUENTE                2️⃣ COMPILADOR C#
┌────────────────┐              ┌────────────────┐
│  Program.cs    │  Roslyn/CSC  │   Programa.exe │
│  (código C#)   │─────────────>│   (IL + Metadata)│
└────────────────┘              └───────┬────────┘
                                        │
                                        ▼
                              3️⃣ IL (Intermediate Language)
                              ┌────────────────┐
                              │  CPU-agnostic  │
                              │  (MSIL/CIL)    │
                              └───────┬────────┘
                                        │
                                        ▼
                              4️⃣ CLR + JIT EN EJECUCIÓN
                              ┌────────────────┐
                              │   Código Nativo│
                              │   (x64, ARM,   │
                              │    x86, etc.)  │
                              └────────────────┘
```

**IL (Intermediate Language):** Lenguaje intermedio, similar a bytecode de Java. Es CPU-agnostic.

**Ventajas de este diseño:**
- **Cross-platform:** El mismo IL corre en cualquier OS con CLR
- **Verificación de tipos:** El CLR verifica tipos antes de ejecutar (type safety)
- **Seguridad:** No puede acceder a memoria directamente (previene buffer overflows)

---

## Value vs Reference Types

### ¿Por qué es IMPORTANTE entender esto?

Este es el concepto **más crítico** en C#. Malentendidos causan bugs sutiles:

```csharp
// Bug común que confunde a principiantes
List<string> lista1 = ["A", "B"];
List<string> lista2 = lista1;  // ¿Copia o referencia?
lista2.Add("C");                // ¿lista1 también cambia?

Console.WriteLine(string.Join(", ", lista1));  // A, B, C (!!!)
Console.WriteLine(string.Join(", ", lista2));  // A, B, C
```

### Value Types (Tipos Valor)

**Características:**
- Almacenados en el **Stack** (pila de memoria)
- Contienen el **valor directamente**
- La asignación **copia el valor**
- Heredan de `System.ValueType`

**Tipos valor primitivos:**
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `int` | Entero 32-bit | `int edad = 25;` |
| `long` | Entero 64-bit | `long poblacion = 8000000000L;` |
| `float` | Punto flotante 32-bit | `float pi = 3.14f;` |
| `double` | Punto flotante 64-bit | `double precio = 99.99;` |
| `decimal` | Precisión financiera | `decimal dinero = 1000.50m;` |
| `bool` | Booleano | `bool activo = true;` |
| `char` | Carácter Unicode | `char letra = 'A';` |
| `byte`, `sbyte` | Entero 8-bit | `byte dato = 255;` |
| `short`, `ushort` | Entero 16-bit | `short year = 2024;` |

**Structs (tipos valor personalizados):**
```csharp
public struct Point
{
    public int X { get; set; }
    public int Y { get; set; }
}

Point p1 = new Point { X = 10, Y = 20 };
Point p2 = p1;      // Copia del valor
p2.X = 100;

Console.WriteLine(p1.X);  // 10 (no cambió)
Console.WriteLine(p2.X);  // 100
```

### Reference Types (Tipos Referencia)

**Características:**
- Almacenados en el **Heap** (montículo de memoria)
- Contienen una **referencia** al objeto
- La asignación **copia la referencia**
- Dos variables pueden referenciar el mismo objeto

**Tipos referencia comunes:**
| Tipo | Descripción |
|------|-------------|
| `string` | Cadena de texto inmutable |
| `class` | Clases (definidas por usuario) |
| `interface` | Interfaces |
| `delegate` | Delegados |
| `array` | Arreglos (`int[]`, `string[]`) |
| `object` | Tipo base de todos |

**Ejemplo con clase:**
```csharp
public class Persona
{
    public string Nombre { get; set; }
}

Persona p1 = new Persona { Nombre = "Juan" };
Persona p2 = p1;      // Copia la referencia (ambos apuntan al mismo objeto)
p2.Nombre = "María";   // Modifica el objeto compartido

Console.WriteLine(p1.Nombre);  // María (!!!)
Console.WriteLine(p2.Nombre);  // María
```

### Visualización de Memoria

```
VALUE TYPE (Stack)
┌─────────────────────────────────┐
│ int edad = 25;                  │
│ ┌───┐                           │
│ │25 │ ← Valor almacenado aquí  │
│ └───┘                           │
└─────────────────────────────────┘

REFERENCE TYPE (Stack + Heap)
┌─────────────────────────────────┐
│ STACK                           │
│ ┌───┐                           │
│ │►──┼─────┐                     │
│ └───┘     │                     │
│           ▼                     │
│ HEAP     ┌─────────────────┐    │
│         │ "Juan Pérez"    │    │
│         │ 1000h           │    │
│         └─────────────────┘    │
└─────────────────────────────────┘
```

### Implicaciones Prácticas

#### 1. Pasaje de parámetros

```csharp
void ModificarValue(int x)
{
    x = 100;  // Solo modifica la copia local
}

void ModificarReference(List<int> lista)
{
    lista.Add(100);  // Modifica el objeto original
}

int numero = 5;
ModificarValue(numero);
Console.WriteLine(numero);  // 5 (no cambió)

List<int> numeros = [1, 2, 3];
ModificarReference(numeros);
Console.WriteLine(string.Join(", ", numeros));  // 1, 2, 3, 100 (cambió)
```

#### 2. Comparación de igualdad

```csharp
// Value types: comparan VALOR
int a = 5;
int b = 5;
Console.WriteLine(a == b);  // True (mismo valor)

// Reference types: comparan REFERENCIA (por defecto)
string s1 = new string("hola");
string s2 = new string("hola");
Console.WriteLine(ReferenceEquals(s1, s2));  // False (distintos objetos)
Console.WriteLine(s1 == s2);  // True (string sobrecarga ==)
```

#### 3. Boxing y Unboxing

Convertir un value type a reference type (boxing) tiene costo de performance:

```csharp
int numero = 42;        // Value type (stack)
object obj = numero;    // Boxing (heap)
int numero2 = (int)obj; // Unboxing (copiar de vuelta)
```

**Boxing/Unboxing es costoso** porque requiere copiar entre stack y heap. Evitarlo en loops críticos.

---

## Nullable Types

### El Problema: Value Types NO aceptan null

```csharp
int edad = null;  // ❌ Error CS0037: Cannot convert null to 'int'
```

**¿Por qué esto es un problema?**

En el mundo real, muchos valores son "opcionales" o "desconocidos":
- Bases de datos: `columna INT NULL`
- Formularios: campo opcional sin llenar
- APIs: JSON con propiedades opcionales
- Configuraciones: valores no definidos

### Solución 1: Nullable<T> (Sintaxis `T?`)

```csharp
int? edad = null;           // Equivalente a Nullable<int>
double? precio = null;      // Nullable<double>
bool? activo = null;        // Nullable<bool>
DateTime? fechaNacimiento = null;  // Nullable<DateTime>
```

**Estructura interna de `Nullable<T>`:**
```csharp
public struct Nullable<T> where T : struct
{
    public bool HasValue { get; }  // true si tiene valor
    public T Value { get; }        // lanza excepción si HasValue == false
}
```

### Operadores Nullable

| Operador | Descripción | Ejemplo |
|----------|-------------|---------|
| **`??`** (null-coalescing) | Valor por defecto si es null | `int edad = x ?? 18;` |
| **`??=`** (null-coalescing assignment) | Asignar si es null | `x ??= y;` |
| **`?.`** (null-conditional) | Acceso seguro (no lanza) | `s?.Length` |
| **`?[]`** (null-conditional element) | Elemento seguro | `arr?[0]` |

```csharp
// ?? : null-coalescing operator
int? edad = null;
int edadDefinida = edad ?? 18;  // Si null, usa 18

// ??= : null-coalescing assignment
List<string>? nombres = null;
nombres ??= new List<string>();  // Inicializa si es null

// ?. : null-conditional access
string? texto = null;
int? longitud = texto?.Length;  // null (no crash)
```

### Patrón Real: Base de Datos → DTO → UI

```csharp
// Tabla SQL con columna NULL
CREATE TABLE Estudiantes (
    Id INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Telefono NVARCHAR(20) NULL  -- Puede ser NULL
);

// DTO (Data Transfer Object)
public class EstudianteDto
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public string? Telefono { get; set; }  // nullable en C#
}

// Lectura desde BD
using (var cmd = new SqlCommand("SELECT * FROM Estudiantes", conn))
using (var reader = cmd.ExecuteReader())
{
    while (reader.Read())
    {
        var estudiante = new EstudianteDto
        {
            Id = reader.GetInt32("Id"),
            Nombre = reader.GetString("Nombre"),
            Telefono = reader.IsDBNull("Telefono")
                ? null  // NULL en BD → null en C#
                : reader.GetString("Telefono")
        };
    }
}

// UI: Mostrar teléfono o "No registrado"
lblTelefono.Text = estudiante.Telefono ?? "No registrado";
```

### Nullable Reference Types (C# 8+)

Desde C# 8, los **reference types también pueden ser nullable**:

```csharp
// C# 8+ con nullable reference types habilitados
string nombre = null;      // Advertencia: posible null
string? apellido = null;   // OK, explícitamente nullable

// El compilador ayuda a prevenir NullReferenceException
if (apellido != null)
{
    Console.WriteLine(apellido.Length);  // Seguro, el compilador sabe que no es null
}
```

**Habilitar nullable reference types en el proyecto (.csproj):**
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
```

---

## Strings y StringBuilder

### String es Inmutable

```csharp
string s = "hola";
s.ToUpper();           // ❌ No modifica s
Console.WriteLine(s);  // "hola"

s = s.ToUpper();       // ✅ Crea nuevo string y reasigna
Console.WriteLine(s);  // "HOLA"
```

**¿Por qué inmutabilidad?**
- **Thread-safe:** Puede compartirse entre hilos sin locks
- **Hashing estable:** `string.GetHashCode()` nunca cambia
- **Interning:** Ahorra memoria reusing strings iguales

**Costo oculto:**
```csharp
// Código INEFICIENTE (crea 1000 strings en memoria)
string resultado = "";
for (int i = 0; i < 1000; i++)
{
    resultado += i + ",";  // Cada += crea un nuevo string
}
```

### StringBuilder para Mutación Eficiente

```csharp
using System.Text;

// Código EFICIENTE (un solo objeto mutable)
var sb = new StringBuilder();
for (int i = 0; i < 1000; i++)
{
    sb.Append(i);
    sb.Append(',');
}
string resultado = sb.ToString();  // Solo crea un string al final
```

### Cuándo usar StringBuilder vs String

| Escenario | Usar | Performance |
|-----------|------|-------------|
| Concatenar 2-3 strings | `+` o `$` | Igual |
| Concatenar en loop | `StringBuilder` | **10-100x más rápido** |
| String de formato complejo | `$` interpolation | Más legible |
| Manipulaciones intensivas | `StringBuilder` | Más eficiente |
| Strings inmutables (claves, IDs) | `string` | Mejor diseño |

### Interpolación de Strings (`$`)

**C# 6+ (recomendado):**
```csharp
string nombre = "Juan";
int edad = 25;
string mensaje = $"Hola, {nombre}. Tienes {edad} años.";
```

**Formateo:**
```csharp
double precio = 1234.5678;
Console.WriteLine($"Precio: {precio:C2}");    // Precio: $1,234.57 (moneda)
Console.WriteLine($"Porcentaje: {precio:P2}"); // Porcentaje: 123,456.78 %
Console.WriteLine($"Fecha: {DateTime.Now:D}"); // Fecha: lunes, 1 de febrero de 2026
Console.WriteLine($"Num: {1234.56:F2}");       // Num: 1234.56
Console.WriteLine($"Num: {1234.56:N2}");       // Num: 1,234.56 (con separadores)
```

**Specificadores de formato:**
| Especificador | Descripción | Ejemplo |
|---------------|-------------|---------|
| `C` / `c` | Moneda | `123.4567.ToString("C")` → `$123.46` |
| `D` / `d` | Decimal (enteros) | `1234.ToString("D6")` → `001234` |
| `E` / `e` | Notación científica | `1234.ToString("E2")` → `1.23E+003` |
| `F` / `f` | Punto fijo | `1234.5678.ToString("F2")` → `1234.57` |
| `N` / `n` | Numérico (con separadores) | `1234.56.ToString("N2")` → `1,234.57` |
| `P` / `p` | Porcentaje | `0.1234.ToString("P2")` → `12.34%` |
| `X` / `x` | Hexadecimal | `255.ToString("X")` → `FF` |

### String Interpolation con Alineación

```csharp
var personas = new[]
{
    new { Nombre = "Juan", Edad = 25 },
    new { Nombre = "María", Edad = 30 },
    new { Nombre = "Pedro", Edad = 20 }
};

Console.WriteLine($"{"Nombre",-15} {"Edad",5}");  // -15 = alinear izquierda, 15 caracteres
Console.WriteLine(new string('-', 20));

foreach (var p in personas)
{
    Console.WriteLine($"{p.Nombre,-15} {p.Edad,5}");
}

// Salida:
// Nombre          Edad
// --------------------
// Juan               25
// María              30
// Pedro              20
```

### Raw String Literals (C# 11+)

**Para JSON, SQL, HTML:**
```csharp
// JSON
string json = """
    {
        "nombre": "Juan",
        "edad": 25,
        "activo": true
    }
    """;

// SQL
string sql = """
    SELECT *
    FROM Estudiantes
    WHERE Edad > @edadMinima
    ORDER BY Nombre
    """;

// HTML
string html = """
    <div class="card">
        <h1>Título</h1>
        <p>Contenido</p>
    </div>
    """;
```

### StringComparison (Importante para búsquedas)

```csharp
string a = "café";
string b = "CAFE";

// Default: culture-sensitive (puede dar resultados inesperados)
bool igual1 = a.Equals(b);  // False

// Ordinal: comparación byte-a-byte (recomendado para IDs, claves)
bool igual2 = a.Equals(b, StringComparison.Ordinal);  // False

// OrdinalIgnoreCase: case-insensitive byte-a-byte
bool igual3 = a.Equals(b, StringComparison.OrdinalIgnoreCase);  // True
```

**Recomendación:** Siempre especificar `StringComparison` para búsquedas.

---

## Convenciones de Código

### Nomenclatura en C#

| Tipo | Convención | Ejemplo |
|------|------------|---------|
| **Clases** | PascalCase | `StudentManager`, `DbContext` |
| **Interfaces** | PascalCase con prefijo `I` | `IRepository`, `ILogger` |
| **Métodos** | PascalCase | `GetStudent()`, `CalculateTotal()` |
| **Propiedades** | PascalCase | `Name`, `IsActive` |
| **Campos públicos** | PascalCase | `const int MaxSize = 100;` |
| **Campos privados** | `_camelCase` con guion bajo | `_studentCount`, `_isActive` |
| **Variables locales** | camelCase | `studentName`, `totalAmount` |
| **Constantes** | UPPER_SNAKE_CASE | `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT` |
| **Parámetros** | camelCase | `firstName`, `pageIndex` |

### Ejemplo Completo

```csharp
using System;
using System.Collections.Generic;

namespace University.System
{
    // Clase: PascalCase
    public class StudentManager
    {
        // Constantes: UPPER_SNAKE_CASE
        private const int MAX_STUDENTS = 1000;
        private const string DEFAULT_STATUS = "Active";

        // Campos privados: _camelCase
        private int _studentCount;
        private readonly List<Student> _students;

        // Constructor: PascalCase
        public StudentManager()
        {
            _students = new List<Student>();
            _studentCount = 0;
        }

        // Propiedad: PascalCase
        public int StudentCount => _studentCount;

        // Método: PascalCase
        public void AddStudent(Student student)
        {
            if (_studentCount >= MAX_STUDENTS)
            {
                throw new InvalidOperationException($"Cannot exceed {MAX_STUDENTS} students");
            }

            // Parámetro: camelCase
            _students.Add(student);
            _studentCount++;
        }

        public Student? FindStudent(int studentId)  // Nullable return
        {
            foreach (var student in _students)  // Variable: camelCase
            {
                if (student.Id == studentId)
                {
                    return student;
                }
            }
            return null;
        }
    }

    // Clase de modelo
    public class Student
    {
        // Propiedades auto-implementadas: PascalCase
        public int Id { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public DateTime EnrollmentDate { get; set; }
        public bool IsActive { get; set; }

        // Método: PascalCase
        public string GetFullName() => $"{FirstName} {LastName}";
    }

    // Interface: PascalCase con prefijo I
    public interface IStudentRepository
    {
        Student? GetById(int id);
        void Add(Student student);
        void Update(Student student);
        void Delete(int id);
    }
}
```

### Reglas de Oro

1. **Nombres descriptivos**
   ```csharp
   // ❌ Mal
   var d = Calc(x, y);

   // ✅ Bien
   var discount = CalculateDiscount(originalPrice, couponCode);
   ```

2. **Sin abreviaturas oscuras**
   ```csharp
   // ❌ Mal
   string fn;  // ¿firstName? fileName? functionNumber?
   List<Student> stds;

   // ✅ Bien
   string firstName;
   List<Student> students;
   ```

3. **Booleanos con prefijos interrogativos**
   ```csharp
   // ✅ Bien
   bool isValid;
   bool hasPermission;
   bool canExecute;
   bool shouldUpdate;

   // ❌ Evitar
   bool valid;
   bool permission;
   ```

4. **Enumeraciones en singular (no plural)**
   ```csharp
   // ✅ Bien
   public enum Status { Active, Inactive, Pending }
   public enum Color { Red, Green, Blue }

   // ❌ Evitar (a menos que sea flags)
   public enum Statuses { ... }  // No
   ```

5. **Async methods con sufijo `Async`**
   ```csharp
   // ✅ Bien
   public async Task<Student> GetStudentAsync(int id)
   {
       return await _context.Students.FindAsync(id);
   }
   ```

### Organización de Archivos

```
Project/
├── Models/
│   ├── Student.cs
│   └── Course.cs
├── Services/
│   ├── IStudentService.cs
│   └── StudentService.cs
├── Repositories/
│   ├── IStudentRepository.cs
│   └── StudentRepository.cs
├── Controllers/
│   └── StudentsController.cs
└── Program.cs (o Main.cs)
```

**Un archivo = Una clase** (excepto clases muy pequeñas relacionadas).

---

## Referencias Adicionales

### Lecturas Recomendadas
- [C# Language Specification](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/)
- [.NET Architecture](https://learn.microsoft.com/en-us/dotnet/standard/framework/)
- [Memory Management in .NET](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/)

### Videos Recomendados
- [C# 12 Features Explained](https://www.youtube.com/results?search_query=c%23+12+features)
- [Stack vs Heap Explained](https://www.youtube.com/results?search_query=stack+vs+heap+c%23)

---

**Volver al [índice](./README.md)**
