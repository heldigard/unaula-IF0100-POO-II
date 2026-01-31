---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 4'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 12: Introducción a ADO.NET
## Acceso a datos con SQL Server

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Comprender** la arquitectura de ADO.NET
2. **Configurar** la cadena de conexión a SQL Server
3. **Implementar** operaciones CRUD con ADO.NET
4. **Utilizar** SqlConnection, SqlCommand y SqlDataReader
5. **Aplicar** buenas prácticas de manejo de conexiones

**Duración:** 90 minutos

---

## Agenda

1. ¿Qué es ADO.NET? (10 min)
2. Arquitectura y componentes (15 min)
3. Conexión a SQL Server (15 min)
4. Operaciones CRUD (25 min)
5. Manejo de transacciones (15 min)
6. Buenas prácticas (10 min)

---

## 1. ¿Qué es ADO.NET?

### Acceso a datos en .NET

```
┌─────────────────────────────────────────────────────────────┐
│                     ADO.NET                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  > Conjunto de clases que permite a las aplicaciones .NET   │
│    acceder a fuentes de datos (SQL Server, Oracle, MySQL,   │
│    PostgreSQL, SQLite, archivos XML, etc.)                  │
│                                                             │
│  CARACTERÍSTICAS:                                           │
│                                                             │
│  📊 Conectado vs Desconectado                              │
│     • DataReader: modo conectado (streaming)               │
│     • DataSet: modo desconectado (en memoria)              │
│                                                             │
│  🔧 Proveedores de datos (Data Providers)                  │
│     • SqlClient: SQL Server                                │
│     • OracleClient: Oracle                                 │
│     • MySql.Data: MySQL                                    │
│     • Npgsql: PostgreSQL                                   │
│                                                             │
│  ⚡ Alto rendimiento                                        │
│     • Acceso directo a la base de datos                    │
│     • Sin capas de abstracción pesadas                     │
│                                                             │
│  🔄 Base de Entity Framework                               │
│     • EF Core usa ADO.NET internamente                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ADO.NET vs Entity Framework

### ¿Cuándo usar cada uno?

```
┌─────────────────────────────────────────────────────────────┐
│              ADO.NET vs ENTITY FRAMEWORK                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ADO.NET (Bajo nivel)                  EF Core (Alto nivel)│
│   ─────────────────────                 ─────────────────── │
│                                                             │
│   ✅ Usar cuando:                       ✅ Usar cuando:     │
│                                                             │
│   • Queries complejas                   • CRUD estándar    │
│   • Stored procedures                   • Mapeo O/R simple │
│   • Control total del SQL               • Productividad    │
│   • Alto rendimiento crítico            • Migrations       │
│   • Batch operations                    • LINQ queries     │
│                                                             │
│   VENTAJAS:                             VENTAJAS:          │
│   • Máximo control                      • Menos código     │
│   • Máximo rendimiento                  • Más mantenible   │
│   • Flexibilidad SQL                    • Strong typing    │
│                                                             │
│   DESVENTAJAS:                          DESVENTAJAS:       │
│   • Más código                          • Menos control    │
│   • Más propenso a errores              • Overhead         │
│   • Mantenimiento difícil               • Queries complejas│
│                                                             │
│   EN ESTE CURSO: Ambos (ADO.NET primero, luego EF)         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Arquitectura ADO.NET

### Componentes principales

