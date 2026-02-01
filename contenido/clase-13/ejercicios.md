# Ejercicios - CRUD ADO.NET

**IF0100 - Lenguaje de Programación OO II**

---

## Ejercicio 1: CRUD Productos

Implementar repositorio completo para Productos:
- GetAll
- GetById
- Insert
- Update
- Delete

---

## Ejercicio 2: Búsqueda con Filtros

```sql
SELECT * FROM Productos
WHERE (@Nombre IS NULL OR Nombre LIKE '%' + @Nombre + '%')
AND (@PrecioMin IS NULL OR Precio >= @PrecioMin)
```

---

**Última actualización:** 2026-02-01
