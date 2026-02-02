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

# Sobrecarga, Sobreescritura y Modelado BD

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 1 - Clase 4**

---

## Objetivos y Agenda

| 🎯 Objetivos | 📋 Agenda (90 min) |
|-------------|-------------------|
| 1. Diferenciar sobrecarga vs sobreescritura | 15' Sobrecarga vs Sobreescritura |
| 2. Implementar sobrecarga de métodos | 15' Sobrecarga de métodos |
| 3. Sobrecargar operadores en C# | 10' Sobrecarga de operadores |
| 4. Modelar BD con diagramas ER | 20' Modelamiento de BD |
| 5. Identificar relaciones 1-1, 1-N, N-M | 15' Mapeo Objeto-Relacional |
| | 15' Ejercicio práctico |

---

## 1. Sobrecarga vs Sobreescritura

### 📊 Tabla Comparativa

| Aspecto | Sobrecarga (Overloading) | Sobreescritura (Overriding) |
|---------|-------------------------|----------------------------|
| **Ubicación** | Misma clase | Padre → Hija |
| **Nombre** | Igual | Igual |
| **Parámetros** | Diferentes | Iguales |
| **Tipo retorno** | Puede variar | Igual o covariante |
| **Palabras clave** | (ninguna) | `virtual`, `override` |
| **Polimorfismo** | Estático (compilación) | Dinámico (ejecución) |

---

## Ejemplos de Código

| 📊 Sobrecarga | 📊 Sobreescritura |
|--------------|------------------|
| ```csharp<br>class Calculadora {<br>&nbsp;&nbsp;int Sumar(int a, int b) {<br>&nbsp;&nbsp;&nbsp;&nbsp;return a + b;<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;double Sumar(double a, double b) {<br>&nbsp;&nbsp;&nbsp;&nbsp;return a + b;<br>&nbsp;&nbsp;}<br>}<br>``` | ```csharp<br>class Animal {<br>&nbsp;&nbsp;virtual void Hablar() {}<br>}<br>class Perro : Animal {<br>&nbsp;&nbsp;override void Hablar() {}<br>}<br>``` |

---

## 2. Sobrecarga de Métodos

### 🎯 Reglas para Sobrecargar

| ✅ Válido | ❌ No válido |
|-----------|-------------|
| Diferente cantidad de parámetros | Solo diferente tipo de retorno |
| Diferentes tipos de parámetros | |
| Diferente orden de parámetros | |

### 💡 Ejemplo Práctico

```csharp
public class Calculadora
{
    // SOBRECARGA 1: Dos enteros
    public int Sumar(int a, int b) => a + b;

    // SOBRECARGA 2: Tres enteros
    public int Sumar(int a, int b, int c) => a + b + c;

    // SOBRECARGA 3: Dos doubles
    public double Sumar(double a, double b) => a + b;

    // SOBRECARGA 4: Array
    public int Sumar(params int[] nums) => nums.Sum();
}
```

### 📖 Término Clave: `params`

- **`params`**: Palabra clave que permite pasar un número variable de argumentos
- El compilador convierte los argumentos en un array automáticamente
- **Debe ser el último parámetro** del método

```csharp
// Estas llamadas son válidas:
calc.Sumar(1, 2);           // → nums = [1, 2]
calc.Sumar(1, 2, 3);        // → nums = [1, 2, 3]
calc.Sumar(1, 2, 3, 4, 5); // → nums = [1, 2, 3, 4, 5]
```

---

## Uso de Sobrecarga

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

| Orden | Regla |
|-------|-------|
| 1 | **Coincidencia exacta** de tipos |
| 2 | **Conversión implícita** si no hay exacta |
| 3 | **`params`** como última opción |
| 4 | **Ambigüedad** genera error de compilación |

---

## Sobrecarga de Constructores

### 🏗️ Constructores Sobrecargados