```
┌─────────────────────────────────────────────────────────────┐
│              ARQUITECTURA ADO.NET                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   APLICACIÓN .NET                                           │
│        │                                                    │
│        ▼                                                    │
│   ┌─────────────────────────────────────────────────────┐   │
│   │           PROVEEDOR DE DATOS                        │   │
│   │          (System.Data.SqlClient)                    │   │
│   │                                                     │   │
│   │  ┌──────────────┐  ┌──────────────┐               │   │
│   │  │ SqlConnection│  │ SqlCommand   │               │   │
│   │  │              │  │              │               │   │
│   │  │ • Abrir      │  │ • Execute    │               │   │
│   │  │ • Cerrar     │  │ • Parameters │               │   │
│   │  │ • Connection │  │ • CommandType│               │   │
│   │  │   String     │  │              │               │   │
│   │  └──────┬───────┘  └──────┬───────┘               │   │
│   │         │                  │                       │   │
│   │         └────────┬─────────┘                       │   │
│   │                  ▼                                 │   │
│   │  ┌─────────────────────────────────────────────┐   │   │
│   │  │              SQL SERVER                      │   │   │
│   │  └─────────────────────────────────────────────┘   │   │
│   │                                                     │   │
│   └─────────────────────────────────────────────────────┘   │
│                            │                                │
│                            ▼                                │
│   ┌─────────────────────────────────────────────────────┐   │
│   │           OBJETOS DE DATOS                          │   │
│   │                                                     │   │
│   │  ┌──────────────┐  ┌──────────────┐               │   │
│   │  │SqlDataReader │  │  DataSet     │               │   │
│   │  │              │  │              │               │   │
│   │  │ • Read()     │  │ • Tables     │               │   │
│   │  │ • GetString()│  │ • Relations  │               │   │
│   │  │ • GetInt32() │  │ • Fill()     │               │   │
│   │  │ (forward-only)│  │ (disconnected)│              │   │
│   │  └──────────────┘  └──────────────┘               │   │
│   │                                                     │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Namespaces y Paquetes

### Instalación

```bash
# Instalar paquete NuGet (ya incluido en ASP.NET Core)
dotnet add package System.Data.SqlClient

# O para SQL Server (recomendado)
dotnet add package Microsoft.Data.SqlClient
```

```csharp
// Namespaces necesarios
using System.Data;           // Tipos genéricos: DataTable, DataSet
using System.Data.SqlClient; // Proveedor SQL Server específico

// O el nuevo paquete (más actualizado)
using Microsoft.Data.SqlClient;
```

---

## 3. Conexión a SQL Server

### Connection String

```csharp
// Program.cs - Configuración

// Opción 1: En appsettings.json (RECOMENDADO)
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=UniversidadDB;Trusted_Connection=True;MultipleActiveResultSets=true",
    "Produccion": "Server=mi-servidor.database.windows.net;Database=UniversidadDB;User Id=usuario;Password=password;"
  }
}

// Leer en Program.cs
var connectionString = builder.Configuration
    .GetConnectionString("DefaultConnection");

builder.Services.AddSingleton(connectionString);

// ─────────────────────────────────────────────────────────────

// Opción 2: Connection String Builder (más seguro)
var builder = new SqlConnectionStringBuilder
{
    DataSource = @"(localdb)\mssqllocaldb",
    InitialCatalog = "UniversidadDB",
    IntegratedSecurity = true,
    MultipleActiveResultSets = true,
    ConnectTimeout = 30
};

string connectionString = builder.ConnectionString;
```

---

## Usando SqlConnection

### Patrón using (siempre)

```csharp
public class EstudianteRepository
{
    private readonly string _connectionString;

    public EstudianteRepository(string connectionString)
    {
        _connectionString = connectionString;
    }

    public List<Estudiante> ObtenerTodos()
    {
        var estudiantes = new List<Estudiante>();
        
        // SIEMPRE usar 'using' para garantizar cierre de conexión
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            
            var query = "SELECT Id, Codigo, Nombre, Email FROM Estudiantes";
            
            using (var command = new SqlCommand(query, connection))
            {
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        estudiantes.Add(new Estudiante
                        {
                            Id = reader.GetInt32(0),
                            Codigo = reader.GetString(1),
                            Nombre = reader.GetString(2),
                            Email = reader.IsDBNull(3) ? null : reader.GetString(3)
                        });
                    }
                }
            }
            
            // La conexión se cierra automáticamente al salir del using
        }
        
        return estudiantes;
    }
}
```

---

## SqlDataReader

### Lectura de datos

```csharp
// Métodos del SqlDataReader

// Por índice (posición)
int id = reader.GetInt32(0);
string nombre = reader.GetString(1);

// Por nombre de columna
string email = reader.GetString(reader.GetOrdinal("Email"));

// Verificar NULL
if (!reader.IsDBNull(3))
{
    email = reader.GetString(3);
}

// Cast genérico (más lento pero flexible)
int id = (int)reader["Id"];
string nombre = reader["Nombre"].ToString();

