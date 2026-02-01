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

# Herencia y Polimorfismo

<!--
[2026-01-31] - Clase enriquecida con infografías

IMÁGENES GENERADAS:
- clase-03-herencia.png: Diagrama visual de jerarquía de herencia en POO
- clase-03-polimorfismo.png: Diagrama explicativo de polimorfismo con animales
-->

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Aplicar** el concepto de herencia entre clases
2. **Utilizar** la palabra clave `base` para acceder a la clase padre
3. **Implementar** polimorfismo con `virtual`, `override` y `abstract`
4. **Distinguir** entre clases abstractas e interfaces
5. **Aplicar** el principio de sustitución de Liskov

**Duración:** 90 minutos

---

## Agenda

1. Herencia: Conceptos fundamentales (20 min)
2. Polimorfismo: virtual y override (20 min)
3. Clases y métodos abstractos (20 min)
4. La palabra clave `sealed` (10 min)
5. Principio de sustitución de Liskov (10 min)
6. Ejemplo práctico: Sistema de figuras geométricas (10 min)

---

## 1. Herencia

### ¿Qué es la herencia?

<div style="display: flex; gap: 30px; align-items: center;">

<div style="flex: 1;">

![Jerarquía de Herencia](../../assets/infografias/clase-03-herencia.png){: style="max-width: 100%; max-height: 350px;"}

</div>

<div style="flex: 1;">

**🎯 Concepto:**

> **Herencia** = Crear nuevas clases basadas en existentes, reutilizando código.

**🔑 Terminología:**

| Término | Significado |
|---------|-------------|
| **Clase Base** | Padre/Superclass (compartida) |
| **Clase Derivada** | Hija/Subclass (extiende) |
| **`:`** | Operador de herencia en C# |
| **`base`** | Referencia a la clase padre |
| **`protected`** | Accesible en clase e hijas |

**✅ Beneficios:**
- Reutilización de código
- Jerarquías lógicas
- Extensibilidad
- Mantenimiento centralizado

**⚠️ Recomendación:**
Máximo 3 niveles de profundidad.

</div>

</div>

---
### Representación ASCII:
```
┌─────────────────────────────────────────────────────────────┐
│                    JERARQUÍA DE HERENCIA                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    ┌───────────────┐                        │
│                    │   Persona     │  ← CLASE BASE          │
│                    │  (base class) │    (padre/super)       │
│                    │  - Nombre     │                        │
│                    │  - Edad       │                        │
│                    └───────┬───────┘                        │
│                            │                                │
│           ┌────────────────┼────────────────┐               │
│           │                │                │               │
│           ▼                ▼                ▼               │
│     ┌──────────┐     ┌──────────┐     ┌──────────┐         │
│     │Estudiante│     │ Profesor │     │Administrativo│      │
│     │(derivada)│     │(derivada)│     │  (derivada)  │      │
│     │- Carrera │     │- Salario │     │  - Departamento│     │
│     │- Semestre│     │- Materias│     │  - Cargo       │     │
│     └──────────┘     └──────────┘     └──────────┘         │
│                                                             │
│     CLASES DERIVADAS heredan de PERSONA + atributos propios │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### La palabra clave `:` (dos puntos)

En C#, el símbolo `:` después del nombre de la clase indica herencia:

```csharp
// ════════════════════════════════════════════════════
// CLASE BASE (Padre) - La clase "general"
// ════════════════════════════════════════════════════
public class Persona
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
    public string Identificacion { get; set; }
    
    public void Saludar()
    {
        Console.WriteLine($"Hola, soy {Nombre}");
    }
}

// ════════════════════════════════════════════════════
// CLASE DERIVADA (Hija) - Sintaxis: Nombre : Base
// ════════════════════════════════════════════════════
public class Estudiante : Persona  // ← Estudiante HEREDA de Persona
{
    // Atributos propios de Estudiante (no heredados)
    public string Codigo { get; set; }
    public string Carrera { get; set; }
    public int Semestre { get; set; }
    
    // Método propio de Estudiante
    public void Estudiar()
    {
        Console.WriteLine($"{Nombre} está estudiando {Carrera}");
    }
    
