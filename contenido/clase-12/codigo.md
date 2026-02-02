# Código - ADO.NET

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Consulta con DataReader

```csharp
using System.Data.SqlClient;

public List<Estudiante> ObtenerEstudiantes()
{
    var estudiantes = new List<Estudiante>();
    var connectionString = _config.GetConnectionString("DefaultConnection");

    using (var connection = new SqlConnection(connectionString))
    {
        connection.Open();

        string sql = "SELECT Codigo, Nombre, Email FROM Estudiantes";
        using (var command = new SqlCommand(sql, connection))
        using (var reader = command.ExecuteReader())
        {
            while (reader.Read())
            {
                estudiantes.Add(new Estudiante
                {
                    Codigo = reader["Codigo"].ToString(),
                    Nombre = reader["Nombre"].ToString(),
                    Email = reader["Email"].ToString()
                });
            }
        }
    }

    return estudiantes;
}
```

---

## 2. Insertar con Parámetros

```csharp
public void InsertarEstudiante(Estudiante estudiante)
{
    var connectionString = _config.GetConnectionString("DefaultConnection");

    using (var connection = new SqlConnection(connectionString))
    {
        connection.Open();

        string sql = @"INSERT INTO Estudiantes (Codigo, Nombre, Email, Edad)
                      VALUES (@Codigo, @Nombre, @Email, @Edad)";

        using (var command = new SqlCommand(sql, connection))
        {
            // Parámetros para prevenir SQL Injection
            command.Parameters.AddWithValue("@Codigo", estudiante.Codigo);
            command.Parameters.AddWithValue("@Nombre", estudiante.Nombre);
            command.Parameters.AddWithValue("@Email", estudiante.Email);
            command.Parameters.AddWithValue("@Edad", estudiante.Edad);

            command.ExecuteNonQuery();
        }
    }
}
```

---

## 3. DataSet Desconectado

```csharp
public DataTable ObtenerEstudiantesDataTable()
{
    var connectionString = _config.GetConnectionString("DefaultConnection");

    using (var connection = new SqlConnection(connectionString))
    {
        string sql = "SELECT * FROM Estudiantes";
        using (var adapter = new SqlDataAdapter(sql, connection))
        {
            var dataTable = new DataTable();
            adapter.Fill(dataTable);
            return dataTable;
        }
    }
}
```

---

**Última actualización:** 2026-02-01
