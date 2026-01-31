---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'

  section {
    font-size: 24px;
  }

---
<style>
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
}
section {
  font-size: 24px;
}
</style>


<!--
[2026-01-31] - Clase enriquecida con infografías

IMÁGENES GENERADAS:
- clase-04-sobrecarga-vs-sobreescritura.png: Comparación visual entre sobrecarga y sobreescritura
-->

# Clase 4: Sobrecarga, Sobreescritura y Modelamiento de BD
## Polimorfismo estático y diseño de datos

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Diferenciar** entre sobrecarga (overload) y sobreescritura (override)
2. **Implementar** sobrecarga de métodos y constructores
3. **Aplicar** sobrecarga de operadores en C#
4. **Modelar** bases de datos relacionales usando diagramas ER
5. **Identificar** relaciones 1-1, 1-N y N-M en el contexto de POO

**Duración:** 90 minutos

---

## Agenda

1. Sobrecarga vs Sobreescritura (15 min)
2. Sobrecarga de métodos (15 min)
3. Sobrecarga de operadores (15 min)
4. Modelamiento de bases de datos (20 min)
5. Mapeo Objetos-Relacional (15 min)
6. Ejercicio práctico (10 min)

---

## 1. Sobrecarga vs Sobreescritura

### Dos conceptos frecuentemente confundidos

![Sobrecarga vs Sobreescritura](../../assets/infografias/clase-04-sobrecarga-vs-sobreescritura.png)

---

### Representación ASCII:
```
┌─────────────────────────────────────────────────────────────┐
│           SOBRECARGA (OVERLOADING)                          │
│                    vs                                         │
│           SOBREESCRITURA (OVERRIDING)                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SOBRECARGA                    SOBREESCRITURA               │
│  ───────────                   ──────────────               │
│                                                             │
│  • Misma clase                 • Clase padre → hija         │
│  • Mismo nombre                • Mismo nombre y firma       │
│  • Diferentes parámetros       • Misma firma                │
│                                                             │
│  class Calculadora {           class Animal {               │
│    int Sumar(int a, int b) {     virtual void Hablar() {}   │
│      return a + b;             }                            │
│    }                           class Perro : Animal {       │
│    double Sumar(double a,        override void Hablar() {}  │
│             double b) {        }                            │
│      return a + b;                                          │
│    }                                                          │
│  }                                                          │
│                                                             │
│  = POLIMORFISMO ESTÁTICO       = POLIMORFISMO DINÁMICO      │
│  (en tiempo de compilación)    (en tiempo de ejecución)     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Sobrecarga de Métodos

### Mismo nombre, diferentes parámetros

```csharp
public class Calculadora
{
    // SOBRECARGA 1: Dos enteros
    public int Sumar(int a, int b)
    {
        Console.WriteLine("Sumando enteros...");
        return a + b;
    }
    
    // SOBRECARGA 2: Tres enteros (cantidad diferente)
    public int Sumar(int a, int b, int c)
    {
        Console.WriteLine("Sumando tres enteros...");
        return a + b + c;
    }
    
    // SOBRECARGA 3: Dos doubles (tipo diferente)
    public double Sumar(double a, double b)
    {
        Console.WriteLine("Sumando doubles...");
        return a + b;
    }
    
    // SOBRECARGA 4: Array de números (estructura diferente)
    public int Sumar(params int[] numeros)
    {
        Console.WriteLine("Sumando array...");
        return numeros.Sum();
    }
}
```

---

## Uso de Sobrecarga

### El compilador elige la versión apropiada

```csharp
class Program
{
    static void Main(string[] args)
    {
        Calculadora calc = new Calculadora();
        
        // El compilador decide cuál método llamar
        int r1 = calc.Sumar(5, 3);           // → Sumar(int, int)
        int r2 = calc.Sumar(5, 3, 2);        // → Sumar(int, int, int)
        double r3 = calc.Sumar(5.5, 3.2);    // → Sumar(double, double)
        int r4 = calc.Sumar(1, 2, 3, 4, 5);  // → Sumar(params int[])
        
        Console.WriteLine($"Resultados: {r1}, {r2}, {r3}, {r4}");
        // Salida: 8, 10, 8.7, 15
    }
}
```

**Reglas para sobrecargar:**
- ✅ Diferente cantidad de parámetros
- ✅ Diferentes tipos de parámetros
- ✅ Diferente orden de parámetros
- ❌ Solo diferente tipo de retorno (no es suficiente)

---

## Sobrecarga de Constructores

### Ya lo hemos visto aplicado

```csharp
public class Estudiante
{
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    public string Carrera { get; set; }
    
