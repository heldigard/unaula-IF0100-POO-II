---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 5'
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

# DataBinding, XML y Proyecto Final

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, el estudiante será capaz de:

1. **Implementar** data binding bidireccional en Windows Forms
2. **Utilizar** archivos XML como fuente de datos
3. **Integrar** todas las tecnologías del curso en un proyecto final
4. **Aplicar** buenas prácticas de arquitectura de software

**Duración:** 150 minutos

---

## 📋 Contenido

### 1. Data Binding - Enlace de Datos (20 min)

**¿Qué es Data Binding?**
Enlazar automáticamente controles visuales (TextBox, DataGridView, ComboBox) con fuentes de datos (DataTable, List, etc.).

**1.1. BindingSource (Recomendado)**

```csharp
using System.Windows.Forms;

public class FormEstudiantes : Form
{
    private DataTable dtEstudiantes;
    private BindingSource bindingSource;
    private DataGridView dgvEstudiantes;
    private TextBox txtNombre, txtApellido, txtEmail;
    private Button btnGuardar, btnEliminar, btnNuevo;
    
    public FormEstudiantes()
    {
        InicializarComponentes();
        CargarDatos();
    }
    
    private void InicializarComponentes()
    {
        // Crear controles
        dgvEstudiantes = new DataGridView
        {
            Dock = DockStyle.Top,
            Height = 300,
            SelectionMode = DataGridViewSelectionMode.FullRowSelect
        };
        
        txtNombre = new TextBox { Location = new Point(100, 320), Width = 200 };
        txtApellido = new TextBox { Location = new Point(100, 350), Width = 200 };
        txtEmail = new TextBox { Location = new Point(100, 380), Width = 200 };
        
        btnNuevo = new Button 
        { 
            Text = "Nuevo", 
            Location = new Point(100, 420),
            Width = 80
        };
        btnNuevo.Click += BtnNuevo_Click;
        
        btnGuardar = new Button 
        { 
            Text = "Guardar", 
            Location = new Point(190, 420),
            Width = 80
        };
        btnGuardar.Click += BtnGuardar_Click;
        
        btnEliminar = new Button 
        { 
            Text = "Eliminar", 
            Location = new Point(280, 420),
            Width = 80
        };
        btnEliminar.Click += BtnEliminar_Click;
        
        // Agregar labels
        Controls.Add(new Label { Text = "Nombre:", Location = new Point(20, 323) });
        Controls.Add(new Label { Text = "Apellido:", Location = new Point(20, 353) });
        Controls.Add(new Label { Text = "Email:", Location = new Point(20, 383) });
        
        // Agregar controles al form
        Controls.Add(dgvEstudiantes);
        Controls.Add(txtNombre);
        Controls.Add(txtApellido);
        Controls.Add(txtEmail);
        Controls.Add(btnNuevo);
        Controls.Add(btnGuardar);
        Controls.Add(btnEliminar);
        
        Text = "Gestión de Estudiantes";
        Width = 600;
        Height = 500;
    }
    
    private void CargarDatos()
    {
        // Crear DataTable (en producción vendría de BD)
        dtEstudiantes = new DataTable("Estudiantes");
        dtEstudiantes.Columns.Add("Id", typeof(int));
        dtEstudiantes.Columns.Add("Nombre", typeof(string));
        dtEstudiantes.Columns.Add("Apellido", typeof(string));
        dtEstudiantes.Columns.Add("Email", typeof(string));
        dtEstudiantes.PrimaryKey = new DataColumn[] { dtEstudiantes.Columns["Id"] };
        
        // Datos de ejemplo
        dtEstudiantes.Rows.Add(1, "Juan", "Pérez", "juan@unaula.edu.co");
        dtEstudiantes.Rows.Add(2, "María", "García", "maria@unaula.edu.co");
        dtEstudiantes.Rows.Add(3, "Carlos", "López", "carlos@unaula.edu.co");
        
        // Configurar BindingSource
        bindingSource = new BindingSource();
        bindingSource.DataSource = dtEstudiantes;
        
        // Enlazar DataGridView
        dgvEstudiantes.DataSource = bindingSource;
        
        // Enlazar TextBoxes individuales
        txtNombre.DataBindings.Add("Text", bindingSource, "Nombre", true);
        txtApellido.DataBindings.Add("Text", bindingSource, "Apellido", true);
        txtEmail.DataBindings.Add("Text", bindingSource, "Email", true);
    }
    
    private void BtnNuevo_Click(object sender, EventArgs e)
    {
        bindingSource.AddNew();
        txtNombre.Focus();
    }
    
    private void BtnGuardar_Click(object sender, EventArgs e)
    {
        bindingSource.EndEdit();
        dtEstudiantes.AcceptChanges();
        MessageBox.Show("Cambios guardados", "Éxito");
    }
    
    private void BtnEliminar_Click(object sender, EventArgs e)
    {
        if (bindingSource.Current != null)
        {
            if (MessageBox.Show("¿Eliminar registro?", "Confirmar", 
                MessageBoxButtons.YesNo) == DialogResult.Yes)
            {
                bindingSource.RemoveCurrent();
            }
        }
    }
}
```


**Ventajas de BindingSource:**
- ✅ Sincronización automática entre controles
- ✅ Navegación entre registros (MoveNext, MovePrevious)
- ✅ Filtrado y ordenamiento
- ✅ Notificación de cambios
---
### 2. DataSet y XML (20 min)

**2.1. Exportar DataSet a XML**

```csharp
public class DataSetXmlHelper
{
    // Exportar solo datos
    public void ExportarDatos(DataSet ds, string archivo)
    {
        ds.WriteXml(archivo, XmlWriteMode.WriteSchema);
        Console.WriteLine($"Datos exportados a {archivo}");
    }
    
    // Exportar solo esquema (estructura)
    public void ExportarEsquema(DataSet ds, string archivo)
    {
        ds.WriteXmlSchema(archivo);
        Console.WriteLine($"Esquema exportado a {archivo}");
    }
    
    // Exportar datos + esquema en archivos separados
    public void ExportarCompleto(DataSet ds, string archivoBase)
    {
        ds.WriteXml($"{archivoBase}_datos.xml");
        ds.WriteXmlSchema($"{archivoBase}_esquema.xsd");
    }
    
    // Importar desde XML
    public DataSet ImportarDatos(string archivo)
    {
        DataSet ds = new DataSet();
        ds.ReadXml(archivo, XmlReadMode.ReadSchema);
        Console.WriteLine($"Datos importados desde {archivo}");
        return ds;
    }
}
```

**Ejemplo de uso:**

```csharp
class Program
{
    static void Main()
    {
        // Crear DataSet con datos
        DataSet dsUniversidad = new DataSet("Universidad");
        
        DataTable dtEstudiantes = new DataTable("Estudiantes");
        dtEstudiantes.Columns.Add("Id", typeof(int));
        dtEstudiantes.Columns.Add("Nombre", typeof(string));
        dtEstudiantes.Columns.Add("Promedio", typeof(decimal));
        
        dtEstudiantes.Rows.Add(1, "Juan Pérez", 4.2m);
        
        dsUniversidad.Tables.Add(dtEstudiantes);
        
        // Exportar
        var helper = new DataSetXmlHelper();
        helper.ExportarDatos(dsUniversidad, "universidad.xml");
        
        // Importar
        DataSet dsImportado = helper.ImportarDatos("universidad.xml");
        Console.WriteLine($"Tablas importadas: {dsImportado.Tables.Count}");
        Console.WriteLine($"Filas: {dsImportado.Tables[0].Rows.Count}");
    }
}
```

