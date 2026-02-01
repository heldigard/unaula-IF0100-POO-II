---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<style>
section {
  font-size: 20px;
  overflow: hidden;
}
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
}
section h1 { font-size: 1.8em; }
section h2 { font-size: 1.4em; }
section h3 { font-size: 1.2em; }
section ul, section ol { font-size: 0.9em; margin-left: 1em; }
section li { margin-bottom: 0.3em; }
section pre { font-size: 0.7em; max-height: 60vh; overflow-y: auto; }
section code { font-size: 0.85em; }
section p { margin: 0.5em 0; }
section table { width: 100%; font-size: 0.85em; border-collapse: collapse; margin: 0.5em auto; }
section th { background-color: #1e40af; color: white; padding: 0.4em 0.6em; text-align: left; font-size: 0.9em; border: 1px solid #ddd; }
section td { padding: 0.4em 0.6em; border: 1px solid #ddd; vertical-align: top; word-wrap: break-word; font-size: 0.85em; }
section tbody tr:nth-child(even) { background-color: #f8f9fa; }
section tbody tr:hover { background-color: #e9ecef; }
</style>

---

# Introducción a C# y .NET

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Comprender** la historia y evolución de C# y .NET
2. **Diferenciar** entre .NET Framework, .NET Core y .NET 8
3. **Configurar** el entorno de desarrollo con Visual Studio 2022
4. **Crear** su primera aplicación en C#
5. **Identificar** la estructura básica de un programa C#

**Duración:** 90 minutos

---

## Agenda

1. ¿Qué es C#? Historia y características (15 min)
2. El ecosistema .NET (15 min)
3. Instalación y configuración de Visual Studio (15 min)
4. Estructura de un programa C# (20 min)
5. Práctica: "Hola Mundo" y conceptos básicos (25 min)

---

## 1. ¿Qué es C#?

### ¿Por qué C# en 2026?

**Razones para aprenderlo:**
- 🚀 **Versátil:** Web, Desktop, Mobile, Cloud, Games, IoT
- 💼 **Demanda laboral:** Alto en empresas grandes
- 🆓 **Gratis y multiplataforma:** Con .NET (Windows, Linux, macOS)
- 🎮 **Unity:** Motor de juegos más popular usa C#
- ☁️ **Cloud:** Azure tiene soporte nativo
- 📈 **Moderno:** Actualizaciones anuales con nuevas características

**Empresas que usan C#:** Microsoft, Stack Overflow, Alibaba, Delivery Hero


### Definición

> **C# (C Sharp)** es un lenguaje de programación moderno, orientado a objetos y type-safe desarrollado por Microsoft como parte de su plataforma .NET.

```
┌─────────────────────────────────────────────────────────┐
│                    C# ES...                             │
├─────────────────────────────────────────────────────────┤
│ ✅ Orientado a objetos (POO puro)                       │
│ ✅ Type-safe (seguridad de tipos)                       │
│ ✅ Moderno (actualizado constantemente)                 │
│ ✅ Multiplataforma (Windows, Linux, macOS)              │
│ ✅ Versátil (web, desktop, móvil, cloud, IoT)           │
│ ✅ Potente (usado por empresas globales)                │
└─────────────────────────────────────────────────────────┘
```

---

## Historia de C#

### Evolución del lenguaje

```
2000        2005        2010        2015        2020        2024
  │           │           │           │           │           │
  ▼           ▼           ▼           ▼           ▼           ▼
┌────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐    ┌──────┐
│C#  │    │ C# 2 │    │ C# 5 │    │ C# 6 │    │ C# 9 │    │ C# 12│
│1.0 │    │Generics│   │async/ │    │.NET  │    │.NET 5│    │.NET 8│
│    │    │      │    │await  │    │Core   │    │      │    │      │
└────┘    └──────┘    └──────┘    └──────┘    └──────┘    └──────┘
  │           │           │           │           │           │
  ▼           ▼           ▼           ▼           ▼           ▼
 Nace      Genéricos    Programación   .NET Core    Unificación    Actual
 Microsoft  (List<T>)    asíncrona      (open source)  de .NET      LTS
```

---

## Creadores de C#

### Anders Hejlsberg - El arquitecto principal

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

**👤 Perfil Profesional**

- **Nacionalidad:** Danesa 🇩🇰
- **Posición:** Chief Architect at Microsoft
- **Años activo:** 1996 - presente

**🏆 Contribuciones Tecnológicas:**

| Año | Tecnología | Impacto |
|-----|------------|---------|
| 1995 | Delphi | Revolucionó el desarrollo Windows |
| 2000 | C# | Lenguaje flagship de Microsoft |
| 2002 | .NET | Plataforma de desarrollo unificada |
| 2012 | TypeScript | JavaScript con tipos estáticos |

</div>

<div style="flex: 1;">

**💡 Filosofía de Diseño:**

> *"C# es el lenguaje que siempre quise tener para desarrollo empresarial. Combina la potencia de C++ con la productividad de Visual Basic."*

**🎯 Principios aplicados:**
- ✅ Productividad del desarrollador
- ✅ Seguridad de tipos en tiempo de compilación
- ✅ Orientación a objetos pura
- ✅ Evolución continua con retrocompatibilidad
- ✅ Código limpio y expresivo

</div>

</div>

---

### Influencia en la Industria

```
┌─────────────────────────────────────────────────────────────┐
│  ANTES DE C# (finales 90s)          DESPUÉS DE C# (2000+)   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Java: Líder pero limitado          C#: Competencia real    │
│  C++: Poderoso pero complejo        Sintaxis familiar       │
│  VB: Fácil pero poco robusto        Type-safe + Productivo  │
│  PHP: Solo web                      Multiplataforma real    │
│                                                             │
│  ────────────────────────────────────────────────────────  │
│                                                             │
│  🎯 Resultado: Microsoft recupera terreno en empresas       │
│     Grandes corporaciones adoptan .NET para sistemas críticos│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. El Ecosistema .NET

### ¿Qué es .NET?

> **.NET** es una plataforma de desarrollo unificada para construir cualquier tipo de aplicación: web, móvil, desktop, cloud, IoT, AI.

---

### Componentes del Ecosistema .NET

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

**🌐 ASP.NET Core**
- Aplicaciones web MVC
- Web APIs RESTful
- Aplicaciones en tiempo real (SignalR)

**🖥️ Desktop**
- WPF (Windows Presentation Foundation)
- WinForms (Aplicaciones tradicionales)
- .NET MAUI (Multiplataforma)

**📱 Mobile**
- .NET MAUI para iOS/Android
- Xamarin (legacy)

</div>

<div style="flex: 1;">

**☁️ Cloud**
- Azure SDK para C#
- Azure Functions (serverless)
- Microservicios con Docker

**🎮 Gaming**
- Unity (motor de juegos líder)
- Unreal Engine con C#

**🤖 ML/AI**
- ML.NET (machine learning)
- Integración con Azure AI

</div>

</div>

---

### Visualización del Ecosistema

![Ecosistema .NET](../../assets/infografias/clase-01-ecosistema-dotnet.png){: style="max-width: 55%; max-height: 350px; display: block; margin: 0 auto;"}

*El diagrama muestra cómo .NET 8 unifica todas las plataformas bajo un solo runtime, permitiendo compartir código entre diferentes tipos de aplicaciones.*

---

### Representación ASCII:

```
┌────────────────────────────────────────────────────────────┐
│                      .NET 8 (2024)                         │
│                    ┌──────────────────┐                    │
│                    │   UNIFICADO      │                    │
│                    │   Una sola       │                    │
│                    │   plataforma     │                    │
│                    └────────┬─────────┘                    │
│                             │                              │
├─────────────────────────────┼──────────────────────────────┤
│                             ▼                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Web     │  │ Desktop  │  │  Mobile  │  │  Cloud   │   │
│  │ASP.NET   │  │WPF/WinForms│ │  .NET MAUI│  │  Azure   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   API    │  │   IoT    │  │ Machine  │  │  Gaming  │   │
│  │REST/gRPC │  │Raspberry │  │ Learning │  │Unity/Unreal│  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└────────────────────────────────────────────────────────────┘
```

---

## Evolución de .NET

### Las tres eras de .NET

| Era | Período | Características |
| ----- | --------- | ----------------- |
| **.NET Framework** | 2002-2024 | Windows-only, monolítico, cerrado |
| **.NET Core** | 2016-2020 | Open source, multiplataforma, modular |
| **.NET 5+** | 2020-presente | Unificación, una sola plataforma |

```
.NET Framework              .NET Core                .NET 5+
     │                          │                        │
     │  ┌────────────────┐      │                        │
     └──┤  CONVERGENCIA  ├──────┘                        │
        └────────────────┘                               │
                 │                                       │
                 └───────────────────────────────────────┘
                                         │
                                    ┌────┴────┐
                                    │  .NET 8 │
                                    │  (LTS)  │
                                    └─────────┘
```

---

## Arquitectura de .NET

### Componentes principales

```
┌─────────────────────────────────────────────────────────────┐
│                    APLICACIÓN C#                            │
├─────────────────────────────────────────────────────────────┤
│                  Base Class Library (BCL)                   │
│     (System.String, System.Collections, System.IO...)      │
├─────────────────────────────────────────────────────────────┤
│                    Common Language Runtime (CLR)            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   JIT       │  │   Garbage   │  │   Type Safety      │ │
│  │ Compiler    │  │ Collector   │  │   Security         │ │
│  │             │  │             │  │   Exception Hand.  │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                 Sistema Operativo                           │
│              (Windows / Linux / macOS)                      │
└─────────────────────────────────────────────────────────────┘
```

---

## Common Language Runtime (CLR)

### El motor de ejecución

```csharp
// Tu código C#
string nombre = "UNAULA";
Console.WriteLine($"Hola, {nombre}!");

         ↓ Compilación (csc.exe)

// CIL (Common Intermediate Language) - Código intermedio
IL_0000: ldstr "UNAULA"
IL_0005: stloc.0
IL_0006: ldstr "Hola, {0}!"
IL_000b: ldloc.0
IL_000c: call string.Format
IL_0011: call Console.WriteLine

         ↓ JIT Compiler (en tiempo de ejecución)

// Código máquina nativo (x64, ARM, etc.)
// Ejecutado por el procesador
```

---

## 3. Visual Studio 2022

### El IDE oficial para desarrollo .NET

```
┌─────────────────────────────────────────────────────────────┐
│  🛠️ VISUAL STUDIO 2022 - Ediciones                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Community   │  │ Professional │  │  Enterprise  │      │
│  │   (Gratis)   │  │   ($$)       │  │   ($$$)      │      │
│  │              │  │              │  │              │      │
│  │ ✅ Estudiantes│  │ ✅ Profesionales│  │ ✅ Grandes    │  │
│  │ ✅ Open source│  │ ✅ Small teams │  │    empresas   │  │
│  │ ✅ Individual │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
│  💡 Usaremos: Visual Studio 2022 Community (gratuita)      │
└─────────────────────────────────────────────────────────────┘
```

---

## Instalación de Visual Studio 2022

### Pasos y workloads necesarios

```
1. Descargar desde: https://visualstudio.microsoft.com/

2. Ejecutar el instalador (Visual Studio Installer)

3. Seleccionar Workloads:
   
   ☑️ Desarrollo de ASP.NET y web
      ├─ ASP.NET
      ├─ HTML/JavaScript
      └─ Herramientas de desarrollo web
   
   ☑️ Almacenamiento y procesamiento de datos
      ├─ SQL Server Data Tools
      └─ Conectividad de datos

4. Pestaña "Componentes individuales":
   ☑️ .NET 8 SDK
   ☑️ Git para Windows
```

---

## 4. Estructura de un Programa C#

### Anatomía de una aplicación console

```csharp
// 1. DIRECTIVAS USING - Importar namespaces
using System;                    // Funcionalidad básica
using System.Collections.Generic; // Colecciones

// 2. DECLARACIÓN DE NAMESPACE - Organización
namespace MiPrimeraApp
{
    // 3. DECLARACIÓN DE CLASE
    class Program
    {
        // 4. MÉTODO MAIN - Punto de entrada
        static void Main(string[] args)
        {
            // 5. CUERPO DEL PROGRAMA
            Console.WriteLine("¡Hola, UNAULA!");
        }
    }
}
```

---

## Namespace (Espacio de Nombres)

### Organización jerárquica

```
System                          ← Nivel raíz
├── System.Console              ← Console.WriteLine
├── System.String               ← Cadena de texto
├── System.Collections          ← Colecciones
│   ├── System.Collections.Generic  ← List<T>, Dictionary<K,V>
│   └── System.Collections          ← ArrayList (legacy)
├── System.IO                   ← Archivos y streams
├── System.Data                 ← ADO.NET
│   └── System.Data.SqlClient   ← SQL Server
└── System.Net                  ← Red e Internet
    └── System.Net.Http         ← HttpClient

// Usando using
using System;
using System.Collections.Generic;
```

---

## Tipos de Proyectos en C#

### ¿Qué podemos crear?

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE PROYECTO                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🖥️ APLICACIONES DE ESCRITORIO                              │
│     • Console App        → Aplicaciones de línea de comandos│
│     • WPF (Windows Presentation Foundation) → Modernas      │
│     • WinForms           → Tradicionales Windows            │
│                                                             │
│  🌐 APLICACIONES WEB                                        │
│     • ASP.NET Core Web App      → Páginas web dinámicas     │
│     • ASP.NET Core Web API      → Servicios REST            │
│     • Blazor Web Assembly       → SPA con C# en navegador   │
│                                                             │
│  📱 OTRAS                                                   │
│     • .NET MAUI          → Multiplataforma (iOS, Android)   │
│     • Class Library      → Bibliotecas reutilizables        │
│     • Unit Test Project  → Pruebas unitarias                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Sintaxis Básica de C#

### Comparación con Java y Python

```csharp
// C# - Nuestro lenguaje
string nombre = "Juan";
int edad = 20;
Console.WriteLine($"Hola {nombre}, tienes {edad} años");
```

```java
// Java - Similar a C#
String nombre = "Juan";
int edad = 20;
System.out.println("Hola " + nombre + ", tienes " + edad + " años");
```

```python
# Python - Más simple
nombre = "Juan"
edad = 20
print(f"Hola {nombre}, tienes {edad} años")
```

**C# se siente familiar si conoces Java o C++**

---

## Variables y Tipos de Datos

### Sistema de tipos de C#

```csharp
// TIPOS DE VALOR (almacenados en stack)
int entero = 42;                    // Entero 32-bit
long grande = 9999999999L;          // Entero 64-bit
double decimal = 3.14159;           // Punto flotante
bool logico = true;                 // Booleano
char caracter = 'A';                // Carácter Unicode

// TIPOS DE REFERENCIA (almacenados en heap)
string texto = "Hola Mundo";        // Cadena de texto
object cualquiera = 123;            // Tipo base de todos

// INFERENCIA DE TIPO (var)
var nombre = "UNAULA";   // El compilador infiere: string
var edad = 20;           // El compilador infiere: int
```

---
### Ejercicio en clase (25 min)


**Objetivo:** Crear una aplicación de consola que calcule el área de un rectángulo

```csharp
using System;

namespace CalculadoraArea
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== CALCULADORA DE ÁREA ===");
            
            // Entrada de datos
            Console.Write("Ingrese la base: ");
            double baseRect = double.Parse(Console.ReadLine());
            
            Console.Write("Ingrese la altura: ");
            double altura = double.Parse(Console.ReadLine());
            
            // Cálculo
            double area = baseRect * altura;
            
            // Salida
            Console.WriteLine($"El área es: {area:F2}");
            
            Console.ReadKey();
        }
    }
}
```

---

## Ejercicios Prácticos Adicionales

### Ejercicio 1: Calculadora Simple

```csharp
using System;

namespace Calculadora
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== CALCULADORA SIMPLE ===\n");
            
            Console.Write("Número 1: ");
            double num1 = double.Parse(Console.ReadLine());
            
            Console.Write("Operación (+ - * /): ");
            char op = Console.ReadLine()[0];
            
            Console.Write("Número 2: ");
            double num2 = double.Parse(Console.ReadLine());
            
            double resultado = 0;
            bool valido = true;
            
            switch (op)
            {
                case '+': resultado = num1 + num2; break;
                case '-': resultado = num1 - num2; break;
                case '*': resultado = num1 * num2; break;
                case '/': 
                    if (num2 != 0) resultado = num1 / num2;
                    else { Console.WriteLine("Error: División por cero"); valido = false; }
                    break;
                default: Console.WriteLine("Operación inválida"); valido = false; break;
            }
            
            if (valido)
                Console.WriteLine($"\nResultado: {resultado:F2}");
            
            Console.ReadKey();
        }
    }
}
```

### Ejercicio 2: Conversor de Temperatura

```csharp
using System;

