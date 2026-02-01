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
| Paginacion | Consultas eficientes |
| Bulk Operations | Inserciones masivas |
| Advanced Queries | Busquedas complejas |

### Proxima Clase: Persistencia en Archivos Planos (TXT, CSV, JSON)


---

## 📄 Paginación de Resultados

### Eficiencia en grandes volúmenes de datos

```
┌─────────────────────────────────────────────────────────────┐
│              PAGINACIÓN OFFSET/FETCH                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Sin Paginación:               Con Paginación:              │
│  ─────────────────             ────────────────             │
│                                                             │
│  SELECT * FROM Estudiantes  SELECT * FROM Estudiantes       │
│  → 100,000 filas              → ORDER BY Id                │
│  → Lento                       → OFFSET 0 ROWS             │
│  → Mucho memoria               → FETCH NEXT 10 ROWS ONLY    │
│                                                             │
│                               → Solo 10 filas              │
│                               → Rápido                      │
│                               → Eficiente                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```csharp
public class PaginatedResult<T>
{
    public List<T> Items { get; set; }
    public int TotalCount { get; set; }
    public int PageNumber { get; set; }
    public int PageSize { get; set; }
    public int TotalPages => (int)Math.Ceiling(TotalCount / (double)PageSize);
    public bool HasPrevious => PageNumber > 1;
    public bool HasNext => PageNumber < TotalPages;
}

public class EstudianteRepositoryPaginado
{
    private readonly string _connectionString;

    public async Task<PaginatedResult<Estudiante>> ObtenerPaginadoAsync(
        int pageNumber, int pageSize)
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        // Query para contar total
        var countQuery = "SELECT COUNT(*) FROM Estudiantes WHERE Activo = 1";
        using (var countCmd = new SqlCommand(countQuery, connection))
        {
            var totalCount = (int)await countCmd.ExecuteScalarAsync();

            // Query paginado
            var offset = (pageNumber - 1) * pageSize;
            var dataQuery = @"
                SELECT Id, Codigo, Nombre, Apellido, Email, Promedio
                FROM Estudiantes
                WHERE Activo = 1
                ORDER BY Apellido, Nombre
                OFFSET @Offset ROWS
                FETCH NEXT @PageSize ROWS ONLY";

            using var dataCmd = new SqlCommand(dataQuery, connection);
            dataCmd.Parameters.AddWithValue("@Offset", offset);
            dataCmd.Parameters.AddWithValue("@PageSize", pageSize);

            using var reader = await dataCmd.ExecuteReaderAsync();
            var items = new List<Estudiante>();

            while (await reader.ReadAsync())
            {
                items.Add(MapFromReader(reader));
            }

            return new PaginatedResult<Estudiante>
            {
                Items = items,
                TotalCount = totalCount,
                PageNumber = pageNumber,
                PageSize = pageSize
            };
        }
    }

    // Búsqueda paginada con filtros
    public async Task<PaginatedResult<Estudiante>> BuscarPaginadoAsync(
        string termino, int carreraId, int pageNumber, int pageSize)
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        // WHERE dinámico según parámetros
        var whereClause = "WHERE Activo = 1";
        var whereParams = new List<string>();

        if (!string.IsNullOrEmpty(termino))
        {
            whereClause += " AND (Nombre LIKE @Termino OR Apellido LIKE @Termino)";
        }

        if (carreraId > 0)
        {
            whereClause += " AND CarreraId = @CarreraId";
        }

        var countQuery = $"SELECT COUNT(*) FROM Estudiantes {whereClause}";
        var dataQuery = $@"
            SELECT Id, Codigo, Nombre, Apellido, Email, Promedio
            FROM Estudiantes
            {whereClause}
            ORDER BY Apellido, Nombre
            OFFSET @Offset ROWS
            FETCH NEXT @PageSize ROWS ONLY";

        using var countCmd = new SqlCommand(countQuery, connection);
        using var dataCmd = new SqlCommand(dataQuery, connection);

        // Agregar parámetros condicionales
        if (!string.IsNullOrEmpty(termino))
        {
            var paramValue = $"%{termino}%";
            countCmd.Parameters.AddWithValue("@Termino", paramValue);
            dataCmd.Parameters.AddWithValue("@Termino", paramValue);
        }

        if (carreraId > 0)
        {
            countCmd.Parameters.AddWithValue("@CarreraId", carreraId);
            dataCmd.Parameters.AddWithValue("@CarreraId", carreraId);
        }

        var offset = (pageNumber - 1) * pageSize;
        countCmd.Parameters.AddWithValue("@Offset", offset);
        countCmd.Parameters.AddWithValue("@PageSize", pageSize);
        dataCmd.Parameters.AddWithValue("@Offset", offset);
        dataCmd.Parameters.AddWithValue("@PageSize", pageSize);

        var totalCount = (int)await countCmd.ExecuteScalarAsync();

        using var reader = await dataCmd.ExecuteReaderAsync();
        var items = new List<Estudiante>();

        while (await reader.ReadAsync())
        {
            items.Add(MapFromReader(reader));
        }

        return new PaginatedResult<Estudiante>
        {
            Items = items,
            TotalCount = totalCount,
            PageNumber = pageNumber,
            PageSize = pageSize
        };
    }
}

