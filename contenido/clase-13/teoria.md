# Teoría - CRUD ADO.NET

**IF0100 - Lenguaje de Programación OO II**

---

## Operaciones CRUD

| Operación | SQL | ADO.NET |
|-----------|-----|---------|
| **Create** | INSERT | ExecuteNonQuery |
| **Read** | SELECT | ExecuteReader / ExecuteScalar |
| **Update** | UPDATE | ExecuteNonQuery |
| **Delete** | DELETE | ExecuteNonQuery |

---

## Patrón Repository

```csharp
public interface IEstudianteRepository
{
    IEnumerable<Estudiante> GetAll();
    Estudiante? GetById(string codigo);
    void Insert(Estudiante estudiante);
    void Update(Estudiante estudiante);
    void Delete(string codigo);
}
```

---

## Mejores Prácticas

1. **Usar parámetros** - Previene SQL Injection
2. **Using statements** - Libera recursos
3. **Transacciones** - Para operaciones atómicas
4. **Connection pooling** - Reutiliza conexiones

---

**Última actualización:** 2026-02-01
