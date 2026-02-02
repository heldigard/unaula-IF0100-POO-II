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

<div class="columns">
<div>

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

</div>
<div>

### Los Tres Pilares

<figure>
<svg width="100%" viewBox="0 0 720 220" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="pillars">
  <title id="pillars">Pilares de la Programación Orientada a Objetos</title>
  <style>
    .pillar{fill:#0b2d6b;rx:8}
    .ph{fill:#fff;font:700 13px Arial, sans-serif}
    .ps{fill:#e6eefc;font:12px Arial, sans-serif}
  </style>
  <rect x="40" y="40" width="200" height="140" rx="8" fill="#0b2d6b"/>
  <text x="140" y="68" text-anchor="middle" class="ph">ENCAPSULAMIENTO</text>
  <text x="140" y="96" text-anchor="middle" class="ps">Ocultar datos</text>

  <rect x="260" y="40" width="200" height="140" rx="8" fill="#0b2d6b"/>
  <text x="360" y="68" text-anchor="middle" class="ph">HERENCIA</text>
  <text x="360" y="96" text-anchor="middle" class="ps">Reutilizar código</text>

  <rect x="480" y="40" width="200" height="140" rx="8" fill="#0b2d6b"/>
  <text x="580" y="68" text-anchor="middle" class="ph">POLIMORFISMO</text>
  <text x="580" y="96" text-anchor="middle" class="ps">Una interfaz, múltiples formas</text>
</svg>
<figcaption>Pilares de la POO: encapsulamiento, herencia y polimorfismo — cada uno con su propósito.</figcaption>
</figure>

**Hoy:** Encapsulamiento  
**Próxima clase:** Herencia y Polimorfismo

</div>
</div>

---

## Clase vs Objeto

<div class="columns">
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
Galleta g1 = new Galleta();  // new: asigna memoria + llama constructor
g1.Sabor = "Chocolate";
g1.Diametro = 5.5;
g1.Hornear();
```

> 💡 **Keyword `new`**: Asigna memoria en el heap para el objeto y ejecuta su constructor. Retorna una referencia al objeto creado.

### 📖 ¿Qué es la Instanciación?

**Instanciación** es el proceso de crear un objeto concreto a partir de una clase. Es como "hornear" una galleta usando la receta (clase). Cada instancia tiene sus propios valores independientes.

```csharp
// Una clase, múltiples instancias
Galleta g1 = new Galleta(); // Instancia 1
Galleta g2 = new Galleta(); // Instancia 2
g1.Sabor = "Chocolate";      // g1 tiene Chocolate
g2.Sabor = "Vainilla";       // g2 tiene Vainilla (independientes)
```

</div>
</div>

### 📊 Comparativa

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

<div class="columns">
<div>

### 📚 STACK (Referencias)

- Almacena variables locales
- Contiene direcciones de memoria
- Limpieza automática al salir del método
- Tipo valor: datos directos

### 🏠 HEAP (Objetos)

- Almacena objetos reales
- Datos accedidos mediante referencias
- Garbage Collector limpia
- Tipo referencia: objetos complejos

</div>
<div>

<figure>
<svg width="100%" viewBox="0 0 820 220" preserveAspectRatio="xMidYMid meet" role="img" aria-labelledby="memoryTitle">
  <title id="memoryTitle">Representación de Stack y Heap</title>
  <style>
    .sbox{fill:#eef2ff;stroke:#dbeafe;rx:8}
    .hbox{fill:#fff1f2;stroke:#fbcfce;rx:8}
    .t{font:600 12px Arial, sans-serif;fill:#0b2d6b}
    .mut{font:12px Arial, sans-serif;fill:#475569}
    .arrow{stroke:#0b2d6b;stroke-width:2;marker-end:url(#arrow)}
  </style>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="#0b2d6b"/></marker>
  </defs>
  <!-- Stack -->
  <rect x="20" y="24" width="300" height="172" rx="8" class="sbox"/>
  <text x="170" y="44" text-anchor="middle" class="t">STACK (Referencias)</text>
  <rect x="40" y="68" width="120" height="36" rx="6" fill="#fff" stroke="#cfe2ff"/>
  <text x="100" y="90" text-anchor="middle" class="mut">est1
0x7F3A...</text>
  <rect x="40" y="116" width="120" height="36" rx="6" fill="#fff" stroke="#cfe2ff"/>
  <text x="100" y="138" text-anchor="middle" class="mut">est2
0x8B2C...</text>
  <!-- Heap -->
  <rect x="380" y="24" width="400" height="172" rx="8" class="hbox"/>
  <text x="580" y="44" text-anchor="middle" class="t">HEAP (Objetos reales)</text>
  <rect x="420" y="72" width="320" height="112" rx="8" fill="#fff" stroke="#ffd6e0"/>
  <text x="580" y="96" text-anchor="middle" class="mut">Obj Estudiante
Nombre: “María”
Cód: “2024001”
Edad: 20 • Prom: 4.2</text>
  <!-- Arrows -->
  <path d="M160 86 L420 96" class="arrow" />
  <path d="M160 134 L420 126" class="arrow" />
</svg>
<figcaption>Ilustración: variables en stack contienen referencias (direcciones) que apuntan a objetos reales almacenados en el heap.</figcaption>
</figure>

**💡 Las variables en stack son referencias a objetos en heap**

### 📖 Términos Clave de Memoria

- **Dirección de memoria**: Número hexadecimal que identifica una posición específica en la memoria RAM (como `0x7F3A...`). Es como la dirección de una casa.
- **Referencia**: Variable que contiene una dirección de memoria. No contiene el objeto en sí, sino "dónde está" el objeto.
- **Garbage Collector**: Componente del .NET que detecta y libera memoria de objetos que ya no se usan (sin referencias activas). Se ejecuta automáticamente cuando hay presión de memoria.

> ⚠️ **Error común:** Creer que una referencia ES el objeto. No - la referencia es solo un "puntero" a donde está el objeto.

</div>
</div>

---

## 2. Clases en C#: Estructura

### 📋 Anatomía de Clase

| Elemento | Propósito |
|----------|-----------|
| `namespace` | Agrupa clases relacionadas |
| `class` | Define tipo/plantilla |
| `field` | Dato interno (variable) |
| `property` | Acceso controlado a datos |
| `method` | Comportamiento/función de la clase |
| `constructor` | Inicialización de objetos |

### 📖 Definiciones Clave

- **Method (Método)**: Función que pertenece a una clase. Define el comportamiento de los objetos de esa clase.
- **Field (Campo)**: Variable declarada a nivel de clase. Almacena datos del objeto.
- **Constructor**: Método especial con el mismo nombre que la clase. Se ejecuta al crear un objeto con `new`.

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

## Ejemplo: Clase Estudiante e Instanciación

<div class="columns">
<div>

### 📋 Definición de Clase

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

⚠️ **Problema:** Campos públicos = mala práctica (sin validación)

</div>
<div>

### 🚀 Instanciación con `new`

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

</div>
</div>

---

## 3. Encapsulamiento

### 🔒 ¿Qué es?

**Encapsulamiento** es ocultar datos internos y exponer solo lo necesario a través de una interfaz pública.

**Interfaz pública** = Conjunto de métodos y propiedades accesibles desde fuera de la clase. Es como el panel de control de un dispositivo - solo ves los botones que puedes usar, no los circuitos internos.

```csharp
// Interfaz pública (visible)
cuenta.Depositar(100);  // ✅ Puede usar
cuenta._saldo = 1000;    // ❌ Error: _saldo es privado
```

<div class="columns">
<div>

### ❌ SIN Encapsulamiento (Frágil)

```csharp
public class Cuenta
{
    public double saldo;  // ¡Peligroso!
}

// Uso
cuenta.saldo = -1000;     // ⚠️ Válido pero incorrecto
```

**Problemas:**
- Sin validación
- Cualquiera modifica
- Difícil mantener

</div>
<div>

### ✅ CON Encapsulamiento (Robusto)

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

// Uso
cuenta.Depositar(-1000);  // ❌ Excepción controlada
```

**Beneficios:**
- Validación de datos
- Protección interna
- Flexibilidad de implementación

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

**💡 Por defecto:** Campos son `private`, clases son `internal`

---

## 4. Propiedades en C#

<div class="columns">
<div>

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

**Problemas:** Sintaxis verbosa, rompe fluidez

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

**Ventajas:** Sintaxis limpia, mantiene encapsulamiento

</div>
<div>

### 🏗️ Anatomía de una Propiedad

```
┌─────────────────────────────────────┐
│     ANATOMÍA DE PROPIEDAD           │
├─────────────────────────────────────┤
│                                     │
│  backing field    propiedad   uso   │
│  ┌──────────┐    ┌──────────┐ ┌───┐ │
│  │ private  │    │ public   │←│obj│ │
│  │ _nombre  │←──→│ Nombre   │ │.N │ │
│  └──────────┘    │ {get;set}│ └───┘ │
│       ↑          └──────────┘       │
│   Almacena                          │
│                                     │
│   `value` = valor a asignar         │
└─────────────────────────────────────┘
```

### 📖 Términos Clave

- **Backing field**: Variable privada que almacena el valor real de la propiedad (por convención con `_` al inicio)
- **Syntactic sugar**: Azúcar sintáctica - sintaxis más limpia que el compilador convierte a código más verboso
- **`value`**: Palabra clave que representa el valor que se está asignando a la propiedad

**💡 Las propiedades son *syntactic sugar* para encapsulamiento**

</div>
</div>

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

### 📖 Términos Clave de Propiedades

- **Auto-implemented property**: Propiedad donde el compilador genera automáticamente el backing field. `{ get; set; }` se convierte internamente en un campo privado con get/set.

```csharp
// Lo que escribes:
public string Nombre { get; set; }

// Lo que el compilador genera:
private string <Nombre>k__BackingField;
public string Nombre { get { return <Nombre>k__BackingField; } set { <Nombre>k__BackingField = value; } }
```

- **Expression-bodied member** (`=>`): Sintaxis concisa para métodos o propiedades que son una sola expresión.

```csharp
// Forma tradicional
public bool Aprobo()
{
    return Promedio >= 3.0;
}

// Expression-bodied (más conciso)
public bool Aprobo() => Promedio >= 3.0;
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

### 🚨 ¿Qué son las Excepciones?

Las excepciones son errores que ocurren durante la ejecución del programa:

| Excepción | Cuándo usarla |
|-----------|---------------|
| `ArgumentException` | El argumento proporcionado no es válido |
| `ArgumentOutOfRangeException` | El valor está fuera del rango permitido |
| `NullReferenceException` | Se intenta usar algo que es null (evitarla validando) |

**`throw`**: Palabra clave que "lanza" una excepción, interrumpiendo el flujo normal del programa. El control pasa al bloque `catch` más cercano (o el programa termina si no hay manejo).

**Beneficio de lanzar excepciones:** El programa no continúa con datos inválidos - falla rápido y con un mensaje claro.

> ⚠️ **Error común:** No capturar excepciones esperadas - el programa se cerrará inesperadamente en producción.

---

## 5. Constructores y Clase Completa

### 🎯 ¿Qué es un Constructor?

Método especial que se ejecuta al crear un objeto.

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Default** | Sin parámetros | `new Estudiante()` |
| **Parametrizado** | Con parámetros | `new Estudiante("Ana", 20)` |
| **Object Initializer** | Sintaxis `{ }` | `new Estudiante { Nombre = "Ana" }` |

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
    
    public string Estado() => Aprobo() ? "APROBADO" : "REPROBADO";

    public void MostrarInfo()
    {
        Console.WriteLine($"📚 {Nombre} ({Codigo})");
        Console.WriteLine($"   Edad: {Edad} | Prom: {Promedio:F2}");
        Console.WriteLine($"   Estado: {Estado()}");
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

<div class="columns">
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
        // List<T> es una colección genérica que crece dinámicamente
        // T se reemplaza por el tipo de datos (en este caso: Estudiante)
        var estudiantes = new List<Estudiante>();

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

### 🎨 Salida Esperada

```
=== ESTUDIANTES ===
📚 María (2024001)
   Edad: 20 | Prom: 4.20
   Estado: APROBADO
```

</div>
</div>

---

## Resumen de la Clase (1/2)

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

---

## 📝 Ejercicios Propuestos (2/2)

<div class="columns">
<div>

### 1. Producto

- Código (solo lectura)
- Nombre (no vacío)
- Precio > 0, Stock >= 0
- `CalcularInventario()`

### 2. CuentaBancaria

- Saldo privado
- `Depositar()`, `Retirar()`
- Validar negativos

</div>
<div>

### 3. 🌟 Biblioteca

**Libro:** ISBN, título, autor
**Usuario:** código, nombre
**Prestamo:** fechas, estado

→ Validaciones completas

</div>
</div>

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

---

## 💡 Pregunta de Reflexión

### ¿Cómo hacer que diferentes tipos de vehículos tengan `Mover()` con comportamientos diferentes?

```csharp
// ¿Cómo diseñar esto?
Vehiculo v = new Carro();   // v.Mover() = "Rodando"
Vehiculo v2 = new Moto();   // v2.Mover() = "Rodando"
Vehiculo v3 = new Bus();    // v3.Mover() = "Rodando con pasajeros"

// ¿Qué mecanismo permite esto?
```

### 📝 Requisitos para la próxima clase

- ✅ Tarea completada
- ✅ Ejercicios de práctica resueltos
- ✅ Repaso de POO básico

---

<!-- _class: lead -->

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