```csharp
public class Estudiante
{
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    public string Carrera { get; set; }

    // Constructor 1: Todos los params
    public Estudiante(string n, string c, int e, string ca)
    {
        Nombre = n; Codigo = c; Edad = e; Carrera = ca;
    }

    // Constructor 2: Parcial
    public Estudiante(string n, string c)
        : this(n, c, 18, "Sin carrera") { }

    // Constructor 3: Vacío
    public Estudiante()
        : this("Sin nombre", "0000000") { }
}
```

---

## La palabra clave `this`

### 🔄 Encadenamiento de Constructores

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

| Beneficio | Descripción |
|-----------|-------------|
| **DRY** | Un solo constructor con lógica |
| **Mantenimiento** | Cambios en un solo lugar |
| **Flexibilidad** | Múltiples formas de creación |
| **Valores por defecto** | Sin repetir código |

---

## 3. Sobrecarga de Operadores

### ➕ Operadores Aritméticos

```csharp
public class Fraccion
{
    public int Numerador { get; set; }
    public int Denominador { get; set; }

    public Fraccion(int n, int d)
    {
        Numerador = n;
        Denominador = d != 0 ? d : 1;
    }

    // Sobrecarga +
    public static Fraccion operator +(Fraccion a, Fraccion b)
    {
        int num = a.Numerador * b.Denominador + b.Numerador * a.Denominador;
        int den = a.Denominador * b.Denominador;
        return new Fraccion(num, den);
    }

    public override string ToString() => $"{Numerador}/{Denominador}";
}
```

### 📖 ¿Por qué `static`?

**Los operadores sobrecargados DEBEN ser `static` porque:**

- El operador se aplica a los TIPOS, no a instancias específicas
- `a + b` llama al método estático de la clase, no de ningún objeto
- Ambos operandos se pasan como parámetros explícitos

```csharp
// Cuando escribes: f1 + f2
// El compilador genera: Fraccion.operator +(f1, f2)
```

### 💻 Uso Natural

```csharp
Fraccion f1 = new(1, 2);   // 1/2
Fraccion f2 = new(1, 3);   // 1/3
Fraccion suma = f1 + f2;   // 5/6
Console.WriteLine($"{f1} + {f2} = {suma}");
```

---

## Operadores Sobrecargables

| Tipo | Operadores |
|------|------------|
| **Aritméticos** | `+ - * / %` |
| **Unarios** | `++ -- ! ~` |
| **Comparación** | `== != < > <= >=` |
| **Bit a bit** | `& \| ^ << >>` |
| **Conversión** | `implicit explicit` |

### ❌ NO se pueden sobrecargar

`&& || ?? ?: = . [] () ->`

---

## Sobrecarga de Operadores de Comparación

### 🔍 Implementando `==` y `!=`

```csharp
public class Punto
{
    public int X { get; set; }
    public int Y { get; set; }

    public Punto(int x, int y) { X = x; Y = y; }

    // Sobrecarga ==
    public static bool operator ==(Punto a, Punto b)
    {
        if (a is null) return b is null;
        return a.X == b.X && a.Y == b.Y;
    }

    // Sobrecarga != (siempre en pareja)
    public static bool operator !=(Punto a, Punto b) => !(a == b);

    public override bool Equals(object obj)
        => obj is Punto p && this == p;

    public override int GetHashCode()
        => (X, Y).GetHashCode();
}
```

---

## Reglas para Comparación

### 📋 Reglas Oro

| # | Regla |
|---|-------|
| 1 | Sobrecarga en **pares**: `==` con `!=`, `<` con `>` |
| 2 | Siempre sobrescribir `Equals()` con `==` |
| 3 | Siempre sobrescribir `GetHashCode()` con `Equals()` |
| 4 | Manejar `null` correctamente |
| 5 | `a == b` debe igualar `a.Equals(b)` |

### 📖 ¿Por qué Equals y GetHashCode?

- **`Equals()`**: Método heredado de `object` que compara por referencia (dirección de memoria). Sobrescribirlo permite comparar por **valor**.
- **`GetHashCode()`**: Retorna un número usado por colecciones hash-based (Dictionary, HashSet). Si dos objetos son "iguales", DEBEN tener el mismo hash.