**Archivo XML generado (universidad.xml):**
```xml
<?xml version="1.0" standalone="yes"?>
<Universidad>
  <xs:schema id="Universidad" xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="Universidad" msdata:IsDataSet="true">
      <xs:complexType>
        <xs:choice minOccurs="0" maxOccurs="unbounded">
          <xs:element name="Estudiantes">
            <xs:complexType>
              <xs:sequence>
                <xs:element name="Id" type="xs:int" />
                <xs:element name="Nombre" type="xs:string" />
                <xs:element name="Promedio" type="xs:decimal" />
              </xs:sequence>
            </xs:complexType>
          </xs:element>
        </xs:choice>
      </xs:complexType>
    </xs:element>
  </xs:schema>
  <Estudiantes>
    <Id>1</Id>
    <Nombre>Juan Pérez</Nombre>
    <Promedio>4.2</Promedio>
  </Estudiantes>
  <Estudiantes>
    <Id>2</Id>
    <Nombre>María García</Nombre>
    <Promedio>4.5</Promedio>
  </Estudiantes>
</Universidad>
```


**2.2. Aplicaciones prácticas:**
- ✅ Backup de datos
- ✅ Intercambio entre aplicaciones
- ✅ Configuración compleja
- ✅ Datos temporales offline
---
### 3. Proyecto Integrador - Especificación (15 min)

**Sistema de Gestión de Biblioteca (Proyecto Final)**

**Objetivo:** Crear una aplicación completa que integre todos los conceptos del semestre.

**Tecnologías requeridas:**
- ✅ C# con POO (Unidad 1)
- ✅ Pruebas unitarias TDD (Unidad 2)
- ✅ ASP.NET Core MVC o Windows Forms (Unidad 3)
- ✅ ADO.NET con SQL Server (Unidad 4)
- ✅ DataSet y XML (Unidad 5)

**Funcionalidades mínimas:**

**1. Gestión de Libros**
- CRUD completo
- Búsqueda por título/autor/ISBN
- Categorización por género
- Estado: Disponible/Prestado

**2. Gestión de Usuarios**
- Registro de usuarios (estudiantes, profesores)
- Validación de email único
- Estado activo/inactivo

**3. Préstamos**
- Registrar préstamo (validar disponibilidad)
- Registrar devolución
- Calcular multas por atraso (>15 días = $1000/día)
- Historial de préstamos

**4. Reportes**
- Libros más prestados (Top 10)
- Usuarios con préstamos activos
- Préstamos vencidos
- Exportar reportes a CSV y XML

**5. Características técnicas**
- Transacciones en operaciones críticas
- Manejo de excepciones
- Validaciones de negocio
- Al menos 10 pruebas unitarias
- DataBinding en formularios

**Modelo de datos (SQL):**

```sql
CREATE TABLE Libros (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Titulo NVARCHAR(200) NOT NULL,
    Autor NVARCHAR(100) NOT NULL,
    ISBN NVARCHAR(20) UNIQUE NOT NULL,
    Genero NVARCHAR(50),
    Disponible BIT DEFAULT 1,
    FechaIngreso DATE DEFAULT GETDATE()
);

CREATE TABLE Usuarios (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    TipoUsuario NVARCHAR(20) NOT NULL, -- 'Estudiante', 'Profesor'
    Activo BIT DEFAULT 1,
    FechaRegistro DATE DEFAULT GETDATE()
);

CREATE TABLE Prestamos (
    Id INT PRIMARY KEY IDENTITY(1,1),
    LibroId INT FOREIGN KEY REFERENCES Libros(Id),
    UsuarioId INT FOREIGN KEY REFERENCES Usuarios(Id),
    FechaPrestamo DATE NOT NULL DEFAULT GETDATE(),
    FechaDevolucionEsperada DATE NOT NULL,
    FechaDevolucionReal DATE NULL,
    Multa DECIMAL(10,2) DEFAULT 0,
    Estado NVARCHAR(20) DEFAULT 'Activo' -- 'Activo', 'Devuelto', 'Vencido'
);
```


**Entregables:**
1. Código fuente completo (GitHub)
2. Script SQL con datos de prueba
3. Manual de usuario (PDF)
4. Video demo de 5-10 minutos
5. Presentación PowerPoint
6. **Sustentación en parejas (20% de la nota)**

**Criterios de evaluación (100 pts):**
- Funcionalidad completa: 30 pts
- Calidad del código: 20 pts
- Uso correcto de POO: 10 pts
- Persistencia (ADO.NET): 15 pts
- Pruebas unitarias: 10 pts
- Interfaz de usuario: 10 pts
- Documentación: 5 pts
---
### 4. Integración de Conocimientos (20 min)

**4.1. Ejemplo: Servicio de Préstamo Completo**

