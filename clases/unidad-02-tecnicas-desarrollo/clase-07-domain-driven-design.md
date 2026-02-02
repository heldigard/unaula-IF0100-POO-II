---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 2'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
style: |
  section {
    font-size: 22px;
  }
  h1 {
    color: #1e40af;
    font-size: 2em;
  }
  h2 {
    color: #1e3a8a;
    font-size: 1.5em;
  }
  h3 {
    color: #3b82f6;
    font-size: 1.2em;
  }
  table {
    font-size: 0.85em;
  }
  code {
    font-size: 0.8em;
  }
  pre {
    font-size: 0.7em;
  }
---

<!-- _class: lead -->

# DDD - Domain-Driven Design

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 2 - Clase 7**

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

| # | Objetivo |
|---|-----------|
| 1 | **Comprender** los fundamentos de Domain Driven Design |
| 2 | **Distinguir** entre Entities, Value Objects y Aggregates |
| 3 | **Aplicar** el patrón Repository para persistencia |
| 4 | **Identificar** Bounded Contexts en un sistema |
| 5 | **Implementar** una arquitectura en capas con DDD |

---

## Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 10' | ¿Qué es DDD? |
| 10' | Ubiquitous Language |
| 15' | Entities vs Value Objects |
| 15' | Aggregates y Aggregate Roots |
| 15' | Repositories y Services |
| 15' | Arquitectura en Capas |
| 10' | Ejemplo práctico: Sistema de Pedidos |

---

## 1. ¿Qué es DDD?

### 📖 Definición

> **DDD** es un enfoque de diseño de software que se centra en modelar el software según el dominio del negocio, utilizando un lenguaje común (Ubiquitous Language) entre desarrolladores y expertos del dominio.

### 🏛️ El Problema que Resuelve

| Problema | Descripción |
|----------|-------------|
| **Desconexión** | Desarrolladores y expertos del negocio no se entienden |
| **Modelo técnico ≠ Modelo mental** | El código no refleja cómo piensa el negocio |
| **Software expresivo** | El código no comunica la intención del dominio |

---

## DDD: Solución al Problema

