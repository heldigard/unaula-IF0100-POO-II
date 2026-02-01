---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<style>
section {
  font-size: 16px;
  overflow: hidden;
}
img {
  max-width: 60% !important;
  max-height: 40vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
}
section h1 { font-size: 1.8em; color: #1e40af; }
section h2 { font-size: 1.2em; color: #1e3a8a; }
section h3 { font-size: 1em; color: #3b82f6; }
section ul, section ol { font-size: 0.8em; margin-left: 0.5em; }
section li { margin-bottom: 0.2em; }
section pre { font-size: 0.55em; max-height: 50vh; overflow-y: auto; }
section code { font-size: 0.7em; }
section p { margin: 0.3em 0; }
section table { width: 100%; font-size: 0.75em; border-collapse: collapse; margin: 0.2em auto; }
section th { background-color: #1e40af; color: white; padding: 0.25em 0.4em; text-align: left; font-size: 0.75em; border: 1px solid #ddd; }
section td { padding: 0.25em 0.4em; border: 1px solid #ddd; vertical-align: top; word-wrap: break-word; font-size: 0.7em; }
section tbody tr:nth-child(even) { background-color: #f8f9fa; }
section tbody tr:hover { background-color: #e9ecef; }
.highlight-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.8em; border-radius: 6px; margin: 0.3em 0; font-size: 0.85em; }
.info-box { background: #f0f9ff; border-left: 3px solid #3b82f6; padding: 0.6em; margin: 0.3em 0; font-size: 0.85em; }
.warning-box { background: #fffbeb; border-left: 3px solid #f59e0b; padding: 0.6em; margin: 0.3em 0; font-size: 0.85em; }
.success-box { background: #f0fdf4; border-left: 3px solid #22c55e; padding: 0.6em; margin: 0.3em 0; font-size: 0.85em; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 1em; }
.three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.8em; }
.col-card { background: white; border: 1px solid #e5e7eb; border-radius: 6px; padding: 0.6em; font-size: 0.85em; }
.compact-list { display: grid; grid-template-columns: 1fr 1fr; gap: 0.5em; font-size: 0.85em; }
</style>

---

# Herencia y Polimorfismo

<div class="info-box" style="text-align: center;">

**IF0100 - Lenguaje de Programación OO II**

*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 1 - Clase 3*

</div>

---

## Objetivos y Agenda

<div class="two-col">

<div>

### 🎯 Objetivos

| # | Meta |
|---|------|
| 1 | Aplicar herencia entre clases |
| 2 | Usar palabra `base` |
| 3 | Polimorfismo: virtual/override |
| 4 | Clases/métodos abstractos |
| 5 | Principio Liskov |

</div>

<div>

### 📋 Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 20' | Herencia fundamentos |
| 20' | Polimorfismo virtual/override |
| 20' | Clases/métodos abstractos |
| 10' | Palabra `sealed` |
| 10' | Principio Liskov |
| 10' | Práctica: figuras |

</div>

</div>

---

## 1. Herencia: Conceptos Fundamentales

<div class="two-col">

<div>

### 🎯 ¿Qué es Herencia?

Crear nuevas clases basadas en existentes.

### 🔑 Terminología

| Término | Significado |
|---------|-------------|
| **Base** | Padre/Superclass |
| **Derivada** | Hija/Subclass |
| **`:`** | Operador herencia |
| **`base`** | Ref. a clase padre |
| **`protected`** | Clase + hijas |

### ✅ Beneficios

- Reutilización código
- Jerarquías lógicas
- Extensibilidad
- Mantenimiento centralizado

<div class="info-box">

**⚠️ Recomendación:** Máximo 3 niveles de profundidad

</div>

</div>

<div>

### 📊 Jerarquía Visual

```
┌─────────────────────────────────┐
│        PERSONA (Base)           │
│  - Nombre                        │
│  - Edad                          │
│  - Saludar()                     │
└────────────┬────────────────────┘
             │
     ┌───────┴────────┐
     ▼                ▼
┌─────────┐    ┌──────────────┐
│Estudiante│    │Administrativo│
│- Carrera │    │- Departamento│
└─────────┘    └──────────────┘
```

</div>

</div>

---

## Sintaxis de Herencia en C#

<div class="two-col">

<div>

### 📋 Clase Base

```csharp
public class Persona
{
    public string Nombre { get; set; }
    public int Edad { get; set; }

    public void Saludar()
    {
        Console.WriteLine(
            $"Hola, soy {Nombre}");
    }
}
```

</div>

<div>

### 📋 Clase Derivada

```csharp
public class Estudiante : Persona
{
    // Atributos propios
    public string Codigo { get; set; }
    public string Carrera { get; set; }

    // Método propio
    public void Estudiar()
    {
        Console.WriteLine(
            $"{Nombre} estudia {Carrera}");
    }

    // Usa heredados + propios
    public void Presentarse()
    {
        Console.WriteLine(
            $"Soy {Nombre}, {Edad} años");
        Console.WriteLine(
            $"Estudio {Carrera}");
    }
}
```

</div>

</div>

---

## Uso de Clases Derivadas

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

<div class="warning-box">

**⚠️ Qué NO se hereda:**
- ❌ Constructores (se llaman con `base`)
- ❌ Miembros `private`

</div>

---

## Modificadores de Acceso en Herencia

```csharp
public class Persona
{
    public string Nombre { get; set;         // ✅ Todos
    private string password;               // ❌ Solo esta clase
    protected double salario;              // ✅ Clase + hijas
    internal string direccion;             // ✅ Mismo proyecto
}
```

| Modificador | Clase Base | Clase Derivada |
|-------------|-----------|----------------|
| **public** | ✅ Acceso | ✅ Acceso |
| **protected** | ✅ Acceso | ✅ Acceso |
| **internal** | ✅ Acceso | ✅ (si mismo proyecto) |
| **private** | ✅ Acceso | ❌ NO acceso |

---

## Palabra clave `base`

<div class="two-col">

<div>

### 🎯 ¿Para qué sirve?

Acceder a miembros de la clase padre.

### 📋 Sintaxis Constructor

```csharp
public class Estudiante : Persona
{
    public string Codigo { get; set; }

    // Constructor llama a base
    public Estudiante(string n, int e, string c)
        : base(n, e)  // ← Llama Persona() primero
    {
        Codigo = c;  // Luego inicia propio
    }
}
```

### 💻 Uso

```csharp
var est = new Estudiante("María", 20, "2024001");
// Salida:
// "Constructor Persona"
// "Constructor Estudiante"
```

</div>

<div>

### 🔑 Otros Usos de `base`

```csharp
public override void Saludar()
{
    base.Saludar();  // Llama método padre
    Console.WriteLine("Soy estudiante");
}

public override decimal CalcSalario()
{
    return base.CalcSalario() + Comision;
}
```

### ⚡ Orden de Ejecución

```
1. Constructor base (Persona)
2. Constructor derivada (Estudiante)
3. Resto del código derivada
```

### ✅ Ventajas

- Reutiliza código padre
- Mantiene consistencia
- Evita duplicación

</div>

</div>

---

## Jerarquías Profundas

```
NIVEL 1: Persona (abuelo)
├─ Nombre, Documento

NIVEL 2: Empleado (padre) : Persona
├─ CódigoEmpleado
├─ FechaContratación
└─ SalarioBase

NIVEL 3: Profesor (hijo) : Empleado
├─ Especialidad
├─ Materias[]
└─ TituloPostgrado
```

<div class="info-box">

**💡 Herencia Transitiva:** Profesor hereda de Empleado que hereda de Persona

</div>

---

## 2. Polimorfismo: Un Nombre, Múltiples Formas

<div class="two-col">

<div>

### 🎭 Concepto

> Mismo mensaje, diferentes comportamientos según el objeto.

### 🔑 Palabras Clave

| Palabra | Propósito |
|---------|-----------|
| `virtual` | Método que PUEDE sobrescribirse |
| `override` | Sobrescribe método virtual/abstract |
| `abstract` | Sin implementación (obliga a hijos) |

### 💡 Analogía

```
Mensaje: "¡Muévete!"
  🐕 Perro → Corre en 4 patas
  🐈 Gato → Salta sigilosamente
  🐟 Pez → Nada en agua
  🦅 Águila → Vuela
```

</div>

<div>

### ✅ Ventajas

- Código flexible y extensible
- Tratamiento uniforme
- Fácil agregar nuevos tipos

### 📊 Visual

```
┌─────────────────────────────────┐
│      MÉTODO: CalcularArea()       │
├─────────────────────────────────┤
│                                 │
│  ┌─────────┐  ┌──────────┐       │
│  │Círculo  │  │Rectángulo │       │
│ │  π×r²   │  │  b×h      │       │
│  └─────────┘  └──────────┘       │
│                                 │
│  Cada uno implementa a su manera  │
└─────────────────────────────────┘
```

</div>

</div>

---

## Virtual y Override

<div class="two-col">

<div>

### 📋 Clase Base

```csharp
public class Animal
{
    public string Nombre { get; set; }

    // VIRTUAL: puede sobrescribirse
    public virtual void HacerSonido()
    {
        Console.WriteLine(
            "Sonido genérico");
    }

    public virtual void Moverse()
    {
        Console.WriteLine("Se mueve");
    }
}
```

</div>

<div>

### 📋 Clases Derivadas

```csharp
public class Perro : Animal
{
    public override void HacerSonido()
    {
        Console.WriteLine(
            "¡Guau guau! 🐕");
    }

    public override void Moverse()
    {
        Console.WriteLine(
            "Corre en 4 patas 🐾");
    }
}

public class Gato : Animal
{
    public override void HacerSonido()
    {
        Console.WriteLine(
            "¡Miau miau! 🐈");
    }
}
```

</div>

</div>

---

## Polimorfismo en Acción

<div class="two-col">

<div>

### 🎭 Referencia Base

```csharp
// Ref. base, objetos específicos
Animal a1 = new Perro() { Nombre = "Rex" };
Animal a2 = new Gato() { Nombre = "Michi" };
Animal a3 = new Animal() { Nombre = "Genérico" };

// Mismo método, diferente comportamiento
a1.HacerSonido();  // "¡Guau guau! 🐕"
a2.HacerSonido();  // "¡Miau miau! 🐈"
a3.HacerSonido();  // "Sonido genérico"
```

### 📊 Ventajas

- Tratamiento uniforme
- Código extensible
- Fácil agregar tipos

</div>

<div>

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
// Toby: ¡Guau guau! 🐕
// Luna: ¡Miau miau! 🐈
```

</div>

</div>

---

## Llamando a `base.Metodo()`

<div class="two-col">

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

### ✅ Ventajas

- Reutiliza código padre
- Agrega comportamiento hijo
- Mantiene consistencia

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
base.CalcSalario() [Empleado]
    ↓
SalarioBase (2000)
    ↑
+ Comision (1500)
    ↓
= 3500
```

</div>

</div>

---

## 3. Clases y Métodos Abstractos

### Forzando Implementación en Hijas

| Característica | `virtual` | `abstract` |
|----------------|-----------|------------|
| Implementación | Tiene default | Sin implementación |
| Obligatoriedad | Hijas PUEDEN | Hijas DEBEN |
| Instanciación | Sí se puede | NO se puede |

```csharp
// CLASE ABSTRACTA: No instanciable
public abstract class Figura
{
    public string Nombre { get; set; }
    public string Color { get; set; }

    // ABSTRACTO: Hijas DEBEN implementar
    public abstract double CalcularArea();
    public abstract double CalcularPerimetro();

    // CONCRETO: Hijas heredan tal cual
    public void MostrarInfo()
    {
        Console.WriteLine($"Figura: {Nombre}");
        Console.WriteLine($"Área: {CalcularArea():F2}");
    }
}
```

---

## Implementando Clases Abstractas

```csharp
// CÍRCULO
public class Circulo : Figura
{
    public double Radio { get; set; }

    public override double CalcularArea()
    {
        return Math.PI * Radio * Radio;
    }

    public override double CalcularPerimetro()
    {
        return 2 * Math.PI * Radio;
    }
}

// RECTÁNGULO
public class Rectangulo : Figura
{
    public double Base { get; set; }
    public double Altura { get; set; }

    public override double CalcularArea()
    {
        return Base * Altura;
    }

    public override double CalcularPerimetro()
    {
        return 2 * (Base + Altura);
    }
}

// Uso
Figura f = new Circulo { Radio = 5 };  // ✅
// Figura f = new Figura();  // ❌ Error: abstracta
```

---

## 4. Palabra clave `sealed`

<div class="two-col">

<div>

### 🔒 Impedir Herencia

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

</div>

<div>

### 🔒 Impedir Sobrescritura

```csharp
public class Impuestos
{
    public virtual decimal Calc()
    {
        return 0;
    }
}

public class ImpuestosCol : Impuestos
{
    // sealed: Ya no se puede sobrescribir
    public sealed override decimal Calc()
    {
        return base.Calc() + 0.19m;
    }
}

// ❌ Error
// class MasImpuestos : ImpuestosCol { ... }
```

</div>

</div>

---

## 5. Principio de Siskov (LSP)

<div class="two-col">

<div>

### 📐 Principio

> Clase hija debe sustituir a padre sin alterar comportamiento.

### ✅ Correcto

```csharp
Animal a = new Perro();
a.HacerSonido();  // ✅ Funciona

// Perro ES UN Animal
```

### ❌ Incorrecto

```csharp
class Rectangulo
{
    virtual void SetAncho(int w) { ... }
}

class Cuadrado : Rectangulo
{
    override void SetAncho(int w)
    {
        ancho = alto = w;  // ⚠️ Cambia alto!
    }
}

Rectangulo r = new Cuadrado();
r.SetAncho(5);
r.SetAlto(10);
// Esperaba área 50, es 100
```

</div>

<div>

### 📊 Reglas LSP

```
✅ BUENA HERENCIA:
  Estudiante → Persona ✅
  Perro → Animal ✅
  Círculo → Figura ✅

❌ MALA HERENCIA:
  Avión → Vehículo (?)  # Tiene motor, pero vuela
  Reloj → Círculo (?)   # Forma física ≠ concepto
```

### 🎯 Pregunta LSP

¿Cuadrado ES UN Rectángulo?

- Matemáticamente: SÍ
- OO: NO (cambia comportamiento)

</div>

</div>

---

## 6. Ejemplo Práctico: Sistema de Figuras

<div class="two-col">

<div>

### 🎯 Objetivo

Sistema polimórfico de figuras geométricas.

### 📋 Implementación

```csharp
// CLASE ABSTRACTA
public abstract class Figura
{
    public string Nombre { get; set; }
    public string Color { get; set; }

    public abstract double CalcArea();
    public abstract double CalcPerim();

    public virtual void MostrarInfo()
    {
        Console.WriteLine(
            $"\n📐 {Nombre} ({Color})");
        Console.WriteLine(
            $"   Área: {CalcArea():F2} cm²");
        Console.WriteLine(
            $"   Perím: {CalcPerim():F2} cm");
    }
}
```

### 💻 Uso

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
    total += f.CalcArea();
}
Console.WriteLine($"\n📊 Total: {total:F2} cm²");
```

</div>

<div>

### 📊 Clases Concretas

```csharp
// CÍRCULO
public class Circulo : Figura
{
    public double Radio { get; set; }

    public override double CalcArea()
        => Math.PI * Radio * Radio;
    public override double CalcPerimetro()
        => 2 * Math.PI * Radio;
}

// RECTÁNGULO
public class Rectangulo : Figura
{
    public double Base { get; set; }
    public double Altura { get; set; }

    public override double CalcArea()
        => Base * Altura;
    public override double CalcPerimetro()
        => 2 * (Base + Altura);
}
```

</div>

</div>

---

## Resumen de la Clase

<div class="compact-list">

<div>

### 📚 Conceptos

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

### 🎯 Habilidades

```
✅ Aplicar herencia con :
✅ Usar base para llamar padre
✅ Implementar virtual/override
✅ Crear clases abstractas
✅ Aplicar principio LSP
```

</div>

<div>

### 📝 Ejercicios

**1. Banco (Abstracta)**
- `CuentaBancaria` (abstracta)
- `CuentaAhorros`: 3% interés
- `CuentaCorriente`: 0%, sobregiro

**2. Universidad (Abstracta)**
- `EmpleadoUniversidad` (abstracta)
- `Profesor`: Base + horas × valor/hora
- `Administrativo`: Salario fijo
- `Monitor`: Horas × valor/hora

**3. 🌟 Figuras Extendido**
```
Agregar:
- Triángulo (base×altura/2)
- Trapecio ((B+b)×h/2)
- Validar lados > 0
```

</div>

</div>

---

## 🎓 Próxima Clase: Sobrecarga y Modelado BD

### Temas Clase 4

- ✅ Sobrecarga de métodos (overloading)
- ✅ Sobrecarga de operadores
- ✅ Sobrecarga vs Sobreescritura
- ✅ Modelado de bases de datos
- ✅ Relaciones: 1-1, 1-N, N-N

### 📖 Preparación

**Repasa herencia y polimorfismo**

**Piensa en ejemplos de sobrecarga:**
- `Sumar(int, int)` vs `Sumar(double, double)`
- `Imprimir(string)` vs `Imprimir(int)`
- `+` para números vs strings

**💡 Pregunta:** ¿Por qué C# permite sobrecargar operadores y Java no?

**Preparar modelado:**
- Entidades: Usuario, Pedido, Producto
- Relaciones: Usuario → muchos pedidos
- Claves primarias y foráneas

---

# ¡Gracias!
## ¿Preguntas?

<div class="info-box" style="text-align: center;">

**UNAULA - Ingeniería Informática - 2026-I**

</div>
