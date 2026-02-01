# Código - Herencia y Polimorfismo

**IF0100 - Lenguaje de Programación OO II**
*Unidad 1 - Clase 3*

---

## Ejemplos Completos y Ejecutables

Todos los ejemplos están listos para copiar y pegar en un proyecto de consola C# (.NET 8).

---

## 1. Herencia Básica: Sistema de Personas

### Código Completo

```csharp
using System;
using System.Collections.Generic;

namespace HerenciaBasica
{
    // CLASE BASE
    public class Persona
    {
        // Propiedades
        public string Nombre { get; set; }
        public int Edad { get; set; }
        public string Documento { get; set; }

        // Constructor
        public Persona(string nombre, int edad, string documento)
        {
            Nombre = nombre;
            Edad = edad;
            Documento = documento;
        }

        // Método
        public void Saludar()
        {
            Console.WriteLine($"¡Hola! Soy {Nombre}, tengo {Edad} años.");
        }

        public void MostrarInfo()
        {
            Console.WriteLine($"=== DATOS DE PERSONA ===");
            Console.WriteLine($"Nombre: {Nombre}");
            Console.WriteLine($"Edad: {Edad}");
            Console.WriteLine($"Documento: {Documento}");
        }
    }

    // CLASE DERIVADA: Estudiante
    public class Estudiante : Persona
    {
        public string Codigo { get; set; }
        public string Carrera { get; set; }
        public int Semestre { get; set; }

        // Constructor que llama a base
        public Estudiante(string nombre, int edad, string documento,
                         string codigo, string carrera, int semestre)
            : base(nombre, edad, documento)  // Llama constructor de Persona
        {
            Codigo = codigo;
            Carrera = carrera;
            Semestre = semestre;
        }

        public void Estudiar()
        {
            Console.WriteLine($"{Nombre} está estudiando {Carrera} ({Semestre}° semestre)");
        }

        public void MostrarInfoEstudiante()
        {
            MostrarInfo();  // Reutiliza método de Persona
            Console.WriteLine($"Código: {Codigo}");
            Console.WriteLine($"Carrera: {Carrera}");
            Console.WriteLine($"Semestre: {Semestre}");
        }
    }

    // CLASE DERIVADA: Profesor
    public class Profesor : Persona
    {
        public string CodigoEmpleado { get; set; }
        public string Departamento { get; set; }
        public decimal SalarioBase { get; set; }

        public Profesor(string nombre, int edad, string documento,
                       string codigo, string departamento, decimal salario)
            : base(nombre, edad, documento)
        {
            CodigoEmpleado = codigo;
            Departamento = departamento;
            SalarioBase = salario;
        }

        public decimal CalcularSalario()
        {
            return SalarioBase;
        }

        public void Ensenar(string materia)
        {
            Console.WriteLine($"El profesor {Nombre} está enseñando {materia}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== SISTEMA DE HERENCIA BÁSICA ===\n");

            // Crear objetos
            Estudiante est = new Estudiante(
                "María López", 20, "12345678",
                "2024001", "Ingeniería de Sistemas", 2
            );

            Profesor prof = new Profesor(
                "Carlos Ruiz", 45, "87654321",
                "P001", "Ciencias de la Computación", 3500000m
            );

            // Usar métodos heredados
            est.Saludar();
            est.Estudiar();

            Console.WriteLine();

            prof.Saludar();
            prof.Ensenar("Programación Orientada a Objetos");
            Console.WriteLine($"Salario: ${prof.CalcularSalario():N2}");

            Console.WriteLine("\n=== INFORMACIÓN DETALLADA ===\n");
            est.MostrarInfoEstudiante();
            Console.WriteLine();
            prof.MostrarInfo();
            Console.WriteLine($"Empleado: {prof.CodigoEmpleado}");
            Console.WriteLine($"Departamento: {prof.Departamento}");
        }
    }
}
```

### Salida Esperada