```
┌─────────────────────────────────────────────────────────────┐
│              DOMAIN DRIVEN DESIGN (Eric Evans, 2003)        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   PROBLEMA QUE RESUELVE:                                    │
│                                                             │
│   Desarrolladores ↔ Expertos de Negocio                    │
│         ↓                    ↓                              │
│   "UserController"     "El cliente tiene un pedido"        │
│   "Tabla Pedidos"      "en estado pendiente de pago"       │
│   "DTO OrderDTO"                                          │
│                                                             │
│   ❌ No se entienden                                      │
│   ❌ Modelo técnico ≠ Modelo mental del negocio            │
│   ❌ Software no refleja el dominio                        │
│                                                             │
│   SOLUCIÓN DDD:                                             │
│   • Mismo lenguaje (técnicos y negocio)                    │
│   • Modelo profundo del dominio                            │
│   • Software = expresión del dominio                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ¿Cuándo Usar DDD?

### ✅ USAR DDD cuando:

| Condición | Descripción |
|-----------|-------------|
| **Complejidad ALTA** | Reglas de negocio complejas, flujos elaborados |
| **Dominio cambiable** | El dominio cambia frecuentemente |
| **Expertos disponibles** | Hay personas que conocen el negocio a fondo |
| **Proyecto largo** | Meses/años de desarrollo |
| **Software estratégico** | Es crítico para el negocio |

### ❌ NO usar DDD cuando:

| Condición | Descripción |
|-----------|-------------|
| **CRUD simple** | Poca lógica de negocio |
| **Proyecto corto** | Proyectos pequeños o de corta duración |
| **Sin expertos** | No hay acceso a expertos de dominio |
| **Prototipo/MVP** | Desarrollo rápido de prototipos |

---

## 2. Lenguaje Ubicuo (Ubiquitous Language)

### 📚 Concepto Fundamental

> El **Lenguaje Ubicuo** es el vocabulario compartido entre desarrolladores y expertos del negocio. Todos usan las mismas palabras para describir el mismo concepto.

### ❌ SIN Ubiquitous Language

| Desarrollador | Negocio | Base de Datos |
|---------------|---------|---------------|
| "UserController" | "El cliente" | "tabla_users" |
| "OrderDTO" | "hace un pedido" | "orders" |
| "save()" | "registra" | "INSERT" |
| "status = 1" | "está pendiente" | "status_id" |

→ **Tres lenguajes diferentes → Confusión → Bugs**

---

## ✅ CON Ubiquitous Language

Todos usan el mismo lenguaje:

| Concepto | Término Correcto |
|----------|-----------------|
| Cliente | "Cliente" (no User, no usuario) |
| Realizar pedido | "RealizarPedido" (no save, no createOrder) |
| Estado | "PedidoPendiente" (no status = 1) |
| Confirmar | "ConfirmarPago" (no updatePaymentStatus) |

→ **Un solo lenguaje → Comprensión compartida → Calidad**

---

## Ejemplo: Código ANTES vs DESPUÉS

### ❌ ANTES: Lenguaje técnico

```csharp
public class OrderController
{
    public IActionResult CreateOrder(OrderDTO dto)
    {
        var order = new Order {
            CustomerId = dto.CustomerId,
            Items = dto.Items,
            Status = 1  // ¿Qué es 1?
        };
        _db.Orders.Add(order);
        _db.SaveChanges();
        return Ok(order.Id);
    }
}
```

### ✅ DESPUÉS: Ubiquitous Language

```csharp
public class RealizarPedidoHandler
{
    public PedidoRealizado Handle(RealizarPedidoCommand command)
    {
        var cliente = _clientes.Obtener(command.ClienteId);
        var pedido = cliente.RealizarPedido(command.Items);
        _pedidos.Guardar(pedido);
        return new PedidoRealizado(pedido.Id);
    }
}
```

---

## 3. Entities vs Value Objects

### 📊 Tabla Comparativa

| Aspecto | **ENTITY** | **VALUE OBJECT** |
|---------|------------|------------------|
| **Definida por** | IDENTIDAD | ATRIBUTOS |
| **¿Tiene ID?** | ✅ Sí, ID único | ❌ No |
| **Mutabilidad** | Mutable | Inmutable |
| **Comparación** | Por identidad | Por valor |
| **Ejemplos** | Cliente, Pedido | Dinero, Dirección, Email, Color |

### 💡 Ejemplos Prácticos

| Entity | Value Object |
|--------|--------------|
| Cliente (mismo ID aunque cambie email) | Dinero (100 USD = 100 USD) |
| Pedido (mismo ID aunque cambie estado) | Dirección (calle, ciudad, código postal) |
| Producto | Email (texto@dominio.com) |
| | Color (RGB) |

---

## Entity en C#

```csharp
// ENTITY: Cliente
// Tiene identidad única que persiste durante todo su ciclo de vida

public class Cliente
{
    // Identidad - Lo define como Entity
    public ClienteId Id { get; private set; }

    // Atributos - Pueden cambiar
    public string Nombre { get; private set; }
    public Email Email { get; private set; }
    public Direccion Direccion { get; private set; }
    public DateTime FechaRegistro { get; private set; }

    // Constructor para crear
    public Cliente(ClienteId id, string nombre, Email email)
    {
        Id = id ?? throw new ArgumentNullException(nameof(id));
        Nombre = !string.IsNullOrWhiteSpace(nombre) ? nombre
            : throw new ArgumentException("Nombre requerido");
        Email = email ?? throw new ArgumentNullException(nameof(email));
        FechaRegistro = DateTime.UtcNow;
    }

    // Comportamientos del dominio
    public void CambiarEmail(Email nuevoEmail)
    {
        Email = nuevoEmail;
        // Evento de dominio: EmailCambiado
    }

    public void ActualizarDireccion(Direccion nuevaDireccion)
    {
        Direccion = nuevaDireccion;
    }

    // Equals basado en identidad
    public override bool Equals(object obj)
    {
        if (obj is not Cliente other) return false;
        return Id.Equals(other.Id);
    }

    public override int GetHashCode() => Id.GetHashCode();
}
```

---

## Value Object en C#

```csharp
// VALUE OBJECT: Dinero
// Definido completamente por sus atributos

public class Dinero : IEquatable<Dinero>
{
    public decimal Monto { get; }
    public string Moneda { get; }  // USD, EUR, COP

