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

<div style="display: flex; gap: 30px; align-items: center;">

<div style="flex: 1;">

![Ecosistema .NET](../../assets/infografias/clase-01-ecosistema-dotnet.png){: style="max-width: 100%; max-height: 350px;"}

</div>

<div style="flex: 1;">

**🎯 Puntos Clave del Ecosistema:**

**✅ Unificación de Plataformas**
- .NET 8 unifica Framework, Core y Xamarin
- Un solo runtime para todas las aplicaciones
- Comparte código entre web, móvil, desktop

**✅ Multiplataforma Real**
- Windows, Linux, macOS nativo
- iOS y Android via MAUI
- Contenedores Docker optimizados

**✅ Modelo de Ejecución**
- Compilación JIT para rendimiento
- IL (Intermediate Language) portable
- AOT (Ahead-of-Time) opcional

**📊 Casos de Uso por Área:**
- **Web:** ASP.NET Core → APIs de alto rendimiento
- **Desktop:** WPF/WinForms → Apps empresariales
- **Cloud:** Azure SDK → Serverless y microservicios
- **Gaming:** Unity → 2.5M+ juegos desarrollados

</div>

</div>

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

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**🎯 Objetivo del Ejercicio:**

Crear una aplicación de consola que calcule el área de un rectángulo aplicando conceptos básicos de C#.

**Conceptos que practicarás:**
- ✅ Entrada/Salida con `Console`
- ✅ Declaración de variables
- ✅ Tipos de datos (`double`)
- ✅ Parseo de strings a números
- ✅ Interpolación de strings (`$`)
- ✅ Estructura de un programa C#

**Reto adicional:**
- Agregar validación para evitar números negativos
- Permitir calcular áreas de otras figuras (círculo, triángulo)
- Usar métodos para organizar el código

</div>

<div style="flex: 1;">

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

**📝 Análisis del código:**
- `Console.Write()` - Sin salto de línea
- `Console.ReadLine()` - Lee como string
- `double.Parse()` - Convierte string a double
- `$"{area:F2}"` - Formatea con 2 decimales

</div>

</div>

---

## Ejercicios Prácticos Adicionales

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**🧮 Ejercicio 1: Calculadora Simple**

**Objetivo:** Implementar operaciones aritméticas básicas con manejo de errores.

```csharp
// Estructura principal:
Console.Write("Número 1: ");
double num1 = double.Parse(Console.ReadLine());

Console.Write("Operación (+ - * /): ");
char op = Console.ReadLine()[0];

Console.Write("Número 2: ");
double num2 = double.Parse(Console.ReadLine());

double resultado = op switch
{
    '+' => num1 + num2,
    '-' => num1 - num2,
    '*' => num1 * num2,
    '/' => num2 != 0 ? num1 / num2 :
           throw new Exception("División por cero"),
    _ => throw new Exception("Operación inválida")
};

Console.WriteLine($"Resultado: {resultado:F2}");
```