// Tipos disponibles:
// GetInt32(), GetInt64(), GetString(), GetDateTime()
// GetDecimal(), GetDouble(), GetBoolean(), GetByte()
```

---

## 4. Operaciones CRUD

### Create (INSERT)

```csharp
public async Task<int> CrearAsync(Estudiante estudiante)
{
    using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync();
    
    var query = @"
        INSERT INTO Estudiantes (Codigo, Nombre, Email, FechaRegistro)
        VALUES (@Codigo, @Nombre, @Email, @FechaRegistro);
        SELECT SCOPE_IDENTITY();";  // Retorna el ID generado
    
    using var command = new SqlCommand(query, connection);
    
    // Agregar parámetros (EVITA SQL INJECTION)
    command.Parameters.AddWithValue("@Codigo", estudiante.Codigo);
    command.Parameters.AddWithValue("@Nombre", estudiante.Nombre);
    command.Parameters.AddWithValue("@Email", 
        (object)estudiante.Email ?? DBNull.Value);
    command.Parameters.AddWithValue("@FechaRegistro", DateTime.Now);
    
    // ExecuteScalar para retornar un solo valor (el ID)
    var id = Convert.ToInt32(await command.ExecuteScalarAsync());
    
    return id;
}

// Uso
var nuevoId = await repo.CrearAsync(new Estudiante
{
    Codigo = "2024001",
    Nombre = "María López",
    Email = "maria@email.com"
});
```

---

## Read (SELECT)

### Obtener por ID y listado

```csharp
public async Task<Estudiante> ObtenerPorIdAsync(int id)
{
    using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync();
    
    var query = "SELECT Id, Codigo, Nombre, Email FROM Estudiantes WHERE Id = @Id";
    
    using var command = new SqlCommand(query, connection);
    command.Parameters.AddWithValue("@Id", id);
    
    using var reader = await command.ExecuteReaderAsync();
    
    if (await reader.ReadAsync())
    {
        return new Estudiante
        {
            Id = reader.GetInt32(0),
            Codigo = reader.GetString(1),
            Nombre = reader.GetString(2),
            Email = reader.IsDBNull(3) ? null : reader.GetString(3)
        };
    }
    
    return null;  // No encontrado
}

public async Task<List<Estudiante>> ObtenerPorNombreAsync(string busqueda)
{
    var estudiantes = new List<Estudiante>();
    
    using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync();
    
    // LIKE para búsqueda parcial
    var query = @"
        SELECT Id, Codigo, Nombre, Email 
        FROM Estudiantes 
        WHERE Nombre LIKE @Busqueda 
        ORDER BY Nombre";
    
    using var command = new SqlCommand(query, connection);
    command.Parameters.AddWithValue("@Busqueda", $"%{busqueda}%");
    
    using var reader = await command.ExecuteReaderAsync();
    while (await reader.ReadAsync())
    {
        estudiantes.Add(MapFromReader(reader));
    }
    
    return estudiantes;
}

private Estudiante MapFromReader(SqlDataReader reader)
{
    return new Estudiante
    {
        Id = reader.GetInt32(reader.GetOrdinal("Id")),
        Codigo = reader.GetString(reader.GetOrdinal("Codigo")),
        Nombre = reader.GetString(reader.GetOrdinal("Nombre")),
        Email = reader.IsDBNull(reader.GetOrdinal("Email")) 
            ? null 
            : reader.GetString(reader.GetOrdinal("Email"))
    };
}
```

---

## Update (UPDATE)

### Actualizar registro

```csharp
public async Task<bool> ActualizarAsync(Estudiante estudiante)
{
    using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync();
    
    var query = @"
        UPDATE Estudiantes 
        SET Codigo = @Codigo, 
            Nombre = @Nombre, 
            Email = @Email
        WHERE Id = @Id";
    
    using var command = new SqlCommand(query, connection);
    command.Parameters.AddWithValue("@Id", estudiante.Id);
    command.Parameters.AddWithValue("@Codigo", estudiante.Codigo);
    command.Parameters.AddWithValue("@Nombre", estudiante.Nombre);
    command.Parameters.AddWithValue("@Email", 
        (object)estudiante.Email ?? DBNull.Value);
    
    // ExecuteNonQuery retorna número de filas afectadas
    int filasAfectadas = await command.ExecuteNonQueryAsync();
    
    return filasAfectadas > 0;  // True si se actualizó algo
}
```

---

## Delete (DELETE)

### Eliminar registro

```csharp
public async Task<bool> EliminarAsync(int id)
{
    using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync();
    
    var query = "DELETE FROM Estudiantes WHERE Id = @Id";
    
    using var command = new SqlCommand(query, connection);
    command.Parameters.AddWithValue("@Id", id);
    
    int filasAfectadas = await command.ExecuteNonQueryAsync();
    
    return filasAfectadas > 0;
}

