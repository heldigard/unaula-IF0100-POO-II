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
### 2️⃣ Repository CSV - Métodos Auxiliares

```csharp
        private string EstudianteACSV(Estudiante e)
        {
            return $"{e.Id}{SEPARADOR}" +
                   $"{e.Codigo}{SEPARADOR}" +
                   $"\"{e.Nombre}\"{SEPARADOR}" +
                   $"\"{e.Apellido}\"{SEPARADOR}" +
                   $"{e.Email}{SEPARADOR}" +
                   $"{e.FechaNacimiento:yyyy-MM-dd}{SEPARADOR}" +
                   $"{e.Promedio:F2}{SEPARADOR}" +
                   $"{(e.Activo ? "1" : "0")}";
        }

        private Estudiante CSVAEstudiante(string linea)
        {
            var campos = SepararCSV(linea);
            if (campos.Length < 8) throw new FormatException("Línea CSV incompleta");
            return new Estudiante
            {
                Id = int.Parse(campos[0]), Codigo = campos[1],
                Nombre = campos[2].Trim('"'), Apellido = campos[3].Trim('"'),
                Email = campos[4], FechaNacimiento = DateTime.Parse(campos[5]),
                Promedio = decimal.Parse(campos[6]), Activo = campos[7] == "1"
            };
        }

        private string[] SepararCSV(string linea)
        {
            var campos = new List<string>();
            bool dentroComillas = false;
            string campoActual = "";
            foreach (char c in linea)
            {
                if (c == '"') dentroComillas = !dentroComillas;
                else if (c == SEPARADOR && !dentroComillas)
                {
                    campos.Add(campoActual);
                    campoActual = "";
                }
                else campoActual += c;
            }
            campos.Add(campoActual);
            return campos.ToArray();
        }

        private void GuardarTodos(List<Estudiante> estudiantes)
        {
            var lineas = new List<string> { "Id,Codigo,Nombre,Apellido,Email,FechaNacimiento,Promedio,Activo" };
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
### 4️⃣ Repository XML - Estructura y CRUD Completo

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
            if (!File.Exists(_filePath)) GuardarTodos(new List<Estudiante>());
        }

        public void Crear(Estudiante estudiante)
        {
            var estudiantes = ObtenerTodos();
            estudiante.Id = estudiantes.Any() ? estudiantes.Max(e => e.Id) + 1 : 1;
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
            if (index == -1) return false;
            estudiantes[index] = estudiante;
            GuardarTodos(estudiantes);
            return true;
        }

        public bool EliminarLogico(int id)
        {
            var estudiante = ObtenerTodos().FirstOrDefault(e => e.Id == id);
            if (estudiante == null) return false;
            estudiante.Activo = false;
            return Actualizar(estudiante);
        }

        private List<Estudiante> LeerTodos()
        {
            using (var stream = File.OpenRead(_filePath))
                return (List<Estudiante>)_serializer.Deserialize(stream);
        }

        private void GuardarTodos(List<Estudiante> estudiantes)
        {
            using (var stream = File.Create(_filePath))
                _serializer.Serialize(stream, estudiantes);
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

## 🔧 Archivos de Configuración INI

### Manejo de archivos .ini para configuraciones

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

namespace UniversidadApp.Config
{
    /// <summary>
    /// Lector de archivos INI simple y eficiente
    /// Formato:
    /// [Seccion]
    /// Clave=Valor
    /// </summary>
    public class IniFile
    {
        private readonly string _filePath;
        private readonly Dictionary<string, Dictionary<string, string>> _data;

        public IniFile(string filePath)
        {
            _filePath = filePath;
            _data = new Dictionary<string, Dictionary<string, string>>();
            Load();
        }

        private void Load()
        {
            if (!File.Exists(_filePath))
            {
                // Crear archivo vacío si no existe
                File.WriteAllText(_filePath, "; Archivo de configuración\n");
                return;
            }

            string currentSection = "DEFAULT";

            foreach (var line in File.ReadAllLines(_filePath))
            {
                var trimmed = line.Trim();

                // Ignorar comentarios y líneas vacías
                if (string.IsNullOrWhiteSpace(trimmed) || trimmed.StartsWith(";"))
                    continue;

                // Sección: [NombreSeccion]
                var sectionMatch = Regex.Match(trimmed, @"^\[([^\]]+)\]$");
                if (sectionMatch.Success)
                {
                    currentSection = sectionMatch.Groups[1].Value;
                    if (!_data.ContainsKey(currentSection))
                        _data[currentSection] = new Dictionary<string, string>();
                    continue;
                }

                // Clave=Valor
                var keyValueMatch = Regex.Match(trimmed, @"^([^=]+)=(.*)$");
                if (keyValueMatch.Success)
                {
                    var key = keyValueMatch.Groups[1].Value.Trim();
                    var value = keyValueMatch.Groups[2].Value.Trim();

                    if (!_data.ContainsKey(currentSection))
                        _data[currentSection] = new Dictionary<string, string>();

                    _data[currentSection][key] = value;
                }
            }
        }

        public void Save()
        {
            using var writer = new StreamWriter(_filePath);

            foreach (var section in _data)
            {
                writer.WriteLine($"[{section.Key}]");

                foreach (var keyValue in section.Value)
                {
                    writer.WriteLine($"{keyValue.Key}={keyValue.Value}");
                }

                writer.WriteLine();
            }
        }

        public string GetValue(string section, string key, string defaultValue = "")
        {
            if (_data.ContainsKey(section) && _data[section].ContainsKey(key))
                return _data[section][key];

            return defaultValue;
        }

        public void SetValue(string section, string key, string value)
        {
            if (!_data.ContainsKey(section))
                _data[section] = new Dictionary<string, string>();

            _data[section][key] = value;
        }

        public int GetInt(string section, string key, int defaultValue = 0)
        {
            var value = GetValue(section, key);
            return int.TryParse(value, out var result) ? result : defaultValue;
        }

        public bool GetBool(string section, string key, bool defaultValue = false)
        {
            var value = GetValue(section, key);
            return bool.TryParse(value, out var result) ? result : defaultValue;
        }
    }
}

// Uso
var config = new IniFile("config.ini");

// Leer valores
var servidor = config.GetValue("Database", "Server", "localhost");
var puerto = config.GetInt("Database", "Port", 1433);
var usarSSL = config.GetBool("Database", "UseSSL", false);

// Escribir valores
config.SetValue("App", "Theme", "Dark");
config.SetValue("App", "Language", "es-CO");
config.Save();

/* Archivo config.ini de ejemplo:
; Archivo de configuración de UniversidadApp

[Database]
Server=localhost
Port=1433
Database=UniversidadDB
UseSSL=true

[App]
Theme=Dark
Language=es-CO
PageSize=20
*/
```

