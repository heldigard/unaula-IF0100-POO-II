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
    font-size: 0.85em;
  }
  pre {
    font-size: 0.7em;
  }
---

<!-- _class: lead -->

# Clases, Objetos y Encapsulamiento

**IF0100 - Lenguaje de Programación OO II**  
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 1 - Clase 2**

---

## Objetivos y Agenda

| 🎯 Objetivos | 📋 Agenda (90 min) |
|-------------|-------------------|
| 1. Definir clases y objetos | 10' Repaso POO |
| 2. Aplicar encapsulamiento | 20' Clases y Objetos |
| 3. Usar propiedades get/set | 20' Encapsulamiento |
| 4. Implementar constructores | 20' Propiedades |
| 5. Campos vs Propiedades | 15' Constructores + 5' Práctica |

---

## 1. Repaso: Programación Orientada a Objetos

### 📜 Procedural vs 🎯 POO

| Aspecto | Procedural | POO |
|---------|-----------|-----|
| Datos | Separados | Unidos |
| Mantenimiento | Difícil | Modular |
| Escalabilidad | Limitada | Fácil |

### 💡 Ventajas POO

- ✅ Código modular
- ✅ Reutilizable
- ✅ Fácil mantenimiento
- ✅ Modela mundo real

---

## Los Tres Pilares de la POO

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

**Hoy:** Encapsulamiento | **Próxima clase:** Herencia y Polimorfismo

---

## Clase vs Objeto: Analogía

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

---

## Clase vs Objeto: Comparativa

| Aspecto | Clase (Molde) | Objeto (Instancia) |
|---------|---------------|-------------------|
| **Naturaleza** | Abstracta | Concreta |
| **Memoria** | No ocupa | Ocupa heap |
| **Cantidad** | Una definición | Múltiples |
| **Valores** | Define qué tendrá | Tiene valores |
| **Declaración** | `class Galleta` | `new Galleta()` |

**💡 Analogía:** Clase = Receta | Objeto = Galleta horneada

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
│ direcciones       │                                         │
└───────────────────┴──────────────────────────────────────────┘
```

---

## 2. Clases en C#: Estructura

### 📋 Anatomía de Clase

| Elemento | Propósito |
|----------|-----------|
| `namespace` | Agrupa clases |
| `class` | Define tipo |
| `field` | Dato interno |
| `property` | Acceso controlado |
| `method` | Comportamiento |

### 🔑 Modificadores

- `public` - Accesible desde fuera
- `private` - Solo interno
- `static` - Compartido por todos

### 💻 Plantilla General

```csharp
public class NombreClase
{
    // Campos
    private tipo _campo;

    // Propiedades
    public tipo Prop { get; set; }

    // Constructor
    public NombreClase(params) { }

    // Métodos
    public tipo Metodo(params)
    {
        // código
    }
}
```

---

## Ejemplo: Clase Estudiante

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
        Console.WriteLine($"Nombre: {nombre}");
        Console.WriteLine($"Código: {codigo}");
        Console.WriteLine($"Edad: {edad}");
        Console.WriteLine($"Promedio: {promedio}");
    }
}
```

### 🔍 Análisis

| Elemento | Descripción |
|----------|-------------|
| `public class` | Clase accesible |
| `string nombre` | Campo público |
| `void` | Sin retorno |

### ⚠️ Problema: Campos públicos = mala práctica

- Sin validación
- Cualquiera modifica
- Difícil mantener

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

---

## Sin vs Con Encapsulamiento

### ❌ SIN (Frágil)

```csharp
public class Cuenta
{
    public double saldo;  // ¡Peligroso!
}
cuenta.saldo = -1000;     // Válido
```

### ✅ CON (Robusto)

```csharp
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

---

## Modificadores de Acceso

| Modificador | ¿Quién accede? | Uso típico |
|-------------|----------------|------------|
| **public** | Todos | API pública |
| **private** | Solo la clase | Campos internos |
| **protected** | Clase + hijas | Herencia |
| **internal** | Mismo proyecto | Clases internas |

**💡 Por defecto:** Campos son `private`, clases son `internal`

---

## 4. Propiedades en C#

### ❌ TRADICIONAL (Java-style)

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

**Problemas:**
- Sintaxis verbosa
- Rompe fluidez
- Paréntesis everywhere

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

**Ventajas:**
- Sintaxis limpia
- Mantiene encapsulamiento
- Parece campo, es método
- Permite lógica

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

**💡 Las propiedades son syntactic sugar para encapsulamiento**

---

## Tipos de Propiedades

### 📝 Tipos de Propiedades

| Tipo | Sintaxis | Uso |
|------|----------|-----|
| **Auto** | `{ get; set; }` | Sin validación |
| **Con field** | Full get/set | Con lógica |
| **Solo lectura** | `{ get; }` | Calculado |
| **Init-only** | `{ get; init; }` | Constructor |

### 💻 Ejemplos

```csharp
// 1. Autoimplementada
public double Precio { get; set; }