    public Dinero(decimal monto, string moneda)
    {
        if (monto < 0) throw new ArgumentException("Monto no puede ser negativo");
        Monto = monto;
        Moneda = !string.IsNullOrEmpty(moneda) ? moneda
            : throw new ArgumentException("Moneda requerida");
    }

    // Inmutable: operaciones retornan nuevas instancias
    public Dinero Sumar(Dinero otro)
    {
        if (Moneda != otro.Moneda)
            throw new InvalidOperationException("No se pueden sumar monedas diferentes");
        return new Dinero(Monto + otro.Monto, Moneda);
    }

    public Dinero AplicarDescuento(decimal porcentaje)
    {
        var descuento = Monto * (porcentaje / 100);
        return new Dinero(Monto - descuento, Moneda);
    }

    // Comparación por valor (todos los atributos)
    public bool Equals(Dinero otro)
    {
        if (otro is null) return false;
        return Monto == otro.Monto && Moneda == otro.Moneda;
    }

    public override bool Equals(object obj) => Equals(obj as Dinero);
    public override int GetHashCode() => HashCode.Combine(Monto, Moneda);

    // Factory methods
    public static Dinero Pesos(decimal monto) => new Dinero(monto, "COP");
    public static Dinero Dolares(decimal monto) => new Dinero(monto, "USD");
}
```

---

## Value Object: Dirección

```csharp
public class Direccion : IEquatable<Direccion>
{
    public string Calle { get; }
    public string Ciudad { get; }
    public string CodigoPostal { get; }
    public string Pais { get; }

    public Direccion(string calle, string ciudad, string codigoPostal, string pais)
    {
        Calle = calle;
        Ciudad = ciudad;
        CodigoPostal = codigoPostal;
        Pais = pais;
    }

    // Value Objects son inmutables
    // Si cambia algo, se crea una nueva instancia
    public Direccion CambiarCalle(string nuevaCalle)
    {
        return new Direccion(nuevaCalle, Ciudad, CodigoPostal, Pais);
    }

    public bool Equals(Direccion otro)
    {
        if (otro is null) return false;
        return Calle == otro.Calle &&
               Ciudad == otro.Ciudad &&
               CodigoPostal == otro.CodigoPostal &&
               Pais == otro.Pais;
    }

    public override string ToString()
    {
        return $"{Calle}, {Ciudad}, {CodigoPostal}, {Pais}";
    }
}

// Uso
var direccion1 = new Direccion("Calle 123", "Medellín", "050001", "Colombia");
var direccion2 = new Direccion("Calle 123", "Medellín", "050001", "Colombia");

Console.WriteLine(direccion1.Equals(direccion2));  // True (mismo valor)
```

---

## 4. Aggregates y Aggregate Roots

### 📦 Concepto

```
┌─────────────────────────────────────────────────────────────┐
│                    AGGREGATE PATTERN                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   AGGREGATE = Grupo de Entities y Value Objects que        │
│   se tratan como una unidad para cambios de datos          │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │              AGGREGATE: Pedido                      │   │
│   │                                                     │   │
│   │  ┌─────────────────────────────────────────────┐   │   │
│   │  │       AGGREGATE ROOT: Pedido                │   │   │
│   │  │       (Entity - tiene ID)                   │   │   │
│   │  │                                             │   │   │
│   │  │  Id: PedidoId                               │   │   │
│   │  │  Fecha: DateTime                            │   │   │
│   │  │  Estado: EstadoPedido                       │   │   │
│   │  │  Total: Dinero                              │   │   │
│   │  │  ClienteId: ClienteId  ← Referencia externa │   │   │
│   │  │                                             │   │   │
│   │  └─────────────────────────────────────────────┘   │   │
│   │            │                                      │   │
│   │            ▼                                      │   │
│   │  ┌─────────────────────────────────────────────┐   │   │
│   │  │   ENTITIES INTERNAS: LíneaPedido            │   │   │
│   │  │   (solo accesibles vía Pedido)              │   │   │
│   │  │                                             │   │   │
│   │  │  • LíneaPedido 1: Producto X, Cantidad 2   │   │   │
│   │  │  • LíneaPedido 2: Producto Y, Cantidad 1   │   │   │
│   │  │                                             │   │   │
│   │  └─────────────────────────────────────────────┘   │   │
│   │                                                     │   │
│   │  FRONTERA DEL AGGREGATE: Solo el Root es           │   │
│   │  accesible desde fuera. Las líneas se acceden      │   │
│   │  mediante el pedido.                               │   │
│   │                                                     │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Reglas de los Aggregates

