# Referencias - Clase 04

**IF0100 - Lenguaje de Programación OO II**
*Unidad 1 - Sobrecarga, Sobreescritura y Modelado BD*

---

## Recursos Oficiales

### Documentación Microsoft

| Recurso | Enlace | Descripción |
|---------|--------|-------------|
| **Method Overloading** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/methods/overloading-methods) | Sobrecarga de métodos |
| **Operator Overloading** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/operator-overloading) | Sobrecarga de operadores |
| **Overloadable Operators** | [docs.microsoft.com](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/operator-overloading#overloadable-operators) | Lista de operadores sobrecargables |
| **Entity Framework** | [docs.microsoft.com](https://learn.microsoft.com/en-us/ef/) | ORM oficial de .NET |
| **EF Core Getting Started** | [docs.microsoft.com](https://learn.microsoft.com/en-us/ef/core/get-started/overview/first-app) | Tutorial de EF Core |

---

## Modelado de Bases de Datos

### Recursos de Diseño

| Recurso | Enlace | Descripción |
|---------|--------|-------------|
| **ER Diagrams** | [ lucidchart.com](https://www.lucidchart.com/pages/er-diagrams) | Guía de diagramas ER |
| **Database Normalization** | [postgresql.org](https://www.postgresql.org/docs/current/ normalization.html) | Normalización explicada |
| **3NF Explained** | [db.grussell.org](http://www.db.grussell.org/) | Tercera Forma Normal |

### Herramientas de Modelado

| Herramienta | Tipo | Licencia |
|-------------|------|----------|
| **SQL Server Management Studio** | ER Designer | Gratis |
| **MySQL Workbench** | ER Designer | Gratis |
| **draw.io** | Diagramas online | Gratis |
| **Lucidchart** | Diagramas online | Freemium |
| **Navicat Data Modeler** | ER Designer | Freemium |

---

## Tutoriales y Cursos Online

### YouTube

| Canal | Video | Duración |
|-------|-------|----------|
| **IAmTimCorey** | C# Operator Overloading | 25 min |
| **Programming with Mosh** | C# Classes | 30 min |
| **kudvenkat** | Entity Framework | 3 horas |

### Cursos Interactivos

| Plataforma | Curso | Duración |
|------------|-------|----------|
| **Microsoft Learn** | Introduction to Entity Framework Core | 2 horas |
| **Pluralsight** | Entity Framework Core Fundamentals | 4 horas |
| **Udemy** | C# Advanced Topics | 6 horas |

---

## Libros Recomendados

### C# y POO

| Libro | Autor | Año | Capítulos |
|-------|-------|-----|-----------|
| **C# in Depth** | Jon Skeet | 2019 | Overloading, Operators |
| **Professional C#** | Christian Nagel | 2021 | OOP, EF Core |

### Bases de Datos

| Libro | Autor | Año |
|-------|-------|-----|
| **Database System Concepts** | Silberschatz | 2020 |
| **SQL for Mere Mortals** | Hernandez | 2019 |

---

## Glosario de Términos

| Término | Definición |
|---------|------------|
| **Sobrecarga (Overload)** | Mismo método, diferentes parámetros |
| **Sobreescritura (Override)** | Mismo método, reimplementación en hija |
| **Operador sobrecargado** | Operador con comportamiento personalizado |
| **PK** | Primary Key, identificador único de una tabla |
| **FK** | Foreign Key, referencia a otra tabla |
| **1:N** | Relación uno a muchos |
| **N:M** | Relación muchos a muchos |
| **3FN** | Tercera Forma Normal de normalización |
| **ORM** | Object-Relational Mapping |
| **Cardinalidad** | Número de entidades en una relación |

---

## Cheat Sheet

### Sobrecarga de Métodos

```csharp
// ✅ Válido: diferentes parámetros
void Imprimir(int x) { }
void Imprimir(string s) { }
void Imprimir(int x, int y) { }

// ❌ Inválido: solo difiere en retorno
int Sumar(int a, int b) => a + b;
double Sumar(int a, int b) => (double)(a + b);
```

### Sobrecarga de Operadores

```csharp
// Operadores aritméticos
public static Tipo operator +(Tipo a, Tipo b)
public static Tipo operator -(Tipo a, Tipo b)

// Operadores de comparación (siempre en pares)
public static bool operator ==(Tipo a, Tipo b)
public static bool operator !=(Tipo a, Tipo b) => !(a == b);

// No olvidar Equals y GetHashCode
public override bool Equals(object obj) => obj is Tipo t && this == t;
public override int GetHashCode() => (Prop1, Prop2).GetHashCode();
```

### Mapeo C# ↔ SQL

| C# | SQL | Ejemplo |
|----|-----|---------|
| `int` | `INT` | `Edad INT` |
| `string` | `VARCHAR(n)` | `Nombre VARCHAR(100)` |
| `decimal` | `DECIMAL(p,s)` | `Precio DECIMAL(10,2)` |
| `bool` | `BIT` | `Activo BIT` |
| `DateTime` | `DATETIME2` | `Fecha DATETIME2` |

---

## Scripts SQL Útiles

### Crear Tabla con FK

```sql
CREATE TABLE Estudiantes (
    Codigo VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    CarreraId INT,
    FOREIGN KEY (CarreraId) REFERENCES Carreras(Id)
);
```

### Tabla Intermedia N:M

```sql
CREATE TABLE Inscripciones (
    Id INT PRIMARY KEY IDENTITY,
    EstudianteCodigo VARCHAR(20),
    MateriaId INT,
    Fecha DATETIME2,
    FOREIGN KEY (EstudianteCodigo) REFERENCES Estudiantes(Codigo),
    FOREIGN KEY (MateriaId) REFERENCES Materias(Id)
);
```

---

**Última actualización:** 2026-02-01