⚠️ **Error común:** Sobrecargar `==` sin sobrescribir `Equals()` y `GetHashCode()` causa comportamiento inconsistente en diccionarios y hash sets.

---

## 4. Modelamiento de Bases de Datos

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

### 📊 Componentes del Modelo

| Concepto | BD | POO |
|----------|-----|-----|
| **Entidad** | Tabla | Clase |
| **Atributo** | Columna | Propiedad |
| **Registro** | Fila | Objeto |
| **PK** | Clave primaria | Id único |
| **FK** | Clave foránea | Referencia |

---

## Entidades y Atributos

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

| Símbolo | Significado |
|---------|-------------|
| `*` | Clave Primaria (PK) |
| `FK` | Clave Foránea (Foreign Key) |
| Subrayado | Atributo obligatorio |

---

## Mapeo C# ↔ SQL

| 🔄 C# Class | 📊 SQL Table |
|------------|------------|
| ```csharp<br>public class Estudiante {<br>&nbsp;&nbsp;public string Codigo { get; set; }<br>&nbsp;&nbsp;public string Nombre { get; set; }<br>&nbsp;&nbsp;public int Edad { get; set; }<br>&nbsp;&nbsp;public string Email { get; set; }<br>&nbsp;&nbsp;public int CarreraId { get; set; }<br>}<br>``` | ```sql<br>CREATE TABLE Estudiantes (<br>&nbsp;&nbsp;Codigo VARCHAR(20) PRIMARY KEY,<br>&nbsp;&nbsp;Nombre VARCHAR(100) NOT NULL,<br>&nbsp;&nbsp;Edad INT,<br>&nbsp;&nbsp;Email VARCHAR(100) UNIQUE,<br>&nbsp;&nbsp;CarreraId INT FOREIGN KEY<br>&nbsp;&nbsp;&nbsp;&nbsp;REFERENCES Carreras(Id)<br>);<br>``` |

---

## Cardinalidad de Relaciones

### 📊 Tipos de Relaciones

```
1:1 (UNO A UNO)
┌──────────┐           ┌──────────┐
│ Persona  │───────────│ Pasaporte│
└──────────┘    1   1  └──────────┘

1:N (UNO A MUCHOS)
┌──────────┐           ┌──────────┐
│ Carrera  │──────────<│Estudiante│
└──────────┘    1   N  └──────────┘

N:M (MUCHOS A MUCHOS)
┌──────────┐           ┌──────────┐
│Estudiante│>──────────<│ Materia  │
└──────────┘    N   M  └──────────┘
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
└─────────────┘              │ FK carrera_id│
                             └──────┬──────┘
                                   │ N
                                 ╱│╲
                            ┌────┴─────┐
                            │INSCRIPCION│
                            ├───────────┤
                            │ PK id     │
                            │ FK est_id │
                            │ FK mat_id │
                            └─────┬─────┘
                                  │ M
                            ┌─────┴─────┐
                            │  MATERIA   │
                            ├───────────┤
                            │ PK id     │
                            │ nombre    │
                            └───────────┘
```

---

## 5. Mapeo Objeto-Relacional (ORM)

### 🔄 C# → SQL Mapping

```csharp
// MODELO ORIENTADO A OBJETOS
public class Estudiante
{
    public string Codigo { get; set; }    // PK
    public string Nombre { get; set; }
    public string Email { get; set; }

    // Relación 1:N
    public Carrera Carrera { get; set; }  // FK en BD

    // Relación N:M
    public List<Inscripcion> Inscripciones { get; set; }
}
```

### 🎯 Mapeo de Tipos

| C# | SQL Server |
|----|------------|
| `int` | `INT` |
| `string` | `VARCHAR(n)` |
| `decimal` | `DECIMAL(p,s)` |
| `bool` | `BIT` |
| `DateTime` | `DATETIME2` |

---

## Normalización de Bases de Datos (3FN)

### ❌ ANORMALIZADO vs ✅ NORMALIZADO

