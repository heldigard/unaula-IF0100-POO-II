# Ejercicios - Sobrecarga, Sobreescritura y Modelado BD

**IF0100 - Lenguaje de Programación OO II**
*Unidad 1 - Clase 4*

---

## Guía de Ejercicios Prácticos

---

## Ejercicio 1: Clase Complejo con Sobrecarga de Operadores

### 🎯 Objetivo
Implementar una clase `Complejo` que represente números complejos con sobrecarga de operadores aritméticos.

### 📋 Especificaciones

#### Clase Complejo

```csharp
public class Complejo
{
    public double Real { get; set; }      // Parte real
    public double Imaginaria { get; set; } // Parte imaginaria

    // Constructores sobrecargados
    public Complejo(double r, double i)
    public Complejo(double r) : this(r, 0)
    public Complejo() : this(0, 0)

    // Operadores a sobrecargar
    public static Complejo operator +(Complejo a, Complejo b)
    public static Complejo operator -(Complejo a, Complejo b)
    public static Complejo operator *(Complejo a, Complejo b)
    public static Complejo operator /(Complejo a, Complejo b)
    public static bool operator ==(Complejo a, Complejo b)
    public static bool operator !=(Complejo a, Complejo b)

    // Otros métodos
    public double Modulo()
    public override string ToString()  // "3 + 2i"
}
```

### ✅ Fórmulas

| Operación | Fórmula |
|-----------|---------|
| **Suma** | (a+bi) + (c+di) = (a+c) + (b+d)i |
| **Resta** | (a+bi) - (c+di) = (a-c) + (b-d)i |
| **Multiplicación** | (a+bi) × (c+di) = (ac-bd) + (ad+bc)i |
| **División** | (a+bi) / (c+di) = [(ac+bd) + (bc-ad)i] / (c²+d²) |
| **Módulo** | \|a+bi\| = √(a² + b²) |

### ✅ Checklist de Implementación

- [ ] Crear clase `Complejo` con propiedades `Real` e `Imaginaria`
- [ ] Implementar 3 constructores sobrecargados con encadenamiento
- [ ] Sobrecargar operadores `+`, `-`, `*`, `/`
- [ ] Sobrecargar operadores `==` y `!=`
- [ ] Sobrescribir `Equals()` y `GetHashCode()`
- [ ] Implementar método `Modulo()`
- [ ] Sobrescribir `ToString()` para formato "a + bi"
- [ ] Crear programa de prueba

### ✅ Criterios de Validación

| Criterio | Validación |
|----------|------------|
| Compilación | Sin errores |
| Operadores | `+`, `-`, `*`, `/` funcionan correctamente |
| Igualdad | `==` compara correctamente dos complejos |
| Constructor | Todos los constructores funcionan |
| Formato | `ToString()` muestra "3 + 2i" o "3 - 2i" |

### 📊 Salida Esperada

```
=== NÚMEROS COMPLEJOS ===

c1 = 3 + 2i
c2 = 1 - 4i
c3 = 5 + 0i

Operaciones:
c1 + c2 = 4 - 2i
c1 - c2 = 2 + 6i
c1 * c2 = 11 - 10i
c1 / c2 = -0.176 + 0.824i

Módulos:
|c1| = 3.61
|c2| = 4.12

Igualdad:
(3 + 2i) == (3 + 2i): True
```

---

## Ejercicio 2: Tienda Online - Modelado ER

### 🎯 Objetivo
Modelar una tienda online con diagrama Entidad-Relación y mapeo a clases C#.

### 📋 Especificaciones

#### Entidades Requeridas

| Entidad | Atributos |
|---------|-----------|
| **Cliente** | ID (PK), Nombre, Email, Dirección, Teléfono |
| **Producto** | ID (PK), Nombre, Descripción, Precio, Stock, CategoriaID |
| **Categoria** | ID (PK), Nombre, Descripción |
| **Orden** | ID (PK), Fecha, Estado, Total, ClienteID (FK) |
| **DetalleOrden** | ID (PK), Cantidad, Subtotal, OrdenID (FK), ProductoID (FK) |

### 📊 Relaciones

| Relación | Tipo | Descripción |
|----------|------|-------------|
| Categoria → Producto | 1:N | Una categoría tiene muchos productos |
| Cliente → Orden | 1:N | Un cliente hace muchas órdenes |
| Orden → DetalleOrden | 1:N | Una orden tiene muchos detalles |
| Producto → DetalleOrden | 1:N | Un producto aparece en muchos detalles |

