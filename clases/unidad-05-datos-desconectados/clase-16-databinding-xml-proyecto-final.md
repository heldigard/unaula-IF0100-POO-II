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

---

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
        
---
### 1. Data Binding - Enlace de Datos (20 min)


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
        
---
### 1. Data Binding - Enlace de Datos (20 min)


        // Agregar labels
        Controls.Add(new Label { Text = "Nombre:", Location = new Point(20, 323) });
        Controls.Add(new Label { Text = "Apellido:", Location = new Point(20, 353) });
        Controls.Add(new Label { Text = "Email:", Location = new Point(20, 383) });
        
        // Agregar controles al form
        Controls.Add(dgvEstudiantes);
        Controls.Add(txtNombre);
---
## 📋 Contenido
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
        
---
## 📋 Contenido


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
    
---
## 📋 Contenido


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

---
## 📋 Contenido


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
    
---
### 2. DataSet y XML (20 min)


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
        
---
### 2. DataSet y XML (20 min)


        DataTable dtEstudiantes = new DataTable("Estudiantes");
        dtEstudiantes.Columns.Add("Id", typeof(int));
        dtEstudiantes.Columns.Add("Nombre", typeof(string));
        dtEstudiantes.Columns.Add("Promedio", typeof(decimal));
        
        dtEstudiantes.Rows.Add(1, "Juan Pérez", 4.2m);
---
        
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

---



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

---
### 3. Proyecto Integrador - Especificación (15 min)


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
---
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

---



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
            
---
### 4. Integración de Conocimientos (20 min)


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
                    
---
### 4. Integración de Conocimientos (20 min)


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
        
---
### 4. Integración de Conocimientos (20 min)


        return prestamoId;
    }
    
    public void RegistrarDevolucion(int prestamoId)
    {
        using (SqlConnection conn = new SqlConnection(connectionString))
        {
            conn.Open();
---
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
                    
---



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
                    
---



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

---



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
        
---



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

