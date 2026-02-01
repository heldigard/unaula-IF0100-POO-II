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

# Clases, Objetos y Encapsulamiento

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Definir** clases y crear objetos en C#
2. **Aplicar** el principio de encapsulamiento
3. **Utilizar** propiedades (getters/setters) correctamente
4. **Implementar** constructores y sobrecarga de constructores
5. **Distinguir** entre campos, propiedades y métodos

**Duración:** 90 minutos

---

## Agenda

1. Repaso: ¿Qué es POO? (10 min)
2. Clases y Objetos en C# (20 min)
3. Encapsulamiento y Modificadores de Acceso (20 min)
4. Propiedades en C# (20 min)
5. Constructores (15 min)
6. Práctica: Clase Estudiante (5 min)

---
## 1. Repaso: Programación Orientada a Objetos

### Evolución de la Programación

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

**📜 Programación Procedural (Años 70-80)**

```csharp
// Datos separados de las funciones
string[] nombres = {"Juan", "María"};
int[] edades = {25, 30};

void ImprimirPersona(int index) {
    Console.WriteLine(nombres[index] + 
                      " tiene " + 
                      edades[index] + " años");
}
```

**❌ Problemas:**
- Datos y lógica desconectados
- Código difícil de mantener
- Alto riesgo de inconsistencias
- Escalabilidad limitada

</div>

<div style="flex: 1;">

**🎯 Programación Orientada a Objetos (POO)**

```csharp
// Datos y comportamiento unidos
Persona juan = new Persona("Juan", 25);
Persona maria = new Persona("María", 30);

juan.CumplirAnios();  // Lógica encapsulada
juan.MostrarInfo();   // Comportamiento asociado
```

**✅ Ventajas:**
- Código modular y reutilizable
- Fácil mantenimiento y extensión
- Modela objetos del mundo real
- Facilita trabajo en equipo

</div>

</div>

---

### Los Tres Pilares de la POO

```
┌─────────────────────────────────────────────────────────────────┐
│                      PILARES DE LA POO                          │
├──────────────────────┬──────────────────────┬───────────────────┤
│  ENCAPSULAMIENTO     │     HERENCIA         │  POLIMORFISMO     │
│       (Hoy)          │    (Clase 3)         │   (Clase 3)       │
├──────────────────────┼──────────────────────┼───────────────────┤
│                      │                      │                   │
│  🔒 Ocultar datos    │  🔄 Reutilizar       │  🎭 Una interfaz, │
│     internos         │     código           │     múltiples     │
│                      │     existente        │     formas        │
│                      │                      │                   │
│  Ejemplo:            │  Ejemplo:            │  Ejemplo:         │
│  Propiedades con     │  Estudiante hereda   │  Dibujar() se     │
│  get/set             │  de Persona          │  comporta         │
│                      │                      │  diferente para   │
│                      │                      │  Círculo/Cuadrado │
└──────────────────────┴──────────────────────┴───────────────────┘
```

---

## Clase vs Objeto

### Analogía: Molde vs Producto

<div style="display: flex; gap: 20px; align-items: center;">

<div style="flex: 1;">

**🎨 CLASE = Molde / Plantilla / Blueprint**

- Define la estructura
- Especifica atributos (datos)
- Define comportamientos (métodos)
- No ocupa memoria por sí sola
- Es el "tipo" de dato

**Ejemplo:**
```csharp
class Galleta {
    public string Sabor;
    public double Diametro;
    
    public void Hornear() { }
}
```

</div>

<div style="flex: 1;">

**🍪 OBJETO = Instancia concreta**

- Creado a partir de una clase
- Ocupa memoria en el heap
- Tiene valores específicos
- Puede ejecutar métodos
- Es una "variable" del tipo

**Ejemplo:**
```csharp
Galleta g1 = new Galleta();
g1.Sabor = "Chocolate";
g1.Diametro = 5.5;
```

</div>

</div>

---

### Visualización Gráfica

![Clase vs Objeto](../../assets/infografias/clase-02-clase-vs-objeto.png){: style="max-width: 50%; max-height: 300px; display: block; margin: 0 auto;"}

*Imagen: La clase Galleta actúa como molde para crear múltiples objetos galleta, cada uno con sus propias características (sabor, tamaño, decoración).*

---

### Representación en Memoria

