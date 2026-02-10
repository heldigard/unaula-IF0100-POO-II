# Ejercicios - Domain-Driven Design (DDD)

**IF0100 - Lenguaje de Programación OO II**

---

## Ejercicio 1: Crear Value Objects

Crear los siguientes Value Objects:

1. **Direccion**: con calle, ciudad, codigo_postal
2. **Telefono**: con numero y validacion de formato
3. **Monto**: con valor, moneda y operaciones matematicas

### Plantilla

```python
@dataclass(frozen=True)
class Direccion:
    """Value Object para direccion."""
    calle: str
    ciudad: str
    codigo_postal: str

    def __post_init__(self):
        if not self.calle:
            raise ValueError("Calle requerida")
```

---

## Ejercicio 2: Implementar Entidad Tarea

Crear la entidad Tarea con:

- ID unico
- titulo, descripcion, estado, prioridad
- Metodos: asignar_a(), marcar_completada(), esta_atrasada()
- Reglas de negocio:
  - No se puede reasignar tarea completada
  - No se puede completar tarea sin asignar

---

## Ejercicio 3: Repository con Archivos JSON

Implementar un repositorio que persista datos en JSON.

```python
class UsuarioFileRepository(UsuarioRepository):
    """Implementación usando archivos JSON."""

    def __init__(self, archivo: str = "data/usuarios.json"):
        self.archivo = archivo
        self._datos = self._cargar_datos()

    def _cargar_datos(self):
        """Carga datos desde archivo."""
        # Implementar...

    def guardar(self, usuario: Usuario) -> Usuario:
        """Guarda usuario en archivo."""
        # Implementar...
```

---

## Ejercicio 4: Refactorizar a DDD

Tomar codigo existente sin DDD y refactorizarlo.

### Codigo "Antes" (sin DDD)

```python
class UsuarioService:
    def crear_usuario(self, username, email, password):
        if len(username) < 3:
            raise ValueError("Username muy corto")

        import sqlite3
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios...", ...)
        conn.close()
```

### Codigo "Despues" (con DDD)

Separar en:
- Entidad Usuario
- Value Objects (Email)
- Repository (abstraccion)
- Service (logica de negocio)

---

**Última actualización:** 2026-02-08
