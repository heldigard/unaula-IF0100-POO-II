# Ejercicios - ADO.NET

**IF0100 - Lenguaje de Programación OO II**

---

## Ejercicio 1: CRUD Completo

- Create: Insertar con parámetros
- Read: Consultar con DataReader
- Update: Actualizar registro
- Delete: Eliminar con parámetro

---

## Ejercicio 2: Transacciones

```csharp
using (var transaction = connection.BeginTransaction())
{
    try
    {
        // Múltiples operaciones
        transaction.Commit();
    }
    catch
    {
        transaction.Rollback();
    }
}
```

---

**Última actualización:** 2026-02-01