**Conceptos aplicados:**
- Switch expressions (C# 8+)
- Manejo de excepciones
- Operadores aritméticos
- Validación de entrada

</div>

<div style="flex: 1;">

**🌡️ Ejercicio 2: Conversor de Temperatura**

**Objetivo:** Convertir Celsius a Fahrenheit y Kelvin con lógica condicional.

```csharp
Console.Write("Temperatura en Celsius: ");
double celsius = double.Parse(Console.ReadLine());

// Fórmulas de conversión
double fahrenheit = (celsius * 9 / 5) + 32;
double kelvin = celsius + 273.15;

Console.WriteLine($"{celsius}°C = {fahrenheit:F2}°F");
Console.WriteLine($"{celsius}°C = {kelvin:F2}K");

// Estado del agua
string estado = celsius <= 0 ? "SÓLIDO ❄️" :
                celsius >= 100 ? "GASEOSO 💨" : "LÍQUIDO 💧";

Console.WriteLine($"→ Estado del agua: {estado}");
```

**Conceptos aplicados:**
- Operador ternario `? :`
- Expresiones matemáticas
- Formato de salida (`:F2`)
- Lógica condicional encadenada

**Reto:** Agregar conversión a Rankine y Réaumur

</div>

</div>

---

## Ejercicio Propuesto: Sistema de Calificaciones

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**🎯 Desafío de Programación:**

Crear un **Sistema de Calificaciones** que calcule promedios de estudiantes.

**Requisitos funcionales:**
1. Solicitar nombre del estudiante
2. Ingresar 3 notas (0.0 - 5.0)
3. Calcular promedio automáticamente
4. Determinar estado: APROBADO (≥3.0) o REPROBADO
5. Validar entrada de datos con manejo de errores
6. Mostrar resultados formateados

**🚀 Niveles de dificultad:**

| Nivel | Requisito |
|-------|-----------|
| **Básico** | Calcular promedio de 3 notas |
| **Intermedio** | Agregar validación de notas (0-5) |
| **Avanzado** | Crear método `PedirNota()` reutilizable |

</div>

<div style="flex: 1;">

**📊 Salida esperada:**

```
================================
  SISTEMA DE CALIFICACIONES
================================
Estudiante: María López

Notas ingresadas:
  Nota 1: 4.5
  Nota 2: 3.8
  Nota 3: 4.2
--------------------------------
Promedio: 4.17
Estado: ✅ APROBADO
================================
```

**💡 Pistas para la solución:**

```csharp
// Pedir nombre
Console.Write("Nombre: ");
string nombre = Console.ReadLine();

// Pedir notas
Console.Write("Nota 1: ");
double n1 = double.Parse(Console.ReadLine());
// ... repetir para n2, n3

// Calcular
double promedio = (n1 + n2 + n3) / 3;

// Determinar estado
string estado = promedio >= 3.0 ?
    "APROBADO ✅" : "REPROBADO ❌";
```

**🔑 Conceptos clave:**
- Console.Write vs WriteLine
- double.Parse para conversión
- Operadores aritméticos
- Operador ternario para estado

</div>

</div>

---

## Ejercicio con Manejo de Errores

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**✅ Validación Robusta de Entrada:**

Aprender a validar datos de entrada es **crítico** para aplicaciones reales.

**Problemas que resuelve la validación:**
- ❌ Usuario ingresa letras en lugar de números
- ❌ Usuario ingresa notas fuera de rango (negativas, >5)
- ❌ El programa se cierra inesperadamente

**🔑 Conceptos clave:**

| Método | Propósito |
|--------|-----------|
| `TryParse()` | Convierte sin lanzar excepción |
| `while(true)` | Repite hasta entrada válida |
| `return nota` | Sale del método con el valor |
| `out nota` | Parámetro de salida |

</div>

<div style="flex: 1;">

```csharp
// Método reutilizable de validación
static double PedirNota(string etiqueta)
{
    double nota;
    while (true)
    {
        Console.Write($"{etiqueta} (0.0 - 5.0): ");

        // TryParse devuelve bool, no lanza excepción
        if (double.TryParse(Console.ReadLine(),
            out nota))
        {
            if (nota >= 0.0 && nota <= 5.0)
                return nota; // ✅ Válido, retornar

            Console.WriteLine("  ⚠️ Fuera de rango");
        }
        else
        {
            Console.WriteLine("  ⚠️ No es un número");
        }
    }
}

// Uso en Main:
double n1 = PedirNota("Nota 1");
double n2 = PedirNota("Nota 2");
double n3 = PedirNota("Nota 3");

double promedio = (n1 + n2 + n3) / 3.0;
```

**💡 Ventajas:**
- Código limpio y reutilizable
- Maneja errores sin crashes
- Retroalimentación inmediata al usuario
- Evita datos inválidos en el sistema

</div>

</div>

---

## Atajos de Visual Studio Útiles

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**⌨️ Atajos Esenciales:**

| Atajo | Acción |
|-------|--------|
| `Ctrl + .` | Quick Actions / Corregir errores |
| `F5` | Ejecutar con debugging |
| `Ctrl + F5` | Ejecutar sin debugging |
| `Shift + F5` | Detener debugging |
| `F9` | Toggle breakpoint |
| `F10` | Step Over (siguiente línea) |
| `F11` | Step Into (entrar en función) |
| `Shift + F11` | Step Out (salir de función) |

</div>

<div style="flex: 1;">

**🛠️ Edición y Navegación:**

| Atajo | Acción |
|-------|--------|
| `Ctrl + K, C` | Comentar selección |
| `Ctrl + K, U` | Descomentar selección |
| `Ctrl + Space` | Forzar IntelliSense |
| `Tab` | Aceptar sugerencia IntelliSense |
| `F12` | Ir a definición |
| `Shift + F12` | Find All References |
| `Ctrl + R, R` | Renombrar (refactor) |
| `Ctrl + -` | Navegar hacia atrás |
| `Ctrl + Shift + -` | Navegar hacia adelante |

**💡 Tip:** Presiona `Ctrl + E, Ctrl + I` para búsqueda incremental

</div>

</div>

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

## 📊 C# vs Otros Lenguajes

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**Benchmark de Rendimiento:**

| Operación | C# | Java | Python | JS |
|-----------|-----|------|--------|-----|
| Hello World | 30ms | 35ms | 50ms | 40ms |
| Loop 1M | 15ms | 18ms | 980ms | 25ms |
| Sort 100K | 180ms | 200ms | 450ms | 300ms |
| JSON | 90ms | 100ms | 150ms | 80ms |
| Memoria | 25MB | 40MB | 15MB | 30MB |

**🏆 Fortalezas de C#:**
- Rendimiento cercano a C++ (JIT)
- Menor memoria que Java
- Tipado estático (errores en compilación)
- Excelente para: APIs empresariales, microservicios, procesamiento en tiempo real

</div>

<div style="flex: 1;">

**🎯 Cuándo elegir cada lenguaje:**

```
┌────────────────────────────────────┐
│ C#       → Empresas, Windows, Cloud │
│ Java     → Legacy, Android          │
│ Python   → Data Science, IA         │
│ JS       → Frontend web, Node.js    │
│ Go       → Microservicios           │
│ Rust     → Bajo nivel, crítico      │
└────────────────────────────────────┘
```

**💼 Mercado Colombia 2026:**
- C#/.NET: ⭐⭐⭐⭐⭐ Alta demanda
- Java: ⭐⭐⭐⭐⭐ Máxima (legacy)
- Python: ⭐⭐⭐⭐⭐ Creciente (Data/AI)
- JavaScript: ⭐⭐⭐⭐⭐ Universal

**📈 Tendencia:** C# creciendo en cloud y microservicios

</div>

</div>

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

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**🏢 Empresas que Usan .NET:**

```
Microsoft    → Azure, VS, Office 365
Stack Overflow→ Sitio web completo
Unity        → Motor de juegos #1
Siemens      → Sistemas industriales
Dell         → Herramientas internas
Alaska Airlines→ Sistema reservas
```

**📊 Impacto en el mercado:**
- Más de 7 millones de desarrolladores .NET
- 90% de PCs Windows ejecutan .NET Framework
- Azure procesa 1B+ transacciones/día con .NET

</div>

<div style="flex: 1;">

**🌟 Proyectos Open Source:**

| Proyecto | Descripción | Stars |
|----------|-------------|-------|
| ASP.NET Core | Framework web | 35K+ |
| Roslyn | Compilador C# | 19K+ |
| ML.NET | Machine Learning | 9K+ |
| Orleans | Actor model | 10K+ |
| Blazor | WebAssembly C# | + |

**🎮 Gaming con C#:**
- Unity: 2.5M+ juegos creados
- 50% de juegos móviles usan Unity
- C# es el lenguaje principal de Unity

**💡 Conclusión:**
C# tiene un ecosistema maduro con amplias oportunidades laborales.

</div>

</div>

---

## 🛠️ Herramientas del Ecosistema .NET

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**💻 IDEs Disponibles:**
- **Visual Studio 2022** - IDE completo (Windows)
- **VS Code + C# Dev Kit** - Ligero, cross-platform
- **JetBrains Rider** - Potente, comercial
- **Visual Studio for Mac** - Nativo macOS

**⚙️ CLI dotnet (Comandos clave):**

```bash
dotnet new console -n App    # Crear
dotnet build                 # Compilar
dotnet run                   # Ejecutar
dotnet test                  # Probar
dotnet publish -c Release    # Producción
```

**📦 Gestión de paquetes:**
```bash
dotnet add package Newtonsoft.Json
dotnet restore                # Restaurar deps
```

</div>

<div style="flex: 1;">

**🧪 Frameworks de Testing:**
- **xUnit** - Popular, open source
- **NUnit** - Ampliamente usado
- **MSTest** - Oficial Microsoft
- **Moq** - Mocking framework
- **BenchmarkDotNet** - Benchmarks

**🔧 Extensiones útiles:**
- **C# Dev Kit** - VS Code completo
- **.NET Core Test Explorer** - Tests en VS Code
- **NuGet Package Manager** - Gestión paquetes

**💡 ¿Por qué aprender la CLI?**
- Automatización de builds
- CI/CD pipelines
- Contenedores Docker
- Servidores sin GUI (Linux)

</div>

</div>

---

## 📦 NuGet: Gestor de Paquetes de .NET

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**📚 ¿Qué es NuGet?**

Es el gestor de paquetes oficial de .NET (similar a npm de Node.js o pip de Python).

**Uso desde CLI:**
```bash
# Buscar paquete
dotnet add package Newtonsoft.Json

# Versión específica
dotnet add package Dapper --version 2.1.28

# Listar paquetes
dotnet list package
```

**Uso en Visual Studio:**
- Click derecho → Manage NuGet Packages
- Buscar → Install

</div>

<div style="flex: 1;">

**🔥 Paquetes Populares (Billones de descargas):**

| Paquete | Uso | Descargas |
|---------|-----|-----------|
| **Newtonsoft.Json** | JSON | 2.5B+ |
| **Dapper** | Micro ORM | 500M+ |
| **Serilog** | Logging | 300M+ |
| **AutoMapper** | Mapeo objetos | 250M+ |
| **FluentValidation** | Validaciones | 100M+ |
| **xUnit** | Testing | 150M+ |

**💡 Ventajas:**
- Reutilización de código
- Actualizaciones automáticas
- Gestión de dependencias
- 400K+ paquetes disponibles

**🔗 https://www.nuget.org/**

</div>

</div>

---

## 🎓 Ejercicio Avanzado: Debugging en Visual Studio

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**🐛 Encuentra el Bug:**

```csharp
int[] numeros = { 10, 20, 30, 40, 50 };
int suma = 0;

// 🐛 Bug en esta línea
for (int i = 0; i <= numeros.Length; i++)
{
    suma += numeros[i];
}

Console.WriteLine($"Suma: {suma}");
```

**🔍 Ejercicio de debugging:**
1. Breakpoint en línea del `for` (F9)
2. F5 para iniciar debug
3. F10 para Step Over (línea por línea)
4. Observa valor de `i` e intenta acceder a `numeros[5]`

**❓ ¿Qué sucede?**
- Excepción: `IndexOutOfRangeException`
- El array tiene índices 0-4 (5 elementos)
- `i <= Length` intenta acceder al índice 5

**✅ Solución:**
```csharp
// Corregir la condición
for (int i = 0; i < numeros.Length; i++)
```

</div>

<div style="flex: 1;">

**🎯 Comandos de Debugging:**

| Tecla | Acción |
|-------|--------|
| `F5` | Iniciar debug |
| `F9` | Toggle breakpoint |
| `F10` | Step Over (siguiente) |
| `F11` | Step Into (entrar func) |
| `Shift+F11` | Step Out (salir func) |
| `Shift+F5` | Detener debug |

**💡 Tips de Debugging:**
- **Watch Window:** Inspeccionar variables
- **Immediate Window:** Ejecutar código en tiempo de ejecución
- **Call Stack:** Ver ruta de ejecución
- **Locals:** Variables locales del scope actual

**🚀 ¿Por qué aprender debugging?**
- Ahorra 50%+ del tiempo de desarrollo
- Permite entender el flujo del código
- Esencial para encontrar bugs complejos
- Habilidad obligatoria para cualquier desarrollador

</div>

</div>

---

## 🔥 Mejores Prácticas desde el Día 1

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**✅ Convenciones de Nomenclatura C#:**

| Elemento | Estilo | Ejemplo |
|----------|--------|---------|
| Clases | PascalCase | `StudentManager` |
| Métodos | PascalCase | `GetStudent()` |
| Propiedades | PascalCase | `Name { get; }` |
| Campos privados | _camelCase | `_studentCount` |
| Variables locales | camelCase | `studentName` |
| Constantes | PascalCase | `MaxCount` |

**Ejemplo correcto:**
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

</div>

<div style="flex: 1;">

**📜 Reglas de Oro:**

1. **Nombres descriptivos:** `GetStudentById()`, no `Get()`
2. **Sin abreviaturas confusas:** `Student`, no `Stu`
3. **Comentarios mínimos:** El código debe explicarse solo
4. **Líneas ≤ 100 caracteres:** Mayor legibilidad
5. **Un archivo por clase:** Organización limpia

**🎨 Formato con EditorConfig:**
```ini
# .editorconfig
indent_style = space
indent_size = 4
end_of_line = crlf
charset = utf-8
trim_trailing_whitespace = true
```

**🚀 Herramientas útiles:**
- **StyleCop Analyzer** - Reglas de estilo
- **Resharper** - Refactoring automático
- **Formatter** - Formato automático (Ctrl+K, D)

**💡 Beneficio:** Código consistente = Código mantenible

</div>

</div>

---

## Resumen de la Clase

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**📚 Conceptos Aprendidos:**

| Concepto | Descripción |
|----------|-------------|
| **C#** | Lenguaje moderno, POO, type-safe |
| **.NET 8** | Plataforma unificada, open source |
| **CLR** | Máquina virtual (JIT, GC, seguridad) |
| **Visual Studio** | IDE oficial para desarrollo |
| **Namespace** | Organización jerárquica |
| **Main()** | Punto de entrada |

</div>

<div style="flex: 1;">

**🎯 Habilidades Desarrolladas:**

```
✅ Instalar y configurar VS 2022
✅ Crear aplicación de consola
✅ Escribir código C# básico
✅ Usar variables y tipos de datos
✅ Implementar entrada/salida
✅ Depurar código (breakpoints)
✅ Aplicar convenciones de código
```

**🚀 Próximos pasos:**
- Clase 2: Clases y Objetos
- Practicar ejercicios propuestos
- Completar tarea de promedios

**💡 Recurso:** Microsoft Learn C#

</div>

</div>

---

## Tarea para la Próxima Clase

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**🖥️ 1. Instalación de Visual Studio 2022**

- Descargar desde: visualstudio.microsoft.com
- Edición: Community (gratis)
- Workloads necesarios:
  - ☑️ ASP.NET y desarrollo web
  - ☑️ Almacenamiento y procesamiento de datos
- Componentes:
  - ☑️ .NET 8 SDK
  - ☑️ Git para Windows

</div>

<div style="flex: 1;">

**💻 2. Proyecto: Calculadora de Promedios**

Crear una app de consola que:

```csharp
// Requisitos funcionales:
1. Solicitar nombre del estudiante
2. Ingresar 3 notas (0.0 - 5.0)
3. Calcular promedio
4. Mostrar con 2 decimales
5. Indicar: APROBADO (≥3.0) o REPROBADO
6. Validar entrada de datos
```

**Salida esperada:**
```
===============================
  SISTEMA DE CALIFICACIONES
===============================
Estudiante: María López
Nota 1: 4.5
Nota 2: 3.8
Nota 3: 4.2
-------------------------------
Promedio: 4.17
Estado: ✅ APROBADO
===============================
```

**📦 3. Entrega:**
- Subir a GitHub/GitLab
- Compartir enlace del repositorio

</div>

</div>

---

## Recursos y Próxima Clase

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**📚 Recursos de Aprendizaje**

**Documentación oficial:**
- [Microsoft Learn C#](https://learn.microsoft.com/es-es/dotnet/csharp/)
- [.NET Downloads](https://dotnet.microsoft.com/download)

**Libros recomendados (según PDF oficial):**
1. "Programación Orientada a Objetos en C#" - Pérez Chaves, Roger
2. "C# and the .NET Platform" - Troelsen, Andrew
3. "Así es Microsoft Visual Studio .NET" - Microsoft Corporation

**Comunidad:**
- Stack Overflow: tag `c#`
- Reddit: r/csharp
- Discord: C# Discord Server

</div>

<div style="flex: 1;">

**🎓 Próxima Clase: Clases, Objetos y Encapsulamiento**

**Temas a tratar:**
- Programación Orientada a Objetos en C#
- Creación de clases y objetos
- Atributos y métodos
- Encapsulamiento: propiedades y modificadores
- Constructores y destructores

**📝 Requisitos:**
- ✅ Visual Studio 2022 instalado
- ✅ Tarea completada (Calculadora de promedios)
- ✅ Repositorio Git creado

**🔗 Preparación:**
Revisa los conceptos básicos de POO: clases, objetos, atributos y métodos.

</div>

</div>

---

# ¡Gracias!
## ¿Preguntas?

**Contacto:** [Tu correo institucional]
**Repositorio:** [Enlace al repo del curso]

**UNAULA - Ingeniería Informática - 2026-I**
