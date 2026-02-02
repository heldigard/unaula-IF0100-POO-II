# Código - Domain Driven Design

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Dominio: Universidad

### Entidades

```csharp
// Entidad: Tiene identidad
public class Estudiante
{
    public string Codigo { get; }
    public string Nombre { get; private set; }
    private List<Inscripcion> _inscripciones = new();

    public IReadOnlyCollection<Inscripcion> Inscripciones => _inscripciones.AsReadOnly();

    public Estudiante(string codigo, string nombre)
    {
        Codigo = codigo ?? throw new ArgumentNullException(nameof(codigo));
        Nombre = nombre ?? throw new ArgumentNullException(nameof(nombre));
    }

    public void Inscribir(Materia materia)
    {
        if (_inscripciones.Any(i => i.Materia.Id == materia.Id))
            throw new InvalidOperationException("Ya inscrito");

        _inscripciones.Add(new Inscripcion(materia));
    }
}

// Value Object: Sin identidad, inmutable
public record Moneda(decimal Cantidad, string Simbolo);

public record Calificacion(decimal Valor, string Escala)
{
    public Calificacion() : this(0, "0-5") { }
}
```

### Agregado

```csharp
// Agregado Root
public class Pedido
{
    public Guid Id { get; }
    private List<LineaPedido> _lineas = new();

    public IReadOnlyCollection<LineaPedido> Lineas => _lineas.AsReadOnly();
    public Moneda Total => _lineas.Aggregate(
        new Moneda(0, "COP"),
        (acc, linea) => acc + linea.Subtotal);

    public void AgregarProducto(Producto producto, int cantidad)
    {
        var linea = new LineaPedido(producto, cantidad);
        _lineas.Add(linea);
    }
}
```

### Repositorio

```csharp
public interface IEstudianteRepository
{
    Estudiante? ObtenerPorCodigo(string codigo);
    void Guardar(Estudiante estudiante);
    IEnumerable<Estudiante> ObtenerTodos();
}
```

---

**Última actualización:** 2026-02-01