namespace Temperatura
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== CONVERSOR DE TEMPERATURA ===\n");
            
            Console.Write("Ingrese temperatura en Celsius: ");
            double celsius = double.Parse(Console.ReadLine());
            
            // Fórmulas de conversión
            double fahrenheit = (celsius * 9 / 5) + 32;
            double kelvin = celsius + 273.15;
            
            Console.WriteLine("\n--- Resultados ---");
            Console.WriteLine($"{celsius}°C = {fahrenheit:F2}°F");
            Console.WriteLine($"{celsius}°C = {kelvin:F2}K");
            
            // Evaluar estado del agua
            if (celsius <= 0)
                Console.WriteLine("→ El agua está en estado SÓLIDO (hielo)");
            else if (celsius >= 100)
                Console.WriteLine("→ El agua está en estado GASEOSO (vapor)");
            else
                Console.WriteLine("→ El agua está en estado LÍQUIDO");
            
            Console.ReadKey();
        }
    }
}
```

---

## Ejercicio Propuesto en Clase

### Calculadora de Promedio Estudiantil

```csharp
// Ejercicio: Calcular promedio de 3 notas
// El programa debe:
// 1. Pedir nombre del estudiante
// 2. Pedir 3 notas (decimal)
// 3. Calcular promedio
// 4. Mostrar si aprobó (>= 3.0) o reprobó
// 5. Manejar errores de entrada (validar números)