---

## 🔒 File Locking y Concurrencia

### Manejo de acceso concurrente a archivos

```
┌─────────────────────────────────────────────────────────────┐
│              CONCURRENCIA DE ARCHIVOS                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Sin Locking                     Con Locking                │
│  ────────────                    ────────────                │
│                                                             │
│  Proceso A → Leer                Proceso A → Leer           │
│  Proceso B → Leer                Proceso B → Leer           │
│  Proceso A → Escribir            Proceso A → Esperar        │
│  Proceso B → Escribir ✗ CORRUPCIÓN │  └─→ Escribir          │
│                                  Proceso B → Esperar        │
│                                    └─→ Escribir            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

```csharp
using System;
using System.IO;
using System.Threading;

namespace UniversidadApp.IO
{
    /// <summary>
    /// Manejo seguro de archivos con locking
    /// </summary>
    public class SafeFileWriter
    {
        private readonly string _filePath;
        private readonly TimeSpan _lockTimeout;
        private readonly int _retryDelay;

        public SafeFileWriter(string filePath,
            TimeSpan? lockTimeout = null, int retryDelay = 100)
        {
            _filePath = filePath;
            _lockTimeout = lockTimeout ?? TimeSpan.FromSeconds(30);
            _retryDelay = retryDelay;
        }

        /// <summary>
        /// Escribir contenido con reintentos en caso de archivo bloqueado
        /// </summary>
        public void WriteWithRetry(string content)
        {
            var startTime = DateTime.Now;

            while (DateTime.Now - startTime < _lockTimeout)
            {
                try
                {
                    // Intentar escribir
                    File.WriteAllText(_filePath, content);
                    return;
                }
                catch (IOException ex) when (IsFileLocked(ex))
                {
                    // Archivo bloqueado - esperar y reintentar
                    Thread.Sleep(_retryDelay);
                }
            }

            throw new TimeoutException(
                $"No se pudo escribir en {_filePath} después de {_lockTimeout.TotalSeconds} segundos");
        }

        /// <summary>
        /// Leer contenido con reintentos
        /// </summary>
        public string ReadWithRetry()
        {
            var startTime = DateTime.Now;

            while (DateTime.Now - startTime < _lockTimeout)
            {
                try
                {
                    return File.ReadAllText(_filePath);
                }
                catch (IOException ex) when (IsFileLocked(ex))
                {
                    Thread.Sleep(_retryDelay);
                }
            }

            throw new TimeoutException(
                $"No se pudo leer {_filePath} después de {_lockTimeout.TotalSeconds} segundos");
        }