### 📋 Invariantes y Consistencia

| Regla | Descripción |
|-------|-------------|
| **1️⃣ Solo el Root es accesible desde fuera** | Las entidades internas se modifican mediante métodos del Aggregate Root |
| **2️⃣ Referencias entre Aggregates por ID** | No guardar objetos completos de otros aggregates |
| **3️⃣ Una transacción modifica un solo Aggregate** | Mantiene consistencia y reduce locking |

### Ejemplo de las Reglas

```csharp
// ✅ Correcto
var pedido = repositorio.Obtener(pedidoId);
pedido.AgregarProducto(producto, cantidad);

// ❌ Incorrecto (rompe encapsulamiento)
var linea = pedido.Lineas[0];  // Acceso directo
linea.Cantidad = 100;          // Modificación externa

// ✅ Correcto: Referencia por ID
public class Pedido {
    public ClienteId ClienteId { get; }  // ✅ Por ID
    // NO: public Cliente Cliente { get; }  // ❌ Objeto completo
}
```

---

## Implementación: Aggregate Root Pedido

```csharp
// AGGREGATE ROOT
public class Pedido
{
    public PedidoId Id { get; private set; }
    public ClienteId ClienteId { get; private set; }
    public DateTime Fecha { get; private set; }
    public EstadoPedido Estado { get; private set; }
    public Direccion DireccionEntrega { get; private set; }

    // Colección interna - solo modificable mediante métodos
    private readonly List<LineaPedido> _lineas;
    public IReadOnlyCollection<LineaPedido> Lineas => _lineas.AsReadOnly();

    // Constructor
    public Pedido(PedidoId id, ClienteId clienteId, Direccion direccion)
    {
        Id = id;
        ClienteId = clienteId;
        DireccionEntrega = direccion;
        Fecha = DateTime.UtcNow;
        Estado = EstadoPedido.Pendiente;
        _lineas = new List<LineaPedido>();
    }

    // Comportamiento del dominio
    public void AgregarProducto(ProductoId productoId, string nombreProducto,
                                 int cantidad, Dinero precioUnitario)
    {
        if (Estado != EstadoPedido.Pendiente)
            throw new InvalidOperationException("Solo se pueden modificar pedidos pendientes");

        if (cantidad <= 0)
            throw new ArgumentException("Cantidad debe ser positiva");

        var linea = new LineaPedido(productoId, nombreProducto, cantidad, precioUnitario);
        _lineas.Add(linea);
    }

    public Dinero CalcularTotal()
    {
        return _lineas.Aggregate(
            Dinero.Pesos(0),
            (total, linea) => total.Sumar(linea.Subtotal)
        );
    }

    public void Confirmar()
    {
        if (_lineas.Count == 0)
            throw new InvalidOperationException("No se puede confirmar pedido vacío");

        Estado = EstadoPedido.Confirmado;
    }
}
```

---

## Entity dentro del Aggregate

```csharp
// ENTITY INTERNA: Solo accesible a través del Pedido
public class LineaPedido
{
    public ProductoId ProductoId { get; private set; }
    public string NombreProducto { get; private set; }
    public int Cantidad { get; private set; }
    public Dinero PrecioUnitario { get; private set; }

    public Dinero Subtotal => PrecioUnitario.Multiplicar(Cantidad);

    public LineaPedido(ProductoId productoId, string nombreProducto,
                       int cantidad, Dinero precioUnitario)
    {
        ProductoId = productoId;
        NombreProducto = nombreProducto;
        Cantidad = cantidad;
        PrecioUnitario = precioUnitario;
    }
}

public enum EstadoPedido
{
    Pendiente,
    Confirmado,
    Pagado,
    Enviado,
    Entregado,
    Cancelado
}
```

---

## 5. Repositories y Domain Services

### 📊 Comparativa

| Aspecto | **REPOSITORY** | **DOMAIN SERVICE** |
|---------|----------------|-------------------|
| **Responsabilidad** | Persistencia de Aggregates | Lógica de negocio que cruza aggregates |
| **Operaciones** | Guardar, Obtener, Buscar, Eliminar | Calcular impuestos, Validar reglas complejas |
| **Ubicación** | Interfaz en Domain, Impl en Infrastructure | En Domain |
| **Estado** | Maneja estado de persistencia | Stateless (sin estado) |