// Uso en consola
static async Task MostrarPaginaAsync(EstudianteRepositoryPaginado repo, int pagina)
{
    var resultado = await repo.ObtenerPaginadoAsync(pagina, 10);

    Console.WriteLine($"\n=== Página {resultado.PageNumber} de {resultado.TotalPages} ===");
    Console.WriteLine($"Total registros: {resultado.TotalCount}\n");

    foreach (var est in resultado.Items)
    {
        Console.WriteLine($"[{est.Codigo}] {est.NombreCompleto} - {est.Promedio:F2}");
    }

    if (resultado.HasPrevious)
        Console.WriteLine("\n[A]nterior");
    if (resultado.HasNext)
        Console.WriteLine("[S]iguiente");
}
```

---

## Bulk Operations

### Inserciones y actualizaciones masivas

```csharp
public class EstudianteRepositoryBulk
{
    // Opción 1: Bulk Insert con SqlBulkCopy (MÁS RÁPIDO)
    public async Task BulkInsertAsync(List<Estudiante> estudiantes)
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        using var bulkCopy = new SqlBulkCopy(connection);
        bulkCopy.DestinationTableName = "Estudiantes";

        // Mapear columnas
        bulkCopy.ColumnMappings.Add("Codigo", "Codigo");
        bulkCopy.ColumnMappings.Add("Nombre", "Nombre");
        bulkCopy.ColumnMappings.Add("Apellido", "Apellido");
        bulkCopy.ColumnMappings.Add("Email", "Email");
        bulkCopy.ColumnMappings.Add("Promedio", "Promedio");
        bulkCopy.ColumnMappings.Add("FechaNacimiento", "FechaNacimiento");
        bulkCopy.ColumnMappings.Add("Activo", "Activo");

        // Convertir a DataTable
        var dataTable = ToDataTable(estudiantes);

        // Ejecutar bulk insert
        await bulkCopy.WriteToServerAsync(dataTable);

