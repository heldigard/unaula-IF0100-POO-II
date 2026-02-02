# Teoría - Proyecto Final

**IF0100 - Lenguaje de Programación OO II**

---

## Proyecto Final

### Especificación

Sistema completo que integre todos los temas del curso:

| Unidad | Componente |
|--------|------------|
| **Unidad 1** | Clases, herencia, polimorfismo |
| **Unidad 2** | TDD/BDD, pruebas unitarias |
| **Unidad 3** | ASP.NET Core, HTML5, Bootstrap |
| **Unidad 4** | ADO.NET, SQL Server |
| **Unidad 5** | DataSet, DataBinding |

### Arquitectura

```
┌─────────────────────────────────────┐
│       ASP.NET CORE WEB APP         │
├─────────────────────────────────────┤
│  Controllers / Razor Pages         │
│  ┌───────────────────────────────┐ │
│  │ Services (BDD/TDD)            │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Repositories (ADO.NET)         │ │
│  └───────────────────────────────┘ │
│  ┌───────────────────────────────┐ │
│  │ Domain Models (POO)           │ │
│  └───────────────────────────────┘ │
├─────────────────────────────────────┤
│  SQL Server Database               │
└─────────────────────────────────────┘
```

---

## Entregables

1. **Código fuente** completo y funcional
2. **Script SQL** de la base de datos
3. **Pruebas unitarias** (xUnit)
4. **Documentación** (README.md)
5. **Sustentación** del proyecto

---

**Última actualización:** 2026-02-01
