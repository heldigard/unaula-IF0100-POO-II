---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 5'
footer: 'UNAULA - Ingeniería Informática - 2026-I'

  section {
    font-size: 24px;
  }

---
<style>
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
}
section {
  font-size: 20px;
  overflow: hidden;
}
section h1 {
  font-size: 1.8em;
}
section h2 {
  font-size: 1.4em;
}
section h3 {
  font-size: 1.2em;
}
section ul, section ol {
  font-size: 0.9em;
  margin-left: 1em;
}
section li {
  margin-bottom: 0.3em;
}
section pre {
  font-size: 0.7em;
  max-height: 60vh;
  overflow-y: auto;
}
section code {
  font-size: 0.85em;
}
section p {
  margin: 0.5em 0;
}
</style>


<!--
IMÁGENES GENERADAS:
- clase-15-dataset.png: Arquitectura desconectada con DataSet y DataAdapter
-->

# Clase 15: Dataset y DataAdapter - Arquitectura Desconectada

**Curso:** IF0100 - Lenguaje de Programación OO II  
**Unidad 5:** Arquitectura de Datos Desconectados  
**Duración:** 90 minutos (Lunes 2h)  
**Fecha:** 2026-05-18

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, el estudiante será capaz de:
1. Comprender el modelo de datos desconectados de ADO.NET
2. Utilizar DataSet como cache de datos en memoria
3. Implementar DataAdapter para sincronizar datos
4. Navegar y manipular datos sin conexión activa
5. Comparar modelo conectado vs desconectado

---

## 📋 Contenido

### 1. Introducción a Datos Desconectados (10 min)

**¿Qué son datos desconectados?**

Datos que se cargan en memoria, se manipulan localmente, y luego se sincronizan con la BD. La conexión solo se usa para:
- ⬇️ Cargar datos (Fill)
- ⬆️ Sincronizar cambios (Update)

**Ventajas:**
- ✅ Menor carga en el servidor de BD
- ✅ Trabaja offline (sin conexión constante)
- ✅ Mejor para aplicaciones distribuidas
- ✅ Múltiples tablas relacionadas en memoria
- ✅ Tracking automático de cambios

**Desventajas:**
- ❌ Mayor uso de memoria cliente
- ❌ Complejidad adicional
- ❌ Posibles conflictos de concurrencia
- ❌ No apto para datos de tiempo real

---

### 2. Componentes Principales (10 min)

```
┌─────────────────────────────────────────┐
│           APLICACIÓN                     │
│                                          │
│  ┌────────────────────────────────┐    │
│  │        DataSet                  │    │
│  │  ┌───────────┐  ┌───────────┐ │    │
│  │  │ DataTable │  │ DataTable │ │    │
│  │  │ (Clientes)│  │ (Pedidos) │ │    │
│  │  └───────────┘  └───────────┘ │    │
│  │                                 │    │
│  │  ┌──────────────────────────┐ │    │
│  │  │   DataRelation           │ │    │
│  │  │   (FK entre tablas)      │ │    │
│  │  └──────────────────────────┘ │    │
│  └────────────────────────────────┘    │
│              ↕                          │
│      ┌───────────────┐                 │
│      │ DataAdapter   │                 │
│      │ (SelectCmd)   │                 │
│      │ (InsertCmd)   │                 │
│      │ (UpdateCmd)   │                 │
│      │ (DeleteCmd)   │                 │
│      └───────────────┘                 │
│              ↕                          │
│      ┌───────────────┐                 │
│      │ Connection    │                 │
│      └───────────────┘                 │
└──────────────│──────────────────────────┘
               ↓
         ┌──────────┐
         │ SQL      │
         │ Server   │
         └──────────┘
```

**Componentes clave:**
- **DataSet:** Contenedor de datos en memoria (mini-BD)
- **DataTable:** Tabla con filas y columnas
- **DataRow:** Fila individual con datos
- **DataColumn:** Definición de columna
- **DataAdapter:** Puente entre DataSet y BD
- **DataRelation:** Relación entre tablas (FK)

---

