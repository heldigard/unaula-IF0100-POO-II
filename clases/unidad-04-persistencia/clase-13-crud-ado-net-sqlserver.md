---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 4'
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

# CRUD con ADO.NET y SQL Server

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## 💡 ¿Por qué es importante el CRUD?

CRUD es la base de toda aplicación que gestiona datos:

**Ejemplos:** 🏦 Banca, 🛒 E-commerce, 📱 Redes sociales

**Industria:** Microsoft, bancos y grandes corporaciones usan ADO.NET para sistemas críticos.

---

## Objetivos

Al finalizar esta clase, el estudiante será capaz de:

1. **Configurar** una conexión a SQL Server
2. **Ejecutar** operaciones CRUD con ADO.NET
3. **Usar** parámetros para evitar SQL Injection
4. **Aplicar** transacciones básicas

**Duración:** 90 minutos

---

## Agenda

1. Conexión a SQL Server (15 min)
2. SqlCommand y parámetros (25 min)
3. CRUD completo (30 min)
4. Transacciones (10 min)
5. Actividad práctica (10 min)

---

## 1. Conexión

```csharp
using System.Data.SqlClient;

var cs = "Server=localhost;Database=tienda;Trusted_Connection=True;";
using var conn = new SqlConnection(cs);
conn.Open();
```

---

## 2. Comandos con parámetros

```csharp
string sql = "INSERT INTO Productos (Nombre, Precio) VALUES (@n, @p)";
using var cmd = new SqlCommand(sql, conn);
cmd.Parameters.AddWithValue("@n", nombre);
cmd.Parameters.AddWithValue("@p", precio);
cmd.ExecuteNonQuery();
```

---

## 3. CRUD básico

- **Create**: INSERT
- **Read**: SELECT + SqlDataReader
- **Update**: UPDATE
- **Delete**: DELETE

```csharp
string sql = "SELECT Id, Nombre, Precio FROM Productos";
using var cmd = new SqlCommand(sql, conn);
using var reader = cmd.ExecuteReader();
while (reader.Read())
{
    Console.WriteLine($"{reader["Id"]} {reader["Nombre"]}");
}
```

---

## 4. Transacciones

```csharp
using var tx = conn.BeginTransaction();
try
{
    var cmd = new SqlCommand(sql, conn, tx);
    cmd.ExecuteNonQuery();
    tx.Commit();
}
catch
{
    tx.Rollback();
}
```

---

## Actividad (10 min)

En parejas:
1. Crear tabla `Clientes`
2. Insertar 3 registros
3. Consultar y mostrar resultados

---

## Resumen

| Concepto | Idea clave |
| ---------- | ------------ |
| SqlConnection | Abre canal con DB |
| SqlCommand | Ejecuta SQL |
| Parámetros | Seguridad |
| Transacciones | Consistencia |

---

## Próxima Clase

### Clase 14: Persistencia en Archivos Planos

- Lectura/escritura
- CSV/JSON
- Serialización

**¡Nos vemos!**


---


## 📚 CRUD Completo con ADO.NET y SQL Server

### Arquitectura de la Aplicación

```
┌─────────────────────────────────────┐
│     Capa de Presentación            │
│     (Windows Forms / Console)       │
└─────────────┬───────────────────────┘
              │
┌─────────────▼───────────────────────┐
│     Capa de Lógica de Negocio       │
│     (Clases, Validaciones)          │
└─────────────┬───────────────────────┘
              │
┌─────────────▼───────────────────────┐
│     Capa de Acceso a Datos          │
│     (ADO.NET - SqlConnection)       │
└─────────────┬───────────────────────┘
              │
┌─────────────▼───────────────────────┐
│        SQL Server Database          │
│        (Tabla: Estudiantes)         │
└─────────────────────────────────────┘
```

---
#### Base de Datos SQL Server