### Ejemplos

| Repository | Domain Service |
|------------|----------------|
| IPedidoRepository | CalculadoraDescuentos |
| IClienteRepository | ProcesadorPagos |
| IProductoRepository | ValidadorInventario |

---

## Repository Pattern en C#

```csharp
// INTERFAZ EN DOMAIN (Capa de Dominio)
// El dominio no sabe CÓMO se persiste, solo QUÉ operaciones existen

public interface IPedidoRepository
{
    Task<Pedido> ObtenerAsync(PedidoId id);
    Task<IEnumerable<Pedido>> ObtenerPorClienteAsync(ClienteId clienteId);
    Task<IEnumerable<Pedido>> ObtenerPendientesAsync();
    Task GuardarAsync(Pedido pedido);
    Task EliminarAsync(PedidoId id);
}

// IMPLEMENTACIÓN EN INFRASTRUCTURE
public class PedidoRepository : IPedidoRepository
{
    private readonly AppDbContext _context;

    public PedidoRepository(AppDbContext context)
    {
        _context = context;
    }

    public async Task<Pedido> ObtenerAsync(PedidoId id)
    {
        return await _context.Pedidos
            .Include(p => p.Lineas)
            .FirstOrDefaultAsync(p => p.Id == id);
    }

    public async Task GuardarAsync(Pedido pedido)
    {
        _context.Pedidos.Update(pedido);
        await _context.SaveChangesAsync();
    }

    // ... otros métodos
}
```

---

## Domain Service en C#

```csharp
// DOMAIN SERVICE: Lógica de negocio que involucra múltiples aggregates
// No tiene estado propio

public class ProcesadorPedidos
{
    private readonly IPedidoRepository _pedidoRepo;
    private readonly IInventarioService _inventario;
    private readonly IProcesadorPagos _pagos;

    public ProcesadorPedidos(
        IPedidoRepository pedidoRepo,
        IInventarioService inventario,
        IProcesadorPagos pagos)
    {
        _pedidoRepo = pedidoRepo;
        _inventario = inventario;
        _pagos = pagos;
    }

    public async Task<ResultadoProcesamiento> ProcesarPedido(PedidoId pedidoId)
    {
        var pedido = await _pedidoRepo.ObtenerAsync(pedidoId);
        if (pedido == null)
            return ResultadoProcesamiento.Error("Pedido no encontrado");

        // 1. Verificar inventario
        foreach (var linea in pedido.Lineas)
        {
            var disponible = await _inventario.VerificarDisponibilidad(
                linea.ProductoId, linea.Cantidad);

            if (!disponible)
                return ResultadoProcesamiento.Error(
                    $"Producto {linea.NombreProducto} sin stock");
        }

        // 2. Procesar pago
        var total = pedido.CalcularTotal();
        var pagoResult = await _pagos.Procesar(pedido.ClienteId, total);

        if (!pagoResult.Exitoso)
            return ResultadoProcesamiento.Error("Pago rechazado");

        // 3. Confirmar pedido
        pedido.Confirmar();
        await _pedidoRepo.GuardarAsync(pedido);

        // 4. Reservar inventario
        foreach (var linea in pedido.Lineas)
        {
            await _inventario.Reservar(linea.ProductoId, linea.Cantidad);
        }

        return ResultadoProcesamiento.Exito(pedidoId);
    }
}
```

---

## 6. Arquitectura en Capas DDD

