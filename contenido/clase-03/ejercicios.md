# Ejercicios - Herencia y Polimorfismo

**IF0100 - Lenguaje de Programación OO II**
*Unidad 1 - Clase 3*

---

## Guía de Ejercicios Prácticos

Cada ejercicio incluye:
- ✅ Objetivo claro
- 📋 Especificaciones detalladas
- 🔍 Pistas de implementación
- ✅ Criterios de validación

---

## Ejercicio 1: Sistema Bancario con Cuentas

### 🎯 Objetivo
Implementar una jerarquía de cuentas bancarias usando clases abstractas y polimorfismo.

### 📋 Especificaciones

#### Clase Abstracta: `CuentaBancaria`

```csharp
public abstract class CuentaBancaria
{
    public string Numero { get; set; }
    public string Titular { get; set; }
    public decimal Saldo { get; protected set; }

    // Constructor
    public CuentaBancaria(string numero, string titular, decimal saldoInicial)

    // MÉTODOS ABSTRACTOS (las hijas DEBEN implementar)
    public abstract decimal CalcularInteresMensual();

    // MÉTODO CONCRETO (las hijas heredan)
    public void Consignar(decimal monto)

    public bool Retirar(decimal monto)

    public void ConsultarSaldo()
}
```

#### Clases Concretas

**CuentaAhorros**
- Interés mensual: **3%** sobre el saldo
- No permite sobregiro
- Tiene un contador de transacciones

**CuentaCorriente**
- Interés mensual: **0%**
- Permite sobregiro hasta un límite
- Cobra comisión por sobregiro

### ✅ Checklist de Implementación

- [ ] Crear clase abstracta `CuentaBancaria`
- [ ] Implementar `CuentaAhorros` con interés del 3%
- [ ] Implementar `CuentaCorriente` con límite de sobregiro
- [ ] Usar `override` en `CalcularInteresMensual()`
- [ ] Validar montos negativos en consignaciones/retiros
- [ ] Crear programa de prueba

### 🔍 Pistas

```csharp
// Para CuentaAhorros
public override decimal CalcularInteresMensual()
{
    return Saldo * 0.03m;  // 3% mensual
}

// Para CuentaCorriente
private decimal _limiteSobregiro = 1000000m;

public override bool Retirar(decimal monto)
{
    if (Saldo - monto >= -_limiteSobregiro)
    {
        Saldo -= monto;
        return true;
    }
    return false;
}
```

### ✅ Criterios de Validación

| Criterio | Validación |
|----------|------------|
| Compilación | Sin errores, todos los métodos abstractos implementados |
| Funcionalidad | CuentaAhorros calcula 3% de interés correctamente |
| Funcionalidad | CuentaCorriente permite retiros hasta el límite |
| Validación | Rechaza montos negativos en consignaciones |
| Polimorfismo | `List<CuentaBancaria>` funciona con ambos tipos |

### 📊 Salida Esperada

```
=== SISTEMA BANCARIO ===

Cuenta de Ahorros: 123-456-789-0
Titular: María López
Saldo actual: $1,030,000.00 (con interés del 3%)

Cuenta Corriente: 987-654-321-0
Titular: Carlos Ruiz
Saldo actual: -$200,000.00 (con sobregiro)
```

---

## Ejercicio 2: Sistema de Nómina Universitaria

### 🎯 Objetivo
Crear una jerarquía de empleados universitarios con cálculo polimórfico de salarios.

### 📋 Especificaciones

#### Clase Abstracta: `EmpleadoUniversidad`

```csharp
public abstract class EmpleadoUniversidad
{
    public string Nombre { get; set; }
    public string Documento { get; set; }

    // MÉTODO ABSTRACTO
    public abstract decimal CalcularSalario();

    // MÉTODO VIRTUAL
    public virtual string GenerarCheque()
    {
        return $"Pagar a la orden de: {Nombre}\n" +
               $"Valor: ${CalcularSalario():N2}";
    }
}
```

#### Clases Concretas

**Profesor**
- Salario base mensual
- Pago por horas extra ($20,000/hora)
- Bonificación por título de posgrado ($500,000)

**Administrativo**
- Salario fijo mensual
- Sin horas extra
- Bonificación por antigüedad (2% por año)

**Monitor**
- Solo pago por horas trabajadas ($15,000/hora)
- Máximo 80 horas/mes
- No tiene salario base