```
=== SISTEMA DE HERENCIA BÁSICA ===

¡Hola! Soy María López, tengo 20 años.
María López está estudiando Ingeniería de Sistemas (2° semestre)

¡Hola! Soy Carlos Ruiz, tengo 45 años.
El profesor Carlos Ruiz está enseñando Programación Orientada a Objetos
Salario: $3,500,000.00

=== INFORMACIÓN DETALLADA ===

=== DATOS DE PERSONA ===
Nombre: María López
Edad: 20
Documento: 12345678
Código: 2024001
Carrera: Ingeniería de Sistemas
Semestre: 2

=== DATOS DE PERSONA ===
Nombre: Carlos Ruiz
Edad: 45
Documento: 87654321
Empleado: P001
Departamento: Ciencias de la Computación
```

---

## 2. Polimorfismo: Sistema de Animales

### Código Completo

```csharp
using System;
using System.Collections.Generic;

namespace PolimorfismoAnimales
{
    // CLASE BASE CON MÉTODO VIRTUAL
    public abstract class Animal
    {
        public string Nombre { get; set; }
        public int Edad { get; set; }

        protected Animal(string nombre, int edad)
        {
            Nombre = nombre;
            Edad = edad;
        }

        // VIRTUAL: Puede sobrescribirse, tiene implementación default
        public virtual void HacerSonido()
        {
            Console.WriteLine($"{Nombre} hace un sonido genérico");
        }

        // ABSTRACTO: Hijas DEBEN implementar
        public abstract void Moverse();

        public void Presentarse()
        {
            Console.WriteLine($"Soy {Nombre}, tengo {Edad} años");
        }
    }

    // CLASES DERIVADAS CON OVERRIDE
    public class Perro : Animal
    {
        public string Raza { get; set; }

        public Perro(string nombre, int edad, string raza)
            : base(nombre, edad)
        {
            Raza = raza;
        }

        public override void HacerSonido()
        {
            Console.WriteLine($"🐕 {Nombre} dice: ¡Guau guau!");
        }

        public override void Moverse()
        {
            Console.WriteLine($"🐾 {Nombre} corre en 4 patas");
        }

        public void Buscar()
        {
            Console.WriteLine($"🎾 {Nombre} busca la pelota");
        }
    }

    public class Gato : Animal
    {
        public Gato(string nombre, int edad)
            : base(nombre, edad)
        {
        }

        public override void HacerSonido()
        {
            Console.WriteLine($"🐈 {Nombre} dice: ¡Miau miau!");
        }

        public override void Moverse()
        {
            Console.WriteLine($"🐾 {Nombre} salta sigilosamente");
        }
    }

    public class Pajaro : Animal
    {
        public string Especie { get; set; }

        public Pajaro(string nombre, int edad, string especie)
            : base(nombre, edad)
        {
            Especie = especie;
        }

        public override void HacerSonido()
        {
            Console.WriteLine($"🐦 {Nombre} canta: ¡Pio pio!");
        }

        public override void Moverse()
        {
            Console.WriteLine($"🪶 {Nombre} vuela por el cielo");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== POLIMORFISMO: SISTEMA DE ANIMALES ===\n");

            // POLIMORFISMO: Referencia base, objetos concretos
            Animal[] animales = new Animal[]
            {
                new Perro("Rex", 5, "Pastor Alemán"),
                new Gato("Michi", 3),
                new Pajaro("Piolín", 1, "Canario"),
                new Perro("Toby", 2, "Golden Retriever")
            };

            // Uso polimórfico
            foreach (Animal animal in animales)
            {
                animal.Presentarse();
                animal.HacerSonido();   // Comportamiento según tipo real
                animal.Moverse();       // Comportamiento según tipo real
                Console.WriteLine();
            }

            // Demostración de tipo específico
            Console.WriteLine("=== ACCIONES ESPECÍFICAS ===\n");
            Perro perro = (Perro)animales[0];
            perro.Buscar();
        }
    }
}
```

### Salida Esperada

```
=== POLIMORFISMO: SISTEMA DE ANIMALES ===

Soy Rex, tengo 5 años
🐕 Rex dice: ¡Guau guau!
🐾 Rex corre en 4 patas

Soy Michi, tengo 3 años
🐈 Michi dice: ¡Miau miau!
🐾 Michi salta sigilosamente

Soy Piolín, tengo 1 años
🐦 Piolín canta: ¡Pio pio!
🪶 Piolín vuela por el cielo

Soy Toby, tengo 2 años
🐕 Toby dice: ¡Guau guau!
🐾 Toby corre en 4 patas

=== ACCIONES ESPECÍFICAS ===

🎾 Rex busca la pelota
```

