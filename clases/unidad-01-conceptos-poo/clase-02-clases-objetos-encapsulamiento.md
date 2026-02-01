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

# Clases, Objetos y Encapsulamiento

<div class="info-box" style="text-align: center;">

**IF0100 - Lenguaje de Programación OO II**

*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 1 - Clase 2*

</div>

---

## Objetivos y Agenda

<div class="two-col">

<div>

### 🎯 Objetivos

| # | Meta |
|---|------|
| 1 | Definir clases y objetos |
| 2 | Aplicar encapsulamiento |
| 3 | Usar propiedades get/set |
| 4 | Implementar constructores |
| 5 | Campos vs Propiedades |

</div>

<div>

### 📋 Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 10' | Repaso POO |
| 20' | Clases y Objetos |
| 20' | Encapsulamiento |
| 20' | Propiedades |
| 15' | Constructores |
| 5' | Práctica |

</div>

</div>

---

## 1. Repaso: Programación Orientada a Objetos

<div class="two-col">

<div>

### 📜 Procedural vs 🎯 POO

| Aspecto | Procedural | POO |
|---------|-----------|-----|
| Datos | Separados | Unidos |
| Mantenimiento | Difícil | Modular |
| Escalabilidad | Limitada | Fácil |

### 💡 Ventajas POO

- Código modular
- Reutilizable
- Fácil mantenimiento
- Modela mundo real

</div>

<div>

### 🏛️ Tres Pilares POO

```
┌────────────────────────────────┐
│   PILARES DE LA POO             │
├────────┬───────────┬─────────────┤
│ ENCAPS │ HERENCIA  │ POLIMORFISMO│
│ (Hoy)  │ (Clase 3) │ (Clase 3)   │
├────────┼───────────┼─────────────┤
│ Ocultar│ Reutilizar│ Una interfaz│
│ datos  │ código    │ múltiples   │
│        │           │ formas      │
└────────┴───────────┴─────────────┘
```

</div>

</div>

---

## Clase vs Objeto: Analogía

<div class="two-col">

<div>

### 🎨 CLASE = Molde/Plantilla

- Define estructura
- Especifica atributos
- Define comportamientos
- NO ocupa memoria
- Es el "tipo"

```csharp
class Galleta {
    public string Sabor;
    public double Diametro;
    public void Hornear() { }
}
```

</div>

<div>

### 🍪 OBJETO = Instancia

- Creado de una clase
- Ocupa memoria (heap)
- Tiene valores específicos
- Ejecuta métodos

```csharp
Galleta g1 = new Galleta();
g1.Sabor = "Chocolate";
g1.Diametro = 5.5;
g1.Hornear();
```

</div>

</div>

---

## Clase vs Objeto: Comparativa

| Aspecto | Clase (Molde) | Objeto (Instancia) |
|---------|---------------|-------------------|
| **Naturaleza** | Abstracta | Concreta |
| **Memoria** | No ocupa | Ocupa heap |
| **Cantidad** | Una definición | Múltiples |
| **Valores** | Define qué tendrá | Tiene valores |
| **Declaración** | `class Galleta` | `new Galleta()` |

<div class="info-box">

**💡 Analogía:** Clase = Receta | Objeto = Galleta horneada

</div>

---

## Representación en Memoria

```
┌─────────────────────────────────────────────────────────────┐
│                    MEMORIA                                  │
├───────────────────┬──────────────────────────────────────────┤
│      STACK        │              HEAP                        │
│  (Referencias)    │         (Objetos reales)                 │
├───────────────────┼──────────────────────────────────────────┤
│ ┌──────────────┐  │  ┌─────────────────────────────┐        │
│ │   est1       │──┼─→│      Objeto Estudiante      │        │
│ │   0x7F3A...  │  │  │  ┌─────────────────────┐    │        │
│ └──────────────┘  │  │  │ Nombre: "María"     │    │        │
│                   │  │  │ Código: "2024001"   │    │        │
│ ┌──────────────┐  │  │  │ Edad: 20            │    │        │
│ │   est2       │──┼─→│  │ Promedio: 4.2       │    │        │
│ │   0x8B2C...  │  │  │  └─────────────────────┘    │        │
│ └──────────────┘  │  └─────────────────────────────┘        │
│                   │                                         │
│ Variables =       │ Objetos = datos reales en heap          │
│ direcciones (4-8B)│                                         │
└───────────────────┴──────────────────────────────────────────┘
```

---

## 2. Clases en C#: Estructura