### 3. DataSet Básico (15 min)

**3.1. Crear DataSet manualmente**

```csharp
using System.Data;

public class EjemploDataSet
{
    public void CrearDataSetManual()
    {
        // 1. Crear DataSet
        DataSet dsUniversidad = new DataSet("Universidad");
        
        // 2. Crear DataTable
        DataTable dtEstudiantes = new DataTable("Estudiantes");
        
        // 3. Definir columnas
        dtEstudiantes.Columns.Add("Id", typeof(int));
        dtEstudiantes.Columns.Add("Nombre", typeof(string));
        dtEstudiantes.Columns.Add("Apellido", typeof(string));
        dtEstudiantes.Columns.Add("Edad", typeof(int));
        dtEstudiantes.Columns.Add("Promedio", typeof(decimal));
        
        // Definir clave primaria
        dtEstudiantes.PrimaryKey = new DataColumn[] { dtEstudiantes.Columns["Id"] };
        
        // 4. Agregar filas
        DataRow fila1 = dtEstudiantes.NewRow();
        fila1["Id"] = 1;
        fila1["Nombre"] = "Juan";
        fila1["Apellido"] = "Pérez";
        fila1["Edad"] = 20;
        fila1["Promedio"] = 4.2m;
        dtEstudiantes.Rows.Add(fila1);
        
        DataRow fila2 = dtEstudiantes.NewRow();
        fila2["Id"] = 2;
        fila2["Nombre"] = "María";
        fila2["Apellido"] = "García";
        fila2["Edad"] = 21;
        fila2["Promedio"] = 4.5m;
        dtEstudiantes.Rows.Add(fila2);
        
        // Método alternativo (más corto)
        dtEstudiantes.Rows.Add(3, "Carlos", "López", 19, 3.8m);
        
        // 5. Agregar tabla al DataSet
        dsUniversidad.Tables.Add(dtEstudiantes);
        
        // 6. Navegar datos
        Console.WriteLine($"DataSet: {dsUniversidad.DataSetName}");
        Console.WriteLine($"Tablas: {dsUniversidad.Tables.Count}");
        Console.WriteLine($"Filas: {dtEstudiantes.Rows.Count}\n");
        
        foreach (DataRow fila in dtEstudiantes.Rows)
        {
            Console.WriteLine($"{fila["Id"]} - {fila["Nombre"]} {fila["Apellido"]} " +
                            $"(Promedio: {fila["Promedio"]})");
        }
    }
}
```

**3.2. Operaciones en DataTable**

```csharp
// Buscar por clave primaria
DataRow filaEncontrada = dtEstudiantes.Rows.Find(2);
if (filaEncontrada != null)
{
    Console.WriteLine($"Encontrado: {filaEncontrada["Nombre"]}");
}

// Filtrar filas
DataRow[] estudiantesDestacados = dtEstudiantes.Select("Promedio >= 4.0");
foreach (DataRow fila in estudiantesDestacados)
{
    Console.WriteLine($"{fila["Nombre"]} - {fila["Promedio"]}");
}

// Ordenar
DataRow[] ordenados = dtEstudiantes.Select("", "Promedio DESC");

// Actualizar
DataRow filaActualizar = dtEstudiantes.Rows.Find(1);
filaActualizar["Promedio"] = 4.7m;

// Eliminar
DataRow filaEliminar = dtEstudiantes.Rows.Find(3);
filaEliminar.Delete();

// Aceptar o rechazar cambios
dtEstudiantes.AcceptChanges(); // Confirma cambios
// dtEstudiantes.RejectChanges(); // Revierte cambios
```

---

### 4. DataAdapter - Puente con la BD (25 min)

**4.1. Cargar datos desde BD (Fill)**

