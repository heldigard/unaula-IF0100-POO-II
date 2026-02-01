# Teoría - Archivos Planos

**IF0100 - Lenguaje de Programación OO II**

---

## Archivos Planos

### Formatos Comunes

| Formato | Ventajas | Desventajas |
|---------|----------|-------------|
| **CSV** | Simple, Excel-compatible | No soporta datos complejos |
| **JSON** | Estructurado, legible | Más verboso |
| **XML** | Estandarizado, schema | Verboso, complejo |

---

## System.IO

### Clases Principales

| Clase | Propósito |
|-------|-----------|
| **File** | Métodos estáticos para archivos |
| **Directory** | Métodos estáticos para directorios |
| **StreamReader** | Lectura de texto |
| **StreamWriter** | Escritura de texto |
| **FileStream** | Lectura/escritura binaria |

---

## Serialización JSON

```csharp
using System.Text.Json;

// Serializar
string json = JsonSerializer.Serialize(objeto);

// Deserializar
var objeto = JsonSerializer.Deserialize<Tipo>(json);
```

---

**Última actualización:** 2026-02-01
