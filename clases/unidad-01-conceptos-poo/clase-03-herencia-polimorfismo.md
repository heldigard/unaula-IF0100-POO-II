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

# Herencia y Polimorfismo

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 1 - Clase 3**

---

## Objetivos y Agenda

| 🎯 Objetivos | 📋 Agenda (90 min) |
|-------------|-------------------|
| 1. Aplicar herencia entre clases | 20' Herencia fundamentos |
| 2. Usar palabra `base` | 20' Polimorfismo virtual/override |
| 3. Polimorfismo: virtual/override | 20' Clases/métodos abstractos |
| 4. Clases/métodos abstractos | 10' Palabra `sealed` |
| 5. Principio Liskov | 10' Principio Liskov |
| | 10' Práctica: figuras |

---

## 1. Herencia: Conceptos Fundamentales

| 🎯 ¿Qué es Herencia? | 🔑 Terminología |
|---------------------|-----------------|
| Crear nuevas clases basadas en existentes | **Base** = Padre/Superclase |
| | **Derivada** = Hija/Subclase |
| | **`:`** = Operador herencia |
| | **`base`** = Ref. a clase padre |
| | **`protected`** = Clase + hijas |

### 📖 Términos Fundamentales

- **Superclase**: Clase padre de la que se hereda. Contiene miembros comunes.
- **Subclase**: Clase hija que hereda de la superclase. Extiende o especializa.
- **Sobrescribir (Override)**: Reemplazar un método heredado con una nueva implementación en la clase hija.

> 💡 **Analogía:** La superclase es como un plano base de una casa. La subclase es como modificar ese plano para agregar un garage o piscina - mantienes lo base pero agregas tus propias características.

### ✅ Beneficios

| Ventaja | Descripción |
|---------|-------------|
| 🔄 | Reutilización de código |
| 🏗️ | Jerarquías lógicas |
| 📈 | Extensibilidad |
| 🔧 | Mantenimiento centralizado |

> ⚠️ **Recomendación:** Máximo 3 niveles de profundidad

---

## Jerarquía y Sintaxis de Herencia

<div class="columns">
<div>

### 🌳 Jerarquía Visual

```
┌─────────────────────────────┐
│      PERSONA (Base)         │
│  - Nombre                   │
│  - Edad                     │
│  - Saludar()                │
└───────────┬─────────────────┘
            │
    ┌───────┴────────┐
    ▼                ▼
┌──────────┐   ┌──────────────┐
│Estudiante│   │Administrativo│
│- Carrera │   │- Departamento│
└──────────┘   └──────────────┘
```

### 📖 Herencia Transitiva

**¿Qué es?** Si A hereda de B, y B hereda de C, entonces A hereda TODO de C también.

```
Profesor → Empleado → Persona
    ↓         ↓          ↓
  Tiene    Tiene     Tiene
  todo de  todo de   todo de
Empleado + Persona  Persona
```

> 💡 **Profesor tiene**: Propiedades de Persona + Empleado + sus propias

</div>
<div>

### 💻 Sintaxis en C#

```csharp
// Clase Base
public class Persona
{
    public string Nombre { get; set; }
    public int Edad { get; set; }

    public void Saludar() =>
        Console.WriteLine($"Hola, soy {Nombre}");
}

// Clase Derivada
public class Estudiante : Persona
{
    public string Codigo { get; set; }
    public string Carrera { get; set; }

    public void Estudiar() =>
        Console.WriteLine($"{Nombre} estudia {Carrera}");
}
```

</div>
</div>

---

## Uso y Modificadores de Acceso

<div class="columns">
<div>

### 💻 Uso de Clases Derivadas

```csharp
Estudiante est = new Estudiante();

// Miembros HEREDADOS de Persona
est.Nombre = "María López";  // ✅
est.Edad = 20;                // ✅
est.Saludar();                 // ✅

// Miembros PROPIOS de Estudiante
est.Codigo = "2024001";       // ✅
est.Carrera = "Ingeniería";     // ✅
est.Estudiar();                // ✅
```

</div>
<div>

### 🔒 Modificadores de Acceso

```csharp
public class Persona
{
    public string Nombre { get; set; }     // ✅ Todos
    private string password;               // ❌ Solo clase
    protected double salario;              // ✅ Clase + hijas
    internal string direccion;             // ✅ Proyecto
}
```