```csharp
// Capa de Entidades (POO - Unidad 1)
public class Prestamo
{
    public int Id { get; set; }
    public int LibroId { get; set; }
    public int UsuarioId { get; set; }
    public DateTime FechaPrestamo { get; set; }
    public DateTime FechaDevolucionEsperada { get; set; }
    public DateTime? FechaDevolucionReal { get; set; }
    public decimal Multa { get; set; }
    public string Estado { get; set; }
    
    public int DiasVencidos
    {
        get
        {
            if (FechaDevolucionReal.HasValue)
                return 0;
            
---
### 4. Integración de Conocimientos (20 min)


            TimeSpan diferencia = DateTime.Now - FechaDevolucionEsperada;
            return diferencia.Days > 0 ? diferencia.Days : 0;
        }
    }
    
    public decimal CalcularMulta()
    {
        int diasVencidos = DiasVencidos;
        return diasVencidos > 0 ? diasVencidos * 1000 : 0;
    }
}

// Capa de Datos (ADO.NET - Unidad 4)
public class PrestamoRepository
{
    private string connectionString = "...";
    
    public int RegistrarPrestamo(int libroId, int usuarioId)
    {
        int prestamoId = 0;
        
        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            conn.Open();
            
            using (SqlTransaction trans = conn.BeginTransaction())
            {
                try
                {
                    // 1. Verificar disponibilidad del libro
                    string queryVerificar = 
                        "SELECT Disponible FROM Libros WHERE Id = @LibroId";
                    
                    using (SqlCommand cmd = new SqlCommand(queryVerificar, conn, trans))
                    {
                        cmd.Parameters.AddWithValue("@LibroId", libroId);
                        bool disponible = (bool)cmd.ExecuteScalar();
                        
                        if (!disponible)
                            throw new Exception("Libro no disponible");
                    }
                    
                    // 2. Insertar préstamo
                    string queryPrestamo = @"
                        INSERT INTO Prestamos 
                        (LibroId, UsuarioId, FechaPrestamo, FechaDevolucionEsperada) 
                        VALUES 
                        (@LibroId, @UsuarioId, GETDATE(), DATEADD(day, 15, GETDATE()));
                        SELECT CAST(SCOPE_IDENTITY() AS INT);";
                    
                    using (SqlCommand cmd = new SqlCommand(queryPrestamo, conn, trans))
                    {
                        cmd.Parameters.AddWithValue("@LibroId", libroId);
                        cmd.Parameters.AddWithValue("@UsuarioId", usuarioId);
                        prestamoId = (int)cmd.ExecuteScalar();
                    }
                    
                    // 3. Marcar libro como no disponible
                    string queryActualizar = 
                        "UPDATE Libros SET Disponible = 0 WHERE Id = @LibroId";
                    
                    using (SqlCommand cmd = new SqlCommand(queryActualizar, conn, trans))
                    {
                        cmd.Parameters.AddWithValue("@LibroId", libroId);
                        cmd.ExecuteNonQuery();
                    }
                    
                    trans.Commit();
                }
                catch
                {
                    trans.Rollback();
                    throw;
                }
            }
        }
        
        return prestamoId;
    }
    
    public void RegistrarDevolucion(int prestamoId)
    {
        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            conn.Open();
            using (SqlTransaction trans = conn.BeginTransaction())
            {
                try
                {
                    // 1. Obtener datos del préstamo
                    string queryPrestamo = @"
                        SELECT LibroId, FechaDevolucionEsperada 
                        FROM Prestamos WHERE Id = @Id";
                    
                    int libroId = 0;
                    DateTime fechaEsperada = DateTime.MinValue;
                    
                    using (SqlCommand cmd = new SqlCommand(queryPrestamo, conn, trans))
                    {
                        cmd.Parameters.AddWithValue("@Id", prestamoId);
                        
                        using (SqlDataReader reader = cmd.ExecuteReader())
                        {
                            if (reader.Read())
                            {
                                libroId = reader.GetInt32(0);
                                fechaEsperada = reader.GetDateTime(1);
                            }
                        }
                    }
                    
                    // 2. Calcular multa si hay atraso
                    decimal multa = 0;
                    TimeSpan diferencia = DateTime.Now - fechaEsperada;
                    if (diferencia.Days > 0)
                    {
                        multa = diferencia.Days * 1000;
                    }
                    
                    // 3. Actualizar préstamo
                    string queryActualizar = @"
                        UPDATE Prestamos 
                        SET FechaDevolucionReal = GETDATE(), 
                            Multa = @Multa, 
                            Estado = 'Devuelto' 
                        WHERE Id = @Id";
                    
                    using (SqlCommand cmd = new SqlCommand(queryActualizar, conn, trans))
                    {
                        cmd.Parameters.AddWithValue("@Id", prestamoId);
                        cmd.Parameters.AddWithValue("@Multa", multa);
                        cmd.ExecuteNonQuery();
                    }
                    
                    // 4. Marcar libro como disponible
                    string queryLibro = 
                        "UPDATE Libros SET Disponible = 1 WHERE Id = @LibroId";
                    
                    using (SqlCommand cmd = new SqlCommand(queryLibro, conn, trans))
                    {
                        cmd.Parameters.AddWithValue("@LibroId", libroId);
                        cmd.ExecuteNonQuery();
                    }
                    
                    trans.Commit();
                }
                catch
                {
                    trans.Rollback();
                    throw;
                }
            }
        }
    }
}


// Pruebas Unitarias (TDD - Unidad 2)
[TestClass]
public class PrestamoTests
{
    [TestMethod]
    public void CalcularMulta_SinAtraso_RetornaCero()
    {
        // Arrange
        var prestamo = new Prestamo
        {
            FechaDevolucionEsperada = DateTime.Now.AddDays(5)
        };
        
        // Act
        decimal multa = prestamo.CalcularMulta();
        
        // Assert
        Assert.AreEqual(0, multa);
    }
    
    [TestMethod]
    public void CalcularMulta_Con10DiasAtraso_Retorna10000()
    {
        // Arrange
        var prestamo = new Prestamo
        {
            FechaDevolucionEsperada = DateTime.Now.AddDays(-10)
        };
        
        // Act
        decimal multa = prestamo.CalcularMulta();
        
        // Assert
        Assert.AreEqual(10000, multa);
    }
}
```
---

## 🎯 Examen Final (70 min)

**Parte 1: Teórica (20 pts - 20 min)**

Preguntas sobre:
- Conceptos de POO (encapsulamiento, herencia, polimorfismo)
- Diferencias entre TDD, BDD, DDD
- Ciclo de vida de una request en ASP.NET MVC
- Conectado vs Desconectado en ADO.NET
- Cuándo usar cada formato de archivo (JSON, XML, CSV)

**Parte 2: Práctica (80 pts - 50 min)**

Implementar un mini-sistema con las siguientes características:

**Contexto:** Sistema de gestión de tareas

**Requisitos:**
1. Clase `Tarea` con propiedades: Id, Titulo, Descripcion, FechaCreacion, FechaVencimiento, Completada
2. Repositorio con ADO.NET que implemente:
   - Insertar nueva tarea
   - Marcar como completada
   - Obtener todas las tareas
3. Exportar tareas a JSON
4. Al menos 2 pruebas unitarias

**Tiempo:** 50 minutos  
**Entrega:** Archivo .zip con código fuente

---

## 📚 Recursos para el Proyecto Final

