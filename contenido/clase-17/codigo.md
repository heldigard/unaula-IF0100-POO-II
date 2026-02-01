# Código - Proyecto Final

**IF0100 - Lenguaje de Programación OO II**

---

## Estructura del Proyecto

```
SistemaUniversidad/
├── src/
│   ├── SistemaUniversidad.Web/     # ASP.NET Core
│   ├── SistemaUniversidad.Core/    # Dominio (POO)
│   ├── SistemaUniversidad.Data/    # Repositories (ADO.NET)
│   └── SistemaUniversidad.Tests/   # xUnit Tests
├── docs/
│   ├── diagramas/
│   └── manual-usuario.md
└── scripts/
    └── base-datos.sql
```

---

## 1. Modelo de Dominio (POO)

```csharp
// Entidad base
public abstract class EntidadBase
{
    public int Id { get; protected set; }
}

// Estudiante (Entidad)
public class Estudiante : EntidadBase
{
    public string Codigo { get; set; }
    public string Nombre { get; set; }
    public string Email { get; set; }
    public int Edad { get; set; }

    // Relación 1:N
    public int CarreraId { get; set; }
    public Carrera Carrera { get; set; }

    // Relación N:M (a través de Inscripcion)
    public IReadOnlyCollection<Inscripcion> Inscripciones { get; protected set; }

    public void Inscribir(Materia materia)
    {
        if (_inscripciones.Any(i => i.MateriaId == materia.Id))
            throw new InvalidOperationException("Ya inscrito");

        _inscripciones.Add(new Inscripcion(this, materia));
    }
}

// Carrera (Entidad)
public class Carrera : EntidadBase
{
    public string Nombre { get; set; }
    public int DuracionSemestres { get; set; }

    public IReadOnlyCollection<Estudiante> Estudiantes { get; protected set; }
}

// Materia (Entidad)
public class Materia : EntidadBase
{
    public string Nombre { get; set; }
    public int Creditos { get; set; }
}

// Inscripcion (Entidad - tabla intermedia)
public class Inscripcion : EntidadBase
{
    public int EstudianteId { get; set; }
    public int MateriaId { get; set; }
    public DateTime FechaInscripcion { get; set; }
    public decimal NotaFinal { get; set; }

    public Estudiante Estudiante { get; set; }
    public Materia Materia { get; set; }

    public Inscripcion(Estudiante estudiante, Materia materia)
    {
        Estudiante = estudiante ?? throw new ArgumentNullException(nameof(estudiante));
        Materia = materia ?? throw new ArgumentNullException(nameof(materia));
        FechaInscripcion = DateTime.Now;
    }
}
```

---

## 2. Repository (ADO.NET)