    // Método que usa propiedades heredadas y propias
    public void Presentarse()
    {
        Console.WriteLine($"Soy {Nombre}, tengo {Edad} años");
        Console.WriteLine($"Estudio {Carrera}, semestre {Semestre}");
    }
}
```

---

## Acceso a Miembros Heredados

### ¿Qué se hereda?

```csharp
public class Program
{
    static void Main(string[] args)
    {
        Estudiante est = new Estudiante();
        
        // Miembros HEREDADOS de Persona
        est.Nombre = "María López";     // ✅ Heredado
        est.Edad = 20;                   // ✅ Heredado
        est.Saludar();                   // ✅ Heredado
        
        // Miembros PROPIOS de Estudiante
        est.Codigo = "2024001";          // ✅ Propio
        est.Carrera = "Ingeniería";      // ✅ Propio
        est.Estudiar();                  // ✅ Propio
    }
}
```

**¿Qué NO se hereda?**
- ❌ Constructores (pero se pueden llamar con `base`)
- ❌ Miembros `private` de la clase base

---

## Modificadores de Acceso y Herencia

### Visibilidad en la jerarquía

```csharp
public class Persona
{
    public string Nombre { get; set; }      // Todos pueden ver
    private string password;                // SOLO esta clase
    protected double salario;               // Esta clase + hijas
    internal string direccion;              // Mismo proyecto
    protected internal string codigoInterno; // Proyecto + hijas
}

public class Empleado : Persona
{
    public void MetodoEjemplo()
    {
        Console.WriteLine(Nombre);       // ✅ public
        // Console.WriteLine(password);  // ❌ private
        Console.WriteLine(salario);      // ✅ protected
        Console.WriteLine(direccion);    // ✅ internal (mismo proyecto)
        Console.WriteLine(codigoInterno);// ✅ protected internal
    }
}
```

---

### La palabra clave `base`

La palabra clave `base` permite acceder a miembros de la clase padre, especialmente útil en constructores:

```csharp
// ════════════════════════════════════════════════════
// CLASE BASE
// ════════════════════════════════════════════════════
public class Persona
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
    
    // Constructor de Persona
    public Persona(string nombre, int edad)
    {
        Console.WriteLine("Constructor Persona ejecutado");
        Nombre = nombre;
        Edad = edad;
    }
}

// ════════════════════════════════════════════════════
// CLASE DERIVADA
// ════════════════════════════════════════════════════
public class Estudiante : Persona
{
    public string Codigo { get; set; }
    
    // Constructor de Estudiante llama a base
    public Estudiante(string nombre, int edad, string codigo) 
        : base(nombre, edad)  // ← Llama constructor de Persona PRIMERO
    {
        Console.WriteLine("Constructor Estudiante ejecutado");
        Codigo = codigo;  // Luego inicializa lo propio
    }
}

// ════════════════════════════════════════════════════
// USO
// ════════════════════════════════════════════════════
Estudiante est = new Estudiante("María", 20, "2024001");
// Salida:
// Constructor Persona ejecutado
// Constructor Estudiante ejecutado
```

---

### Jerarquías más profundas

La herencia puede extenderse a múltiples niveles (aunque se recomienda máximo 3):

```csharp
// ════════════════════════════════════════════════════
// NIVEL 1: Clase base (abuelo)
// ════════════════════════════════════════════════════
public class Persona 
{ 
    public string Nombre { get; set; }
    public string Documento { get; set; }
}

// ════════════════════════════════════════════════════
// NIVEL 2: Hereda de Persona (padre)
// ════════════════════════════════════════════════════
public class Empleado : Persona 
{ 
    public string CodigoEmpleado { get; set; }
    public DateTime FechaContratacion { get; set; }
    public decimal SalarioBase { get; set; }
}

// ════════════════════════════════════════════════════
// NIVEL 3: Hereda de Empleado (hijo)
// Hereda TRANSITIVAMENTE de Persona también
// ════════════════════════════════════════════════════
public class Profesor : Empleado 
{ 
    public string Especialidad { get; set; }
    public List<string> Materias { get; set; }
    public string TituloPostgrado { get; set; }
}