    // Constructor 1: Sin parámetros
    public Estudiante()
    {
        Nombre = "Sin nombre";
        Codigo = "0000000";
        Edad = 18;
        Carrera = "Sin carrera";
    }
    
    // Constructor 2: Dos parámetros
    public Estudiante(string nombre, string codigo)
    {
        Nombre = nombre;
        Codigo = codigo;
        Edad = 18;
        Carrera = "Sin carrera";
    }
    
    // Constructor 3: Cuatro parámetros
    public Estudiante(string nombre, string codigo, int edad, string carrera)
    {
        Nombre = nombre;
        Codigo = codigo;
        Edad = edad;
        Carrera = carrera;
    }
}
```

---

## Llamando Constructores Entre Sí

### La palabra clave `this`

```csharp
public class Estudiante
{
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    public string Carrera { get; set; }
    
    // Constructor principal (con todos los parámetros)
    public Estudiante(string nombre, string codigo, int edad, string carrera)
    {
        Nombre = nombre;
        Codigo = codigo;
        Edad = edad;
        Carrera = carrera;
    }
    
    // Llama al constructor principal con valores por defecto
    public Estudiante(string nombre, string codigo) 
        : this(nombre, codigo, 18, "Sin carrera")
    {
        // No necesita código, todo lo hace el otro constructor
    }
    
    // Llama al de 2 parámetros, que a su vez llama al principal
    public Estudiante() 
        : this("Sin nombre", "0000000")
    {
    }
}
```

---

## 3. Sobrecarga de Operadores

### Definiendo comportamiento de operadores

```csharp
public class Fraccion
{
    public int Numerador { get; set; }
    public int Denominador { get; set; }
    
    public Fraccion(int numerador, int denominador)
    {
        Numerador = numerador;
        Denominador = denominador != 0 ? denominador : 1;
    }
    
    // SOBRECARGA DEL OPERADOR +
    public static Fraccion operator +(Fraccion a, Fraccion b)
    {
        int nuevoNum = a.Numerador * b.Denominador + b.Numerador * a.Denominador;
        int nuevoDen = a.Denominador * b.Denominador;
        return new Fraccion(nuevoNum, nuevoDen);
    }
    
    // SOBRECARGA DEL OPERADOR -
    public static Fraccion operator -(Fraccion a, Fraccion b)
    {
        int nuevoNum = a.Numerador * b.Denominador - b.Numerador * a.Denominador;
        int nuevoDen = a.Denominador * b.Denominador;
        return new Fraccion(nuevoNum, nuevoDen);
    }
    
    // SOBRECARGA DE ToString()
    public override string ToString()
    {
        return $"{Numerador}/{Denominador}";
    }
}
```

---

## Uso de Operadores Sobrecargados

### Sintaxis natural

```csharp
class Program
{
    static void Main(string[] args)
    {
        Fraccion f1 = new Fraccion(1, 2);   // 1/2
        Fraccion f2 = new Fraccion(1, 3);   // 1/3
        
        // Usar operadores sobrecargados
        Fraccion suma = f1 + f2;    // Llama a operator +
        Fraccion resta = f1 - f2;   // Llama a operator -
        
        Console.WriteLine($"{f1} + {f2} = {suma}");   // 1/2 + 1/3 = 5/6
        Console.WriteLine($"{f1} - {f2} = {resta}");  // 1/2 - 1/3 = 1/6
    }
}
```

**Operadores que se pueden sobrecargar:**
- Aritméticos: `+`, `-`, `*`, `/`, `%`
- Comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Conversión: `implicit`, `explicit`
- Otros: `++`, `--`, `!`, `~`, `&`, `|`, `^`

**NO se pueden sobrecargar:** `&&`, `||`, `??`, `?:`, `=`, `.`

---

## Sobrecarga de Operadores de Comparación

### Implementando igualdad

```csharp
public class Punto
{
    public int X { get; set; }
    public int Y { get; set; }
    
    public Punto(int x, int y) { X = x; Y = y; }
    
    // Sobrecarga de ==
    public static bool operator ==(Punto a, Punto b)
    {
        if (ReferenceEquals(a, null))
            return ReferenceEquals(b, null);
        return a.X == b.X && a.Y == b.Y;
    }
    
