---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 5'
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

# Proyecto Final: Integración

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 75 minutos

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, el estudiante será capaz de:

1. **Integrar** todas las tecnologías del curso en un proyecto final
2. **Aplicar** buenas prácticas de arquitectura de software (capas, patrones)
3. **Documentar** y presentar un proyecto completo
4. **Implementar** patrones de diseño profesionales

---

## 💻 Actividad Final: Proyecto Integrador

### Descripción del Proyecto

Desarrollar un **Sistema de Gestión Académica** que integre todos los conceptos del curso:

#### Tecnologías Obligatorias
- ✅ C# con POO avanzada
- ✅ Windows Forms / WPF
- ✅ ADO.NET con SQL Server
- ✅ Dataset y DataAdapter
- ✅ Data Binding
- ✅ Persistencia en XML (exportación)
- ✅ TDD (pruebas unitarias con xUnit/NUnit)

---

### Funcionalidades Mínimas

#### Módulo 1: Gestión de Estudiantes
- [x] CRUD completo (Create, Read, Update, Delete)
- [x] Validación de datos
- [x] Búsqueda y filtros
- [x] Exportar a XML

#### Módulo 2: Gestión de Cursos
- [x] CRUD de cursos
- [x] Asignación de estudiantes a cursos
- [x] Capacidad máxima por curso

#### Módulo 3: Gestión de Notas
- [x] Registrar calificaciones
- [x] Calcular promedios automáticamente
- [x] Generar reportes (top 10, estudiantes en riesgo)

#### Módulo 4: Reportes
- [x] Reporte de estudiantes por curso
- [x] Historial académico de estudiante
- [x] Estadísticas generales

---

### Entregables

| Entregable | Descripción | Peso |
|------------|-------------|------|
| **Código Fuente** | Proyecto completo en GitHub | 40% |
| **Base de Datos** | Script SQL con esquema y datos | 10% |
| **Pruebas Unitarias** | Cobertura >70% | 15% |
| **Documentación Técnica** | README, diagramas UML | 15% |
| **Presentación** | Demo de 15 min | 10% |
| **Video** | Screencast explicando arquitectura | 10% |

---

### Estructura del Proyecto

```
SistemaAcademico/
├── src/
│   ├── SistemaAcademico.Core/          # Lógica de negocio
│   │   ├── Entities/
│   │   │   ├── Estudiante.cs
│   │   │   ├── Curso.cs
│   │   │   └── Nota.cs
│   │   ├── Interfaces/
│   │   │   └── IEstudianteRepository.cs
│   │   └── Services/
│   │       └── EstudianteService.cs
│   │
│   ├── SistemaAcademico.Data/          # Acceso a datos
│   │   ├── Repositories/
│   │   │   └── EstudianteRepository.cs
│   │   └── AppDbContext.cs
│   │
│   ├── SistemaAcademico.UI/            # Interfaz gráfica
│   │   ├── Forms/
│   │   │   ├── frmEstudiantes.cs
│   │   │   └── frmCursos.cs
│   │   └── Program.cs
│   │
│   └── SistemaAcademico.Tests/         # Pruebas unitarias
│       └── EstudianteServiceTests.cs
│
├── database/
│   └── create_schema.sql
│
├── docs/
│   ├── README.md
│   ├── arquitectura.md
│   └── manual_usuario.pdf
│
└── SistemaAcademico.sln
```

---

### Cronograma de Desarrollo

| Semana | Actividades |
|--------|-------------|
| **1-2** | Diseño de BD, modelos de entidades, interfaces |
| **3-4** | Implementación de repositorios y servicios |
| **5-6** | Desarrollo de interfaz gráfica (Windows Forms) |
| **7** | Pruebas unitarias y corrección de bugs |
| **8** | Documentación, video y preparación de presentación |

---

### Rúbrica de Evaluación Detallada

#### Arquitectura y Diseño (25 puntos)
- Separación de capas (Presentation, Business, Data) - 10 pts
- Uso de interfaces y abstracciones - 8 pts
- Patrones de diseño aplicados (Repository, Singleton, etc.) - 7 pts

#### Funcionalidad (30 puntos)
- CRUD completo funcional - 15 pts
- Validaciones robustas - 8 pts
- Manejo de errores - 7 pts

#### Calidad de Código (20 puntos)
- Código limpio y legible - 8 pts
- Naming conventions - 5 pts
- Comentarios y documentación inline - 7 pts

#### Pruebas (15 puntos)
- Cobertura >70% - 10 pts
- Tests bien diseñados (AAA pattern) - 5 pts

#### Presentación (10 puntos)
- Claridad en la explicación - 5 pts
- Dominio del tema - 5 pts

---

## Patrones de Diseño para el Proyecto Final

