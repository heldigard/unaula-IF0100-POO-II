# Teoría - DataSet y DataAdapter

**IF0100 - Lenguaje de Programación OO II**

---

## Datos Desconectados

### Arquitectura

```
┌─────────┐  Fill  ┌───────────┐  Editar  ┌─────────┐
│ BD      │───────▶│  DataSet  │─────────▶│ Usuario │
└─────────┘         └───────────┘         └─────────┘
                      ▲  │
                      │  │ Update
                      │ └───────────────
                      │
                ┌─────┴─────────┐
                │ DataAdapter   │
                └───────────────┘
```

### Componentes

| Componente | Descripción |
|-------------|-------------|
| **DataSet** | Contiene DataTables en memoria |
| **DataTable** | Tabla de datos en memoria |
| **DataAdapter** | Puente entre BD y DataSet |
| **DataRelation** | Relaciones entre DataTables |

---

## DataSet vs DataReader

| Aspecto | DataSet | DataReader |
|---------|---------|------------|
| **Conexión** | Desconectado | Conectado |
| **Velocidad** | Más lento | Más rápido |
| **Uso ideal** | UI, binding | Procesamiento secuencial |
| **Memoria** | Mayor consumo | Menor consumo |

---

**Última actualización:** 2026-02-01
