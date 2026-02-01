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

# Sobrecarga, Sobreescritura y Modelado de BD

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

![Sobrecarga vs Sobreescritura](../../assets/infografias/clase-04-sobrecarga-vs-sobreescritura.png){: style="max-width: 60%; max-height: 400px; display: block; margin: 0 auto;"}

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
### Representación ASCII:


---
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
    
---
### Mismo nombre, diferentes parámetros


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
---
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
    
---
### Ya lo hemos visto aplicado


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
    
---
### La palabra clave `this`


    // Llama al de 2 parámetros, que a su vez llama al principal
    public Estudiante() 
        : this("Sin nombre", "0000000")
    {
    }
}
```

---
## 3. Sobrecarga de Operadores
---
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
    
---
### Definiendo comportamiento de operadores


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
| - Otros: `++`, `--`, `!`, `~`, `&`, ` | `, `^` |

| **NO se pueden sobrecargar:** `&&`, ` |  | `, `??`, `?:`, `=`, `.` |

---
## Sobrecarga de Operadores de Comparación
---
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
    
---
### Implementando igualdad


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
### Clasificación de propiedades


---
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
### Cardinalidad


---
## Ejemplo: Sistema Universitario
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

---
## Tablas SQL Equivalentes


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
| ---- | ------------ | ------------- |
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

### Sistema de Biblioteca Universitaria

**Objetivo:** Diseñar el modelo de datos para un sistema de biblioteca con las siguientes entidades:

**Entidad: Libro**
- ISBN (único, identificador)
- Título
- Autor
- Año de publicación
- Cantidad de ejemplares disponibles

**Entidad: Categoría**
- ID (autoincremental)
- Nombre de categoría (Ficción, Ciencia, Tecnología, etc.)
- *Relación: Una categoría tiene muchos libros*

**Entidad: Usuario**
- Código de usuario (único)
- Nombre completo
- Email
- Tipo (estudiante, profesor, externo)
- *Relación: Un usuario puede tener varios préstamos*

**Entidad: Préstamo**
- ID (autoincremental)
- Fecha de préstamo
- Fecha de devolución esperada
- Fecha de devolución real (nullable)
- Estado (activo, devuelto, vencido)
- *Relación: Un préstamo involucra un libro y un usuario*
- *Relación: Un libro puede estar en varios préstamos (en diferentes momentos)*
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
---
## Clases C# para Biblioteca (Continuación)

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

---

## Clases C# para Biblioteca (Continuación)

```csharp
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
| ---------- | ------------- |
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

**Ejercicio 3: Sistema de Reservas**
Modelar un sistema de reservas de hotel con:
- `Habitacion`: número, tipo, precio, disponible
- `Cliente`: identificación, nombre, email, teléfono
- `Reserva`: fechas, estado, métodos para calcular total
- Relaciones: Un cliente hace muchas reservas, una reserva tiene una habitación

---

## Normalización de Bases de Datos

### Formas Normales - Evitar redundancia

```
┌─────────────────────────────────────────────────────────────┐
│                  ANORMALIZADO (PROBLEMAS)                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TABLA: Estudiantes                                          │
│  ┌──────┬──────────┬──────────┬──────────────┬────────────┐ │
│  │ ID   │ Nombre   │ Carrera  │ Facultad     │ Ciudad     │ │
│  ├──────┼──────────┼──────────┼──────────────┼────────────┤ │
│  │ 001  │ María    │ Ingeniería│ Ingeniería   │ Pereira    │ │
│  │ 002  │ Juan     │ Ingeniería│ Ingeniería   │ Pereira    │ │
│  │ 003  │ Ana      │ Medicina │ Salud       │ Pereira    │ │
│  │ 004  │ Pedro    │ Medicina │ Salud       │ Pereira    │ │
│  └──────┴──────────┴──────────┴──────────────┴────────────┘ │
│                                                             │
│  PROBLEMAS:                                                 │
│  • Redundancia: "Ingeniería" se repite                       │
│  • Anomalías: Si cambio "Ingeniería" por "Ingeniería de     │
│    Sistemas", debo actualizar TODOS los registros            │
│  • Eliminación: Si borro a Juan, pierdo info de Ingeniería  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│                    NORMALIZADO (SOLUCIÓN)                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TABLA: Estudiantes      TABLA: Carreras                    │
│  ┌──────┬──────────┬─────┐  ┌─────────┬──────────┬──────┐    │
│  │ ID   │ Nombre   │ FK │  │   ID    │ Nombre   │ Fac..│    │
│  ├──────┼──────────┼─────┤  ├─────────┼──────────┼──────┤    │
│  │ 001  │ María    │  1 │  │    1    │Ingeniería│Ingen.│    │
│  │ 002  │ Juan     │  1 │  │    2    │ Medicina │Salud │    │
│  │ 003  │ Ana      │  2 │  └─────────┴──────────┴──────┘    │
│  │ 004  │ Pedro    │  2 │                                     │
│  └──────┴──────────┴─────┘                                     │
│                                                             │
│  VENTAJAS:                                                  │
│  • No redundancia: Cada carrera aparece una vez             │
│  • Actualización: Cambio en un solo lugar                    │
│  • Integridad: No se pierde información                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Tercera Forma Normal (3FN)

Una tabla está en 3FN si:
1. Está en 2FN
2. **No** hay atributos que dependan de otros atributos que no sean la clave primaria

```sql
-- ❌ NO ESTÁ EN 3FN
CREATE TABLE Estudiantes (
    INT ID PRIMARY KEY,
    VARCHAR Nombre,
    VARCHAR Ciudad,
    VARCHAR Zona,           -- Depende funcionalmente de Ciudad
    VARCHAR CodAreaPostal   -- Depende funcionalmente de Ciudad
);