// Ejemplo de salida:
// ================================
//   SISTEMA DE CALIFICACIONES
// ================================
// Estudiante: María López
// Nota 1: 4.5
// Nota 2: 3.8
// Nota 3: 4.2
// -------------------------------
// Promedio: 4.17
// Estado: ✅ APROBADO
// ================================
```

---

## Ejercicio con Manejo de Errores

### Validación de entrada de datos

```csharp
using System;

namespace ValidacionNotas
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== CALCULADORA DE PROMEDIO CON VALIDACIÓN ===\n");

            // Pedir nombre
            Console.Write("Nombre del estudiante: ");
            string nombre = Console.ReadLine();

            double nota1 = PedirNota("Nota 1");
            double nota2 = PedirNota("Nota 2");
            double nota3 = PedirNota("Nota 3");

            double promedio = (nota1 + nota2 + nota3) / 3.0;

            Console.WriteLine($"\n=== RESULTADO ===");
            Console.WriteLine($"Estudiante: {nombre}");
            Console.WriteLine($"Promedio: {promedio:F2}");
            Console.WriteLine($"Estado: {(promedio >= 3.0 ? "✅ APROBADO" : "❌ REPROBADO")}");

            Console.ReadKey();
        }

        static double PedirNota(string etiqueta)
        {
            double nota;
            while (true)
            {
                Console.Write($"{etiqueta} (0.0 - 5.0): ");
                if (double.TryParse(Console.ReadLine(), out nota))
                {
                    if (nota >= 0.0 && nota <= 5.0)
                        return nota;
                    Console.WriteLine("  ⚠️ Error: La nota debe estar entre 0.0 y 5.0");
                }
                else
                {
                    Console.WriteLine("  ⚠️ Error: Ingrese un número válido");
                }
            }
        }
    }
}
```

---

## Atajos de Visual Studio Útiles

### Productividad

| Atajo | Acción |
| ------- | -------- |
| `Ctrl + K, Ctrl + C` | Comentar selección |
| `Ctrl + K, Ctrl + U` | Descomentar selección |
| `Ctrl + .` | Quick Actions (corregir errores) |
| `F5` | Ejecutar con debugging |
| `Ctrl + F5` | Ejecutar sin debugging |
| `Tab` | Autocompletar (IntelliSense) |
| `Ctrl + Space` | Forzar IntelliSense |
| `F12` | Ir a definición |
| `Ctrl + R, Ctrl + R` | Renombrar refactoring |

---

## 🔄 Ciclo de Vida de un Programa C#

### De código a ejecución

```
┌──────────────────────────────────────────────────────────────┐
│                  CICLO DE EJECUCIÓN C#                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1. ESCRITURA                                                │
│     ┌─────────────┐                                          │
│     │ Código C#   │  ← Tu programa (.cs)                     │
│     └──────┬──────┘                                          │
│            │                                                 │
│            ▼                                                 │
│  2. COMPILACIÓN (csc.exe)                                    │
│     ┌─────────────┐                                          │
│     │ Compilador  │  → Verifica sintaxis y tipos             │
│     │  C#         │  → Genera código IL                       │
│     └──────┬──────┘                                          │
│            │                                                 │
│            ▼                                                 │
│  3. CÓDIGO IL (Intermediate Language)                         │
│     ┌─────────────┐                                          │
│     │  .exe/.dll  │  → Bytecode multiplataforma              │
│     │     IL      │  → Independiente del SO                  │
│     └──────┬──────┘                                          │
│            │                                                 │
│            ▼                                                 │
│  4. EJECUCIÓN (CLR)                                          │
│     ┌─────────────────────────────────────┐                  │
│     │     JIT (Just-In-Time)             │                  │
│     │  Compila IL → Código máquina       │                  │
│     └──────────────┬──────────────────────┘                  │
│                    │                                         │
│                    ▼                                         │
│     ┌─────────────────────────────────────┐                  │
│     │    Código NATIVO ejecutándose      │                  │
│     │    (Windows/Linux/macOS)           │                  │
│     └─────────────────────────────────────┘                  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📝 Conceptos Clave de C#

