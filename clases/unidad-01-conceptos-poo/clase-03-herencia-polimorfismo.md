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

### ✅ Beneficios

| Ventaja | Descripción |
|---------|-------------|
| 🔄 | Reutilización de código |
| 🏗️ | Jerarquías lógicas |
| 📈 | Extensibilidad |
| 🔧 | Mantenimiento centralizado |

> ⚠️ **Recomendación:** Máximo 3 niveles de profundidad

---

## Jerarquía Visual de Herencia

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

### 💡 Herencia Transitiva

Si `Profesor` hereda de `Empleado` y `Empleado` hereda de `Persona`:
→ `Profesor` tiene TODO de `Persona` + `Empleado`

---

## Sintaxis de Herencia en C#

| 📋 Clase Base | 📋 Clase Derivada |
|--------------|------------------|
| ```csharp<br>public class Persona<br>{<br>&nbsp;&nbsp;public string Nombre { get; set; }<br>&nbsp;&nbsp;public int Edad { get; set; }<br><br>&nbsp;&nbsp;public void Saludar()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Console.WriteLine(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$"Hola, soy {Nombre}");<br>&nbsp;&nbsp;}<br>}<br>``` | ```csharp<br>public class Estudiante : Persona<br>{<br>&nbsp;&nbsp;// Atributos propios<br>&nbsp;&nbsp;public string Codigo { get; set; }<br>&nbsp;&nbsp;public string Carrera { get; set; }<br><br>&nbsp;&nbsp;// Método propio<br>&nbsp;&nbsp;public void Estudiar()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Console.WriteLine(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$"{Nombre} estudia {Carrera}");<br>&nbsp;&nbsp;}<br>}<br>``` |

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

### ⚠️ Qué NO se hereda

| ❌ NO se hereda | ✅ Sí se hereda |
|-----------------|----------------|
| Constructores | Métodos públicos |
| Miembros `private` | Métodos `protected` |
| | Propiedades públicas/protected |

---

## Modificadores de Acceso en Herencia