```
┌─────────────────────────────────────────────────────────────┐
│                 ARQUITECTURA EN CAPAS DDD                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │                   PRESENTATION                         │ │
│  │              (Controllers, Views, API)                 │ │
│  │                                                      │ │
│  │   • ASP.NET Controllers                              │ │
│  │   • DTOs (Data Transfer Objects)                     │ │
│  │   • Validación de entrada                            │ │
│  └───────────────────────┬───────────────────────────────┘ │
│                          │                                  │
│  ┌───────────────────────▼───────────────────────────────┐ │
│  │                  APPLICATION                           │ │
│  │         (Casos de uso, Servicios de aplicación)        │ │
│  │                                                      │ │
│  │   • Commands/Queries (CQRS opcional)                 │ │
│  │   • Application Services                             │ │
│  │   • Mapeo DTO ↔ Domain                               │ │
│  └───────────────────────┬───────────────────────────────┘ │
│                          │                                  │
│  ┌───────────────────────▼───────────────────────────────┐ │
│  │                     DOMAIN                             │ │
│  │      (Entities, Value Objects, Aggregates, Services)   │ │
│  │                                                      │ │
│  │   • Lógica de negocio pura                           │ │
│  │   • No depende de frameworks externos                │ │
│  │   • Interfaces de Repositories                       │ │
│  └───────────────────────┬───────────────────────────────┘ │
│                          │                                  │
│  ┌───────────────────────▼───────────────────────────────┐ │
│  │                 INFRASTRUCTURE                         │ │
│  │   (Persistencia, External Services, Logging)           │ │
│  │                                                      │ │
│  │   • EF Core / ADO.NET                                │ │
│  │   • Implementación de Repositories                   │ │
│  │   • Servicios externos (email, SMS, etc.)            │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  ↓ Flujo de dependencias (Domain no depende de nadie)      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Regla de Dependencia

```
┌─────────────────────────────────────────────────────────────┐
│              REGLA DE DEPENDENCIA                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   "Las dependencias apuntan siempre hacia el centro"       │
│                                                             │
│   Presentation ───────────────────────────────┐            │
│        ↓                                       │            │
│   Application ────────────────────────────────┤            │
│        ↓                                       │ Solo usa    │
│   Domain ◄────────────────────────────────────┤ interfaces  │
│        ↓                                       │            │
│   Infrastructure ─────────────────────────────┘            │
│                                                             │
│   ❌ PROHIBIDO:                                            │
│   • Domain referencia Application                         │
│   • Domain referencia Infrastructure                      │
│   • Application referencia Presentation                   │
│                                                             │
│   ✅ PERMITIDO:                                            │
│   • Presentation referencia Application                   │
│   • Application referencia Domain                         │
│   • Infrastructure implementa interfaces de Domain        │
│   • Infrastructure usa Application (inyección)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Ejemplo Completo: Application Layer

```csharp
// ==================== APPLICATION ====================

// Command (para operaciones que modifican datos)
public class RealizarPedidoCommand
{
    public ClienteId ClienteId { get; set; }
    public List<ItemPedidoDto> Items { get; set; }
    public DireccionDto DireccionEntrega { get; set; }
}

// Command Handler
public class RealizarPedidoHandler
{
    private readonly IPedidoRepository _pedidoRepo;
    private readonly IProductoRepository _productoRepo;

    public async Task<PedidoId> Handle(RealizarPedidoCommand command)
    {
        // Crear pedido
        var pedidoId = new PedidoId(Guid.NewGuid());
        var direccion = new Direccion(
            command.DireccionEntrega.Calle,
            command.DireccionEntrega.Ciudad,
            command.DireccionEntrega.CodigoPostal,
            command.DireccionEntrega.Pais
        );

        var pedido = new Pedido(pedidoId, command.ClienteId, direccion);

        // Agregar productos
        foreach (var item in command.Items)
        {
            var producto = await _productoRepo.ObtenerAsync(item.ProductoId);
            if (producto == null)
                throw new ArgumentException($"Producto {item.ProductoId} no existe");

            pedido.AgregarProducto(
                producto.Id,
                producto.Nombre,
                item.Cantidad,
                producto.Precio
            );
        }

        // Guardar
        await _pedidoRepo.GuardarAsync(pedido);
        return pedidoId;
    }
}
```

---

## Ejemplo: Presentation Layer

```csharp
// ==================== PRESENTATION ====================

[ApiController]
[Route("api/[controller]")]
public class PedidosController : ControllerBase
{
    private readonly RealizarPedidoHandler _realizarPedidoHandler;

    public PedidosController(RealizarPedidoHandler realizarPedidoHandler)
    {
        _realizarPedidoHandler = realizarPedidoHandler;
    }

    [HttpPost]
    public async Task<ActionResult> CrearPedido([FromBody] CrearPedidoRequest request)
    {
        // Mapear Request → Command
        var command = new RealizarPedidoCommand
        {
            ClienteId = new ClienteId(request.ClienteId),
            Items = request.Items.Select(i => new ItemPedidoDto
            {
                ProductoId = new ProductoId(i.ProductoId),
                Cantidad = i.Cantidad
            }).ToList(),
            DireccionEntrega = new DireccionDto
            {
                Calle = request.Direccion.Calle,
                Ciudad = request.Direccion.Ciudad,
                CodigoPostal = request.Direccion.CodigoPostal,
                Pais = request.Direccion.Pais
            }
        };

        // Ejecutar
        var pedidoId = await _realizarPedidoHandler.Handle(command);

        return CreatedAtAction(nameof(ObtenerPedido),
            new { id = pedidoId.Value },
            new { Id = pedidoId.Value });
    }
}
```