```csharp
[modificador] class NombreClase
{
    // CAMPOS (atributos)
    [modificador] tipo nombreCampo;

    // PROPIEDADES (encapsulamiento)
    [modificador] tipo NombreProp { get; set; }

    // CONSTRUCTORES
    [modificador] NombreClase([params])
    {
        // inicialización
    }

    // MÉTODOS (comportamientos)
    [modificador] tipoRetorno NombreMetodo([params])
    {
        // código
    }
}
```

| Elemento | Propósito |
|----------|-----------|
| `namespace` | Agrupa clases |
| `class` | Define tipo |
| `field` | Dato interno |
| `property` | Acceso controlado |
| `method` | Comportamiento |

---

## Ejemplo: Clase Estudiante

<div class="two-col">

<div>

### 📋 Código C#

```csharp
public class Estudiante
{
    // Campos (⚠️ público)
    public string nombre;
    public string codigo;
    public int edad;
    public double promedio;

    // Método
    public void MostrarInfo()
    {
        Console.WriteLine(
            $"Nombre: {nombre}");
        Console.WriteLine(
            $"Código: {codigo}");
        Console.WriteLine(
            $"Edad: {edad}");
        Console.WriteLine(
            $"Promedio: {promedio}");
    }
}
```

</div>

<div>

### 🔍 Análisis

| Elemento | Descripción |
|----------|-------------|
| `public class` | Clase accesible |
| `string nombre` | Campo público |
| `void` | Sin retorno |

<div class="warning-box">

**⚠️ Campos públicos = mala práctica**

- Sin validación
- Cualquiera modifica
- Difícil mantener

</div>

</div>

</div>

---

## Instanciación con new

```csharp
// CREAR OBJETO
Estudiante est1 = new Estudiante();

// ASIGNAR VALORES
est1.nombre = "María López";
est1.codigo = "2024001";
est1.edad = 20;
est1.promedio = 4.2;

// USAR MÉTODOS
est1.MostrarInfo();

// MÁS OBJETOS (independientes)
Estudiante est2 = new Estudiante();
est2.nombre = "Carlos Ruiz";
est2.MostrarInfo();
```

---

## 3. Encapsulamiento

<div class="two-col">

<div>

### 🔒 ¿Qué es?

Ocultar datos internos y exponer solo lo necesario.

```
┌─────────────────────────────┐
│   INTERFAZ PÚBLICA          │
│  ✅ Propiedades (get/set)   │
│  ✅ Métodos públicos        │
│  ══════════════════════════ │
│   IMPLEMENTACIÓN PRIVADA    │
│  🔒 Campos privados         │
│  🔒 Lógica de validación    │
└─────────────────────────────┘
```

### 💡 Beneficios

| Beneficio | Descripción |
|-----------|-------------|
| Protección | Datos no modificables |
| Validación | Control de valores |
| Flexibilidad | Cambiar impl. interna |
| Abstracción | Usuario no sabe cómo |

</div>

<div>

### ❌ Sin vs ✅ Con Encapsulamiento

```csharp
// ❌ SIN (Frágil)
public class Cuenta
{
    public double saldo;  // ¡Peligroso!
}
cuenta.saldo = -1000;     // Válido

// ✅ CON (Robusto)
public class Cuenta
{
    private double _saldo;

    public void Depositar(double monto)
    {
        if (monto <= 0)
            throw new ArgumentException(
                "Monto debe ser positivo");
        _saldo += monto;
    }
}
cuenta.Depositar(-1000);  // Excepción
```

</div>

</div>

---

## Modificadores de Acceso

| Modificador | ¿Quién accede? | Uso típico |
|-------------|----------------|------------|
| **public** | Todos | API pública |
| **private** | Solo la clase | Campos internos |
| **protected** | Clase + hijas | Herencia |
| **internal** | Mismo proyecto | Clases internas |

<div class="info-box">

**💡 Por defecto:** Campos son `private`, clases son `internal`

</div>

---

## 4. Propiedades en C#

<div class="two-col">

<div>

### ❌ TRADICIONAL (Java)

```csharp
private string nombre;

public string GetNombre()
{
    return nombre;
}

public void SetNombre(string v)
{
    nombre = v;
}

// Uso verboso
p.SetNombre("María");
```

### ❌ Problemas

- Sintaxis verbosa
- Rompe fluidez
- Paréntesis everywhere

</div>

<div>

### ✅ MODERNO C#

```csharp
private string _nombre;

public string Nombre
{
    get { return _nombre; }
    set { _nombre = value; }
}

// Uso natural
p.Nombre = "María";
```

### ✅ Ventajas

