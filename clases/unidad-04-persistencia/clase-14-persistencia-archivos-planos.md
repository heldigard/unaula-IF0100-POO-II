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
- clase-14-formatos-archivo.png: Comparación de formatos JSON, CSV y XML
-->

# Clase 14: Persistencia en Archivos Planos
## TXT, CSV y JSON en C#

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## Objetivos

Al finalizar esta clase, el estudiante será capaz de:

1. **Leer y escribir** archivos de texto en C#
2. **Manipular** CSV con estructuras básicas
3. **Serializar** objetos a JSON
4. **Comparar** archivos planos vs bases de datos

**Duración:** 90 minutos

---

## Agenda

1. System.IO básico (20 min)
2. CSV: formato y lectura (20 min)
3. JSON: serialización (30 min)
4. Buenas prácticas (10 min)
5. Actividad (10 min)

---

## 1. Lectura y escritura

```csharp
using System.IO;

File.WriteAllText("datos.txt", "Hola UNAULA");
string contenido = File.ReadAllText("datos.txt");
```

---

## 2. CSV simple

```
Id,Nombre,Precio
1,Teclado,120000
2,Mouse,80000
```

```csharp
var lineas = File.ReadAllLines("productos.csv");
foreach (var l in lineas.Skip(1))
{
    var partes = l.Split(',');
}
```

---

## 3. JSON

```csharp
using System.Text.Json;

var p = new Producto { Id = 1, Nombre = "Teclado" };
string json = JsonSerializer.Serialize(p);
File.WriteAllText("producto.json", json);
```

---

## 4. ¿Cuándo usar archivos planos?

| Caso | Archivo plano | BD |
|------|---------------|----|
| Pocos datos | ✅ | ❌ |
| Multiusuario | ❌ | ✅ |
| Consultas complejas | ❌ | ✅ |
| Portabilidad | ✅ | ❌ |

---

## Actividad (10 min)

En parejas:
1. Guardar una lista de 5 productos en CSV
2. Leer el CSV y mostrarlo en consola
3. Serializar 1 producto a JSON

---

## Resumen

| Concepto | Idea clave |
|----------|------------|
| System.IO | API base de archivos |
| CSV | Datos tabulares simples |
| JSON | Intercambio estructurado |
| Persistencia | Archivos vs BD |

---

## Próxima Clase

### Clase 15: DataSet y DataAdapter

- Datos desconectados
- Navegación y edición

**¡Nos vemos!**
