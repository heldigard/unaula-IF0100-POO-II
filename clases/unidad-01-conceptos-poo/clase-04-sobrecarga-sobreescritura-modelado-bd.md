---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<style>
section { font-size: 16px; overflow: hidden; }
img { max-width: 70% !important; max-height: 45vh !important; object-fit: contain !important; height: auto !important; display: block !important; margin: 0 auto !important; }
section h1 { font-size: 1.8em; color: #1e40af; }
section h2 { font-size: 1.2em; color: #1e3a8a; margin-top: 0.5em; }
section h3 { font-size: 1.05em; color: #1e3a8a; }
section ul, section ol { font-size: 0.85em; margin-left: 1em; }
section li { margin-bottom: 0.25em; }
section pre { font-size: 0.55em; max-height: 50vh; overflow-y: auto; background: #1e293b; color: #e2e8f0; padding: 0.8em; border-radius: 6px; }
section code { font-size: 0.8em; background: #f1f5f9; padding: 0.1em 0.3em; border-radius: 3px; }
section p { margin: 0.4em 0; font-size: 0.9em; }
section table { width: 100%; font-size: 0.75em; border-collapse: collapse; margin: 0.5em auto; }
section th { background-color: #1e40af; color: white; padding: 0.3em 0.5em; text-align: left; font-size: 0.85em; border: 1px solid #ddd; }
section td { padding: 0.3em 0.5em; border: 1px solid #ddd; vertical-align: top; word-wrap: break-word; font-size: 0.8em; }
section tbody tr:nth-child(even) { background-color: #f8f9fa; }
section tbody tr:hover { background-color: #e9ecef; }

.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; }
.three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.8em; }
.highlight-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.8em 1em; border-radius: 8px; margin: 0.5em 0; }
.info-box { background: #f0f9ff; border-left: 3px solid #3b82f6; padding: 0.6em 0.8em; margin: 0.4em 0; }
.warning-box { background: #fefce8; border-left: 3px solid #eab308; padding: 0.6em 0.8em; margin: 0.4em 0; }
.success-box { background: #f0fdf4; border-left: 3px solid #22c55e; padding: 0.6em 0.8em; margin: 0.4em 0; }
</style>

---

# Sobrecarga, Sobreescritura y Modelado BD

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos y Agenda

<div class="two-col">

<div>

### 🎯 Objetivos

| # | Meta |
|---|------|
| 1 | Diferenciar sobrecarga vs sobreescritura |
| 2 | Implementar sobrecarga de métodos |
| 3 | Sobrecargar operadores en C# |
| 4 | Modelar BD con diagramas ER |
| 5 | Identificar relaciones 1-1, 1-N, N-M |

</div>

<div>

### 📋 Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 15' | Sobrecarga vs Sobreescritura |
| 15' | Sobrecarga de métodos |
| 10' | Sobrecarga de operadores |
| 20' | Modelamiento de BD |
| 15' | Mapeo Objeto-Relacional |
| 15' | Ejercicio práctico |

</div>

</div>

---

## 1. Sobrecarga vs Sobreescritura

<div class="two-col">

<div>

### 📊 Comparativa

```
┌────────────────────────────────┐
│  SOBRECARGA (OVERLOADING)      │
├────────────────────────────────┤
│ • Misma clase                  │
│ • Mismo nombre                 │
│ • Diferentes parámetros        │
│ • Polimorfismo ESTÁTICO        │
│   (compilación)                │
└────────────────────────────────┘
```

```csharp
class Calculadora {
  int Sumar(int a, int b) {
    return a + b;
  }
  double Sumar(double a, double b) {
    return a + b;
  }
}
```

</div>

<div>

### 📊 Comparativa

```
┌────────────────────────────────┐
│  SOBREESCRITURA (OVERRIDING)   │
├────────────────────────────────┤
│ • Clase padre → hija           │
│ • Mismo nombre y firma         │
│ • Misma firma                  │
│ • Polimorfismo DINÁMICO        │
│   (ejecución)                  │
└────────────────────────────────┘
```

```csharp
class Animal {
  virtual void Hablar() {}
}
class Perro : Animal {
  override void Hablar() {}
}
```

</div>

</div>

---

### Tabla Comparativa

| Aspecto | Sobrecarga | Sobreescritura |
|---------|------------|---------------|
| **Ubicación** | Misma clase | Padre → Hija |
| **Nombre** | Igual | Igual |
| **Parámetros** | Diferentes | Iguales |
| **Tipo retorno** | Puede variar | Igual o covariante |
| **Palabras clave** | (ninguna) | `virtual`, `override` |
| **Polimorfismo** | Estático | Dinámico |
| **Resolución** | Compilación | Ejecución |

---

## 2. Sobrecarga de Métodos

<div class="two-col">

<div>

### 🎯 Reglas para Sobrecargar

✅ **Válido:**
- Diferente cantidad de parámetros
- Diferentes tipos de parámetros
- Diferente orden de parámetros

❌ **No válido:**
- Solo diferente tipo de retorno

```csharp
// ERROR: Misma firma
public int Procesar(int x) {}
public double Procesar(int x) {}
// ❌ Error de compilación
```

</div>

<div>

### 💡 Ejemplo Práctico

```csharp
public class Calculadora {
  // SOBRECARGA 1: Dos enteros
  public int Sumar(int a, int b) =>
    a + b;

  // SOBRECARGA 2: Tres enteros
  public int Sumar(int a, int b, int c) =>
    a + b + c;

  // SOBRECARGA 3: Dos doubles
  public double Sumar(double a, double b) =>
    a + b;

  // SOBRECARGA 4: Array
  public int Sumar(params int[] nums) =>
    nums.Sum();
}
```

</div>

</div>

---

### Uso de Sobrecarga

```csharp
class Program {
  static void Main() {
    Calculadora calc = new();

    // El compilador decide cuál llamar
    int r1 = calc.Sumar(5, 3);        // → Sumar(int, int)
    int r2 = calc.Sumar(5, 3, 2);     // → Sumar(int, int, int)
    double r3 = calc.Sumar(5.5, 3.2); // → Sumar(double, double)
    int r4 = calc.Sumar(1, 2, 3, 4);  // → Sumar(params int[])

    Console.WriteLine($"Resultados: {r1}, {r2}, {r3}, {r4}");
    // Salida: 8, 10, 8.7, 15
  }
}
```

### 📌 Reglas de Resolución

1. **Coincidencia exacta** de tipos
2. **Conversión implícita** si no hay exacta
3. **`params`** como última opción
4. **Ambigüedad** genera error de compilación

---

## Sobrecarga de Constructores

<div class="two-col">

<div>

### 🏗️ Constructores Sobrecargados

```csharp
public class Estudiante {
  public string Nombre { get; set; }
  public string Codigo { get; set; }
  public int Edad { get; set; }
  public string Carrera { get; set; }

  // Constructor 1: Todos los params
  public Estudiante(string n, string c, int e, string ca) {
    Nombre = n;
    Codigo = c;
    Edad = e;
    Carrera = ca;
  }

  // Constructor 2: Parcial
  public Estudiante(string n, string c)
    : this(n, c, 18, "Sin carrera") {
  }

  // Constructor 3: Vacío
  public Estudiante()
    : this("Sin nombre", "0000000") {
  }
}
```

</div>

<div>

### 🔄 La palabra clave `this`

```
┌─────────────────────────────────┐
│  ENCADENAMIENTO DE CONSTRUCTORES│
├─────────────────────────────────┤
│                                 │
│  Estudiante()                   │
│      └─→ : this("...", "...")   │
│           └─→ : this(..., 18, ..)│
│                └─→ Asigna props │
│                                 │
│  Estudiante e = new();          │
│  → Llama constructor vacío      │
│  → Este llama al de 2 params    │
│  → Este llama al principal      │
│                                 │
└─────────────────────────────────┘
```

### ✅ Beneficios

- **DRY:** Un solo constructor con lógica
- **Mantenimiento:** Cambios en un solo lugar
- **Flexibilidad:** Múltiples formas de creación
- **Valores por defecto:** Sin repetir código

</div>

</div>

---

## 3. Sobrecarga de Operadores

<div class="two-col">

<div>

### ➕ Operadores Aritméticos

```csharp
public class Fraccion {
  public int Numerador { get; set; }
  public int Denominador { get; set; }

  public Fraccion(int n, int d) {
    Numerador = n;
    Denominador = d != 0 ? d : 1;
  }

  // Sobrecarga +
  public static Fraccion operator +(
    Fraccion a, Fraccion b) {
    int num = a.Numerador * b.Denominador
            + b.Numerador * a.Denominador;
    int den = a.Denominador * b.Denominador;
    return new(num, den);
  }

  // Sobrecarga -
  public static Fraccion operator -(
    Fraccion a, Fraccion b) {
    int num = a.Numerador * b.Denominador
            - b.Numerador * a.Denominador;
    int den = a.Denominador * b.Denominador;
    return new(num, den);
  }

  public override string ToString()
    => $"{Numerador}/{Denominador}";
}
```

</div>

<div>

### 💻 Uso Natural

```csharp
class Program {
  static void Main() {
    Fraccion f1 = new(1, 2);   // 1/2
    Fraccion f2 = new(1, 3);   // 1/3

    Fraccion suma = f1 + f2;   // 5/6
    Fraccion resta = f1 - f2;  // 1/6

    Console.WriteLine($"{f1} + {f2} = {suma}");
    Console.WriteLine($"{f1} - {f2} = {resta}");
  }
}
```

### ✅ Operadores Sobrecargables

| Tipo | Operadores |
|------|------------|
| **Aritméticos** | `+ - * / %` |
| **Unarios** | `++ -- ! ~` |
| **Comparación** | `== != < > <= >=` |
| **Bit a bit** | `& | ^ << >>` |
| **Conversión** | `implicit explicit` |

### ❌ NO se pueden sobrecargar

`&& || ?? ?: = . [] () ->`

</div>

</div>

---

## Sobrecarga de Operadores de Comparación

<div class="two-col">

<div>

### 🔍 Implementando `==` y `!=`

```csharp
public class Punto {
  public int X { get; set; }
  public int Y { get; set; }

  public Punto(int x, int y) {
    X = x;
    Y = y;
  }

  // Sobrecarga ==
  public static bool operator ==(
    Punto a, Punto b) {
    if (a is null)
      return b is null;
    return a.X == b.X && a.Y == b.Y;
  }

  // Sobrecarga != (siempre en pareja)
  public static bool operator !=(
    Punto a, Punto b) => !(a == b);

  public override bool Equals(object obj)
    => obj is Punto p && this == p;

  public override int GetHashCode()
    => (X, Y).GetHashCode();
}
```

</div>

<div>

### 📋 Reglas para Comparación

1. **Sobrecarga en pares:**
   - `==` con `!=`
   - `<` con `>`
   - `<=` con `>=`

2. **Siempre sobrescribir:**
   - `Equals()` junto con `==`
   - `GetHashCode()` con `Equals()`

3. **Manejo de `null`:**
   ```csharp
   if (ReferenceEquals(a, null))
     return ReferenceEquals(b, null);
   ```

4. **Consistencia:**
   - `a == b` debe igualar `a.Equals(b)`
   - `GetHashCode()` debe ser consistente

```csharp
// Uso
Punto p1 = new(1, 2);
Punto p2 = new(1, 2);
Console.WriteLine(p1 == p2);  // True
Console.WriteLine(p1 != p2);  // False
```

</div>

</div>

---

## 4. Modelamiento de Bases de Datos

<div class="two-col">

<div>

### 🔄 Mundo Real → BD

```
┌──────────────────────────┐
│  MUNDO REAL → BD         │
├──────────────────────────┤
│                          │
│ MUNDO REAL    BD         │
│                          │
│ Estudiante  → Tabla      │
│   ↓          ↓           │
│ Nombre    → Columna      │
│ Código    → Campo PK     │
│ Edad      → Tipo INT     │
│ Carrera   → FK           │
│                          │
└──────────────────────────┘
```

</div>

<div>

### 📊 Componentes del Modelo

| Concepto | BD | POO |
|----------|-----|-----|
| **Entidad** | Tabla | Clase |
| **Atributo** | Columna | Propiedad |
| **Registro** | Fila | Objeto |
| **PK** | Clave primaria | Id único |
| **FK** | Clave foránea | Referencia |

### 🎯 Transformación

**Entidad → Tabla**
- Estudiante → `Estudiantes`

**Atributos → Columnas**
- nombre → `VARCHAR(100)`
- edad → `INT`

**PK (Primary Key)**
- `id INT PRIMARY KEY`
- Identificador único

**FK (Foreign Key)**
- `carrera_id INT FK`
- Relación entre tablas

</div>

</div>

---

## Entidades y Atributos

<div class="two-col">

<div>

### 📋 Diagrama ER: Estudiante

```
┌─────────────────────────┐
│     ESTUDIANTE          │
├─────────────────────────┤
│ * PK codigo             │
│   nombre                │
│   edad                  │
│   email                 │
│   fecha_nacimiento      │
│ FK carrera_id           │
└─────────────────────────┘
```

### 📝 Simbología ER

- `*` = Clave Primaria (PK)
- `FK` = Clave Foránea (Foreign Key)
- Subrayado = Atributo obligatorio

</div>

<div>

### 🔄 Mapeo C# ↔ SQL

```csharp
// C# Class
public class Estudiante {
  public string Codigo { get; set; }   // PK
  public string Nombre { get; set; }
  public int Edad { get; set; }
  public string Email { get; set; }
  public int CarreraId { get; set; }   // FK
}
```

```sql
-- SQL Table
CREATE TABLE Estudiantes (
  Codigo VARCHAR(20) PRIMARY KEY,
  Nombre VARCHAR(100) NOT NULL,
  Edad INT,
  Email VARCHAR(100) UNIQUE,
  CarreraId INT FOREIGN KEY
    REFERENCES Carreras(Id)
);
```

### 💡 Tipos de Atributos

**Por cardinalidad:**
- Simple: nombre (único valor)
- Compuesto: dirección (calle, ciudad)
- Multivaluado: teléfonos (varios)

**Por nulidad:**
- Obligatorio: `NOT NULL`
- Opcional: `NULL`

**Derivado:**
- edad (se calcula de fecha_nacimiento)

</div>

</div>

---

## Cardinalidad de Relaciones

```
┌─────────────────────────────────────────────────────────────────┐
│                    TIPOS DE RELACIONES                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1:1 (UNO A UNO)                                                │
│  ┌──────────┐           ┌──────────┐                           │
│  │ Persona  │───────────│ Pasaporte│                           │
│  └──────────┘    1   1  └──────────┘                           │
│  Una persona tiene un solo pasaporte                           │
│                                                                 │
│  1:N (UNO A MUCHOS)                                             │
│  ┌──────────┐           ┌──────────┐                           │
│  │ Carrera  │──────────<│Estudiante│                           │
│  └──────────┘    1   N  └──────────┘                           │
│  Una carrera tiene muchos estudiantes                          │
│                                                                 │
│  N:M (MUCHOS A MUCHOS)                                          │
│  ┌──────────┐           ┌──────────┐                           │
│  │Estudiante│>──────────<│ Materia  │                           │
│  └──────────┘    N   M  └──────────┘                           │
│  Un estudiante cursa muchas materias                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Ejemplo: Sistema Universitario

### Diagrama ER Completo

```
┌─────────────┐              ┌─────────────┐
│   CARRERA   │              │  ESTUDIANTE │
├─────────────┤              ├─────────────┤
│ PK id       │1───────────N│ PK codigo   │
│   nombre    │              │   nombre    │
│   duracion  │              │   email     │
│   facultad  │              │ FK carrera_id│
└─────────────┘              └──────┬──────┘
                                    │ N
                                    │
                                  ╱│╲
                                 ╱ │ ╲
                            ┌────┴─────┐
                            │INSCRIPCION│
                            ├───────────┤
                            │ PK id     │
                            │ FK est_id │
                            │ FK mat_id │
                            │ semestre  │
                            │ nota      │
                            └─────┬─────┘
                                  │ M
                            ┌─────┴─────┐
                            │  MATERIA   │
                            ├───────────┤
                            │ PK id     │
                            │ nombre    │
                            │ creditos  │
                            └───────────┘
```

---

## 5. Mapeo Objeto-Relacional (ORM)

<div class="two-col">

<div>

### 🔄 C# → SQL Mapping

```csharp
// MODELO ORIENTADO A OBJETOS
public class Estudiante {
  public string Codigo { get; set; }    // PK
  public string Nombre { get; set; }
  public string Email { get; set; }

  // Relación 1:N
  public Carrera Carrera { get; set; }  // FK en BD

  // Relación 1:N
  public List<Inscripcion>
    Inscripciones { get; set; }
}

public class Carrera {
  public int Id { get; set; }           // PK
  public string Nombre { get; set; }

  // Relación 1:N inversa
  public List<Estudiante>
    Estudiantes { get; set; }
}
```

</div>

<div>

### 📊 Tablas SQL Equivalentes

```sql
-- MODELO RELACIONAL
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
  CarreraId INT,
  FOREIGN KEY (CarreraId)
    REFERENCES Carreras(Id)
);

CREATE TABLE Inscripciones (
  Id INT PRIMARY KEY IDENTITY,
  EstudianteCodigo VARCHAR(20),
  MateriaId INT,
  Semestre VARCHAR(10),
  NotaFinal DECIMAL(3,2),
  FOREIGN KEY (EstudianteCodigo)
    REFERENCES Estudiantes(Codigo)
);
```

</div>

</div>

---

### Conversión de Tipos: C# ↔ SQL Server

| C# | SQL Server | Descripción |
|----|------------|-------------|
| `int` | `INT` | Entero 32-bit |
| `long` | `BIGINT` | Entero 64-bit |
| `string` | `VARCHAR(n)` / `NVARCHAR(n)` | Texto |
| `decimal` | `DECIMAL(p,s)` | Decimal preciso |
| `double` | `FLOAT` | Punto flotante |
| `bool` | `BIT` | Booleano (0/1) |
| `DateTime` | `DATETIME2` | Fecha y hora |
| `DateTimeOffset` | `DATETIMEOFFSET` | Con zona horaria |
| `byte[]` | `VARBINARY(MAX)` | Datos binarios |
| `Guid` | `UNIQUEIDENTIFIER` | GUID único |
| `char` | `CHAR(1)` | Carácter simple |
| `TimeSpan` | `TIME` | Duración |

---

### Normalización de Bases de Datos (3FN)

<div class="two-col">

<div>

### ❌ ANORMALIZADO (Problemas)

```
TABLA: Estudiantes
┌────┬────────┬──────────┬───────────┬────────┐
│ ID │ Nombre │ Carrera  │ Facultad  │ Ciudad │
├────┼────────┼──────────┼───────────┼────────┤
│ 001│ María  │Ingeniería│ Ingeniería│Pereira │
│ 002│ Juan   │Ingeniería│ Ingeniería│Pereira │
│ 003│ Ana    │ Medicina │ Salud     │Pereira │
└────┴────────┴──────────┴───────────┴────────┘

PROBLEMAS:
• Redundancia: "Ingeniería" se repite
• Anomalía de actualización
• Riesgo de inconsistencia
```

</div>

<div>

### ✅ NORMALIZADO (Solución)

```
Estudiantes        Carreras
┌────┬────────┬─────┐  ┌────┬──────────┬──────┐
│ ID │ Nombre │ FK │  │ ID │ Nombre   │ Fac..│
├────┼────────┼─────┤  ├────┼──────────┼──────┤
│001 │ María  │  1  │  │ 1  │Ingeniería│Ingen.│
│002 │ Juan   │  1  │  │ 2  │ Medicina │Salud │
│003 │ Ana    │  2  │  └────┴──────────┴──────┘
└────┴────────┴─────┘

VENTAJAS:
• Sin redundancia
• Actualización en un lugar
• Integridad referencial
```

### 📋 Tercera Forma Normal (3FN)

1. **Está en 2FN**
2. **No hay dependencias transitivas**
3. **Todos los atributos dependen solo de la PK**

```sql
-- ✅ 3FN: Cada tabla tiene un propósito
CREATE TABLE Estudiantes (
  ID INT PRIMARY KEY,
  Nombre VARCHAR(100),
  CarreraID INT FOREIGN KEY
);
```

</div>

</div>

---

## 6. Ejercicio Práctico: Biblioteca

<div class="two-col">

<div>

### 📚 Especificación

**Entidad: Libro**
- ISBN (PK, único)
- Título, Autor, Año
- Cantidad disponible

**Entidad: Categoría**
- ID (PK, autoincremental)
- Nombre
- 1:Categoría → N:Libros

**Entidad: Usuario**
- Código (PK)
- Nombre, Email, Tipo
- 1:Usuario → N:Préstamos

**Entidad: Préstamo**
- ID (PK, autoincremental)
- Fechas: préstamo, devolución
- Estado (activo, devuelto, vencido)
- N:Libros → 1:Préstamo
- N:Usuarios → 1:Préstamo

</div>

<div>

### 📊 Diagrama ER

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│CATEGORIA │1───N│  LIBRO   │1───N│ PRESTAMO │
├──────────┤     ├──────────┤     ├──────────┤
│PK id     │     │PK isbn   │     │PK id     │
│  nombre  │     │  titulo  │     │FK libro  │
└──────────┘     │  autor   │     │FK usuario│
                 │  anio    │     │  fechas  │
                 │  cantidad│     │  estado  │
                 └──────────┘     └─────┬────┘
                                       │ N
                                       │
                                  ┌────┴─────┐
                                  │ USUARIO  │
                                  ├──────────┤
                                  │PK codigo │
                                  │  nombre  │
                                  │  email   │
                                  │  tipo    │
                                  └──────────┘
```

</div>

</div>

---

### Solución: Clases C#

<div class="two-col">

<div>

```csharp
public class Categoria {
  public int Id { get; set; }
  public string Nombre { get; set; }
  public List<Libro> Libros { get; set; }
}

public class Libro {
  public string ISBN { get; set; }
  public string Titulo { get; set; }
  public string Autor { get; set; }
  public int Anio { get; set; }
  public int Cantidad { get; set; }

  public int CategoriaId { get; set; }
  public Categoria Categoria { get; set; }
  public List<Prestamo> Prestamos { get; set; }
}

public class Usuario {
  public string Codigo { get; set; }
  public string Nombre { get; set; }
  public string Email { get; set; }
  public string Tipo { get; set; }

  public List<Prestamo> Prestamos { get; set; }
}
```

</div>

<div>

```csharp
public class Prestamo {
  public int Id { get; set; }
  public DateTime FechaPrestamo { get; set; }
  public DateTime FechaDevolucionEsperada { get; set; }
  public DateTime? FechaDevolucionReal { get; set; }
  public string Estado { get; set; }

  public string LibroISBN { get; set; }
  public Libro Libro { get; set; }

  public string UsuarioCodigo { get; set; }
  public Usuario Usuario { get; set; }
}
```

### 💡 Patrones ORM

**Lazy Loading:**
```csharp
var est = ctx.Estudiantes.First(id);
string carrera = est.Carrera.Nombre; // Se carga aquí
```

**Eager Loading:**
```csharp
var est = ctx.Estudiantes
  .Include(e => e.Carrera)
  .Include(e => e.Prestamos)
    .ThenInclude(p => p.Libro)
  .First(id);
```

</div>

</div>

---

### Patrones de Diseño en Modelado BD

<div class="info-box">

**🏗️ Repository Pattern**

```csharp
public interface IEstudianteRepository {
  Estudiante ObtenerPorCodigo(string codigo);
  IEnumerable<Estudiante> ObtenerTodos();
  void Agregar(Estudiante estudiante);
  void Actualizar(Estudiante estudiante);
  void Eliminar(string codigo);
}

public class EstudianteRepository
  : IEstudianteRepository {
  private readonly DbContext _context;

  public Estudiante ObtenerPorCodigo(string codigo)
    => _context.Estudiantes
      .FirstOrDefault(e => e.Codigo == codigo);
}
```

</div>

<div class="info-box">

**📦 Unit of Work Pattern**

```csharp
public interface IUnitOfWork : IDisposable {
  IEstudianteRepository Estudiantes { get; }
  ICarreraRepository Carreras { get; }
  IMateriaRepository Materias { get; }
  int GuardarCambios();
}

public class UnitOfWork : IUnitOfWork {
  private readonly DbContext _context;

  public IEstudianteRepository Estudiantes { get; }
  public ICarreraRepository Carreras { get; }

  public int GuardarCambios()
    => _context.SaveChanges();
}
```

</div>

---

## Resumen y Próxima Clase

<div class="two-col">

<div>

### 📚 Resumen

| Concepto | Clave |
|----------|-------|
| **Sobrecarga** | Mismo nombre, diferentes params |
| **Sobreescritura** | Misma firma, reimplementación |
| **`this`** | Llama a otro constructor |
| **`operator`** | Sobrecarga de operadores |
| **PK/FK** | Claves primarias/foráneas |
| **1:N, N:M** | Cardinalidad de relaciones |
| **3FN** | Tercera Forma Normal |

### ✏️ Ejercicios

1. **Clase Complejo:** Sobrecargar `+`, `-`, `*`, `/`
2. **Tienda Online:** Modelar ER (Clientes, Productos, Órdenes)
3. **Sistema Reservas:** Habitaciones, Clientes, Reservas

</div>

<div>

### 🚀 Unidad 2: Técnicas de Desarrollo

- **TDD:** Red-Green-Refactor, xUnit
- **BDD:** Gherkin, Given-When-Then
- **DDD:** Entidades, Value Objects, Aggregates

### 📦 Instalación

```bash
dotnet new xunit
dotnet add package Moq
dotnet add package FluentAssertions
```

### 📝 Evaluación 1 (Semana 4)

- **Quiz teórico:** 30 min
- **Práctico en VS:** 90 min
- **Tema:** POO completo (Unidad 1)

</div>

</div>

---

# ¡Gracias!

## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