// Alternativa: Eliminación lógica (más segura)
public async Task<bool> DesactivarAsync(int id)
{
    using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync();
    
    var query = @"
        UPDATE Estudiantes 
        SET Activo = 0, FechaEliminacion = @Fecha 
        WHERE Id = @Id";
    
    using var command = new SqlCommand(query, connection);
    command.Parameters.AddWithValue("@Id", id);
    command.Parameters.AddWithValue("@Fecha", DateTime.Now);
    
    return await command.ExecuteNonQueryAsync() > 0;
}
```

---

## Métodos Execute

### Diferencias

```
┌─────────────────────────────────────────────────────────────┐
│              MÉTODOS DE EJECUCIÓN                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ExecuteReader()                                            │
│  ────────────────                                           │
│  • Retorna: SqlDataReader                                   │
│  • Uso: SELECT (múltiples filas)                            │
│  • Conexión: Mantiene abierta mientras se lee              │
│  • Ejemplo:                                                 │
│    var reader = command.ExecuteReader();                    │
│    while (reader.Read()) { ... }                           │
│                                                             │
│  ExecuteScalar()                                            │
│  ────────────────                                           │
│  • Retorna: object (primer valor de primera fila)          │
│  • Uso: SELECT COUNT(*), SUM(), MAX(), SCOPE_IDENTITY()     │
│  • Ejemplo:                                                 │
│    var count = (int)command.ExecuteScalar();                │
│                                                             │
│  ExecuteNonQuery()                                          │
│  ──────────────────                                         │
│  • Retorna: int (número de filas afectadas)                │
│  • Uso: INSERT, UPDATE, DELETE, CREATE TABLE               │
│  • Ejemplo:                                                 │
│    int rows = command.ExecuteNonQuery();                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Manejo de Transacciones

### Consistencia de datos

```csharp
public async Task<bool> TransferirEstudianteAsync(
    int estudianteId, int carreraOrigenId, int carreraDestinoId)
{
    using var connection = new SqlConnection(_connectionString);
    await connection.OpenAsync();
    
    // Iniciar transacción
    using var transaction = connection.BeginTransaction();
    
    try
    {
        // 1. Registrar historial de transferencia
        var query1 = @"INSERT INTO HistorialTransferencias 
                       (EstudianteId, CarreraOrigenId, CarreraDestinoId, Fecha)
                       VALUES (@EstId, @OrigId, @DestId, @Fecha)";
        
        using (var cmd1 = new SqlCommand(query1, connection, transaction))
        {
            cmd1.Parameters.AddWithValue("@EstId", estudianteId);
            cmd1.Parameters.AddWithValue("@OrigId", carreraOrigenId);
            cmd1.Parameters.AddWithValue("@DestId", carreraDestinoId);
            cmd1.Parameters.AddWithValue("@Fecha", DateTime.Now);
            await cmd1.ExecuteNonQueryAsync();
        }
        
        // 2. Actualizar carrera del estudiante
        var query2 = @"UPDATE Estudiantes 
                       SET CarreraId = @CarreraId 
                       WHERE Id = @Id";
        
        using (var cmd2 = new SqlCommand(query2, connection, transaction))
        {
            cmd2.Parameters.AddWithValue("@CarreraId", carreraDestinoId);
            cmd2.Parameters.AddWithValue("@Id", estudianteId);
            await cmd2.ExecuteNonQueryAsync();
        }
        
        // Si todo va bien, confirmar transacción
        transaction.Commit();
        return true;
    }
    catch (Exception ex)
    {
        // Si hay error, deshacer todo
        transaction.Rollback();
        _logger.LogError(ex, "Error en transferencia");
        return false;
    }
}
```

---

## 6. Buenas Prácticas

### Checklist ADO.NET