        /// <summary>
        /// Escribir de forma atómica (usando archivo temporal)
        /// </summary>
        public void WriteAtomic(string content)
        {
            var tempPath = _filePath + ".tmp";

            try
            {
                // Escribir en archivo temporal
                File.WriteAllText(tempPath, content);

                // Reemplazar original de forma atómica
                File.Replace(tempPath, _filePath, backupPath: null);
            }
            catch
            {
                // Limpiar archivo temporal en caso de error
                if (File.Exists(tempPath))
                    File.Delete(tempPath);
                throw;
            }
        }

        /// <summary>
        /// Usar FileStream con modo exclusivo para locking a nivel de SO
        /// </summary>
        public void WriteWithLock(string content)
        {
            using var stream = new FileStream(
                _filePath,
                FileMode.Create,
                FileAccess.Write,
                FileShare.None  // Nadie más puede acceder mientras escribimos
            );

            using var writer = new StreamWriter(stream);
            writer.Write(content);
        }

        private bool IsFileLocked(IOException exception)
        {
            // Código de error para archivo bloqueado en Windows
            const int ERROR_SHARING_VIOLATION = unchecked((int)0x80070020);
            const int ERROR_LOCK_VIOLATION = unchecked((int)0x80070021);

            return exception.HResult == ERROR_SHARING_VIOLATION ||
                   exception.HResult == ERROR_LOCK_VIOLATION;
        }
    }

    /// <summary>
    /// Monitor de cambios en archivos
    /// </summary>
    public class FileWatcher : IDisposable
    {
        private readonly FileSystemWatcher _watcher;
        private readonly string _filePath;

        public event Action<FileChangeType> OnFileChanged;

        public FileWatcher(string filePath)
        {
            _filePath = filePath;
            var directory = Path.GetDirectoryName(filePath);
            var fileName = Path.GetFileName(filePath);

            _watcher = new FileSystemWatcher(directory)
            {
                Filter = fileName,
                NotifyFilter = NotifyFilters.LastWrite | NotifyFilters.Size
            };

            _watcher.Changed += (s, e) => OnFileChanged?.Invoke(FileChangeType.Modified);
            _watcher.Created += (s, e) => OnFileChanged?.Invoke(FileChangeType.Created);
            _watcher.Deleted += (s, e) => OnFileChanged?.Invoke(FileChangeType.Deleted);

            _watcher.EnableRaisingEvents = true;
        }

        public void Dispose()
        {
            _watcher?.Dispose();
        }
    }

    public enum FileChangeType
    {
        Created,
        Modified,
        Deleted
    }
}

// Uso
var writer = new SafeFileWriter("datos.txt");

// Escritura segura con reintentos
writer.WriteWithRetry("Contenido nuevo");

// Escritura atómica (garantiza que no hay datos corruptos)
writer.WriteAtomic("Contenido crítico");

