# Código - TDD y xUnit

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Proyecto xUnit Completo

### Configuración

```bash
dotnet new xunit -n Calculadora.Tests
cd Calculadora.Tests
dotnet add reference ../Calculadora/Calculadora.csproj
```

### Calculadora.cs

```csharp
public class Calculadora
{
    public int Sumar(int a, int b) => a + b;
    public int Restar(int a, int b) => a - b;
    public int Multiplicar(int a, int b) => a * b;
    public int Dividir(int a, int b)
    {
        if (b == 0)
            throw new DivideByZeroException();
        return a / b;
    }
}
```

### Pruebas Completas

```csharp
using Xunit;

public class CalculadoraTests
{
    [Fact]
    public void Sumar_DosNumeros_RetornaSuma()
    {
        var calc = new Calculadora();
        int resultado = calc.Sumar(5, 3);
        Assert.Equal(8, resultado);
    }

    [Theory]
    [InlineData(1, 1, 2)]
    [InlineData(5, 3, 8)]
    [InlineData(-1, 1, 0)]
    public void Sumar_VariosNumeros_RetornaSuma(int a, int b, int esperado)
    {
        var calc = new Calculadora();
        Assert.Equal(esperado, calc.Sumar(a, b));
    }

    [Fact]
    public void Dividir_DivisorCero_LanzaExcepcion()
    {
        var calc = new Calculadora();
        Assert.Throws<DivideByZeroException>(() => calc.Dividir(10, 0));
    }
}
```

---

## 2. Billetera con TDD

```csharp
public class Billetera
{
    private decimal _saldo;

    public decimal Saldo => _saldo;

    public void Agregar(decimal monto)
    {
        if (monto <= 0)
            throw new ArgumentException("Monto debe ser positivo");
        _saldo += monto;
    }

    public void Retirar(decimal monto)
    {
        if (monto <= 0)
            throw new ArgumentException("Monto debe ser positivo");
        if (monto > _saldo)
            throw new InvalidOperationException("Saldo insuficiente");
        _saldo -= monto;
    }
}
```

### Tests Billetera

```csharp
public class BilleteraTests
{
    [Fact]
    public void Saldo_Inicialmente_EsCero()
    {
        var billetera = new Billetera();
        Assert.Equal(0, billetera.Saldo);
    }

    [Fact]
    public void Agregar_MontoPosicional_IncrementaSaldo()
    {
        var billetera = new Billetera();
        billetera.Agregar(100);
        Assert.Equal(100, billetera.Saldo);
    }

    [Fact]
    public void Retirar_SaldoSuficiente_DecrementaSaldo()
    {
        var billetera = new Billetera();
        billetera.Agregar(100);
        billetera.Retirar(30);
        Assert.Equal(70, billetera.Saldo);
    }

    [Fact]
    public void Retirar_SaldoInsuficiente_LanzaExcepcion()
    {
        var billetera = new Billetera();
        billetera.Agregar(50);
        Assert.Throws<InvalidOperationException>(() => billetera.Retirar(100));
    }
}
```

---

**Última actualización:** 2026-02-01
