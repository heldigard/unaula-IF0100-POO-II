# Teoría - DataBinding y XML

**IF0100 - Lenguaje de Programación OO II**

---

## DataBinding

### Concepto

Vincular datos a controles de UI automáticamente.

```
DATOS ─────binding────▶ CONTROLES UI
  ↑                         ↓
  └─────────actualiza────────┘
```

### Tipos

| Tipo | Descripción |
|------|-------------|
| **Simple** | Propiedad individual |
| **List** | ComboBox, ListBox |
| **Grid** | DataGridView, GridView |

---

## XML en ADO.NET

### DataSet a XML

```csharp
// Escribir XML
dataSet.WriteXml("datos.xml");
dataSet.WriteXmlSchema("esquema.xsd");

// Leer XML
dataSet.ReadXml("datos.xml");
```

---

## DataBinding en ASP.NET

```aspx
<asp:GridView ID="gvEstudiantes" runat="server"
    AutoGenerateColumns="false"
    DataKeyNames="Codigo">
    <Columns>
        <asp:BoundField DataField="Codigo" HeaderText="Código" />
        <asp:BoundField DataField="Nombre" HeaderText="Nombre" />
        <asp:BoundField DataField="Email" HeaderText="Email" />
    </Columns>
</asp:GridView>
```

```csharp
gvEstudiantes.DataSource = dataSet.Tables["Estudiantes"];
gvEstudiantes.DataBind();
```

---

**Última actualización:** 2026-02-01