```
┌────────────────────────────────────────────────────────────────────┐
│                         MEMORIA                                    │
├─────────────────────────┬──────────────────────────────────────────┤
│      STACK              │              HEAP                        │
│  (Referencias)          │         (Objetos reales)                 │
├─────────────────────────┼──────────────────────────────────────────┤
│                         │                                          │
│  ┌─────────────────┐    │    ┌─────────────────────────────┐      │
│  │   est1          │────┼───→│      Objeto Estudiante      │      │
│  │   0x7F3A...     │    │    │  ┌─────────────────────┐    │      │
│  └─────────────────┘    │    │  │ Nombre: "María"     │    │      │
│                         │    │  │ Código: "2024001"   │    │      │
│  ┌─────────────────┐    │    │  │ Edad: 20            │    │      │
│  │   est2          │────┼───→│  │ Promedio: 4.2       │    │      │
│  │   0x8B2C...     │    │    │  └─────────────────────┘    │      │
│  └─────────────────┘    │    └─────────────────────────────┘      │
│                         │                                          │
│  Las variables son      │    Los objetos contienen los datos      │
│  solo "direcciones"     │    reales y ocupan memoria en el heap   │
│  (4 u 8 bytes)          │                                          │
└─────────────────────────┴──────────────────────────────────────────┘
```

> **💡 Concepto clave:** En C#, las variables de tipo clase almacenan **referencias** (direcciones de memoria), no los objetos en sí. Esto es diferente de los tipos valor como `int` o `struct`.

---

## 2. Clases en C#

### Sintaxis de declaración

```csharp
// ESTRUCTURA BÁSICA DE UNA CLASE

[modificador] class NombreClase
{
    // CAMPOS (atributos/variables de instancia)
    [modificador] tipo nombreCampo;
    
    // PROPIEDADES (encapsulamiento)
    [modificador] tipo NombrePropiedad { get; set; }
    
    // CONSTRUCTORES
    [modificador] NombreClase([parámetros])
    {
        // inicialización
    }
    
    // MÉTODOS (comportamientos)
    [modificador] tipoRetorno NombreMetodo([parámetros])
    {
        // código
    }
}
```

---
### Ejemplo: Clase Estudiante - Primera Versión

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

**📋 Código C#:**

```csharp
using System;

namespace Universidad
{
    public class Estudiante
    {
        // CAMPOS (fields) - Variables de instancia
        public string nombre;
        public string codigo;
        public int edad;
        public double promedio;
        
        // MÉTODO
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
}
```

</div>

<div style="flex: 1;">

**🔍 Análisis:**

| Elemento | Descripción |
|----------|-------------|
| `namespace` | Agrupa clases relacionadas |
| `public class` | Define una clase accesible |
| `string nombre` | Campo público (❌ mala práctica) |
| `void MostrarInfo()` | Método sin retorno |

**⚠️ Problemas de esta versión:**
- Campos públicos = violación de encapsulamiento
- Cualquiera puede modificar los datos
- Sin validación de valores
- Difícil mantener consistencia

**✅ Usar esto solo para ejemplos iniciales**

</div>

</div>

---
### Instanciación con new


```csharp
using System;
using Universidad;  // Namespace de la clase

class Program
{
    static void Main(string[] args)
    {
        // CREAR OBJETO (instanciar)
        Estudiante est1 = new Estudiante();
        
        // ASIGNAR VALORES A LOS CAMPOS
        est1.nombre = "María López";
        est1.codigo = "2024001";
        est1.edad = 20;
        est1.promedio = 4.2;
        
        // USAR MÉTODOS
        est1.MostrarInfo();
        
        // CREAR MÁS OBJETOS (independientes)
        Estudiante est2 = new Estudiante();
        est2.nombre = "Carlos Ruiz";
        // ...
    }
}
```

---

## Diagrama de Memoria

### ¿Qué ocurre en memoria?

```
STACK (variables)              HEAP (objetos)
┌─────────────┐                ┌─────────────────────┐
│  est1       │──referencia──→│  Objeto Estudiante  │
│  (dirección)│                │  ├─ nombre: "María" │
└─────────────┘                │  ├─ codigo: "2024.."│
                               │  ├─ edad: 20        │
┌─────────────┐                │  └─ promedio: 4.2   │
│  est2       │──referencia──→└─────────────────────┘
│  (dirección)│                ┌─────────────────────┐
└─────────────┘                │  Objeto Estudiante  │
                               │  ├─ nombre: "Carlos"│
                               │  ├─ codigo: null    │
                               │  ├─ edad: 0         │
                               │  └─ promedio: 0.0   │
                               └─────────────────────┘
```