```sql
-- Crear base de datos
CREATE DATABASE UniversidadDB;
GO

USE UniversidadDB;
GO

-- Crear tabla Estudiantes
CREATE TABLE Estudiantes (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Codigo NVARCHAR(20) NOT NULL UNIQUE,
    Nombre NVARCHAR(100) NOT NULL,
    Apellido NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL,
    FechaNacimiento DATE,
    Promedio DECIMAL(3,2) CHECK (Promedio BETWEEN 0 AND 5),
    Activo BIT DEFAULT 1,
    FechaCreacion DATETIME DEFAULT GETDATE()
);
GO

---
#### Base de Datos SQL Server


-- Insertar datos de prueba
INSERT INTO Estudiantes (Codigo, Nombre, Apellido, Email, FechaNacimiento, Promedio)
VALUES 
    ('EST001', 'Juan', 'Pérez', 'juan.perez@unaula.edu.co', '2000-05-15', 4.2),
    ('EST002', 'María', 'González', 'maria.gonzalez@unaula.edu.co', '1999-08-20', 4.5),
    ('EST003', 'Carlos', 'Ramírez', 'carlos.ramirez@unaula.edu.co', '2001-03-10', 3.8);
GO
```

---
### 2️⃣ Modelo de Entidad (Clase C#)

```csharp
using System;

namespace UniversidadApp.Models
{
    public class Estudiante
    {
        public int Id { get; set; }
        public string Codigo { get; set; }
        public string Nombre { get; set; }
        public string Apellido { get; set; }
        public string Email { get; set; }
        public DateTime FechaNacimiento { get; set; }
        public decimal Promedio { get; set; }
        public bool Activo { get; set; }
        public DateTime FechaCreacion { get; set; }

        // Propiedad calculada
        public string NombreCompleto => $"{Nombre} {Apellido}";
        
        // Edad
        public int Edad => DateTime.Now.Year - FechaNacimiento.Year;

---
### 2️⃣ Modelo de Entidad (Clase C#)


        // Override ToString para facilitar visualización
        public override string ToString()
        {
            return $"[{Codigo}] {NombreCompleto} - Promedio: {Promedio:F2}";
        }
    }
}
```

---
### 3️⃣ Capa de Acceso a Datos - Estructura Base

```csharp
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using UniversidadApp.Models;

namespace UniversidadApp.Data
{
    public class EstudianteRepository
    {
        private readonly string _connectionString;

        public EstudianteRepository()
        {
            // Cadena de conexión desde configuración
            _connectionString = "Server=localhost;Database=UniversidadDB;" +
                              "Integrated Security=true;";
        }
```

---
### 3️⃣ Capa de Acceso a Datos - Método CREATE

```csharp
        public int Crear(Estudiante estudiante)
        {
            const string query = @"
                INSERT INTO Estudiantes (Codigo, Nombre, Apellido, Email, 
                                       FechaNacimiento, Promedio, Activo)
                VALUES (@Codigo, @Nombre, @Apellido, @Email, 
                       @FechaNacimiento, @Promedio, @Activo);
                SELECT CAST(SCOPE_IDENTITY() AS INT);";

            using (var conexion = new SqlConnection(_connectionString))
            using (var comando = new SqlCommand(query, conexion))
            {
                comando.Parameters.AddWithValue("@Codigo", estudiante.Codigo);
                comando.Parameters.AddWithValue("@Nombre", estudiante.Nombre);
                comando.Parameters.AddWithValue("@Apellido", estudiante.Apellido);
                comando.Parameters.AddWithValue("@Email", estudiante.Email);
                comando.Parameters.AddWithValue("@FechaNacimiento", 
                    estudiante.FechaNacimiento);
                comando.Parameters.AddWithValue("@Promedio", estudiante.Promedio);
                comando.Parameters.AddWithValue("@Activo", estudiante.Activo);

                try
                {
                    conexion.Open();
                    int nuevoId = (int)comando.ExecuteScalar();
                    return nuevoId;
                }
                catch (SqlException ex)
                {
                    // Manejo de errores (código duplicado, etc.)
                    if (ex.Number == 2627) // Violación de clave única
                        throw new Exception($"Ya existe un estudiante con código {estudiante.Codigo}");
                    
                    throw;
                }
            }
        }
```

---
### 3️⃣ Capa de Acceso a Datos - Método READ (Lista)

```csharp
        public List<Estudiante> ObtenerTodos()
        {
            const string query = @"
                SELECT Id, Codigo, Nombre, Apellido, Email, 
                       FechaNacimiento, Promedio, Activo, FechaCreacion
                FROM Estudiantes
                WHERE Activo = 1
                ORDER BY Apellido, Nombre";

            var estudiantes = new List<Estudiante>();

            using (var conexion = new SqlConnection(_connectionString))
            using (var comando = new SqlCommand(query, conexion))
            {
                conexion.Open();
                using (var reader = comando.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        estudiantes.Add(MapearEstudiante(reader));
                    }
                }
            }

            return estudiantes;
        }
```