```csharp
using System.Data.SqlClient;

public class EstudianteDataAdapter
{
    private string connectionString = 
        "Server=localhost;Database=Universidad;Trusted_Connection=True;";
    
    public DataSet CargarEstudiantes()
    {
        DataSet ds = new DataSet("Universidad");
        
        string query = "SELECT Id, Nombre, Apellido, Cedula, Email FROM Estudiantes";
        
        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            // Crear DataAdapter
            SqlDataAdapter adapter = new SqlDataAdapter(query, conn);
            
            // Llenar DataSet (abre y cierra conexión automáticamente)
            adapter.Fill(ds, "Estudiantes");
        }
        
        Console.WriteLine($"Filas cargadas: {ds.Tables["Estudiantes"].Rows.Count}");
        return ds;
    }
    
    public DataTable CargarEstudiantesTabla()
    {
        DataTable dt = new DataTable("Estudiantes");
        
        string query = "SELECT * FROM Estudiantes";
        
        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            SqlDataAdapter adapter = new SqlDataAdapter(query, conn);
            adapter.Fill(dt); // Llena directamente el DataTable
        }
        
        return dt;
    }
}
```

**4.2. Sincronizar cambios con BD (Update)**

```csharp
public int GuardarCambios(DataTable dt)
{
    int filasAfectadas = 0;
    
    using (SqlConnection conn = new SqlConnection(connectionString))
    {
        string selectQuery = "SELECT * FROM Estudiantes";
        SqlDataAdapter adapter = new SqlDataAdapter(selectQuery, conn);
        
        // SqlCommandBuilder genera automáticamente INSERT, UPDATE, DELETE
        SqlCommandBuilder builder = new SqlCommandBuilder(adapter);
        
        // Aplicar cambios a la BD
        filasAfectadas = adapter.Update(dt);
    }
    
    Console.WriteLine($"Filas afectadas: {filasAfectadas}");
    return filasAfectadas;
}
```

**Ejemplo completo de uso:**

```csharp
class Program
{
    static void Main()
    {
        var repo = new EstudianteDataAdapter();
        
        // 1. Cargar datos desde BD
        DataTable dt = repo.CargarEstudiantesTabla();
        Console.WriteLine($"Cargados: {dt.Rows.Count} estudiantes\n");
        
        // 2. Modificar datos localmente (sin tocar la BD aún)
        
        // Insertar nuevo estudiante
        DataRow nuevaFila = dt.NewRow();
        nuevaFila["Nombre"] = "Ana";
        nuevaFila["Apellido"] = "Martínez";
        nuevaFila["Cedula"] = "1234567890";
        nuevaFila["Email"] = "ana@unaula.edu.co";
        nuevaFila["FechaNacimiento"] = new DateTime(2001, 3, 10);
        dt.Rows.Add(nuevaFila);
        
        // Actualizar estudiante existente
        DataRow filaActualizar = dt.Rows.Find(1);
        if (filaActualizar != null)
        {
            filaActualizar["Email"] = "nuevo_email@unaula.edu.co";
        }
        
        // Eliminar estudiante
        DataRow filaEliminar = dt.Rows.Find(5);
        if (filaEliminar != null)
        {
            filaEliminar.Delete();
        }
        
        // 3. Sincronizar todos los cambios con la BD
        int afectadas = repo.GuardarCambios(dt);
        Console.WriteLine($"\nTotal cambios guardados: {afectadas}");
        
        // 4. Aceptar cambios en el DataTable
        dt.AcceptChanges();
    }
}
```

**4.3. Comandos personalizados (sin CommandBuilder)**

Para mayor control, podemos definir comandos manualmente:

```csharp
public SqlDataAdapter CrearAdapterConComandos(SqlConnection conn)
{
    string selectQuery = "SELECT Id, Nombre, Apellido, Email FROM Estudiantes";
    SqlDataAdapter adapter = new SqlDataAdapter(selectQuery, conn);
    
    // INSERT personalizado
    adapter.InsertCommand = new SqlCommand(
        "INSERT INTO Estudiantes (Nombre, Apellido, Email) " +
        "VALUES (@Nombre, @Apellido, @Email); SELECT SCOPE_IDENTITY();", conn);
    
    adapter.InsertCommand.Parameters.Add("@Nombre", SqlDbType.NVarChar, 100, "Nombre");
    adapter.InsertCommand.Parameters.Add("@Apellido", SqlDbType.NVarChar, 100, "Apellido");
    adapter.InsertCommand.Parameters.Add("@Email", SqlDbType.NVarChar, 100, "Email");
    
    // UPDATE personalizado
    adapter.UpdateCommand = new SqlCommand(
        "UPDATE Estudiantes SET Nombre = @Nombre, Apellido = @Apellido, " +
        "Email = @Email WHERE Id = @Id", conn);
    
    adapter.UpdateCommand.Parameters.Add("@Id", SqlDbType.Int, 0, "Id");
    adapter.UpdateCommand.Parameters.Add("@Nombre", SqlDbType.NVarChar, 100, "Nombre");
    adapter.UpdateCommand.Parameters.Add("@Apellido", SqlDbType.NVarChar, 100, "Apellido");
    adapter.UpdateCommand.Parameters.Add("@Email", SqlDbType.NVarChar, 100, "Email");
    
    // DELETE personalizado
    adapter.DeleteCommand = new SqlCommand(
        "DELETE FROM Estudiantes WHERE Id = @Id", conn);
    
    adapter.DeleteCommand.Parameters.Add("@Id", SqlDbType.Int, 0, "Id");
    
    return adapter;
}
```

---

### 5. Tracking de Cambios (10 min)

**RowState - Estado de cada fila:**

```csharp
public void MostrarEstadoFilas(DataTable dt)
{
    foreach (DataRow fila in dt.Rows)
    {
        Console.WriteLine($"ID: {fila["Id"]} - Estado: {fila.RowState}");
        
        // Mostrar valor original vs actual (solo si fue modificada)
        if (fila.RowState == DataRowState.Modified)
        {
            Console.WriteLine($"  Original: {fila["Nombre", DataRowVersion.Original]}");
            Console.WriteLine($"  Actual: {fila["Nombre", DataRowVersion.Current]}");
        }
    }
}
```

**Estados posibles:**
- `Unchanged`: Sin cambios desde Fill o AcceptChanges
- `Added`: Nueva fila agregada
- `Modified`: Fila modificada
- `Deleted`: Fila eliminada
- `Detached`: Fila no pertenece a ninguna tabla

**Versiones de datos:**
- `Current`: Valor actual
- `Original`: Valor original desde la BD
- `Proposed`: Valor en edición (BeginEdit/EndEdit)
- `Default`: Valor predeterminado

---

### 6. DataSet con Múltiples Tablas (10 min)

```csharp
public DataSet CargarUniversidadCompleta()
{
    DataSet ds = new DataSet("Universidad");
    
    using (SqlConnection conn = new SqlConnection(connectionString))
    {
        // Tabla Estudiantes
        SqlDataAdapter adapterEst = new SqlDataAdapter(
            "SELECT * FROM Estudiantes", conn);
        adapterEst.Fill(ds, "Estudiantes");
        
        // Tabla Cursos
        SqlDataAdapter adapterCursos = new SqlDataAdapter(
            "SELECT * FROM Cursos", conn);
        adapterCursos.Fill(ds, "Cursos");
        
        // Tabla Matriculas (relación)
        SqlDataAdapter adapterMat = new SqlDataAdapter(
            "SELECT * FROM Matriculas", conn);
        adapterMat.Fill(ds, "Matriculas");
    }
    
    // Definir relaciones
    DataColumn pkEstudiante = ds.Tables["Estudiantes"].Columns["Id"];
    DataColumn fkMatricula = ds.Tables["Matriculas"].Columns["EstudianteId"];
    
    DataRelation relEstudianteMatricula = new DataRelation(
        "Estudiante_Matriculas", pkEstudiante, fkMatricula);
    
    ds.Relations.Add(relEstudianteMatricula);
    
    return ds;
}

// Navegar usando relaciones
public void MostrarMatriculasPorEstudiante(DataSet ds, int estudianteId)
{
    DataRow estudiante = ds.Tables["Estudiantes"].Rows.Find(estudianteId);
    
    if (estudiante != null)
    {
        Console.WriteLine($"Estudiante: {estudiante["Nombre"]} {estudiante["Apellido"]}");
        Console.WriteLine("Matrículas:");
        
        // Obtener filas hijas usando la relación
        DataRow[] matriculas = estudiante.GetChildRows("Estudiante_Matriculas");
        
        foreach (DataRow mat in matriculas)
        {
            Console.WriteLine($"  - Curso ID: {mat["CursoId"]}, Fecha: {mat["FechaMatricula"]}");
        }
    }
}
```

