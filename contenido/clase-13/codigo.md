# Código - CRUD ADO.NET

**IF0100 - Lenguaje de Programación OO II**

---

## Repository Completo

```csharp
public class EstudianteRepository : IEstudianteRepository
{
    private readonly string _connectionString;

    public EstudianteRepository(IConfiguration config)
    {
        _connectionString = config.GetConnectionString("DefaultConnection");
    }

    public IEnumerable<Estudiante> GetAll()
    {
        var estudiantes = new List<Estudiante>();

        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = "SELECT * FROM Estudiantes ORDER BY Nombre";

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

    public Estudiante? GetById(string codigo)
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = "SELECT * FROM Estudiantes WHERE Codigo = @Codigo";

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

    public void Insert(Estudiante estudiante)
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = @"INSERT INTO Estudiantes (Codigo, Nombre, Email, Edad, CarreraId)
                          VALUES (@Codigo, @Nombre, @Email, @Edad, @CarreraId)";

            using (var command = new SqlCommand(sql, connection))
            {
                AddParameters(command, estudiante);
                command.ExecuteNonQuery();
            }
        }
    }

    public void Update(Estudiante estudiante)
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = @"UPDATE Estudiantes
                          SET Nombre = @Nombre, Email = @Email, Edad = @Edad, CarreraId = @CarreraId
                          WHERE Codigo = @Codigo";

            using (var command = new SqlCommand(sql, connection))
            {
                AddParameters(command, estudiante);
                command.ExecuteNonQuery();
            }
        }
    }

    public void Delete(string codigo)
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            string sql = "DELETE FROM Estudiantes WHERE Codigo = @Codigo";

            using (var command = new SqlCommand(sql, connection))
            {
                command.Parameters.AddWithValue("@Codigo", codigo);
                command.ExecuteNonQuery();
            }
        }
    }

    private Estudiante MapFromReader(SqlDataReader reader)
    {
        return new Estudiante
        {
            Codigo = reader["Codigo"].ToString(),
            Nombre = reader["Nombre"].ToString(),
            Email = reader["Email"].ToString(),
            Edad = Convert.ToInt32(reader["Edad"])
        };
    }

    private void AddParameters(SqlCommand command, Estudiante estudiante)
    {
        command.Parameters.AddWithValue("@Codigo", estudiante.Codigo);
        command.Parameters.AddWithValue("@Nombre", estudiante.Nombre);
        command.Parameters.AddWithValue("@Email", estudiante.Email);
        command.Parameters.AddWithValue("@Edad", estudiante.Edad);
        command.Parameters.AddWithValue("@CarreraId", estudiante.CarreraId);
    }
}
```

---

**Última actualización:** 2026-02-01