```csharp
public interface IEstudianteRepository
{
    IEnumerable<Estudiante> ObtenerTodos();
    Estudiante? ObtenerPorId(int id);
    Estudiante? ObtenerPorCodigo(string codigo);
    void Agregar(Estudiante estudiante);
    void Actualizar(Estudiante estudiante);
    void Eliminar(int id);
}

public class EstudianteRepository : IEstudianteRepository
{
    private readonly string _connectionString;

    public EstudianteRepository(IConfiguration configuration)
    {
        _connectionString = configuration.GetConnectionString("DefaultConnection");
    }

    public IEnumerable<Estudiante> ObtenerTodos()
    {
        var estudiantes = new List<Estudiante>();

        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = @"SELECT e.*, c.Nombre as CarreraNombre
                          FROM Estudiantes e
                          LEFT JOIN Carreras c ON e.CarreraId = c.Id";

            using (var command = new SqlCommand(sql, connection))
            using (var reader = command.ExecuteReader())
            {
                while (reader.Read())
                {
                    estudiantes.Add(MapFromReader(reader));
                }
            }
        }

        return estudiantes;
    }

    public Estudiante? ObtenerPorCodigo(string codigo)
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = @"SELECT e.*, c.Nombre as CarreraNombre
                          FROM Estudiantes e
                          LEFT JOIN Carreras c ON e.CarreraId = c.Id
                          WHERE e.Codigo = @Codigo";

            using (var command = new SqlCommand(sql, connection))
            {
                command.Parameters.AddWithValue("@Codigo", codigo);

                using (var reader = command.ExecuteReader())
                {
                    if (reader.Read())
                        return MapFromReader(reader);
                }
            }
        }

        return null;
    }

    public void Agregar(Estudiante estudiante)
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = @"INSERT INTO Estudiantes (Codigo, Nombre, Email, Edad, CarreraId)
                          VALUES (@Codigo, @Nombre, @Email, @Edad, @CarreraId);
                          SELECT CAST(scope_identity() AS int);";

            using (var command = new SqlCommand(sql, connection))
            {
                command.Parameters.AddWithValue("@Codigo", estudiante.Codigo);
                command.Parameters.AddWithValue("@Nombre", estudiante.Nombre);
                command.Parameters.AddWithValue("@Email", estudiante.Email);
                command.Parameters.AddWithValue("@Edad", estudiante.Edad);
                command.Parameters.AddWithValue("@CarreraId", estudiante.CarreraId);

                estudiante.Id = (int)command.ExecuteScalar();
            }
        }
    }

    public void Actualizar(Estudiante estudiante)
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = @"UPDATE Estudiantes
                          SET Nombre = @Nombre, Email = @Email, Edad = @Edad, CarreraId = @CarreraId
                          WHERE Id = @Id";

            using (var command = new SqlCommand(sql, connection))
            {
                command.Parameters.AddWithValue("@Id", estudiante.Id);
                command.Parameters.AddWithValue("@Nombre", estudiante.Nombre);
                command.Parameters.AddWithValue("@Email", estudiante.Email);
                command.Parameters.AddWithValue("@Edad", estudiante.Edad);
                command.Parameters.AddWithValue("@CarreraId", estudiante.CarreraId);

                command.ExecuteNonQuery();
            }
        }
    }

    public void Eliminar(int id)
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = "DELETE FROM Estudiantes WHERE Id = @Id";

            using (var command = new SqlCommand(sql, connection))
            {
                command.Parameters.AddWithValue("@Id", id);
                command.ExecuteNonQuery();
            }
        }
    }

    private Estudiante MapFromReader(SqlDataReader reader)
    {
        return new Estudiante
        {
            Id = Convert.ToInt32(reader["Id"]),
            Codigo = reader["Codigo"].ToString(),
            Nombre = reader["Nombre"].ToString(),
            Email = reader["Email"].ToString(),
            Edad = Convert.ToInt32(reader["Edad"]),
            CarreraId = reader["CarreraId"] != DBNull.Value ? Convert.ToInt32(reader["CarreraId"]) : 0,
            Carrera = new Carrera
            {
                Id = reader["CarreraId"] != DBNull.Value ? Convert.ToInt32(reader["CarreraId"]) : 0,
                Nombre = reader["CarreraNombre"]?.ToString()
            }
        };
    }
}
```

---

## 3. Razor Page con TDD

```csharp
public class IndexModel : PageModel
{
    private readonly IEstudianteRepository _estudianteRepository;

    public IndexModel(IEstudianteRepository estudianteRepository)
    {
        _estudianteRepository = estudianteRepository;
    }

    public IList<Estudiante> Estudiantes { get; set; }

    public void OnGet()
    {
        Estudiantes = _estudianteRepository.ObtenerTodos().ToList();
    }
}
```

---

## 4. Tests (xUnit)

```csharp
public class EstudianteTests
{
    [Fact]
    public void Constructor_ConDatosValidos_CreaEstudiante()
    {
        // Arrange
        var codigo = "2024001";
        var nombre = "María López";

        // Act
        var estudiante = new Estudiante
        {
            Codigo = codigo,
            Nombre = nombre,
            Email = "maria@email.com",
            Edad = 20
        };

        // Assert
        Assert.Equal(codigo, estudiante.Codigo);
        Assert.Equal(nombre, estudiante.Nombre);
    }

    [Fact]
    public void Inscribir_MateriaNoInscrita_AgregaInscripcion()
    {
        // Arrange
        var estudiante = new Estudiante();
        var materia = new Materia { Id = 1, Nombre = "POO" };

        // Act
        estudiante.Inscribir(materia);

        // Assert
        Assert.Single(estudiante.Inscripciones);
    }

    [Fact]
    public void Inscribir_MateriaYaInscrita_LanzaExcepcion()
    {
        // Arrange
        var estudiante = new Estudiante();
        var materia = new Materia { Id = 1, Nombre = "POO" };
        estudiante.Inscribir(materia);

        // Act & Assert
        Assert.Throws<InvalidOperationException>(() =>
            estudiante.Inscribir(materia));
    }
}
```

---

**Última actualización:** 2026-02-01