---

## 3. Clases Abstractas: Sistema de Figuras

### Código Completo

```csharp
using System;
using System.Collections.Generic;

namespace FigurasGeometricas
{
    // CLASE ABSTRACTA: No se puede instanciar
    public abstract class Figura
    {
        public string Nombre { get; set; }
        public string Color { get; set; }

        protected Figura(string nombre, string color)
        {
            Nombre = nombre;
            Color = color;
        }

        // MÉTODOS ABSTRACTOS: Hijas DEBEN implementar
        public abstract double CalcularArea();
        public abstract double CalcularPerimetro();

        // MÉTODO CONCRETO: Hijas lo heredan
        public void MostrarInfo()
        {
            Console.WriteLine($"📐 {Nombre} ({Color})");
            Console.WriteLine($"   Área: {CalcularArea():F2} cm²");
            Console.WriteLine($"   Perímetro: {CalcularPerimetro():F2} cm");
        }

        // MÉTODO VIRTUAL CON IMPLEMENTACIÓN DEFAULT
        public virtual void Dibujar()
        {
            Console.WriteLine($"   Dibujando {Nombre}...");
        }
    }

    // IMPLEMENTACIONES CONCRETAS
    public class Circulo : Figura
    {
        public double Radio { get; set; }

        public Circulo(string nombre, string color, double radio)
            : base(nombre, color)
        {
            if (radio <= 0)
                throw new ArgumentException("El radio debe ser positivo");
            Radio = radio;
        }

        public override double CalcularArea()
        {
            return Math.PI * Radio * Radio;
        }

        public override double CalcularPerimetro()
        {
            return 2 * Math.PI * Radio;
        }

        public override void Dibujar()
        {
            Console.WriteLine($"   ⭕ Dibujando círculo de radio {Radio} cm");
        }
    }

    public class Rectangulo : Figura
    {
        public double Base { get; set; }
        public double Altura { get; set; }

        public Rectangulo(string nombre, string color, double @base, double altura)
            : base(nombre, color)
        {
            if (@base <= 0 || altura <= 0)
                throw new ArgumentException("Base y altura deben ser positivas");
            Base = @base;
            Altura = altura;
        }

        public override double CalcularArea()
        {
            return Base * Altura;
        }

        public override double CalcularPerimetro()
        {
            return 2 * (Base + Altura);
        }

        public override void Dibujar()
        {
            Console.WriteLine($"   ⬜ Dibujando rectángulo de {Base}x{Altura} cm");
        }
    }

    public class Triangulo : Figura
    {
        public double Base { get; set; }
        public double Altura { get; set; }
        public double Lado1 { get; set; }
        public double Lado2 { get; set; }
        public double Lado3 { get; set; }

        public Triangulo(string nombre, string color,
                        double @base, double altura,
                        double l1, double l2, double l3)
            : base(nombre, color)
        {
            Base = @base;
            Altura = altura;
            Lado1 = l1;
            Lado2 = l2;
            Lado3 = l3;

            // Validación de desigualdad triangular
            if (l1 + l2 <= l3 || l1 + l3 <= l2 || l2 + l3 <= l1)
                throw new ArgumentException("Los lados no forman un triángulo válido");
        }

        public override double CalcularArea()
        {
            return (Base * Altura) / 2;
        }

        public override double CalcularPerimetro()
        {
            return Lado1 + Lado2 + Lado3;
        }

        public override void Dibujar()
        {
            Console.WriteLine($"   🔺 Dibujando triángulo");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== SISTEMA DE FIGURAS GEOMÉTRICAS ===\n");

            // Crear lista polimórfica
            List<Figura> figuras = new()
            {
                new Circulo("Círculo 1", "Rojo", 5),
                new Rectangulo("Rectángulo 1", "Azul", 4, 6),
                new Triangulo("Triángulo 1", "Verde", 8, 6, 5, 5, 8),
                new Circulo("Círculo 2", "Amarillo", 3)
            };

            double areaTotal = 0;
            double perimetroTotal = 0;

            foreach (Figura figura in figuras)
            {
                figura.MostrarInfo();
                figura.Dibujar();
                Console.WriteLine();

                areaTotal += figura.CalcularArea();
                perimetroTotal += figura.CalcularPerimetro();
            }

            Console.WriteLine("=== RESUMEN ===");
            Console.WriteLine($"Cantidad de figuras: {figuras.Count}");
            Console.WriteLine($"Área total: {areaTotal:F2} cm²");
            Console.WriteLine($"Perímetro total: {perimetroTotal:F2} cm");
        }
    }
}
```

