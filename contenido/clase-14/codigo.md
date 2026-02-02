# Código - Archivos Planos

**IF0100 - Lenguaje de Programación OO II**

---

## 1. CSV - Lectura y Escritura

```csharp
public class CsvEstudianteRepository
{
    private readonly string _filePath;

    public CsvEstudianteRepository(string filePath)
    {
        _filePath = filePath;
    }

    public void Guardar(IEnumerable<Estudiante> estudiantes)
    {
        using (var writer = new StreamWriter(_filePath))
        {
            writer.WriteLine("Codigo,Nombre,Email,Edad"); // Header

            foreach (var est in estudiantes)
            {
                writer.WriteLine($"{est.Codigo},{est.Nombre},{est.Email},{est.Edad}");
            }
        }
    }

    public List<Estudiante> Leer()
    {
        var estudiantes = new List<Estudiante>();

        if (!File.Exists(_filePath))
            return estudiantes;

        var lineas = File.ReadAllLines(_filePath);
        foreach (var linea in lineas.Skip(1)) // Skip header
        {
            var campos = linea.Split(',');
            estudiantes.Add(new Estudiante
            {
                Codigo = campos[0],
                Nombre = campos[1],
                Email = campos[2],
                Edad = int.Parse(campos[3])
            });
        }

        return estudiantes;
    }
}
```

---

## 2. JSON - Serialización

```csharp
using System.Text.Json;

public class JsonEstudianteRepository
{
    private readonly string _filePath;

    public JsonEstudianteRepository(string filePath)
    {
        _filePath = filePath;
    }

    public void Guardar(List<Estudiante> estudiantes)
    {
        var options = new JsonSerializerOptions { WriteIndented = true };
        string json = JsonSerializer.Serialize(estudiantes, options);
        File.WriteAllText(_filePath, json);
    }

    public List<Estudiante> Leer()
    {
        if (!File.Exists(_filePath))
            return new List<Estudiante>();

        string json = File.ReadAllText(_filePath);
        return JsonSerializer.Deserialize<List<Estudiante>>(json)
               ?? new List<Estudiante>();
    }
}
```

---

**Última actualización:** 2026-02-01
