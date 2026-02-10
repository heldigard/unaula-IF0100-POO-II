# Evaluación 4 - IF0100: Persistencia con SQLAlchemy

**Curso:** IF0100 - Lenguaje de Programación OO II
**Tipo:** Examen práctico (individual)
**Porcentaje:** 15%
**Fecha:** 2026-04-23 (Jueves)
**Duración:** 1 hora
**Modalidad:** En laboratorio

---

## 🎯 Objetivo

Evaluar la capacidad de implementar operaciones de persistencia de datos usando SQLAlchemy con PostgreSQL o SQLite, incluyendo conexión, CRUD, relaciones y transacciones.

---

## 📝 Estructura del Examen

### Preparación (proporcionada por el profesor)

Se proporcionará una base de datos con la siguiente estructura:

```python
# models/producto.py
from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200))

    productos = relationship("Producto", back_populates="categoria")

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500))
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    activo = Column(Boolean, default=True)

    categoria = relationship("Categoria", back_populates="productos")

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)
    total = Column(Numeric(10, 2), nullable=False)
    fecha_venta = Column(DateTime(timezone=True), server_default=func.now())
```

---

### Parte A: Conexión y Consultas (30 pts)

**1. (10 pts) Crear clase de conexión:**

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

# Implemente una clase de conexión que:
# - Maneje el DATABASE_URL de forma segura
# - Tenga método para obtener sesión
# - Use context manager correctamente

DATABASE_URL = "sqlite:///./tienda.db"  # o postgresql://...

engine = create_engine(DATABASE_URL, ...)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    """Dependencia para obtener sesión de base de datos."""
    pass
```

**2. (10 pts) Consulta con filtros:**

```python
# repositories/producto_repository.py
from sqlalchemy.orm import Session
from typing import List, Optional
from models.producto import Producto

class ProductoRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_productos(self, criterio: str) -> List[Producto]:
        """
        Implementar método que:
        - Reciba un criterio de búsqueda
        - Use filtros para buscar por código o nombre
        - Retorne lista de productos que coincidan
        """
        pass
```

**3. (10 pts) Consulta con JOIN:**

```python
    def obtener_productos_con_categoria(self) -> List[Producto]:
        """
        Implementar método que:
        - Retorne productos con nombre de categoría
        - Use JOIN entre Productos y Categorias
        - Use relationship de SQLAlchemy
        """
        pass
```

---

### Parte B: Operaciones CRUD (40 pts)

**4. (10 pts) Insertar producto:**

```python
    def insertar_producto(self, producto: Producto) -> int:
        """
        Implementar método que:
        - Reciba un objeto Producto
        - Inserte en la base de datos
        - Retorne el ID generado
        - Maneje excepciones apropiadamente
        """
        pass
```

**5. (10 pts) Actualizar producto:**

```python
    def actualizar_producto(self, producto_id: int, datos_actualizacion: dict) -> bool:
        """
        Implementar método que:
        - Actualice un producto existente
        - Use update de SQLAlchemy
        - Retorne True si se actualizó, False si no existe
        """
        pass
```

**6. (10 pts) Eliminar producto (soft delete):**

```python
    def eliminar_producto(self, producto_id: int) -> bool:
        """
        Implementar método que:
        - No elimine físicamente, solo marque activo = False
        - Valide que no tenga ventas asociadas antes de "eliminar"
        - Use consulta previa para verificar
        """
        pass
```

**7. (10 pts) Registrar venta con transacción:**

```python
    def registrar_venta(self, producto_id: int, cantidad: int) -> bool:
        """
        Implementar método que:
        - Registre una venta
        - Actualice el stock del producto
        - Use transacción (ambas operaciones o ninguna)
        - Valide stock suficiente antes de vender
        """
        pass
```

---

### Parte C: Manejo de Errores (30 pts)

**8. (15 pts) Excepciones personalizadas:**

```python
# exceptions/producto_exceptions.py

# Crear excepciones específicas:
class ProductoNoEncontradoError(Exception):
    """Producto no encontrado en la base de datos."""
    pass

class StockInsuficienteError(Exception):
    """No hay suficiente stock para la operación."""
    pass

class ErrorConexionBD(Exception):
    """Error al conectar con la base de datos."""
    pass

# Usarlas apropiadamente en los métodos anteriores
```

**9. (15 pts) Logging básico:**

```python
# utils/logger.py
import logging

# Implementar logging que:
# - Configure logger con formato apropiado
# - Registre todas las operaciones
# - Incluya timestamp, operación, resultado
# - Registre errores con detalle

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

---

## 📋 Código Base Proporcionado

```python
# models/producto.py (modelo proporcionado)
from database import Base
from sqlalchemy import Column, Integer, String, Numeric, Boolean

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(500))
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    categoria_id = Column(Integer)
    fecha_creacion = Column(DateTime)
    activo = Column(Boolean, default=True)

# Connection string (ajustar según laboratorio)
# SQLite: "sqlite:///./tienda.db"
# PostgreSQL: "postgresql://user:password@localhost/tiendadb"
```

---

## 📏 Rúbrica

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Conexión** | 10 | Manejo correcto de conexión SQLAlchemy |
| **Consultas** | 20 | Filtros, JOINs, prevención SQL Injection |
| **CRUD** | 40 | Todas las operaciones funcionan |
| **Transacciones** | 10 | Implementación correcta con commit/rollback |
| **Excepciones** | 10 | Manejo apropiado de errores |
| **Código limpio** | 10 | Type hints, docstrings, nomenclatura |
| **TOTAL** | **100** | |

---

## ⚠️ Reglas del Examen

1. **Individual** - No consultar con compañeros
2. **Puede usar:** Documentación oficial de SQLAlchemy
3. **NO puede usar:** ChatGPT, StackOverflow, código de proyectos anteriores
4. **Tiempo:** 1 hora estricta
5. **El código debe ejecutarse correctamente**

---

## 💡 Consejos

1. Empiece por la conexión
2. Pruebe cada método antes de continuar
3. Use context manager `with` para sesiones
4. Siempre use consultas filtradas (nunca interpolate strings)
5. Maneje excepciones con try-except
6. Use las relaciones de SQLAlchemy para JOINs

---

**Fecha:** Jueves 23 de abril de 2026
**Hora:** 06:00 - 07:00 AM
**Lugar:** TU301
**UNAULA - POO II - 2026-I**
