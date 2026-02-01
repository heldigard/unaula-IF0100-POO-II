# Código - Sobrecarga, Sobreescritura y Modelado BD

**IF0100 - Lenguaje de Programación OO II**
*Unidad 1 - Clase 4*

---

## 1. Sobrecarga de Métodos y Constructores

### Sistema de Estudiantes con Constructores Sobrecargados

```csharp
using System;

namespace SobrecargaConstructores
{
    public class Estudiante
    {
        public string Nombre { get; set; }
        public string Codigo { get; set; }
        public int Edad { get; set; }
        public string Carrera { get; set; }

        // Constructor 1: Principal con todos los parámetros
        public Estudiante(string nombre, string codigo, int edad, string carrera)
        {
            Nombre = nombre;
            Codigo = codigo;
            Edad = edad;
            Carrera = carrera;
            Console.WriteLine($"Creado estudiante: {Nombre} ({Carrera})");
        }

        // Constructor 2: Parcial (edad default 18)
        public Estudiante(string nombre, string codigo, string carrera)
            : this(nombre, codigo, 18, carrera) { }

        // Constructor 3: Solo nombre y código
        public Estudiante(string nombre, string codigo)
            : this(nombre, codigo, 18, "Sin carrera") { }

        // Constructor 4: Vacío
        public Estudiante()
            : this("Sin nombre", "0000000") { }

        // MÉTODOS SOBRECARGADOS
        public void Estudiar()
        {
            Console.WriteLine($"{Nombre} está estudiando");
        }

        public void Estudiar(string materia)
        {
            Console.WriteLine($"{Nombre} está estudiando {materia}");
        }

        public void Estudiar(string materia, int horas)
        {
            Console.WriteLine($"{Nombre} está estudiando {materia} por {horas} horas");
        }

        public void MostrarInfo()
        {
            Console.WriteLine($"=== {Nombre} ===");
            Console.WriteLine($"Código: {Codigo}");
            Console.WriteLine($"Edad: {Edad}");
            Console.WriteLine($"Carrera: {Carrera}");
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("=== SOBRECARGA DE CONSTRUCTORES ===\n");

            // Diferentes formas de crear el mismo objeto
            Estudiante e1 = new Estudiante("María López", "2024001", 20, "Ingeniería");
            Estudiante e2 = new Estudiante("Carlos Ruiz", "2024002", "Medicina");
            Estudiante e3 = new Estudiante("Ana Gómez", "2024003");
            Estudiante e4 = new Estudiante();

            Console.WriteLine("\n=== MÉTODOS SOBRECARGADOS ===\n");

            e2.Estudiar();
            e2.Estudiar("Anatomía");
            e2.Estudiar("Fisiología", 4);
        }
    }
}
```

### Salida

```
=== SOBRECARGA DE CONSTRUCTORES ===

Creado estudiante: María López (Ingeniería)
Creado estudiante: Carlos Ruiz (Medicina)
Creado estudiante: Ana Gómez (Sin carrera)
Creado estudiante: Sin nombre (Sin carrera)

=== MÉTODOS SOBRECARGADOS ===

Carlos Ruiz está estudiando
Carlos Ruiz está estudiando Anatomía
Carlos Ruiz está estudiando Fisiología por 4 horas
```

---

## 2. Sobrecarga de Operadores

### Clase Fracción con Operadores Sobrecargados