### Salida Esperada

```
=== SISTEMA DE FIGURAS GEOMÉTRICAS ===

📐 Círculo 1 (Rojo)
   Área: 78.54 cm²
   Perímetro: 31.42 cm
   ⭕ Dibujando círculo de radio 5 cm

📐 Rectángulo 1 (Azul)
   Área: 24.00 cm²
   Perímetro: 20.00 cm
   ⬜ Dibujando rectángulo de 4x6 cm

📐 Triángulo 1 (Verde)
   Área: 24.00 cm²
   Perímetro: 18.00 cm
   🔺 Dibujando triángulo

📐 Círculo 2 (Amarillo)
   Área: 28.27 cm²
   Perímetro: 18.85 cm
   ⭕ Dibujando círculo de radio 3 cm

=== RESUMEN ===
Cantidad de figuras: 4
Área total: 154.81 cm²
Perímetro total: 88.27 cm
```

---

## 4. Uso de `base` para Extender Comportamiento

### Código Completo

```csharp
using System;

namespace UsoDeBase
{
    // SISTEMA DE NÓMINA
    public class Empleado
    {
        public string Nombre { get; set; }
        public string Cargo { get; set; }
        public decimal SalarioBase { get; set; }

        public Empleado(string nombre, string cargo, decimal salarioBase)
        {
            Nombre = nombre;
            Cargo = cargo;
            SalarioBase = salarioBase;
        }

        public virtual decimal CalcularSalario()
        {
            return SalarioBase;
        }

        public virtual string GenerarReporte()
        {
            return $"Empleado: {Nombre}\n" +
                   $"Cargo: {Cargo}\n" +
                   $"Salario: ${SalarioBase:N2}";
        }
    }

    public class Vendedor : Empleado
    {
        public decimal Comision { get; set; }
        public decimal VentasTotales { get; set; }

        public Vendedor(string nombre, decimal salarioBase,
                       decimal comision, decimal ventas)
            : base(nombre, "Vendedor", salarioBase)
        {
            Comision = comision;
            VentasTotales = ventas;
        }

        // EXTENDIDO: Llama a base y AGREGA
        public override decimal CalcularSalario()
        {
            decimal salarioBase = base.CalcularSalario();
            decimal comisionTotal = VentasTotales * (Comision / 100);
            return salarioBase + comisionTotal;
        }

        // EXTENDIDO: Llama a base y AGREGA
        public override string GenerarReporte()
        {
            string reporteBase = base.GenerarReporte();
            return reporteBase + $"\n" +
                   $"Ventas: ${VentasTotales:N2}\n" +
                   $"Comisión: {Comision}%\n" +
                   $"Total: ${CalcularSalario():N2}";
        }
    }

    public class Gerente : Empleado
    {
        public decimal Bonificacion { get; set; }
        public List<string> Subordinados { get; set; }

        public Gerente(string nombre, decimal salarioBase,
                      decimal bonificacion, List<string> subordinados)
            : base(nombre, "Gerente", salarioBase)
        {
            Bonificacion = bonificacion;
            Subordinados = subordinados;
        }

        public override decimal CalcularSalario()
        {
            return base.CalcularSalario() + Bonificacion;
        }

        public override string GenerarReporte()
        {
            string reporteBase = base.GenerarReporte();
            string subordinados = string.Join(", ", Subordinados);
            return reporteBase + $"\n" +
                   $"Bonificación: ${Bonificacion:N2}\n" +
                   $"Subordinados: {subordinados}\n" +
                   $"Total: ${CalcularSalario():N2}";
        }
    }

    class Program
    {
        static void Main(string[] args)
    {
        Console.WriteLine("=== SISTEMA DE NÓMINA ===\n");

        Empleado emp = new Empleado("Juan Pérez", "Auxiliar", 2000000m);
        Vendedor ven = new Vendedor("María López", 1800000m, 5, 15000000m);
        Gerente ger = new Gerente("Carlos Ruiz", 3500000m, 1200000m,
                                  new List<string> { "Ana", "Luis", "Pedro" });

        Empleado[] empleados = { emp, ven, ger };

        foreach (Empleado empleado in empleados)
        {
            Console.WriteLine(empleado.GenerarReporte());
            Console.WriteLine(new string('-', 40));
        }

        Console.WriteLine("\n=== RESUMEN DE NÓMINA ===");
        decimal totalNomina = 0;
        foreach (Empleado empleado in empleados)
        {
            totalNomina += empleado.CalcularSalario();
        }
        Console.WriteLine($"Total nómina: ${totalNomina:N2}");
    }
    }
}
```

