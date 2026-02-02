# Teoría - Sobrecarga, Sobreescritura y Modelado BD

**IF0100 - Lenguaje de Programación OO II**
*Unidad 1 - Clase 4*

---

## 1. Sobrecarga vs Sobreescritura

### Diferencias Fundamentales

| Aspecto | Sobrecarga (Overloading) | Sobreescritura (Overriding) |
|---------|-------------------------|----------------------------|
| **Ubicación** | Misma clase | Padre → Hija |
| **Nombre del método** | Igual | Igual |
| **Parámetros** | Deben ser diferentes | Deben ser idénticos |
| **Tipo de retorno** | Puede variar | Igual o covariante |
| **Palabras clave** | (ninguna específica) | `virtual`, `override`, `abstract` |
| **Resolución** | Estática (en compilación) | Dinámica (en ejecución) |
| **Polimorfismo** | Compile-time | Runtime |

### ¿Cuándo usar cada uno?

**Sobrecarga** (Overload):
- ✅ Quieres un método con diferentes formas de llamarlo
- ✅ Los parámetros son diferentes en tipo o cantidad
- ✅ Misma operación con diferentes entradas

**Sobreescritura** (Override):
- ✅ Quieres cambiar comportamiento de una clase hija
- ✅ Los parámetros son idénticos
- ✅ La operación se realiza diferente según el tipo

---

## 2. Sobrecarga de Métodos

### Reglas para Sobrecargar

Un método está sobrecargado cuando:

| ✅ Válido | ❌ No válido |
|-----------|-------------|
| Diferente **cantidad** de parámetros | Solo diferente **tipo de retorno** |
| Diferentes **tipos** de parámetros | Solo diferente **nombre de parámetros** |
| Diferente **orden** de parámetros | |

### Resolución de Sobrecarga

El compilador decide cuál método llamar en este orden:

```
1. Coincidencia EXACTA de tipos
2. Conversión IMPLÍCITA si no hay exacta
3. params como ÚLTIMA opción
4. AMBIGÜEDAD → Error de compilación
```

### Ejemplo Completo

```csharp
public class Calculadora
{
    // Sobrecarga 1: Dos enteros
    public int Sumar(int a, int b) => a + b;

    // Sobrecarga 2: Tres enteros
    public int Sumar(int a, int b, int c) => a + b + c;

    // Sobrecarga 3: Dos doubles
    public double Sumar(double a, double b) => a + b;

    // Sobrecarga 4: Array con params
    public int Sumar(params int[] nums) => nums.Sum();

    // Sobrecarga 5: Diferente orden
    public void Imprimir(string nombre, int edad) { }
    public void Imprimir(int edad, string nombre) { }
}
```

### Uso con Resolución

```csharp
Calculadora calc = new();

// El compilador decide según los argumentos
int r1 = calc.Sumar(5, 3);        // → Sumar(int, int)
int r2 = calc.Sumar(5, 3, 2);     // → Sumar(int, int, int)
double r3 = calc.Sumar(5.5, 3.2); // → Sumar(double, double)
int r4 = calc.Sumar(1, 2, 3, 4);  // → Sumar(params int[])
```

---

## 3. Sobrecarga de Constructores

### Patrón de Encadenamiento

```csharp
public class Estudiante
{
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    public string Carrera { get; set; }

    // CONSTRUCTOR PRINCIPAL: Tiene toda la lógica
    public Estudiante(string nombre, string codigo, int edad, string carrera)
    {
        Nombre = nombre;
        Codigo = codigo;
        Edad = edad;
        Carrera = carrera;
    }

    // Constructor 2: Llama al principal con valores default
    public Estudiante(string nombre, string codigo)
        : this(nombre, codigo, 18, "Sin carrera") { }

    // Constructor 3: Llama al anterior
    public Estudiante()
        : this("Sin nombre", "0000000") { }
}
```

### Flujo de Ejecución

```
new Estudiante()
    ↓
Llama a Estudiante(string, string)
    ↓
Llama a Estudiante(string, string, int, string)
    ↓
Asigna todas las propiedades
```

### Beneficios del Encadenamiento

| Beneficio | Descripción |
|-----------|-------------|
| **DRY** | Un solo constructor con lógica de inicialización |
| **Mantenimiento** | Cambios en un solo lugar |
| **Flexibilidad** | Múltiples formas de crear objetos |
| **Valores por defecto** | Sin repetir código |

---

## 4. Sobrecarga de Operadores

### ¿Qué es Sobrecargar Operadores?

Permite definir cómo se comportan los operadores (`+`, `-`, `*`, etc.) con tipos personalizados.

### Operadores Sobrecargables

| Tipo | Operadores |
|------|------------|
| **Aritméticos** | `+`, `-`, `*`, `/`, `%` |
| **Unarios** | `++`, `--`, `!`, `~` |
| **Comparación** | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| **Bit a bit** | `&`, `\|`, `^`, `<<`, `>>` |
| **Conversión** | `implicit`, `explicit` |

### ❌ NO se pueden sobrecargar

