---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 4'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<style>
section {
  font-size: 20px;
  overflow: hidden;
}
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
}
section h1 { font-size: 1.8em; }
section h2 { font-size: 1.4em; }
section h3 { font-size: 1.2em; }
section ul, section ol { font-size: 0.9em; margin-left: 1em; }
section li { margin-bottom: 0.3em; }
section pre { font-size: 0.7em; max-height: 60vh; overflow-y: auto; }
section code { font-size: 0.85em; }
section p { margin: 0.5em 0; }
section table { width: 100%; font-size: 0.85em; border-collapse: collapse; margin: 0.5em auto; }
section th { background-color: #1e40af; color: white; padding: 0.4em 0.6em; text-align: left; font-size: 0.9em; border: 1px solid #ddd; }
section td { padding: 0.4em 0.6em; border: 1px solid #ddd; vertical-align: top; word-wrap: break-word; font-size: 0.85em; }
section tbody tr:nth-child(even) { background-color: #f8f9fa; }
section tbody tr:hover { background-color: #e9ecef; }
</style>

---

# Persistencia en Archivos Planos

<!--
IMÁGENES GENERADAS:
- clase-14-formatos-archivo.png: Comparación de formatos JSON, CSV y XML
-->

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


---


## 📁 Persistencia con Archivos Planos en C#

### ¿Cuándo usar archivos planos?

✅ **Casos de uso adecuados:**
- Configuraciones de aplicación
- Logs y auditorías
- Exportación de datos (CSV, JSON)
- Caché simple
- Aplicaciones sin acceso a DBMS

❌ **Evitar para:**
- Grandes volúmenes de datos
- Múltiples usuarios concurrentes
- Necesidad de consultas complejas
- Alta frecuencia de escritura

---
### 2️⃣ Repository CSV - Ejemplo de Archivo


```csv
Codigo,Nombre,Apellido,Email,Promedio
EST001,Juan,Pérez,juan.perez@unaula.edu.co,4.2
EST002,María,González,maria.gonzalez@unaula.edu.co,4.5
EST003,Carlos,Ramírez,carlos.ramirez@unaula.edu.co,3.8
```

---
### 2️⃣ Repository CSV - Estructura Base

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using UniversidadApp.Models;

namespace UniversidadApp.Data
{
    public class EstudianteRepositoryCSV
    {
        private readonly string _filePath;
        private const char SEPARADOR = ',';

        public EstudianteRepositoryCSV(string filePath = "estudiantes.csv")
        {
            _filePath = filePath;
            
            // Crear archivo con encabezado si no existe
            if (!File.Exists(_filePath))
            {
                File.WriteAllText(_filePath, 
                    "Id,Codigo,Nombre,Apellido,Email,FechaNacimiento,Promedio,Activo\n");
            }
        }
```

---
### 2️⃣ Repository CSV - Método CREATE

```csharp
        public void Crear(Estudiante estudiante)
        {
            // Generar ID automático
            var estudiantes = ObtenerTodos();
            estudiante.Id = estudiantes.Any() 
                ? estudiantes.Max(e => e.Id) + 1 
                : 1;

            // Validar código único
            if (estudiantes.Any(e => e.Codigo == estudiante.Codigo))
                throw new Exception($"Ya existe un estudiante con código " +
                    $"{estudiante.Codigo}");

            // Agregar al final del archivo
            string linea = EstudianteACSV(estudiante);
            File.AppendAllText(_filePath, linea + "\n");
        }
```

---
### 2️⃣ Repository CSV - Método READ

```csharp
        public List<Estudiante> ObtenerTodos()
        {
            var estudiantes = new List<Estudiante>();
            string[] lineas = File.ReadAllLines(_filePath);

            // Saltar encabezado (primera línea)
            for (int i = 1; i < lineas.Length; i++)
            {
                if (string.IsNullOrWhiteSpace(lineas[i]))
                    continue;

                try
                {
                    var estudiante = CSVAEstudiante(lineas[i]);
                    if (estudiante.Activo)
                        estudiantes.Add(estudiante);
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error en línea {i}: {ex.Message}");
                }
            }

            return estudiantes;
        }

        public Estudiante ObtenerPorId(int id)
        {
            return ObtenerTodos().FirstOrDefault(e => e.Id == id);
        }

        public Estudiante ObtenerPorCodigo(string codigo)
        {
            return ObtenerTodos().FirstOrDefault(e => e.Codigo == codigo);
        }
```

---
### 2️⃣ Repository CSV - Métodos UPDATE y DELETE

```csharp
        public bool Actualizar(Estudiante estudiante)
        {
            var estudiantes = ObtenerTodos();
            var index = estudiantes.FindIndex(e => e.Id == estudiante.Id);

            if (index == -1)
                return false;

            estudiantes[index] = estudiante;
            GuardarTodos(estudiantes);
            return true;
        }

        public bool EliminarLogico(int id)
        {
            var estudiante = ObtenerPorId(id);
            if (estudiante == null)
                return false;

            estudiante.Activo = false;
            return Actualizar(estudiante);
        }

        public bool EliminarFisico(int id)
        {
            var estudiantes = ObtenerTodos();
            var count = estudiantes.RemoveAll(e => e.Id == id);

            if (count > 0)
            {
                GuardarTodos(estudiantes);
                return true;
            }

            return false;
        }
```

---
### 2️⃣ Repository CSV - Métodos Auxiliares (1/2)

```csharp
        private string EstudianteACSV(Estudiante e)
        {
            return $"{e.Id}{SEPARADOR}" +
                   $"{e.Codigo}{SEPARADOR}" +
                   $"\"{e.Nombre}\"{SEPARADOR}" +  // Comillas por si tiene comas
                   $"\"{e.Apellido}\"{SEPARADOR}" +
                   $"{e.Email}{SEPARADOR}" +
                   $"{e.FechaNacimiento:yyyy-MM-dd}{SEPARADOR}" +
                   $"{e.Promedio:F2}{SEPARADOR}" +
                   $"{(e.Activo ? "1" : "0")}";
        }

        private Estudiante CSVAEstudiante(string linea)
        {
            // Separar campos (considerando comillas)
            var campos = SepararCSV(linea);

            if (campos.Length < 8)
                throw new FormatException("Línea CSV incompleta");

            return new Estudiante
            {
                Id = int.Parse(campos[0]),
                Codigo = campos[1],
                Nombre = campos[2].Trim('"'),
                Apellido = campos[3].Trim('"'),
                Email = campos[4],
                FechaNacimiento = DateTime.Parse(campos[5]),
                Promedio = decimal.Parse(campos[6]),
                Activo = campos[7] == "1"
            };
        }
```

---
### 2️⃣ Repository CSV - Métodos Auxiliares (2/2)

```csharp
        private string[] SepararCSV(string linea)
        {
            // Implementación simple (no maneja todos los casos edge)
            var campos = new List<string>();
            bool dentroComillas = false;
            string campoActual = "";

            foreach (char c in linea)
            {
                if (c == '"')
                {
                    dentroComillas = !dentroComillas;
                }
                else if (c == SEPARADOR && !dentroComillas)
                {
                    campos.Add(campoActual);
                    campoActual = "";
                }
                else
                {
                    campoActual += c;
                }
            }

            campos.Add(campoActual);
            return campos.ToArray();
        }

        private void GuardarTodos(List<Estudiante> estudiantes)
        {
            var lineas = new List<string>
            {
                "Id,Codigo,Nombre,Apellido,Email,FechaNacimiento,Promedio,Activo"
            };

            lineas.AddRange(estudiantes.Select(EstudianteACSV));
            File.WriteAllLines(_filePath, lineas);
        }
    }
}
```

---
### 3️⃣ Repository JSON - Ejemplo de Archivo

```json
[
  {
    "Id": 1,
    "Codigo": "EST001",
    "Nombre": "Juan",
    "Apellido": "Pérez",
    "Email": "juan.perez@unaula.edu.co",
    "FechaNacimiento": "2000-05-15T00:00:00",
    "Promedio": 4.2,
    "Activo": true
  },
  {
    "Id": 2,
    "Codigo": "EST002",
    "Nombre": "María",
    "Apellido": "González",
    "Email": "maria.gonzalez@unaula.edu.co",
    "FechaNacimiento": "1999-08-20T00:00:00",
    "Promedio": 4.5,
    "Activo": true
  }
]
```

---
### 3️⃣ Repository JSON - Estructura Base

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;
using UniversidadApp.Models;

namespace UniversidadApp.Data
{
    public class EstudianteRepositoryJSON
    {
        private readonly string _filePath;
        private readonly JsonSerializerOptions _jsonOptions;

        public EstudianteRepositoryJSON(string filePath = "estudiantes.json")
        {
            _filePath = filePath;
            _jsonOptions = new JsonSerializerOptions
            {
                WriteIndented = true,  // Formato legible
                PropertyNamingPolicy = JsonNamingPolicy.CamelCase
            };

            // Crear archivo vacío si no existe
            if (!File.Exists(_filePath))
            {
                File.WriteAllText(_filePath, "[]");
            }
        }
```

---
### 3️⃣ Repository JSON - Método CREATE

```csharp
        public void Crear(Estudiante estudiante)
        {
            var estudiantes = ObtenerTodos();

            // Generar ID automático
            estudiante.Id = estudiantes.Any() 
                ? estudiantes.Max(e => e.Id) + 1 
                : 1;

            // Validar código único
            if (estudiantes.Any(e => e.Codigo == estudiante.Codigo))
                throw new Exception($"Ya existe un estudiante con código " +
                    $"{estudiante.Codigo}");

            estudiantes.Add(estudiante);
            GuardarTodos(estudiantes);
        }
```

---
### 3️⃣ Repository JSON - Métodos READ

```csharp
        public List<Estudiante> ObtenerTodos()
        {
            try
            {
                string json = File.ReadAllText(_filePath);
                var estudiantes = JsonSerializer
                    .Deserialize<List<Estudiante>>(json, _jsonOptions);
                return estudiantes?.Where(e => e.Activo).ToList() 
                    ?? new List<Estudiante>();
            }
            catch (JsonException ex)
            {
                Console.WriteLine($"Error al leer JSON: {ex.Message}");
                return new List<Estudiante>();
            }
        }

        public Estudiante ObtenerPorId(int id)
        {
            return ObtenerTodos().FirstOrDefault(e => e.Id == id);
        }

        public Estudiante ObtenerPorCodigo(string codigo)
        {
            return ObtenerTodos().FirstOrDefault(e => e.Codigo == codigo);
        }
```

---
### 3️⃣ Repository JSON - Métodos UPDATE y DELETE

```csharp
        public bool Actualizar(Estudiante estudiante)
        {
            var estudiantes = LeerTodos();  // Incluye inactivos
            var index = estudiantes.FindIndex(e => e.Id == estudiante.Id);

            if (index == -1)
                return false;

            estudiantes[index] = estudiante;
            GuardarTodos(estudiantes);
            return true;
        }

        public bool EliminarLogico(int id)
        {
            var estudiante = ObtenerPorId(id);
            if (estudiante == null)
                return false;

            estudiante.Activo = false;
            return Actualizar(estudiante);
        }

        public bool EliminarFisico(int id)
        {
            var estudiantes = LeerTodos();
            var count = estudiantes.RemoveAll(e => e.Id == id);

            if (count > 0)
            {
                GuardarTodos(estudiantes);
                return true;
            }

            return false;
        }
```

---
### 3️⃣ Repository JSON - Métodos Auxiliares y Backup

```csharp
        private List<Estudiante> LeerTodos()
        {
            string json = File.ReadAllText(_filePath);
            return JsonSerializer.Deserialize<List<Estudiante>>(json, _jsonOptions) 
                ?? new List<Estudiante>();
        }

        private void GuardarTodos(List<Estudiante> estudiantes)
        {
            string json = JsonSerializer.Serialize(estudiantes, _jsonOptions);
            File.WriteAllText(_filePath, json);
        }

        public void CrearBackup()
        {
            string backupPath = _filePath.Replace(".json", 
                $"_backup_{DateTime.Now:yyyyMMdd_HHmmss}.json");
            File.Copy(_filePath, backupPath);
            Console.WriteLine($"Backup creado: {backupPath}");
        }

        public void RestaurarBackup(string backupPath)
        {
            if (!File.Exists(backupPath))
                throw new FileNotFoundException("Archivo de backup no encontrado");

            File.Copy(backupPath, _filePath, overwrite: true);
            Console.WriteLine("Backup restaurado correctamente");
        }
    }
}
```

---
### 4️⃣ Repository XML - Estructura Base

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml.Serialization;
using UniversidadApp.Models;

namespace UniversidadApp.Data
{
    public class EstudianteRepositoryXML
    {
        private readonly string _filePath;
        private readonly XmlSerializer _serializer;

        public EstudianteRepositoryXML(string filePath = "estudiantes.xml")
        {
            _filePath = filePath;
            _serializer = new XmlSerializer(typeof(List<Estudiante>));

            if (!File.Exists(_filePath))
            {
                GuardarTodos(new List<Estudiante>());
            }
        }
```

---
### 4️⃣ Repository XML - Métodos CRUD

```csharp
        public void Crear(Estudiante estudiante)
        {
            var estudiantes = ObtenerTodos();
            estudiante.Id = estudiantes.Any() 
                ? estudiantes.Max(e => e.Id) + 1 
                : 1;
            estudiantes.Add(estudiante);
            GuardarTodos(estudiantes);
        }

        public List<Estudiante> ObtenerTodos()
        {
            using (var stream = File.OpenRead(_filePath))
            {
                var estudiantes = (List<Estudiante>)_serializer.Deserialize(stream);
                return estudiantes.Where(e => e.Activo).ToList();
            }
        }

        public bool Actualizar(Estudiante estudiante)
        {
            var estudiantes = LeerTodos();
            var index = estudiantes.FindIndex(e => e.Id == estudiante.Id);

            if (index == -1)
                return false;

            estudiantes[index] = estudiante;
            GuardarTodos(estudiantes);
            return true;
        }

        public bool EliminarLogico(int id)
        {
            var estudiante = ObtenerTodos().FirstOrDefault(e => e.Id == id);
            if (estudiante == null)
                return false;

            estudiante.Activo = false;
            return Actualizar(estudiante);
        }
```

---
### 4️⃣ Repository XML - Métodos Auxiliares

```csharp
        private List<Estudiante> LeerTodos()
        {
            using (var stream = File.OpenRead(_filePath))
            {
                return (List<Estudiante>)_serializer.Deserialize(stream);
            }
        }

        private void GuardarTodos(List<Estudiante> estudiantes)
        {
            using (var stream = File.Create(_filePath))
            {
                _serializer.Serialize(stream, estudiantes);
            }
        }
    }
}
```

---

### 📊 Comparación de Formatos

| Aspecto | CSV | JSON | XML |
|---------|-----|------|-----|
| **Legibilidad** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Tamaño** | ⭐⭐⭐ (más pequeño) | ⭐⭐ | ⭐ (más grande) |
| **Facilidad parsing** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Soporte tipos** | ⭐ (todo es texto) | ⭐⭐⭐ | ⭐⭐⭐ |
| **Interoperabilidad** | ⭐⭐⭐ (universal) | ⭐⭐⭐ | ⭐⭐⭐ |
| **Complejidad** | ⭐ | ⭐⭐ | ⭐⭐⭐ |

---

## 💻 Actividad Práctica

### Ejercicio 1: Migración de Formatos

Implementar método que convierta datos entre CSV ↔ JSON ↔ XML.

```csharp
public class MigradorDatos
{
    public void CSVaJSON(string csvPath, string jsonPath)
    {
        var repoCSV = new EstudianteRepositoryCSV(csvPath);
        var estudiantes = repoCSV.ObtenerTodos();
        
        var repoJSON = new EstudianteRepositoryJSON(jsonPath);
        // TODO: Guardar estudiantes en JSON
    }
}
```

### Ejercicio 2: Logs de Auditoría

Crear sistema que registre todas las operaciones CRUD en un archivo `auditoria.log`:

```
[2026-01-31 18:30:15] CREATE - Estudiante EST004 creado por Usuario1
[2026-01-31 18:32:20] UPDATE - Estudiante EST002 actualizado por Usuario1
[2026-01-31 18:35:10] DELETE - Estudiante EST001 eliminado por Usuario2
```

### Ejercicio 3: Exportación a Excel

Usando una librería como EPPlus o ClosedXML, exportar los datos a un archivo Excel (.xlsx).

### Tiempo estimado: 75 minutos

---