| ❌ Problema | ✅ Solución |
|------------|------------|
| Redundancia de datos | Tablas separadas |
| Anomalía de actualización | Un solo lugar para actualizar |
| Riesgo de inconsistencia | Integridad referencial |

### 📋 Tercera Forma Normal (3FN)

| Regla | Descripción |
|-------|-------------|
| 1 | Está en 2FN |
| 2 | No hay dependencias transitivas |
| 3 | Todos los atributos dependen solo de la PK |

---

## 6. Ejercicio Práctico: Biblioteca

### 📚 Especificación

| Entidad | Atributos |
|---------|-----------|
| **Libro** | ISBN (PK), Título, Autor, Año, Cantidad |
| **Categoría** | ID (PK), Nombre |
| **Usuario** | Código (PK), Nombre, Email, Tipo |
| **Préstamo** | ID (PK), Fechas, Estado, FK Libro, FK Usuario |

### 📊 Relaciones

| Relación | Tipo |
|----------|------|
| Categoría → Libro | 1:N |
| Usuario → Préstamo | 1:N |
| Libro → Préstamo | 1:N |

---

## Diagrama ER: Biblioteca

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│CATEGORIA │1───N│  LIBRO   │1───N│ PRESTAMO │
├──────────┤     ├──────────┤     ├──────────┤
│PK id     │     │PK isbn   │     │PK id     │
│  nombre  │     │  titulo  │     │FK libro  │
└──────────┘     │  autor   │     │FK usuario│
                 │  anio    │     │  fechas  │
                 └──────────┘     │  estado  │
                                  └─────┬────┘
                                        │ N
                                  ┌────┴─────┐
                                  │ USUARIO  │
                                  ├──────────┤
                                  │PK codigo │
                                  │  nombre  │
                                  │  email   │
                                  │  tipo    │
                                  └──────────┘
```

---

## Solución: Clases C#

### 📊 Entidades Principales

```csharp
public class Categoria
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public List<Libro> Libros { get; set; }
}

public class Libro
{
    public string ISBN { get; set; }
    public string Titulo { get; set; }
    public string Autor { get; set; }
    public int Cantidad { get; set; }
    public int CategoriaId { get; set; }
    public Categoria Categoria { get; set; }
    public List<Prestamo> Prestamos { get; set; }
}

public class Usuario
{
    public string Codigo { get; set; }
    public string Nombre { get; set; }
    public string Email { get; set; }
    public List<Prestamo> Prestamos { get; set; }
}
```

---

## Patrones de Diseño en Modelado BD

### 🏗️ Repository Pattern

```csharp
public interface IEstudianteRepository
{
    Estudiante ObtenerPorCodigo(string codigo);
    IEnumerable<Estudiante> ObtenerTodos();
    void Agregar(Estudiante estudiante);
}

public class EstudianteRepository : IEstudianteRepository
{
    public Estudiante ObtenerPorCodigo(string codigo)
        => _context.Estudiantes.FirstOrDefault(e => e.Codigo == codigo);
}
```

### 📖 ¿Qué es el Repository Pattern?

**Repository Pattern**: Patrón de diseño que medía entre el dominio (clases) y la capa de datos (BD), actuando como una colección en memoria de objetos del dominio.

**Responsabilidades:**
- Abrir conexiones a BD
- Ejecutar consultas SQL
- Mapear resultados a objetos C#
- Manejar transacciones

**Beneficios:**
| Ventaja | Descripción |
|---------|-------------|
| **Desacopla** | Lógica de BD separada del dominio |
| **Testing** | Facilita unit tests con mocks |
| **Reutilización** | Consultas centralizadas |
| **Mantenimiento** | Cambios en BD afectan solo al repositorio |

---

## Resumen de la Clase

### 📚 Conceptos Clave

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

---

## 🚀 Próxima Clase: TDD - Pruebas Unitarias

### Temas Clase 5

| Tema | Descripción |
|------|-------------|
| **TDD** | Red-Green-Refactor cycle |
| **xUnit** | Framework de testing en C# |
| **Moq** | Mocking de dependencias |
| **FluentAssertions** | Aserciones legibles |

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

---

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