    // Sobrecarga de != (siempre en pareja con ==)
    public static bool operator !=(Punto a, Punto b)
    {
        return !(a == b);
    }
    
    // Siempre sobrescribir Equals y GetHashCode junto con ==
    public override bool Equals(object obj)
    {
        if (obj is Punto otro)
            return this == otro;
        return false;
    }
    
    public override int GetHashCode()
    {
        return (X, Y).GetHashCode();
    }
}
```

---

## 4. Modelamiento de Bases de Datos

### Introducción al diseño de datos

```
┌─────────────────────────────────────────────────────────────┐
│              DEL MUNDO REAL A LA BASE DE DATOS              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   MUNDO REAL        →   MODELO CONCEPTUAL   →   TABLAS     │
│                                                             │
│   Estudiantes            Entidad             Tabla          │
│      ↓                      ↓                   ↓           │
│   • Nombre              Atributos          Columnas         │
│   • Código              (propiedades)      (campos)         │
│   • Edad                                     ↓              │
│   • Carrera               ↓                Registros        │
│                        Relaciones          (filas)          │
│                          (PK, FK)                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Entidades y Atributos

### Representación en diagramas ER

```
┌─────────────────────────────────────────────────────────────┐
│                   DIAGRAMA ENTIDAD-RELACIÓN                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────────────┐                                   │
│   │    ESTUDIANTE       │  ← Entidad (tabla)                │
│   ├─────────────────────┤                                   │
│   │ * PK codigo         │  ← Clave primaria (identificador) │
│   │   nombre            │  ← Atributo simple                │
│   │   edad              │  ← Atributo numérico              │
│   │   email             │  ← Atributo único                 │
│   │   fecha_nacimiento  │  ← Atributo fecha                 │
│   │ FK carrera_id       │  ← Clave foránea (relación)       │
│   └─────────────────────┘                                   │
│                                                             │
│   PK = Primary Key (no nulo, único)                         │
│   FK = Foreign Key (referencia a otra tabla)                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Tipos de Atributos

### Clasificación de propiedades

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE ATRIBUTOS                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Por Cardinalidad:                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Simple     │  │  Compuesto   │  │ Multivaluado │      │
│  │              │  │              │  │              │      │
│  │ nombre       │  │ dirección    │  │ teléfonos    │      │
│  │ (único)      │  │ (calle,      │  │ (varios)     │      │
│  │              │  │  ciudad...)  │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
│  Por Nulidad:                                               │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │  Obligatorio │  │   Opcional   │                        │
│  │  (NOT NULL)  │  │   (NULL)     │                        │
│  │              │  │              │                        │
│  │ nombre       │  │  teléfono2   │                        │
│  └──────────────┘  └──────────────┘                        │
│                                                             │
│  Derivado:                                                  │
│  ┌──────────────┐                                          │
│  │   edad       │  ← Se calcula de fecha_nacimiento        │
│  └──────────────┘                                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Relaciones entre Entidades

### Cardinalidad

```
┌─────────────────────────────────────────────────────────────┐
│                   TIPOS DE RELACIONES                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1:1 (UNO A UNO)                                            │
│  ┌─────────┐         ┌─────────┐                           │
│  │ Persona │─────────│ Pasaporte│                           │
│  └─────────┘ 1     1 └─────────┘                           │
│  Una persona tiene un solo pasaporte                        │
│                                                             │
│  1:N (UNO A MUCHOS)                                         │
│  ┌─────────┐         ┌─────────┐                           │
│  │ Carrera │────────<│Estudiante│                           │
│  └─────────┘ 1     N └─────────┘                           │
│  Una carrera tiene muchos estudiantes                       │
│                                                             │
│  N:M (MUCHOS A MUCHOS)                                      │
│  ┌─────────┐         ┌─────────┐                           │
│  │Estudiante│>───────<│ Materia │                           │
│  └─────────┘ N     M └─────────┘                           │
│  Un estudiante cursa muchas materias,                       │
│  una materia tiene muchos estudiantes                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Ejemplo: Sistema Universitario

### Diagrama ER completo