| Modificador | Clase Base | Derivada |
|-------------|-----------|----------|
| **public** | ✅ | ✅ |
| **protected** | ✅ | ✅ |
| **internal** | ✅ | ✅* |
| **private** | ✅ | ❌ |

</div>
</div>

### ⚠️ Qué NO se hereda

❌ Constructores | ❌ Miembros `private`  
✅ Métodos públicos | ✅ Miembros `protected`

### 📌 Constructores y Herencia

**Importante:** Los constructores NO se heredan, pero la clase hija DEBE llamar a un constructor de la clase padre (explícita o implícitamente).

```csharp
// Implicitamente (sin parámetros)
public class Hija : Padre
{
    // El compilador agrega automáticamente : base()
}

// Explícitamente (con parámetros)
public class Hija : Padre
{
    public Hija(string nombre) : base(nombre)  // Llama constructor padre
    {
        // Código adicional de hija
    }
}
```

⚠️ **Si no se especifica `base(...)`:** Se llama al constructor sin parámetros del padre (`base()`). Si este no existe, hay error de compilación.

---

## Palabra clave `base`

<div class="columns">
<div>

### 🎯 ¿Para qué sirve?

Acceder a miembros de la clase padre:
- Llamar constructores base
- Extender métodos padre
- Reutilizar código

### ⚡ Orden de Ejecución

```
1. Constructor base (Persona)
2. Constructor derivada (Estudiante)
3. Resto del código
```

</div>
<div>

### 💻 Sintaxis Constructor

```csharp
public class Estudiante : Persona
{
    public string Codigo { get; set; }

    // Constructor llama a base
    public Estudiante(string n, int e, string c)
        : base(n, e)  // ← Primero padre
    {
        Codigo = c;   // Luego propio
    }
}
```

</div>
</div>

---

## Otros Usos de `base` y Jerarquías

<div class="columns">
<div>

### 🔄 Extender Método

```csharp
public override void Saludar()
{
    base.Saludar();  // Llama padre
    Console.WriteLine("Soy estudiante");
}
```

### ✅ Ventajas

- Reutiliza código padre
- Mantiene consistencia
- Evita duplicación

</div>
<div>

### 🌳 Jerarquías Profundas

```
NIVEL 1: Persona (abuelo)
├─ Nombre, Documento

NIVEL 2: Empleado (padre)
├─ CódigoEmpleado
├─ FechaContratación
└─ SalarioBase

NIVEL 3: Profesor (hijo)
├─ Especialidad
├─ Materias[]
└─ TítuloPostgrado
```

**💡 Herencia Transitiva:** `Profesor` → `Empleado` → `Persona`

</div>
</div>

---

## 2. Polimorfismo: Un Nombre, Múltiples Formas

<div class="columns">
<div>

### 🎭 Concepto

> Mismo mensaje, diferentes comportamientos según el objeto.

### 🔑 Palabras Clave

| Palabra | Propósito |
|---------|-----------|
| `virtual` | PUEDE sobrescribirse |
| `override` | Sobrescribe virtual/abstract |
| `abstract` | Obliga implementación |

### 💡 Analogía

```
Mensaje: "¡Muévete!"
  🐕 Perro → Corre
  🐈 Gato → Salta
  🐟 Pez → Nada
  🦅 Águila → Vuela
```

</div>
<div>

### 🎨 Polimorfismo Visual

```
┌─────────────────────────────────┐
│    MÉTODO: CalcularArea()       │
├─────────────────────────────────┤
│                                 │
│  ┌─────────┐  ┌──────────┐      │
│  │Círculo  │  │Rectángulo│      │
│  │  π×r²   │  │  b×h     │      │
│  └─────────┘  └──────────┘      │
│                                 │
│  Cada uno implementa distinto   │
└─────────────────────────────────┘
```

### ✅ Ventajas

- Código flexible
- Tratamiento uniforme
- Fácil extender

### 🔄 ¿Cómo funciona? (Binding Dinámico)

**Upcasting**: Convertir una referencia de hija a padre (implícito y seguro).

```csharp
Perro perro = new Perro();
Animal animal = perro;  // Upcasting implícito ✅
```

**Binding dinámico**: En tiempo de ejecución, .NET determina qué método llamar según el tipo REAL del objeto (no el tipo de la variable).