- Sintaxis limpia
- Mantiene encapsulamiento
- Parece campo, es método
- Permite lógica

</div>

</div>

---

## Anatomía de una Propiedad

```
┌─────────────────────────────────────────────────────────┐
│          ANATOMÍA DE UNA PROPIEDAD                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   backing field      propiedad      uso                  │
│   ┌──────────┐      ┌──────────┐      ┌──────────┐    │
│   │ private   │      │ public   │      │ obj.Nom  │    │
│   │ string    │←────→│ string   │←────→│ = "Ana"  │    │
│   │ _nombre   │      │ Nombre   │      └──────────┘    │
│   └──────────┘      │ { get;   │      Console.WriteLine│
│         ↑          │   set; } │      (obj.Nombre);    │
│    Almacena         └──────────┘                       │
│                                                         │
│   value = palabra clave con el valor a asignar         │
└─────────────────────────────────────────────────────────┘
```

<div class="info-box">

**💡 Las propiedades son sintactic sugar para encapsulamiento**

</div>

---

## Tipos de Propiedades

<div class="two-col">

<div>

### 📝 Tipos

| Tipo | Sintaxis | Uso |
|------|----------|-----|
| **Auto** | `{ get; set; }` | Sin validación |
| **Con field** | Full get/set | Con lógica |
| **Solo lectura** | `{ get; }` | Calculado |
| **Init-only** | `{ get; init; }` | Constructor |

```csharp
// 1. Autoimplementada
public double Precio { get; set; }

// 2. Solo lectura
public double PrecioFinal
{
    get { return Precio * 1.19; }
}

// 3. Con valor default
public double IVA { get; set; } = 0.19;
```

</div>

<div>

### ✅ Con Validación

```csharp
private string _nombre;

public string Nombre
{
    get { return _nombre; }
    set
    {
        if (!string.IsNullOrWhiteSpace(value))
            _nombre = value;
        else
            throw new ArgumentException(
                "Nombre no puede estar vacío");
    }
}

private int _edad;

public int Edad
{
    get { return _edad; }
    set
    {
        if (value >= 0 && value <= 120)
            _edad = value;
        else
            throw new ArgumentOutOfRangeException();
    }
}
```

</div>

</div>

---

## 5. Constructores

<div class="two-col">

<div>

### 🎯 ¿Qué es?

Método especial que se ejecuta al crear un objeto.

### 📋 Tipos

| Tipo | Descripción |
|------|-------------|
| **Default** | Sin parámetros |
| **Parametrizado** | Con parámetros |
| **Cadena** | Llama a otro |

```csharp
public Estudiante()
{
    Nombre = "Sin nombre";
    Edad = 18;
}

public Estudiante(string n, int e)
{
    Nombre = n;
    Edad = e;
}
```

</div>

<div>

### 💻 Uso

```csharp
// Default
Estudiante e1 = new Estudiante();

// Parametrizado
Estudiante e2 = new Estudiante(
    "María", 20);

// Object initializer
Estudiante e3 = new Estudiante
{
    Nombre = "Carlos",
    Edad = 22,
    Promedio = 4.5
};
```

### 🔒 Solo Lectura

```csharp
public string Codigo { get; }

public Estudiante(string cod)
{
    Codigo = cod;  // Solo en constructor
}
// e.Codigo = "otro";  // ❌ Error
```

</div>

</div>

---

## Clase Completa: Estudiante

```csharp
public class Estudiante
{
    // Propiedades autoimplementadas
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    public double Promedio { get; set; }

    // Constructor default
    public Estudiante()
    {
        Nombre = "Sin nombre";
        Codigo = "0000000";
        Edad = 18;
        Promedio = 0.0;
    }

    // Constructor parametrizado
    public Estudiante(string n, string c, int e)
    {
        Nombre = n;
        Codigo = c;
        Edad = e;
        Promedio = 0.0;
    }

    // Métodos de negocio
    public bool Aprobo() => Promedio >= 3.0;

    public string Estado() =>
        Aprobo() ? "APROBADO" : "REPROBADO";

    public void MostrarInfo()
    {
        Console.WriteLine($"📚 {Nombre} ({Codigo})");
        Console.WriteLine($"   Edad: {Edad}");
        Console.WriteLine($"   Promedio: {Promedio:F2}");
        Console.WriteLine($"   Estado: {Estado()}");
    }
}
```

---

## Static vs Instance

<div class="two-col">

<div>

### 🔄 STATIC (Compartido)

- Una copia para TODOS
- Acceso desde la clase
- Usa `static` keyword

