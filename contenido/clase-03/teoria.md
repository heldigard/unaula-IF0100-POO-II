# Teoría - Herencia y Polimorfismo

**IF0100 - Lenguaje de Programación OO II**
*Unidad 1 - Clase 3*

---

## 1. Herencia: Fundamentos

### ¿Qué es la Herencia?

La herencia es uno de los pilares fundamentales de la Programación Orientada a Objetos. Permite crear una nueva clase (clase derivada o hija) que **adquiere** las características y comportamientos de una clase existente (clase base o padre).

### Terminología Clave

| Término | Sinónimos | Descripción |
|---------|-----------|-------------|
| **Clase Base** | Padre, Superclase | La clase que se hereda |
| **Clase Derivada** | Hija, Subclase | La clase que hereda |
| **`:`** | Operador herencia | Sintaxis C# para herencia |
| **`base`** | Referencia padre | Para acceder a miembros de la clase padre |
| **`protected`** | Protegido | Accesible solo en la clase y sus hijas |

### Beneficios de la Herencia

1. **Reutilización de Código**: No repitas lógica común
2. **Jerarquías Lógicas**: Modela relaciones del mundo real
3. **Extensibilidad**: Fácil agregar nuevas funcionalidades
4. **Mantenimiento Centralizado**: Cambios en un lugar afectan a todos

### Regla de Oro: Máximo 3 Niveles

```
✅ BUENO: Animal → Mamífero → Perro (3 niveles)
❌ MALO: A → B → C → D → E → F (6 niveles, difícil de mantener)
```

---

## 2. Sintaxis de Herencia en C#

### Declaración Básica

```csharp
// Clase Base
public class Persona
{
    public string Nombre { get; set; }
    public int Edad { get; set; }

    public void Saludar()
    {
        Console.WriteLine($"Hola, soy {Nombre}");
    }
}

// Clase Derivada (usa el operador :)
public class Estudiante : Persona
{
    public string Codigo { get; set; }
    public string Carrera { get; set; }

    public void Estudiar()
    {
        Console.WriteLine($"{Nombre} estudia {Carrera}");
    }
}
```

### Modificadores de Acceso en Herencia

| Modificador | Clase Base | Clase Derivada | Otras Clases |
|-------------|-----------|----------------|--------------|
| `public` | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `internal` | ✅ | ✅* | ✅* |
| `private` | ✅ | ❌ | ❌ |
| `protected internal` | ✅ | ✅ | ✅* |

*Depende del ensamblado

### Qué NO se Hereda

- ❌ **Constructores**: No se heredan, pero pueden llamarse con `base`
- ❌ **Miembros privados**: Inaccesibles desde clases derivadas
- ✅ **Métodos públicos**: Se heredan completamente
- ✅ **Miembros protegidos**: Accesibles solo en la jerarquía

---

## 3. La Palabra Clave `base`

### Propósito

`base` permite acceder a miembros de la clase padre desde la clase hija. Se usa para:

1. **Llamar constructores de la clase base**
2. **Extender métodos existentes** (no reemplazarlos)
3. **Reutilizar código validado**

### Llamada a Constructor Base

```csharp
public class Estudiante : Persona
{
    public string Codigo { get; set; }

    // Constructor con llamada a base
    public Estudiante(string nombre, int edad, string codigo)
        : base(nombre, edad)  // ← Primero se ejecuta el constructor de Persona
    {
        Codigo = codigo;       // ← Luego se inicializan los miembros propios
    }
}
```

### Orden de Ejecución

```
1. Constructor de Persona (base)
2. Constructor de Estudiante (derivada)
3. Resto del código del constructor de Estudiante
```

### Extender Métodos con `base`

```csharp
public class Empleado
{
    public virtual decimal CalcularSalario()
    {
        return SalarioBase;
    }
}

public class Vendedor : Empleado
{
    public decimal Comision { get; set; }

    public override decimal CalcularSalario()
    {
        // Llama al método padre y AGREGA funcionalidad
        return base.CalcularSalario() + Comision;
    }
}
```

---

## 4. Herencia Transitiva

La herencia es transitiva: si `C` hereda de `B`, y `B` hereda de `A`, entonces `C` hereda todo de `A` y `B`.