```csharp
using System;

namespace SobrecargaOperadores
{
    public class Fraccion
    {
        public int Numerador { get; set; }
        public int Denominador { get; set; }

        public Fraccion(int numerador, int denominador)
        {
            if (denominador == 0)
                throw new ArgumentException("El denominador no puede ser 0");
            Numerador = numerador;
            Denominador = denominador;
            Simplificar();
        }

        // SOBRECARGA DE OPERADORES ARITMÉTICOS
        public static Fraccion operator +(Fraccion a, Fraccion b)
        {
            int num = a.Numerador * b.Denominador + b.Numerador * a.Denominador;
            int den = a.Denominador * b.Denominador;
            return new Fraccion(num, den);
        }

        public static Fraccion operator -(Fraccion a, Fraccion b)
        {
            int num = a.Numerador * b.Denominador - b.Numerador * a.Denominador;
            int den = a.Denominador * b.Denominador;
            return new Fraccion(num, den);
        }

        public static Fraccion operator *(Fraccion a, Fraccion b)
        {
            return new Fraccion(a.Numerador * b.Numerador, a.Denominador * b.Denominador);
        }

        public static Fraccion operator /(Fraccion a, Fraccion b)
        {
            return new Fraccion(a.Numerador * b.Denominador, a.Denominador * b.Numerador);
        }

        // SOBRECARGA DE OPERADORES DE COMPARACIÓN
        public static bool operator ==(Fraccion a, Fraccion b)
        {
            if (a is null) return b is null;
            return a.Numerador * b.Denominador == b.Numerador * a.Denominador;
        }

        public static bool operator !=(Fraccion a, Fraccion b) => !(a == b);

        public static bool operator <(Fraccion a, Fraccion b)
        {
            return a.Numerador * b.Denominador < b.Numerador * a.Denominador;
        }

        public static bool operator >(Fraccion a, Fraccion b)
        {
            return a.Numerador * b.Denominador > b.Numerador * a.Denominador;
        }

        // Sobrescribir Equals y GetHashCode para consistencia
        public override bool Equals(object obj) => obj is Fraccion f && this == f;
        public override int GetHashCode() => (Numerador, Denominador).GetHashCode();

        public override string ToString() => $"{Numerador}/{Denominador}";

        // Método auxiliar para simplificar
        private void Simplificar()
        {
            int mcd = MCD(Numerador, Denominador);
            Numerador /= mcd;
            Denominador /= mcd;
        }

        private static int MCD(int a, int b) => b == 0 ? a : MCD(b, a % b);
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("=== SOBRECARGA DE OPERADORES ===\n");

            Fraccion f1 = new Fraccion(1, 2);  // 1/2
            Fraccion f2 = new Fraccion(1, 3);  // 1/3
            Fraccion f3 = new Fraccion(2, 4);  // 2/4 = 1/2 simplificado

            Console.WriteLine($"f1 = {f1}");
            Console.WriteLine($"f2 = {f2}");
            Console.WriteLine($"f3 = {f3}");

            // Operadores aritméticos
            Console.WriteLine($"\n{f1} + {f2} = {f1 + f2}");
            Console.WriteLine($"{f1} - {f2} = {f1 - f2}");
            Console.WriteLine($"{f1} * {f2} = {f1 * f2}");
            Console.WriteLine($"{f1} / {f2} = {f1 / f2}");

            // Operadores de comparación
            Console.WriteLine($"\n{f1} == {f3}: {f1 == f3}");  // True (1/2 == 2/4)
            Console.WriteLine($"{f1} == {f2}: {f1 == f2}");  // False
            Console.WriteLine($"{f1} > {f2}: {f1 > f2}");    // True
        }
    }
}
```

### Salida

```
=== SOBRECARGA DE OPERADORES ===

f1 = 1/2
f2 = 1/3
f3 = 1/2

1/2 + 1/3 = 5/6
1/2 - 1/3 = 1/6
1/2 * 1/3 = 1/6
1/2 / 1/3 = 3/2

1/2 == 1/2: True
1/2 == 1/3: False
1/2 > 1/3: True
```

---

## 3. Clase Punto con Operadores de Comparación

