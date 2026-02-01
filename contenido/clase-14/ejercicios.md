# Ejercicios - Archivos Planos

**IF0100 - Lenguaje de Programación OO II**

---

## Ejercicio 1: Exportar a CSV

Exportar lista de estudiantes a CSV con encoding UTF-8.

---

## Ejercicio 2: Importar desde JSON

Leer archivo JSON de productos y cargar en BD.

---

## Ejercicio 3: Logger en Archivo

Implementar logger que escriba en archivo de texto con fecha.

```csharp
public void Log(string mensaje)
{
    var linea = $"[{DateTime.Now:yyyy-MM-dd HH:mm:ss}] {mensaje}";
    File.AppendAllText("log.txt", linea + Environment.NewLine);
}
```

---

**Última actualización:** 2026-02-01