---
### 3️⃣ Capa de Acceso a Datos - Método READ (Individual)

```csharp
        public Estudiante ObtenerPorId(int id)
        {
            const string query = @"
                SELECT Id, Codigo, Nombre, Apellido, Email, 
                       FechaNacimiento, Promedio, Activo, FechaCreacion
                FROM Estudiantes
                WHERE Id = @Id";

            using (var conexion = new SqlConnection(_connectionString))
            using (var comando = new SqlCommand(query, conexion))
            {
                comando.Parameters.AddWithValue("@Id", id);
                
                conexion.Open();
                using (var reader = comando.ExecuteReader())
                {
                    if (reader.Read())
                        return MapearEstudiante(reader);
                    
                    return null;
                }
            }
        }

        public Estudiante ObtenerPorCodigo(string codigo)
        {
            const string query = @"
                SELECT Id, Codigo, Nombre, Apellido, Email, 
                       FechaNacimiento, Promedio, Activo, FechaCreacion
                FROM Estudiantes
                WHERE Codigo = @Codigo";

            using (var conexion = new SqlConnection(_connectionString))
            using (var comando = new SqlCommand(query, conexion))
            {
                comando.Parameters.AddWithValue("@Codigo", codigo);
                
                conexion.Open();
                using (var reader = comando.ExecuteReader())
                {
                    if (reader.Read())
                        return MapearEstudiante(reader);
                    
                    return null;
                }
            }
        }
```

---
### 3️⃣ Capa de Acceso a Datos - Método UPDATE

```csharp
        public bool Actualizar(Estudiante estudiante)
        {
            const string query = @"
                UPDATE Estudiantes
                SET Nombre = @Nombre,
                    Apellido = @Apellido,
                    Email = @Email,
                    FechaNacimiento = @FechaNacimiento,
                    Promedio = @Promedio,
                    Activo = @Activo
                WHERE Id = @Id";

            using (var conexion = new SqlConnection(_connectionString))
            using (var comando = new SqlCommand(query, conexion))
            {
                comando.Parameters.AddWithValue("@Id", estudiante.Id);
                comando.Parameters.AddWithValue("@Nombre", estudiante.Nombre);
                comando.Parameters.AddWithValue("@Apellido", estudiante.Apellido);
                comando.Parameters.AddWithValue("@Email", estudiante.Email);
                comando.Parameters.AddWithValue("@FechaNacimiento", 
                    estudiante.FechaNacimiento);
                comando.Parameters.AddWithValue("@Promedio", estudiante.Promedio);
                comando.Parameters.AddWithValue("@Activo", estudiante.Activo);

                conexion.Open();
                int filasAfectadas = comando.ExecuteNonQuery();
                return filasAfectadas > 0;
            }
        }
```

---
### 3️⃣ Capa de Acceso a Datos - Métodos DELETE

```csharp
        public bool EliminarLogico(int id)
        {
            // Eliminación lógica (cambia Activo = 0)
            const string query = "UPDATE Estudiantes SET Activo = 0 WHERE Id = @Id";

            using (var conexion = new SqlConnection(_connectionString))
            using (var comando = new SqlCommand(query, conexion))
            {
                comando.Parameters.AddWithValue("@Id", id);
                
                conexion.Open();
                int filasAfectadas = comando.ExecuteNonQuery();
                return filasAfectadas > 0;
            }
        }

        public bool EliminarFisico(int id)
        {
            // Eliminación física (borra el registro)
            const string query = "DELETE FROM Estudiantes WHERE Id = @Id";

            using (var conexion = new SqlConnection(_connectionString))
            using (var comando = new SqlCommand(query, conexion))
            {
                comando.Parameters.AddWithValue("@Id", id);
                
                conexion.Open();
                int filasAfectadas = comando.ExecuteNonQuery();
                return filasAfectadas > 0;
            }
        }
```

---
### 3️⃣ Capa de Acceso a Datos - Métodos Auxiliares

