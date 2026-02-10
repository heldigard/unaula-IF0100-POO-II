# Clase 02 - Teoría Profunda
## Clases, Objetos y Encapsulamiento

**IF0100 - Lenguaje de Programación OO II** | Unidad 1

---

## Tabla de Contenidos

- [Programación Orientada a Objetos](#programación-orientada-a-objetos)
- [Clase vs Objeto](#clase-vs-objeto)
- [Representación en Memoria](#representación-en-memoria)
- [Encapsulamiento](#encapsulamiento)
- [Modificadores de Acceso](#modificadores-de-acceso)
- [Propiedades](#propiedades)
- [Constructores](#constructores)
- [Static vs Instance](#static-vs-instance)

---

## Programación Orientada a Objetos

### ¿Qué es la POO?

La Programación Orientada a Objetos (POO) es un paradigma de programación que se basa en el concepto de "objetos", que pueden contener datos y código:

- **Datos**: Atributos o propiedades (campos)
- **Código**: Comportamientos o métodos (funciones)

### 📜 Procedural vs 🎯 POO

| Aspecto | Programación Procedural | Programación Orientada a Objetos |
|---------|------------------------|----------------------------------|
| **Unidad básica** | Funciones/procedimientos | Clases/objetos |
| **Datos** | Separados de funciones | Unidos con métodos |
| **Organización** | Procedimientos que actúan sobre datos | Objetos que encapsulan datos y comportamiento |
| **Mantenimiento** | Difícil (código acoplado) | Modular (código desacoplado) |
| **Escalabilidad** | Limitada | Fácil de extender |
| **Reutilización** | Baja | Alta (herencia, composición) |

### Ejemplo Comparativo

**Enfoque Procedural (C tradicional):**
```c
// Datos separados
struct Estudiante {
    char nombre[100];
    int edad;
    double promedio;
};

// Funciones separadas
void imprimir_estudiante(struct Estudiante* e) {
    printf("Nombre: %s\n", e->nombre);
}

double calcular_promedio(struct Estudiante* e) {
    return e->promedio;
}

int main() {
    struct Estudiante est1;
    // ... asignación manual
    imprimir_estudiante(&est1);
    return 0;
}
```

**Enfoque POO (C#):**
```csharp
// Datos y comportamiento UNIDOS
public class Estudiante
{
    // Datos (propiedades)
    public string Nombre { get; set; }
    public int Edad { get; set; }
    public double Promedio { get; set; }

    // Comportamiento (métodos)
    public void Imprimir() => Console.WriteLine($"Nombre: {Nombre}");

    public double CalcularPromedio() => Promedio;

    public bool Aprobado() => Promedio >= 3.0;
}

// Uso
var est1 = new Estudiante { Nombre = "María", Edad = 20, Promedio = 4.2 };
est1.Imprimir();
```

### Ventajas de POO

| Ventaja | Descripción |
|---------|-------------|
| **Modularidad** | Código organizado en unidades lógicas (clases) |
| **Reutilización** | Código reutilizable mediante herencia y composición |
| **Mantenibilidad** | Cambios localizados en clases específicas |
| **Extensibilidad** | Fácil agregar nuevas funcionalidades sin modificar código existente |
| **Abstracción** | Oculta complejidad, expone solo lo necesario |
| **Modelado del mundo real** | Objetos representan entidades del dominio |

---

## Los Tres Pilares de la POO

```
┌─────────────────────────────────────────────────┐
│          PILARES DE LA PROGRAMACIÓN ORIENTADA    │
│                  A OBJETOS (POO)                  │
├─────────────┬───────────────┬───────────────────┤
│  1️⃣        │  2️⃣           │  3️⃣               │
│ ENCAPSULA   │  HERENCIA     │   POLIMORFISMO     ││
│ MIENTO      │               │                   │
├─────────────┼───────────────┼───────────────────┤
│ Ocultar     │ Reutilizar    │ Una interfaz,     │
│ datos       │ código        │ múltiples formas  │
│ internos    │               │                   │
│             │               │                   │
│ Exponer     │ Crear         │ Misma llamada,    │
│ compor-     │ jerarquías    │ diferente         │
│ tamiento    │               │ comportamiento   │
│ público     │               │                   │
│             │               │                   │
│ **HOY**     │ **CLASE 03**  │ **CLASE 03**      │
└─────────────┴───────────────┴───────────────────┘
```

### 1. Encapsulamiento (Clase 2 - Hoy)

> Ocultar los detalles internos de un objeto y exponer solo lo necesario a través de una interfaz pública.

**Beneficios:**
- Protección de datos (no se pueden modificar directamente)
- Control sobre cómo se accede y modifica la información
- Flexibilidad para cambiar la implementación interna sin afectar a quien usa la clase

### 2. Herencia (Clase 3 - Próxima)

> Crear nuevas clases basadas en clases existentes, reutilizando código y extendiendo funcionalidad.

**Beneficios:**
- Reutilización de código
- Jerarquías lógicas (Estudiante → Persona)
- Extensibilidad sin modificar código original

### 3. Polimorfismo (Clase 3 - Próxima)

> Capacidad de objetos de diferentes tipos responder al mismo mensaje de diferentes formas.

**Beneficios:**
- Código flexible y extensible
- Tratamiento uniforme de objetos diferentes
- Fácil agregar nuevos tipos sin modificar código existente

---

## Clase vs Objeto

### 🎨 CLASE = Molde / Plantilla / Definición

Una clase es una **definición** o **plantilla** para crear objetos. Es abstracta y no ocupa memoria por sí misma.

**Características:**
- Define estructura (qué datos tendrá)
- Especifica comportamiento (qué podrá hacer)
- NO ocupa memoria en tiempo de ejecución
- Es el "tipo" o "categóría"
- Escrita una vez, usada muchas veces

### 🍪 OBJETO = Instancia / Ejemplar / Creación Concreta

Un objeto es una **instancia concreta** de una clase. Ocupa memoria y tiene valores específicos.

**Características:**
- Creado a partir de una clase con `new`
- Ocupa memoria (heap para reference types)
- Tiene valores específicos para sus atributos
- Puede ejecutar sus métodos
- Cada objeto es independiente

### 📊 Comparativa Detallada

| Aspecto | Clase (Molde) | Objeto (Instancia) |
|---------|---------------|-------------------|
| **Naturaleza** | Abstracta (definición) | Concreta (ejecución) |
| **Memoria** | NO ocupa (metadata del tipo) | SÍ ocupa (heap) |
| **Cantidad** | Una definición | Múltiples instancias |
| **Valores** | Define QUÉ atributos tendrá | TIENE valores específicos |
| **Declaración** | `class Galleta { ... }` | `new Galleta()` |
| **Relación** | Es un "tipo de dato" | Es una "variable" de ese tipo |
| **Analogía** | Receta de cocina | Galleta horneada |
| **Analogía** | Plano de arquitectura | Casa construida |
| **Analogía** | Formulario en blanco | Formulario lleno |

### 💡 Analogías Ilustrativas

#### Analogía 1: Galletas

```
CLASE = Receta de galletas
- Define ingredientes: harina, azúcar, chocolate
- Define procedimiento: mezclar, hornear, enfriar
- NO se puede comer (es abstracta)

OBJETO = Galleta horneada específica
- Tiene cantidades específicas de ingredientes
- Se puede comer (es concreta)
- Cada galleta es única pero sigue la receta
```

#### Analogía 2: Arquitectura

```
CLASE = Plano arquitectónico de una casa
- Define distribución: habitaciones, puertas, ventanas
- Define materiales: ladrillo, cemento, vidrio
- NO se puede habitar (es papel)

OBJETO = Casa construida específica
- Tiene ubicación específica
- Se puede habitar (es física)
- Cada casa es única pero sigue el plano
```

#### Analogía 3: Formularios

```
CLASE = Formulario en blanco
- Define campos: nombre, dirección, teléfono
- NO tiene información específica

OBJETO = Formulario lleno con datos
- Tiene valores específicos: "Juan", "Calle 123", "555-1234"
- Cada formulario es diferente pero misma estructura
```

### Ejemplo de Código

```csharp
// ============================================
// CLASE: Definición (plantilla)
// ============================================
public class Estudiante
{
    // Campos (atributos)
    public string Nombre;
    public string Codigo;
    public int Edad;
    public double Promedio;

    // Métodos (comportamiento)
    public void MostrarInfo()
    {
        Console.WriteLine($"Nombre: {Nombre}");
        Console.WriteLine($"Código: {Codigo}");
        Console.WriteLine($"Edad: {Edad}");
        Console.WriteLine($"Promedio: {Promedio}");
    }

    public bool Aprobado() => Promedio >= 3.0;
}

// ============================================
// OBJETOS: Instancias (creaciones concretas)
// ============================================
class Program
{
    static void Main()
    {
        // Crear PRIMER objeto (instancia)
        Estudiante est1 = new Estudiante();
        est1.Nombre = "María López";
        est1.Codigo = "2024001";
        est1.Edad = 20;
        est1.Promedio = 4.2;

        // Crear SEGUNDO objeto (independiente)
        Estudiante est2 = new Estudiante();
        est2.Nombre = "Carlos Ruiz";
        est2.Codigo = "2024002";
        est2.Edad = 22;
        est2.Promedio = 2.8;

        // Cada objeto es independiente
        est1.MostrarInfo();
        Console.WriteLine();
        est2.MostrarInfo();
    }
}
```

**Salida:**
```
Nombre: María López
Código: 2024001
Edad: 20
Promedio: 4.2

Nombre: Carlos Ruiz
Código: 2024002
Edad: 22
Promedio: 2.8
```

---

## Representación en Memoria

### 📚 STACK vs HEAP

En C#, los objetos (reference types) se almacenan en dos áreas de memoria:

#### STACK (Pila)

- Almacena **variables locales** y **referencias** a objetos
- Crecce y decrece rápidamente (LIFO - Last In, First Out)
- Limpieza automática al salir del método
- Cada hilo tiene su propio stack
- Almacena directamente los **value types** (int, double, bool, struct)

#### HEAP (Montículo)

- Almacena **objetos reales** (instancias de clases)
- Memoria más grande pero más lenta de gestionar
- Limpieza automática por el **Garbage Collector (GC)**
- Compartido por todos los hilos
- Almacena los **reference types** (class, string, array)

### Visualización de Memoria

```
┌─────────────────────────────────────────────────────────────┐
│                    MEMORIA EN EJECUCIÓN                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌────────────────────┐      ┌──────────────────────────┐ │
│  │      STACK         │      │         HEAP              │ │
│  │  (Referencias)     │      │    (Objetos Reales)       │ │
│  ├────────────────────┤      ├──────────────────────────┤ │
│  │                    │      │                          │ │
│  │  ┌──────────────┐  │      │  ┌────────────────────┐ │ │
│  │  │ est1         │──┼─────┼─→│ Objeto Estudiante   │ │ │
│  │  │ 0x7F3A...B4  │  │      │  │ ┌────────────────┐ │ │ │
│  │  └──────────────┘  │      │  │ │ Nombre: "María" │ │ │ │
│  │                    │      │  │ │ Código: "2024.."│ │ │ │
│  │  ┌──────────────┐  │      │  │ │ Edad: 20        │ │ │ │
│  │  │ est2         │──┼─────┼─→│ │ Promedio: 4.2   │ │ │ │
│  │  │ 0x8B2C...F8  │  │      │  │ └────────────────┘ │ │ │
│  │  └──────────────┘  │      │  └────────────────────┘ │ │
│  │                    │      │                          │ │
│  │  ┌──────────────┐  │      │  ┌────────────────────┐ │ │
│  │  │ nombre       │  │      │  │ Objeto String      │ │ │
│  │  │ "María"      │  │      │  │ "María López"      │ │ │
│  │  │ (inmutable)  │  │      │  │ (interned)         │ │ │
│  │  └──────────────┘  │      │  └────────────────────┘ │ │
│  │                    │      │                          │ │
│  └────────────────────┘      └──────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Flujo de Creación de un Objeto

```csharp
// Paso 1: Declaración (stack - variable de referencia)
Estudiante est1;  // stack: est1 = null

// Paso 2: Instanciación (heap - objeto creado)
est1 = new Estudiante();  // heap: new Estudiante object

// Paso 3: Asignación de valores
est1.Nombre = "María";  // heap: Nombre = "María"
est1.Edad = 20;         // heap: Edad = 20
```

### Puntos Clave

1. **La variable en el STACK contiene una dirección de memoria** (referencia) al objeto en el HEAP
2. **Múltiples variables pueden referenciar el mismo objeto**:
   ```csharp
   Estudiante est1 = new Estudiante { Nombre = "María" };
   Estudiante est2 = est1;  // Ambos referencian el MISMO objeto
   est2.Nombre = "Carlos";   // est1.Nombre también cambia
   ```
3. **Cuando una variable sale del scope**, la referencia en el stack se elimina, pero el objeto en el heap permanece hasta que el Garbage Collector lo reclama

---

## Encapsulamiento

### 🔒 ¿Qué es Encapsulamiento?

> Encapsulamiento es el principio de ocultar los detalles internos de implementación de un objeto y exponer solo lo necesario a través de una interfaz pública.

**Metáfora:** Un coche tiene un encapsulamiento - tú solo interactúas con el volante, pedales y botones. No necesitas saber cómo funciona el motor internamente.

### ¿Por qué es IMPORTANTE?

| Problema sin encapsulamiento | Solución con encapsulamiento |
|------------------------------|------------------------------|
| Datos expuestos pueden modificarse a valores inválidos | Validación controlada |
| Difícil mantener (cambios afectan a todos) | Cambios localizados |
| Acoplamiento alto (dependencias ocultas) | Bajo acoplamiento |
| Código frágil (se rompe fácil) | Código robusto |

### ❌ SIN Encapsulamiento (Frágil)

```csharp
public class CuentaBancaria
{
    // ⚠️ Campos PÚBLICOS = peligro
    public double saldo;
    public string titular;
}

// Uso problemático
var cuenta = new CuentaBancaria();
cuenta.saldo = -1000;  // ⚠️ Válido pero INCORRECTO
cuenta.titular = "";   // ⚠️ Nombre vacío permitido
```

**Problemas:**
- Sin validación de datos
- Cualquiera puede modificar
- Difícil rastrear quién modificó
- No se pueden agregar reglas de negocio

### ✅ CON Encapsulamiento (Robusto)

```csharp
public class CuentaBancaria
{
    // ✅ Campos PRIVADOS = protegidos
    private double _saldo;
    private string _titular;

    // ✅ Propiedad con validación
    public string Titular
    {
        get => _titular;
        set
        {
            if (string.IsNullOrWhiteSpace(value))
                throw new ArgumentException("El titular no puede estar vacío");
            _titular = value;
        }
    }

    // ✅ Métodos controlados
    public void Depositar(double monto)
    {
        if (monto <= 0)
            throw new ArgumentException("El monto debe ser positivo");
        _saldo += monto;
    }

    public void Retirar(double monto)
    {
        if (monto <= 0)
            throw new ArgumentException("El monto debe ser positivo");
        if (monto > _saldo)
            throw new InvalidOperationException("Saldo insuficiente");
        _saldo -= monto;
    }

    public double Saldo => _saldo;  // Solo lectura
}

// Uso controlado
var cuenta = new CuentaBancaria();
cuenta.Titular = "Juan Pérez";   // ✅ Validación
cuenta.Depositar(1000);          // ✅ Método seguro
cuenta.Retirar(500);             // ✅ Validación de saldo
// cuenta.Retirar(2000);         // ❌ Excepción: Saldo insuficiente
// cuenta.Saldo = -1000;         // ❌ Error: Saldo es solo lectura
```

**Beneficios:**
- Validación de datos en entrada
- Control sobre modificaciones
- Fácil agregar lógica de negocio
- Protección del estado interno

### Niveles de Encapsulamiento

```
┌─────────────────────────────────────────────────────────┐
│         NIVELES DE ENCAPSULAMIENTO                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  PÚBLICO (API)          PRIVADO (Implementación)        │
│  ┌───────────────┐    ┌───────────────────────────┐   │
│  │ Propiedades   │    │ Campos                    │   │
│  │ Métodos       │    │ Métodos auxiliares        │   │
│  │ Constructores │    │ Lógica interna            │   │
│  └───────────────┘    │ Validaciones              │   │
│         │             │ Cálculos                  │   │
│         │             └───────────────────────────┘   │
│         ▲                                               │
│         │ Acceso controlado                           │
│         └───────────────────────────────────────────   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Principio de Mínima Exposición

> **Expón solo lo que es necesario para usar la clase. Oculta todo lo demás.**

**Ejemplo:**

```csharp
public class Estudiante
{
    // ✅ PÚBLICO: Parte de la API externa
    public string Nombre { get; set; }
    public int Edad { get; set; }

    // ❌ PRIVADO: Implementación interna
    private double _promedioInterno;
    private void _calcularPromedioInterno() { ... }

    // ✅ PÚBLICO: Expone resultado calculado (no los detalles)
    public double Promedio => _promedioInterno;
}
```

---

## Modificadores de Acceso

### Tabla de Modificadores en C#

| Modificador | ¿Quién accede? | Descripción | Uso típico |
|-------------|----------------|-------------|-----------|
| **`public`** | TODOS | Accesible desde cualquier lugar | API pública de la clase |
| **`private`** | Solo la clase | Solo accesible dentro de la clase | Campos internos, métodos auxiliares |
| **`protected`** | Clase + hijas | Accesible en la clase y sus derivadas | Miembros para herencia |
| **`internal`** | Mismo proyecto | Accesible solo dentro del mismo assembly (.dll/exe) | Clases auxiliares del proyecto |
| **`protected internal`** | Misma clase + hijas + mismo proyecto | Combinación de protected y internal | Miembros especializados |
| **`private protected`** | Clase + hijas (mismo proyecto) | Solo hijas en el mismo proyecto | Herencia interna |

### Ejemplo Visual

```
┌─────────────────────────────────────────────────────────┐
│         CLASE: Estudiante                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  PUBLIC (accesible desde fuera)                 │   │
│  │  ┌──────────────┐  ┌──────────────┐             │   │
│  │  │ Propiedades  │  │ Métodos      │             │   │
│  │  │ - Nombre     │  │ - Mostrar()  │             │   │
│  │  │ - Edad       │  │ - Aprobo()   │             │   │
│  │  └──────────────┘  └──────────────┘             │   │
│  └─────────────────────────────────────────────────┘   │
│              ▲                                          │
│              │ Llamadas desde fuera                   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  PRIVATE (solo interno)                         │   │
│  │  ┌─────────────────────────────────────────┐   │   │
│  │  │ Campos                                   │   │   │
│  │  │ - _nombre                                │   │   │
│  │  │ - _edad                                  │   │   │
│  │  │                                         │   │   │
│  │  │ Métodos auxiliares                      │   │   │
│  │  │ - _validarNombre()                       │   │   │
│  │  │ - _calcularPromedio()                    │   │   │
│  │  └─────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Reglas de Oro

1. **Campos SIEMPRE privados** (convención `_camelCase`)
2. **Propiedades públicas** para acceso controlado
3. **Métodos privados** para lógica interna
4. **Minimizar `public`** - expón solo lo necesario

### Ejemplo Completo

```csharp
public class CuentaBancaria
{
    // ✅ PRIVADOS: Solo uso interno
    private double _saldo;
    private readonly string _numeroCuenta;

    // ✅ PÚBLICOS: API externa
    public string Titular { get; set; }

    // ✅ SOLO LECTURA: No se puede modificar después de crear
    public string NumeroCuenta => _numeroCuenta;

    // ✅ PROPORCIONAL: Saldo expuesto pero sin modificación directa
    public double Saldo => _saldo;

    // Constructor
    public CuentaBancaria(string titular, string numeroCuenta, double saldoInicial)
    {
        Titular = titular;
        _numeroCuenta = numeroCuenta;
        _saldo = saldoInicial;
    }

    // ✅ PÚBLICO: Comportamiento controlado
    public void Depositar(double monto)
    {
        _validarMontoPositivo(monto);
        _saldo += monto;
    }

    public void Retirar(double monto)
    {
        _validarMontoPositivo(monto);
        if (monto > _saldo)
            throw new InvalidOperationException("Saldo insuficiente");
        _saldo -= monto;
    }

    // ❌ PRIVADO: Validación interna (reutilizable)
    private void _validarMontoPositivo(double monto)
    {
        if (monto <= 0)
            throw new ArgumentException("El monto debe ser positivo");
    }
}
```

---

## Propiedades

### ¿Qué son las Propiedades?

Las propiedades son **syntactic sugar** para encapsulamiento. Parecen campos pero son métodos (`get` y `set`) disfrazados.

### ❌ TRADICIONAL (Java-style) - Verboso

```csharp
public class Persona
{
    private string _nombre;

    // Método getter
    public string GetNombre()
    {
        return _nombre;
    }

    // Método setter
    public void SetNombre(string valor)
    {
        _nombre = valor;
    }
}

// Uso verboso
var p = new Persona();
p.SetNombre("María");
string n = p.GetNombre();
```

### ✅ MODERNO C# - Propiedades

```csharp
public class Persona
{
    private string _nombre;

    // Propiedad con get y set
    public string Nombre
    {
        get { return _nombre; }
        set { _nombre = value; }
    }
}

// Uso natural
var p = new Persona();
p.Nombre = "María";      // ← Usa 'set'
string n = p.Nombre;     // ← Usa 'get'
```

### Anatomía de una Propiedad

```
┌─────────────────────────────────────────────────────────┐
│           ANATOMÍA DE UNA PROPIEDAD                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   backing field        propiedad        uso            │
│   (almacenamiento)      (interfaz)       (acceso)       │
│   ┌──────────┐       ┌──────────┐      ┌──────┐       │
│   │ private  │       │ public   │ ◄────│ obj  │       │
│   │ _nombre  │◄──────│ Nombre   │      │ .N   │       │
│   └──────────┘       │ { get;   │      └──────┘       │
│         ▲            │   set; } │                      │
│         │            └──────────┘                      │
│         │                                               │
│         └── 'value' es el valor asignado en set        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Tipos de Propiedades

| Tipo | Sintaxis | Cuándo usar |
|------|----------|-------------|
| **Autoimplementada** | `{ get; set; }` | Sin validación, simple |
| **Con backing field** | get/set con lógica | Con validación |
| **Solo lectura** | `{ get; }` | Calculado o inmutable |
| **Init-only** | `{ get; init; }` | Solo en constructor |
| **Expresión bodied** | `=> valor` | Propiedades calculadas |

### Ejemplos Completos

```csharp
public class Estudiante
{
    // 1. AUTOIMPLEMENTADA (sin validación)
    public string Nombre { get; set; }
    public int Edad { get; set; }

    // 2. CON VALIDACIÓN (usa backing field)
    private double _promedio;
    public double Promedio
    {
        get => _promedio;
        set
        {
            if (value < 0.0 || value > 5.0)
                throw new ArgumentOutOfRangeException("Promedio", "Debe estar entre 0 y 5");
            _promedio = value;
        }
    }

    // 3. SOLO LECTURA (calculada)
    public bool Aprobado => Promedio >= 3.0;

    // 4. INIT-ONLY (solo se asigna en constructor o inicializador)
    public string Matricula { get; init; }

    // 5. CON VALOR DEFAULT
    public string Carrera { get; set; } = "Sin carrera";

    // 6. EXPRESIÓN BODIED (C# 7+)
    public string InfoCompleta => $"{Nombre} ({Edad} años) - {Carrera}";
}
```

---

## Constructores

### ¿Qué es un Constructor?

Un constructor es un **método especial** que se ejecuta automáticamente al crear una instancia de una clase con `new`.

**Propósito:**
- Inicializar valores predeterminados
- Recibir parámetros obligatorios
- Validar estado inicial
- Establecer invariantes de clase

### Tipos de Constructores

| Tipo | Sintaxis | Ejemplo |
|------|----------|---------|
| **Default** | `sin parámetros` | `new Estudiante()` |
| **Parametrizado** | `con parámetros` | `new Estudiante("María", 20)` |
| **Object Initializer** | `sintaxis { }` | `new Estudiante { Nombre = "María" }` |
| **Primary (C# 12)** | `parámetros en clase` | `public class Estudiante(string nombre)` |

### Ejemplo Completo

```csharp
public class Estudiante
{
    // Propiedades
    public string Nombre { get; set; }
    public string Codigo { get; set; }
    public int Edad { get; set; }
    public double Promedio { get; set; }

    // 1. CONSTRUCTOR DEFAULT
    public Estudiante()
    {
        Nombre = "Sin nombre";
        Codigo = "0000000";
        Edad = 18;
        Promedio = 0.0;
    }

    // 2. CONSTRUCTOR PARAMETRIZADO
    public Estudiante(string nombre, string codigo, int edad)
    {
        if (string.IsNullOrWhiteSpace(nombre))
            throw new ArgumentException("Nombre requerido");
        if (edad < 16 || edad > 100)
            throw new ArgumentOutOfRangeException("Edad");

        Nombre = nombre;
        Codigo = codigo;
        Edad = edad;
        Promedio = 0.0;
    }

    // 3. CONSTRUCTOR CON ENCADENAMIENTO (this)
    public Estudiante(string nombre, string codigo)
        : this(nombre, codigo, 18)  // Llama al constructor de 3 params
    {
        // Edad ya se inicializó en 18
    }
}

// USO
var e1 = new Estudiante();                              // Default
var e2 = new Estudiante("María", "2024001", 20);       // Parametrizado
var e3 = new Estudiante("Carlos", "2024002");          // Encadenado (edad=18)
```

### Orden de Ejecución con `this`

```
┌─────────────────────────────────────────────────────────┐
│         ENCADENAMIENTO DE CONSTRUCTORES                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  new Estudiante("Carlos", "2024002")                   │
│       │                                                 │
│       ▼                                                 │
│  ┌─────────────────────────────────────────┐           │
│  │ Estudiante(string, string)             │           │
│  │     : this(n, c, 18)  ────────────────┐ │           │
│  └────────────────────────────────────────┘           │
│       │                                             │    │
│       │ Llama                                       │    │
│       ▼                                             │    │
│  ┌─────────────────────────────────────────┐           │    │
│  │ Estudiante(string, string, int)        │           │    │
│  │     - Validaciones                     │ ◄────────┘    │
│  │     - Asignaciones                     │                │
│  └─────────────────────────────────────────┘                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Static vs Instance

### 🔄 STATIC (Compartido)

Los miembros `static` son **compartidos por TODAS** las instancias de una clase. No requieren un objeto para ser accedidos.

**Características:**
- Una sola copia en memoria (compartida)
- Acceso desde la clase (no desde el objeto)
- Usan la palabra clave `static`
- Viven durante toda la vida del programa

### Instance (Normal)

Los miembros de instancia son **únicos para cada objeto**.

**Características:**
- Una copia por cada objeto
- Acceso desde el objeto
- Viven mientras el objeto exista

### Ejemplo Visual

```csharp
public class Contador
{
    // STATIC: Compartido por todos
    public static int Global = 0;

    // INSTANCE: Único por objeto
    public int Instancia = 0;

    public Contador()
    {
        Global++;     // Incrementa el contador compartido
        Instancia++; // Incrementa el contador de este objeto
    }
}

// Uso
var c1 = new Contador(); // Global=1, Instancia=1
var c2 = new Contador(); // Global=2, Instancia=1
var c3 = new Contador(); // Global=3, Instancia=1

// Static: desde la clase
Console.WriteLine(Contador.Global); // 3

// Instance: desde el objeto
Console.WriteLine(c1.Instancia);   // 1
Console.WriteLine(c2.Instancia);   // 1
Console.WriteLine(c3.Instancia);   // 1
```

### Cuándo Usar Static

| ✅ Usa static para | ❌ NO uses static para |
|---------------------|----------------------|
| Constantes (`Math.PI`) | Datos que varían por objeto |
| Utilidades (`Console.WriteLine`) | Estado del objeto |
| Configuraciones globales | Métodos que usan estado de instancia |
| Contadores compartidos | Propiedades del objeto |

### Ejemplos Comunes

```csharp
// ✅ Static: Constantes matemáticas
public static class Math
{
    public static double PI => 3.14159265358979;
    public static double E => 2.71828182845905;
}

// Uso
double area = Math.PI * radio * radio;

// ✅ Static: Utilidades
public static class Convertidor
{
    public static double CelsiusAFahrenheit(double c) => c * 9 / 5 + 32;
    public static double FahrenheitACelsius(double f) => (f - 32) * 5 / 9;
}

// Uso
double f = Convertidor.CelsiusAFahrenheit(25);

// ❌ Instance: Datos de objeto
public class Estudiante
{
    public string Nombre { get; set; }  // ✅ Instance (cada estudiante tiene su nombre)
    public int Edad { get; set; }      // ✅ Instance (cada estudiante tiene su edad)
}
```

---

## class vs struct

### Diferencias Fundamentales

| Aspecto | class | struct |
|---------|-------|--------|
| **Tipo** | Reference type | Value type |
| **Ubicación** | Heap | Stack |
| **Asignación** | Copia referencia | Copia valor completo |
| **Herencia** | Soporta herencia | No soporta herencia (solo interfaces) |
| **NULL** | Puede ser `null` | No puede ser `null` (usa `Nullable<struct>`) |
| **Constructor** | Sin constructor default | Siempre tiene constructor default |
| **Uso típico** | Objetos grandes, complejos | Datos pequeños, inmutables |

### Ejemplo Comparativo

```csharp
// CLASS (Reference Type)
public class PersonaClass
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
}

// STRUCT (Value Type)
public struct PersonaStruct
{
    public string Nombre { get; set; }
    public int Edad { get; set; }
}

// Uso
var pc1 = new PersonaClass { Nombre = "Juan", Edad = 25 };
var pc2 = pc1;              // Copia REFERENCIA
pc2.Nombre = "María";
Console.WriteLine(pc1.Nombre); // "María" (!!) - ambos referencian el mismo objeto

var ps1 = new PersonaStruct { Nombre = "Juan", Edad = 25 };
var ps2 = ps1;              // Copia VALOR completo
ps2.Nombre = "María";
Console.WriteLine(ps1.Nombre); // "Juan" - independientes
```

### Cuándo Usar struct

Usa `struct` cuando:
- El tipo es **pequeño** (menos de 16 bytes)
- Es **inmutable** (no cambia después de crear)
- Representa **un solo valor** (como un primitivo)
- No necesitas **herencia**

Ejemplos: `Point`, `Size`, `Color`, `DateTime` (partial)

---

**Volver al [índice](./README.md)**