---

## Bounded Contexts

```
┌─────────────────────────────────────────────────────────────┐
│                  BOUNDED CONTEXTS                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Un Bounded Context es un límite conceptual y técnico      │
│   donde un modelo de dominio es válido y aplicable          │
│                                                             │
│   EJEMPLO: Tienda en línea                                  │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                                                     │   │
│   │  ┌─────────────┐  ┌─────────────┐  ┌───────────┐  │   │
│   │  │   VENTAS    │  │  INVENTARIO │  │  ENVÍOS   │  │   │
│   │  │             │  │             │  │           │  │   │
│   │  │ • Pedido    │  │ • Stock     │  │ • Envío   │  │   │
│   │  │ • Cliente   │  │ • Producto  │  │ • Tracking│  │   │
│   │  │ • Factura   │  │ • Almacén   │  │ • Courier │  │   │
│   │  │             │  │             │  │           │  │   │
│   │  │ Context:    │  │ Context:    │  │ Context:  │  │   │
│   │  │ "Ventas"    │  │ "Stock"     │  │ "Logística"│  │   │
│   │  └─────────────┘  └─────────────┘  └───────────┘  │   │
│   │                                                     │   │
│   │  Nota: "Producto" significa cosas diferentes        │   │
│   │  en cada contexto (en Ventas: precio+descripcion,  │   │
│   │  en Inventario: stock+ubicación)                   │   │
│   │                                                     │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Domain Events

```csharp
// DOMINIO: Eventos que representan hechos ocurridos
// Los eventos son INMUTABLES y representan algo que ya pasó

public abstract record DomainEvent
{
    public DateTime OccurredOn { get; } = DateTime.UtcNow;
}

// Eventos específicos del dominio
public record PedidoCreadoEvent(PedidoId PedidoId, ClienteId ClienteId, DateTime Fecha)
    : DomainEvent;

public record PagadoEvent(PedidoId PedidoId, Dinero Monto, DateTime FechaPago)
    : DomainEvent;

public record EnviadoEvent(PedidoId PedidoId, string NumeroGuia, DateTime FechaEnvio)
    : DomainEvent;

// AGGREGATE ROOT con soporte de eventos
public abstract class AggregateRoot<TId>
{
    private readonly List<DomainEvent> _domainEvents = new();
    public IReadOnlyCollection<DomainEvent> DomainEvents => _domainEvents.AsReadOnly();

    protected void RaiseEvent(DomainEvent domainEvent)
    {
        _domainEvents.Add(domainEvent);
    }

    public void ClearDomainEvents() => _domainEvents.Clear();
}