        Console.WriteLine($"✓ {estudiantes.Count} registros insertados en bulk");
    }

    // Opción 2: Transacción con múltiples INSERT
    public async Task BulkInsertTransaccionAsync(List<Estudiante> estudiantes)
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        using var transaction = connection.BeginTransaction();

        try
        {
            var query = @"
                INSERT INTO Estudiantes (Codigo, Nombre, Apellido, Email, Promedio, Activo)
                VALUES (@Codigo, @Nombre, @Apellido, @Email, @Promedio, @Activo)";

            using var command = new SqlCommand(query, connection, transaction);
            command.Parameters.Add("@Codigo", SqlDbType.NVarChar, 20);
            command.Parameters.Add("@Nombre", SqlDbType.NVarChar, 100);
            command.Parameters.Add("@Apellido", SqlDbType.NVarChar, 100);
            command.Parameters.Add("@Email", SqlDbType.NVarChar, 100);
            command.Parameters.Add("@Promedio", SqlDbType.Decimal);
            command.Parameters.Add("@Activo", SqlDbType.Bit);

            foreach (var est in estudiantes)
            {
                command.Parameters["@Codigo"].Value = est.Codigo;
                command.Parameters["@Nombre"].Value = est.Nombre;
                command.Parameters["@Apellido"].Value = est.Apellido;
                command.Parameters["@Email"].Value = (object)est.Email ?? DBNull.Value;
                command.Parameters["@Promedio"].Value = est.Promedio;
                command.Parameters["@Activo"].Value = est.Activo;

                await command.ExecuteNonQueryAsync();
            }

            transaction.Commit();
            Console.WriteLine($"✓ {estudiantes.Count} registros insertados con transacción");
        }
        catch
        {
            transaction.Rollback();
            throw;
        }
    }

    // Opción 3: Table-Valued Parameter (TVP) - MEJOR OPCIÓN
    public async Task BulkInsertTVPAsync(List<Estudiante> estudiantes)
    {
        // CREATE TYPE EstudianteTableType AS TABLE
        // (
        //     Codigo NVARCHAR(20),
        //     Nombre NVARCHAR(100),
        //     Apellido NVARCHAR(100),
        //     Email NVARCHAR(100),
        //     Promedio DECIMAL(3,2)
        // );

        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        var query = @"
            INSERT INTO Estudiantes (Codigo, Nombre, Apellido, Email, Promedio, Activo)
            SELECT Codigo, Nombre, Apellido, Email, Promedio, 1
            FROM @Estudiantes";

        using var command = new SqlCommand(query, connection);

        // Crear DataTable como parámetro
        var dataTable = ToDataTable(estudiantes);
        var param = command.Parameters.AddWithValue("@Estudiantes", dataTable);
        param.SqlDbType = SqlDbType.Structured;
        param.TypeName = "dbo.EstudianteTableType";

        var rowsAffected = await command.ExecuteNonQueryAsync();
        Console.WriteLine($"✓ {rowsAffected} registros insertados con TVP");
    }

    // Bulk Update
    public async Task BulkUpdateAsync(List<Estudiante> estudiantes)
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        using var transaction = connection.BeginTransaction();

        try
        {
            var query = @"
                UPDATE Estudiantes
                SET Nombre = @Nombre, Apellido = @Apellido, Email = @Email, Promedio = @Promedio
                WHERE Id = @Id";

            using var command = new SqlCommand(query, connection, transaction);

            foreach (var est in estudiantes)
            {
                command.Parameters.Clear();
                command.Parameters.AddWithValue("@Nombre", est.Nombre);
                command.Parameters.AddWithValue("@Apellido", est.Apellido);
                command.Parameters.AddWithValue("@Email", (object)est.Email ?? DBNull.Value);
                command.Parameters.AddWithValue("@Promedio", est.Promedio);
                command.Parameters.AddWithValue("@Id", est.Id);

                await command.ExecuteNonQueryAsync();
            }

            transaction.Commit();
            Console.WriteLine($"✓ {estudiantes.Count} registros actualizados en bulk");
        }
        catch
        {
            transaction.Rollback();
            throw;
        }
    }

    private DataTable ToDataTable(List<Estudiante> estudiantes)
    {
        var dataTable = new DataTable();
        dataTable.Columns.Add("Codigo", typeof(string));
        dataTable.Columns.Add("Nombre", typeof(string));
        dataTable.Columns.Add("Apellido", typeof(string));
        dataTable.Columns.Add("Email", typeof(string));
        dataTable.Columns.Add("Promedio", typeof(decimal));
        dataTable.Columns.Add("FechaNacimiento", typeof(DateTime));
        dataTable.Columns.Add("Activo", typeof(bool));

        foreach (var est in estudiantes)
        {
            dataTable.Rows.Add(
                est.Codigo,
                est.Nombre,
                est.Apellido,
                est.Email,
                est.Promedio,
                est.FechaNacimiento,
                est.Activo
            );
        }

        return dataTable;
    }
}
```

---

## Advanced Queries

### Consultas complejas y optimizadas

```csharp
public class EstudianteRepositoryAdvanced
{
    // JOIN con múltiples tablas
    public async Task<List<EstudianteConCarrera>> ObtenerConCarreraAsync()
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        var query = @"
            SELECT
                e.Id, e.Codigo, e.Nombre, e.Apellido, e.Email, e.Promedio,
                c.Id as CarreraId, c.Nombre as CarreraNombre, c.Codigo as CarreraCodigo
            FROM Estudiantes e
            INNER JOIN Carreras c ON e.CarreraId = c.Id
            WHERE e.Activo = 1
            ORDER BY c.Nombre, e.Apellido, e.Nombre";