### Salida Esperada

```
=== SISTEMA DE NÓMINA ===

Empleado: Juan Pérez
Cargo: Auxiliar
Salario: $2,000,000.00
----------------------------------------
Empleado: María López
Cargo: Vendedor
Salario: $1,800,000.00
Ventas: $15,000,000.00
Comisión: 5%
Total: $2,550,000.00
----------------------------------------
Empleado: Carlos Ruiz
Cargo: Gerente
Salario: $3,500,000.00
Bonificación: $1,200,000.00
Subordinados: Ana, Luis, Pedro
Total: $4,700,000.00
----------------------------------------

=== RESUMEN DE NÓMINA ===
Total nómina: $9,250,000.00
```

---

## 5. Ejemplo con `sealed`: Clase No Heredable

### Código Completo

```csharp
using System;

namespace ClaseSellada
{
    // CLASE SELLADA: No se puede heredar
    public sealed class SeguridadSocial
    {
        public string Numero { get; set; }
        public decimal Saldo { get; set; }
        private string _claveAdministrativa = "SECRET";

        public SeguridadSocial(string numero, decimal saldo)
        {
            Numero = numero;
            Saldo = saldo;
        }

        public void ConsultarSaldo()
        {
            Console.WriteLine($"Saldo disponible: ${Saldo:N2}");
        }

        private void OperacionInterna()
        {
            // Solo accesible dentro de la clase
        }
    }

    // ❌ ESTO DARÍA ERROR DE COMPILACIÓN:
    // public class HackeoSS : SeguridadSocial
    // {
    //     // No se puede heredar de una clase sealed
    // }

    // EJEMPLO DE MÉTODO SELLADO
    public class Base
    {
        public virtual void Metodo()
        {
            Console.WriteLine("Método base");
        }
    }

    public class Derivada : Base
    {
        public sealed override void Metodo()
        {
            Console.WriteLine("Método final - no se puede sobrescribir más");
            base.Metodo();
        }
    }

    // ❌ ESTO DARÍA ERROR:
    // public class TerceraNivel : Derivada
    // {
    //     public override void Metodo()
    //     {
    //         // Error: no puede sobrescribir un método sealed
    //     }
    // }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== CLASE SELLADA ===\n");

            SeguridadSocial ss = new SeguridadSocial("123-456-789", 5000000m);
            ss.ConsultarSaldo();

            Console.WriteLine("\n=== MÉTODO SELLADO ===\n");
            Derivada d = new Derivada();
            d.Metodo();
        }
    }
}
```

---

## Cómo Ejecutar Estos Ejemplos

### Opción 1: Visual Studio

1. Crear nuevo proyecto **Console App** (C#)
2. Reemplazar `Program.cs` con el código deseado
3. Press `F5` o clic en **Iniciar**

### Opción 2: .NET CLI

```bash
# Crear proyecto
dotnet new console -n HerenciaEjemplo
cd HerenciaEjemplo

# Copiar el código en Program.cs

# Ejecutar
dotnet run
```

### Opción 3: Compilación Manual

```bash
# Guardar como Program.cs
csc Program.cs
Program.exe
```

---

**Última actualización:** 2026-02-01