```csharp
        private Estudiante MapearEstudiante(SqlDataReader reader)
        {
            return new Estudiante
            {
                Id = reader.GetInt32(0),
                Codigo = reader.GetString(1),
                Nombre = reader.GetString(2),
                Apellido = reader.GetString(3),
                Email = reader.GetString(4),
                FechaNacimiento = reader.GetDateTime(5),
                Promedio = reader.GetDecimal(6),
                Activo = reader.GetBoolean(7),
                FechaCreacion = reader.GetDateTime(8)
            };
        }
    }
}
```

---
### 4️⃣ Aplicación de Consola - Menú Principal

```csharp
using System;
using UniversidadApp.Data;
using UniversidadApp.Models;

namespace UniversidadApp
{
    class Program
    {
        static void Main(string[] args)
        {
            var repo = new EstudianteRepository();

            while (true)
            {
                Console.Clear();
                Console.WriteLine("╔════════════════════════════════════╗");
                Console.WriteLine("║   GESTIÓN DE ESTUDIANTES UNAULA   ║");
                Console.WriteLine("╚════════════════════════════════════╝");
                Console.WriteLine();
                Console.WriteLine("1. Crear estudiante");
                Console.WriteLine("2. Listar estudiantes");
                Console.WriteLine("3. Buscar por ID");
                Console.WriteLine("4. Actualizar estudiante");
                Console.WriteLine("5. Eliminar estudiante");
                Console.WriteLine("6. Salir");
                Console.WriteLine();
                Console.Write("Seleccione opción: ");

                var opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1": CrearEstudiante(repo); break;
                    case "2": ListarEstudiantes(repo); break;
                    case "3": BuscarPorId(repo); break;
                    case "4": ActualizarEstudiante(repo); break;
                    case "5": EliminarEstudiante(repo); break;
                    case "6": return;
                }

                Console.WriteLine("\nPresione cualquier tecla...");
                Console.ReadKey();
            }
        }
```

---
### 4️⃣ Aplicación de Consola - Crear Estudiante

```csharp
        static void CrearEstudiante(EstudianteRepository repo)
        {
            Console.WriteLine("\n--- CREAR NUEVO ESTUDIANTE ---\n");

            var estudiante = new Estudiante();

            Console.Write("Código: ");
            estudiante.Codigo = Console.ReadLine();

            Console.Write("Nombre: ");
            estudiante.Nombre = Console.ReadLine();

            Console.Write("Apellido: ");
            estudiante.Apellido = Console.ReadLine();

            Console.Write("Email: ");
            estudiante.Email = Console.ReadLine();

            Console.Write("Fecha de Nacimiento (yyyy-MM-dd): ");
            estudiante.FechaNacimiento = DateTime.Parse(Console.ReadLine());

            Console.Write("Promedio (0.0 - 5.0): ");
            estudiante.Promedio = decimal.Parse(Console.ReadLine());

            estudiante.Activo = true;

            try
            {
                int id = repo.Crear(estudiante);
                Console.WriteLine($"\n✓ Estudiante creado con ID: {id}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"\n✗ Error: {ex.Message}");
            }
        }
```

---
### 4️⃣ Aplicación de Consola - Listar y Buscar

```csharp
        static void ListarEstudiantes(EstudianteRepository repo)
        {
            Console.WriteLine("\n--- LISTA DE ESTUDIANTES ---\n");

            var estudiantes = repo.ObtenerTodos();

            if (estudiantes.Count == 0)
            {
                Console.WriteLine("No hay estudiantes registrados.");
                return;
            }

            Console.WriteLine($"{"ID",-5} {"Código",-10} {"Nombre Completo",-30} " +
                            $"{"Promedio",-10} {"Edad",-5}");
            Console.WriteLine(new string('-', 70));

            foreach (var est in estudiantes)
            {
                Console.WriteLine($"{est.Id,-5} {est.Codigo,-10} " +
                                $"{est.NombreCompleto,-30} " +
                                $"{est.Promedio,-10:F2} {est.Edad,-5}");
            }

            Console.WriteLine($"\nTotal: {estudiantes.Count} estudiantes");
        }

        static void BuscarPorId(EstudianteRepository repo)
        {
            Console.Write("\nIngrese ID del estudiante: ");
            int id = int.Parse(Console.ReadLine());

            var estudiante = repo.ObtenerPorId(id);

            if (estudiante == null)
            {
                Console.WriteLine("\n✗ Estudiante no encontrado.");
                return;
            }

            Console.WriteLine("\n--- DATOS DEL ESTUDIANTE ---");
            Console.WriteLine($"ID:              {estudiante.Id}");
            Console.WriteLine($"Código:          {estudiante.Codigo}");
            Console.WriteLine($"Nombre:          {estudiante.NombreCompleto}");
            Console.WriteLine($"Email:           {estudiante.Email}");
            Console.WriteLine($"Fecha Nac.:      " +
                            $"{estudiante.FechaNacimiento:dd/MM/yyyy}");
            Console.WriteLine($"Edad:            {estudiante.Edad} años");
            Console.WriteLine($"Promedio:        {estudiante.Promedio:F2}");
            Console.WriteLine($"Estado:          " +
                            $"{(estudiante.Activo ? "Activo" : "Inactivo")}");
        }
```