---

## 3. Encapsulamiento

![Encapsulamiento](../../assets/infografias/clase-02-encapsulamiento.png){: style="max-width: 80%; max-height: 500px; display: block; margin: 0 auto;"}

### Problema con campos públicos

```csharp
// ❌ PROBLEMA: Campos públicos
public class CuentaBancaria
{
    public double saldo;  // Cualquiera puede modificarlo
}

// En algún lugar del código...
CuentaBancaria cuenta = new CuentaBancaria();
cuenta.saldo = 1000000;  // ¡Creé dinero de la nada!
cuenta.saldo = -5000;    // ¡Saldo negativo válido!
```

**El encapsulamiento protege la integridad de los datos**

---

## Encapsulamiento: Solución

### Modificadores de acceso

```csharp
┌─────────────────────────────────────────────────────────────┐
│              MODIFICADORES DE ACCESO EN C#                  │
├───────────────┬─────────────────────────────────────────────┤
│ Modificador   │ Alcance                                     │
├───────────────┼─────────────────────────────────────────────┤
│ public        │ Accesible desde cualquier lugar             │
│ private       │ Solo dentro de la misma clase               │
│ protected     │ Dentro de la clase y sus hijas (herencia)   │
│ internal      │ Dentro del mismo ensamblado/proyecto        │
│ protected     │ Combinación: proyecto + herencia            │
│ internal      │                                             │
└───────────────┴─────────────────────────────────────────────┘
```

---
### Campos privados, acceso controlado


```csharp
public class CuentaBancaria
{
    // Campo PRIVADO (nadie fuera de la clase puede verlo)
    private double saldo;
    
    // MÉTODOS PÚBLICOS para acceder/modificar
    public double ObtenerSaldo()
    {
        return saldo;  // Solo lectura
    }
    
    public void Depositar(double cantidad)
    {
        if (cantidad > 0)
            saldo += cantidad;  // Validación incluida
    }
    
    public bool Retirar(double cantidad)
    {
        if (cantidad > 0 && cantidad <= saldo)
        {
            saldo -= cantidad;
            return true;
        }
        return false;  // No se pudo retirar
    }
}
```

---

## 4. Propiedades en C#

### Sintaxis moderna de C#

```csharp
// FORMA TRADICIONAL (Java, C++ antiguo)
private string nombre;
public string GetNombre() { return nombre; }
public void SetNombre(string value) { nombre = value; }

// FORMA MODERNA C# - PROPIEDADES
public string Nombre 
{ 
    get { return nombre; }
    set { nombre = value; }
}

// USO (más limpio)
estudiante.Nombre = "María";     // set
Console.WriteLine(estudiante.Nombre);  // get
```

**Las propiedades parecen campos, pero son métodos disfrazados**

---
### Diferentes configuraciones


```csharp
public class Producto
{
    // 1. Propiedad de lectura/escritura completa
    private string nombre;
    public string Nombre
    {
        get { return nombre; }
        set { nombre = value; }  // 'value' es palabra clave
    }
    
    // 2. Propiedad de solo lectura (calculada)
    public double PrecioFinal 
    { 
        get { return Precio * (1 + IVA); }
    }
    
    // 3. Propiedad de solo escritura (raro)
    private string clave;
    public string Clave
    {
        set { clave = value; }
    }
    
---
### Diferentes configuraciones


    // 4. Propiedad AUTOIMPLEMENTADA (sintaxis corta)
    public double Precio { get; set; }
    
    // 5. Propiedad con valor por defecto
    public double IVA { get; set; } = 0.19;  // 19% por defecto
    
    // 6. Propiedad de solo lectura (init-only C# 9+)
    public string SKU { get; init; }
}
```

---

### Cuándo usar cada tipo de propiedad

| Tipo | Sintaxis | Uso recomendado |
|------|----------|-----------------|
| **Autoimplementada** | `{ get; set; }` | Cuando no necesitas validación |
| **Con backing field** | `{ get { return x; } set { x = value; } }` | Cuando necesitas lógica en get/set |
| **Solo lectura** | `{ get; }` o `{ get; private set; }` | Valores calculados o inmutables |
| **Init-only** | `{ get; init; }` | Asignable solo en construcción |
| **C# 12 auto** | `public string Nombre { get; set; } = "";` | Evita null warnings |