### ✅ Checklist de Implementación

- [ ] Dibujar diagrama ER completo en papel
- [ ] Crear clases `Cliente`, `Producto`, `Categoria`, `Orden`, `DetalleOrden`
- [ ] Implementar propiedades de navegación (Listas)
- [ ] Implementar propiedades FK (IDs)
- [ ] Crear constructor principal para cada clase
- [ ] Implementar `ToString()` en todas las clases
- [ ] Crear programa de prueba con datos de ejemplo
- [ ] Demostrar navegación de relaciones

### 🔍 Pistas

```csharp
public class Cliente
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public string Email { get; set; }
    public List<Orden> Ordenes { get; set; }  // Relación 1:N
}

public class Orden
{
    public int Id { get; set; }
    public DateTime Fecha { get; set; }
    public string Estado { get; set; }
    public decimal Total { get; set; }

    // FK
    public int ClienteId { get; set; }

    // Navegación
    public Cliente Cliente { get; set; }
    public List<DetalleOrden> Detalles { get; set; }
}
```

### ✅ Criterios de Validación

| Criterio | Validación |
|----------|------------|
| Diagrama ER | Todas las entidades y relaciones identificadas |
| Mapeo | Todas las clases mapean correctamente a tablas |
| Relaciones 1:N | Listas y FKs implementadas |
| Navegación | Se puede navegar de Cliente a Orden a Detalle |
| SQL | Generar scripts CREATE TABLE para todas las entidades |

---

## Ejercicio 3: Sistema de Reservas de Hotel

### 🎯 Objetivo
Modelar un sistema de reservas de hotel con relaciones complejas.

### 📋 Especificaciones

#### Entidades

| Entidad | Atributos |
|---------|-----------|
| **Hotel** | ID (PK), Nombre, Dirección, Estrellas, Ciudad |
| **Habitacion** | Numero (PK), HotelID (FK), Tipo, PrecioNoche, Disponible |
| **Cliente** | DNI (PK), Nombre, Email, Telefono |
| **Reserva** | ID (PK), FechaEntrada, FechaSalida, Estado, Total, ClienteDNI (FK), HabitacionNumero (FK), HotelID (FK) |

### 📊 Relaciones

| Relación | Tipo |
|----------|------|
| Hotel → Habitacion | 1:N |
| Cliente → Reserva | 1:N |
| Habitacion → Reserva | 1:N |

### ✅ Checklist de Implementación

- [ ] Crear diagrama ER
- [ ] Implementar todas las clases
- [ ] Relaciones 1:N con Listas y FKs
- [ ] Validar que una habitación no tenga reservas solapadas
- [ ] Calcular total de reserva automáticamente
- [ ] Método para buscar habitaciones disponibles por fechas
- [ ] Programa de prueba

### 🔍 Pistas

```csharp
public class Reserva
{
    public int Id { get; set; }
    public DateTime FechaEntrada { get; set; }
    public DateTime FechaSalida { get; set; }

    // Calcular total automáticamente
    public decimal Total
    {
        get
        {
            int noches = (FechaSalida - FechaEntrada).Days;
            return Habitacion?.PrecioNoche * noches ?? 0;
        }
    }

    public bool EstaSolapadaCon(Reserva otra)
    {
        return FechaEntrada < otra.FechaSalida &&
               FechaSalida > otra.FechaEntrada;
    }
}
```

---

## Ejercicio 4: 🌟 Desafío - Vector Matemático

### 🎯 Objetivo
Implementar una clase `Vector` con sobrecarga completa de operadores.

### 📋 Especificaciones

```csharp
public class Vector
{
    public double[] Componentes { get; set; }

    // Constructores
    public Vector(int dimension)
    public Vector(params double[] componentes)

    // Operadores aritméticos
    public static Vector operator +(Vector a, Vector b)
    public static Vector operator -(Vector a, Vector b)
    public static Vector operator *(Vector v, double escalar)
    public static Vector operator *(double escalar, Vector v)
    public static double operator *(Vector a, Vector b)  // Producto punto

    // Operadores de comparación
    public static bool operator ==(Vector a, Vector b)
    public static bool operator !=(Vector a, Vector b)

    // Métodos
    public double Norma()           // √(Σx²)
    public Vector Normalizar()      // v / ‖v‖
    public bool EsOrtonogonalCon(Vector otro)
}
```

### ✅ Fórmulas