```
┌──────────────────────────────────────────────────────────────────────┐
│                    SISTEMA UNIVERSITARIO                             │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   ┌─────────────┐              ┌─────────────┐                      │
│   │   CARRERA   │              │  ESTUDIANTE │                      │
│   ├─────────────┤              ├─────────────┤                      │
│   │ PK id       │1────────────N│ PK codigo   │                      │
│   │   nombre    │              │   nombre    │                      │
│   │   duracion  │              │   email     │                      │
│   │   facultad  │              │ FK carrera_id│                     │
│   └─────────────┘              └──────┬──────┘                      │
│                                       │                              │
│                                       │ N                            │
│                                       │                              │
│                                      ╱│╲                             │
│                                     ╱ │ ╲                            │
│                                    ╱  │  ╲                           │
│                              ┌────────┴────────┐                     │
│                              │  INSCRIPCION    │                     │
│                              ├─────────────────┤                     │
│                              │ PK id           │                     │
│                              │ FK estudiante_id│                     │
│                              │ FK materia_id   │                     │
│                              │   semestre      │                     │
│                              │   nota_final    │                     │
│                              └────────┬────────┘                     │
│                                       │ M                            │
│                                       │                              │
│                              ┌────────┴────────┐                     │
│                              │    MATERIA      │                     │
│                              ├─────────────────┤                     │
│                              │ PK id           │                     │
│                              │   nombre        │                     │
│                              │   creditos      │                     │
│                              │ FK profesor_id  │                     │
│                              └─────────────────┘                     │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 5. Mapeo Objeto-Relacional

### De clases a tablas

```csharp
// MODELO ORIENTADO A OBJETOS (C#)
public class Estudiante
{
    public string Codigo { get; set; }      // PK
    public string Nombre { get; set; }
    public string Email { get; set; }
    
    // Relación: Estudiante pertenece a una Carrera
    public Carrera Carrera { get; set; }    // FK en BD
    
    // Relación: Estudiante tiene muchas Inscripciones
    public List<Inscripcion> Inscripciones { get; set; }
}

public class Carrera
{
    public int Id { get; set; }             // PK
    public string Nombre { get; set; }
    
    // Relación: Carrera tiene muchos Estudiantes
    public List<Estudiante> Estudiantes { get; set; }
}
```

---

## Tablas SQL Equivalentes

```sql
-- MODELO RELACIONAL (SQL Server)

CREATE TABLE Carreras (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    Duracion INT,
    Facultad VARCHAR(100)
);

CREATE TABLE Estudiantes (
    Codigo VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Edad INT,
    CarreraId INT,
    FOREIGN KEY (CarreraId) REFERENCES Carreras(Id)
);

CREATE TABLE Materias (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    Creditos INT
);

CREATE TABLE Inscripciones (
    Id INT PRIMARY KEY IDENTITY(1,1),
    EstudianteCodigo VARCHAR(20),
    MateriaId INT,
    Semestre VARCHAR(10),
    NotaFinal DECIMAL(3,2),
    FOREIGN KEY (EstudianteCodigo) REFERENCES Estudiantes(Codigo),
    FOREIGN KEY (MateriaId) REFERENCES Materias(Id)
);
```

---

## Conversión de Tipos de Datos

### C# ↔ SQL Server

| C# | SQL Server | Descripción |
|----|------------|-------------|
| `int` | `INT` | Entero 32-bit |
| `long` | `BIGINT` | Entero 64-bit |
| `string` | `VARCHAR(n)` / `NVARCHAR(n)` | Texto (Unicode) |
| `decimal` | `DECIMAL(p,s)` | Decimal preciso |
| `double` | `FLOAT` | Punto flotante |
| `bool` | `BIT` | Booleano (0/1) |
| `DateTime` | `DATETIME` / `DATE` | Fecha y hora |
| `byte[]` | `VARBINARY` | Datos binarios |
| `Guid` | `UNIQUEIDENTIFIER` | GUID único |

---

## 6. Ejercicio Práctico

### Diseñar modelo para Biblioteca

```
REQUISITOS:

1. La biblioteca tiene LIBROS
   - ISBN (único)
   - Título
   - Autor
   - Año de publicación
   - Cantidad de ejemplares

2. Los libros pertenecen a CATEGORÍAS
   - Una categoría tiene muchos libros
   - Nombre de categoría

3. La biblioteca tiene USUARIOS
   - Código de usuario
   - Nombre
   - Email
   - Tipo (estudiante, profesor, externo)

4. Los usuarios realizan PRÉSTAMOS
   - Un usuario puede tener varios préstamos
   - Un libro puede estar en varios préstamos (en el tiempo)
   - Fecha de préstamo
   - Fecha de devolución esperada
   - Fecha de devolución real
   - Estado (activo, devuelto, vencido)