```csharp
Animal animal = new Perro();  // Variable dice Animal
animal.HacerSonido();          // PERO ejecuta Perro.HacerSonido()
// El compilador no sabe qué método llamar - el runtime lo decide
```

> ⚠️ **Error común:** Creer que el tipo de la variable determina el método. No - es el tipo del objeto (new Perro()) lo determina.

</div>
</div>

---

## Virtual y Override en Acción

<div class="columns">
<div>

### 📋 Clase Base

```csharp
public class Animal
{
    public string Nombre { get; set; }

    // VIRTUAL: puede sobrescribirse
    public virtual void HacerSonido()
    {
        Console.WriteLine("Sonido genérico");
    }

    public virtual void Moverse()
    {
        Console.WriteLine("Se mueve");
    }
}
```

### 🎭 Uso Polimórfico

```csharp
Animal a1 = new Perro() { Nombre = "Rex" };
Animal a2 = new Gato() { Nombre = "Michi" };

a1.HacerSonido();  // "¡Guau guau! 🐕"
a2.HacerSonido();  // "¡Miau miau! 🐈"
```

</div>
<div>

### 📋 Clases Derivadas

```csharp
public class Perro : Animal
{
    public override void HacerSonido()
    {
        Console.WriteLine("¡Guau guau! 🐕");
    }

    public override void Moverse()
    {
        Console.WriteLine("Corre en 4 patas 🐾");
    }
}

public class Gato : Animal
{
    public override void HacerSonido()
    {
        Console.WriteLine("¡Miau miau! 🐈");
    }
}
```

</div>
</div>

### 🔄 Colección Polimórfica

```csharp
List<Animal> animales = new()
{
    new Perro { Nombre = "Rex" },
    new Gato { Nombre = "Michi" },
    new Perro { Nombre = "Toby" },
    new Gato { Nombre = "Luna" }
};

foreach (Animal a in animales)
{
    Console.Write($"{a.Nombre}: ");
    a.HacerSonido();
}
// Rex: ¡Guau guau! 🐕
// Michi: ¡Miau miau! 🐈
```

---

## Llamando a `base.Metodo()`

<div class="columns">
<div>

### 🔄 Extender, No Reemplazar

```csharp
public class Empleado
{
    public virtual decimal CalcSalario()
    {
        return SalarioBase;
    }
}

public class Vendedor : Empleado
{
    public decimal Comision { get; set; }

    public override decimal CalcSalario()
    {
        // Llama base + agrega propio
        return base.CalcSalario() + Comision;
    }
}
```

</div>
<div>

### 💻 Uso Práctico

```csharp
Vendedor v = new Vendedor
{
    Nombre = "Carlos",
    SalarioBase = 2000,
    Comision = 1500
};

Console.WriteLine(v.CalcSalario());
// 3500 (base + comisión)
```

### 📊 Flujo

```
CalcSalario() [Vendedor]
    ↓
base.CalcSalario() = 2000
    ↓
+ Comision (1500)
    ↓
= 3500
```

</div>
</div>

---

## 3. Clases y Métodos Abstractos

<div class="columns">
<div>

### 📊 `virtual` vs `abstract`

| Característica | `virtual` | `abstract` |
|----------------|-----------|------------|
| Implementación | Tiene default | Sin código |
| Obligatoriedad | Hijas PUEDEN | Hijas DEBEN |
| Instanciación | ✅ Sí | ❌ NO |

### 🎯 Cuándo Usar Abstract

✅ Hay comportamiento común pero implementación diferente
✅ Quieres forzar diseño en hijas
✅ La clase base es solo un "contrato"

**Contrato**: En POO, una clase abstracta define un "contrato" - especifica QUÉ deben hacer las hijas (métodos abstractos) sin CÓMO hacerlo. Las hijas están obligadas a cumplir este contrato implementando los métodos abstractos.

</div>
<div>

### 💻 Clase Abstracta Ejemplo

```csharp
// ABSTRACTA: No instanciable
public abstract class Figura
{
    public string Nombre { get; set; }
    public string Color { get; set; }

    // ABSTRACTO: Hijas DEBEN implementar
    public abstract double CalcularArea();
    public abstract double CalcularPerimetro();

    // CONCRETO: Hijas heredan
    public void MostrarInfo()
    {
        Console.WriteLine($"Figura: {Nombre}");
        Console.WriteLine($"Área: {CalcularArea():F2}");
    }
}
```