### Value Types vs Reference Types

```csharp
// VALUE TYPE (almacenado en STACK)
int edad = 25;
// Copia el valor
int edad2 = edad;  // edad2 = 25 (copia independiente)
edad2 = 30;        // edad sigue siendo 25

// REFERENCE TYPE (almacenado en HEAP)
string nombre = "Juan";
// Copia la referencia (misma dirección de memoria)
string nombre2 = nombre;  // Ambos apuntan al mismo objeto
nombre2 = "Maria";        // nombre sigue siendo "Juan"
```

---

### Nullable Types

```csharp
// Tipos que pueden ser null
int? numero = null;           // int? es equivalente a Nullable<int>
double? precio = null;        // Puede ser null o un double
bool? activo = null;          // Puede ser null, true o false

// Operador null-coalescing (??)
int edad = numero ?? 18;      // Si numero es null, usa 18

// Verificar si tiene valor
if (numero.HasValue)
{
    Console.WriteLine(numero.Value);
}
```

---

### Strings en C#

```csharp
// Concatenación
string nombre = "Juan";
string saludo = "Hola, " + nombre;  // "Hola, Juan"

// Interpolación de cadenas (C# 6+)
string saludo2 = $"Hola, {nombre}";  // "Hola, Juan"

// Strings verbatim (mantienen formato)
string ruta = @"C:\Users\Nombre\Archivos";

// Strings multilínea (C# 11+)
string texto = """
    Esta es una línea
    Esta es otra línea
    """;

// Métodos útiles
string texto = "  Hola Mundo  ";
texto = texto.Trim();           // "Hola Mundo"
texto = texto.ToUpper();        // "HOLA MUNDO"
bool contiene = texto.Contains("Mundo");  // true
string[] partes = texto.Split(' ');      // ["Hola", "Mundo"]
```