-- ✅ ESTÁ EN 3FN (separamos en tablas)
CREATE TABLE Estudiantes (
    INT ID PRIMARY KEY,
    VARCHAR Nombre,
    INT CiudadID,           -- FK a Ciudades
    FOREIGN KEY (CiudadID) REFERENCES Ciudades(ID)
);

CREATE TABLE Ciudades (
    INT ID PRIMARY KEY,
    VARCHAR Nombre,
    VARCHAR Zona,
    VARCHAR CodAreaPostal
);
```

---

## Ejercicio Práctico: Normalización

### De 1FN a 3FN - Sistema de Ventas

**Situación inicial (1FN):**
```sql
CREATE TABLE Ventas (
    INT ID PRIMARY KEY,
    DATE Fecha,
    VARCHAR ClienteNombre,
    VARCHAR ClienteDireccion,
    VARCHAR ClienteTelefono,
    VARCHAR Producto1,
    DECIMAL Precio1,
    INT Cantidad1,
    VARCHAR Producto2,
    DECIMAL Precio2,
    INT Cantidad2,
    DECIMAL Total
);
```

**Problemas:**
1. Producto2 puede ser NULL (espacio desperdiciado)
2. Solo puede comprar hasta 2 productos
3. Datos del cliente se repiten en cada venta

**Actividad:** Normalizar a 3NF

---

## Mapeo ORM: Conceptos Avanzados

### Lazy Loading vs Eager Loading

```csharp
// EAGER LOADING: Cargar todo de una vez
var estudiante = context.Estudiantes
    .Include(e => e.Carrera)      // Carga la carrera relacionada
    .Include(e => e.Inscripciones) // Carga las inscripciones
        .ThenInclude(i => i.Materia)
    .FirstOrDefault(e => e.Codigo == "2024001");

// LAZY LOADING: Cargar bajo demanda
var estudiante = context.Estudiantes.FirstOrDefault(e => e.Codigo == "2024001");
// La carrera NO se carga hasta que se accede:
string nombreCarrera = estudiante.Carrera.Nombre;  // Recién aquí se carga
```

---

## Patrones de Diseño en Modelado BD

### Repository Pattern y Unit of Work

```csharp
// REPOSITORY: Abstrae el acceso a datos
public interface IEstudianteRepository
{
    Estudiante ObtenerPorCodigo(string codigo);
    IEnumerable<Estudiante> ObtenerTodos();
    void Agregar(Estudiante estudiante);
    void Actualizar(Estudiante estudiante);
    void Eliminar(string codigo);
}

public class EstudianteRepository : IEstudianteRepository
{
    private readonly ApplicationDbContext _context;

    public EstudianteRepository(ApplicationDbContext context)
    {
        _context = context;
    }

    public Estudiante ObtenerPorCodigo(string codigo)
    {
        return _context.Estudiantes.FirstOrDefault(e => e.Codigo == codigo);
    }

    // ... otros métodos
}

// UNIT OF WORK: Agrupa múltiples repositorios
public interface IUnitOfWork : IDisposable
{
    IEstudianteRepository Estudiantes { get; }
    ICarreraRepository Carreras { get; }
    IMateriaRepository Materias { get; }
    int GuardarCambios();
}
```

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

