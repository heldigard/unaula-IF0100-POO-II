# Teoría - ADO.NET

**IF0100 - Lenguaje de Programación OO II**

---

## ¿Qué es ADO.NET?

Framework de acceso a datos de .NET para conectarse a bases de datos.

### Arquitectura

```
┌─────────────────────────────────────┐
│         APLICACIÓN .NET             │
├─────────────────────────────────────┤
│  ADO.NET                            │
│  ┌───────────────────────────────┐ │
│  │ Connection (SqlConnection)    │ │
│  │ Command (SqlCommand)          │ │
│  │ DataReader (SqlDataReader)    │ │
│  │ DataSet/DataTable             │ │
│  └───────────────────────────────┘ │
├─────────────────────────────────────┤
│  Data Provider (System.Data.SqlClient)│
├─────────────────────────────────────┤
│  SQL Server / OLE DB / ODBC         │
└─────────────────────────────────────┘
```

### Objetos Principales

| Objeto | Propósito |
|--------|-----------|
| **Connection** | Abrir conexión a BD |
| **Command** | Ejecutar SQL |
| **DataReader** | Lectura forward-only, rápido |
| **DataAdapter** | Llenar DataSet, desconectado |
| **DataSet** | Tablas en memoria, desconectado |

---

## Connection String

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=MiDB;User Id=sa;Password=Password123;TrustServerCertificate=True;"
  }
}
```

---

**Última actualización:** 2026-02-01