```csharp
public class Persona
{
    public string Nombre { get; set; }        // ✅ Todos
    private string password;                  // ❌ Solo esta clase
    protected double salario;                 // ✅ Clase + hijas
    internal string direccion;                // ✅ Mismo proyecto
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

| 🎯 ¿Para qué sirve? | 📋 Sintaxis Constructor |
|---------------------|----------------------|
| Acceder a miembros de la clase padre | ```csharp<br>public class Estudiante : Persona<br>{<br>&nbsp;&nbsp;public string Codigo { get; set; }<br><br>&nbsp;&nbsp;// Constructor llama a base<br>&nbsp;&nbsp;public Estudiante(string n, int e, string c)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: base(n, e)  // ← Llama Persona() primero<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Codigo = c;  // Luego inicia propio<br>&nbsp;&nbsp;}<br>}<br>``` |

### ⚡ Orden de Ejecución

```
1. Constructor base (Persona)
2. Constructor derivada (Estudiante)
3. Resto del código derivada
```

---

## Otros Usos de `base`

| 🔄 Extender método | 💻 Uso práctico |
|-------------------|----------------|
| ```csharp<br>public override void Saludar()<br>{<br>&nbsp;&nbsp;base.Saludar();  // Llama método padre<br>&nbsp;&nbsp;Console.WriteLine("Soy estudiante");<br>}<br>``` | ```csharp<br>public override decimal CalcSalario()<br>{<br>&nbsp;&nbsp;// base + comisión<br>&nbsp;&nbsp;return base.CalcSalario() + Comision;<br>}<br>``` |

### ✅ Ventajas de usar `base`

| Ventaja | Descripción |
|---------|-------------|
| 🔄 | Reutiliza código padre |
| ✅ | Mantiene consistencia |
| 📉 | Evita duplicación |

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
└─ TítuloPostgrado
```

> 💡 **Herencia Transitiva:** `Profesor` hereda de `Empleado` que hereda de `Persona`

---

## 2. Polimorfismo: Un Nombre, Múltiples Formas

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

---

## Polimorfismo Visual

```
┌─────────────────────────────────┐
│      MÉTODO: CalcularArea()       │
├─────────────────────────────────┤
│                                 │
│  ┌─────────┐  ┌──────────┐       │
│  │Círculo  │  │Rectángulo │       │
│  │  π×r²   │  │  b×h      │       │
│  └─────────┘  └──────────┘       │
│                                 │
│  Cada uno implementa a su manera  │
└─────────────────────────────────┘
```

### ✅ Ventajas del Polimorfismo

| Ventaja | Descripción |
|---------|-------------|
| 🔄 | Código flexible y extensible |
| 📦 | Tratamiento uniforme |
| ➕ | Fácil agregar nuevos tipos |

---

## Virtual y Override

| 📋 Clase Base | 📋 Clases Derivadas |
|--------------|-------------------|
| ```csharp<br>public class Animal<br>{<br>&nbsp;&nbsp;public string Nombre { get; set; }<br><br>&nbsp;&nbsp;// VIRTUAL: puede sobrescribirse<br>&nbsp;&nbsp;public virtual void HacerSonido()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Console.WriteLine("Sonido genérico");<br>&nbsp;&nbsp;}<br><br>&nbsp;&nbsp;public virtual void Moverse()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Console.WriteLine("Se mueve");<br>&nbsp;&nbsp;}<br>}<br>``` | ```csharp<br>public class Perro : Animal<br>{<br>&nbsp;&nbsp;public override void HacerSonido()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Console.WriteLine("¡Guau guau! 🐕");<br>&nbsp;&nbsp;}<br><br>&nbsp;&nbsp;public override void Moverse()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Console.WriteLine("Corre en 4 patas 🐾");<br>&nbsp;&nbsp;}<br>}<br><br>public class Gato : Animal<br>{<br>&nbsp;&nbsp;public override void HacerSonido()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Console.WriteLine("¡Miau miau! 🐈");<br>&nbsp;&nbsp;}<br>}<br>``` |

---

## Polimorfismo en Acción

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

---

## Llamando a `base.Metodo()`

| 🔄 Extender, No Reemplazar | 💻 Uso Práctico |
|---------------------------|----------------|
| ```csharp<br>public class Empleado<br>{<br>&nbsp;&nbsp;public virtual decimal CalcSalario()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;return SalarioBase;<br>&nbsp;&nbsp;}<br>}<br><br>public class Vendedor : Empleado<br>{<br>&nbsp;&nbsp;public decimal Comision { get; set; }<br><br>&nbsp;&nbsp;public override decimal CalcSalario()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;// Llama base + agrega propio<br>&nbsp;&nbsp;&nbsp;&nbsp;return base.CalcSalario() + Comision;<br>&nbsp;&nbsp;}<br>}<br>``` | ```csharp<br>Vendedor v = new Vendedor<br>{<br>&nbsp;&nbsp;Nombre = "Carlos",<br>&nbsp;&nbsp;SalarioBase = 2000,<br>&nbsp;&nbsp;Comision = 1500<br>};<br><br>Console.WriteLine(v.CalcSalario());<br>// 3500 (base + comisión)<br>``` |

### 📊 Flujo de Ejecución

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

| 📊 CÍRCULO | 📐 RECTÁNGULO |
|-----------|--------------|
| ```csharp<br>public class Circulo : Figura<br>{<br>&nbsp;&nbsp;public double Radio { get; set; }<br><br>&nbsp;&nbsp;public override double CalcularArea()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒ Math.PI * Radio * Radio;<br><br>&nbsp;&nbsp;public override double CalcularPerimetro()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒ 2 * Math.PI * Radio;<br>}<br>``` | ```csharp<br>public class Rectangulo : Figura<br>{<br>&nbsp;&nbsp;public double Base { get; set; }<br>&nbsp;&nbsp;public double Altura { get; set; }<br><br>&nbsp;&nbsp;public override double CalcularArea()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒ Base * Altura;<br><br>&nbsp;&nbsp;public override double CalcularPerimetro()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒ 2 * (Base + Altura);<br>}<br>``` |

### 💻 Uso de Clases Abstractas

```csharp
// ✅ Ref. base, objeto concreto
Figura f1 = new Circulo { Radio = 5 };
Figura f2 = new Rectangulo { Base=4, Altura=6 };

f1.MostrarInfo();  // Área: 78.54 cm²
f2.MostrarInfo();  // Área: 24.00 cm²

// ❌ Error: no se puede instanciar
// Figura f = new Figura();
```

---

## Reglas de Clases Abstractas

| Aspecto | Regla |
|---------|-------|
| Instanciar | ❌ NO |
| Heredar | ✅ Sí |
| Métodos abstractos | DEBEN implementarse |
| Métodos concretos | Se heredan |

### 🎯 Cuándo Usar

| ✅ Usa abstract cuando... | ❌ NO uses cuando... |
|--------------------------|---------------------|
| Hay comportamiento común pero implementación diferente | Solo hay una clase concreta |
| Quieres forzar diseño en hijas | No necesitas polimorfismo |
| La clase base es solo un "contrato" | La clase se va a instanciar |

---

## 4. Palabra clave `sealed`

| 🔒 Impedir Herencia | 🔒 Impedir Sobrescritura |
|-------------------|------------------------|
| ```csharp<br>// sealed: Nadie puede heredar<br>public sealed class SeguridadSocial<br>{<br>&nbsp;&nbsp;public string Numero { get; set; }<br>&nbsp;&nbsp;public decimal Saldo { get; set; }<br>}<br><br>// ❌ Error<br>// public class HackeoSS : SeguridadSocial { }<br>``` | ```csharp<br>public class Impuestos<br>{<br>&nbsp;&nbsp;public virtual decimal Calc()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;return 0;<br>&nbsp;&nbsp;}<br>}<br><br>public class ImpuestosCol : Impuestos<br>{<br>&nbsp;&nbsp;// sealed: Ya no se puede sobrescribir<br>&nbsp;&nbsp;public sealed override decimal Calc()<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;return base.Calc() + 0.19m;<br>&nbsp;&nbsp;}<br>}<br>``` |

### 🎯 Cuándo Usar `sealed`

| ✅ Usa sealed cuando... | Ejemplo |
|------------------------|---------|
| La clase NO está diseñada para heredar | `String`, `DateTime` |
| Quieres proteger lógica crítica | Seguridad, encriptación |
| El método override finaliza una cadena | Cálculos de impuestos |

---

## 5. Principio de Liskov (LSP)

### 📐 Principio

> **Clase hija debe sustituir a padre sin alterar comportamiento.**

| ✅ Correcto | ❌ Incorrecto |
|------------|--------------|
| ```csharp<br>Animal a = new Perro();<br>a.HacerSonido();  // ✅ Funciona<br><br>// Perro ES UN Animal<br>``` | ```csharp<br>class Rectangulo<br>{<br>&nbsp;&nbsp;virtual void SetAncho(int w) { ... }<br>}<br><br>class Cuadrado : Rectangulo<br>{<br>&nbsp;&nbsp;override void SetAncho(int w)<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;ancho = alto = w;  // ⚠️ Cambia alto!<br>&nbsp;&nbsp;}<br>}<br><br>Rectangulo r = new Cuadrado();<br>r.SetAncho(5);<br>r.SetAlto(10);<br>// Esperaba área 50, es 100<br>``` |

---

## Reglas de Buen Diseño LSP

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

¿`Cuadrado` ES UN `Rectángulo`?
- Matemáticamente: **SÍ**
- Orientación a Objetos: **NO** (cambia comportamiento)

> 💡 El LSP se trata de **comportamiento**, no de taxonomía

---

## 6. Ejemplo Práctico: Sistema de Figuras

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
        Console.WriteLine($"\n📐 {Nombre} ({Color})");
        Console.WriteLine($"   Área: {CalcularArea():F2} cm²");
        Console.WriteLine($"   Perím: {CalcularPerimetro():F2} cm");
    }
}
```

---

## Clases Concretas del Sistema

| 📊 CÍRCULO | 📐 RECTÁNGULO |
|-----------|--------------|
| ```csharp<br>public class Circulo : Figura<br>{<br>&nbsp;&nbsp;public double Radio { get; set; }<br><br>&nbsp;&nbsp;public override double CalcularArea()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒ Math.PI * Radio * Radio;<br>&nbsp;&nbsp;public override double CalcularPerimetro()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒ 2 * Math.PI * Radio;<br>}<br>``` | ```csharp<br>public class Rectangulo : Figura<br>{<br>&nbsp;&nbsp;public double Base { get; set; }<br>&nbsp;&nbsp;public double Altura { get; set; }<br><br>&nbsp;&nbsp;public override double CalcularArea()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒ Base * Altura;<br>&nbsp;&nbsp;public override double CalcularPerimetro()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒ 2 * (Base + Altura);<br>}<br>``` |

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
   Perím: 31.42 cm

📐 R1 (Azul)
   Área: 24.00 cm²
   Perím: 20.00 cm

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