```csharp
using System;

namespace SobrecargaPunto
{
    public class Punto
    {
        public int X { get; set; }
        public int Y { get; set; }

        public Punto(int x, int y)
        {
            X = x;
            Y = y;
        }

        // Sobrecarga de +
        public static Punto operator +(Punto a, Punto b)
        {
            return new Punto(a.X + b.X, a.Y + b.Y);
        }

        // Sobrecarga de -
        public static Punto operator -(Punto a, Punto b)
        {
            return new Punto(a.X - b.X, a.Y - b.Y);
        }

        // Sobrecarga de ==
        public static bool operator ==(Punto a, Punto b)
        {
            if (a is null) return b is null;
            return a.X == b.X && a.Y == b.Y;
        }

        // Sobrecarga de != (siempre en pareja)
        public static bool operator !=(Punto a, Punto b) => !(a == b);

        // Sobrescribir Equals
        public override bool Equals(object obj)
            => obj is Punto p && this == p;

        // Sobrescribir GetHashCode
        public override int GetHashCode()
            => (X, Y).GetHashCode();

        public override string ToString()
            => $"({X}, {Y})";

        // Método para calcular distancia
        public double Distancia(Punto otro)
        {
            int dx = X - otro.X;
            int dy = Y - otro.Y;
            return Math.Sqrt(dx * dx + dy * dy);
        }
    }

    class Program
    {
        static void Main()
        {
            Punto p1 = new Punto(3, 4);
            Punto p2 = new Punto(6, 8);
            Punto p3 = new Punto(3, 4);

            Console.WriteLine($"p1 = {p1}");
            Console.WriteLine($"p2 = {p2}");
            Console.WriteLine($"p3 = {p3}");

            Console.WriteLine($"\np1 + p2 = {p1 + p2}");
            Console.WriteLine($"p2 - p1 = {p2 - p1}");

            Console.WriteLine($"\np1 == p3: {p1 == p3}");
            Console.WriteLine($"p1 == p2: {p1 == p2}");
            Console.WriteLine($"p1 != p2: {p1 != p2}");

            Console.WriteLine($"\nDistancia p1 a p2: {p1.Distancia(p2):F2}");
        }
    }
}
```

---

## 4. Modelado Objeto-Relacional

### Sistema Universitario Completo