---
## Propiedades con Validación

### El poder del encapsulamiento

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

**💡 Concepto:**
Las propiedades permiten validar datos antes de asignarlos, garantizando la integridad del objeto.

```csharp
public class Estudiante
{
    private string nombre;
    private int edad;
    private double promedio;
    
    public string Nombre
    {
        get { return nombre; }
        set 
        { 
            if (!string.IsNullOrWhiteSpace(value))
                nombre = value;
            else
                throw new ArgumentException(
                    "Nombre no puede estar vacío");
        }
    }
```

</div>

<div style="flex: 1;">

**🔍 Más validaciones:**

```csharp
    public int Edad
    {
        get { return edad; }
        set 
        { 
            if (value >= 0 && value <= 120)
                edad = value;
            else
                throw new ArgumentOutOfRangeException(
                    "Edad debe estar entre 0 y 120");
        }
    }
    
    public double Promedio
    {
        get { return promedio; }
        set 
        { 
            if (value >= 0.0 && value <= 5.0)
                promedio = value;
            else
                throw new ArgumentOutOfRangeException(
                    "Promedio debe ser 0-5");
        }
    }
}
```

</div>

</div>

---

### Ejemplo de uso con validación

```csharp
var est = new Estudiante();

// ✅ Asignaciones válidas
est.Nombre = "María López";
est.Edad = 20;
est.Promedio = 4.5;

// ❌ Asignaciones inválidas (lanzan excepciones)
est.Nombre = "";           // ArgumentException
est.Edad = -5;             // ArgumentOutOfRangeException
est.Promedio = 10.0;       // ArgumentOutOfRangeException
```

> **💼 En proyectos reales:** Usa estas validaciones para garantizar que los objetos siempre estén en un estado válido. Esto previene bugs difíciles de rastrear.
---
### Inicialización en Constructores

**Concepto:** Algunas propiedades deben establecerse solo durante la creación del objeto y no cambiar después.

```csharp
public class Estudiante
{
    // Propiedad de solo lectura (desde fuera)
    public string Codigo { get; }
    
    // Propiedad de solo lectura con valor calculado
    public DateTime FechaIngreso { get; }
    
    // Propiedad con setter privado (modificable solo dentro de la clase)
    public int SemestreActual { get; private set; }
    
    // CONSTRUCTOR
    public Estudiante(string codigo)
    {
        Codigo = codigo;              // Se asigna una sola vez
        FechaIngreso = DateTime.Now;  // Registro automático
        SemestreActual = 1;           // Valor inicial
    }
    
    // Método que modifica la propiedad de lectura privada
    public void AvanzarSemestre()
    {
        SemestreActual++;  // ✅ Válido: dentro de la clase
    }
}
```

---

### Uso del constructor

```csharp
// Crear estudiante - código asignado en constructor
var est = new Estudiante("2024001");

Console.WriteLine(est.Codigo);           // "2024001"
Console.WriteLine(est.FechaIngreso);     // Fecha actual
Console.WriteLine(est.SemestreActual);   // 1

// est.Codigo = "otro";     // ❌ ERROR: propiedad de solo lectura
// est.SemestreActual = 5;  // ❌ ERROR: setter es privado

est.AvanzarSemestre();       // ✅ Válido
Console.WriteLine(est.SemestreActual);   // 2
```

---
### Constructores - Múltiples Versiones

Una clase puede tener varios constructores (sobrecarga) para diferentes escenarios:

```csharp
public class Estudiante
{
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    
    // ═══════════════════════════════════════════════════
    // CONSTRUCTOR POR DEFECTO (sin parámetros)
    // ═══════════════════════════════════════════════════
    public Estudiante()
    {
        Nombre = "Sin nombre";
        Codigo = "0000000";
        Edad = 18;
        Console.WriteLine("Constructor por defecto ejecutado");
    }
    
    // ═══════════════════════════════════════════════════
    // CONSTRUCTOR PARAMETRIZADO (3 parámetros)
    // ═══════════════════════════════════════════════════
    public Estudiante(string nombre, string codigo, int edad)
    {
        Nombre = nombre;
        Codigo = codigo;
        Edad = edad;
    }
    
    // ═══════════════════════════════════════════════════
    // CONSTRUCTOR CON PARÁMETROS OPCIONALES (2 params)
    // ═══════════════════════════════════════════════════
    public Estudiante(string nombre, string codigo)
    {
        Nombre = nombre;
        Codigo = codigo;
        Edad = 18;  // valor por defecto
    }
}
```