### ✅ Checklist de Implementación

- [ ] Crear `EmpleadoUniversidad` como abstracta
- [ ] Implementar `Profesor` con salario base + horas extra + posgrado
- [ ] Implementar `Administrativo` con salario fijo + antigüedad
- [ ] Implementar `Monitor` con solo horas trabajadas
- [ ] Validar máximo de horas para Monitor
- [ ] Sobrescribir `GenerarCheque()` en al menos una clase
- [ ] Crear lista polimórfica y procesar nómina

### 🔍 Pistas

```csharp
public class Profesor : EmpleadoUniversidad
{
    public decimal SalarioBase { get; set; }
    public int HorasExtra { get; set; }
    public bool TienePosgrado { get; set; }

    public override decimal CalcularSalario()
    {
        decimal total = SalarioBase;
        total += HorasExtra * 20000m;
        if (TienePosgrado)
            total += 500000m;
        return total;
    }
}

public class Monitor : EmpleadoUniversidad
{
    public int HorasTrabajadas { get; set; }
    private const int MAX_HORAS = 80;
    private const decimal VALOR_HORA = 15000m;

    public override decimal CalcularSalario()
    {
        if (HorasTrabajadas > MAX_HORAS)
            throw new ArgumentException($"Máximo {MAX_HORAS} horas permitidas");
        return HorasTrabajadas * VALOR_HORA;
    }
}
```

### ✅ Criterios de Validación

| Criterio | Validación |
|----------|------------|
| Polimorfismo | Salario se calcula diferente según tipo |
| Validación | Monitor rechaza más de 80 horas |
| Herencia | Todos los empleados tienen Nombre y Documento |
| Override | Al menos una clase sobrescribe `GenerarCheque()` |

---

## Ejercicio 3: Sistema de Figuras Extendido

### 🎯 Objetivo
Extender el sistema de figuras geométricas con nuevas formas y validaciones.

### 📋 Especificaciones

#### Nuevas Figuras a Implementar

**Triángulo**
- Propiedades: `Base`, `Altura`, `Lado1`, `Lado2`, `Lado3`
- Área: `(Base × Altura) / 2`
- Perímetro: `Lado1 + Lado2 + Lado3`
- Validar desigualdad triangular

**Trapecio**
- Propiedades: `BaseMayor`, `BaseMenor`, `Altura`
- Área: `((BaseMayor + BaseMenor) × Altura) / 2`
- Perímetro: Requiere los 4 lados

**Cuadrado** (hereda de `Rectangulo`)
- Un solo lado (lado = base = altura)
- Área: `Lado²`
- Perímetro: `4 × Lado`

### ✅ Checklist de Implementación

- [ ] Crear `Triangulo` con validación de desigualdad triangular
- [ ] Crear `Trapecio` con bases y altura
- [ ] Crear `Cuadrado` heredando de `Rectangulo`
- [ ] Validar que todos los lados sean positivos
- [ ] Agregar todas las figuras a una lista polimórfica
- [ ] Calcular área y perímetro total de todas las figuras
- [ ] Implementar método `Dibujar()` específico para cada figura

### 🔍 Pistas

```csharp
// Validación de desigualdad triangular
private bool ValidarTriangulo(double l1, double l2, double l3)
{
    return (l1 + l2 > l3) && (l1 + l3 > l2) && (l2 + l3 > l1);
}

// Constructor de Triángulo
public Triangulo(double @base, double altura,
                double l1, double l2, double l3)
{
    if (!ValidarTriangulo(l1, l2, l3))
        throw new ArgumentException("Los lados no forman un triángulo válido");
    // ...
}

// Cuadrado hereda de Rectangulo
public class Cuadrado : Rectangulo
{
    public double Lado
    {
        get => Base;
        set => Base = Altura = value;
    }

    public Cuadrado(string nombre, string color, double lado)
        : base(nombre, color, lado, lado)
    {
    }
}
```

### ✅ Criterios de Validación

| Criterio | Validación |
|----------|------------|
| Herencia | `Cuadrado` hereda correctamente de `Rectangulo` |
| Validación | `Triangulo` rechaza lados inválidos |
| Polimorfismo | Lista `List<Figura>` contiene todos los tipos |
| Cálculos | Áreas y perímetros son correctos |

---