| Operación | Fórmula |
|-----------|---------|
| **Suma** | (a₁,...,aₙ) + (b₁,...,bₙ) = (a₁+b₁,...,aₙ+bₙ) |
| **Producto escalar** | v × k = (v₁×k, ..., vₙ×k) |
| **Producto punto** | a · b = Σ(aᵢ × bᵢ) |
| **Norma** | ‖v‖ = √(Σvᵢ²) |
| **Normalizar** | v̂ = v / ‖v‖ |

---

## Ejercicio 5: Banco - Modelado Completo

### 🎯 Objetivo
Modelar el sistema bancario del ejercicio anterior con diagrama ER y mapeo completo.

### 📋 Especificaciones

#### Entidades

| Entidad | Atributos |
|---------|-----------|
| **Banco** | ID (PK), Nombre, Dirección |
| **Sucursal** | ID (PK), Nombre, Direccion, BancoID (FK) |
| **Cliente** | ID (PK), Nombre, Documento, Email |
| **Cuenta** | Numero (PK), Tipo, Saldo, ClienteID (FK), SucursalID (FK) |
| **Transaccion** | ID (PK), Fecha, Tipo, Monto, CuentaNumero (FK) |

### 📊 Relaciones

| Relación | Tipo |
|----------|------|
| Banco → Sucursal | 1:N |
| Cliente → Cuenta | 1:N |
| Sucursal → Cuenta | 1:N |
| Cuenta → Transaccion | 1:N |

### ✅ Requisitos Adicionales

- [ ] Validar que `Saldo` nunca sea negativo para `CuentaAhorros`
- [ ] Validar sobregiro para `CuentaCorriente`
- [ ] Método `Consignar()` y `Retirar()` en `Cuenta`
- [ ] Registrar todas las transacciones
- [ ] Generar extracto mensual

---

## Ejercicio 6: Normalización de BD

### 🎯 Objetivo
Convertir una tabla anormalizada a Tercera Forma Normal (3FN).

### ❌ Tabla Anormalizada

```sql
CREATE TABLE VentasAnormal (
    VentaID INT PRIMARY KEY,
    Fecha DATE,
    ClienteNombre VARCHAR(100),
    ClienteDireccion VARCHAR(200),
    ClienteTelefono VARCHAR(20),
    ProductoNombre VARCHAR(100),
    ProductoCategoria VARCHAR(50),
    ProductoPrecio DECIMAL(10,2),
    Cantidad INT,
    VendedorNombre VARCHAR(100),
    VendedorComision DECIMAL(5,2)
);
```

### ✅ Tareas

- [ ] Identificar todas las anomalías
- [ ] Normalizar a 1FN
- [ ] Normalizar a 2FN
- [ ] Normalizar a 3FN
- [ ] Crear scripts SQL para todas las tablas
- [ ] Crear diagrama ER
- [ ] Mapear a clases C#
- [ ] Documentar las relaciones con FKs

---

## Guía de Solución

### Paso 1: Análisis

Antes de codificar:
1. Dibujar el diagrama ER
2. Identificar todas las relaciones
3. Definir PKs y FKs
4. Normalizar a 3FN

### Paso 2: Implementación

1. Crear las entidades (clases)
2. Implementar propiedades de navegación
3. Implementar FKs
4. Crear constructores
5. Sobrescribir `ToString()`

### Paso 3: Validación

1. Compila sin errores?
2. Las relaciones funcionan?
3. La navegación es correcta?
4. El mapeo SQL es válido?

---

## Errores Comunes

### Error 1: Olvidar par de operadores

```csharp
// ❌ ERROR
public static bool operator ==(Complejo a, Complejo b) { }
// Falta !=

// ✅ CORRECTO
public static bool operator ==(Complejo a, Complejo b) { }
public static bool operator !=(Complejo a, Complejo b) => !(a == b);
```

### Error 2: No normalizar BD

```csharp
// ❌ ERROR: Datos redundantes
public class Estudiante
{
    public string CarreraNombre { get; set; }
    public string CarreraDuracion { get; set; }  // Redundante
}

// ✅ CORRECTO: Relación 1:N
public class Estudiante
{
    public int CarreraId { get; set; }
    public Carrera Carrera { get; set; }
}
```

### Error 3: Relación N:M sin tabla intermedia

```csharp
// ❌ ERROR: No se puede mapear directamente a SQL
public class Estudiante
{
    public List<Materia> Materias { get; set; }  // ¿Cómo se guarda?
}

// ✅ CORRECTO: Tabla intermedia
public class Estudiante
{
    public List<Inscripcion> Inscripciones { get; set; }
}
```

---

**Última actualización:** 2026-02-01