// ════════════════════════════════════════════════════
// USO: Acceso a todos los niveles
// ════════════════════════════════════════════════════
Profesor prof = new Profesor();
prof.Nombre = "Carlos Ruiz";          // ← De Persona (Nivel 1)
prof.Documento = "1234567890";        // ← De Persona (Nivel 1)
prof.CodigoEmpleado = "EMP001";       // ← De Empleado (Nivel 2)
prof.SalarioBase = 3500000;           // ← De Empleado (Nivel 2)
prof.Especialidad = "Programación";   // ← De Profesor (Nivel 3)
prof.Materias = new List<string> { "POO I", "POO II" };  // ← De Profesor
```

---
### Jerarquías más profundas


---

## 2. Polimorfismo

### Un nombre, múltiples formas

<div style="display: flex; gap: 30px; align-items: center;">

<div style="flex: 1;">

![Polimorfismo](../../assets/infografias/clase-03-polimorfismo.png){: style="max-width: 100%; max-height: 350px;"}

</div>

<div style="flex: 1;">

**🎭 El Poder del Polimorfismo:**

> **Polimorfismo** = Mismo mensaje, diferentes comportamientos según el objeto.

**🔑 Palabras clave:**

| Palabra | Propósito |
|---------|-----------|
| `virtual` | Método que PUEDE sobrescribirse |
| `override` | Sobrescribe método virtual/abstract |
| `abstract` | Método SIN implementación (obliga a hijos) |

**💡 Analogía del mundo real:**
```
Mismo mensaje: "¡Muévete!"
  🐕 Perro → Corre en 4 patas
  🐈 Gato → Salta y camina sigilosamente
  🐟 Pez → Nada en el agua
  🦅 Águila → Vuela en el aire
```

**✅ Ventajas:**
- Código flexible y extensible
- Tratamiento uniforme de objetos diferentes
- Fácil agregar nuevos tipos sin modificar código existente

</div>

</div>

---
### Representación ASCII:

```
┌─────────────────────────────────────────────────────────────┐
│              POLIMORFISMO EN ACCIÓN                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Mismo mensaje: CalcularArea()                            │
│                                                             │
│        ┌─────────────────┐                                  │
│        │   Figura        │ ← Clase abstracta               │
│        │ CalcularArea()  │   (define el contrato)          │
│        └────────┬────────┘                                  │
│                 │                                           │
│     ┌───────────┼───────────┬───────────┐                  │
│     ▼           ▼           ▼           ▼                  │
│  ┌──────┐   ┌──────┐   ┌────────┐   ┌──────────┐          │
│  │Círculo│   │Rectángulo│ │ Triángulo│ │  Trapecio  │          │
│  │π*r²   │   │b*h       │ │(b*h)/2   │ │(B+b)*h/2   │          │
│  └──────┘   └──────┘   └────────┘   └──────────┘          │
│                                                             │
│  Cada clase implementa CalcularArea() a su manera           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Virtual y Override

### Sobrescritura de métodos

```csharp
// ════════════════════════════════════════════════════
// CLASE BASE con métodos virtual
// ════════════════════════════════════════════════════
public class Animal
{
    public string Nombre { get; set; }
    
    // Método VIRTUAL: puede ser sobrescrito por hijos
    public virtual void HacerSonido()
    {
        Console.WriteLine("El animal hace un sonido genérico");
    }
    
    public virtual void Moverse()
    {
        Console.WriteLine("El animal se mueve");
    }
}

// ════════════════════════════════════════════════════
// CLASE DERIVADA que sobrescribe
// ════════════════════════════════════════════════════
public class Perro : Animal
{
    // OVERRIDE: proporciona implementación específica
    public override void HacerSonido()
    {
        Console.WriteLine("¡Guau guau! 🐕");
    }
    
    public override void Moverse()
    {
        Console.WriteLine("El perro corre en 4 patas 🐾");
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
---

### Uso con referencias de clase base (Polimorfismo en acción)

```csharp
class Program
{
    static void Main(string[] args)
    {
        // ════════════════════════════════════════════════════
        // POLIMORFISMO: Referencias de tipo base, objetos específicos
        // ════════════════════════════════════════════════════
        
        Animal animal1 = new Perro() { Nombre = "Rex" };    // ← Perro como Animal
        Animal animal2 = new Gato() { Nombre = "Michi" };   // ← Gato como Animal
        Animal animal3 = new Animal() { Nombre = "Genérico" }; // ← Animal puro
        
        // Mismo método llamado, diferente comportamiento (POLIMORFISMO)
        Console.WriteLine("=== SONIDOS ===");
        animal1.HacerSonido();  // "¡Guau guau! 🐕"  ← Ejecuta Perro.HacerSonido()
        animal2.HacerSonido();  // "¡Miau miau! 🐈"  ← Ejecuta Gato.HacerSonido()
        animal3.HacerSonido();  // "El animal hace un sonido"  ← Ejecuta Animal.HacerSonido()
        
        // ════════════════════════════════════════════════════
        // COLECCIÓN POLIMÓRFICA: Almacenar diferentes tipos
        // ════════════════════════════════════════════════════
        List<Animal> animales = new List<Animal> 
        { 
            new Perro { Nombre = "Rex" }, 
            new Gato { Nombre = "Michi" }, 
            new Perro { Nombre = "Toby" },
            new Gato { Nombre = "Luna" }
        };
        
        Console.WriteLine("\n=== RECORRIENDO LA LISTA ===");
        foreach (Animal a in animales)
        {
            Console.Write($"{a.Nombre}: ");
            a.HacerSonido();  // Cada animal hace su propio sonido!
        }
    }
}
// Output: Rex: ¡Guau guau! 🐕
//         Michi: ¡Miau miau! 🐈
//         Toby: ¡Guau guau! 🐕
//         Luna: ¡Miau miau! 🐈
```

---
## Llamando al Método Base
---
### Preservando comportamiento padre

```csharp
public class Empleado
{
    public string Nombre { get; set; }
    public decimal SalarioBase { get; set; }
    
