# Clase 01 - Referencias y Recursos
## Introducción a C# y .NET

**IF0100 - Lenguaje de Programación OO II** | Unidad 1

---

## Tabla de Contenidos

- [Instalación y Configuración](#instalación-y-configuración)
- [Documentación Oficial](#documentación-oficial)
- [Cursos Gratuitos](#cursos-gratuitos)
- [Videos Recomendados](#videos-recomendados)
- [Libros Recomendados](#libros-recomendados)
- [Herramientas y Extensiones](#herramientas-y-extensiones)
- [Comunidad y Soporte](#comunidad-y-soporte)
- [Ejercicios Adicionales](#ejercicios-adicionales)

---

## Instalación y Configuración

### Visual Studio 2022 Community

**Descarga oficial:** https://visualstudio.microsoft.com/downloads/

#### Workloads Necesarios

Durante la instalación, selecciona:

```
☑️ ASP.NET y desarrollo web
   ├─ ASP.NET Core
   └─ Herramientas de desarrollo de Azure

☑️ Almacenamiento de datos
   ├─ SQL Server Data Tools
   └─ Conectividad de datos

☑️ Herramientas de .NET 8
```

#### Verificar Instalación

1. Abre **Developer Command Prompt for VS 2022**
2. Ejecuta: `dotnet --version`
3. Debería mostrar: `8.0.xxx` o superior

### .NET 8 SDK (Standalone)

Si prefieres no instalar Visual Studio completo:

**Descarga:** https://dotnet.microsoft.com/download/dotnet/8.0

| OS | Link |
|----|-----|
| **Windows** | [x64](https://dotnet.microsoft.com/download/dotnet/8.0) / [x86](https://dotnet.microsoft.com/download/dotnet/8.0) |
| **macOS** | [Intel](https://dotnet.microsoft.com/download/dotnet/8.0) / [Apple Silicon](https://dotnet.microsoft.com/download/dotnet/8.0) |
| **Linux** | [Paquetes](https://learn.microsoft.com/en-us/dotnet/core/install/linux) |

### Git para Windows

**Descarga:** https://git-scm.com/download/win

Configuración recomendada:
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
git config --global core.autocrlf true  # Importante en Windows
```

---

## Documentación Oficial

### C# Language Reference

| Tema | Link |
|------|------|
| **Guía de C#** | https://learn.microsoft.com/es-es/dotnet/csharp/ |
| **Palabras clave de C#** | https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/keywords/ |
| **Operadores de C#** | https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/operators/ |
| **Tipos de valor** | https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/value-types |
| **Tipos de referencia** | https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/reference-types |
| **Nullable** | https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/nullable-value-types |
| **Strings** | https://learn.microsoft.com/es-es/dotnet/csharp/how-to/concatenate-multiple-strings |
| **Pattern Matching** | https://learn.microsoft.com/es-es/dotnet/csharp/fundamentals/functional/pattern-matching |

### .NET Documentation

| Tema | Link |
|------|------|
| **Guía de .NET** | https://learn.microsoft.com/es-es/dotnet/ |
| **.NET 8 - Novedades** | https://learn.microsoft.com/es-es/dotnet/core/whats-new/dotnet-8 |
| **BCL (Base Class Library)** | https://learn.microsoft.com/es-es/dotnet/api/system/ |
| **Colecciones** | https://learn.microsoft.com/es-es/dotnet/standard/collections/ |
| **Genéricos** | https://learn.microsoft.com/es-es/dotnet/standard/generics/ |

### ADO.NET (para unidades futuras)

| Tema | Link |
|------|------|
| **ADO.NET Overview** | https://learn.microsoft.com/es-es/dotnet/framework/data/adonet/ado-net-overview |
| **SqlConnection** | https://learn.microsoft.com/es-es/dotnet/api/system.data.sqlclient.sqlconnection |
| **SqlCommand** | https://learn.microsoft.com/es-es/dotnet/api/system.data.datacommand |
| **SqlDataReader** | https://learn.microsoft.com/es-es/dotnet/api/system.data.sqlclient.sqldatareader |

---

## Cursos Gratuitos

### Microsoft Learn

| Curso | Nivel | Duración | Link |
|-------|-------|----------|------|
| **C# para principiantes** | Principiante | 10 módulos | [Ver](https://learn.microsoft.com/es-es/training/paths/csharp-first-steps/) |
| **Crear apps de consola con C#** | Principiante | 12 módulos | [Ver](https://learn.microsoft.com/es-es/training/paths/build-csharp-console-apps/) |
| **Crear apps web con ASP.NET Core** | Intermedio | 15 módulos | [Ver](https://learn.microsoft.com/es-es/training/paths/build-web-apps-aspnet-core/) |
| **Trabajar con datos en .NET** | Intermedio | 8 módulos | [Ver](https://learn.microsoft.com/es-es/training/paths/work-data-dotnet/) |

### Otros Cursos Gratuitos

| Plataforma | Curso | Link |
|------------|-------|------|
| **freeCodeCamp** | C# Tutorial - Full Course | [YouTube](https://www.youtube.com/watch?v=Gghh8YrUWLI) |
| **Microsoft Virtual Academy** | C# Fundamentals | [Archivos](https://mva.microsoft.com/) |
| **Pluralsight (prueba gratis)** | C# Language Fundamentals | [Ver](https://www.pluralsight.com/) |

---

## Videos Recomendados

### Conceptos Fundamentales

| Tema | Duración | Link |
|------|----------|------|
| **Stack vs Heap explicado** | 10 min | [YouTube](https://www.youtube.com/results?search_query=stack+vs+heap+c%23) |
| **Value vs Reference Types** | 15 min | [YouTube](https://www.youtube.com/results?search_query=value+vs+reference+types+c%23) |
| **Nullable Types en C#** | 8 min | [YouTube](https://www.youtube.com/results?search_query=nullable+types+c%23) |
| **Pattern Matching C# 8+** | 12 min | [YouTube](https://www.youtube.com/results?search_query=pattern+matching+c%23) |
| **StringBuilder vs String** | 6 min | [YouTube](https://www.youtube.com/results?search_query=stringbuilder+vs+string+c%23) |

### Tutoriales de Visual Studio

| Tema | Duración | Link |
|------|----------|------|
| **Instalación de VS 2022** | 5 min | [YouTube](https://www.youtube.com/results?search_query=visual+studio+2022+installation) |
| **Debugging en VS 2022** | 15 min | [YouTube](https://www.youtube.com/results?search_query=debugging+visual+studio+2022) |
| **Atajos de VS 2022** | 8 min | [YouTube](https://www.youtube.com/results?search_query=visual+studio+shortcuts+2022) |

### C# 12 Features

| Tema | Duración | Link |
|------|----------|------|
| **Primary Constructors** | 10 min | [YouTube](https://www.youtube.com/results?search_query=primary+constructors+c%23+12) |
| **Collection Expressions** | 8 min | [YouTube](https://www.youtube.com/results?search_query=collection+expressions+c%23+12) |
| **Novedades de C# 12** | 20 min | [YouTube](https://www.youtube.com/results?search_query=whats+new+c%23+12) |

---

## Libros Recomendados

### Gratuitos / Open Source

| Libro | Autor | Año | Link |
|-------|-------|-----|------|
| **C# 10 in a Nutshell** | Joseph Albahari | 2022 | [Online](https://www.oreilly.com/library/view/c-10-in/9781098121896/) |
| **Programming C#** | Ian Griffiths | 2021 | [O'Reilly](https://www.oreilly.com/library/view/programming-c-8/9781492057190/) |
| **C# Yellow Book** | Rob Miles | 2020 | [PDF Gratis](http://www.robmiles.com/c-yellow-book) |

### Comerciales (Recomendados)

| Libro | Autor | Nivel | Precio aprox. |
|-------|-------|-------|---------------|
| **C# 12 and .NET 8 - Modern Cross-Platform** | Mark J. Price | Principiante-Intermedio | $35-50 USD |
| **Pro C# 10 with .NET 6** | Andrew Troelsen | Intermedio-Avanzado | $40-60 USD |
| **Clean Code in C#** | Jason Alls | Intermedio | $30-45 USD |
| **Design Patterns in C#** | Steven Metsker | Avanzado | $40-55 USD |

---

## Herramientas y Extensiones

### Visual Studio Extensions

| Extensión | Propósito | Link |
|-----------|-----------|------|
| **Productivity Power Tools** | Mejoras de productividad | [Marketplace](https://marketplace.visualstudio.com/items?itemName=VisualStudioProductTeam.ProductivityPowerTools2022) |
| **CodeMaid** | Limpieza de código | [Marketplace](https://marketplace.visualstudio.com/items?itemName=SteveCadwallader.CodeMaid) |
| **NuGet Package Explorer** | Explorar paquetes NuGet | [Marketplace](https://marketplace.visualstudio.com/items?SelectedItem=NuGetPackageExplorer.NuGetPackageExplorer) |
| **GitLens** | Git supercharge | [Marketplace](https://marketplace.visualstudio.com/items?itemName=GitLens.GitLensforVisualStudio2022) |
| **Live Share** | Colaboración en tiempo real | [Marketplace](https://marketplace.visualstudio.com/items?itemName=MSCELiveShare.v2022) |

### VS Code Extensions (para archivos .cs)

| Extensión | Propósito | Link |
|-----------|-----------|------|
| **C# Dev Kit** | Desarrollo C# en VS Code | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit) |
| **.NET Install Tool** | Instalar .NET SDK | [Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscode-dotnet-runtime) |

### Herramientas de Línea de Comando

| Herramienta | Propósito | Instalación |
|-------------|-----------|-------------|
| **dotnet ef** | Entity Framework Core | `dotnet tool install --global dotnet-ef` |
| **dotnet format** | Formatear código | `dotnet tool install --global dotnet-format` |
| **JetBrains Rider** | IDE alternativo (multi-plataforma) | [Descargar](https://www.jetbrains.com/rider/) |

---

## Comunidad y Soporte

### Foros y Comunidades

| Comunidad | Link |
|-----------|------|
| **Stack Overflow - C# Tag** | https://stackoverflow.com/questions/tagged/c%23 |
| **C# Discord** | https://discord.gg/csharp |
| **Reddit - r/csharp** | https://reddit.com/r/csharp |
| **Microsoft Q&A** | https://learn.microsoft.com/en-us/answers/products/ |
| **C# Corner** | https://www.c-sharpcorner.com/ |

### Grupos en Español

| Comunidad | Link |
|-----------|------|
| **Comunidad de .NET en Español (Slack)** | https://dotnetnet.slack.com |
| **DotNet Colombia** | https://www.meetup.com/es-ES/DotNetColombia/ |
| **Argentina .NET User Group** | https://www.meetup.com/es-ARG/Argentina-NET-User-Group/ |

### Cuentas de Twitter/X a Seguir

| Cuenta | Descripción |
|--------|-------------|
| [@dotnet](https://twitter.com/dotnet) | Cuenta oficial de .NET |
| [@csharp](https://twitter.com/search?q=%23csharp) | Hashtag C# |
| [@scottgu](https://twitter.com/scottgu) | Scott Guthrie (VP Microsoft) |
| [@davidfowl](https://twitter.com/davidfowl) | David Fowler (Architect ASP.NET) |

---

## Ejercicios Adicionales

### Sitios de Práctica

| Sitio | Descripción | Link |
|-------|-------------|------|
| **Exercism - C# Track** | Ejercicios con mentoría | https://exercism.org/tracks/csharp |
| **Codewars - C#** | Katas de programación | https://www.codewars.com/kata/search/c%23 |
| **HackerRank - C#** | Desafíos de código | https://www.hackerrank.com/domains/csharp |
| **LeetCode - C#** | Algoritmos y estructuras | https://leetcode.com/ |

### Proyectos de Práctica

| Nivel | Proyecto | Descripción |
|-------|----------|-------------|
| **Principiante** | Calculadora | App de consola con operaciones básicas |
| **Principiante** | To-Do List | CRUD de tareas en consola |
| **Intermedio** | Agenda de Contactos | Persistencia en archivos JSON |
| **Intermedio** | Sistema de Biblioteca | Gestión de libros y préstamos |
| **Avanzado** | API REST | ASP.NET Core con base de datos |

---

## Cheat Sheets

### Atajos de Visual Studio 2022

| Atajo | Acción |
|-------|--------|
| `F5` | Iniciar debug |
| `Ctrl+F5` | Ejecutar sin debug |
| `Shift+F5` | Detener debug |
| `F9` | Toggle breakpoint |
| `F10` | Step Over |
| `F11` | Step Into |
| `Shift+F11` | Step Out |
| `Ctrl+K, C` | Comentar selección |
| `Ctrl+K, U` | Descomentar selección |
| `Ctrl+Space` | IntelliSense |
| `Ctrl+.` | Quick Actions |
| `F12` | Ir a definición |
| `Shift+F12` | Find all references |
| `Ctrl+R, R` | Renombrar |
| `Ctrl+-` | Navegar atrás |

### Comandos dotnet CLI

| Comando | Descripción |
|---------|-------------|
| `dotnet new console` | Crear proyecto de consola |
| `dotnet new mvc` | Crear proyecto ASP.NET MVC |
| `dotnet build` | Compilar proyecto |
| `dotnet run` | Ejecutar proyecto |
| `dotnet test` | Ejecutar pruebas |
| `dotnet add package <nombre>` | Agregar paquete NuGet |
| `dotnet list package` | Listar paquetes |
| `dotnet publish -c Release` | Publicar para producción |
| `dotnet format` | Formatear código |

### Especificadores de Formato

| Especificador | Ejemplo | Salida |
|---------------|---------|--------|
| `C` / `c` | `1234.56.ToString("C")` | `$1,234.56` |
| `D` / `d` | `1234.ToString("D6")` | `001234` |
| `E` / `e` | `1234.ToString("E2")` | `1.23E+003` |
| `F` / `f` | `1234.5678.ToString("F2")` | `1234.57` |
| `N` / `n` | `1234.56.ToString("N2")` | `1,234.57` |
| `P` / `p` | `0.1234.ToString("P2")` | `12.34%` |
| `X` / `x` | `255.ToString("X")` | `FF` |

---

## Próximos Pasos

### Preparación para la Clase 2

Antes de la próxima clase, asegúrate de:

- [ ] Revisar conceptos de **clases y objetos** (POO básico)
- [ ] Entender qué es **encapsulamiento**
- [ ] Tener lista la **tarea de Calculadora de Promedios**
- [ ] Crear tu **cuenta de GitHub** (si no tienes)
- [ ] Leer sobre **propiedades** en C# (getters/setters)

### Lecturas Recomendadas

1. **Object-Oriented Programming Concepts**
   https://learn.microsoft.com/es-es/dotnet/csharp/fundamentals/object-oriented-programming

2. **Classes and Structs**
   https://learn.microsoft.com/es-es/dotnet/csharp/fundamentals/types/classes-and-structs

3. **Properties**
   https://learn.microsoft.com/es-es/dotnet/csharp/programming-guide/classes-and-structs/properties

---

**Volver al [índice](./README.md)**