`&&`, `\|\|`, `??`, `?:`, `=`, `.`, `[]`, `()`, `->`

### Ejemplo: Fracción

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

    // Sobrecarga del operador +
    public static Fraccion operator +(Fraccion a, Fraccion b)
    {
        int num = a.Numerador * b.Denominador + b.Numerador * a.Denominador;
        int den = a.Denominador * b.Denominador;
        return new Fraccion(num, den);
    }

    public override string ToString() => $"{Numerador}/{Denominador}";
}

// Uso natural
Fraccion f1 = new(1, 2);   // 1/2
Fraccion f2 = new(1, 3);   // 1/3
Fraccion suma = f1 + f2;   // 5/6
```

### Reglas para Sobrecarga de Comparación

| # | Regla | Explicación |
|---|-------|-------------|
| 1 | **Sobrecarga en pares** | Si sobrecargas `==`, también `!=` |
| 2 | **Sobrescribir Equals()** | Para consistencia con `==` |
| 3 | **Sobrescribir GetHashCode()** | Para consistencia con Equals() |
| 4 | **Manejar null** | El operador debe manejar null correctamente |
| 5 | **Consistencia** | `a == b` debe igualar `a.Equals(b)` |

### Ejemplo Completo: Punto

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

    // Sobrescribir Equals para consistencia
    public override bool Equals(object obj)
        => obj is Punto p && this == p;

    // Sobrescribir GetHashCode
    public override int GetHashCode()
        => (X, Y).GetHashCode();
}
```

---

## 5. Modelamiento de Bases de Datos

### Mundo Real → Base de Datos

```
MUNDO REAL              BASE DE DATOS
────────────           ───────────────
Estudiante      →      Tabla ESTUDIANTE
   ↓ Nombre             → Columna NOMBRE
   ↓ Código             → Campo PK CODIGO
   ↓ Edad               → Tipo INT EDAD
   ↓ Carrera            → FK CARRERA_ID
```

### Componentes del Modelo ER

| Concepto POO | Concepto BD | Descripción |
|--------------|-------------|-------------|
| **Clase** | Tabla | Estructura de datos |
| **Propiedad** | Columna/Campo | Atributo de la entidad |
| **Objeto** | Registro/Fila | Instancia de datos |
| **Id único** | Clave Primaria (PK) | Identificador único |
| **Referencia** | Clave Foránea (FK) | Relación con otra tabla |

### Simbología ER

| Símbolo | Significado |
|---------|-------------|
| `PK` o `*` | Clave Primaria (Primary Key) |
| `FK` | Clave Foránea (Foreign Key) |
| Subrayado | Atributo obligatorio (NOT NULL) |
| `(1)` | Cardinalidad mínima 1 |
| `(N)` o `(0..N)` | Cardinalidad muchos |

---

## 6. Cardinalidad de Relaciones

### Tipos de Relaciones

#### 1:1 (Uno a Uno)

```
┌──────────┐           ┌──────────┐
│ Persona  │───────────│ Pasaporte│
└──────────┘    1   1  └──────────┘

Una persona tiene un pasaporte
Un pasaporte pertenece a una persona
```

**Mapeo en C#:**
```csharp
public class Persona
{
    public int Id { get; set; }
    public Pasaporte Pasaporte { get; set; }  // 1:1
}

public class Pasaporte
{
    public string Numero { get; set; }
    public int PersonaId { get; set; }  // FK
}
```

#### 1:N (Uno a Muchos)

```
┌──────────┐           ┌──────────┐
│ Carrera  │──────────<│Estudiante│
└──────────┘    1   N  └──────────┘

Una carrera tiene muchos estudiantes
Un estudiante pertenece a una carrera
```

**Mapeo en C#:**
```csharp
public class Carrera
{
    public int Id { get; set; }
    public List<Estudiante> Estudiantes { get; set; }  // 1:N
}

public class Estudiante
{
    public string Codigo { get; set; }
    public int CarreraId { get; set; }  // FK
    public Carrera Carrera { get; set; }
}
```

#### N:M (Muchos a Muchos)

```
┌──────────┐           ┌──────────┐
│Estudiante│>──────────<│ Materia  │
└──────────┘    N   M  └──────────┘

Un estudiante se inscribe en muchas materias
Una materia tiene muchos estudiantes
```

**Mapeo en C# (con tabla intermedia):**
```csharp
public class Estudiante
{
    public string Codigo { get; set; }
    public List<Inscripcion> Inscripciones { get; set; }
}

public class Materia
{
    public int Id { get; set; }
    public List<Inscripcion> Inscripciones { get; set; }
}

// Tabla intermedia
public class Inscripcion
{
    public int Id { get; set; }
    public string EstudianteCodigo { get; set; }  // FK
    public int MateriaId { get; set; }            // FK
    public DateTime Fecha { get; set; }
}
```

---

## 7. Mapeo Objeto-Relacional (ORM)

### Mapeo de Tipos C# ↔ SQL Server