    public virtual decimal CalcularSalario()
    {
        return SalarioBase;
    }
    
    public virtual void MostrarInfo()
    {
        Console.WriteLine($"Empleado: {Nombre}");
        Console.WriteLine($"Salario: {CalcularSalario():C}");
    }
}

public class Vendedor : Empleado
{
    public decimal Comision { get; set; }
    
    public override decimal CalcularSalario()
    {
        // Llamar al método base + agregar comportamiento propio
        return base.CalcularSalario() + Comision;
    }
    
    public override void MostrarInfo()
    {
        Console.WriteLine("=== VENDEDOR ===");
        base.MostrarInfo();  // Reutiliza código del padre
        Console.WriteLine($"Comisión: {Comision:C}");
        Console.WriteLine($"TOTAL: {CalcularSalario():C}");
    }
}

// ════════════════════════════════════════════════════
// USO
// ════════════════════════════════════════════════════
Empleado emp = new Empleado { Nombre = "Ana", SalarioBase = 3000 };
emp.MostrarInfo();  // Muestra solo salario base

Vendedor vend = new Vendedor { Nombre = "Carlos", SalarioBase = 2000, Comision = 1500 };
vend.MostrarInfo();  // Muestra base + comisión + total
---

## 3. Clases y Métodos Abstractos

### Forzando la implementación

```csharp
// CLASE ABSTRACTA: No se puede instanciar directamente
public abstract class Figura
{
    public string Nombre { get; set; }
    public string Color { get; set; }
    
    // MÉTODO ABSTRACTO: Sin implementación, las hijas DEBEN implementarlo
    public abstract double CalcularArea();
    
    // MÉTODO ABSTRACTO
    public abstract double CalcularPerimetro();
    
    // MÉTODO CONCRETO: Tiene implementación, las hijas pueden heredarlo
    public void MostrarInfo()
    {
        Console.WriteLine($"Figura: {Nombre}");
        Console.WriteLine($"Color: {Color}");
        Console.WriteLine($"Área: {CalcularArea():F2}");
        Console.WriteLine($"Perímetro: {CalcularPerimetro():F2}");
    }
}
```

---
## Implementando Clases Abstractas
---
### Clases concretas que heredan

```csharp
public class Circulo : Figura
{
    public double Radio { get; set; }
    
    // DEBE implementar CalcularArea (es abstracto)
    public override double CalcularArea()
    {
        return Math.PI * Radio * Radio;
    }
    
    // DEBE implementar CalcularPerimetro
    public override double CalcularPerimetro()
    {
        return 2 * Math.PI * Radio;
    }
}

public class Rectangulo : Figura
{
    public double Base { get; set; }
    public double Altura { get; set; }
    
---
### Clases concretas que heredan


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
// Figura f = new Figura();  // ❌ ERROR: no se puede instanciar abstracta
Figura f = new Circulo { Radio = 5 };  // ✅ Sí se puede
f.CalcularArea();  // Llama a la implementación de Circulo
```
---

## Diferencias: Virtual vs Abstract