---

## 🎯 Características Avanzadas de C# 12

### 1. Primary Constructors

Simplifica la declaración de constructores en clases y structs:

```csharp
// Antes (C# 11)
public class Persona
{
    private string _nombre;
    private int _edad;
    
    public Persona(string nombre, int edad)
    {
        _nombre = nombre;
        _edad = edad;
    }
}

// Ahora (C# 12) - Más conciso
public class Persona(string nombre, int edad)
{
    public void Saludar() => 
        Console.WriteLine($"Hola, soy {nombre} y tengo {edad} años");
}
```

---

### 2. Collection Expressions

Nueva sintaxis unificada para crear colecciones:

```csharp
// Arrays
int[] numeros = [1, 2, 3, 4, 5];

// Listas
List<string> nombres = ["Ana", "Juan", "María"];

// Diccionarios
Dictionary<string, int> edades = new()
{
    ["Ana"] = 25,
    ["Juan"] = 30
};

// Span (para alto rendimiento)
Span<int> span = [1, 2, 3];
```

---

### 3. Pattern Matching Avanzado

Lógica condicional más expresiva y legible:

```csharp
// Switch expression con rangos
string categoria = edad switch
{
    < 13 => "Niño",
    >= 13 and < 20 => "Adolescente",
    >= 20 and < 65 => "Adulto",
    >= 65 => "Adulto mayor"
};

// Pattern matching con tipos
string descripcion = obj switch
{
    int i when i > 0 => $"Entero positivo: {i}",
    string s => $"Texto de {s.Length} caracteres",
    null => "Valor nulo",
    _ => "Tipo desconocido"
};
```