        using var command = new SqlCommand(query, connection);
        using var reader = await command.ExecuteReaderAsync();

        var resultados = new List<EstudianteConCarrera>();

        while (await reader.ReadAsync())
        {
            resultados.Add(new EstudianteConCarrera
            {
                Id = reader.GetInt32(0),
                Codigo = reader.GetString(1),
                Nombre = reader.GetString(2),
                Apellido = reader.GetString(3),
                Email = reader.IsDBNull(4) ? null : reader.GetString(4),
                Promedio = reader.GetDecimal(5),
                Carrera = new Carrera
                {
                    Id = reader.GetInt32(6),
                    Nombre = reader.GetString(7),
                    Codigo = reader.GetString(8)
                }
            });
        }

        return resultados;
    }

    // Agregación con GROUP BY
    public async Task<List<EstadisticaPorCarrera>> ObtenerEstadisticasPorCarreraAsync()
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        var query = @"
            SELECT
                c.Id,
                c.Nombre as CarreraNombre,
                COUNT(e.Id) as TotalEstudiantes,
                AVG(e.Promedio) as PromedioPromedio,
                MAX(e.Promedio) as PromedioMaximo,
                MIN(e.Promedio) as PromedioMinimo
            FROM Carreras c
            LEFT JOIN Estudiantes e ON c.Id = e.CarreraId AND e.Activo = 1
            GROUP BY c.Id, c.Nombre
            ORDER BY PromedioPromedio DESC";

        using var command = new SqlCommand(query, connection);
        using var reader = await command.ExecuteReaderAsync();

        var estadisticas = new List<EstadisticaPorCarrera>();

        while (await reader.ReadAsync())
        {
            estadisticas.Add(new EstadisticaPorCarrera
            {
                CarreraId = reader.GetInt32(0),
                CarreraNombre = reader.GetString(1),
                TotalEstudiantes = reader.GetInt32(2),
                PromedioPromedio = reader.IsDBNull(3) ? 0 : reader.GetDecimal(3),
                PromedioMaximo = reader.IsDBNull(4) ? 0 : reader.GetDecimal(4),
                PromedioMinimo = reader.IsDBNull(5) ? 0 : reader.GetDecimal(5)
            });
        }

        return estadisticas;
    }

    // CTE (Common Table Expression) para jerarquías
    public async Task<List<Estudiante>> ObtenerMejoresPorCarreraAsync(int topN)
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        // CTE para obtener los N mejores por carrera
        var query = @"
            WITH MejoresEstudiantes AS (
                SELECT
                    e.Id, e.Codigo, e.Nombre, e.Apellido, e.Promedio, e.CarreraId,
                    c.Nombre as CarreraNombre,
                    ROW_NUMBER() OVER (PARTITION BY e.CarreraId ORDER BY e.Promedio DESC) as Ranking
                FROM Estudiantes e
                INNER JOIN Carreras c ON e.CarreraId = c.Id
                WHERE e.Activo = 1
            )
            SELECT Id, Codigo, Nombre, Apellido, Promedio, CarreraId, CarreraNombre
            FROM MejoresEstudiantes
            WHERE Ranking <= @TopN
            ORDER BY CarreraNombre, Promedio DESC";

        using var command = new SqlCommand(query, connection);
        command.Parameters.AddWithValue("@TopN", topN);

        using var reader = await command.ExecuteReaderAsync();
        var estudiantes = new List<Estudiante>();

        while (await reader.ReadAsync())
        {
            estudiantes.Add(new Estudiante
            {
                Id = reader.GetInt32(0),
                Codigo = reader.GetString(1),
                Nombre = reader.GetString(2),
                Apellido = reader.GetString(3),
                Promedio = reader.GetDecimal(4)
            });
        }

        return estudiantes;
    }

    // Subquery y EXISTS
    public async Task<List<Estudiante>> ObtenerSinMateriasAsync()
    {
        using var connection = new SqlConnection(_connectionString);
        await connection.OpenAsync();

        var query = @"
            SELECT e.Id, e.Codigo, e.Nombre, e.Apellido, e.Email
            FROM Estudiantes e
            WHERE e.Activo = 1
            AND NOT EXISTS (
                SELECT 1 FROM EstudianteMaterias em
                WHERE em.EstudianteId = e.Id
            )
            ORDER BY e.Apellido, e.Nombre";

        using var command = new SqlCommand(query, connection);
        using var reader = await command.ExecuteReaderAsync();

        var estudiantes = new List<Estudiante>();

        while (await reader.ReadAsync())
        {
            estudiantes.Add(MapFromReader(reader));
        }

        return estudiantes;
    }
}

