# Referencias - Clase 03

**IF0100 - Lenguaje de Programación OO II**
*Unidad 1 - Herencia y Polimorfismo*

---

## Recursos Oficiales

### Documentación Microsoft

| Recurso | Enlace | Descripción |
|---------|--------|-------------|
| **Polimorfismo** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/polymorphism) | Guía oficial de polimorfismo en C# |
| **Herencia** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/inheritance) | Guía oficial de herencia |
| **abstract** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract) | Palabra clave abstract |
| **virtual** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual) | Palabra clave virtual |
| **override** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/override) | Palabra clave override |
| **sealed** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/sealed) | Palabra clave sealed |
| **base** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/base) | Palabra clave base |

---

## Libros Recomendados

### C# y .NET

| Libro | Autor | Año | Capítulos Relevantes |
|-------|-------|-----|---------------------|
| **C# and the .NET Platform** | Andrew Troelsen | 2000 | Herencia, Polimorfismo |
| **Professional C#** | Christian Nagel | 2021 | OOP, Clases Abstractas |
| **C# in Depth** | Jon Skeet | 2019 | Polimorfismo Avanzado |

### Diseño Orientado a Objetos

| Libro | Autor | Año | Relevancia |
|-------|-------|-----|------------|
| **Clean Code** | Robert C. Martin | 2008 | Principios SOLID |
| **Agile Software Development** | Robert C. Martin | 2002 | LSP explicado |
| **Design Patterns** | Gang of Four | 1994 | Patrones de diseño |

---

## Tutoriales y Cursos Online

### Microsoft Learn

| Curso | Duración | Nivel | Enlace |
|-------|----------|-------|--------|
| **Object-Oriented Programming** | 2 horas | Principiante | [learn.microsoft.com](https://learn.microsoft.com/en-us/training/paths/explore-c-shell/) |
| **C# Polymorphism** | 1 hora | Intermedio | [learn.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/object-oriented/polymorphism) |

### YouTube

| Canal | Video | Duración |
|-------|-------|----------|
| **Microsoft Developers** | C# Inheritance | 15 min |
| **IAmTimCorey** | OOP in C# | 45 min |
| **Programming with Mosh** | C# Abstract Classes | 20 min |

---

## Artículos y Blog Posts

### Principios SOLID

| Artículo | Autor | Enlace |
|----------|-------|--------|
| **Liskov Substitution Principle** | Robert C. Martin | [butunclebob.com](https://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod) |
| **LSP Explained** | Derek Greer | [codebetter.com](https://codebetter.com/derekgreer/2011/11/09/liskov-substitution-principle/) |

### Casos de Estudio

| Artículo | Tema | Enlace |
|----------|------|--------|
| **Cuadrado vs Rectángulo** | LSP violation | [stackoverflow.com](https://stackoverflow.com/questions/14942412) |
| **When to use abstract** | Design guidelines | [docs.microsoft.com](https://docs.microsoft.com/en-us/archive/blogs/ericlippert) |

---

## Herramientas y Utilidades

### IDEs

| Herramienta | Versión | Licencia |
|-------------|---------|----------|
| **Visual Studio 2022** | 17.x | Gratis (Community) |
| **Visual Studio Code** | 1.x | Gratis |
| **Rider** | 2023.x | Pago |

### Extensiones Útiles

| Extensión | Propósito |
|-----------|-----------|
| **C# Dev Kit** | Desarrollo C# en VS Code |
| **.NET Core Test Explorer** | Ejecutar pruebas |
| **ReSharper** | Refactorización |

---

## Ejercicios Interactivos

### Plataformas de Práctica

| Plataforma | Ejercicios | Enlace |
|------------|------------|--------|
| **Exercism** | C# Track | [exercism.org](https://exercism.org/tracks/csharp) |
| **Codewars** | C# Katas | [codewars.com](https://www.codewars.com) |
| **LeetCode** | Algorithm problems | [leetcode.com](https://leetcode.com) |

---

## Glosario de Términos

| Término | Definición |
|---------|------------|
| **Herencia** | Mecanismo donde una clase adquiere miembros de otra |
| **Polimorfismo** | Capacidad de un método de tener diferentes comportamientos |
| **Clase Abstracta** | Clase que no puede instanciarse, sirve como plantilla |
| **Método Virtual** | Método que puede ser sobrescrito por clases derivadas |
| **Override** | Reemplazar la implementación de un método virtual/abstract |
| **Sealed** | Previene que una clase o método sea heredado/sobrescrito |
| **LSP** | Principio de Sustitución de Liskov |
| **Clase Base** | Clase que se hereda (padre, superclase) |
| **Clase Derivada** | Clase que hereda (hija, subclase) |

---

## Cheat Sheet

### Modificadores en Herencia

```csharp
// Clase sellada: no se puede heredar
public sealed class MiClase { }

// Método sellado: no se puede sobrescribir más
public sealed override void MiMetodo() { }

// Miembros protegidos: accesibles en la jerarquía
protected string MiCampo { get; set; }
```

### Plantilla de Clase Abstracta

```csharp
public abstract class MiClaseBase
{
    // Propiedad concreta
    public string Nombre { get; set; }

    // Método abstracto: hijas DEBEN implementar
    public abstract void MetodoAbstracto();

    // Método virtual: hijas PUEDEN sobrescribir
    public virtual void MetodoVirtual()
    {
        // Implementación default
    }

    // Método sellado: hijas NO pueden sobrescribir
    public sealed void MetodoFinal()
    {
        // Implementación fija
    }
}
```

---

## Preguntas Frecuentes

### ¿Cuándo usar `abstract` vs `interface`?

| `abstract` | `interface` |
|------------|-------------|
| Puede tener implementación | Solo firmas |
| Puede tener campos | Solo propiedades/métodos |
| Una sola herencia | Múltiples interfaces |
| Para relaciones "ES-UN" | Para comportamientos "PUEDE HACER" |

### ¿Por qué máximo 3 niveles de herencia?

- Más niveles = difícil de mantener
- Problemas de debugging
- Violación de principios de diseño
- Código frágil

### ¿Cuándo violo el principio LSP?

- Cuando la clase hija **cambia** el comportamiento esperado
- Cuando la clase hija **lanza excepciones** que el padre no
- Cuando la clase hija **requiere** condiciones que el padre no

---

## Bibliografía del Curso

### Básica (según syllabus oficial)

1. **"Programación Orientada a Objetos en C#"** - Pérez Chaves, Roger, Universidad de Matanzas, Colombia, 2003

2. **"C# and the .NET Platform"** - TROELSEN, Andrew, Apress, Colombia, 2000

3. **"Así es Microsoft Visual Studio .NET"** - Microsoft Corporation, Mc Graw-Hill, Colombia, 2000

4. **"Microsoft .NET Framework"** - Microsoft Corporation, Mc Graw-Hill, Colombia, 2000

---

**Última actualización:** 2026-02-01
