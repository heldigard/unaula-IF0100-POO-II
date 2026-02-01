# Clase 01 - Ejercicios Guiados y Soluciones
## Introducción a C# y .NET

**IF0100 - Lenguaje de Programación OO II** | Unidad 1

---

## Tabla de Contenidos

- [Ejercicios de Clase](#ejercicios-de-clase)
- [Tarea para Casa](#tarea-para-casa)
- [Laboratorios Adicionales](#laboratorios-adicionales)

---

## Ejercicios de Clase

### Ejercicio 1: Calculadora de Área

#### Objetivo
Crear una aplicación de consola que calcule el área de diferentes figuras geométricas.

#### Requisitos Funcionales
1. Mostrar un menú con opciones:
   - 1. Rectángulo
   - 2. Círculo
   - 3. Triángulo
   - 4. Salir
2. Según la opción, solicitar los datos necesarios
3. Calcular y mostrar el área
4. Validar que los datos sean números positivos
5. Permitir realizar múltiples cálculos hasta que el usuario elija salir

#### Solución Completa

```csharp
using System;

namespace CalculadoraArea
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== CALCULADORA DE ÁREA ===\n");

            bool continuar = true;

            while (continuar)
            {
                Console.WriteLine("Seleccione una figura:");
                Console.WriteLine("1. Rectángulo");
                Console.WriteLine("2. Círculo");
                Console.WriteLine("3. Triángulo");
                Console.WriteLine("4. Salir");
                Console.Write("Opción: ");

                string entrada = Console.ReadLine();

                switch (entrada)
                {
                    case "1":
                        CalcularAreaRectangulo();
                        break;
                    case "2":
                        CalcularAreaCirculo();
                        break;
                    case "3":
                        CalcularAreaTriangulo();
                        break;
                    case "4":
                        continuar = false;
                        Console.WriteLine("\n¡Gracias por usar la calculadora!");
                        break;
                    default:
                        Console.WriteLine("\n⚠️ Opción inválida. Intente nuevamente.\n");
                        break;
                }

                Console.WriteLine(); // Línea en blanco
            }
        }

        static void CalcularAreaRectangulo()
        {
            Console.WriteLine("\n--- RECTÁNGULO ---");

            double baseRect = PedirNumeroPositivo("Base");
            double altura = PedirNumeroPositivo("Altura");

            double area = baseRect * altura;

            Console.WriteLine($"\nÁrea del rectángulo: {area:F2}");
        }

        static void CalcularAreaCirculo()
        {
            Console.WriteLine("\n--- CÍRCULO ---");

            double radio = PedirNumeroPositivo("Radio");

            double area = Math.PI * Math.Pow(radio, 2);

            Console.WriteLine($"\nÁrea del círculo: {area:F2}");
        }

        static void CalcularAreaTriangulo()
        {
            Console.WriteLine("\n--- TRIÁNGULO ---");

            double baseTri = PedirNumeroPositivo("Base");
            double altura = PedirNumeroPositivo("Altura");

            double area = (baseTri * altura) / 2.0;

            Console.WriteLine($"\nÁrea del triángulo: {area:F2}");
        }

        static double PedirNumeroPositivo(string etiqueta)
        {
            while (true)
            {
                Console.Write($"{etiqueta}: ");
                string entrada = Console.ReadLine()?.Trim() ?? "";

                if (double.TryParse(entrada, out double numero))
                {
                    if (numero > 0)
                    {
                        return numero;
                    }

                    Console.WriteLine("⚠️ El número debe ser positivo. Intente nuevamente.");
                }
                else
                {
                    Console.WriteLine("⚠️ Entrada inválida. Ingrese un número válido.");
                }
            }
        }
    }
}
```

#### Retos Adicionales

| Reto | Descripción |
|------|-------------|
| **Reto 1** | Agregar cálculo de área para trapecio |
| **Reto 2** | Guardar el historial de cálculos en una lista |
| **Reto 3** | Permitir elegir el número de decimales a mostrar |
| **Reto 4** | Crear una clase `Figura` con métodos virtuales |

---

### Ejercicio 2: Sistema de Calificaciones

#### Objetivo
Crear un sistema que calcule promedios de notas con validación robusta.

#### Requisitos Funcionales
1. Solicitar nombre del estudiante (no puede estar vacío)
2. Solicitar 3 notas (rango 0.0 - 5.0)
3. Calcular el promedio
4. Mostrar:
   - Promedio numérico
   - Calificación cualitativa (Excelente/Muy Bueno/etc.)
   - Estado (APROBADO/REPROBADO)
5. Validar todas las entradas

#### Solución Completa

Ver la solución completa en [codigo.md#ejemplo-sistema-de-calificaciones-completo](./codigo.md#ejemplo-sistema-de-calificaciones-completo)

#### Calificación Cualitativa

| Rango Promedio | Calificación |
|----------------|--------------|
| 4.5 - 5.0 | Excelente ⭐⭐⭐⭐⭐ |
| 4.0 - 4.49 | Muy Bueno ⭐⭐⭐⭐ |
| 3.5 - 3.99 | Bueno ⭐⭐⭐ |
| 3.0 - 3.49 | Aceptable ⭐⭐ |
| 0.0 - 2.99 | Insuficiente ⭐ |

#### Retos Adicionales

| Reto | Descripción |
|------|-------------|
| **Reto 1** | Permitir cantidad variable de notas (no solo 3) |
| **Reto 2** | Guardar los estudiantes en una lista |
| **Reto 3** | Exportar los resultados a un archivo de texto |
| **Reto 4** | Crear un menú para: Agregar, Listar, Buscar estudiantes |

---

## Tarea para Casa

### Proyecto: Calculadora de Promedios con POO

#### Descripción
Crear una aplicación de consola que gestione las calificaciones de múltiples estudiantes utilizando Programación Orientada a Objetos.

#### Requisitos

##### 1. Estructura del Proyecto

```
CalculadoraPromedios/
├── Models/
│   └── Estudiante.cs
├── Services/
│   └── EstudianteService.cs
├── Program.cs
└── appsettings.json (opcional)
```

##### 2. Clase Estudiante

```csharp
public class Estudiante
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public List<double> Calificaciones { get; set; }

    // Métodos requeridos:
    public double CalcularPromedio()
    public string CalificacionCualitativa()
    public string Estado()
    public override string ToString()
}
```

##### 3. Clase EstudianteService

```csharp
public class EstudianteService
{
    private List<Estudiante> _estudiantes;

    // Métodos requeridos:
    public void AgregarEstudiante(Estudiante estudiante)
    public Estudiante? ObtenerPorId(int id)
    public List<Estudiante> ObtenerTodos()
    public List<Estudiante> ObtenerAprobados()
    public List<Estudiante> ObtenerReprobados()
    public void MostrarReporteGeneral()
}
```

##### 4. Menú Principal

```
========================================
  CALCULADORA DE PROMEDIOS (POO)
========================================
1. Agregar Estudiante
2. Buscar Estudiante por ID
3. Listar Todos los Estudiantes
4. Ver Reporte General
5. Salir
========================================
Opción: _
```

##### 5. Validaciones

| Campo | Validación |
|-------|------------|
| Nombre | No vacío, mínimo 3 caracteres |
| Calificaciones | Entre 0.0 y 5.0 |
| Cantidad mínima | Al menos 1 calificación |

#### Checklist de Entrega

- [ ] **Funcionalidad**: El programa ejecuta sin errores
- [ ] **Validación**: Todas las entradas están validadas
- [ ] **POO**: Usa clases, propiedades, métodos correctamente
- [ ] **Colecciones**: Usa List<T> para almacenar estudiantes
- [ ] **Menú**: Navegación clara entre opciones
- [ ] **Formateo**: Salida bien presentada (tablas, alineación)
- [ ] **README**: Instrucciones de instalación y uso
- [ ] **Repositorio**: GitHub público con nombre descriptivo

#### Rúbrica de Evaluación

| Criterio | Excelente (5.0) | Bueno (4.0) | Aceptable (3.0) | Insuficiente (1.0-2.0) |
|----------|-----------------|-------------|-----------------|------------------------|
| **Funcionalidad** | Todos los requisitos funcionan correctamente | Funcionalidad principal completa, faltan detalles | Funcionalidad básica, varios faltantes | No funciona o faltan requisitos críticos |
| **POO** | Diseño correcto con encapsulación, métodos bien definidos | Usa clases pero falta encapsulación | Uso básico de clases sin diseño | No usa POO |
| **Validación** | Todas las validaciones con mensajes claros | Validaciones básicas | Pocas validaciones | Sin validaciones |
| **Código Limpio** | Convenciones correctas, comments, código legible | Algún error de convención | Varios errores de estilo | Código ilegible |
| **README** | Completo con screenshots y ejemplos | Básico pero funcional | Incompleto | Sin README |

#### Plantilla de Proyecto Starter

```csharp
// Models/Estudiante.cs
using System.Collections.Generic;

namespace CalculadoraPromedios.Models
{
    public class Estudiante
    {
        public int Id { get; set; }
        public string Nombre { get; set; }
        public List<double> Calificaciones { get; set; }

        public Estudiante(int id, string nombre)
        {
            Id = id;
            Nombre = nombre;
            Calificaciones = new List<double>();
        }

        public void AgregarCalificacion(double calificacion)
        {
            if (calificacion < 0.0 || calificacion > 5.0)
                throw new ArgumentOutOfRangeException(nameof(calificacion), "La calificación debe estar entre 0.0 y 5.0");

            Calificaciones.Add(calificacion);
        }

        public double CalcularPromedio()
        {
            if (Calificaciones.Count == 0)
                return 0.0;

            double suma = 0.0;
            foreach (var calificacion in Calificaciones)
            {
                suma += calificacion;
            }

            return suma / Calificaciones.Count;
        }

        public string CalificacionCualitativa()
        {
            double promedio = CalcularPromedio();

            return promedio switch
            {
                >= 4.5 => "Excelente ⭐⭐⭐⭐⭐",
                >= 4.0 => "Muy Bueno ⭐⭐⭐⭐",
                >= 3.5 => "Bueno ⭐⭐⭐",
                >= 3.0 => "Aceptable ⭐⭐",
                _ => "Insuficiente ⭐"
            };
        }

        public string Estado()
        {
            return CalcularPromedio() >= 3.0 ? "✅ APROBADO" : "❌ REPROBADO";
        }

        public override string ToString()
        {
            string calificacionesStr = string.Join(", ", Calificaciones.ConvertAll(c => c.ToString("F2")));
            return $"ID: {Id} | {Nombre} | Notas: [{calificacionesStr}] | Promedio: {CalcularPromedio():F2} | {Estado()}";
        }
    }
}

// Services/EstudianteService.cs
using System.Collections.Generic;
using System;
using CalculadoraPromedios.Models;
using System.Linq;

namespace CalculadoraPromedios.Services
{
    public class EstudianteService
    {
        private readonly List<Estudiante> _estudiantes;
        private int _nextId;

        public EstudianteService()
        {
            _estudiantes = new List<Estudiante>();
            _nextId = 1;
        }

        public Estudiante CrearEstudiante(string nombre)
        {
            var estudiante = new Estudiante(_nextId++, nombre);
            _estudiantes.Add(estudiante);
            return estudiante;
        }

        public Estudiante? ObtenerPorId(int id)
        {
            foreach (var estudiante in _estudiantes)
            {
                if (estudiante.Id == id)
                    return estudiante;
            }
            return null;
        }

        public List<Estudiante> ObtenerTodos()
        {
            return new List<Estudiante>(_estudiantes);
        }

        public List<Estudiante> ObtenerAprobados()
        {
            var aprobados = new List<Estudiante>();
            foreach (var estudiante in _estudiantes)
            {
                if (estudiante.CalcularPromedio() >= 3.0)
                    aprobados.Add(estudiante);
            }
            return aprobados;
        }

        public List<Estudiante> ObtenerReprobados()
        {
            var reprobados = new List<Estudiante>();
            foreach (var estudiante in _estudiantes)
            {
                if (estudiante.CalcularPromedio() < 3.0)
                    reprobados.Add(estudiante);
            }
            return reprobados;
        }

        public void MostrarReporteGeneral()
        {
            if (_estudiantes.Count == 0)
            {
                Console.WriteLine("No hay estudiantes registrados.");
                return;
            }

            Console.WriteLine("\n========================================");
            Console.WriteLine("           REPORTE GENERAL");
            Console.WriteLine("========================================");

            foreach (var estudiante in _estudiantes)
            {
                Console.WriteLine(estudiante.ToString());
            }

            Console.WriteLine("────────────────────────────────────────");

            double promedioGeneral = 0.0;
            foreach (var estudiante in _estudiantes)
            {
                promedioGeneral += estudiante.CalcularPromedio();
            }
            promedioGeneral /= _estudiantes.Count;

            var aprobados = ObtenerAprobados();
            var reprobados = ObtenerReprobados();

            Console.WriteLine($"Total estudiantes: {_estudiantes.Count}");
            Console.WriteLine($"Aprobados: {aprobados.Count} ({(aprobados.Count * 100.0 / _estudiantes.Count):F1}%)");
            Console.WriteLine($"Reprobados: {reprobados.Count} ({(reprobados.Count * 100.0 / _estudiantes.Count):F1}%)");
            Console.WriteLine($"Promedio general: {promedioGeneral:F2}");
            Console.WriteLine("========================================\n");
        }
    }
}

// Program.cs
using System;
using CalculadoraPromedios.Services;
using CalculadoraPromedios.Models;

namespace CalculadoraPromedios
{
    class Program
    {
        static void Main(string[] args)
        {
            var servicio = new EstudianteService();
            bool continuar = true;

            Console.OutputEncoding = System.Text.Encoding.UTF8;

            Console.WriteLine("========================================");
            Console.WriteLine("  CALCULADORA DE PROMEDIOS (POO)");
            Console.WriteLine("========================================\n");

            while (continuar)
            {
                MostrarMenu();
                string opcion = Console.ReadLine()?.Trim() ?? "";

                switch (opcion)
                {
                    case "1":
                        AgregarEstudiante(servicio);
                        break;
                    case "2":
                        BuscarEstudiante(servicio);
                        break;
                    case "3":
                        ListarEstudiantes(servicio);
                        break;
                    case "4":
                        servicio.MostrarReporteGeneral();
                        break;
                    case "5":
                        continuar = false;
                        Console.WriteLine("\n¡Gracias por usar el sistema!");
                        break;
                    default:
                        Console.WriteLine("\n⚠️ Opción inválida.\n");
                        break;
                }
            }
        }

        static void MostrarMenu()
        {
            Console.WriteLine("1. Agregar Estudiante");
            Console.WriteLine("2. Buscar Estudiante por ID");
            Console.WriteLine("3. Listar Todos los Estudiantes");
            Console.WriteLine("4. Ver Reporte General");
            Console.WriteLine("5. Salir");
            Console.Write("Opción: ");
        }

        static void AgregarEstudiante(EstudianteService servicio)
        {
            Console.WriteLine("\n--- AGREGAR ESTUDIANTE ---");

            string nombre = PedirNombre();
            var estudiante = servicio.CrearEstudiante(nombre);

            Console.WriteLine($"\nEstudiante creado con ID: {estudiante.Id}");

            bool agregarMas = true;
            while (agregarMas)
            {
                double nota = PedirNota();
                estudiante.AgregarCalificacion(nota);

                Console.Write("¿Agregar otra nota? (s/n): ");
                agregarMas = Console.ReadLine()?.Trim().ToLower() == "s";
            }

            Console.WriteLine("\n✅ Estudiante agregado exitosamente!");
            Console.WriteLine(estudiante.ToString());
            Console.WriteLine();
        }

        static void BuscarEstudiante(EstudianteService servicio)
        {
            Console.WriteLine("\n--- BUSCAR ESTUDIANTE ---");

            int id = PedirId();

            var estudiante = servicio.ObtenerPorId(id);

            if (estudiante != null)
            {
                Console.WriteLine("\n📋 Estudiante encontrado:");
                Console.WriteLine(estudiante.ToString());
            }
            else
            {
                Console.WriteLine($"\n⚠️ No se encontró estudiante con ID {id}");
            }

            Console.WriteLine();
        }

        static void ListarEstudiantes(EstudianteService servicio)
        {
            Console.WriteLine("\n--- LISTA DE ESTUDIANTES ---");

            var estudiantes = servicio.ObtenerTodos();

            if (estudiantes.Count == 0)
            {
                Console.WriteLine("No hay estudiantes registrados.");
            }
            else
            {
                foreach (var estudiante in estudiantes)
                {
                    Console.WriteLine(estudiante.ToString());
                }
            }

            Console.WriteLine();
        }

        static string PedirNombre()
        {
            while (true)
            {
                Console.Write("Nombre del estudiante: ");
                string nombre = Console.ReadLine()?.Trim() ?? "";

                if (!string.IsNullOrWhiteSpace(nombre) && nombre.Length >= 3)
                {
                    return nombre;
                }

                Console.WriteLine("⚠️ El nombre debe tener al menos 3 caracteres.\n");
            }
        }

        static double PedirNota()
        {
            while (true)
            {
                Console.Write("Calificación (0.0 - 5.0): ");
                string entrada = Console.ReadLine()?.Trim() ?? "";

                if (double.TryParse(entrada, out double nota))
                {
                    if (nota >= 0.0 && nota <= 5.0)
                    {
                        return nota;
                    }
                }

                Console.WriteLine("⚠️ Calificación inválida. Debe estar entre 0.0 y 5.0.\n");
            }
        }

        static int PedirId()
        {
            while (true)
            {
                Console.Write("ID del estudiante: ");
                string entrada = Console.ReadLine()?.Trim() ?? "";

                if (int.TryParse(entrada, out int id) && id > 0)
                {
                    return id;
                }

                Console.WriteLine("⚠️ ID inválido. Debe ser un número positivo.\n");
            }
        }
    }
}
```

---

## Laboratorios Adicionales

### Lab 1: Debugger de Memoria (Stack vs Heap)

#### Objetivo
Visualizar cómo funciona el stack y heap usando breakpoints en Visual Studio.

#### Instrucciones

1. Crear un nuevo proyecto de consola
2. Copiar el siguiente código
3. Poner breakpoints en las líneas indicadas
4. Ejecutar con F5 (Debug)
5. Inspeccionar las variables en cada breakpoint

```csharp
using System;
using System.Collections.Generic;

namespace MemoryDebuggerLab
{
    class Program
    {
        static void Main(string[] args)
        {
            // BREAKPOINT 1: Inspeccionar 'numero'
            int numero = 42;
            Console.WriteLine($"numero = {numero}");

            // BREAKPOINT 2: Inspeccionar 'lista1' y 'lista2'
            List<string> lista1 = new List<string> { "A", "B" };
            List<string> lista2 = lista1;  // Ambos referencian el mismo objeto

            Console.WriteLine($"lista1 = [{string.Join(", ", lista1)}]");
            Console.WriteLine($"lista2 = [{string.Join(", ", lista2)}]");

            // BREAKPOINT 3: ¿Cambió lista1 también?
            lista2.Add("C");

            Console.WriteLine($"Después de lista2.Add('C'):");
            Console.WriteLine($"lista1 = [{string.Join(", ", lista1)}]");
            Console.WriteLine($"lista2 = [{string.Join(", ", lista2)}]");

            // BREAKPOINT 4: Inspeccionar p1 y p2
            Persona p1 = new Persona("Juan", 25);
            Persona p2 = p1;

            Console.WriteLine($"\np1.Nombre = {p1.Nombre}");
            Console.WriteLine($"p2.Nombre = {p2.Nombre}");

            // BREAKPOINT 5: ¿Cambió p1 también?
            p2.Nombre = "María";

            Console.WriteLine($"\nDespués de p2.Nombre = 'María':");
            Console.WriteLine($"p1.Nombre = {p1.Nombre}");
            Console.WriteLine($"p2.Nombre = {p2.Nombre}");
        }
    }

    class Persona
    {
        public string Nombre { get; set; }
        public int Edad { get; set; }

        public Persona(string nombre, int edad)
        {
            Nombre = nombre;
            Edad = edad;
        }
    }
}
```

#### Preguntas de Reflexión

1. En el BREAKPOINT 2: ¿Cuál es el valor de `lista1.Count`?
2. En el BREAKPOINT 3: ¿Cuántos elementos tiene `lista1`? ¿Por qué?
3. En el BREAKPOINT 4: ¿Apuntan `p1` y `p2` al mismo objeto? (Usa `object.ReferenceEquals(p1, p2)`)
4. En el BREAKPOINT 5: ¿Por qué cambió `p1.Nombre`?

---

### Lab 2: Pattern Matching Refactorización

#### Objetivo
Refactorizar código con if-else anidados a pattern matching.

#### Código Original (Antes)

```csharp
public string ObtenerCategoriaCliente(Cliente cliente)
{
    if (cliente == null)
    {
        return "Cliente no registrado";
    }
    else
    {
        if (cliente.Tipo == "VIP")
        {
            if (cliente.AñosAntiguedad >= 5)
            {
                return "VIP Platinum";
            }
            else if (cliente.AñosAntiguedad >= 2)
            {
                return "VIP Gold";
            }
            else
            {
                return "VIP Standard";
            }
        }
        else if (cliente.Tipo == "Regular")
        {
            if (cliente.ComprasTotales > 10000)
            {
                return "Regular Premium";
            }
            else
            {
                return "Regular Básico";
            }
        }
        else
        {
            return "Tipo desconocido";
        }
    }
}
```

#### Tu Tarea

1. Analizar el código anterior
2. Refactorizarlo usando **switch expressions** y **pattern matching**
3. Mantener la misma funcionalidad
4. El código debe ser más legible y conciso

#### Clase Cliente

```csharp
public class Cliente
{
    public string Tipo { get; set; }
    public int AñosAntiguedad { get; set; }
    public decimal ComprasTotales { get; set; }
}
```

#### Solución Sugerida (click para revelar)

<details>
<summary>Ver solución refactorizada</summary>

```csharp
public string ObtenerCategoriaCliente(Cliente cliente)
{
    return cliente switch
    {
        null => "Cliente no registrado",
        { Tipo: "VIP", AñosAntiguedad: >= 5 } => "VIP Platinum",
        { Tipo: "VIP", AñosAntiguedad: >= 2 } => "VIP Gold",
        { Tipo: "VIP" } => "VIP Standard",
        { Tipo: "Regular", ComprasTotales: > 10000 } => "Regular Premium",
        { Tipo: "Regular" } => "Regular Básico",
        _ => "Tipo desconocido"
    };
}
```

</details>

---

### Lab 3: Nullable con Base de Datos Simulada

#### Objetivo
Manejar valores NULL correctamente al leer de una "base de datos" simulada.

#### Escenario

Tienes una tabla `Productos` con estas columnas:

| Columna | Tipo | ¿NULL? |
|---------|------|--------|
| Id | int | NO |
| Nombre | string | NO |
| Descripcion | string | SÍ |
| Precio | decimal | NO |
| Descuento | decimal | SÍ |

#### Tu Tarea

1. Crear una clase `ProductoDto` con nullable types donde corresponda
2. Crear un método que "lea" de la base de datos (simulada con DataTable)
3. Manejar correctamente los valores NULL
4. Mostrar los productos con formato especial para valores NULL

```csharp
// ProductsDao.cs (simulación)
public static class ProductosDao
{
    public static DataTable ObtenerTodos()
    {
        var dt = new DataTable();
        dt.Columns.Add("Id", typeof(int));
        dt.Columns.Add("Nombre", typeof(string));
        dt.Columns.Add("Descripcion", typeof(string));
        dt.Columns.Add("Precio", typeof(decimal));
        dt.Columns.Add("Descuento", typeof(decimal));

        dt.Rows.Add(1, "Laptop", "Laptop de alto rendimiento", 2500000m, 10.0m);
        dt.Rows.Add(2, "Mouse", DBNull.Value, 45000m, DBNull.Value);  // Sin descripción, sin descuento
        dt.Rows.Add(3, "Teclado", "Teclado mecánico RGB", 120000m, 5.0m);
        dt.Rows.Add(4, "Monitor", DBNull.Value, 850000m, DBNull.Value);

        return dt;
    }
}
```

#### Solución Sugerida

<details>
<summary>Ver solución completa</summary>

```csharp
using System;
using System.Data;
using System.Collections.Generic;

public class ProductoDto
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public string? Descripcion { get; set; }  // Nullable
    public decimal Precio { get; set; }
    public decimal? Descuento { get; set; }  // Nullable

    public decimal PrecioFinal =>
        Descuento.HasValue
            ? Precio * (1 - Descuento.Value / 100)
            : Precio;

    public override string ToString()
    {
        string desc = Descripcion ?? "Sin descripción";
        string descuentoStr = Descuento.HasValue ? $"{Descuento.Value:F1}%" : "N/A";

        return $"[{Id}] {Nombre} - {desc} | ${PrecioFinal:N0} (was ${Precio:N0}, {descuentoStr} off)";
    }
}

public class ProductoService
{
    public static List<ProductoDto> ObtenerTodos()
    {
        var productos = new List<ProductoDto>();
        var dt = ProductosDao.ObtenerTodos();

        foreach (DataRow row in dt.Rows)
        {
            productos.Add(MapearAProducto(row));
        }

        return productos;
    }

    private static ProductoDto MapearAProducto(DataRow row)
    {
        return new ProductoDto
        {
            Id = (int)row["Id"],
            Nombre = (string)row["Nombre"],
            Descripcion = row["Descripcion"] as string,  // NULL → null
            Precio = (decimal)row["Precio"],
            Descuento = row["Descuento"] as decimal?  // NULL → null
        };
    }
}

// Uso
var productos = ProductoService.ObtenerTodos();
foreach (var p in productos)
{
    Console.WriteLine(p.ToString());
}
```

Salida esperada:

```
[1] Laptop - Laptop de alto rendimiento | $2,250,000 (was $2,500,000, 10.0% off)
[2] Mouse - Sin descripción | $45,000 (was $45,000, N/A off)
[3] Teclado - Teclado mecánico RGB | $114,000 (was $120,000, 5.0% off)
[4] Monitor - Sin descripción | $850,000 (was $850,000, N/A off)
```

</details>

---

## Ejercicios de Repaso

### Ejercicio R1: ¿Qué imprime este código?

```csharp
var a = new List<int> { 1, 2, 3 };
var b = a;
b.Add(4);

Console.WriteLine(string.Join(", ", a));  // ¿Qué imprime?
```

<details>
<summary>Ver respuesta</summary>

**Salida:** `1, 2, 3, 4`

**Explicación:** `List<int>` es un reference type. `b = a` copia la referencia, no la lista. Ambos `a` y `b` apuntan al mismo objeto en memoria.

</details>

---

### Ejercicio R2: ¿Cuál es el valor de `x`?

```csharp
int? y = null;
int x = y ?? -1;

Console.WriteLine(x);  // ¿Qué imprime?
```

<details>
<summary>Ver respuesta</summary>

**Salida:** `-1`

**Explicación:** El operador `??` (null-coalescing) retorna el valor derecho si el izquierdo es `null`. Como `y` es `null`, `x` se asigna con `-1`.

</details>

---

### Ejercicio R3: ¿Qué devuelve este método?

```csharp
string ObtenerCategoria(double promedio)
{
    return promedio switch
    {
        >= 4.5 => "Excelente",
        >= 4.0 => "Muy Bueno",
        >= 3.5 => "Bueno",
        _ => "Otro"
    };
}

// ¿Qué devuelve ObtenerCategoria(4.2)?
```

<details>
<summary>Ver respuesta</summary>

**Salida:** `"Muy Bueno"`

**Explicación:** El switch expression evalúa de arriba a abajo. `4.2 >= 4.5` es `false`, pero `4.2 >= 4.0` es `true`, por lo que retorna `"Muy Bueno"`.

</details>

---

**Volver al [índice](./README.md)**