</div>
</div>

---

## Implementando Clases Abstractas

<div class="columns">
<div>

### 📊 Círculo

```csharp
public class Circulo : Figura
{
    public double Radio { get; set; }

    public override double CalcularArea() =>
        Math.PI * Radio * Radio;

    public override double CalcularPerimetro() =>
        2 * Math.PI * Radio;
}
```

### 📖 Notas Matemáticas

- **`Math`**: Clase estática de .NET que proporciona constantes y métodos matemáticos
- **`Math.PI`**: Constante con el valor de π (pi) ≈ 3.14159265358979
- **`Math.E`**: Constante con el valor de e (número de Euler) ≈ 2.71828182845905

</div>
<div>

### 📐 Rectángulo

```csharp
public class Rectangulo : Figura
{
    public double Base { get; set; }
    public double Altura { get; set; }

    public override double CalcularArea() =>
        Base * Altura;

    public override double CalcularPerimetro() =>
        2 * (Base + Altura);
}
```

</div>
</div>

### 💻 Uso Polimórfico

```csharp
// ✅ Ref. base, objeto concreto
Figura f1 = new Circulo { Radio = 5 };
Figura f2 = new Rectangulo { Base = 4, Altura = 6 };

f1.MostrarInfo();  // Área: 78.54 cm²
f2.MostrarInfo();  // Área: 24.00 cm²

// ❌ Error: no se puede instanciar
// Figura f = new Figura();
```

---

## 4. Reglas y Palabra clave `sealed`

<div class="columns">
<div>

### 📋 Reglas de Abstractas

| Aspecto | Regla |
|---------|-------|
| Instanciar | ❌ NO |
| Heredar | ✅ Sí |
| Métodos abstractos | DEBEN implementarse |
| Métodos concretos | Se heredan |

### 🎯 Cuándo Usar Abstract

✅ Comportamiento común, implementación diferente  
✅ Quieres forzar diseño en hijas  
✅ Clase base como "contrato"

</div>
<div>

### 🔒 Palabra `sealed`

```csharp
// sealed: Nadie puede heredar
public sealed class SeguridadSocial
{
    public string Numero { get; set; }
    public decimal Saldo { get; set; }
}

// ❌ Error
// public class HackeoSS : SeguridadSocial { }
```

| ✅ Usar `sealed` | Ejemplo |
|-----------------|---------|
| No diseñada para heredar | `String` |
| Proteger lógica crítica | Seguridad |
| Finalizar cadena override | Impuestos |

</div>
</div>

---

## 5. Principio de Liskov (LSP)

<div class="columns">
<div>

### 📐 Principio

> **Clase hija debe sustituir a padre sin alterar comportamiento.**

### ✅ Buena Herencia

```
Estudiante → Persona ✅
Perro → Animal ✅
Círculo → Figura ✅
```

### ❌ Mala Herencia

```
Avión → Vehículo (?)  
# Tiene motor, pero vuela

Reloj → Círculo (?)   
# Forma ≠ concepto
```

</div>
<div>

### 💡 Ejemplo Problema

```csharp
class Rectangulo
{
    virtual void SetAncho(int w) { ... }
}

class Cuadrado : Rectangulo
{
    override void SetAncho(int w)
    {
        ancho = alto = w;  // ⚠️
    }
}

// Uso
Rectangulo r = new Cuadrado();
r.SetAncho(5);
r.SetAlto(10);
// Esperaba área 50, es 100
```

### 🎯 Pregunta Clave

¿`Cuadrado` ES UN `Rectángulo`?
- Matemáticamente: **SÍ**
- En POO: **NO** (cambia comportamiento)

> 💡 LSP = **comportamiento**, no taxonomía

</div>
</div>

---

## 6. Ejemplo Práctico: Sistema de Figuras

<div class="columns">
<div>

### 🎯 Objetivo

Sistema polimórfico de figuras geométricas.

### 📋 Clase Abstracta

```csharp
public abstract class Figura
{
    public string Nombre { get; set; }
    public string Color { get; set; }

    public abstract double CalcularArea();
    public abstract double CalcularPerimetro();

    public virtual void MostrarInfo()
    {
        Console.WriteLine($"📐 {Nombre} ({Color})");
        Console.WriteLine($"   Área: {CalcularArea():F2} cm²");
        Console.WriteLine($"   Per: {CalcularPerimetro():F2} cm");
    }
}
```

