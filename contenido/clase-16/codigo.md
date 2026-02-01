# Código - DataBinding y XML

**IF0100 - Lenguaje de Programación OO II**

---

## 1. DataBinding Windows Forms

```csharp
public partial class EstudiantesForm : Form
{
    private DataTable _estudiantesTable;

    public EstudiantesForm()
    {
        InitializeComponent();
        CargarDatos();
    }

    private void CargarDatos()
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            var adapter = new SqlDataAdapter("SELECT * FROM Estudiantes", connection);
            _estudiantesTable = new DataTable();
            adapter.Fill(_estudiantesTable);
        }

        // DataBinding
        txtCodigo.DataBindings.Add("Text", _estudiantesTable, "Codigo");
        txtNombre.DataBindings.Add("Text", _estudiantesTable, "Nombre");
        txtEmail.DataBindings.Add("Text", _estudiantesTable, "Email");

        // Navegación
        var bindingSource = new BindingSource(_estudiantesTable, "");
        dgvEstudiantes.DataSource = bindingSource;
    }

    private void btnGuardar_Click(object sender, EventArgs e)
    {
        // Actualizar cambios a BD
        using (var connection = new SqlConnection(_connectionString))
        {
            var adapter = new SqlDataAdapter("SELECT * FROM Estudiantes", connection);
            var builder = new SqlCommandBuilder(adapter);
            adapter.Update(_estudiantesTable);
        }

        MessageBox.Show("Datos guardados");
    }
}
```

---

## 2. XML Serialización

```csharp
// DataSet a XML
dataSet.WriteXml("estudiantes.xml", XmlWriteMode.WriteSchema);

// Leer XML
var dataSet = new DataSet();
dataSet.ReadXml("estudiantes.xml");

// XmlDocument
var doc = new XmlDocument();
doc.Load("estudiantes.xml");

// LINQ to XML
var xml = XElement.Load("estudiantes.xml");
var nombres = xml.Descendants("Estudiante")
    .Select(e => e.Element("Nombre").Value);
```

---

**Última actualización:** 2026-02-01
