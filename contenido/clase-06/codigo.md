# Código - BDD y SpecFlow

**IF0100 - Lenguaje de Programación OO II**

---

## Proyecto SpecFlow Completo

### 1. Feature File

```gherkin
Feature: Carrito de Compras
  Como cliente
  Quiero agregar productos al carrito
  Para comprarlos

  Scenario: Agregar producto al carrito
    Given un carrito vacío
    When agrego un producto con nombre "Laptop" y precio 1000
    Then el carrito debe tener 1 producto
    And el total debe ser 1000

  Scenario: Agregar múltiples productos
    Given un carrito vacío
    When agrego los siguientes productos:
      | Nombre  | Precio |
      | Laptop  | 1000   |
      | Mouse   | 50     |
      | Teclado | 80     |
    Then el carrito debe tener 3 productos
    And el total debe ser 1130
```

### 2. Step Definitions

```csharp
using TechTalk.SpecFlow;
using Xunit;

namespace Carrito.Specs.Steps
{
    [Binding]
    public class CarritoSteps
    {
        private Carrito _carrito;
        private Producto _producto;

        [Given(@"un carrito vacío")]
        public void GivenUnCarritoVacio()
        {
            _carrito = new Carrito();
        }

        [When(@"agrego un producto con nombre ""(.*)"" y precio (.*)")]
        public void WhenAgregoProducto(string nombre, decimal precio)
        {
            _producto = new Producto { Nombre = nombre, Precio = precio };
            _carrito.Agregar(_producto);
        }

        [When(@"agrego los siguientes productos:")]
        public void WhenAgregoProductos(Table table)
        {
            foreach (var row in table.Rows)
            {
                var p = new Producto
                {
                    Nombre = row["Nombre"],
                    Precio = decimal.Parse(row["Precio"])
                };
                _carrito.Agregar(p);
            }
        }

        [Then(@"el carrito debe tener (.*) productos")]
        public void ThenCarritoTieneProductos(int cantidad)
        {
            Assert.Equal(cantidad, _carrito.CantidadProductos);
        }

        [Then(@"el total debe ser (.*)")]
        public void ThenTotalEs(decimal total)
        {
            Assert.Equal(total, _carrito.Total);
        }
    }
}
```

### 3. Clases del Sistema

```csharp
public class Carrito
{
    private List<Producto> _productos = new();

    public void Agregar(Producto producto)
    {
        _productos.Add(producto);
    }

    public int CantidadProductos => _productos.Count;

    public decimal Total => _productos.Sum(p => p.Precio);
}

public class Producto
{
    public string Nombre { get; set; }
    public decimal Precio { get; set; }
}
```

---

**Última actualización:** 2026-02-01