</div>
<div>

### 📊 Implementaciones

```csharp
public class Circulo : Figura
{
    public double Radio { get; set; }
    public override double CalcularArea() =>
        Math.PI * Radio * Radio;
    public override double CalcularPerimetro() =>
        2 * Math.PI * Radio;
}

public class Rectangulo : Figura
{
    public double Base { get; set; }
    public double Altura { get; set; }
    public override double CalcularArea() =>
        Base * Altura;
    public override double CalcularPerimetro() =>
        2 * (Base + Altura);
}
```

</div>
</div>

---

## Uso del Sistema de Figuras

```csharp
List<Figura> figuras = new()
{
    new Circulo { Nombre="C1", Color="Rojo", Radio=5 },
    new Rectangulo { Nombre="R1", Color="Azul", Base=4, Altura=6 }
};

double total = 0;
foreach (var f in figuras)
{
    f.MostrarInfo();
    total += f.CalcularArea();
}
Console.WriteLine($"\n📊 Total: {total:F2} cm²");
```

### 🎨 Salida Esperada

```
📐 C1 (Rojo)
   Área: 78.54 cm²
   Per: 31.42 cm

📐 R1 (Azul)
   Área: 24.00 cm²
   Per: 20.00 cm

📊 Total: 102.54 cm²
```

---

## Resumen de la Clase

### 📚 Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **Herencia** | `:` crea jerarquías |
| **base** | Llama miembros padre |
| **protected** | Clase + hijas |
| **virtual** | Puede sobrescribir |
| **override** | Sobrescribe virtual/abstract |
| **abstract** | Sin implementación |
| **sealed** | Impide herencia |
| **Polimorfismo** | Una interfaz, múltiples formas |

### 🎯 Habilidades Adquiridas

| Habilidad | Estado |
|-----------|--------|
| Aplicar herencia con `:` | ✅ |
| Usar `base` para llamar padre | ✅ |
| Implementar `virtual`/`override` | ✅ |
| Crear clases abstractas | ✅ |
| Aplicar principio LSP | ✅ |

---

## 📝 Ejercicios Prácticos

### 1. Banco (Abstracta)

- `CuentaBancaria` (abstracta)
  - `Numero`, `Saldo`
  - `CalcularInteres()` (abstract)
- `CuentaAhorros`: 3% interés mensual
- `CuentaCorriente`: 0% interés, permite sobregiro

### 2. Universidad (Abstracta)

- `EmpleadoUniversidad` (abstracta)
  - `Nombre`, `Documento`
  - `CalcularSalario()` (abstract)
- `Profesor`: Base + horas × valor/hora
- `Administrativo`: Salario fijo
- `Monitor`: Horas × valor/hora

### 3. 🌟 Figuras Extendido

```
Agregar al sistema de figuras:
- Triángulo (base×altura/2)
- Trapecio ((B+b)×h/2)
- Validar lados > 0
```

---

## 🎓 Próxima Clase: Sobrecarga y Modelado BD

### Temas Clase 4

| Tema | Descripción |
|------|-------------|
| ✅ Sobrecarga de métodos | Mismo nombre, diferentes parámetros |
| ✅ Sobrecarga de operadores | `+`, `-`, `==` personalizados |
| ✅ Sobrecarga vs Sobreescritura | Diferencias clave |
| ✅ Modelado de bases de datos | Entidades y relaciones |
| ✅ Relaciones: 1-1, 1-N, N-N | Cardinalidad |

### 📖 Términos Clave de Modelado BD

- **Cardinalidad**: Número máximo de objetos de una entidad que pueden relacionarse con objetos de otra entidad.
  - **1-1**: Un cliente tiene una dirección, una dirección pertenece a un cliente
  - **1-N**: Un cliente tiene muchas facturas, una factura pertenece a un cliente
  - **N-N**: Un estudiante se matricula en muchos cursos, un curso tiene muchos estudiantes

### 📖 Preparación

**Repasa herencia y polimorfismo**

**Piensa en ejemplos de sobrecarga:**
- `Sumar(int, int)` vs `Sumar(double, double)`
- `Imprimir(string)` vs `Imprimir(int)`
- `+` para números vs strings

> 💡 **Pregunta:** ¿Por qué C# permite sobrecargar operadores y Java no?

---

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
