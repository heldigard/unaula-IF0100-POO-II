# Código - DataSet y DataAdapter

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Llenar DataSet

```csharp
public DataSet ObtenerEstudiantesYCarreras()
{
    var dataSet = new DataSet();

    using (var connection = new SqlConnection(_connectionString))
    {
        connection.Open();

        // Adaptador para Estudiantes
        var estAdapter = new SqlDataAdapter(
            "SELECT * FROM Estudiantes", connection);
        var estTable = new DataTable("Estudiantes");
        estAdapter.Fill(estTable);
        dataSet.Tables.Add(estTable);

        // Adaptador para Carreras
        var carrAdapter = new SqlDataAdapter(
            "SELECT * FROM Carreras", connection);
        var carrTable = new DataTable("Carreras");
        carrAdapter.Fill(carrTable);
        dataSet.Tables.Add(carrTable);

        // Crear relación
        dataSet.Relations.Add("EstudianteCarrera",
            dataSet.Tables["Carreras"].Columns["Id"],
            dataSet.Tables["Estudiantes"].Columns["CarreraId"]);
    }

    return dataSet;
}
```

---

## 2. Actualizar DataSet

```csharp
public void GuardarCambios(DataSet dataSet)
{
    using (var connection = new SqlConnection(_connectionString))
    {
        var adapter = new SqlDataAdapter();

        // SELECT para obtener esquema
        adapter.SelectCommand = new SqlCommand(
            "SELECT * FROM Estudiantes", connection);

        // INSERT
        adapter.InsertCommand = new SqlCommand(
            @"INSERT INTO Estudiantes (Codigo, Nombre, Email)
              VALUES (@Codigo, @Nombre, @Email)", connection);
        adapter.InsertCommand.Parameters.Add("@Codigo", SqlDbType.VarChar, 20, "Codigo");
        adapter.InsertCommand.Parameters.Add("@Nombre", SqlDbType.VarChar, 100, "Nombre");
        adapter.InsertCommand.Parameters.Add("@Email", SqlDbType.VarChar, 100, "Email");

        // UPDATE
        adapter.UpdateCommand = new SqlCommand(
            @"UPDATE Estudiantes SET Nombre = @Nombre, Email = @Email
              WHERE Codigo = @Codigo", connection);
        adapter.UpdateCommand.Parameters.Add("@Codigo", SqlDbType.VarChar, 20, "Codigo");
        adapter.UpdateCommand.Parameters.Add("@Nombre", SqlDbType.VarChar, 100, "Nombre");
        adapter.UpdateCommand.Parameters.Add("@Email", SqlDbType.VarChar, 100, "Email");

        // DELETE
        adapter.DeleteCommand = new SqlCommand(
            "DELETE FROM Estudiantes WHERE Codigo = @Codigo", connection);
        adapter.DeleteCommand.Parameters.Add("@Codigo", SqlDbType.VarChar, 20, "Codigo");

        // Guardar cambios
        adapter.Update(dataSet.Tables["Estudiantes"]);
    }
}
```

---

## 3. Navegar Relaciones

```csharp
foreach (DataRow estRow in dataSet.Tables["Estudiantes"].Rows)
{
    var estudianteRow = estRow;
    DataRow carreraRow = estudianteRow.GetParentRow("EstudianteCarrera");

    Console.WriteLine($"{estudianteRow["Nombre"]} - {carreraRow["Nombre"]}");
}
```

---

**Última actualización:** 2026-02-01