---

### 4. Strings Multilínea y Null-Coalescing

```csharp
// String interpolation con formato
string reporte = $"""
    === REPORTE DE USUARIO ===
    Nombre: {nombre.ToUpper()}
    Edad: {edad} años
    Fecha: {DateTime.Now:yyyy-MM-dd HH:mm}
    ==========================
    """;

// Null-coalescing assignment
string nombre ??= "Anónimo";  // Asigna solo si es null

// Null-conditional operator
int? longitud = texto?.Length;  // null si texto es null
```

---

## 📊 C# vs Otros Lenguajes: Comparativa

### Benchmark de Rendimiento

| Operación | C# | Java | Python | JavaScript |
|-----------|-----|------|--------|------------|
| **Hello World** | 30ms | 35ms | 50ms | 40ms |
| **Loop 1M iteraciones** | 15ms | 18ms | 980ms | 25ms |
| **Ordenar 100K items** | 180ms | 200ms | 450ms | 300ms |
| **Manejo JSON** | 90ms | 100ms | 150ms | 80ms |
| **Consumo memoria** | 25MB | 40MB | 15MB | 30MB |

---

### Análisis de Resultados

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

**🏆 Fortalezas de C#**

- **Rendimiento cercano a C++:** Gracias al compilador JIT que optimiza en runtime
- **Menor consumo de memoria vs Java:** CLR más eficiente en gestión de objetos
- **Velocidad de desarrollo:** Equilibrio entre performance y productividad
- **Tipado estático:** Detección de errores en compilación, no en ejecución