TAREA: Crear diagrama ER y clases C# correspondientes
```

---

## Solución Ejercicio Biblioteca

### Diagrama ER

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│  CATEGORIA  │       │    LIBRO    │       │  PRESTAMO   │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ PK id       │1─────N│ PK isbn     │1─────N│ PK id       │
│   nombre    │       │   titulo    │       │ FK libro_id │
└─────────────┘       │   autor     │       │ FK usuario_id│
                      │   anio      │       │   fecha_prestamo│
                      │   cantidad  │       │   fecha_devolucion│
                      │ FK categoria_id    │   estado    │
                      └─────────────┘       └──────┬──────┘
                                                   │ N
                                                   │
                                          ┌────────┴────────┐
                                          │    USUARIO      │
                                          ├─────────────────┤
                                          │ PK codigo       │
                                          │   nombre        │
                                          │   email         │
                                          │   tipo          │
                                          └─────────────────┘
```

---

## Clases C# para Biblioteca

```csharp
public class Categoria
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    
    // Relación 1:N
    public List<Libro> Libros { get; set; }
}

public class Libro
{
    public string ISBN { get; set; }
    public string Titulo { get; set; }
    public string Autor { get; set; }
    public int AnioPublicacion { get; set; }
    public int CantidadEjemplares { get; set; }
    
    // Relación N:1
    public int CategoriaId { get; set; }
    public Categoria Categoria { get; set; }
    
    // Relación 1:N
    public List<Prestamo> Prestamos { get; set; }
}

public class Usuario
{
    public string Codigo { get; set; }
    public string Nombre { get; set; }
    public string Email { get; set; }
    public string Tipo { get; set; } // Estudiante, Profesor, Externo
    
    // Relación 1:N
    public List<Prestamo> Prestamos { get; set; }
}

public class Prestamo
{
    public int Id { get; set; }
    public DateTime FechaPrestamo { get; set; }
    public DateTime FechaDevolucionEsperada { get; set; }
    public DateTime? FechaDevolucionReal { get; set; }
    public string Estado { get; set; }
    
    // Relaciones N:1
    public string LibroISBN { get; set; }
    public Libro Libro { get; set; }
    
    public string UsuarioCodigo { get; set; }
    public Usuario Usuario { get; set; }
}
```

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **Sobrecarga** | Mismo nombre, diferentes parámetros (misma clase) |
| **Sobreescritura** | Misma firma, reimplementación (padre→hija) |
| `this` | Llama a otro constructor de la misma clase |
| **Operador sobrecargado** | Define comportamiento de operadores |
| **Entidad** | Objeto del mundo real → tabla en BD |
| **Atributo** | Propiedad de entidad → columna en BD |
| **Relación 1:N** | Una entidad tiene muchas otras |
| **Relación N:M** | Tabla intermedia para relacionar |

---

## Ejercicios Propuestos

### Para practicar

**Ejercicio 1: Clase Complejo**
Crear una clase `Complejo` que represente números complejos (a + bi) con sobrecarga de:
- `+` (suma de complejos)
- `-` (resta)
- `*` (multiplicación)
- `==` y `!=` (comparación)
- `ToString()` para mostrar como "3 + 4i"

**Ejercicio 2: Modelar Tienda Online**
Diseñar diagrama ER y clases C# para:
- Clientes, Productos, Categorías, Órdenes, DetalleOrden
- Un cliente hace muchas órdenes
- Una orden tiene muchos productos (detalle)
- Un producto pertenece a una categoría

---

## Preparación Unidad 2

### Próximos temas: TDD, BDD, DDD

```
UNIDAD 2: TÉCNICAS DE DESARROLLO DE SOFTWARE

• Test Driven Development (TDD)
  - Red-Green-Refactor
  - Pruebas unitarias con xUnit/NUnit
  
• Behavior Driven Development (BDD)
  - Lenguaje Gherkin
  - Given-When-Then
  
• Domain Driven Design (DDD)
  - Entidades, Value Objects, Aggregates
  - Repositorios, Servicios de dominio
```

**Instalar para la próxima clase:**
- Extensión xUnit para Visual Studio
- O crear proyecto con: `dotnet new xunit`

---

## Evaluación 1 (15%) - Semana 4

### Taller + Quiz de POO

**Contenido:**
- Clases, objetos, propiedades
- Herencia y polimorfismo
- Sobrecarga y sobreescritura
- Modelamiento de bases de datos

**Formato:**
- Quiz teórico (30 min)
- Ejercicio práctico en Visual Studio (90 min)

**Entrega:** Proyecto de C# con el ejercicio resuelto

---

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