| C# | SQL Server | Notas |
|----|------------|-------|
| `int` | `INT` | 32-bit |
| `long` | `BIGINT` | 64-bit |
| `string` | `VARCHAR(n)` | Longitud variable |
| `string` | `NVARCHAR(n)` | Unicode |
| `decimal` | `DECIMAL(p,s)` | Precisión, escala |
| `double` | `FLOAT` | |
| `bool` | `BIT` | 0 o 1 |
| `DateTime` | `DATETIME2` | Precisión alta |
| `DateTimeOffset` | `DATETIMEOFFSET` | Con zona horaria |
| `byte[]` | `VARBINARY(MAX)` | Datos binarios |
| `Guid` | `UNIQUEIDENTIFIER` | UUID |

### Ejemplo de Mapeo Completo

```csharp
// MODELO ORIENTADO A OBJETOS
public class Estudiante
{
    // PK: Clave Primaria
    public string Codigo { get; set; }

    // Columnas simples
    public string Nombre { get; set; }
    public int Edad { get; set; }
    public string Email { get; set; }

    // FK: Clave Foránea
    public int CarreraId { get; set; }

    // Navegación 1:N
    public Carrera Carrera { get; set; }

    // Navegación N:M (a través de tabla intermedia)
    public List<Inscripcion> Inscripciones { get; set; }
}
```

```sql
-- ESQUEMA RELACIONAL
CREATE TABLE Estudiantes (
    Codigo VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Edad INT,
    Email VARCHAR(100) UNIQUE,
    CarreraId INT FOREIGN KEY REFERENCES Carreras(Id)
);
```

---

## 8. Normalización (Tercera Forma Normal - 3FN)

### ¿Por qué Normalizar?

| ❌ Problema sin Normalizar | ✅ Solución con 3FN |
|--------------------------|-------------------|
| Redundancia de datos | Cada dato en un solo lugar |
| Anomalía de actualización | Un solo lugar para actualizar |
| Anomalía de inserción | No dependencias ocultas |
| Anomalía de eliminación | No se pierden datos por cascada |
| Riesgo de inconsistencia | Integridad referencial |

### Reglas de la 3FN

| Regla | Descripción |
|-------|-------------|
| **1FN** | Todos los atributos son atómicos (sin valores repetidos) |
| **2FN** | Todos los atributos no-clave dependen de la PK completa |
| **3FN** | No hay dependencias transitivas (A → B → C) |

### Ejemplo: Anormalizado vs Normalizado

```sql
-- ❌ ANORMALIZADO
CREATE TABLE Estudiantes (
    Codigo VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(100),
    CarreraNombre VARCHAR(100),      -- Redundante
    CarreraDuracion INT,             -- Redundante
    CarreraDecano VARCHAR(100)       -- Redundante
);

-- ✅ NORMALIZADO (3FN)
CREATE TABLE Carreras (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Duracion INT,
    Decano VARCHAR(100)
);

CREATE TABLE Estudiantes (
    Codigo VARCHAR(20) PRIMARY KEY,
    Nombre VARCHAR(100),
    CarreraId INT FOREIGN KEY REFERENCES Carreras(Id)
);
```

---

## 9. Errores Comunes

### Error 1: Sobrecarga solo por retorno

```csharp
// ❌ ERROR: No compila
public int Sumar(int a, int b) => a + b;
public double Sumar(int a, int b) => (double)(a + b);
// Solo difiere en tipo de retorno
```

**Solución:** Cambiar los parámetros.

### Error 2: Olvidar par de operadores

```csharp
// ❌ ERROR: Si sobrecargas ==, también !=
public static bool operator ==(Punto a, Punto b) { }
// Falta sobrecargar !=
```

**Solución:** Siempre sobrecargar en pares.

### Error 3: No sobrescribir Equals

```csharp
// ❌ ERROR: Inconsistencia
public static bool operator ==(Persona a, Persona b)
    => a.Id == b.Id;

// Falta override Equals y GetHashCode
```

**Solución:** Sobrescribir `Equals()` y `GetHashCode()`.

### Error 4: Relación N:M sin tabla intermedia

```csharp
// ❌ ERROR: No se puede mapear directamente
public class Estudiante
{
    public List<Materia> Materias { get; set; }  // ¿Cómo se guarda en BD?
}
```

**Solución:** Usar tabla intermedia `Inscripcion`.

---

## 10. Mejores Prácticas

### Sobrecarga de Métodos

1. **Misma operación, diferentes parámetros**
2. **Documentar cada sobrecarga**
3. **Evitar demasiadas sobrecargas** (máx. 5-6)
4. **Usar parámetros opcionales** cuando sea posible

### Sobrecarga de Operadores

1. **Solo cuando tenga sentido intuitivo**
2. **Sobrecargar en pares** (`==` con `!=`)
3. **Sobrescribir Equals y GetHashCode**
4. **Documentar el comportamiento**

### Modelado de BD

1. **Normalizar a 3FN**
2. **Usar PKs simples** (un solo campo)
3. **Documentar las relaciones**
4. **Usar índices en FKs**
5. **Validar integridad referencial**

---

**Última actualización:** 2026-02-01