// 2. Solo lectura
public double PrecioFinal
{
    get { return Precio * 1.19; }
}

// 3. Con default
public double IVA { get; set; } = 0.19;
```

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

---

## 5. Constructores

### 🎯 ¿Qué es?

Método especial que se ejecuta al crear un objeto.

### 📋 Tipos

| Tipo | Descripción |
|------|-------------|
| **Default** | Sin parámetros |
| **Parametrizado** | Con parámetros |
| **Cadena** | Llama a otro |

### 💻 Definición

```csharp
// Constructor default
public Estudiante()
{
    Nombre = "Sin nombre";
    Edad = 18;
}

// Constructor parametrizado
public Estudiante(string n, int e)
{
    Nombre = n;
    Edad = e;
}
```

### 🔧 Uso

```csharp
// Default
Estudiante e1 = new Estudiante();

// Parametrizado
Estudiante e2 = new Estudiante("María", 20);

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

---

## Clase Completa: Estudiante

### 📋 Propiedades

```csharp
public class Estudiante
{
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    public double Promedio { get; set; }
```

### 🔧 Constructores

```csharp
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
```

### 💡 Métodos de Negocio

```csharp
    // Métodos
    public bool Aprobo() =>
        Promedio >= 3.0;

    public string Estado() =>
        Aprobo() ? "APROBADO" : "REPROBADO";

    public void MostrarInfo()
    {
        Console.WriteLine($"📚 {Nombre}");
        Console.WriteLine($"   Edad: {Edad}");
        Console.WriteLine($"   Prom: {Promedio:F2}");
        Console.WriteLine($"   Est: {Estado()}");
    }
}
```

### 🎯 Uso

```csharp
var est = new Estudiante("María", "2024001", 20);
est.Promedio = 4.2;
est.MostrarInfo();
```

---

## Static vs Instance

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

**Static:** contador global  
**Instance:** valor único por objeto

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

        Console.WriteLine("=== ESTUDIANTES ===");

        foreach (var est in estudiantes)
        {
            est.MostrarInfo();
            Console.WriteLine();
        }
    }
}
```

### 🎨 Salida

```
=== ESTUDIANTES ===
📚 María (2024001)
   Edad: 20
   Prom: 4.20
   Est: APROBADO
```

---

## Resumen de la Clase

### 📚 Conceptos Clave

| Tema | Descripción |
|------|-------------|
| **Clase** | Plantilla de objetos |
| **Objeto** | Instancia concreta |
| **Campo** | Dato interno (privado) |
| **Propiedad** | Encapsulamiento (get/set) |
| **Constructor** | Inicialización de objetos |
| **Encapsulamiento** | Ocultar datos, exponer comportamiento |

### 🎯 Habilidades Adquiridas

- ✅ Definir clases C#
- ✅ Crear objetos con new
- ✅ Aplicar encapsulamiento
- ✅ Usar propiedades
- ✅ Implementar constructores

### 📝 Ejercicios Propuestos

**1. Producto**
- Código (solo lectura)
- Nombre (no vacío)
- Precio > 0, Stock >= 0
- `CalcularInventario()`

**2. CuentaBancaria**
- Saldo privado
- `Depositar()`, `Retirar()`
- Validar negativos

**3. 🌟 Biblioteca**  
Libro: ISBN, título, autor  
Usuario: código, nombre  
Prestamo: fechas, estado  
→ Validaciones completas

---

## 🎓 Próxima Clase: Herencia y Polimorfismo

### Temas Clase 3

- ✅ Herencia: Clases base y derivadas
- ✅ Palabra clave `base`
- ✅ Polimorfismo: virtual/override
- ✅ Clases/métodos abstractos
- ✅ Principio de Liskov

### 📖 Preparación

**Repasa conceptos POO:**
- ¿Qué es la herencia?
- ¿Qué es el polimorfismo?

**Piensa en ejemplos:**
- Vehículo → Carro, Moto, Bus
- Animal → Perro, Gato, Pájaro
- Figura → Círculo, Rectángulo

**💡 Pregunta:** ¿Cómo hacer que diferentes tipos de vehículos tengan `Mover()` con comportamientos diferentes?

---

<!-- _class: lead -->

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