**📈 Casos donde C# brilla:**
- Aplicaciones empresariales de alto tráfico
- Procesamiento de datos en tiempo real
- APIs de alto rendimiento
- Microservicios en contenedores

</div>

<div style="flex: 1;">

**🎯 Cuándo elegir cada lenguaje:**

```
C#          → Aplicaciones empresariales Windows/Cloud
Java        → Sistemas legacy, Android nativo
Python      → Data Science, IA, scripts rápidos
JavaScript  → Frontend web, Node.js full-stack
Go          → Microservicios de alta concurrencia
Rust        → Sistemas de bajo nivel, seguridad crítica
```

**💼 Mercado laboral Colombia (2025):**
- C#/.NET: ⭐⭐⭐⭐⭐ Alta demanda en empresas medianas/grandes
- Java: ⭐⭐⭐⭐⭐ Máxima demanda (sistemas legacy)
- Python: ⭐⭐⭐⭐⭐ En crecimiento (Data/AI)
- JavaScript: ⭐⭐⭐⭐⭐ Universal para web

</div>

</div>

---

### Conclusión

> **C# ofrece el mejor balance entre rendimiento, productividad y ecosistema empresarial. Ideal para desarrolladores que buscan un lenguaje moderno con amplia demanda laboral.**

---

## 🏗️ Arquitectura .NET Core/8

### Cómo Funciona Internamente

```
┌──────────────────────────────────────────────────────────┐
│                   TU APLICACIÓN C#                       │
│              (código de alto nivel)                      │
└────────────────────┬─────────────────────────────────────┘
                     │ Compilación
                     ▼
┌──────────────────────────────────────────────────────────┐
│            INTERMEDIATE LANGUAGE (IL)                    │
│              (bytecode independiente)                    │
└────────────────────┬─────────────────────────────────────┘
                     │ JIT Compilation
                     ▼
┌──────────────────────────────────────────────────────────┐
│     COMMON LANGUAGE RUNTIME (CLR)                        │
│  ┌────────────┬──────────────┬─────────────────────┐    │
│  │ Garbage    │   Security   │  Exception          │    │
│  │ Collector  │   Manager    │  Handler            │    │
│  └────────────┴──────────────┴─────────────────────┘    │
└────────────────────┬─────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────┐
│          SISTEMA OPERATIVO (Windows/Linux/macOS)         │
└──────────────────────────────────────────────────────────┘
```

### Ventajas del CLR
- ✅ **Garbage Collection automático**
- ✅ **Seguridad de tipos en runtime**
- ✅ **Manejo de excepciones estructurado**
- ✅ **Interoperabilidad entre lenguajes**

---

## 💼 Casos de Uso Reales de .NET

### Empresas que Usan .NET

```
MICROSOFT           → Azure, Visual Studio, Office 365
STACK OVERFLOW      → Sitio web completo
UNITY               → Motor de juegos (millones de juegos)
SIEMENS             → Sistemas industriales
DELL                → Herramientas internas
ALASKA AIRLINES     → Sistema de reservas
```

### Proyectos Open Source Famosos

| Proyecto | Descripción | GitHub Stars |
|----------|-------------|--------------|
| **ASP.NET Core** | Framework web | 35K+ ⭐ |
| **Roslyn** | Compilador C# | 19K+ ⭐ |
| **ML.NET** | Machine Learning | 9K+ ⭐ |
| **Orleans** | Actor model framework | 10K+ ⭐ |
| **Blazor** | WebAssembly con C# | (Parte de ASP.NET) |

---

## 🛠️ Herramientas del Ecosistema .NET

### Más Allá de Visual Studio

**IDEs Alternativos:**
- 🟦 **Visual Studio Code** + C# Extension (Ligero, multiplataforma)
- 🟦 **JetBrains Rider** (Potente, comercial)
- 🟦 **Visual Studio for Mac** (Nativo macOS)

**CLI (dotnet command):**
```bash
# Crear proyecto
dotnet new console -n MiApp

# Restaurar dependencias
dotnet restore

# Compilar
dotnet build

# Ejecutar
dotnet run

# Publicar para producción
dotnet publish -c Release

# Agregar paquete NuGet
dotnet add package Newtonsoft.Json
```

**Herramientas de Testing:**
- xUnit, NUnit, MSTest (frameworks de pruebas)
- Moq (mocking)
- BenchmarkDotNet (benchmarks)

---

## 📦 NuGet: Gestor de Paquetes

### El "npm" de .NET