```csharp
public class Contador
{
    public static int Global = 0;
    public int Instancia = 0;

    public Contador()
    {
        Global++;     // Todos
        Instancia++; // Este
    }
}
```

</div>

<div>

### 💻 Uso

```csharp
Contador c1 = new Contador(); // G=1, I=1
Contador c2 = new Contador(); // G=2, I=1
Contador c3 = new Contador(); // G=3, I=1

// Static: desde clase
Console.WriteLine(Contador.Global); // 3

// Instance: desde objeto
Console.WriteLine(c1.Instancia);   // 1
Console.WriteLine(c2.Instancia);   // 1
```

**Static:** contador global<br>
**Instance:** valor único por objeto

</div>

</div>

---

## class vs struct

| Aspecto | class | struct |
|---------|-------|--------|
| **Tipo** | Reference | Value |
| **Ubicación** | Heap | Stack |
| **Asignación** | Copia referencia | Copia valor |
| **Uso** | Objetos grandes | Datos pequeños |
| **Herencia** | Soporta | No |

```csharp
// CLASS (Reference)
Persona p1 = new Persona("Juan");
Persona p2 = p1;      // Misma referencia
p2.Nombre = "María";  // p1 también cambia

// STRUCT (Value)
Punto pt1 = new Punto(10, 20);
Punto pt2 = pt1;      // Copia independiente
pt2.X = 50;          // pt1.X sigue siendo 10
```

---

## 6. Práctica: Sistema Estudiantil

<div class="two-col">

<div>

### 🎯 Objetivo

App que gestione estudiantes con POO.

### 📋 Pasos

1. Crear proyecto Console
2. Agregar clase `Estudiante`
3. Implementar programa principal
4. Crear 3+ estudiantes
5. Mostrar información

### 🧪 Datos Prueba

| Nombre | Código | Edad | Promedio |
|--------|--------|------|----------|
| M. López | 2024001 | 20 | 4.2 |
| C. Ruiz | 2024002 | 22 | 2.8 |
| A. Mart. | 2024003 | 19 | 3.5 |

</div>

<div>

### 💻 Código Main

```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<Estudiante> estudiantes
            = new List<Estudiante>();

        estudiantes.Add(
            new Estudiante("María", "2024001", 20)
            { Promedio = 4.2 });

        estudiantes.Add(
            new Estudiante("Carlos", "2024002", 22)
            { Promedio = 2.8 });

        Console.WriteLine(
            "=== ESTUDIANTES ===\n");

        foreach (var est in estudiantes)
        {
            est.MostrarInfo();
            Console.WriteLine();
        }
    }
}
```

</div>

</div>

---

## Resumen de la Clase

<div class="compact-list">

<div>

### 📚 Conceptos

| Tema | Descripción |
|------|-------------|
| **Clase** | Plantilla |
| **Objeto** | Instancia |
| **Campo** | Dato |
| **Propiedad** | Encapsulamiento |
| **Constructor** | Inicialización |
| **Encapsulamiento** | Ocultar datos |

### 🎯 Habilidades

```
✅ Definir clases C#
✅ Crear objetos con new
✅ Aplicar encapsulamiento
✅ Usar propiedades
✅ Implementar constructores
```

</div>

<div>

### 📝 Ejercicios

**1. Producto**
- Código (solo lectura)
- Nombre (no vacío)
- Precio > 0, Stock >= 0
- `CalcularInventario()`

**2. CuentaBancaria**
- Saldo privado
- `Depositar()`, `Retirar()`
- Validar negativo

**3. Tienda (Static)**
- Contador estático
- Total productos

**4. 🌟 Biblioteca**
```
Libro: ISBN, título, autor
Usuario: código, nombre
Prestamo: fechas, estado
→ Validaciones completas
```

</div>

</div>

---

## 🎓 Próxima Clase: Herencia y Polimorfismo

### Temas Clase 3

- ✅ Herencia: Base y derivada
- ✅ Palabra `base`
- ✅ Polimorfismo: virtual/override
- ✅ Clases/métodos abstractos
- ✅ Principio Liskov

### 📖 Preparación

**Repasa conceptos POO**

**Piensa en ejemplos:**
- Vehículo → Carro, Moto, Bus
- Animal → Perro, Gato, Pájaro
- Figura → Círculo, Rectángulo

**💡 Pregunta:** ¿Cómo hacer que diferentes tipos de vehículos tengan `Mover()` con comportamientos diferentes?

---

# ¡Gracias!
## ¿Preguntas?

<div class="info-box" style="text-align: center;">

**UNAULA - Ingeniería Informática - 2026-I**

</div>