```
┌─────────────────────────────────┐
│     PERSONA (Nivel 1)           │
│  - Nombre, Documento            │
│  - Saludar()                    │
└─────────────┬───────────────────┘
              │
┌─────────────┴───────────────────┐
│     EMPLEADO (Nivel 2)          │
│  - CódigoEmpleado               │
│  - FechaContratación            │
│  - CalcularSalario()            │
└─────────────┬───────────────────┘
              │
┌─────────────┴───────────────────┐
│     PROFESOR (Nivel 3)          │
│  - Especialidad                 │
│  - Materias[]                   │
│  - TítuloPostgrado              │
└─────────────────────────────────┘
```

**Resultado**: `Profesor` tiene acceso a TODO de `Persona` y `Empleado`.

---

## 5. Polimorfismo: Un Nombre, Múltiples Formas

### Concepto

El polimorfismo permite que un mismo mensaje (llamada a método) tenga **diferentes comportamientos** según el objeto que lo recibe.

### Palabras Clave

| Palabra | Propósito | Cuándo Usar |
|---------|-----------|-------------|
| `virtual` | El método PUEDE ser sobrescrito | Tienes una implementación default |
| `override` | Sobrescribe un método virtual/abstract | Quieres comportamientos específicos |
| `abstract` | Obliga a las hijas a implementar | No tienes implementación útil |

### Analogía

```
Mensaje: "¡Muévete!"
  🐕 Perro → Corre
  🐈 Gato → Salta
  🐟 Pez → Nada
  🦅 Águila → Vuela
```

### Implementación

```csharp
// Clase base con método virtual
public class Animal
{
    public string Nombre { get; set; }

    public virtual void HacerSonido()
    {
        Console.WriteLine("Sonido genérico");
    }
}

// Clases derivadas con override
public class Perro : Animal
{
    public override void HacerSonido()
    {
        Console.WriteLine("¡Guau guau!");
    }
}

public class Gato : Animal
{
    public override void HacerSonido()
    {
        Console.WriteLine("¡Miau miau!");
    }
}
```

### Uso Polimórfico

```csharp
// Referencia base, objeto concreto
Animal a1 = new Perro() { Nombre = "Rex" };
Animal a2 = new Gato() { Nombre = "Michi" };

a1.HacerSonido();  // "¡Guau guau!" (comportamiento de Perro)
a2.HacerSonido();  // "¡Miau miau!" (comportamiento de Gato)

// Colección polimórfica
List<Animal> animales = new()
{
    new Perro { Nombre = "Rex" },
    new Gato { Nombre = "Michi" },
    new Perro { Nombre = "Toby" }
};

foreach (Animal a in animales)
{
    a.HacerSonido();  // Cada uno se comporta según su tipo
}
```

---

## 6. Clases y Métodos Abstractos

### `virtual` vs `abstract`

| Característica | `virtual` | `abstract` |
|----------------|-----------|------------|
| Implementación | Tiene código por defecto | Sin implementación |
| Obligatoriedad | Hijas PUEDEN sobrescribir | Hijas DEBEN implementar |
| Instanciación | ✅ Se puede crear instancias | ❌ NO se puede instanciar |

### Cuándo Usar `abstract`

✅ Hay comportamiento común pero implementaciones diferentes
✅ Quieres forzar un diseño en las clases hijas
✅ La clase base es solo un "contrato" o plantilla

### Ejemplo de Clase Abstracta

```csharp
// abstract: No se puede instanciar
public abstract class Figura
{
    public string Nombre { get; set; }
    public string Color { get; set; }

    // abstract: Hijas DEBEN implementar
    public abstract double CalcularArea();
    public abstract double CalcularPerimetro();

    // Método concreto: hijas lo heredan tal cual
    public void MostrarInfo()
    {
        Console.WriteLine($"Figura: {Nombre}");
        Console.WriteLine($"Área: {CalcularArea():F2}");
    }
}
```

### Implementación en Clases Derivadas

```csharp
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
```

### Uso

```csharp
// ✅ Correcto: referencia base, objeto concreto
Figura f1 = new Circulo { Radio = 5 };

// ❌ Error: no se puede instanciar clase abstracta
// Figura f = new Figura();
```

---

## 7. Palabra Clave `sealed`

### Propósito