### Repository Pattern

```csharp
// Abstrae el acceso a datos
public interface IEstudianteRepository
{
    Estudiante ObtenerPorId(int id);
    IEnumerable<Estudiante> ObtenerTodos();
    void Agregar(Estudiante estudiante);
    void Actualizar(Estudiante estudiante);
    void Eliminar(int id);
}

public class EstudianteRepository : IEstudianteRepository
{
    private readonly string _connectionString;

    public EstudianteRepository(string connectionString)
    {
        _connectionString = connectionString;
    }

    public Estudiante ObtenerPorId(int id)
    {
        using var conn = new SqlConnection(_connectionString);
        using var cmd = new SqlCommand("SELECT * FROM Estudiantes WHERE Id = @Id", conn);
        cmd.Parameters.AddWithValue("@Id", id);
        conn.Open();

        using var reader = cmd.ExecuteReader();
        if (reader.Read())
        {
            return new Estudiante
            {
                Id = reader.GetInt32(0),
                Nombre = reader.GetString(1),
                // ... mapear resto de campos
            };
        }
        return null;
    }

    // ... otros métodos
}
```

---

### Service Layer Pattern

```csharp
// Lógica de negocio separada del acceso a datos
public interface IEstudianteService
{
    Estudiante RegistrarEstudiante(NuevoEstudianteDto dto);
    void ActualizarPromedio(int estudianteId);
    IReadOnlyList<Estudiante> ObtenerEstudiantesDestacados();
}

public class EstudianteService : IEstudianteService
{
    private readonly IEstudianteRepository _repository;
    private readonly IUnitOfWork _unitOfWork;

    public EstudianteRegistrar(NuevoEstudianteDto dto)
    {
        // Validaciones de negocio
        if (_repository.ObtenerPorCodigo(dto.Codigo) != null)
            throw new Exception("Código ya existe");

        var estudiante = new Estudiante
        {
            Codigo = dto.Codigo,
            Nombre = dto.Nombre,
            Promedio = 0
        };

        _repository.Agregar(estudiante);
        _unitOfWork.Commit();

        return estudiante;
    }

    // ... otros métodos
}
```

---

### Unit of Work Pattern

```csharp
// Agrupa múltiples repositorios en una sola transacción
public interface IUnitOfWork : IDisposable
{
    IEstudianteRepository Estudiantes { get; }
    ICursoRepository Cursos { get; }
    INotaRepository Notas { get; }
    void Commit();
    void Rollback();
}

public class SqlUnitOfWork : IUnitOfWork
{
    private readonly SqlTransaction _transaction;
    private readonly SqlConnection _connection;

    public IEstudianteRepository Estudiantes { get; }
    public ICursoRepository Cursos { get; }
    public INotaRepository Notas { get; }

    public void Commit()
    {
        try
        {
            _transaction.Commit();
        }
        catch
        {
            _transaction.Rollback();
            throw;
        }
    }

    public void Dispose()
    {
        _transaction?.Dispose();
        _connection?.Dispose();
    }
}
```

---

## DataGridView Avanzado - Personalización Completa

### Configuración profesional del grid

```csharp
private void ConfigurarGrid()
{
    dgv = new DataGridView
    {
        Dock = DockStyle.Fill,
        AutoGenerateColumns = false,
        AllowUserToAddRows = false,
        SelectionMode = DataGridViewSelectionMode.FullRowSelect,
        MultiSelect = false,
        BackgroundColor = Color.White,
        AlternatingRowsDefaultCellStyle = new DataGridViewCellStyle
        {
            BackColor = Color.AliceBlue
        },
        ColumnHeadersDefaultCellStyle = new DataGridViewCellStyle
        {
            BackColor = Color.Navy,
            ForeColor = Color.White,
            Font = new Font("Segoe UI", 10F, FontStyle.Bold)
        }
    };

    // Configurar columnas manualmente
    var colCodigo = new DataGridViewTextBoxColumn
    {
        Name = "Codigo",
        HeaderText = "Código",
        DataPropertyName = "Codigo",
        Width = 100
    };

    var colNombre = new DataGridViewTextBoxColumn
    {
        Name = "Nombre",
        HeaderText = "Nombre Completo",
        DataPropertyName = "Nombre",
        Width = 200
    };

    var colPromedio = new DataGridViewTextBoxColumn
    {
        Name = "Promedio",
        HeaderText = "Promedio",
        DataPropertyName = "Promedio",
        Width = 100,
        DefaultCellStyle = new DataGridViewCellStyle
        {
            Format = "F2",
            Alignment = DataGridViewContentAlignment.MiddleRight
        }
    };

    dgv.Columns.AddRange(colCodigo, colNombre, colPromedio);
}
```

---