---
### 4️⃣ Aplicación de Consola - Actualizar y Eliminar

```csharp
        static void ActualizarEstudiante(EstudianteRepository repo)
        {
            Console.Write("\nIngrese ID del estudiante a actualizar: ");
            int id = int.Parse(Console.ReadLine());

            var estudiante = repo.ObtenerPorId(id);

            if (estudiante == null)
            {
                Console.WriteLine("\n✗ Estudiante no encontrado.");
                return;
            }

            Console.WriteLine($"\nActualizando: {estudiante}");
            Console.WriteLine("(Presione Enter para mantener el valor actual)\n");

            Console.Write($"Nombre [{estudiante.Nombre}]: ");
            string nombre = Console.ReadLine();
            if (!string.IsNullOrEmpty(nombre))
                estudiante.Nombre = nombre;

            Console.Write($"Apellido [{estudiante.Apellido}]: ");
            string apellido = Console.ReadLine();
            if (!string.IsNullOrEmpty(apellido))
                estudiante.Apellido = apellido;

            Console.Write($"Promedio [{estudiante.Promedio}]: ");
            string promedio = Console.ReadLine();
            if (!string.IsNullOrEmpty(promedio))
                estudiante.Promedio = decimal.Parse(promedio);

            bool actualizado = repo.Actualizar(estudiante);

            Console.WriteLine(actualizado 
                ? "\n✓ Estudiante actualizado correctamente." 
                : "\n✗ Error al actualizar.");
        }

        static void EliminarEstudiante(EstudianteRepository repo)
        {
            Console.Write("\nIngrese ID del estudiante a eliminar: ");
            int id = int.Parse(Console.ReadLine());

            var estudiante = repo.ObtenerPorId(id);

            if (estudiante == null)
            {
                Console.WriteLine("\n✗ Estudiante no encontrado.");
                return;
            }

            Console.WriteLine($"\n¿Está seguro de eliminar a {estudiante}?");
            Console.Write("(S/N): ");
            string confirmacion = Console.ReadLine();

            if (confirmacion.ToUpper() == "S")
            {
                bool eliminado = repo.EliminarLogico(id);
                Console.WriteLine(eliminado 
                    ? "\n✓ Estudiante eliminado correctamente." 
                    : "\n✗ Error al eliminar.");
            }
        }
    }
}
```

---

## 💻 Actividad Práctica

### Ejercicio 1: Agregar Búsqueda por Nombre

Implementar método `BuscarPorNombre(string nombre)` que retorne todos los estudiantes cuyo nombre o apellido contenga el texto buscado.

### Ejercicio 2: Paginación

Modificar `ObtenerTodos()` para que acepte parámetros `int pagina, int registrosPorPagina`.

### Ejercicio 3: Transacciones

Implementar método `TransferirPromedios()` que actualice múltiples estudiantes en una sola transacción.

### Tiempo estimado: 90 minutos

---

## Resumen de la Clase

### Conceptos Clave Aprendidos

| Concepto | Descripcion |
|----------|-------------|
| SqlConnection | Maneja la conexion a SQL Server |
| SqlCommand | Ejecuta comandos SQL |
| SqlDataReader | Lee datos forward-only |
| Parametros | Evitan SQL Injection |
| Transacciones | Garantizan integridad |

### Proxima Clase: Persistencia en Archivos Planos (TXT, CSV, JSON)

---