---

## Sobrecarga de Constructores

### Múltiples formas de crear objetos

```csharp
// Uso de diferentes constructores

// 1. Constructor por defecto
Estudiante e1 = new Estudiante();
// Nombre="Sin nombre", Codigo="0000000", Edad=18

// 2. Constructor con 2 parámetros
Estudiante e2 = new Estudiante("María", "2024001");
// Nombre="María", Codigo="2024001", Edad=18

// 3. Constructor con 3 parámetros
Estudiante e3 = new Estudiante("Carlos", "2024002", 22);
// Nombre="Carlos", Codigo="2024002", Edad=22

// 4. Sintaxis simplificada (C# 9.0+)
Estudiante e4 = new();  // Target-typed new
var e5 = new Estudiante { Nombre = "Ana", Edad = 20 };  // Object initializer
```

---

## Inicialización de Objetos

### Object Initializers (Sintaxis moderna)

```csharp
// FORMA TRADICIONAL
Estudiante est = new Estudiante("María", "2024001", 20);

// OBJECT INITIALIZER (C# moderno)
Estudiante est = new Estudiante
{
    Nombre = "María López",
    Codigo = "2024001",
    Edad = 20,
    Promedio = 4.5
};

// CONSTRUCTOR + INITIALIZER COMBINADOS
Estudiante est = new Estudiante("María", "2024001")
{
    Edad = 20,           // Propiedad adicional
    Promedio = 4.5
};
```

---
## Clase Estudiante Completa

### Versión final con buenas prácticas

```csharp
using System;

public class Estudiante
{
    // ═══════════════════════════════════════════════════════
    // PROPIEDADES AUTOIMPLEMENTADAS
    // ═══════════════════════════════════════════════════════
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    public double Promedio { get; set; }
    
    // ═══════════════════════════════════════════════════════
    // CONSTRUCTORES
    // ═══════════════════════════════════════════════════════
    public Estudiante()
    {
        Nombre = "Sin nombre";
        Codigo = "0000000";
        Edad = 18;
        Promedio = 0.0;
    }
    
    public Estudiante(string nombre, string codigo, int edad)
    {
        Nombre = nombre;
        Codigo = codigo;
        Edad = edad;
        Promedio = 0.0;
    }
    
    // ═══════════════════════════════════════════════════════
    // MÉTODOS DE NEGOCIO
    // ═══════════════════════════════════════════════════════
    public bool Aprobo()
    {
        return Promedio >= 3.0;
    }
    
    public string ObtenerEstado()
    {
        return Aprobo() ? "APROBADO" : "REPROBADO";
    }
    
    public void MostrarInfo()
    {
        Console.WriteLine($"📚 {Nombre} ({Codigo})");
        Console.WriteLine($"   Edad: {Edad} años");
        Console.WriteLine($"   Promedio: {Promedio:F2}");
        Console.WriteLine($"   Estado: {(Aprobo() ? "✅" : "❌")} {ObtenerEstado()}");
    }
}
```
---

## Miembros Estáticos vs de Instancia

### Comprender la diferencia

```csharp
public class Contador
{
    // Campo estático: compartido por TODAS las instancias
    public static int ContadorGlobal = 0;

    // Campo de instancia: cada objeto tiene su propio valor
    public int ContadorInstancia = 0;

    public Contador()
    {
        ContadorGlobal++;    // Se incrementa para TODOS los objetos
        ContadorInstancia++; // Se incrementa solo para este objeto
    }
}

// Uso
Contador c1 = new Contador();  // ContadorGlobal=1, c1.ContadorInstancia=1
Contador c2 = new Contador();  // ContadorGlobal=2, c2.ContadorInstancia=1
Contador c3 = new Contador();  // ContadorGlobal=3, c3.ContadorInstancia=1

// Acceso a miembros estáticos (desde la clase, no desde objetos)
Console.WriteLine(Contador.ContadorGlobal);  // 3

// Acceso a miembros de instancia
Console.WriteLine(c1.ContadorInstancia);     // 1
Console.WriteLine(c2.ContadorInstancia);     // 1
```

---

## class vs struct en C#

### ¿Cuándo usar cada uno?