`sealed` previene que una clase sea heredada o que un método sea sobrescrito.

### Usos Comunes

| Situación | Ejemplo |
|-----------|---------|
| Clase no diseñada para herencia | `String`, `DateTime` |
| Proteger lógica crítica | Clases de seguridad |
| Finalizar cadena de override | Método de cálculo final |

### Ejemplo

```csharp
// sealed: Nadie puede heredar de esta clase
public sealed class SeguridadSocial
{
    public string Numero { get; set; }
    public decimal Saldo { get; set; }
}

// ❌ Error de compilación
// public class HackeoSS : SeguridadSocial { }
```

### Método Sealed

```csharp
public class A
{
    public virtual void Metodo() { }
}

public class B : A
{
    public sealed override void Metodo()
    {
        // Implementación final
        base.Metodo();
    }
}

public class C : B
{
    // ❌ Error: no puede sobrescribir Metodo()
    // public override void Metodo() { }
}
```

---

## 8. Principio de Sustitución de Liskov (LSP)

### Enunciado

> **"Las clases derivadas deben poder sustituir a sus clases base sin alterar el comportamiento del programa."**

### Buena Herencia (cumple LSP)

```
Estudiante → Persona ✅
Perro → Animal ✅
Círculo → Figura ✅
```

### Mala Herencia (violación LSP)

```
Avión → Vehículo ❌
# Tiene motor, pero su comportamiento es diferente (vuela vs rueda)

Reloj → Círculo ❌
# Tiene forma circular, pero no es una figura geométrica
```

### Ejemplo Clásico: Cuadrado vs Rectángulo

```csharp
// Matemáticamente: Un cuadrado ES UN rectángulo
// En POO: ¡Puede violar LSP!

class Rectangulo
{
    public virtual int Ancho { get; set; }
    public virtual int Alto { get; set; }

    public int Area() => Ancho * Alto;
}

class Cuadrado : Rectangulo
{
    // ⚠️ PROBLEMA: En cuadrado, ancho = alto
    public override int Ancho
    {
        get => base.Ancho;
        set { base.Ancho = base.Alto = value; }
    }

    public override int Alto
    {
        get => base.Alto;
        set { base.Ancho = base.Alto = value; }
    }
}

// Uso que falla
Rectangulo r = new Cuadrado();
r.Ancho = 5;
r.Alto = 10;
Console.WriteLine(r.Area());  // ¿Esperas 50 o 100?
```

### Pregunta Clave para Validar LSP

**¿Puedo sustituir la clase hija por la padre sin romper nada?**

- Si la respuesta es SÍ → ✅ Buena herencia
- Si la respuesta es NO → ❌ Violación de LSP

> 💡 **LSP es sobre COMPORTAMIENTO**, no sobre taxonomía o forma.

---

## 9. Errores Comunes y Debugging

### Error 1: Olvidar `virtual` en la clase base

```csharp
// ❌ Error
public class Padre
{
    public void Metodo() { }  // Falta virtual
}

public class Hija : Padre
{
    public override void Metodo() { }  // Error: nada que sobrescribir
}
```

**Solución**: Agregar `virtual` al método de la clase base.

### Error 2: Intentar instanciar clase abstracta

```csharp
// ❌ Error
Figura f = new Figura();  // Figura es abstract
```

**Solución**: Crear una clase concreta que herede de la abstracta.

### Error 3: Violación accidental de LSP

```csharp
// ⚠️ Peligroso
class Ave
{
    public virtual void Volar() => Console.WriteLine("Vuela");
}

class Pinguino : Ave
{
    public override void Volar() => throw new Exception("No puedo volar");
}
```

**Solución**: Usar interfaces o separar comportamientos.

---

## 10. Mejores Prácticas

1. **Prefer composición sobre herencia**: Cuando no haya relación clara "ES-UN"
2. **Máximo 3 niveles de profundidad**: Mantén la jerarquía simple
3. **Usa `abstract` para contratos**: Fuerza implementación en hijas
4. **Usa `sealed` para clases finales**: Previente herencia inesperada
5. **Valida LSP**: Pregunta si la hija puede sustituir al padre
6. **Documenta jerarquías**: Explica por qué existe la herencia

---

**Última actualización:** 2026-02-01