**Plantillas de código:**
- [Repositorio GitHub del curso](https://github.com/...)
- Ejemplos de cada unidad

**Herramientas recomendadas:**
- Visual Studio 2022 Community
- SQL Server Express
- Postman (si hacen API)
- Git para control de versiones

**Documentación:**
- [ASP.NET Core MVC](https://docs.microsoft.com/en-us/aspnet/core/mvc/)
- [ADO.NET Best Practices](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/ado-net-code-examples)
- [xUnit Testing](https://xunit.net/docs/getting-started)

---
## 🎯 Resumen del Semestre

**Lo que aprendimos:**

**Unidad 1 - POO en C#:**
- ✅ Clases, objetos, encapsulamiento
- ✅ Herencia y polimorfismo
- ✅ Interfaces y clases abstractas

**Unidad 2 - Técnicas de Desarrollo:**
- ✅ TDD con pruebas unitarias
- ✅ BDD para comportamiento
- ✅ DDD para dominio de negocio

**Unidad 3 - Desarrollo Web:**
- ✅ ASP.NET Core MVC
- ✅ HTML5 y Bootstrap
- ✅ Formularios y validación

**Unidad 4 - Persistencia:**
- ✅ ADO.NET conectado (SqlDataReader)
- ✅ CRUD completo
- ✅ Transacciones
- ✅ Archivos planos (JSON, XML, CSV)

---
## 🎯 Resumen del Semestre

**Unidad 5 - Datos Desconectados:**
- ✅ DataSet y DataTable
- ✅ DataAdapter
- ✅ DataBinding
- ✅ Exportación a XML

---

## 💬 Palabras Finales

¡Felicitaciones por completar POO II! 🎉

Han desarrollado habilidades fundamentales para cualquier desarrollador .NET:
- Programación orientada a objetos profesional
- Testing como práctica estándar
- Desarrollo web moderno
- Persistencia de datos robusta

**Próximos pasos sugeridos:**
1. Profundizar en Entity Framework (ORM moderno)
2. Aprender LINQ avanzado
3. APIs REST con Web API
4. Arquitecturas limpias (Clean Architecture)
5. Patrones de diseño

¡Éxitos en sus proyectos futuros! 🚀

---

**Fecha:** 2026-05-28 (Jueves) - ÚLTIMA CLASE  
**Profesor:** [Nombre]  
**Curso:** IF0100 - POO II  
**¡Gracias por un excelente semestre!** 🎓



---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, el estudiante será capaz de:

1. **Implementar** data binding bidireccional en Windows Forms
2. **Utilizar** archivos XML como fuente de datos
3. **Integrar** todas las tecnologías del curso en un proyecto final
4. **Aplicar** buenas prácticas de arquitectura de software (capas, patrones)
5. **Documentar** y presentar un proyecto completo

---

## 💻 Actividad Final: Proyecto Integrador

### Descripción del Proyecto

Desarrollar un **Sistema de Gestión Académica** que integre todos los conceptos del curso:

#### Tecnologías Obligatorias
- ✅ C# con POO avanzada
- ✅ Windows Forms / WPF
- ✅ ADO.NET con SQL Server
- ✅ Dataset y DataAdapter
- ✅ Data Binding
- ✅ Persistencia en XML (exportación)
- ✅ TDD (pruebas unitarias con xUnit/NUnit)

---

### Funcionalidades Mínimas

#### Módulo 1: Gestión de Estudiantes
- [x] CRUD completo (Create, Read, Update, Delete)
- [x] Validación de datos
- [x] Búsqueda y filtros
- [x] Exportar a XML

#### Módulo 2: Gestión de Cursos
- [x] CRUD de cursos
- [x] Asignación de estudiantes a cursos
- [x] Capacidad máxima por curso

#### Módulo 3: Gestión de Notas
- [x] Registrar calificaciones
- [x] Calcular promedios automáticamente
- [x] Generar reportes (top 10, estudiantes en riesgo)

#### Módulo 4: Reportes
- [x] Reporte de estudiantes por curso
- [x] Historial académico de estudiante
- [x] Estadísticas generales

---

### Entregables

| Entregable | Descripción | Peso |
|------------|-------------|------|
| **Código Fuente** | Proyecto completo en GitHub | 40% |
| **Base de Datos** | Script SQL con esquema y datos | 10% |
| **Pruebas Unitarias** | Cobertura >70% | 15% |
| **Documentación Técnica** | README, diagramas UML | 15% |
| **Presentación** | Demo de 15 min | 10% |
| **Video** | Screencast explicando arquitectura | 10% |

---
### Estructura del Proyecto

```
SistemaAcademico/
├── src/
│   ├── SistemaAcademico.Core/          # Lógica de negocio
│   │   ├── Entities/
│   │   │   ├── Estudiante.cs
│   │   │   ├── Curso.cs
│   │   │   └── Nota.cs
│   │   ├── Interfaces/
│   │   │   └── IEstudianteRepository.cs
│   │   └── Services/
│   │       └── EstudianteService.cs
│   │
│   ├── SistemaAcademico.Data/          # Acceso a datos
│   │   ├── Repositories/
│   │   │   └── EstudianteRepository.cs
│   │   └── AppDbContext.cs
│   │
│   ├── SistemaAcademico.UI/            # Interfaz gráfica
│   │   ├── Forms/
│   │   │   ├── frmEstudiantes.cs
│   │   │   └── frmCursos.cs
│   │   └── Program.cs
│   │
│   └── SistemaAcademico.Tests/         # Pruebas unitarias
│       └── EstudianteServiceTests.cs
│
├── database/
│   └── create_schema.sql
│
├── docs/
│   ├── README.md
│   ├── arquitectura.md
│   └── manual_usuario.pdf
│
└── SistemaAcademico.sln
```

---

## Estructura del Proyecto
### Ejemplo de Código: Data Binding Bidireccional

```csharp
// frmEstudiantes.cs
public partial class frmEstudiantes : Form
{
    private BindingSource bindingSource;
    private DataSet dsEstudiantes;
    private SqlDataAdapter dataAdapter;

    public frmEstudiantes()
    {
        InitializeComponent();
        ConfigurarDataBinding();
        CargarDatos();
    }

    private void ConfigurarDataBinding()
    {
        bindingSource = new BindingSource();
        
        // Binding bidireccional
        txtNombre.DataBindings.Add("Text", bindingSource, "Nombre", true, 
            DataSourceUpdateMode.OnPropertyChanged);
        txtApellido.DataBindings.Add("Text", bindingSource, "Apellido", true,
            DataSourceUpdateMode.OnPropertyChanged);
        txtEmail.DataBindings.Add("Text", bindingSource, "Email", true,
            DataSourceUpdateMode.OnPropertyChanged);
        numPromedio.DataBindings.Add("Value", bindingSource, "Promedio", true,
            DataSourceUpdateMode.OnPropertyChanged);

---
### Ejemplo de Código: Data Binding Bidireccional


        // DataGridView
        dgvEstudiantes.DataSource = bindingSource;
    }

    private void CargarDatos()
    {
        string connectionString = ConfigurationManager.ConnectionStrings["UniversidadDB"].ConnectionString;
        
        dsEstudiantes = new DataSet();
        
        using (var connection = new SqlConnection(connectionString))
        {
            dataAdapter = new SqlDataAdapter("SELECT * FROM Estudiantes", connection);
            
            // Comandos automáticos para INSERT, UPDATE, DELETE
            var commandBuilder = new SqlCommandBuilder(dataAdapter);
            
            dataAdapter.Fill(dsEstudiantes, "Estudiantes");
        }

        bindingSource.DataSource = dsEstudiantes.Tables["Estudiantes"];
    }

    private void btnGuardar_Click(object sender, EventArgs e)
    {
        try
        {
            // Validar cambios
            if (dsEstudiantes.HasChanges())
            {
                // Actualizar base de datos
                dataAdapter.Update(dsEstudiantes, "Estudiantes");
                dsEstudiantes.AcceptChanges();
                
---
### Ejemplo de Código: Data Binding Bidireccional


                MessageBox.Show("Cambios guardados exitosamente", "Éxito",
                    MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("No hay cambios para guardar", "Info",
                    MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
        catch (DBConcurrencyException ex)
        {
            MessageBox.Show("Conflicto de concurrencia. Otro usuario modificó los datos.",
                "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            CargarDatos(); // Recargar datos
        }
        catch (Exception ex)
        {
            MessageBox.Show($"Error al guardar: {ex.Message}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }

---
### Ejemplo de Código: Data Binding Bidireccional


    private void btnExportarXML_Click(object sender, EventArgs e)
    {
        using (var saveDialog = new SaveFileDialog())
        {
            saveDialog.Filter = "XML Files|*.xml";
            saveDialog.Title = "Exportar Estudiantes a XML";
            saveDialog.FileName = $"estudiantes_{DateTime.Now:yyyyMMdd}.xml";

            if (saveDialog.ShowDialog() == DialogResult.OK)
            {
                dsEstudiantes.Tables["Estudiantes"].WriteXml(saveDialog.FileName, XmlWriteMode.WriteSchema);
                MessageBox.Show("Exportación exitosa", "Éxito",
                    MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }

    private void btnImportarXML_Click(object sender, EventArgs e)
    {
        using (var openDialog = new OpenFileDialog())
        {
            openDialog.Filter = "XML Files|*.xml";
            openDialog.Title = "Importar Estudiantes desde XML";

---
### Ejemplo de Código: Data Binding Bidireccional


            if (openDialog.ShowDialog() == DialogResult.OK)
            {
                var dsImportado = new DataSet();
                dsImportado.ReadXml(openDialog.FileName);
                
                // Merge con datos existentes
                dsEstudiantes.Merge(dsImportado);
                
                MessageBox.Show($"Importados {dsImportado.Tables[0].Rows.Count} registros",
                    "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }

    private void btnNuevo_Click(object sender, EventArgs e)
    {
        bindingSource.AddNew();
    }

    private void btnEliminar_Click(object sender, EventArgs e)
    {
        if (MessageBox.Show("¿Eliminar este estudiante?", "Confirmar",
            MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
        {
            bindingSource.RemoveCurrent();
        }
    }

---
### Ejemplo de Código: Data Binding Bidireccional


    private void btnPrimero_Click(object sender, EventArgs e) => bindingSource.MoveFirst();
    private void btnAnterior_Click(object sender, EventArgs e) => bindingSource.MovePrevious();
    private void btnSiguiente_Click(object sender, EventArgs e) => bindingSource.MoveNext();
    private void btnUltimo_Click(object sender, EventArgs e) => bindingSource.MoveLast();
}
```

---

### Cronograma de Desarrollo

| Semana | Actividades |
|--------|-------------|
| **1-2** | Diseño de BD, modelos de entidades, interfaces |
| **3-4** | Implementación de repositorios y servicios |
| **5-6** | Desarrollo de interfaz gráfica (Windows Forms) |
| **7** | Pruebas unitarias y corrección de bugs |
| **8** | Documentación, video y preparación de presentación |

---

### Rúbrica de Evaluación Detallada

#### Arquitectura y Diseño (25 puntos)
- Separación de capas (Presentation, Business, Data) - 10 pts
- Uso de interfaces y abstracciones - 8 pts
- Patrones de diseño aplicados (Repository, Singleton, etc.) - 7 pts

#### Funcionalidad (30 puntos)
- CRUD completo funcional - 15 pts
- Validaciones robustas - 8 pts
- Manejo de errores - 7 pts

#### Calidad de Código (20 puntos)
- Código limpio y legible - 8 pts
- Naming conventions - 5 pts
- Comentarios y documentación inline - 7 pts

#### Pruebas (15 puntos)
- Cobertura >70% - 10 pts
- Tests bien diseñados (AAA pattern) - 5 pts

#### Presentación (10 puntos)
- Claridad en la explicación - 5 pts
- Dominio del tema - 5 pts

---

### Tiempo Total Estimado: 80 horas

**¡Éxito en su proyecto final!** 🎓

---

## DataGridView Avanzado - Personalización Completa

### Configuración profesional del grid

```csharp
using System.Windows.Forms;
using System.Drawing;

public class DataGridViewAvanzado : Form
{
    private DataGridView dgv;
    private BindingSource bindingSource;
    private ContextMenuStrip contextMenu;

    public DataGridViewAvanzado()
    {
        ConfigurarGrid();
        ConfigurarMenuContextual();
        ConfigurarEventos();
    }

    private void ConfigurarGrid()
    {
        dgv = new DataGridView
        {
            Dock = DockStyle.Fill,
            AutoGenerateColumns = false,
            AllowUserToAddRows = false,
            AllowUserToDeleteRows = false,
            ReadOnly = false,
            SelectionMode = DataGridViewSelectionMode.FullRowSelect,
            MultiSelect = false,
            GridColor = Color.LightGray,
            BorderStyle = BorderStyle.Fixed3D,
            CellBorderStyle = DataGridViewCellBorderStyle.SingleHorizontal,
            RowHeadersBorderStyle = DataGridViewHeaderBorderStyle.Single,
            ColumnHeadersBorderStyle = DataGridViewHeaderBorderStyle.Single,
            BackgroundColor = Color.White,
            AlternatingRowsDefaultCellStyle = new DataGridViewCellStyle
            {
                BackColor = Color.AliceBlue,
                ForeColor = Color.Black
            },
            DefaultCellStyle = new DataGridViewCellStyle
            {
                SelectionBackColor = Color.SteelBlue,
                SelectionForeColor = Color.White,
                Font = new Font("Segoe UI", 10F)
            },
            ColumnHeadersDefaultCellStyle = new DataGridViewCellStyle
            {
                BackColor = Color.Navy,
                ForeColor = Color.White,
                Font = new Font("Segoe UI", 10F, FontStyle.Bold),
                Alignment = DataGridViewContentAlignment.MiddleCenter
            },
            RowHeadersDefaultCellStyle = new DataGridViewCellStyle
            {
                BackColor = Color.Navy,
                ForeColor = Color.White,
                Font = new Font("Segoe UI", 9F)
            },
            EnableHeadersVisualStyles = false,
            RowTemplate = { Height = 24 }
        };

        // Modo de edición
        dgv.EditMode = DataGridViewEditMode.EditOnKeystrokeOrF2;
        dgv.BeginEdit += (s, e) => { Console.WriteLine("Editando fila"); };

        // Auto-sizing de columnas
        dgv.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.DisplayedCells;
        dgv.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.DisplayedCells;

        // Habilitar reorder de columnas
        dgv.AllowUserToOrderColumns = true;
        dgv.ColumnDisplayIndexChanged += (s, e) =>
        {
            Console.WriteLine($"Columna {e.Column.Name} movida a índice {e.NewDisplayIndex}");
        };

        // Habilitar resize de columnas
        dgv.AllowUserToResizeColumns = true;
        dgv.AllowUserToResizeRows = false;

        // Habilitar ordenamiento
        dgv.SortCompare += (s, e) =>
        {
            // Ordenamiento personalizado para promedios
            if (e.Column.Name == "Promedio")
            {
                e.SortResult = Comparer<decimal>.Default.Compare(
                    (decimal)e.CellValue1,
                    (decimal)e.CellValue2);
                e.Handled = true;
            }
        };

        // Configurar columnas manualmente
        ConfigurarColumnas();
    }

    private void ConfigurarColumnas()
    {
        // Columna ID (oculta o de solo lectura)
        DataGridViewTextBoxColumn colId = new DataGridViewTextBoxColumn
        {
            Name = "Id",
            HeaderText = "ID",
            DataPropertyName = "Id",
            Visible = false,  // No mostrar, pero sí existe
            ReadOnly = true
        };

        // Columna Código
        DataGridViewTextBoxColumn colCodigo = new DataGridViewTextBoxColumn
        {
            Name = "Codigo",
            HeaderText = "Código",
            DataPropertyName = "Codigo",
            Width = 100,
            ReadOnly = false,
            MaxInputLength = 20
        };

        // Columna Nombre
        DataGridViewTextBoxColumn colNombre = new DataGridViewTextBoxColumn
        {
            Name = "Nombre",
            HeaderText = "Nombre Completo",
            DataPropertyName = "Nombre",
            Width = 200,
            ReadOnly = false
        };

        // Columna Promedio (con formato)
        DataGridViewTextBoxColumn colPromedio = new DataGridViewTextBoxColumn
        {
            Name = "Promedio",
            HeaderText = "Promedio",
            DataPropertyName = "Promedio",
            Width = 100,
            DefaultCellStyle = new DataGridViewCellStyle
            {
                Format = "F2",
                Alignment = DataGridViewContentAlignment.MiddleRight,
                NullValue = "0.00"
            }
        };

        // Columna Activo (CheckBox)
        DataGridViewCheckBoxColumn colActivo = new DataGridViewCheckBoxColumn
        {
            Name = "Activo",
            HeaderText = "Activo",
            DataPropertyName = "Activo",
            Width = 60,
            TrueValue = true,
            FalseValue = false,
            IndeterminateValue = false
        };

        // Columna de imagen (opcional)
        DataGridViewImageColumn colImagen = new DataGridViewImageColumn
        {
            Name = "Foto",
            HeaderText = "Foto",
            ImageLayout = DataGridViewImageCellLayout.Zoom,
            Width = 60,
            ValuesAreIcons = false
        };

        // Columna de botón (acciones)
        DataGridViewButtonColumn colAcciones = new DataGridViewButtonColumn
        {
            Name = "Acciones",
            HeaderText = "",
            Text = "Ver",
            UseColumnTextForButtonValue = false,
            Width = 60
        };
        colAcciones.CellTemplate = new DataGridViewButtonCell();

        dgv.Columns.AddRange(new DataGridViewColumn[] {
            colId, colCodigo, colNombre, colPromedio, colActivo, colImagen, colAcciones
        });
    }

    private void ConfigurarMenuContextual()
    {
        contextMenu = new ContextMenuStrip();

        var tsmEditar = new ToolStripMenuItem("Editar", null, OnEditar);
        var tsmEliminar = new ToolStripMenuItem("Eliminar", null, OnEliminar);
        var tsmCopiar = new ToolStripMenuItem("Copiar", null, OnCopiar);
        var tsmDuplicar = new ToolStripMenuItem("Duplicar", null, OnDuplicar);

        contextMenu.Items.AddRange(new ToolStripItem[] { tsmEditar, tsmEliminar,
            new ToolStripSeparator(), tsmCopiar, tsmDuplicar });

        dgv.ContextMenuStrip = contextMenu;
    }

    private void ConfigurarEventos()
    {
        // Selección de fila
        dgv.SelectionChanged += (s, e) =>
        {
            if (dgv.SelectedRows.Count > 0)
            {
                var fila = dgv.SelectedRows[0];
                Console.WriteLine($"Seleccionado: ID={fila.Cells["Id"].Value}");
            }
        };

        // Click en celda
        dgv.CellClick += (s, e) =>
        {
            if (e.ColumnIndex == dgv.Columns["Acciones"].Index)
            {
                var id = dgv.Rows[e.RowIndex].Cells["Id"].Value;
                MessageBox.Show($"Acción para ID: {id}");
            }
        };

        // Validación de celda
        dgv.CellValidating += (s, e) =>
        {
            if (dgv.Columns[e.ColumnIndex].Name == "Promedio")
            {
                if (e.FormattedValue != null && decimal.TryParse(e.FormattedValue.ToString(), out decimal valor))
                {
                    if (valor < 0 || valor > 5)
                    {
                        e.Cancel = true;
                        dgv.Rows[e.RowIndex].ErrorText = "Promedio debe estar entre 0 y 5";
                    }
                }
            }
        };

        dgv.CellEndEdit += (s, e) =>
        {
            dgv.Rows[e.RowIndex].ErrorText = string.Empty;
        };

        // Formateo de celdas por valor
        dgv.CellFormatting += (s, e) =>
        {
            if (dgv.Columns[e.ColumnIndex].Name == "Promedio")
            {
                if (e.Value != null && e.Value != DBNull.Value)
                {
                    decimal promedio = (decimal)e.Value;
                    e.CellStyle.BackColor = promedio >= 4.0 ? Color.PaleGreen :
                                                 promedio >= 3.0 ? Color.Yellow : Color.IndianRed;
                }
            }

            if (dgv.Columns[e.ColumnIndex].Name == "Activo")
            {
                // Mostrar check verde/rojo
                var cell = dgv.Rows[e.RowIndex].Cells[e.ColumnIndex];
                if (cell.Value != null && (bool)cell.Value)
                {
                    e.CellStyle.BackColor = Color.LightGreen;
                }
            }
        };

        // DataError para errores de conversión
        dgv.DataError += (s, e) =>
        {
            MessageBox.Show($"Error: {e.Exception.Message}", "Error de datos",
                MessageBoxButtons.OK, MessageBoxIcon.Warning);
            e.ThrowException = false;
        };
    }

    private void OnEditar(object sender, EventArgs e) => EditarFilaSeleccionada();
    private void OnEliminar(object sender, EventArgs e) => EliminarFilaSeleccionada();
    private void OnCopiar(object sender, EventArgs e) => CopiarFilaSeleccionada();
    private void OnDuplicar(object sender, EventArgs e) => DuplicarFilaSeleccionada();

    private void EditarFilaSeleccionada()
    {
        if (dgv.SelectedRows.Count > 0)
        {
            var id = dgv.SelectedRows[0].Cells["Id"].Value;
            // Abrir formulario de edición
        }
    }

    // Filtrado en tiempo real
    public void FiltrarDatos(string texto)
    {
        if (string.IsNullOrEmpty(texto))
        {
            bindingSource.RemoveFilter();
        }
        else
        {
            bindingSource.Filter = $"Nombre LIKE '%{texto}%' OR Codigo LIKE '%{texto}%'";
        }
    }
}
```

---

## XML Serialization Avanzada

### Atributos de serialización personalizados

```csharp
using System;
using System.Xml.Serialization;
using System.IO;
using System.Collections.Generic;

namespace UniversidadApp.Serialization
{
    /// <summary>
    /// Clase con atributos de serialización XML personalizados
    /// </summary>
    [XmlRoot("Universidad", Namespace = "http://www.unaula.edu.co/esquema")]
    public class Universidad
    {
        [XmlElement("Estudiante")]
        [XmlElement("Alumno")]  // Permite ambos nombres en XML
        public List<Estudiante> Estudiantes { get; set; } = new List<Estudiante>();

        [XmlAttribute("Nombre")]
        public string NombreInstitucion { get; set; }

        [XmlAttribute("AnioFundacion")]
        public int AnioFundacion { get; set; }
    }

    public class Estudiante
    {
        [XmlAttribute("Id")]
        public int Id { get; set; }

        [XmlAttribute("Codigo")]
        public string Codigo { get; set; }

        [XmlElement("NombreCompleto")]
        public string Nombre { get; set; }

        [XmlElement("Correo")]
        [XmlElement("Email")]  // Alias
        public string Email { get; set; }

        [XmlIgnore]  // Ignorar propiedad en serialización
        public string Password { get; set; }

        [XmlArray("Notas")]
        [XmlArrayItem("Nota")]
        public List<decimal> Calificaciones { get; set; } = new List<decimal>();

        [XmlIgnore]
        public decimal Promedio
        {
            get
            {
                if (Calificaciones.Count == 0)
                    return 0;
                return Calificaciones.Sum() / Calificaciones.Count;
            }
        }

        // Propiedad con nombre diferente en XML
        [XmlElement("FechaDeNacimiento")]
        public DateTime FechaNacimiento { get; set; }

        // Tipo enumerado
        [XmlElement("Estado")]
        public EstadoEstudiante Estado { get; set; }
    }

    public enum EstadoEstudiante
    {
        [XmlEnum("Activo")]
        Activo = 1,

        [XmlEnum("Inactivo")]
        Inactivo = 2,

        [XmlEnum("Graduado")]
        Graduado = 3
    }

    /// <summary>
    /// Serializador con opciones
    /// </summary>
    public class XmlSerializerHelper
    {
        public static void Serializar(T obj, string archivo, bool indentar = true)
        {
            var serializer = new XmlSerializer(typeof(T));

            var opciones = new XmlWriterSettings
            {
                Indent = indentar,
                IndentChars = "  ",
                NewLineOnAttributes = false,
                OmitXmlDeclaration = false,
                ConformanceLevel = ConformanceLevel.Document
            };

            using var writer = XmlWriter.Create(archivo, opciones);
            var namespaces = new XmlSerializerNamespaces();
            namespaces.Add("xsd", "http://www.w3.org/2001/XMLSchema");

            serializer.Serialize(writer, obj, namespaces);
        }

        public static T Deserializar(string archivo)
        {
            var serializer = new XmlSerializer(typeof(T));

            using var reader = new StreamReader(archivo);
            return (T)serializer.Deserialize(reader);
        }

        // Serializar a string
        public static string SerializarToString(T obj)
        {
            var serializer = new XmlSerializer(typeof(T));

            using var stringWriter = new StringWriter();
            using var writer = XmlWriter.Create(stringWriter, new XmlWriterSettings
            {
                Indent = true,
                OmitXmlDeclaration = false
            });

            serializer.Serialize(writer, obj);
            return stringWriter.ToString();
        }

        // Deserializar desde string
        public static T DeserializarDesdeString(string xml)
        {
            var serializer = new XmlSerializer(typeof(T));

            using var stringReader = new StringReader(xml);
            return (T)serializer.Deserialize(stringReader);
        }
    }

    // Uso
    class Program
    {
        static void Main()
        {
            var universidad = new Universidad
            {
                NombreInstitucion = "UNAULA",
                AnioFundacion = 1995,
                Estudiantes = new List<Estudiante>
                {
                    new Estudiante
                    {
                        Id = 1,
                        Codigo = "EST001",
                        Nombre = "Juan Pérez",
                        Email = "juan@unaula.edu.co",
                        Password = "secreto",  // No se serializa
                        Calificaciones = new List<decimal> { 4.2m, 3.8m, 4.5m },
                        FechaNacimiento = new DateTime(2000, 5, 15),
                        Estado = EstadoEstudiante.Activo
                    }
                }
            };

            // Serializar
            XmlSerializerHelper.Serializar(universidad, "universidad.xml");

            // Deserializar
            var universidadCargada = XmlSerializerHelper.Deserializar<Universidad>("universidad.xml");

            Console.WriteLine($"Institución: {universidadCargada.NombreInstitucion}");
            Console.WriteLine($"Estudiantes: {universidadCargada.Estudiantes.Count}");
        }
    }
}

/* XML generado (universidad.xml):
<?xml version="1.0" encoding="utf-8"?>
<Universidad xmlns:xsd="http://www.w3.org/2001/XMLSchema"
           Nombre="UNAULA"
           AnioFundacion="1995"
           xmlns="http://www.unaula.edu.co/esquema">
  <Estudiante Id="1" Codigo="EST001">
    <NombreCompleto>Juan Pérez</NombreCompleto>
    <Email>juan@unaula.edu.co</Email>
    <FechaDeNacimiento>2000-05-15T00:00:00</FechaDeNacimiento>
    <Estado>Activo</Estado>
    <Notas>
      <Nota>4.2</Nota>
      <Nota>3.8</Nota>
      <Nota>4.5</Nota>
    </Notas>
  </Estudiante>
</Universidad>
*/
```

---

## ConcurrentDictionary - Datos Compartidos en Memoria

### Caché de datos thread-safe para aplicaciones web

```csharp
using System;
using System.Collections.Concurrent;
using System.Linq;

namespace UniversidadApp.Cache
{
    /// <summary>
    /// Caché thread-safe usando ConcurrentDictionary
    /// Ideal para aplicaciones web con múltiples usuarios concurrentes
    /// </summary>
    public class EstudianteCache
    {
        private readonly ConcurrentDictionary<int, Estudiante> _cache;
        private readonly TimeSpan _tiempoExpiracion;
        private readonly ConcurrentDictionary<int, DateTime> _expiraciones;

        public EstudianteCache(TimeSpan? tiempoExpiracion = null)
        {
            _cache = new ConcurrentDictionary<int, Estudiante>();
            _expiraciones = new ConcurrentDictionary<int, DateTime>();
            _tiempoExpiracion = tiempoExpiracion ?? TimeSpan.FromMinutes(30);
        }

        public void AgregarOActualizar(int id, Estudiante estudiante)
        {
            _cache.AddOrUpdate(id,
                addKey: estudiante,
                updateKeyFactory: (key, existing) => estudiante);

            _expiraciones.AddOrUpdate(id,
                addKey: DateTime.Now.Add(_tiempoExpiracion),
                updateKeyFactory: (key, existing) => DateTime.Now.Add(_tiempoExpiracion));
        }

        public bool Obtener(int id, out Estudiante estudiante)
        {
            // Verificar expiración
            if (_expiraciones.TryGetValue(id, out var expiracion))
            {
                if (DateTime.Now > expiracion)
                {
                    Remover(id);
                    estudiante = null;
                    return false;
                }
            }

            return _cache.TryGetValue(id, out estudiante);
        }

        public bool Remover(int id)
        {
            _expiraciones.TryRemove(id, out _);
            return _cache.TryRemove(id, out _);
        }

        public void Limpiar()
        {
            _cache.Clear();
            _expiraciones.Clear();
        }

        public void LimpiarExpirados()
        {
            var ahora = DateTime.Now;
            var expirados = _expiraciones.Where(kvp => kvp.Value < ahora).Select(kvp => kvp.Key).ToList();

            foreach (var id in expirados)
            {
                Remover(id);
            }
        }

        public int Total => _cache.Count;

        // Obtener o crear (carga diferida)
        public Estudiante ObtenerOCrear(int id, Func<int, Estudiante> factory)
        {
            return _cache.GetOrAdd(id, factory);
        }

        // Obtener múltiples
        public Estudiante[] ObtenerTodos()
        {
            LimpiarExpirados();
            return _cache.Values.ToArray();
        }

        // Agregar lote
        public void AgregarLote(IEnumerable<Estudiante> estudiantes)
        {
            foreach (var est in estudiantes)
            {
                AgregarOActualizar(est.Id, est);
            }
        }
    }

    // Uso en aplicación web
    public class GlobalCache
    {
        public static EstudianteCache Estudiantes { get; } = new EstudianteCache();

        // En Global.asax o Startup
        public static void Inicializar()
        {
            // Cargar datos al inicio
            var estudiantes = CargarEstudiantesDesdeBD();
            Estudiantes.AgregarLote(estudiantes);
        }

        private static Estudiante[] CargarEstudiantesDesdeBD()
        {
            // Cargar desde ADO.NET
            return new Estudiante[0];
        }
    }
}
```

---

## Patrones de Diseño para el Proyecto Final

### Patrones recomendados por Microsoft

```csharp
// ========== Repository Pattern ==========
// Abstrae el acceso a datos
public interface IEstudianteRepository
{
    Estudiante ObtenerPorId(int id);
    IEnumerable<Estudiante> ObtenerTodos();
    void Agregar(Estudiante estudiante);
    void Actualizar(Estudiante estudiante);
    void Eliminar(int id);
}

public class EstudianteRepository : IEstudianteRepository
{
    private readonly string _connectionString;

    public Estudiante ObtenerPorId(int id)
    {
        // Implementación ADO.NET
        return null;
    }

    // ... otros métodos
}

// ========== Unit of Work Pattern ==========
// Agrupa múltiples repositorios en una sola transacción
public interface IUnitOfWork : IDisposable
{
    IEstudianteRepository Estudiantes { get; }
    ICursoRepository Cursos { get; }
    IMatriculaRepository Matriculas { get; }
    void Commit();
    void Rollback();
}

public class SqlUnitOfWork : IUnitOfWork
{
    private readonly SqlTransaction _transaction;
    private readonly SqlConnection _connection;

    public IEstudianteRepository Estudiantes { get; }
    public ICursoRepository Cursos { get; }
    public IMatriculaRepository Matriculas { get; }

    public void Commit()
    {
        try
        {
            _transaction.Commit();
        }
        catch
        {
            _transaction.Rollback();
            throw;
        }
    }

    public void Rollback()
    {
        _transaction.Rollback();
    }

    public void Dispose()
    {
        _transaction?.Dispose();
        _connection?.Dispose();
    }
}

// ========== Service Layer Pattern ==========
// Lógica de negocio separada del acceso a datos
public interface IEstudianteService
{
    Estudiante RegistrarEstudiante(NuevoEstudianteDto dto);
    void ActualizarPromedio(int estudianteId);
    IReadOnlyList<Estudiante> ObtenerEstudiantesDestacados();
}

public class EstudianteService : IEstudianteService
{
    private readonly IEstudianteRepository _repository;
    private readonly IUnitOfWork _unitOfWork;
    private readonly INotificationService _notification;

    public Estudiante RegistrarEstudiante(NuevoEstudianteDto dto)
    {
        // Validaciones de negocio
        if (_repository.ObtenerPorCodigo(dto.Codigo) != null)
            throw new Exception("Código ya existe");

        var estudiante = new Estudiante
        {
            Codigo = dto.Codigo,
            Nombre = dto.Nombre,
            // ...
        };

        _repository.Agregar(estudiante);
        _unitOfWork.Commit();

        _notification.EnviarBienvenida(estudiante.Email);

        return estudiante;
    }
}

// ========== Factory Pattern ==========
// Creación de objetos complejos
public interface IEstudianteFactory
{
    Estudiante CrearRegular(string codigo, string nombre);
    Estudiante CrearBecado(string codigo, string nombre);
}

public class EstudianteFactory : IEstudianteFactory
{
    public Estudiante CrearRegular(string codigo, string nombre)
    {
        return new Estudiante
        {
            Codigo = codigo,
            Nombre = nombre,
            Tipo = TipoEstudiante.Regular,
            FechaRegistro = DateTime.Now
        };
    }

    public Estudiante CrearBecado(string codigo, string nombre)
    {
        return new Estudiante
        {
            Codigo = codigo,
            Nombre = nombre,
            Tipo = TipoEstudiante.Becado,
            FechaRegistro = DateTime.Now,
            Beneficios = new[] { "Beca20", "Transporte" }
        };
    }
}

// ========== Singleton Pattern ==========
// Una sola instancia de configuración
public sealed class ConfiguracionAplicacion
{
    private static readonly Lazy<ConfiguracionApp> _instance =
        new Lazy<ConfiguracionApp>(() => new ConfiguracionApp());

    public static ConfiguracionAplicacion Instance => _instance.Value;

    private ConfiguracionAplicacion() { }

    public string ConnectionString { get; set; }
    public string ApiKey { get; set; }
    public int TimeoutSegundos { get; set; } = 30;
}

// ========== Strategy Pattern ==========
// Algoritmos intercambiables
public interface ICalculoPromedio
{
    decimal Calcular(decimal[] notas);
}

public class PromedioSimple : ICalculoPromedio
{
    public decimal Calcular(decimal[] notas)
    {
        return notas.Average();
    }
}

public class PromedioPonderado : ICalculoPromedio
{
    private readonly decimal[] _pesos;

    public PromedioPonderado(decimal[] pesos)
    {
        _pesos = pesos;
    }

    public decimal Calcular(decimal[] notas)
    {
        decimal suma = 0;
        decimal totalPesos = 0;

        for (int i = 0; i < notas.Length; i++)
        {
            suma += notas[i] * _pesos[i];
            totalPesos += _pesos[i];
        }

        return suma / totalPesos;
    }
}

public class CalculadoraPromedio
{
    private ICalculoPromedio _estrategia;

    public void SetEstrategia(ICalculoPromedio estrategia)
    {
        _estrategia = estrategia;
    }

    public decimal Calcular(decimal[] notas)
    {
        return _estrategia.Calcular(notas);
    }
}
```

---

## Logging y Auditoría

### Sistema de logs para el proyecto

```csharp
using System;
using System.IO;

namespace UniversidadApp.Logging
{
    /// <summary>
    /// Logger simple para aplicaciones de escritorio
    /// </summary>
    public class Logger
    {
        private static readonly Lazy<Logger> _instance =
            new Lazy<Logger>(() => new Logger());

        public static Logger Instance => _instance.Value;

        private readonly string _logPath;
        private readonly object _lock = new object();

        private Logger()
        {
            var appData = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            var logDir = Path.Combine(appData, "UniversidadApp", "Logs");
            Directory.CreateDirectory(logDir);

            _logPath = Path.Combine(logDir, $"app_{DateTime.Now:yyyyMMdd}.log");
        }

        public void Info(string mensaje)
        {
            EscribirLog("INFO", mensaje);
        }

        public void Warning(string mensaje)
        {
            EscribirLog("WARN", mensaje);
        }

        public void Error(string mensaje, Exception ex = null)
        {
            var mensajeCompleto = ex != null
                ? $"{mensaje}: {ex.Message}\n{ex.StackTrace}"
                : mensaje;

            EscribirLog("ERROR", mensajeCompleto);
        }

        public void Debug(string mensaje)
        {
            #if DEBUG
            EscribirLog("DEBUG", mensaje);
            #endif
        }

        public void Auditoria(string usuario, string accion, string detalles)
        {
            var mensaje = $"[{usuario}] {accion}: {detalles}";
            EscribirLog("AUDIT", mensaje);
        }

        private void EscribirLog(string nivel, string mensaje)
        {
            lock (_lock)
            {
                var entrada = $"[{DateTime.Now:yyyy-MM-dd HH:mm:ss.fff}] [{nivel}] {mensaje}";
                File.AppendAllText(_logPath, entrada + Environment.NewLine);
            }
        }

        public string[] ObtenerUltimosLogs(int cantidad = 100)
        {
            if (!File.Exists(_logPath))
                return Array.Empty<string>();

            var lineas = File.ReadAllLines(_logPath);
            return lineas.TakeLast(cantidad).ToArray();
        }
    }

    // Uso
    class Program
    {
        static void Main()
        {
            var logger = Logger.Instance;

            logger.Info("Aplicación iniciada");
            logger.Debug("Modo depuración activado");

            try
            {
                // Operación que puede fallar
                int resultado = Dividir(10, 0);
            }
            catch (Exception ex)
            {
                logger.Error("Error en división", ex);
            }

            logger.Auditoria("admin", "ELIMINAR", "Estudiante ID=123");
            logger.Info("Aplicación finalizada");
        }

        static int Dividir(int a, int b) => a / b;
    }
}
```

---