// Monitorear cambios
using var watcher = new FileWatcher("datos.txt");
watcher.OnFileChanged += (changeType) =>
{
    Console.WriteLine($"Archivo {changeType}: Recargando datos...");
    // Recargar datos del archivo
};
```

---

## 🗜️ Compresión de Archivos

### Reducir tamaño de archivos con compresión

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Text;

namespace UniversidadApp.IO
{
    /// <summary>
    /// Utilidades de compresión y descompresión
    /// </summary>
    public static class FileCompression
    {
        /// <summary>
        /// Comprimir archivo usando GZIP
        /// </summary>
        public static void CompressGzip(string sourcePath, string compressedPath)
        {
            using var originalStream = File.OpenRead(sourcePath);
            using var compressedStream = File.Create(compressedPath);
            using var gzipStream = new GZipStream(compressedStream, CompressionMode.Compress);

            originalStream.CopyTo(gzipStream);

            var originalSize = originalStream.Length;
            var compressedSize = compressedStream.Length;
            var ratio = (1 - (double)compressedSize / originalSize) * 100;

            Console.WriteLine($"Original: {originalSize:N0} bytes");
            Console.WriteLine($"Comprimido: {compressedSize:N0} bytes");
            Console.WriteLine($"Ratio de compresión: {ratio:F1}%");
        }

        /// <summary>
        /// Descomprimir archivo GZIP
        /// </summary>
        public static void DecompressGzip(string compressedPath, string decompressedPath)
        {
            using var compressedStream = File.OpenRead(compressedPath);
            using var gzipStream = new GZipStream(compressedStream, CompressionMode.Decompress);
            using var decompressedStream = File.Create(decompressedPath);

            gzipStream.CopyTo(decompressedStream);
        }

        /// <summary>
        /// Comprimir string en memoria
        /// </summary>
        public static byte[] CompressString(string text)
        {
            var bytes = Encoding.UTF8.GetBytes(text);

            using var outputStream = new MemoryStream();
            using (var gzipStream = new GZipStream(outputStream, CompressionMode.Compress))
            {
                gzipStream.Write(bytes, 0, bytes.Length);
            }

            return outputStream.ToArray();
        }

        /// <summary>
        /// Descomprimir string desde memoria
        /// </summary>
        public static string DecompressString(byte[] compressedBytes)
        {
            using var inputStream = new MemoryStream(compressedBytes);
            using var gzipStream = new GZipStream(inputStream, CompressionMode.Decompress);
            using var outputStream = new MemoryStream();

            gzipStream.CopyTo(outputStream);
            return Encoding.UTF8.GetString(outputStream.ToArray());
        }

        /// <summary>
        /// Crear archivo ZIP con múltiples archivos
        /// </summary>
        public static void CreateZip(string zipPath, params string[] filesToInclude)
        {
            if (File.Exists(zipPath))
                File.Delete(zipPath);

            using var archive = ZipFile.Open(zipPath, ZipArchiveMode.Create);

            foreach (var filePath in filesToInclude)
            {
                if (!File.Exists(filePath))
                    continue;

                var entryName = Path.GetFileName(filePath);
                archive.CreateEntryFromFile(filePath, entryName);
            }

            Console.WriteLine($"ZIP creado: {zipPath}");
        }

        /// <summary>
        /// Extraer archivo ZIP
        /// </summary>
        public static void ExtractZip(string zipPath, string destinationFolder)
        {
            if (!Directory.Exists(destinationFolder))
                Directory.CreateDirectory(destinationFolder);

            ZipFile.ExtractToDirectory(zipPath, destinationFolder);

            Console.WriteLine($"ZIP extraído en: {destinationFolder}");
        }

        /// <summary>
        /// Comprimir CSV a JSON comprimido
        /// </summary>
        public static void CompressRepositoryData(string csvPath, string jsonCompressedPath)
        {
            // 1. Leer CSV
            var lines = File.ReadAllLines(csvPath);

            // 2. Convertir a JSON
            var json = string.Join(",", lines);
            var jsonArray = $"[{json}]";

            // 3. Comprimir JSON
            var compressedJson = CompressString(jsonArray);

            // 4. Guardar comprimido
            File.WriteAllBytes(jsonCompressedPath, compressedJson);

            Console.WriteLine($"CSV: {new FileInfo(csvPath).Length:N0} bytes");
            Console.WriteLine($"JSON comprimido: {compressedJson.Length:N0} bytes");
        }
    }
}

// Uso
// Comprimir un solo archivo
FileCompression.CompressGzip("estudiantes.json", "estudiantes.json.gz");

// Descomprimir
FileCompression.DecompressGzip("estudiantes.json.gz", "estudiantes_restored.json");

// Crear ZIP con múltiples archivos
FileCompression.CreateZip(
    "backup.zip",
    "estudiantes.csv",
    "estudiantes.json",
    "config.ini"
);

// Extraer ZIP
FileCompression.ExtractZip("backup.zip", "backup_extraido");

// Comprimir string en memoria
var original = "Datos muy largos que se repiten muchas veces...";
var compressed = FileCompression.CompressString(original);
var decompressed = FileCompression.DecompressString(compressed);

Console.WriteLine($"Original: {original.Length} bytes");
Console.WriteLine($"Comprimido: {compressed.Length} bytes");
Console.WriteLine($"Igual: {original == decompressed}");
```

---

## Comparación Final: Cuándo Usar Cada Formato

| Aspecto | CSV | JSON | XML | INI | ZIP/GZIP |
|---------|-----|------|-----|-----|----------|
| **Legibilidad** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ |
| **Tamaño** | ⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Parsing** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ |
| **Soporte tipos** | ⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐⭐ |
| **Metadatos** | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Configuración** | ⭐⭐ | ⭐ | ⭐ | ⭐⭐⭐ | ⭐ |
| **Intercambio web** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐ |
| **Compresión** | ⭐ | ⭐ | ⭐ | ⭐ | ⭐⭐⭐⭐⭐ |

### Casos de uso recomendados

| Formato | Mejor para... |
|---------|--------------|
| **CSV** | Exportar datos tabulares, Excel, importación masiva |
| **JSON** | APIs web, configuración moderna, intercambio de datos |
| **XML** | APIs SOAP, documentos con metadatos, legacy systems |
| **INI** | Configuración de aplicación simple, settings locales |
| **ZIP** | Backup, distribución de múltiples archivos, archivado |

---
