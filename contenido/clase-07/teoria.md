# Teoría - Domain Driven Design

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es DDD?

**Domain Driven Design** es una metodología que centra el desarrollo en el **dominio del negocio**, usando su lenguaje y conceptos.

### Estrategia vs Dominio

```
ESTRATEGIA           DOMINIO
├─ Visión            ├─ Entidades
├─ Objetivos         ├─ Value Objects
└─ Planes            ├─ Agregados
                     ├─ Repositorios
                     └─ Servicios de Dominio
```

---

## 2. Patrones Fundamentales

### Entidad (Entity)

| Característica | Descripción |
|----------------|-------------|
| **Identidad única** | Tiene ID que la distingue |
| **Ciclo de vida** | Persiste en el tiempo |
| **Igualdad** | Por ID, no por atributos |

```csharp
public class Estudiante  // Entidad
{
    public string Codigo { get; }  // Identidad
    public string Nombre { get; set; }

    // Igualdad por identidad
    public override bool Equals(object obj)
        => obj is Estudiante e && Codigo == e.Codigo;
}
```

### Value Object

| Característica | Descripción |
|----------------|-------------|
| **Sin identidad** | No tiene ID |
| **Inmutable** | No cambia después de crear |
| **Igualdad** | Por todos sus atributos |

```csharp
public record Dinero(decimal Monto, string Moneda);  // Value Object
```

### Agregado (Aggregate)

```
┌──────────────────────┐
│      PEDIDO          │ ← Agregado Root
│  ├── Id              │
│  ├── Fecha           │
│  └── LineasPedido[]  │ ← Entidades internas
│      ├── Producto
│      ├── Cantidad
│      └── Precio
└──────────────────────┘
```

---

## 3. Bounded Contexts

Dividir el dominio en contexts con límites claros:

```
VENTAS          INVENTARIO        CONTABILIDAD
├─ Pedido       ├─ Producto       ├─ Factura
├─ Cliente      ├─ Stock         ├─ Asiento
└─ Descuento    └─ Almacén        └─ Cuenta
```

---

**Última actualización:** 2026-02-01