// Clases de soporte
public class EstudianteConCarrera : Estudiante
{
    public Carrera Carrera { get; set; }
}

public class EstadisticaPorCarrera
{
    public int CarreraId { get; set; }
    public string CarreraNombre { get; set; }
    public int TotalEstudiantes { get; set; }
    public decimal PromedioPromedio { get; set; }
    public decimal PromedioMaximo { get; set; }
    public decimal PromedioMinimo { get; set; }
}
```

---

## Validations Layer

### Capa de validación antes de persistencia

```csharp
using System.ComponentModel.DataAnnotations;

public class EstudianteValidator
{
    public (bool IsValid, List<string> Errors) Validate(Estudiante estudiante)
    {
        var errors = new List<string>();

        // Validaciones de código
        if (string.IsNullOrWhiteSpace(estudiante.Codigo))
            errors.Add("El código es obligatorio");
        else if (estudiante.Codigo.Length < 3 || estudiante.Codigo.Length > 20)
            errors.Add("El código debe tener entre 3 y 20 caracteres");
        else if (!estudiante.Codigo.StartsWith("EST"))
            errors.Add("El código debe comenzar con 'EST'");

        // Validaciones de nombre
        if (string.IsNullOrWhiteSpace(estudiante.Nombre))
            errors.Add("El nombre es obligatorio");
        else if (estudiante.Nombre.Length < 2 || estudiante.Nombre.Length > 100)
            errors.Add("El nombre debe tener entre 2 y 100 caracteres");

        // Validaciones de apellido
        if (string.IsNullOrWhiteSpace(estudiante.Apellido))
            errors.Add("El apellido es obligatorio");

        // Validaciones de email
        if (!string.IsNullOrEmpty(estudiante.Email))
        {
            var emailAttribute = new EmailAddressAttribute();
            if (!emailAttribute.IsValid(estudiante.Email))
                errors.Add("El formato del email no es válido");
        }

        // Validaciones de promedio
        if (estudiante.Promedio < 0 || estudiante.Promedio > 5)
            errors.Add("El promedio debe estar entre 0 y 5");

        // Validaciones de fecha
        if (estudiante.FechaNacimiento > DateTime.Now.AddYears(-15))
            errors.Add("El estudiante debe tener al menos 15 años");
        if (estudiante.FechaNacimiento < DateTime.Now.AddYears(-100))
            errors.Add("Fecha de nacimiento inválida");

        return (errors.Count == 0, errors);
    }

    // Validación asíncrona contra base de datos
    public async Task<(bool IsValid, List<string> Errors)> ValidateUniqueAsync(
        Estudiante estudiante, EstudianteRepository repository)
    {
        var (isValid, errors) = Validate(estudiante);

        if (!isValid)
            return (false, errors);

        // Verificar código único
        var existente = await repository.ObtenerPorCodigoAsync(estudiante.Codigo);
        if (existente != null && existente.Id != estudiante.Id)
            errors.Add($"Ya existe un estudiante con código {estudiante.Codigo}");

        // Verificar email único
        if (!string.IsNullOrEmpty(estudiante.Email))
        {
            var existenteEmail = await repository.ObtenerPorEmailAsync(estudiante.Email);
            if (existenteEmail != null && existenteEmail.Id != estudiante.Id)
                errors.Add($"El email {estudiante.Email} ya está registrado");
        }

        return (errors.Count == 0, errors);
    }
}

// Uso en el repository
public class EstudianteRepositoryValidated
{
    private readonly EstudianteValidator _validator;

    public async Task<int> CrearValidadoAsync(Estudiante estudiante)
    {
        // Validar antes de insertar
        var (isValid, errors) = await _validator.ValidateUniqueAsync(
            estudiante, this);

        if (!isValid)
        {
            throw new ValidationException(
                $"Validación fallida: {string.Join(", ", errors)}");
        }

        return await CrearAsync(estudiante);
    }
}
```

---

---