## Ejercicio 4: 🌟 Desafío - Sistema de Transporte

### 🎯 Objetivo
Modelar un sistema de transporte con diferentes tipos de vehículos, aplicando correctamente el principio LSP.

### 📋 Especificaciones

#### Análisis LSP

**¿Qué vehícu­los NO deberían heredar de otros?**

- ❌ `Avion` NO debería heredar de `VehiculoTerrestre`
- ❌ `Barco` NO debería hereda de `VehiculoTerrestre`
- ✅ `Auto`, `Camion`, `Moto` SÍ pueden heredar de `VehiculoTerrestre`

#### Jerarquía Propuesta

```
Vehiculo (abstracta)
├── VehiculoTerrestre (abstracta)
│   ├── Auto
│   ├── Camion
│   └── Moto
├── VehiculoAereo (abstracta)
│   ├── Avion
│   └── Helicoptero
└── VehiculoAcuatico (abstracta)
    ├── Barco
    └── Submarino
```

### ✅ Checklist de Implementación

- [ ] Diseñar jerarquía que respete LSP
- [ ] Crear `Vehiculo` con métodos abstractos comunes
- [ ] Crear clases intermedias (`VehiculoTerrestre`, etc.)
- [ ] Implementar vehículos concretos
- [ ] Cada tipo tiene comportamiento de movimiento diferente
- [ ] Crear lista polimórfica de vehículos
- [ ] Simular movimiento de todos los vehículos

### 🔍 Pistas

```csharp
public abstract class Vehiculo
{
    public string Nombre { get; set; }
    public abstract void Moverse();
    public abstract decimal CalcularVelocidadMaxima();
}

public abstract class VehiculoTerrestre : Vehiculo
{
    public int NumeroRuedas { get; set; }
    public string TipoCombustible { get; set; }
}

public class Auto : VehiculoTerrestre
{
    public override void Moverse()
    {
        Console.WriteLine($"{Nombre} rueda por la carretera");
    }
}

public class Avion : VehiculoAereo
{
    public override void Moverse()
    {
        Console.WriteLine($"{Nombre} vuela por el cielo");
    }
}
```

### ✅ Criterios de Validación

| Criterio | Validación |
|----------|------------|
| LSP | Ninguna clase viola el principio de sustitución |
| Polimorfismo | `List<Vehiculo>` funciona con todos los tipos |
| Comportamiento | Cada vehículo se mueve según su naturaleza |
| Jerarquía | Máximo 3 niveles de profundidad |

---

## Guía de Solución

### Paso 1: Diseño

Antes de codificar, dibuja la jerarquía en papel:

```
Clase Base
  ├── Hija 1
  ├── Hija 2
  └── Hija 3
```

### Paso 2: Identificar

- ¿Qué métodos deben ser `abstract`?
- ¿Qué métodos deben ser `virtual`?
- ¿Qué métodos son concretos (no cambian)?

### Paso 3: Implementar

1. Primero la clase base
2. Luego las clases derivadas
3. Finalmente, el programa de prueba

### Paso 4: Validar

- Compila sin errores?
- El polimorfismo funciona?
- Las validaciones están correctas?

---

## Errores Comunes y Cómo Evitarlos

### Error 1: Olvidar `override`

```csharp
// ❌ ERROR
public class Hija : Padre
{
    public void Metodo() { }  // Falta override
}

// ✅ CORRECTO
public class Hija : Padre
{
    public override void Metodo() { }
}
```

### Error 2: No implementar métodos abstractos

```csharp
// ❌ ERROR: CalcularSalario es abstract
public class Empleado : EmpleadoUniversidad
{
    // Falta implementar CalcularSalario()
}

// ✅ CORRECTO
public class Empleado : EmpleadoUniversidad
{
    public override decimal CalcularSalario()
    {
        return 1000000m;
    }
}
```

### Error 3: Violación de LSP

```csharp
// ❌ ERROR: Un pingüino no puede volar
class Ave
{
    public virtual void Volar() { }
}

class Pinguino : Ave
{
    public override void Volar()
    {
        throw new Exception("No puedo volar");
    }
}

// ✅ CORRECTO: Separar comportamientos
class Ave { }
class AveVoladora : Ave
{
    public virtual void Volar() { }
}
class Pinguino : Ave  // No hereda de AveVoladora
{ }
```

---

**Última actualización:** 2026-02-01