| Característica | `virtual` | `abstract` |
| ---------------- | ----------- | ------------ |
| Implementación | Tiene implementación por defecto | Sin implementación |
| Obligatoriedad | Las hijas PUEDEN sobrescribir | Las hijas DEBEN sobrescribir |
| Clase | Puede estar en clase normal | Solo en clases abstractas |
| Instanciación | Clase se puede instanciar | Clase NO se puede instanciar |

```csharp
// Clase normal con virtual
public class Animal 
{
    public virtual void Hablar() { Console.WriteLine("Sonido"); }
}

// Clase abstracta con abstract
public abstract class Figura 
{
    public abstract double CalcularArea();  // Sin cuerpo
}
```

---
### Impidiendo la herencia


```csharp
// sealed: Nadie puede heredar de esta clase
public sealed class SeguridadSocial
{
    public string Numero { get; set; }
    public decimal Saldo { get; set; }
}

// public class HackeoSS : SeguridadSocial { }  // ❌ ERROR

// sealed en método: Nadie puede sobrescribir más
public class Impuestos
{
    public virtual decimal Calcular() { return 0; }
}

public class ImpuestosColombia : Impuestos
{
    // Este método ya no puede ser sobrescrito más
    public sealed override decimal Calcular() 
    { 
        return base.Calcular() + 0.19m; 
    }
}

---
### Impidiendo la herencia


// public class ImpuestosBogota : ImpuestosColombia
// {
//     public override decimal Calcular() { }  // ❌ ERROR
// }
```

---

## 5. Principio de Sustitución de Liskov

### Diseño correcto de herencia

> **Principio LSP (Liskov Substitution Principle):** Una clase hija debe poder sustituir a su clase padre sin alterar el comportamiento correcto del programa.

```
✅ EJEMPLO CORRECTO:

   Animal a = new Perro();  // Perro ES UN Animal
   a.HacerSonido();         // Funciona correctamente


❌ EJEMPLO INCORRECTO (violación LSP):

   class Rectangulo { virtual void SetAncho(int w) { ... } }
   
   class Cuadrado : Rectangulo  // Cuadrado ES UN Rectángulo?
   {
       override void SetAncho(int w) 
       { 
           ancho = alto = w;  // ¡Cambia alto también!
       }
   }
   
   Rectangulo r = new Cuadrado();
   r.SetAncho(5);
   r.SetAlto(10);
   // ¡Esperaba área 50, pero es 100! (5x5 o 10x10)
```

---

## Reglas del Principio LSP

### Indicadores de herencia incorrecta

```
❌ "ES UN" no funciona:
   • Un Cuadrado ES UN Rectángulo? (matemáticamente sí, OO no)
   
❌ Violación de precondiciones:
   • Padre acepta null, hijo lanza excepción
   
❌ Cambio de comportamiento inesperado:
   • Mismo método, resultados incompatibles
   
✅ BUENA HERENCIA:
   • Estudiante ES UNA Persona ✅
   • Perro ES UN Animal ✅
   • Círculo ES UNA Figura ✅
   
❌ MALA HERENCIA:
   • Avión ES UN Vehículo? (tiene motor, pero vuela)
   • Reloj ES UN Círculo? (forma física ≠ concepto)
```

---
## 6. Ejemplo Práctico: Sistema de Figuras
---
### Implementación completa

```csharp
// CLASE ABSTRACTA BASE
public abstract class Figura
{
    public string Nombre { get; set; }
    public string Color { get; set; }
    
    public abstract double CalcularArea();
    public abstract double CalcularPerimetro();
    
    public virtual void MostrarInfo()
    {
        Console.WriteLine($"\n📐 {Nombre} ({Color})");
        Console.WriteLine($"   Área: {CalcularArea():F2} cm²");
        Console.WriteLine($"   Perímetro: {CalcularPerimetro():F2} cm");
    }
}

// CÍRCULO
public class Circulo : Figura
{
    public double Radio { get; set; }
    
---
### Implementación completa


    public override double CalcularArea() => Math.PI * Radio * Radio;
    public override double CalcularPerimetro() => 2 * Math.PI * Radio;
}

// RECTÁNGULO
public class Rectangulo : Figura
{
    public double Base { get; set; }
    public double Altura { get; set; }
    
    public override double CalcularArea() => Base * Altura;
    public override double CalcularPerimetro() => 2 * (Base + Altura);
}
```
---
## Uso del Sistema de Figuras