```xml
<!-- Archivo .csproj -->
<ItemGroup>
  <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
  <PackageReference Include="Dapper" Version="2.1.28" />
  <PackageReference Include="Serilog" Version="3.1.1" />
</ItemGroup>
```

**Repositorio oficial:** https://www.nuget.org/

**Paquetes populares:**
- **Newtonsoft.Json** - Manejo JSON (2.5B descargas)
- **AutoMapper** - Mapeo de objetos
- **Dapper** - Micro ORM rápido
- **Serilog** - Logging estructurado
- **FluentValidation** - Validaciones fluidas

---

## 🎓 Ejercicio Avanzado: Debugging

### Práctica con Breakpoints

**Código con bug intencional:**
```csharp
using System;

class Program
{
    static void Main()
    {
        int[] numeros = { 10, 20, 30, 40, 50 };
        int suma = 0;
        
        for (int i = 0; i <= numeros.Length; i++)  // 🐛 Bug aquí
        {
            suma += numeros[i];
        }
        
        Console.WriteLine($"Suma: {suma}");
    }
}
```

**Instrucciones:**
1. Copiar código a Visual Studio
2. Poner breakpoint en línea del `for`
3. Presionar F5 (Debug)
4. Usar F10 (Step Over) para ver el error
5. Identificar y corregir el bug
6. ¿Qué excepción lanza? ¿En qué línea?

**Respuesta:** `IndexOutOfRangeException` - `i <= numeros.Length` debe ser `i < numeros.Length`

---

## 🔥 Mejores Prácticas desde el Día 1

### Code Style y Convenciones

```csharp
// ✅ CORRECTO
public class StudentManager        // PascalCase para clases
{
    private int _studentCount;     // camelCase con _ para campos privados
    
    public string Name { get; set; }  // PascalCase para propiedades
    
    public void AddStudent()       // PascalCase para métodos
    {
        int localVar = 10;         // camelCase para variables locales
    }
}

// ❌ INCORRECTO
public class student_manager      // Minúsculas y guiones bajos
{
    private int StudentCount;     // Sin _
    
    public string name { get; set; }  // Minúsculas
    
    public void add_student()     // Estilo Python
    {
        int LocalVar = 10;        // Mayúscula inicial
    }
}
```

### Reglas de Oro
1. ✅ Usar nombres descriptivos
2. ✅ Evitar abreviaturas confusas
3. ✅ Comentar solo lo necesario
4. ✅ Máximo 100-120 caracteres por línea
5. ✅ Un archivo por clase (usualmente)

---

## Resumen de la Clase

| Concepto | Descripción |
| ---------- | ------------- |
| **C#** | Lenguaje moderno, orientado a objetos, type-safe |
| **.NET 8** | Plataforma unificada, multiplataforma, open source |
| **CLR** | Common Language Runtime, máquina virtual de .NET |
| **Visual Studio** | IDE oficial para desarrollo .NET |
| **Namespace** | Organización jerárquica del código |
| **Main()** | Punto de entrada de la aplicación |

---

## Tarea para la Próxima Clase

### Preparación (individual)

1. **Instalar** Visual Studio 2022 Community
   - Workloads: ASP.NET y desarrollo web
   - Componente: .NET 8 SDK

2. **Crear** una aplicación de consola que:
   - Pida el nombre de un estudiante
   - Pida 3 notas
   - Calcule el promedio
   - Muestre el resultado con 2 decimales
   - Indique si aprobó o reprobó

3. **Subir** el código a un repositorio Git (GitHub/GitLab)

---

## Recursos de Aprendizaje

### Documentación oficial

- **Microsoft Learn:** https://learn.microsoft.com/es-es/dotnet/csharp/
- **Documentación C#:** https://docs.microsoft.com/es-es/dotnet/csharp/
- **Descargas .NET:** https://dotnet.microsoft.com/download

### Libros recomendados (PDF oficial)

1. "Programación Orientada a Objetos en C#" - Pérez Chaves, Roger
2. "C# and the .NET Platform" - Troelsen, Andrew
3. "Así es Microsoft Visual Studio .NET" - Microsoft Corporation

---

## Próxima Clase

### Clase 2: Clases, Objetos y Encapsulamiento

- Programación Orientada a Objetos en C#
- Creación de clases y objetos
- Atributos y métodos
- Encapsulamiento: propiedades y modificadores de acceso
- Constructores

**¡Traigan Visual Studio instalado!**

---

# ¡Gracias!
## ¿Preguntas?

**Contacto:** [Tu correo institucional]
**Repositorio:** [Enlace al repo del curso]

**UNAULA - Ingeniería Informática - 2026-I**