// Pedido con eventos
public class Pedido : AggregateRoot<PedidoId>
{
    public void Confirmar()
    {
        if (_lineas.Count == 0)
            throw new InvalidOperationException("No se puede confirmar pedido vacío");

        Estado = EstadoPedido.Confirmado;

        // Publicar evento de dominio
        RaiseEvent(new PedidoConfirmadoEvent(Id, ClienteId, DateTime.UtcNow));
    }
}
```

---

## CQRS con DDD

```
┌─────────────────────────────────────────────────────────────┐
│                    CQRS + DDD                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   CQRS: Separar operaciones de lectura (Query)              │
│   de operaciones de escritura (Command)                     │
│                                                             │
│   ┌────────────────────────────────────────────────────┐    │
│   │                    CLIENT                           │    │
│   └───────────────────┬────────────────────────────────┘    │
│                       │                                     │
│           ┌───────────┴───────────┐                         │
│           │                       │                         │
│           ▼                       ▼                         │
│   ┌───────────────┐       ┌───────────────┐                │
│   │   COMMANDS    │       │    QUERIES    │                │
│   │  (Escribir)   │       │   (Leer)     │                │
│   │               │       │               │                │
│   │ CrearPedido   │       │ ObtenerPedido │                │
│   │ ConfirmarPago │       │ ListarPedidos │                │
│   │ CancelarPedido│       │ BuscarPorEstado│                │
│   └───────┬───────┘       └───────┬───────┘                │
│           │                       │                         │
│           ▼                       ▼                         │
│   ┌───────────────┐       ┌───────────────┐                │
│   │  WRITE MODEL  │       │  READ MODEL   │                │
│   │   (Domain)    │       │ (Proyecciones)│                │
│   │               │       │               │                │
│   │ DDD Aggregates│       │ DTOs planos   │                │
│   │ Entities      │       │ Optimizados   │                │
│   │ Value Objects │       │ para queries  │                │
│   │               │       │               │                │
│   │ DB Principal  │       │ DB Lectura    │                │
│   │ (Normalizada) │       │ (Denormalizada)│                │
│   └───────────────┘       └───────────────┘                │
│                                                             │
│   Ventajas:                                                 │
│   • Modelo de escritura optimizado para validaciones        │
│   • Modelo de lectura optimizado para presentación          │
│   • Escalabilidad independiente (lectura >> escritura)      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Resumen de DDD

| Concepto | Descripción |
|----------|-------------|
| **Ubiquitous Language** | Lenguaje compartido entre técnicos y negocio |
| **Entity** | Objeto con identidad única |
| **Value Object** | Objeto definido por sus atributos, inmutable |
| **Aggregate** | Grupo de objetos tratados como unidad |
| **Aggregate Root** | Único punto de entrada al aggregate |
| **Repository** | Abstracción de persistencia |
| **Domain Service** | Lógica de negocio que cruza aggregates |
| **Bounded Context** | Límite del dominio (microservicio, módulo) |
| **Domain Events** | Eventos que representan hechos ocurridos |
| **CQRS** | Separación de lecturas y escrituras |

---

## Cuándo NO usar DDD

### ❌ Evitar Over-engineering

| Situación | Razón |
|-----------|-------|
| **CRUD simple** | Solo guardar y leer datos, sin lógica de negocio |
| **Proyectos cortos** | < 2 meses, el overhead no se justifica |
| **Sin expertos** | No hay quién defina el lenguaje ubicuo |
| **Tecnología > Negocio** | Proyectos de investigación tecnológica |
| **Reportes simples** | Solo consultas a base de datos |

### ✅ Alternativas más simples
- Transaction Script
- Active Record
- Simple CRUD con validaciones

---

## Ejercicio Práctico

### 📋 Diseñar modelo DDD para Biblioteca

**Requisitos:**
- Usuarios pueden solicitar préstamos
- Cada libro tiene ejemplares físicos
- Un usuario puede tener máximo 3 préstamos activos
- Los préstamos tienen fecha de devolución
- Multa de $1000 por día de retraso
- El bibliotecario puede renovar préstamos

**Tareas:**
1. Identificar Entities y Value Objects
2. Definir Aggregates y sus roots
3. Crear Repository interfaces
4. Identificar posibles Domain Services

**Preguntas guía:**
- ¿Es Usuario un Entity o Value Object?
- ¿Cuál es el Aggregate Root: Prestamo o Libro?
- ¿Dónde va la lógica de la multa?

---

## 🚀 Próxima Clase: ASP.NET Core

| Tema | Descripción |
|------|-------------|
| **ASP.NET Core** | Framework web moderno |
| **MVC** | Model-View-Controller |
| **Razor Pages** | Page-focused programming |
| **HTML5 + Bootstrap** | Frontend moderno |

---

## Evaluación 2 (15%) - Semana 7

### 📝 Laboratorio + Sustentación

**Formato:**
- Desarrollar sistema con TDD/BDD
- Pruebas unitarias con xUnit
- Al menos 2 escenarios SpecFlow
- Implementar mínimo 1 Aggregate con DDD

**Sustentación:**
- Explicar decisiones de diseño
- Mostrar cobertura de pruebas
- Justificar uso de Entities vs Value Objects

**Trabajo en parejas**

---

# ¡Gracias!
## ¿Preguntas?

**"El software es una representación del dominio del negocio"**

**UNAULA - Ingeniería Informática - 2026-I**