```csharp
class Program
{
    static void Main(string[] args)
    {
        // Colección polimórfica
        List<Figura> figuras = new List<Figura>
        {
            new Circulo { Nombre = "Círculo 1", Color = "Rojo", Radio = 5 },
            new Rectangulo { Nombre = "Rectángulo 1", Color = "Azul", Base = 4, Altura = 6 },
            new Circulo { Nombre = "Círculo 2", Color = "Verde", Radio = 3 }
        };
        
        double areaTotal = 0;
        
        Console.WriteLine("=== SISTEMA DE FIGURAS ===\n");
        
        foreach (Figura f in figuras)
        {
            f.MostrarInfo();
            areaTotal += f.CalcularArea();
        }
        
---
## Uso del Sistema de Figuras


        Console.WriteLine($"\n📊 Área total de todas las figuras: {areaTotal:F2} cm²");
    }
}
```

---

## Resumen, Ejercicios y Conceptos Avanzados

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**📚 Resumen de Conceptos:**

| Concepto | Descripción |
|----------|-------------|
| **Herencia** | `:` crea jerarquías de clases |
| **base** | Llama miembros de clase padre |
| **protected** | Visible en clase y derivadas |
| **virtual** | Método que PUEDE sobrescribirse |
| **override** | Sobrescribe método virtual/abstract |
| **abstract** | Sin implementación, obliga a hijos |
| **sealed** | Impide herencia/sobrescritura |
| **Polimorfismo** | Un interfaz, múltiples formas |

**📝 Ejercicios Propuestos:**

**1. Sistema Bancario**
- `CuentaBancaria` (abstracta): Número, Saldo, `CalcularInteres()` (abstract)
- `CuentaAhorros`: 3% interés anual
- `CuentaCorriente`: 0% interés, permite sobregiro

**2. Empleados Universitarios**
- `EmpleadoUniversidad` (abstracta): `CalcularSalario()` (abstract)
- `Profesor`: Base + horas × valor/hora
- `Administrativo`: Salario fijo
- `Monitor`: Horas × valor/hora

</div>

<div style="flex: 1;">

**🔗 Binding: Temprano vs Tardío**

| Tipo | ¿Cuándo se decide? | Ejemplo |
|------|-------------------|---------|
| **Temprano** (Early) | Compilación | Sobrecarga de métodos |
| **Tardío** (Late) | Ejecución | Polimorfismo virtual/override |

```csharp
// Early binding (compilación)
calc.Sumar(5, 3);  // Tipos conocidos

// Late binding (ejecución)
animal.Hablar();   // Tipo Animal, objeto Perro
                    // Se decide en runtime
```

**🎯 Interfaces vs Clases Abstractas:**

| Aspecto | Interfaz | Clase Abstracta |
|----------|-----------|-----------------|
| Implementación | Ninguna (solo firma) | Puede tener código |
| Herencia | Múltiple | Simple (1 clase) |
| Uso | Contratos/capacidades | Compartir código |

**Regla:**
- Interface → "PUEDE hacer" (IVolador, IComparable)
- Abstract → "ES un" (Ave, Vehículo, Figura)

</div>

</div>

---

## Próxima Clase: Sobrecarga y Modelado BD

<div style="display: flex; gap: 30px;">

<div style="flex: 1;">

**📋 Temas de la Clase 4:**

- ✅ **Sobrecarga de métodos** (overloading)
- ✅ **Sobrecarga de operadores**
- ✅ **Sobrecarga vs Sobreescritura**
- ✅ **Modelamiento de bases de datos**
- ✅ **Relaciones: 1-1, 1-N, N-N**

**🎯 Objetivo:**
Entender sobrecarga (mismo método, diferentes parámetros) vs sobreescritura (mismo método, diferente implementación), y aprender fundamentos de modelado BD.

</div>

<div style="flex: 1;">

**📖 Preparación:**

1. **Repasar** herencia y polimorfismo
2. **Practicar** ejercicios propuestos
3. **Pensar** en ejemplos de sobrecarga:
   - `Sumar(int, int)` vs `Sumar(double, double)`
   - `Imprimir(string)` vs `Imprimir(int)`
   - `+` para números vs `+` para strings

**💡 Pregunta reflexiva:**
¿Por qué C# permite sobrecargar operadores pero Java no?

**Preparar modelado:**
- Entidades: Usuario, Pedido, Producto
- Relaciones: Un usuario → muchos pedidos
- Claves primarias y foráneas

**¡Nos vemos!**

</div>

</div>

---

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
