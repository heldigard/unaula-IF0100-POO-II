# Clase 01 - Código Completo
## Introducción a C# y .NET

**IF0100 - Lenguaje de Programación OO II** | Unidad 1

---

## Tabla de Contenidos

- [Generics y Performance](#generics-y-performance)
- [Value vs Reference Types - Demo Completa](#value-vs-reference-types---demo-completa)
- [Nullable en Escenario Real](#nullable-en-escenario-real-bd)
- [StringBuilder vs String Concatenation](#stringbuilder-vs-string-concatenation)
- [C# 12 Primary Constructors](#primary-constructors)
- [Collection Expressions](#collection-expressions)
- [Pattern Matching](#pattern-matching)
- [Ejemplo: Sistema de Calificaciones Completo](#ejemplo-sistema-de-calificaciones-completo)

---

## Generics y Performance

### Demo: ArrayList vs List<int>

Este código demuestra por qué `List<T>` es superior a `ArrayList`.

```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;

namespace GenericosDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== GENERICS PERFORMANCE DEMO ===\n");

            // 1. DEMOSTRACIÓN DE SEGURIDAD DE TIPOS
            Console.WriteLine("1. TYPE SAFETY:");
            Console.WriteLine("-------------------");

            // ❌ ANTES: ArrayList (sin type safety)
            ArrayList arrayList = new ArrayList();
            arrayList.Add(42);        // Boxing: int → object
            arrayList.Add("hola");    // ⚠️ Mezcla de tipos permitido
            arrayList.Add(3.14);      // ⚠️ Mezcla de tipos permitido

            Console.WriteLine($"ArrayList contiene: {arrayList.Count} elementos");

            // Recuperar valor requiere cast y puede fallar en runtime
            try
            {
                int valor = (int)arrayList[0];  // Unboxing: object → int
                Console.WriteLine($"Valor recuperado: {valor}");

                // ❌ Esto lanza InvalidCastException en runtime
                int error = (int)arrayList[1];  // "hola" no puede convertirse a int
            }
            catch (InvalidCastException ex)
            {
                Console.WriteLine($"⚠️ ERROR: {ex.Message}");
            }

            Console.WriteLine();

            // ✅ DESPUÉS: List<int> (type-safe)
            List<int> listaEnteros = new List<int>();
            listaEnteros.Add(42);
            // listaEnteros.Add("hola");  // ❌ Error de COMPILACIÓN (no deja compilar)
            // listaEnteros.Add(3.14);    // ❌ Error de COMPILACIÓN

            Console.WriteLine($"List<int> contiene: {listaEnteros.Count} elementos");

            // Recuperar valor NO requiere cast (sin unboxing overhead)
            int valorEntero = listaEnteros[0];
            Console.WriteLine($"Valor recuperado: {valorEntero}");

            Console.WriteLine("\n");

            // 2. DEMOSTRACIÓN DE PERFORMANCE (BOXING/UNBOXING)
            Console.WriteLine("2. PERFORMANCE (1,000,000 iteraciones):");
            Console.WriteLine("----------------------------------------");

            int iteraciones = 1_000_000;
            Random random = new Random();

            // Test con ArrayList (con boxing/unboxing)
            var sw = Stopwatch.StartNew();
            ArrayList arrayListNumbers = new ArrayList();
            for (int i = 0; i < iteraciones; i++)
            {
                int num = random.Next(100);
                arrayListNumbers.Add(num);           // Boxing en cada Add
            }
            long sumaArrayList = 0;
            foreach (object num in arrayListNumbers)
            {
                sumaArrayList += (int)num;           // Unboxing en cada iteración
            }
            sw.Stop();
            long tiempoArrayList = sw.ElapsedMilliseconds;

            // Test con List<int> (sin boxing/unboxing)
            sw.Restart();
            List<int> listNumbers = new List<int>();
            for (int i = 0; i < iteraciones; i++)
            {
                int num = random.Next(100);
                listNumbers.Add(num);                // Directo, sin boxing
            }
            long sumaList = 0;
            foreach (int num in listNumbers)
            {
                sumaList += num;                     // Directo, sin unboxing
            }
            sw.Stop();
            long tiempoList = sw.ElapsedMilliseconds;

            // Resultados
            Console.WriteLine($"ArrayList (con boxing/unboxing):");
            Console.WriteLine($"  - Tiempo: {tiempoArrayList} ms");
            Console.WriteLine($"  - Suma: {sumaArrayList:N0}");

            Console.WriteLine($"\nList<int> (sin boxing/unboxing):");
            Console.WriteLine($"  - Tiempo: {tiempoList} ms");
            Console.WriteLine($"  - Suma: {sumaList:N0}");

            double mejora = ((double)(tiempoArrayList - tiempoList) / tiempoArrayList) * 100;
            Console.WriteLine($"\n📈 Mejora de performance: {mejora:F1}% más rápido con List<int>");

            Console.WriteLine("\n");
        }

        // 3. EJEMPLO PRÁCTICO: Lista genérica personalizada
        // Este ejemplo muestra cómo crear tu propia clase genérica

        /// <summary>
        /// Pila (Stack) genérica implementada con List<T>
        /// </summary>
        /// <typeparam name="T">Tipo de elementos en la pila</typeparam>
        public class Pila<T>
        {
            private readonly List<T> _elementos = new List<T>();

            /// <summary>
            /// Agrega un elemento en la cima de la pila
            /// </summary>
            public void Push(T elemento)
            {
                _elementos.Add(elemento);
            }

            /// <summary>
            /// Remueve y retorna el elemento de la cima
            /// </summary>
            /// <returns>Elemento removido</returns>
            /// <exception cref="InvalidOperationException">Si la pila está vacía</exception>
            public T Pop()
            {
                if (_elementos.Count == 0)
                    throw new InvalidOperationException("La pila está vacía");

                int indiceUltimo = _elementos.Count - 1;
                T elemento = _elementos[indiceUltimo];
                _elementos.RemoveAt(indiceUltimo);
                return elemento;
            }

            /// <summary>
            /// Retorna el elemento de la cima sin removerlo
            /// </summary>
            public T Peek()
            {
                if (_elementos.Count == 0)
                    throw new InvalidOperationException("La pila está vacía");

                return _elementos[_elementos.Count - 1];
            }

            /// <summary>
            /// Cantidad de elementos en la pila
            /// </summary>
            public int Count => _elementos.Count;

            /// <summary>
            /// Verifica si la pila está vacía
            /// </summary>
            public bool IsEmpty => _elementos.Count == 0;
        }

        // DEMO DE USO DE LA CLASE GENÉRICA
        static void DemoPilaGenerica()
        {
            Console.WriteLine("3. CLASE GENÉRICA PERSONALIZADA:");
            Console.WriteLine("-----------------------------------");

            // Pila de enteros
            var pilaEnteros = new Pila<int>();
            pilaEnteros.Push(10);
            pilaEnteros.Push(20);
            pilaEnteros.Push(30);

            Console.WriteLine("Pila de enteros:");
            while (!pilaEnteros.IsEmpty)
            {
                Console.WriteLine($"  Pop: {pilaEnteros.Pop()}");
            }

            // Pila de strings
            var pilaStrings = new Pila<string>();
            pilaStrings.Push("Primero");
            pilaStrings.Push("Segundo");
            pilaStrings.Push("Tercero");

            Console.WriteLine("\nPila de strings:");
            while (!pilaStrings.IsEmpty)
            {
                Console.WriteLine($"  Pop: {pilaStrings.Pop()}");
            }

            // Pila de objetos personalizados
            var pilaPersonas = new Pila<Persona>();
            pilaPersonas.Push(new Persona("Juan", 25));
            pilaPersonas.Push(new Persona("María", 30));

            Console.WriteLine("\nPila de personas:");
            while (!pilaPersonas.IsEmpty)
            {
                Persona p = pilaPersonas.Pop();
                Console.WriteLine($"  Pop: {p.Nombre} ({p.Edad} años)");
            }
        }

        // Clase de apoyo para demos
        class Persona
        {
            public string Nombre { get; }
            public int Edad { get; }

            public Persona(string nombre, int edad)
            {
                Nombre = nombre;
                Edad = edad;
            }
        }
    }
}
```

### Salida Esperada

```
=== GENERICS PERFORMANCE DEMO ===

1. TYPE SAFETY:
-------------------
ArrayList contiene: 3 elementos
Valor recuperado: 42
⚠️ ERROR: Unable to cast object of type 'System.String' to type 'System.Int32'.

List<int> contiene: 1 elementos
Valor recuperado: 42


2. PERFORMANCE (1,000,000 iteraciones):
----------------------------------------
ArrayList (con boxing/unboxing):
  - Tiempo: 125 ms
  - Suma: 49,512,847

List<int> (sin boxing/unboxing):
  - Tiempo: 45 ms
  - Suma: 49,512,847

📈 Mejora de performance: 64.0% más rápido con List<int>
```

---

## Value vs Reference Types - Demo Completa

```csharp
using System;
using System.Collections.Generic;

namespace ValueVsReferenceDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== VALUE VS REFERENCE TYPES ===\n");

            // 1. VALUE TYPE: Asignación copia el VALOR
            Console.WriteLine("1. VALUE TYPE (int):");
            Console.WriteLine("------------------------");

            int edad1 = 25;
            int edad2 = edad1;      // Copia el valor

            Console.WriteLine($"edad1 = {edad1}, edad2 = {edad2}");

            edad2 = 30;             // Modificar edad2 NO afecta edad1

            Console.WriteLine($"Después de edad2 = 30:");
            Console.WriteLine($"  edad1 = {edad1} (no cambió)");
            Console.WriteLine($"  edad2 = {edad2}");

            Console.WriteLine("\n");

            // 2. REFERENCE TYPE: Asignación copia la REFERENCIA
            Console.WriteLine("2. REFERENCE TYPE (List<string>):");
            Console.WriteLine("-----------------------------------");

            List<string> lista1 = new List<string> { "A", "B" };
            List<string> lista2 = lista1;  // Copia la referencia (ambos apuntan al mismo objeto)

            Console.WriteLine($"lista1 = [{string.Join(", ", lista1)}]");
            Console.WriteLine($"lista2 = [{string.Join(", ", lista2)}]");
            Console.WriteLine($"¿lista1 y lista2 son el mismo objeto? {ReferenceEquals(lista1, lista2)}");

            lista2.Add("C");          // Modificar lista2 AFECTA lista1

            Console.WriteLine($"\nDespués de lista2.Add(\"C\"):");
            Console.WriteLine($"  lista1 = [{string.Join(", ", lista1)}] (!!)");
            Console.WriteLine($"  lista2 = [{string.Join(", ", lista2)}]");

            Console.WriteLine("\n");

            // 3. PASAJE DE PARÁMETROS
            Console.WriteLine("3. PASAJE DE PARÁMETROS:");
            Console.WriteLine("-------------------------");

            int numero = 5;
            Console.WriteLine($"Antes de ModificarValue: numero = {numero}");
            ModificarValue(numero);
            Console.WriteLine($"Después de ModificarValue: numero = {numero} (no cambió)");

            Console.WriteLine();

            List<int> numeros = new List<int> { 1, 2, 3 };
            Console.WriteLine($"Antes de ModificarReference: [{string.Join(", ", numeros)}]");
            ModificarReference(numeros);
            Console.WriteLine($"Después de ModificarReference: [{string.Join(", ", numeros)}] (cambió)");

            Console.WriteLine("\n");

            // 4. STRUCT (VALUE TYPE) vs CLASS (REFERENCE TYPE)
            Console.WriteLine("4. STRUCT vs CLASS:");
            Console.WriteLine("---------------------");

            PointStruct ps1 = new PointStruct { X = 10, Y = 20 };
            PointStruct ps2 = ps1;    // Copia el valor completo
            ps2.X = 100;

            Console.WriteLine($"PointStruct:");
            Console.WriteLine($"  ps1.X = {ps1.X} (no cambió)");
            Console.WriteLine($"  ps2.X = {ps2.X}");

            Console.WriteLine();

            PointClass pc1 = new PointClass { X = 10, Y = 20 };
            PointClass pc2 = pc1;     // Copia la referencia
            pc2.X = 100;

            Console.WriteLine($"PointClass:");
            Console.WriteLine($"  pc1.X = {pc1.X} (cambió!!)");
            Console.WriteLine($"  pc2.X = {pc2.X}");

            Console.WriteLine("\n");

            // 5. STRING: Reference Type con comportamiento especial
            Console.WriteLine("5. STRING INMUTABILIDAD:");
            Console.WriteLine("-------------------------");

            string s1 = "hola";
            string s2 = s1;           // Copia referencia al mismo string

            Console.WriteLine($"s1 = \"{s1}\", s2 = \"{s2}\"");

            s2 = "mundo";             // s2 ahora apunta a un NUEVO string

            Console.WriteLine($"Después de s2 = \"mundo\":");
            Console.WriteLine($"  s1 = \"{s1}\" (no cambió)");
            Console.WriteLine($"  s2 = \"{s2}\"");

            Console.WriteLine($"\n¿s1 y s2 son el mismo objeto? {ReferenceEquals(s1, s2)}");

            // String interning (strings iguales comparten memoria)
            string s3 = "hola";
            string s4 = "hola";
            Console.WriteLine($"¿s3 y s4 son el mismo objeto? {ReferenceEquals(s3, s4)} (interning)");
        }

        // Modifica una COPIA local del valor
        static void ModificarValue(int x)
        {
            x = 100;  // Solo modifica la copia local
        }

        // Modifica el objeto original (porque pasan la referencia)
        static void ModificarReference(List<int> lista)
        {
            lista.Add(100);  // Modifica el objeto compartido
        }
    }

    // Struct: VALUE TYPE
    public struct PointStruct
    {
        public int X { get; set; }
        public int Y { get; set; }
    }

    // Class: REFERENCE TYPE
    public class PointClass
    {
        public int X { get; set; }
        public int Y { get; set; }
    }
}
```

### Salida Esperada

```
=== VALUE VS REFERENCE TYPES ===

1. VALUE TYPE (int):
------------------------
edad1 = 25, edad2 = 25
Después de edad2 = 30:
  edad1 = 25 (no cambió)
  edad2 = 30

2. REFERENCE TYPE (List<string>):
-----------------------------------
lista1 = [A, B]
lista2 = [A, B]
¿lista1 y lista2 son el mismo objeto? True

Después de lista2.Add("C"):
  lista1 = [A, B, C] (!!)
  lista2 = [A, B, C]

3. PASAJE DE PARÁMETROS:
-------------------------
Antes de ModificarValue: numero = 5
Después de ModificarValue: numero = 5 (no cambió)

Antes de ModificarReference: [1, 2, 3]
Después de ModificarReference: [1, 2, 3, 100] (cambió)

4. STRUCT vs CLASS:
---------------------
PointStruct:
  ps1.X = 10 (no cambió)
  ps2.X = 100

PointClass:
  pc1.X = 100 (cambió!!)
  pc2.X = 100

5. STRING INMUTABILIDAD:
-------------------------
s1 = "hola", s2 = "hola"
Después de s2 = "mundo":
  s1 = "hola" (no cambió)
  s2 = "mundo"

¿s1 y s2 son el mismo objeto? False
¿s3 y s4 son el mismo objeto? True (interning)
```

---

## Nullable en Escenario Real (BD)

```csharp
using System;
using System.Data;
using System.Data.SqlClient;

namespace NullableBdDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== NULLABLE EN ESCENARIO BASE DE DATOS ===\n");

            // Simular datos desde una base de datos donde Telefono puede ser NULL
            DataTable dt = SimularLecturaBd();

            Console.WriteLine("Datos recibidos de BD:");
            Console.WriteLine("ID | Nombre       | Telefono");
            Console.WriteLine("---+--------------+-------------------");

            foreach (DataRow row in dt.Rows)
            {
                int id = (int)row["Id"];
                string nombre = (string)row["Nombre"];

                // ⚠️ Telefono puede ser NULL en BD
                string? telefono = row["Telefono"] as string ?? null;

                Console.WriteLine($"{id,2} | {nombre,-12} | {(telefono ?? "NULL"),-17}");
            }

            Console.WriteLine("\n");

            // Procesar con DTOs
            Console.WriteLine("Procesando con DTOs:");
            Console.WriteLine("---------------------");

            foreach (DataRow row in dt.Rows)
            {
                EstudianteDto estudiante = MapearAEstudianteDto(row);

                Console.WriteLine($"Estudiante: {estudiante.Nombre}");
                Console.WriteLine($"  Teléfono: {estudiante.Telefono ?? "No registrado"}");

                if (estudiante.Telefono != null)
                {
                    Console.WriteLine($"  ✅ Tiene teléfono: {estudiante.Telefono}");
                }
                else
                {
                    Console.WriteLine($"  ⚠️ Sin teléfono registrado");
                }

                Console.WriteLine();
            }
        }

        // Mapea un DataRow a un EstudianteDto, manejando NULLs correctamente
        static EstudianteDto MapearAEstudianteDto(DataRow row)
        {
            return new EstudianteDto
            {
                Id = (int)row["Id"],
                Nombre = (string)row["Nombre"],
                // Manejo de NULL: usar as string + null-coalescing
                Telefono = row["Telefono"] as string ?? null,
                // Otro patrón: IsNull + GetValueOrDefault
                Edad = row.IsNull("Edad") ? null : (int?)(int)row["Edad"]
            };
        }

        // Simula la lectura de BD
        static DataTable SimularLecturaBd()
        {
            DataTable dt = new DataTable();
            dt.Columns.Add("Id", typeof(int));
            dt.Columns.Add("Nombre", typeof(string));
            dt.Columns.Add("Telefono", typeof(string));
            dt.Columns.Add("Edad", typeof(int));

            dt.Rows.Add(1, "Juan Pérez", "300-123-4567", 25);
            dt.Rows.Add(2, "María López", DBNull.Value, 30);  // Telefono NULL
            dt.Rows.Add(3, "Pedro García", "310-987-6543", DBNull.Value);  // Edad NULL
            dt.Rows.Add(4, "Ana Martínez", DBNull.Value, 22);  // Ambos NULL

            return dt;
        }
    }

    // DTO (Data Transfer Object)
    public class EstudianteDto
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public string? Telefono { get; set; }  // Nullable porque BD permite NULL
        public int? Edad { get; set; }         // Nullable porque BD permite NULL
    }

    // Ejemplo de uso con ADO.NET real
    public class EstudianteRepository
    {
        private readonly string _connectionString;

        public EstudianteRepository(string connectionString)
        {
            _connectionString = connectionString;
        }

        public EstudianteDto? ObtenerPorId(int estudianteId)
        {
            using (var conn = new SqlConnection(_connectionString))
            using (var cmd = new SqlCommand("SELECT * FROM Estudiantes WHERE Id = @Id", conn))
            {
                cmd.Parameters.AddWithValue("@Id", estudianteId);
                conn.Open();

                using (var reader = cmd.ExecuteReader())
                {
                    if (reader.Read())
                    {
                        return new EstudianteDto
                        {
                            Id = reader.GetInt32(reader.GetOrdinal("Id")),
                            Nombre = reader.GetString(reader.GetOrdinal("Nombre")),
                            // Manejo de NULL con IsDBNull
                            Telefono = reader.IsDBNull(reader.GetOrdinal("Telefono"))
                                ? null
                                : reader.GetString(reader.GetOrdinal("Telefono")),
                            Edad = reader.IsDBNull(reader.GetOrdinal("Edad"))
                                ? (int?)null
                                : reader.GetInt32(reader.GetOrdinal("Edad"))
                        };
                    }
                }
            }

            return null;  // No encontrado
        }

        // Ejemplo de INSERT con parámetros nullable
        public void Insertar(EstudianteDto estudiante)
        {
            using (var conn = new SqlConnection(_connectionString))
            using (var cmd = new SqlCommand(@"
                INSERT INTO Estudiantes (Nombre, Telefono, Edad)
                VALUES (@Nombre, @Telefono, @Edad)", conn))
            {
                cmd.Parameters.AddWithValue("@Nombre", estudiante.Nombre);

                // Manejo de NULL en parámetros
                if (estudiante.Telefono != null)
                    cmd.Parameters.AddWithValue("@Telefono", estudiante.Telefono);
                else
                    cmd.Parameters.AddWithValue("@Telefono", DBNull.Value);

                if (estudiante.Edad.HasValue)
                    cmd.Parameters.AddWithValue("@Edad", estudiante.Edad.Value);
                else
                    cmd.Parameters.AddWithValue("@Edad", DBNull.Value);

                conn.Open();
                cmd.ExecuteNonQuery();
            }
        }
    }
}
```

---

## StringBuilder vs String Concatenation

```csharp
using System;
using System.Diagnostics;
using System.Text;

namespace StringBuilderDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== STRINGBUILDER VS STRING CONCATENATION ===\n");

            // 1. DEMO VISUAL: QUÉ PASA CON STRING INMUTABLE
            Console.WriteLine("1. STRING INMUTABILIDAD:");
            Console.WriteLine("-------------------------");

            string texto = "Hola";
            Console.WriteLine($"Valor original: \"{texto}\"");
            Console.WriteLine($"Dirección memoria: {GetObjectId(texto)}");

            texto = texto + " Mundo";
            Console.WriteLine($"Después de concatenación: \"{texto}\"");
            Console.WriteLine($"Dirección memoria: {GetObjectId(texto)} (NUEVO OBJETO!)");

            Console.WriteLine("\n");

            // 2. PERFORMANCE BENCHMARK
            Console.WriteLine("2. BENCHMARK (10,000 concatenaciones):");
            Console.WriteLine("----------------------------------------");

            int iteraciones = 10_000;

            // Método 1: Concatenación con +
            var sw = Stopwatch.StartNew();
            string resultado1 = "";
            for (int i = 0; i < iteraciones; i++)
            {
                resultado1 += i + ",";  // Crea nuevo string en cada iteración
            }
            sw.Stop();
            long tiempoConcatenacion = sw.ElapsedMilliseconds;

            // Método 2: StringBuilder
            sw.Restart();
            var sb = new StringBuilder();
            for (int i = 0; i < iteraciones; i++)
            {
                sb.Append(i);
                sb.Append(',');
            }
            string resultado2 = sb.ToString();
            sw.Stop();
            long tiempoStringBuilder = sw.ElapsedMilliseconds;

            // Resultados
            Console.WriteLine($"Concatenación con +: {tiempoConcatenacion} ms");
            Console.WriteLine($"StringBuilder: {tiempoStringBuilder} ms");

            long mejora = tiempoConcatenacion - tiempoStringBuilder;
            double porcentajeMejora = ((double)mejora / tiempoConcatenacion) * 100;

            Console.WriteLine($"\n📈 StringBuilder es {mejora} ms más rápido ({porcentajeMejora:F1}% menos tiempo)");

            Console.WriteLine("\n");

            // 3. CUÁNDO USAR CADA UNO
            Console.WriteLine("3. REGLAS PRÁCTICAS:");
            Console.WriteLine("---------------------");

            // ✅ Usar + o $ para pocas concatenaciones (1-3)
            string nombre = "Juan";
            string saludo = "Hola, " + nombre + "!";  // OK para pocas concatenaciones

            // ✅ Usar $ para formateo (más legible)
            string mensaje = $"Hola, {nombre}. Tienes {25} años.";

            // ✅ Usar StringBuilder para muchas concatenaciones o en loops
            var sb2 = new StringBuilder();
            for (int i = 0; i < 100; i++)
            {
                sb2.AppendLine($"Línea {i}");
            }

            Console.WriteLine($"Concatenación simple (1-3 strings): Usar + o $");
            Console.WriteLine($"Loop con concatenaciones: Usar StringBuilder");
            Console.WriteLine($"Formateo complejo: Usar $ interpolation");

            Console.WriteLine("\n");

            // 4. STRINGBUILDER MÉTODOS ÚTILES
            Console.WriteLine("4. MÉTODOS ÚTILES DE STRINGBUILDER:");
            Console.WriteLine("--------------------------------------");

            var sb3 = new StringBuilder();
            sb3.Append("Hola");           // Append: agrega al final
            sb3.Append(" ");
            sb3.Append("Mundo");
            Console.WriteLine($"Append: \"{sb3}\"");

            sb3.AppendLine("!");          // AppendLine: agrega + nueva línea
            sb3.AppendLine("¿Cómo estás?");
            Console.WriteLine($"AppendLine:\n\"{sb3}\"");

            sb3.Replace("Mundo", "C#");   // Replace: reemplaza texto
            Console.WriteLine($"Replace: \"{sb3}\"");

            sb3.Insert(5, " querido ");   // Insert: inserta en posición
            Console.WriteLine($"Insert: \"{sb3}\"");

            sb3.Remove(5, 8);            // Remove: remueve rango
            Console.WriteLine($"Remove: \"{sb3}\"");

            Console.WriteLine($"\nCapacidad: {sb3.Capacity}, Longitud: {sb3.Length}");

            // Optimizar capacidad si se conoce el tamaño final
            var sb4 = new StringBuilder(1000);  // Capacidad inicial = 1000
            Console.WriteLine($"StringBuilder con capacidad inicial: {sb4.Capacity}");
        }

        // Helper para obtener "identidad" del objeto (simulado)
        static string GetObjectId(object obj)
        {
            return $"0x{obj.GetHashCode():X8}";
        }
    }
}
```

### Salida Esperada

```
=== STRINGBUILDER VS STRING CONCATENATION ===

1. STRING INMUTABILIDAD:
-------------------------
Valor original: "Hola"
Dirección memoria: 0x5F3A1B2C
Después de concatenación: "Hola Mundo"
Dirección memoria: 0x3E4C9D1A (NUEVO OBJETO!)

2. BENCHMARK (10,000 concatenaciones):
----------------------------------------
Concatenación con +: 45 ms
StringBuilder: 2 ms

📈 StringBuilder es 43 ms más rápido (95.6% menos tiempo)

3. REGLAS PRÁCTICAS:
---------------------
Concatenación simple (1-3 strings): Usar + o $
Loop con concatenaciones: Usar StringBuilder
Formateo complejo: Usar $ interpolation
```

---

## Primary Constructors (C# 12)

```csharp
using System;

namespace PrimaryConstructorsDemo
{
    // ❌ ANTES (C# 11 y anteriores): Verboso
    public class PersonaAntes
    {
        private readonly string _nombre;
        private readonly int _edad;

        public PersonaAntes(string nombre, int edad)
        {
            _nombre = nombre;
            _edad = edad;
        }

        public string Nombre => _nombre;
        public int Edad => _edad;

        public void Saludar()
        {
            Console.WriteLine($"Hola, soy {_nombre}");
        }

        public string ObtenerInfo()
        {
            return $"{_nombre} ({_edad} años)";
        }
    }

    // ✅ DESPUÉS (C# 12): Conciso
    public class PersonaDespues(string nombre, int edad)
    {
        // Los parámetros del constructor primario están disponibles en toda la clase
        public void Saludar() => Console.WriteLine($"Hola, soy {nombre}");

        public string Info => $"{nombre} ({edad} años)";

        // Propiedad que expone el parámetro
        public string Nombre => nombre;
        public int Edad => edad;
    }

    // ✅ EJEMPLO PRÁCTICO: DTO con primary constructor
    public class EstudianteDto(string nombre, int edad, double promedio)
    {
        // Validación en el cuerpo del constructor
        public EstudianteDto(string nombre, int edad, double promedio)
            : this(nombre, edad, promedio)
        {
            if (string.IsNullOrWhiteSpace(nombre))
                throw new ArgumentException("El nombre no puede estar vacío", nameof(nombre));

            if (edad < 0 || edad > 120)
                throw new ArgumentOutOfRangeException(nameof(edad), "Edad inválida");

            if (promedio < 0.0 || promedio > 5.0)
                throw new ArgumentOutOfRangeException(nameof(promedio), "Promedio debe estar entre 0 y 5");
        }

        // Propiedades que exponen los parámetros
        public string Nombre { get; } = nombre;
        public int Edad { get; } = edad;
        public double Promedio { get; } = promedio;

        // Propiedad computada
        public string Estado => Promedio >= 3.0 ? "APROBADO" : "REPROBADO";

        // Método
        public void MostrarInfo()
        {
            Console.WriteLine($"Estudiante: {nombre}");
            Console.WriteLine($"  Edad: {edad} años");
            Console.WriteLine($"  Promedio: {promedio:F2}");
            Console.WriteLine($"  Estado: {Estado}");
        }
    }

    // ✅ RECORD con primary constructor (inmutable)
    public record PersonaRecord(string Nombre, int Edad);

    // Demo de uso
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== PRIMARY CONSTRUCTORS (C# 12) ===\n");

            // Usar la clase con primary constructor
            var estudiante = new EstudianteDto("María López", 20, 4.2);
            estudiante.MostrarInfo();

            Console.WriteLine();

            // Record con primary constructor
            var persona1 = new PersonaRecord("Juan", 25);
            var persona2 = new PersonaRecord("Juan", 25);
            var persona3 = new PersonaRecord("Ana", 30);

            Console.WriteLine($"persona1 == persona2: {persona1 == persona2}");  // True (records comparan por valor)
            Console.WriteLine($"persona1 == persona3: {persona1 == persona3}");  // False
        }
    }
}
```

---

## Collection Expressions (C# 12)

```csharp
using System;
using System.Collections.Generic;

namespace CollectionExpressionsDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== COLLECTION EXPRESSIONS (C# 12) ===\n");

            // 1. ARRAYS
            Console.WriteLine("1. ARRAYS:");
            Console.WriteLine("-------------");

            // ❌ ANTES
            int[] nums1 = new int[] { 1, 2, 3 };

            // ✅ DESPUÉS
            int[] nums2 = [1, 2, 3];

            Console.WriteLine($"Array: [{string.Join(", ", nums2)}]");

            Console.WriteLine();

            // 2. LISTS
            Console.WriteLine("2. LISTS:");
            Console.WriteLine("-----------");

            // ❌ ANTES
            var lista1 = new List<int> { 1, 2, 3 };

            // ✅ DESPUÉS
            List<int> lista2 = [1, 2, 3];
            List<string> nombres = ["Ana", "Juan", "María"];

            Console.WriteLine($"List<int>: [{string.Join(", ", lista2)}]");
            Console.WriteLine($"List<string>: [{string.Join(", ", nombres)}]");

            Console.WriteLine();

            // 3. SPREAD OPERATOR (..)
            Console.WriteLine("3. SPREAD OPERATOR:");
            Console.WriteLine("--------------------");

            int[] pares = [2, 4, 6];
            int[] impares = [1, 3, 5];

            // Combinar arrays con spread operator
            int[] todos = [..pares, ..impares];

            Console.WriteLine($"Pares: [{string.Join(", ", pares)}]");
            Console.WriteLine($"Impares: [{string.Join(", ", impares)}]");
            Console.WriteLine($"Todos: [{string.Join(", ", todos)}]");

            Console.WriteLine();

            // 4. SPREAD CON ELEMENTOS ADICIONALES
            Console.WriteLine("4. SPREAD CON ELEMENTOS:");
            Console.WriteLine("-------------------------");

            int[] partes1 = [1, 2];
            int[] partes2 = [4, 5];
            int[] combinado = [..partes1, 3, ..partes2];  // [1, 2, 3, 4, 5]

            Console.WriteLine($"Combinado: [{string.Join(", ", combinado)}]");

            Console.WriteLine();

            // 5. SPREAD CON RANGES
            Console.WriteLine("5. SPREAD CON RANGES:");
            Console.WriteLine("----------------------");

            int[] original = [1, 2, 3, 4, 5];
            int[] primerosTres = [..original[..3]];  // Primeros 3 elementos
            int[] ultimosDos = [..original[3..]];   // Desde índice 3 hasta el final
            int[] rangoMedio = [..original[1..4]];  // Del índice 1 al 4

            Console.WriteLine($"Original: [{string.Join(", ", original)}]");
            Console.WriteLine($"Primeros 3: [{string.Join(", ", primerosTres)}]");
            Console.WriteLine($"Últimos 2: [{string.Join(", ", ultimosDos)}]");
            Console.WriteLine($"Rango medio: [{string.Join(", ", rangoMedio)}]");

            Console.WriteLine();

            // 6. DICTIONARIES
            Console.WriteLine("6. DICTIONARIES:");
            Console.WriteLine("-----------------");

            // ❌ ANTES
            var dict1 = new Dictionary<string, int>
            {
                { "Ana", 25 },
                { "Juan", 30 }
            };

            // ✅ DESPUÉS (C# 12 no permite [] para diccionarios directamente aún,
            // pero puedes usar inicializador mejorado)
            var dict2 = new Dictionary<string, int>
            {
                ["Ana"] = 25,
                ["Juan"] = 30
            };

            Console.WriteLine("Dictionary:");
            foreach (var kvp in dict2)
            {
                Console.WriteLine($"  {kvp.Key}: {kvp.Value}");
            }

            Console.WriteLine();

            // 7. EJEMPLO PRÁCTICO: Filtrar y combinar
            Console.WriteLine("7. EJEMPLO PRÁCTICO:");
            Console.WriteLine("---------------------");

            List<int> numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

            // Filtrar pares
            List<int> paresFiltrados = [..numeros.FindAll(x => x % 2 == 0)];

            // Filtrar impares
            List<int> imparesFiltrados = [..numeros.FindAll(x => x % 2 != 0)];

            // Multiplos de 3
            List<int> multiplos3 = [..numeros.FindAll(x => x % 3 == 0)];

            Console.WriteLine($"Números originales: [{string.Join(", ", numeros)}]");
            Console.WriteLine($"Pares: [{string.Join(", ", paresFiltrados)}]");
            Console.WriteLine($"Impares: [{string.Join(", ", imparesFiltrados)}]");
            Console.WriteLine($"Múltiplos de 3: [{string.Join(", ", multiplos3)}]");

            // Combinar todos sin duplicados
            List<int> combinados = [..paresFiltrados, ..imparesFiltrados];
            Console.WriteLine($"Combinados: [{string.Join(", ", combinados)}]");
        }
    }
}
```

---

## Pattern Matching

```csharp
using System;

namespace PatternMatchingDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== PATTERN MATCHING ===\n");

            // 1. SWITCH EXPRESSION (C# 8+)
            Console.WriteLine("1. SWITCH EXPRESSION:");
            Console.WriteLine("----------------------");

            int edad = 25;

            // ❌ ANTES: switch tradicional
            string categoria1;
            switch (edad)
            {
                case int n when n < 13:
                    categoria1 = "Niño";
                    break;
                case int n when n >= 13 && n < 20:
                    categoria1 = "Adolescente";
                    break;
                case int n when n >= 20 && n < 65:
                    categoria1 = "Adulto";
                    break;
                default:
                    categoria1 = "Mayor";
                    break;
            }

            // ✅ DESPUÉS: switch expression
            string categoria2 = edad switch
            {
                < 13 => "Niño",
                >= 13 and < 20 => "Adolescente",
                >= 20 and < 65 => "Adulto",
                _ => "Mayor"
            };

            Console.WriteLine($"Edad: {edad}");
            Console.WriteLine($"Categoría: {categoria2}");

            Console.WriteLine();

            // 2. PATTERN MATCHING POR TIPO
            Console.WriteLine("2. PATTERN MATCHING POR TIPO:");
            Console.WriteLine("--------------------------------");

            object[] objetos = { 42, "hola", 3.14, null, true };

            foreach (var obj in objetos)
            {
                string descripcion = obj switch
                {
                    int i when i > 0 => $"Entero positivo: {i}",
                    int i when i < 0 => $"Entero negativo: {i}",
                    int i => $"Cero",
                    string s when string.IsNullOrWhiteSpace(s) => "String vacío",
                    string s => $"String ({s.Length} caracteres): {s}",
                    double d => $"Double: {d:F2}",
                    null => "Valor nulo",
                    _ => $"Tipo: {obj.GetType().Name}"
                };

                Console.WriteLine($"  {obj} → {descripcion}");
            }

            Console.WriteLine();

            // 3. RELATIONAL PATTERNs
            Console.WriteLine("3. RELATIONAL PATTERNS:");
            Console.WriteLine("------------------------");

            double promedio = 4.2;

            string calificacion = promedio switch
            {
                >= 4.5 => "Excelente ⭐⭐⭐⭐⭐",
                >= 4.0 => "Muy Bueno ⭐⭐⭐⭐",
                >= 3.5 => "Bueno ⭐⭐⭐",
                >= 3.0 => "Aceptable ⭐⭐",
                _ => "Reprobado ⭐"
            };

            Console.WriteLine($"Promedio: {promedio:F1}");
            Console.WriteLine($"Calificación: {calificacion}");

            Console.WriteLine();

            // 4. LOGICAL PATTERNS (and, or, not)
            Console.WriteLine("4. LOGICAL PATTERNS:");
            Console.WriteLine("---------------------");

            int numero = 15;

            string tipo = numero switch
            {
                > 0 and < 10 => "Dígito positivo",
                >= 10 and < 100 => "Número de dos dígitos",
                not 0 => "Otro número positivo",
                _ => "Cero"
            };

            Console.WriteLine($"Número: {numero}");
            Console.WriteLine($"Tipo: {tipo}");

            Console.WriteLine();

            // 5. LIST PATTERNS (C# 11+)
            Console.WriteLine("5. LIST PATTERNS:");
            Console.WriteLine("------------------");

            int[] coords1 = [1, 2, 3];
            int[] coords2 = [1, 5, 3];
            int[] coords3 = [0, 0, 5];

            string AnalizarCoordenadas(int[] coords) => coords switch
            {
                [1, 2, 3] => "Coordenadas exactas (1, 2, 3)",
                [1, _, 3] => "Empieza con 1, termina con 3",
                [0, 0, _] => "En el eje Z",
                [_, _, 5] => "Termina en 5",
                _ => "Otro patrón"
            };

            Console.WriteLine($"[1, 2, 3] → {AnalizarCoordenadas(coords1)}");
            Console.WriteLine($"[1, 5, 3] → {AnalizarCoordenadas(coords2)}");
            Console.WriteLine($"[0, 0, 5] → {AnalizarCoordenadas(coords3)}");

            Console.WriteLine();

            // 6. PROPERTY PATTERNs
            Console.WriteLine("6. PROPERTY PATTERNS:");
            Console.WriteLine("----------------------");

            var persona = new Persona { Nombre = "Juan", Edad = 25, Activo = true };

            string estado = persona switch
            {
                { Activo: true, Edad: >= 18 } => "Adulto activo",
                { Activo: false } => "Inactivo",
                { Edad: < 18 } => "Menor de edad",
                _ => "Estado desconocido"
            };

            Console.WriteLine($"Persona: {persona.Nombre}");
            Console.WriteLine($"Estado: {estado}");

            Console.WriteLine();

            // 7. EJEMPLO PRÁCTICO: VALIDACIÓN DE FORMULARIO
            Console.WriteLine("7. EJEMPLO PRÁCTICO:");
            Console.WriteLine("---------------------");

            var formulario = new FormularioData
            {
                Email = "usuario@example.com",
                Edad = 25,
                Pais = "Colombia"
            };

            string resultado = ValidarFormulario(formulario);
            Console.WriteLine($"Resultado de validación: {resultado}");
        }

        static string ValidarFormulario(FormularioData data)
        {
            return (data.Email, data.Edad, data.Pais) switch
            {
                // Validaciones
                { Email: null } => "El email es requerido",
                { Email: "" } => "El email no puede estar vacío",
                { Email: var e } when !e.Contains('@') => "Email inválido (sin @)",
                { Edad: < 18 } => "Debe ser mayor de edad",
                { Pais: "Colombia" } when data.Edad < 21 => "En Colombia, edad mínima: 21",
                _ => "✅ Formulario válido"
            };
        }
    }

    // Clases de apoyo
    class Persona
    {
        public string Nombre { get; set; }
        public int Edad { get; set; }
        public bool Activo { get; set; }
    }

    class FormularioData
    {
        public string Email { get; set; }
        public int Edad { get; set; }
        public string Pais { get; set; }
    }
}
```

---

## Ejemplo: Sistema de Calificaciones Completo

Este es el código completo del ejercicio de clase, con validación robusta y solución detallada.

```csharp
using System;
using System.Collections.Generic;

namespace SistemaCalificaciones
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;

            Console.WriteLine("================================");
            Console.WriteLine("  SISTEMA DE CALIFICACIONES");
            Console.WriteLine("================================\n");

            // 1. Solicitar nombre del estudiante
            string nombre = SolicitarNombre();

            // 2. Solicitar las 3 notas con validación
            double nota1 = PedirNota("Primera");
            double nota2 = PedirNota("Segunda");
            double nota3 = PedirNota("Tercera");

            // 3. Calcular promedio
            double promedio = (nota1 + nota2 + nota3) / 3.0;

            // 4. Determinar estado
            string estado = promedio >= 3.0 ? "✅ APROBADO" : "❌ REPROBADO";

            // 5. Determinar calificación cualitativa
            string calificacion = CalificacionCualitativa(promedio);

            // 6. Mostrar resultados
            Console.WriteLine("\n================================");
            Console.WriteLine("  RESULTADO");
            Console.WriteLine("================================");
            Console.WriteLine($"Estudiante: {nombre}");
            Console.WriteLine($"Nota 1: {nota1:F2}");
            Console.WriteLine($"Nota 2: {nota2:F2}");
            Console.WriteLine($"Nota 3: {nota3:F2}");
            Console.WriteLine($"────────────────────────────────");
            Console.WriteLine($"Promedio: {promedio:F2}");
            Console.WriteLine($"Calificación: {calificacion}");
            Console.WriteLine($"Estado: {estado}");
            Console.WriteLine("================================");

            // 7. Mensaje motivacional
            MostrarMensajeMotivacional(promedio);
        }

        /// <summary>
        /// Solicita el nombre del estudiante con validación
        /// </summary>
        static string SolicitarNombre()
        {
            while (true)
            {
                Console.Write("Nombre del estudiante: ");
                string nombre = Console.ReadLine()?.Trim() ?? "";

                if (!string.IsNullOrWhiteSpace(nombre))
                {
                    return nombre;
                }

                Console.WriteLine("⚠️ El nombre no puede estar vacío. Intente nuevamente.\n");
            }
        }

        /// <summary>
        /// Solicita una nota con validación de rango (0.0 - 5.0)
        /// </summary>
        /// <param name="etiqueta">Etiqueta de la nota (ej: "Primera", "Segunda")</param>
        /// <returns>Nota validada</returns>
        static double PedirNota(string etiqueta)
        {
            while (true)
            {
                Console.Write($"{etiqueta} nota (0.0 - 5.0): ");
                string entrada = Console.ReadLine()?.Trim() ?? "";

                // Intentar parsear
                if (double.TryParse(entrada, out double nota))
                {
                    // Validar rango
                    if (nota >= 0.0 && nota <= 5.0)
                    {
                        return nota;
                    }

                    Console.WriteLine("⚠️ La nota debe estar entre 0.0 y 5.0. Intente nuevamente.\n");
                }
                else
                {
                    Console.WriteLine("⚠️ Entrada inválida. Ingrese un número válido.\n");
                }
            }
        }

        /// <summary>
        /// Determina la calificación cualitativa según el promedio
        /// </summary>
        /// <param name="promedio">Promedio numérico</param>
        /// <returns>Calificación cualitativa</returns>
        static string CalificacionCualitativa(double promedio)
        {
            return promedio switch
            {
                >= 4.5 => "Excelente ⭐⭐⭐⭐⭐",
                >= 4.0 => "Muy Bueno ⭐⭐⭐⭐",
                >= 3.5 => "Bueno ⭐⭐⭐",
                >= 3.0 => "Aceptable ⭐⭐",
                _ => "Insuficiente ⭐"
            };
        }

        /// <summary>
        /// Muestra un mensaje motivacional según el promedio
        /// </summary>
        static void MostrarMensajeMotivacional(double promedio)
        {
            Console.WriteLine("\n💬 Mensaje:");

            if (promedio >= 4.5)
            {
                Console.WriteLine("    ¡Excelente trabajo! Sigue así.");
            }
            else if (promedio >= 3.5)
            {
                Console.WriteLine("    ¡Buen trabajo! Puedes mejorar.");
            }
            else if (promedio >= 3.0)
            {
                Console.WriteLine("    Aprobaste, pero hay margen de mejora.");
            }
            else
            {
                Console.WriteLine("    No te rindas. ¡Sigue estudiando!");
            }

            Console.WriteLine();
        }
    }
}
```

### Variante: Con Clases (POO)

```csharp
using System;

namespace SistemaCalificacionesPOO
{
    // Clase que representa una calificación
    public class Calificacion
    {
        public string Etiqueta { get; }
        public double Valor { get; }

        public Calificacion(string etiqueta, double valor)
        {
            if (valor < 0.0 || valor > 5.0)
                throw new ArgumentOutOfRangeException(nameof(valor), "La nota debe estar entre 0.0 y 5.0");

            Etiqueta = etiqueta;
            Valor = valor;
        }

        public override string ToString() => $"{Etiqueta}: {Valor:F2}";
    }

    // Clase que representa un estudiante
    public class Estudiante
    {
        public string Nombre { get; }
        public List<Calificacion> Calificaciones { get }

        public Estudiante(string nombre)
        {
            if (string.IsNullOrWhiteSpace(nombre))
                throw new ArgumentException("El nombre no puede estar vacío", nameof(nombre));

            Nombre = nombre;
            Calificaciones = new List<Calificacion>();
        }

        public void AgregarCalificacion(Calificacion calificacion)
        {
            Calificaciones.Add(calificacion);
        }

        public double CalcularPromedio()
        {
            if (Calificaciones.Count == 0)
                return 0.0;

            double suma = 0.0;
            foreach (var calificacion in Calificaciones)
            {
                suma += calificacion.Valor;
            }

            return suma / Calificaciones.Count;
        }

        public string Estado => CalcularPromedio() >= 3.0 ? "✅ APROBADO" : "❌ REPROBADO";

        public string CalificacionCualitativa => CalcularPromedio() switch
        {
            >= 4.5 => "Excelente ⭐⭐⭐⭐⭐",
            >= 4.0 => "Muy Bueno ⭐⭐⭐⭐",
            >= 3.5 => "Bueno ⭐⭐⭐",
            >= 3.0 => "Aceptable ⭐⭐",
            _ => "Insuficiente ⭐"
        };

        public void MostrarReporte()
        {
            Console.WriteLine("================================");
            Console.WriteLine("  REPORTE DE CALIFICACIONES");
            Console.WriteLine("================================");
            Console.WriteLine($"Estudiante: {Nombre}");
            Console.WriteLine();

            foreach (var calificacion in Calificaciones)
            {
                Console.WriteLine($"  {calificacion}");
            }

            Console.WriteLine("────────────────────────────────");
            Console.WriteLine($"Promedio: {CalcularPromedio():F2}");
            Console.WriteLine($"Calificación: {CalificacionCualitativa}");
            Console.WriteLine($"Estado: {Estado}");
            Console.WriteLine("================================");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var estudiante = new Estudiante(SolicitarNombre());

            estudiante.AgregarCalificacion(new Calificacion("Nota 1", PedirNota("Primera")));
            estudiante.AgregarCalificacion(new Calificacion("Nota 2", PedirNota("Segunda")));
            estudiante.AgregarCalificacion(new Calificacion("Nota 3", PedirNota("Tercera")));

            estudiante.MostrarReporte();
        }

        static string SolicitarNombre()
        {
            while (true)
            {
                Console.Write("Nombre del estudiante: ");
                string nombre = Console.ReadLine()?.Trim() ?? "";

                if (!string.IsNullOrWhiteSpace(nombre))
                {
                    return nombre;
                }

                Console.WriteLine("⚠️ El nombre no puede estar vacío.\n");
            }
        }

        static double PedirNota(string etiqueta)
        {
            while (true)
            {
                Console.Write($"{etiqueta} nota (0.0 - 5.0): ");
                string entrada = Console.ReadLine()?.Trim() ?? "";

                if (double.TryParse(entrada, out double nota) && nota >= 0.0 && nota <= 5.0)
                {
                    return nota;
                }

                Console.WriteLine("⚠️ Nota inválida. Debe estar entre 0.0 y 5.0.\n");
            }
        }
    }
}
```

---

**Volver al [índice](./README.md)**
