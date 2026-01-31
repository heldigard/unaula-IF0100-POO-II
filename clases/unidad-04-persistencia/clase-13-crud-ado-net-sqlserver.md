---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 4'
footer: 'UNAULA - Ingeniería Informática - 2026-I'

  section {
    font-size: 24px;
  }

---
<style>
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
}
section {
  font-size: 24px;
}
</style>


<!--
IMÁGENES GENERADAS:
- clase-13-crud.png: Operaciones CRUD en ADO.NET
-->

# Clase 13: CRUD con ADO.NET y SQL Server
## Conexión, comandos y transacciones

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos

Al finalizar esta clase, el estudiante será capaz de:

1. **Configurar** una conexión a SQL Server
2. **Ejecutar** operaciones CRUD con ADO.NET
3. **Usar** parámetros para evitar SQL Injection
4. **Aplicar** transacciones básicas

**Duración:** 90 minutos

---

## Agenda

1. Conexión a SQL Server (15 min)
2. SqlCommand y parámetros (25 min)
3. CRUD completo (30 min)
4. Transacciones (10 min)
5. Actividad práctica (10 min)

---

## 1. Conexión

```csharp
using System.Data.SqlClient;

var cs = "Server=localhost;Database=tienda;Trusted_Connection=True;";
using var conn = new SqlConnection(cs);
conn.Open();
```

---

## 2. Comandos con parámetros

```csharp
string sql = "INSERT INTO Productos (Nombre, Precio) VALUES (@n, @p)";
using var cmd = new SqlCommand(sql, conn);
cmd.Parameters.AddWithValue("@n", nombre);
cmd.Parameters.AddWithValue("@p", precio);
cmd.ExecuteNonQuery();
```

---

## 3. CRUD básico

- **Create**: INSERT
- **Read**: SELECT + SqlDataReader
- **Update**: UPDATE
- **Delete**: DELETE

```csharp
string sql = "SELECT Id, Nombre, Precio FROM Productos";
using var cmd = new SqlCommand(sql, conn);
using var reader = cmd.ExecuteReader();
while (reader.Read())
{
    Console.WriteLine($"{reader["Id"]} {reader["Nombre"]}");
}
```

---

## 4. Transacciones

```csharp
using var tx = conn.BeginTransaction();
try
{
    var cmd = new SqlCommand(sql, conn, tx);
    cmd.ExecuteNonQuery();
    tx.Commit();
}
catch
{
    tx.Rollback();
}
```

---

## Actividad (10 min)

En parejas:
1. Crear tabla `Clientes`
2. Insertar 3 registros
3. Consultar y mostrar resultados

---

## Resumen

| Concepto | Idea clave |
|----------|------------|
| SqlConnection | Abre canal con DB |
| SqlCommand | Ejecuta SQL |
| Parámetros | Seguridad |
| Transacciones | Consistencia |

---

## Próxima Clase

### Clase 14: Persistencia en Archivos Planos

- Lectura/escritura
- CSV/JSON
- Serialización

**¡Nos vemos!**
