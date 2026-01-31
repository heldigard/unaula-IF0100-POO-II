---
marp: true
theme: default
paginate: true
| header: 'IF0100 - Lenguaje de Programación OO II | Unidad 4' |
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
  display: block !important;
  margin: 0 auto !important;
}
section {
  font-size: 20px;
  overflow: hidden;
}
section h1 {
  font-size: 1.8em;
}
section h2 {
  font-size: 1.4em;
}
section h3 {
  font-size: 1.2em;
}
section ul, section ol {
  font-size: 0.9em;
  margin-left: 1em;
}
section li {
  margin-bottom: 0.3em;
}
section pre {
  font-size: 0.7em;
  max-height: 60vh;
  overflow-y: auto;
}
section code {
  font-size: 0.85em;
}
section p {
  margin: 0.5em 0;
}
/* Estilos para tablas responsivas */
section table {
  width: 100%;
  max-width: 100%;
  font-size: 0.85em;
  border-collapse: collapse;
  margin: 0.5em auto;
  table-layout: auto;
}
---
## TXT, CSV y JSON en C#
section th {
  background-color: #1e40af;
  color: white;
  padding: 0.4em 0.6em;
  text-align: left;
  font-size: 0.9em;
  border: 1px solid #ddd;
}
section td {
  padding: 0.4em 0.6em;
  border: 1px solid #ddd;
  vertical-align: top;
  word-wrap: break-word;
  font-size: 0.85em;
}
section tbody tr:nth-child(even) {
  background-color: #f8f9fa;
}
section tbody tr:hover {
  background-color: #e9ecef;
}
/* Asegurar que el contenido no desborde */
section {
  padding: 1em 2em;
  box-sizing: border-box;
}
/* Responsividad para tablas anchas */
@media screen and (max-width: 1280px) {
  section table {
    font-size: 0.75em;
  }
  section th, section td {
    padding: 0.3em 0.4em;
  }
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
| ------ | --------------- | ---- |
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
| ---------- | ------------ |
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
