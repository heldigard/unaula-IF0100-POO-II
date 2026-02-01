# Teoría - TDD y Pruebas Unitarias

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es TDD?

**Test-Driven Development (TDD)** es una práctica de desarrollo donde se escriben las pruebas ANTES del código de producción.

### Ciclo Red-Green-Refactor

```
🔴 RED   → Escribir prueba que falla
🟢 GREEN → Código mínimo para pasar
🔵 REFACTOR → Eliminar duplicación
🔁 REPEAT → Siguiente prueba
```

### Las Tres Leyes de TDD (Uncle Bob)

1. No escribirás código de producción hasta haber escrito una prueba que falle
2. No escribirás más de una prueba suficiente para fallar
3. No escribirás más código del necesario para pasar la prueba

---

## 2. xUnit Framework

### Atributos Principales

| Atributo | Uso |
|----------|-----|
| `[Fact]` | Prueba sin parámetros |
| `[Theory]` | Prueba parametrizada |
| `[InlineData(...)]` | Datos para [Theory] |

### Patrón AAA

```csharp
[Fact]
public void Sumar_DosNumeros_RetornaSuma()
{
    // Arrange - Configurar
    var calc = new Calculadora();

    // Act - Ejecutar
    int resultado = calc.Sumar(5, 3);

    // Assert - Verificar
    Assert.Equal(8, resultado);
}
```

---

## 3. Test Doubles

| Tipo | Propósito |
|------|-----------|
| **Dummy** | Llena parámetros, sin uso |
| **Stub** | Respuestas predefinidas |
| **Fake** | Implementación simplificada |
| **Mock** | Verifica comportamiento |

---

**Última actualización:** 2026-02-01