```csharp
using System;
using System.Collections.Generic;

namespace ModeloUniversidad
{
    // ENTIDADES DEL MODELO

    public class Carrera
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public int DuracionSemestres { get; set; }

        // Relación 1:N con Estudiantes
        public List<Estudiante> Estudiantes { get; set; } = new();

        public override string ToString() => $"[{Id}] {Nombre} ({DuracionSemestres} semestres)";
    }

    public class Estudiante
    {
        public string Codigo { get; set; }          // PK
        public string Nombre { get; set; }
        public string Email { get; set; }
        public int Edad { get; set; }

        // FK para relación 1:N
        public int CarreraId { get; set; }

        // Navegación 1:N
        public Carrera Carrera { get; set; }

        // Relación N:M a través de Inscripcion
        public List<Inscripcion> Inscripciones { get; set; } = new();

        public override string ToString() => $"[{Codigo}] {Nombre} ({Edad} años)";
    }

    public class Materia
    {
        public int Id { get; set; }                 // PK
        public string Nombre { get; set; }
        public int Creditos { get; set; }
        public string Semestre { get; set; }

        // Relación N:M a través de Inscripcion
        public List<Inscripcion> Inscripciones { get; set; } = new();

        public override string ToString() => $"[{Id}] {Nombre} ({Creditos} créditos)";
    }

    // TABLA INTERMEDIA PARA RELACIÓN N:M
    public class Inscripcion
    {
        public int Id { get; set; }                 // PK
        public DateTime FechaInscripcion { get; set; }
        public decimal NotaFinal { get; set; }

        // FKs para relación N:M
        public string EstudianteCodigo { get; set; }
        public int MateriaId { get; set; }

        // Navegación
        public Estudiante Estudiante { get; set; }
        public Materia Materia { get; set; }

        public override string ToString()
            => $"{Estudiante?.Nombre} - {Materia?.Nombre}: {NotaFinal}";
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("=== SISTEMA UNIVERSITARIO ===\n");

            // Crear carreras
            Carrera ingSistemas = new()
            {
                Id = 1,
                Nombre = "Ingeniería de Sistemas",
                DuracionSemestres = 10
            };

            Carrera medicina = new()
            {
                Id = 2,
                Nombre = "Medicina",
                DuracionSemestres = 12
            };

            // Crear materias
            Materia poo = new() { Id = 1, Nombre = "Programación OO", Creditos = 4, Semestre = "2026-I" };
            Materia bd = new() { Id = 2, Nombre = "Bases de Datos", Creditos = 3, Semestre = "2026-I" };
            Materia web = new() { Id = 3, Nombre = "Desarrollo Web", Creditos = 4, Semestre = "2026-II" };

            // Crear estudiantes
            Estudiante maria = new()
            {
                Codigo = "2024001",
                Nombre = "María López",
                Email = "maria@email.com",
                Edad = 20,
                CarreraId = 1,
                Carrera = ingSistemas
            };

            Estudiante carlos = new()
            {
                Codigo = "2024002",
                Nombre = "Carlos Ruiz",
                Email = "carlos@email.com",
                Edad = 19,
                CarreraId = 1,
                Carrera = ingSistemas
            };

            // Agregar estudiantes a las carreras (relación 1:N)
            ingSistemas.Estudiantes.Add(maria);
            ingSistemas.Estudiantes.Add(carlos);

            // Crear inscripciones (relación N:M)
            Inscripcion insc1 = new()
            {
                Id = 1,
                FechaInscripcion = DateTime.Now,
                NotaFinal = 4.5m,
                EstudianteCodigo = maria.Codigo,
                MateriaId = poo.Id,
                Estudiante = maria,
                Materia = poo
            };

            Inscripcion insc2 = new()
            {
                Id = 2,
                FechaInscripcion = DateTime.Now,
                NotaFinal = 3.8m,
                EstudianteCodigo = maria.Codigo,
                MateriaId = bd.Id,
                Estudiante = maria,
                Materia = bd
            };

            Inscripcion insc3 = new()
            {
                Id = 3,
                FechaInscripcion = DateTime.Now,
                NotaFinal = 0m, // Aún cursando
                EstudianteCodigo = carlos.Codigo,
                MateriaId = poo.Id,
                Estudiante = carlos,
                Materia = poo
            };

            // Agregar inscripciones a estudiantes y materias
            maria.Inscripciones.Add(insc1);
            maria.Inscripciones.Add(insc2);
            poo.Inscripciones.Add(insc1);
            bd.Inscripciones.Add(insc2);

            carlos.Inscripciones.Add(insc3);
            poo.Inscripciones.Add(insc3);

            // DEMOSTRACIÓN DE RELACIONES
            Console.WriteLine("=== RELACIÓN 1:N: Carrera → Estudiantes ===\n");
            Console.WriteLine($"{ingSistemas.Nombre}:");
            foreach (var est in ingSistemas.Estudiantes)
            {
                Console.WriteLine($"  - {est}");
            }

            Console.WriteLine("\n=== RELACIÓN N:M: Estudiantes ↔ Materias ===\n");
            Console.WriteLine("Inscripciones de María López:");
            foreach (var insc in maria.Inscripciones)
            {
                Console.WriteLine($"  - {insc.Materia.Nombre} | Nota: {insc.NotaFinal}");
            }

            Console.WriteLine($"\nEstudiantes inscritos en {poo.Nombre}:");
            foreach (var insc in poo.Inscripciones)
            {
                Console.WriteLine($"  - {insc.Estudiante.Nombre} | Nota: {insc.NotaFinal}");
            }

            // SQL equivalente
            Console.WriteLine("\n=== SQL EQUIVALENTE ===\n");
            Console.WriteLine("-- Tablas");
            Console.WriteLine("CREATE TABLE Carreras (Id INT PRIMARY KEY, Nombre VARCHAR(100));");
            Console.WriteLine("CREATE TABLE Estudiantes (Codigo VARCHAR(20) PRIMARY KEY, CarreraId INT FOREIGN KEY REFERENCES Carreras(Id));");
            Console.WriteLine("CREATE TABLE Materias (Id INT PRIMARY KEY);");
            Console.WriteLine("CREATE TABLE Inscripciones (Id INT PRIMARY KEY, EstudianteCodigo VARCHAR(20), MateriaId INT, FOREIGN KEY (EstudianteCodigo) REFERENCES Estudiantes(Codigo), FOREIGN KEY (MateriaId) REFERENCES Materias(Id));");
        }
    }
}
```

### Salida

```
=== SISTEMA UNIVERSITARIO ===

=== RELACIÓN 1:N: Carrera → Estudiantes ===

[1] Ingeniería de Sistemas (10 semestres):
  - [2024001] María López (20 años)
  - [2024002] Carlos Ruiz (19 años)

=== RELACIÓN N:M: Estudiantes ↔ Materias ===

Inscripciones de María López:
  - Programación OO | Nota: 4.5
  - Bases de Datos | Nota: 3.8

Estudiantes inscritos en Programación OO:
  - María López | Nota: 4.5
  - Carlos Ruiz | Nota: 0
```

---

**Última actualización:** 2026-02-01