```
┌─────────────────────────────────────────────────────────────┐
│              BUENAS PRÁCTICAS ADO.NET                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✅ SIEMPRE USAR USING                                      │
│     • SqlConnection, SqlCommand, SqlDataReader              │
│     • Garantiza liberación de recursos                     │
│                                                             │
│  ✅ SIEMPRE USAR PARÁMETROS                                │
│     • NUNCA concatenar strings para SQL                    │
│     • Protege contra SQL Injection                         │
│                                                             │
│     ❌ MAL:                                                │
│     var sql = $"SELECT * FROM Users WHERE Id = {id}";     │
│                                                             │
│     ✅ BIEN:                                               │
│     command.Parameters.AddWithValue("@Id", id);             │
│                                                             │
│  ✅ CERRAR CONEXIONES RÁPIDO                               │
│     • Abrir justo antes de usar                            │
│     • Cerrar inmediatamente después                        │
│     • NO mantener conexiones abiertas                      │
│                                                             │
│  ✅ USAR ASYNC/AWAIT                                       │
│     • ExecuteReaderAsync(), ExecuteNonQueryAsync()         │
│     • Mejor rendimiento en aplicaciones web                │
│                                                             │
│  ✅ MANEJAR NULLS                                          │
│     • Usar DBNull.Value para valores nulos                 │
│     • Verificar IsDBNull() al leer                         │
│                                                             │
│  ✅ USAR TRANSACCIONES                                     │
│     • Para operaciones múltiples relacionadas              │
│     • Mantiene consistencia de datos                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## SQL Injection

### El peligro de concatenar strings

```csharp
// ❌ VULNERABLE A SQL INJECTION
public Estudiante BuscarPorCodigo(string codigo)
{
    var query = $"SELECT * FROM Estudiantes WHERE Codigo = '{codigo}'";
    // Si codigo = "'; DROP TABLE Estudiantes; --"
    // Query resultante: SELECT * FROM Estudiantes WHERE Codigo = ''; 
    //                    DROP TABLE Estudiantes; --'
    // ¡DESASTRE!
}

// ✅ SEGURO CON PARÁMETROS
public Estudiante BuscarPorCodigo(string codigo)
{
    var query = "SELECT * FROM Estudiantes WHERE Codigo = @Codigo";
    command.Parameters.AddWithValue("@Codigo", codigo);
    // El parámetro se escapa automáticamente
    // Caracteres peligrosos se neutralizan
}
```

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **SqlConnection** | Conexión a base de datos |
| **SqlCommand** | Ejecutar SQL |
| **SqlDataReader** | Leer resultados (forward-only) |
| **ExecuteReader** | Para SELECT |
| **ExecuteScalar** | Para valor único (COUNT, etc.) |
| **ExecuteNonQuery** | Para INSERT, UPDATE, DELETE |
| **Parameters** | Protección contra SQL Injection |
| **Transaction** | Consistencia en operaciones múltiples |

---

## Ejercicio Práctico

### Implementar Repository

```
EJERCICIO: Repository de Estudiantes

Crear clase EstudianteRepository con métodos:

1. Crear(Estudiante estudiante) : Task<int>
   - Insertar nuevo estudiante
   - Retornar ID generado

2. ObtenerPorId(int id) : Task<Estudiante>
   - Buscar por ID
   - Retornar null si no existe

3. ObtenerTodos() : Task<List<Estudiante>>
   - Lista completa ordenada por nombre

4. Actualizar(Estudiante estudiante) : Task<bool>
   - Actualizar datos
   - Retornar true si se actualizó

5. Eliminar(int id) : Task<bool>
   - Eliminar físicamente

6. BuscarPorNombre(string termino) : Task<List<Estudiante>>
   - Búsqueda parcial con LIKE

REQUISITOS:
- Usar parámetros en todas las queries
- Usar async/await
- Usar transacción en método CrearConMateriasIniciales
```

---

## Próxima Clase

### Clase 13: Entity Framework Core

```
CONTENIDO PRÓXIMA CLASE:

• Entity Framework Core
  - DbContext y DbSet
  - Code First approach
  - Migrations
  
• LINQ to Entities
  - Consultas LINQ
  - Eager Loading (Include)
  
• Relaciones
  - One-to-Many
  - Many-to-Many
  
• Comparación ADO.NET vs EF Core
```

---

# ¡Gracias!
## ¿Preguntas?

**"ADO.NET: Control total sobre tus datos"**

**UNAULA - Ingeniería Informática - 2026-I**
