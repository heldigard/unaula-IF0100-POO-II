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

# DataBinding y XML

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 75 minutos

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta clase, el estudiante será capaz de:

1. **Implementar** data binding bidireccional en Windows Forms
2. **Utilizar** archivos XML como fuente de datos
3. **Exportar** e importar datos usando DataSet y XML
4. **Aplicar** BindingSource para sincronización de controles

---

## 📋 Contenido

### 1. Data Binding - Enlace de Datos (30 min)

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

### 2. DataSet y XML (30 min)

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

### 3. DataBinding con ADO.NET (15 min)

**Integración completa con base de datos:**

```csharp
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
            if (dsEstudiantes.HasChanges())
            {
                dataAdapter.Update(dsEstudiantes, "Estudiantes");
                dsEstudiantes.AcceptChanges();

                MessageBox.Show("Cambios guardados exitosamente", "Éxito",
                    MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
        catch (DBConcurrencyException ex)
        {
            MessageBox.Show("Conflicto de concurrencia. Otro usuario modificó los datos.",
                "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            CargarDatos();
        }
        catch (Exception ex)
        {
            MessageBox.Show($"Error al guardar: {ex.Message}", "Error",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }

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
}
```

---

## 🎯 Resumen de la Clase

### 📚 Conceptos Clave

| Tema | Descripción |
|------|-------------|
| **BindingSource** | Componente intermediario entre datos y controles UI |
| **Data Binding** | Enlace automático bidireccional de datos |
| **DataSet.WriteXml()** | Exporta datos a formato XML |
| **DataSet.ReadXml()** | Importa datos desde XML |
| **SqlDataAdapter** | Llena DataSet y actualiza BD automáticamente |

### 🎯 Habilidades Adquiridas

- ✅ Implementar BindingSource para sincronizar controles
- ✅ Exportar DataSet a XML con esquema
- ✅ Importar datos desde XML a DataSet
- ✅ Integrar ADO.NET con DataBinding completo

---

## 📝 Ejercicios Propuestos

### 1. Aplicación de Gestión

Crear una app de gestión de productos con:
- DataGridView para listar productos
- TextBoxes para editar producto seleccionado
- Botones para CRUD completo
- Exportar a XML

### 2. XML Personalizado

Crear un serializador XML personalizado con atributos:
- `[XmlRoot]`, `[XmlElement]`, `[XmlAttribute]`
- `[XmlIgnore]` para propiedades sensibles
- Exportar/importar objetos complejos

### 3. 🌟 Integración Completa

Aplicación con:
- BindingSource + ADO.NET
- Exportar/importar XML
- Navegación (MoveFirst, MoveNext, etc.)
- Filtrado en tiempo real

---

## 🎓 Próxima Clase: Proyecto Final Integración

### Temas Clase 17

- ✅ Especificación del proyecto final
- ✅ Estructura del proyecto en capas
- ✅ Patrones de diseño recomendados
- ✅ Requerimientos funcionales y técnicos
- ✅ Rúbrica de evaluación

### 📖 Preparación

**Revisar todos los temas del semestre:**
- POO en C# (Unidad 1)
- TDD/BDD/DDD (Unidad 2)
- ASP.NET MVC (Unidad 3)
- ADO.NET (Unidad 4)
- DataSet y DataBinding (Unidad 5)

---

<!-- _class: lead -->

# ¡Gracias!
## ¿Preguntas?

**UNAULA - Ingeniería Informática - 2026-I**