## XML Serialization Avanzada

### Atributos de serialización personalizados

```csharp
using System.Xml.Serialization;

[XmlRoot("Universidad", Namespace = "http://www.unaula.edu.co/esquema")]
public class Universidad
{
    [XmlElement("Estudiante")]
    public List<Estudiante> Estudiantes { get; set; } = new List<Estudiante>();

    [XmlAttribute("Nombre")]
    public string NombreInstitucion { get; set; }
}

public class Estudiante
{
    [XmlAttribute("Id")]
    public int Id { get; set; }

    [XmlAttribute("Codigo")]
    public string Codigo { get; set; }

    [XmlElement("NombreCompleto")]
    public string Nombre { get; set; }

    [XmlIgnore]  // No serializar
    public string Password { get; set; }

    [XmlArray("Notas")]
    [XmlArrayItem("Nota")]
    public List<decimal> Calificaciones { get; set; } = new List<decimal>();
}
```

---

## Logging y Auditoría

### Sistema de logs para el proyecto

```csharp
public class Logger
{
    private static readonly Lazy<Logger> _instance =
        new Lazy<Logger>(() => new Logger());

    public static Logger Instance => _instance.Value;

    private readonly string _logPath;
    private readonly object _lock = new object();

    private Logger()
    {
        var appData = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
        var logDir = Path.Combine(appData, "UniversidadApp", "Logs");
        Directory.CreateDirectory(logDir);

        _logPath = Path.Combine(logDir, $"app_{DateTime.Now:yyyyMMdd}.log");
    }

    public void Info(string mensaje)
    {
        EscribirLog("INFO", mensaje);
    }

    public void Error(string mensaje, Exception ex = null)
    {
        var mensajeCompleto = ex != null
            ? $"{mensaje}: {ex.Message}\n{ex.StackTrace}"
            : mensaje;

        EscribirLog("ERROR", mensajeCompleto);
    }

    public void Auditoria(string usuario, string accion, string detalles)
    {
        var mensaje = $"[{usuario}] {accion}: {detalles}";
        EscribirLog("AUDIT", mensaje);
    }

    private void EscribirLog(string nivel, string mensaje)
    {
        lock (_lock)
        {
            var entrada = $"[{DateTime.Now:yyyy-MM-dd HH:mm:ss.fff}] [{nivel}] {mensaje}";
            File.AppendAllText(_logPath, entrada + Environment.NewLine);
        }
    }
}
```

---

## 🎯 Resumen del Semestre

**Lo que aprendimos:**

**Unidad 1 - POO en C#:**
- ✅ Clases, objetos, encapsulamiento
- ✅ Herencia y polimorfismo
- ✅ Interfaces y clases abstractas

**Unidad 2 - Técnicas de Desarrollo:**
- ✅ TDD con pruebas unitarias
- ✅ BDD para comportamiento
- ✅ DDD para dominio de negocio

**Unidad 3 - Desarrollo Web:**
- ✅ ASP.NET Core MVC
- ✅ HTML5 y Bootstrap
- ✅ Formularios y validación

**Unidad 4 - Persistencia:**
- ✅ ADO.NET conectado (SqlDataReader)
- ✅ CRUD completo
- ✅ Transacciones
- ✅ Archivos planos (JSON, XML, CSV)

**Unidad 5 - Datos Desconectados:**
- ✅ DataSet y DataTable
- ✅ DataAdapter
- ✅ DataBinding
- ✅ Exportación a XML

---

## 💬 Palabras Finales

¡Felicitaciones por completar POO II! 🎉

Han desarrollado habilidades fundamentales para cualquier desarrollador .NET:
- Programación orientada a objetos profesional
- Testing como práctica estándar
- Desarrollo web moderno
- Persistencia de datos robusta

**Próximos pasos sugeridos:**
1. Profundizar en Entity Framework (ORM moderno)
2. Aprender LINQ avanzado
3. APIs REST con Web API
4. Arquitecturas limpias (Clean Architecture)
5. Patrones de diseño

¡Éxitos en sus proyectos futuros! 🚀

---

## 📚 Recursos para el Proyecto Final

**Plantillas de código:**
- [Repositorio GitHub del curso](https://github.com/...)
- Ejemplos de cada unidad

**Herramientas recomendadas:**
- Visual Studio 2022 Community
- SQL Server Express
- Postman (si hacen API)
- Git para control de versiones

**Documentación:**
- [ASP.NET Core MVC](https://docs.microsoft.com/en-us/aspnet/core/mvc/)
- [ADO.NET Best Practices](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/ado-net-code-examples)
- [xUnit Testing](https://xunit.net/docs/getting-started)

**¡Tiempo Total Estimado: 80 horas!**

---

<!-- _class: lead -->

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