```csharp
// CLASS (Reference Type) - USO COMÚN
public class Persona
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
}

// STRUCT (Value Type) - Para datos pequeños
public struct Punto
{
    public double X { get; set; }
    public double Y { get; set; }
}

// DIFERENCIAS:
Persona p1 = new Persona("Juan", 25);
Persona p2 = p1;      // Copia REFERENCIA (misma dirección)
p2.Nombre = "María";  // ¡p1 también cambia!

Punto pt1 = new Punto(10, 20);
Punto pt2 = pt1;      // Copia VALOR (independiente)
pt2.X = 50;          // pt1.X sigue siendo 10
```

**USAR CLASS PARA:** Objetos con identidad, herencia, polimorfismo
**USAR STRUCT PARA:** Datos pequeños, inmutables, mejor rendimiento

---

## 6. Práctica en Clase

### Ejercicio: Sistema de Gestión Estudiantil

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

**🎯 Objetivo:** Crear una aplicación que gestione estudiantes usando los conceptos de POO aprendidos.

**📋 Instrucciones:**
1. Crear un nuevo proyecto Console App en Visual Studio
2. Agregar la clase `Estudiante` (versión completa)
3. Implementar el programa principal (→)
4. Probar creando al menos 3 estudiantes
5. Mostrar información de todos

**🧪 Datos de prueba:**
- María López, 2024001, 20 años, Promedio: 4.2
- Carlos Ruiz, 2024002, 22 años, Promedio: 2.8
- Ana Martínez, 2024003, 19 años, Promedio: 3.5

</div>

<div style="flex: 1;">

**💻 Código del programa principal:**

```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // Lista para almacenar estudiantes
        List<Estudiante> estudiantes = 
            new List<Estudiante>();
        
        // Agregar estudiantes usando object initializer
        estudiantes.Add(new Estudiante(
            "María López", "2024001", 20) 
        { 
            Promedio = 4.2 
        });
        
        estudiantes.Add(new Estudiante(
            "Carlos Ruiz", "2024002", 22) 
        { 
            Promedio = 2.8 
        });
        
        estudiantes.Add(new Estudiante(
            "Ana Martínez", "2024003", 19) 
        { 
            Promedio = 3.5 
        });
        
        // Mostrar información
        Console.WriteLine(
            "=== LISTA DE ESTUDIANTES ===\n");
        
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

| Concepto | Descripción |
| ---------- | ------------- |
| **Clase** | Plantilla/blueprint para crear objetos |
| **Objeto** | Instancia concreta de una clase |
| **Campo** | Variable de instancia (dato) |
| **Propiedad** | Encapsulamiento con get/set |
| **Método** | Comportamiento/acción del objeto |
| **Constructor** | Método especial para inicializar objetos |
| **Encapsulamiento** | Ocultar implementación, exponer interfaz |

---

## Ejercicios Propuestos

### Para practicar en casa

**Ejercicio 1: Clase Producto**
Crear una clase `Producto` con:
- Código (solo lectura, asignado en constructor)
- Nombre (propiedad con validación: no vacío)
- Precio (propiedad con validación: > 0)
- Cantidad en stock (>= 0)
- Método `CalcularValorInventario()` que retorne Precio * Stock

**Ejercicio 2: Clase CuentaBancaria**
Crear una clase con:
- Número de cuenta (solo lectura)
- Saldo (privado, acceso solo mediante métodos)
- Métodos: Depositar(), Retirar(), ConsultarSaldo()
- Validar que no se pueda retirar más del saldo disponible

**Ejercicio 3: Clase con Miembros Estáticos**
Crear una clase `Tienda` con:
- Campo estático para contar productos creados
- Propiedad estática de solo lectura para obtener el total
- Constructor que incremente el contador
- Método estático para mostrar estadísticas

**Ejercicio 4: Sistema de Biblioteca (Avanzado)**
Modelar las siguientes clases:
- `Libro`: ISBN, título, autor, año, cantidad disponible
- `Usuario`: código, nombre, email, tipo (estudiante/profesor)
- `Prestamo`: fecha préstamo, fecha devolución, estado
- Implementar propiedades con validación
- Agregar métodos para calcular fechas de devolución según tipo de usuario

---

## Próxima Clase

### Clase 3: Herencia y Polimorfismo

- Herencia: clase base y clase derivada
- Palabra clave `base`
- Polimorfismo: virtual, override, abstract
- Clases y métodos abstractos
- Principio de sustitución de Liskov

**¡Nos vemos!**

---

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