---

### 7. Comparación: Conectado vs Desconectado (5 min)

| Aspecto | Conectado (SqlDataReader) | Desconectado (DataSet) |
|---------|---------------------------|------------------------|
| **Conexión** | Abierta todo el tiempo | Solo para Fill/Update |
| **Memoria** | Bajo consumo | Alto consumo |
| **Navegación** | Solo hacia adelante | Bidireccional, aleatoria |
| **Modificación** | No permite | Permite CRUD local |
| **Relaciones** | No soporta | Soporta DataRelation |
| **Tracking cambios** | No | Sí (RowState) |
| **Concurrencia** | Mejor | Posibles conflictos |
| **Performance lectura** | Más rápido | Más lento (carga todo) |
| **Offline** | No funciona | Funciona |
| **Uso ideal** | Reportes, lectura simple | Edición, app distribuida |

**Cuándo usar cada uno:**
- **Conectado:** Reportes de solo lectura, consultas simples, tiempo real
- **Desconectado:** Aplicaciones de escritorio, edición compleja, trabajo offline

---

## 🛠️ Ejercicio para Casa (En Parejas)

**Sistema de Gestión de Inventario Desconectado**

Crear una aplicación de consola que use DataSet/DataAdapter para gestionar un inventario.

**Tablas:**

```sql
CREATE TABLE Productos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock INT NOT NULL
);

CREATE TABLE Movimientos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    ProductoId INT FOREIGN KEY REFERENCES Productos(Id),
    Tipo NVARCHAR(10) NOT NULL, -- 'Entrada' o 'Salida'
    Cantidad INT NOT NULL,
    Fecha DATETIME DEFAULT GETDATE()
);
```

**Requisitos:**

1. **Cargar datos al iniciar** (Fill de ambas tablas)
2. **Menú interactivo:**
   - Ver todos los productos
   - Agregar nuevo producto
   - Modificar precio/stock
   - Eliminar producto
   - Registrar entrada de mercancía
   - Registrar salida de mercancía
   - Ver historial de movimientos
   - **Guardar cambios** (Update)
   - Salir

3. **Validaciones:**
   - Stock no puede ser negativo
   - Precio debe ser mayor a 0
   - No permitir salida si no hay stock suficiente

4. **Características:**
   - Mostrar estado de cada fila (Added, Modified, Deleted)
   - Opción para deshacer cambios (RejectChanges)
   - Confirmar antes de guardar cambios

5. **Bonus:**
   - Exportar inventario a XML
   - Reporte de productos con bajo stock (< 10)
   - Calcular valor total del inventario

**Entrega:**
- Código fuente completo
- Script SQL para crear tablas
- Video de 5 min demostrando funcionamiento
- **Sustentación en parejas**

---

## 📚 Recursos Adicionales

**Documentación oficial:**
- [DataSet Overview](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/dataset-datatable-dataview/)
- [DataAdapter Overview](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/populating-a-dataset-from-a-dataadapter)
- [DataRelation](https://docs.microsoft.com/en-us/dotnet/api/system.data.datarelation)

---

## 🎯 Resumen

Hoy aprendimos:
- ✅ Arquitectura de datos desconectados
- ✅ DataSet como contenedor en memoria
- ✅ DataAdapter para sincronizar datos
- ✅ Tracking automático de cambios
- ✅ Relaciones entre tablas en memoria
- ✅ Comparación conectado vs desconectado

**Próxima clase:** DataBinding, XML y proyecto integrador final

---

**Fecha:** 2026-05-18 (Lunes)  
**Profesor:** [Nombre]  
**Curso:** IF0100 - POO II
