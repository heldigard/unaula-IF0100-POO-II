# Evaluación 5 - IF0100: CRUD Completo con FastAPI y SQLAlchemy

**Curso:** IF0100 - Lenguaje de Programación OO II
**Tipo:** Proyecto práctico (en parejas)
**Porcentaje:** 15%
**Fecha de entrega:** 2026-05-07 (Jueves)
**Sustentación:** Obligatoria

---

## 🎯 Objetivo

Desarrollar una aplicación web completa que demuestre dominio de FastAPI y SQLAlchemy para operaciones de persistencia con API REST y templates Jinja2.

---

## 📋 Descripción del Proyecto

### Tema: Sistema de Gestión de Inventario

Crear un sistema web completo para gestionar el inventario de una tienda, con todas las operaciones CRUD y reportes, usando FastAPI + SQLAlchemy + Jinja2 + HTMX.

---

## 🔧 Requerimientos Funcionales

### 1. Gestión de Productos (25 pts)
- **Crear:** Agregar nuevos productos
- **Leer:** Listar, buscar y filtrar productos
- **Actualizar:** Modificar información de productos
- **Eliminar:** Eliminar productos (validando dependencias)

### 2. Gestión de Categorías (15 pts)
- CRUD completo de categorías
- Relación con productos

### 3. Gestión de Proveedores (15 pts)
- CRUD completo de proveedores
- Asociar productos con proveedores

### 4. Movimientos de Inventario (25 pts)
- Registrar entradas (compras)
- Registrar salidas (ventas)
- Ajustes de inventario
- Todo con transacciones

### 5. Reportes (20 pts)
- Productos con stock bajo
- Movimientos por fecha
- Inventario valorizado
- Exportar a CSV

---

## 🏗️ Arquitectura del Proyecto

```
sistema_inventario/
├── src/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app entry point
│   ├── config.py                  # Configuración (Settings)
│   ├── database.py                # Conexión SQLAlchemy
│   ├── models/
│   │   ├── __init__.py
│   │   ├── categoria.py
│   │   ├── producto.py
│   │   ├── proveedor.py
│   │   └── movimiento_inventario.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── categoria.py
│   │   ├── producto.py
│   │   └── movimiento.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── categoria_repository.py
│   │   ├── producto_repository.py
│   │   └── movimiento_repository.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── inventario_service.py
│   │   └── reporte_service.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── home.py
│   │   ├── productos.py
│   │   ├── categorias.py
│   │   └── reportes.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── productos/
│       │   ├── list.html
│       │   ├── form.html
│       │   └── detail.html
│       ├── categorias/
│       ├── proveedores/
│       └── reportes/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── htmx.min.js
├── alembic/
│   ├── env.py
│   └── versions/
├── tests/
│   ├── __init__.py
│   └── test_repositories.py
├── alembic.ini
├── requirements.txt
└── pyproject.toml
```

---

## 💾 Modelo de Base de Datos

```python
# models/categoria.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True)
    descripcion = Column(Text)

    productos = relationship("Producto", back_populates="categoria")


# models/proveedor.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base

class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    contacto = Column(String(100))
    telefono = Column(String(20))
    email = Column(String(100))
    direccion = Column(Text)

    productos = relationship("Producto", back_populates="proveedor")


# models/producto.py
from sqlalchemy import Column, Integer, String, Numeric, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    precio_compra = Column(Numeric(10, 2), nullable=False)
    precio_venta = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    stock_minimo = Column(Integer, default=10)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"))
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    activo = Column(Boolean, default=True)

    categoria = relationship("Categoria", back_populates="productos")
    proveedor = relationship("Proveedor", back_populates="productos")


# models/movimiento_inventario.py
from sqlalchemy import Column, Integer, String, Numeric, Integer, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class MovimientoInventario(Base):
    __tablename__ = "movimientos_inventario"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    tipo_movimiento = Column(String(20), nullable=False)  # 'ENTRADA', 'SALIDA', 'AJUSTE'
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2))
    motivo = Column(Text)
    fecha_movimiento = Column(DateTime(timezone=True), server_default=func.now())
    usuario = Column(String(50))

    producto = relationship("Producto", back_populates="movimientos")
```

---

## 💻 Requisitos Técnicos

### 1. Patrón Repository (obligatorio)

```python
# repositories/base_repository.py
from typing import TypeVar, Generic, Type, Optional, List
from sqlalchemy.orm import Session
from database import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get_by_id(self, id: int) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self) -> List[ModelType]:
        return self.db.query(self.model).all()

    def find(self, predicate) -> List[ModelType]:
        return self.db.query(self.model).filter(predicate).all()

    def add(self, entity: ModelType) -> ModelType:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, entity: ModelType) -> ModelType:
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def delete(self, id: int) -> bool:
        entity = self.get_by_id(id)
        if entity:
            self.db.delete(entity)
            self.db.commit()
            return True
        return False
```

### 2. Uso de Transacciones

```python
# services/inventario_service.py
from sqlalchemy.orm import Session
from repositories import ProductoRepository, MovimientoRepository

class InventarioService:
    def __init__(self, db: Session):
        self.db = db
        self.producto_repo = ProductoRepository(db)
        self.movimiento_repo = MovimientoRepository(db)

    def registrar_movimiento(self, movimiento: MovimientoInventario) -> bool:
        """
        Registrar movimiento con transacción.
        Si falla algo, hacer rollback.
        """
        try:
            # 1. Insertar movimiento
            self.movimiento_repo.add(movimiento)

            # 2. Actualizar stock según tipo
            if movimiento.tipo_movimiento == "ENTRADA":
                self.producto_repo.aumentar_stock(
                    movimiento.producto_id,
                    movimiento.cantidad
                )
            elif movimiento.tipo_movimiento == "SALIDA":
                self.producto_repo.disminuir_stock(
                    movimiento.producto_id,
                    movimiento.cantidad
                )

            self.db.commit()
            return True

        except Exception:
            self.db.rollback()
            raise
```

### 3. Parámetros con SQLAlchemy (obligatorio - prevenir SQL Injection)

```python
# CORRECTO - Usar consultas filtradas de SQLAlchemy
def buscar_productos(self, nombre: str) -> List[Producto]:
    return self.db.query(Producto).filter(
        Producto.nombre.ilike(f"%{nombre}%")
    ).all()

# INCORRECTO - NUNCA HACER
# self.db.execute(f"SELECT * FROM productos WHERE nombre = '{nombre}'")
```

### 4. Manejo de Sesiones

```python
# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./inventario.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependencia para obtener sesión."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 📤 Entrega

1. **Repositorio GitHub** con todo el código
2. **ZIP con:**
   - Código fuente completo
   - requirements.txt
   - Script SQL (init_db.py) de creación de BD
   - Datos de prueba (fixtures)
   - README.md con:
     - Instrucciones de instalación
     - Cómo ejecutar (`uvicorn main:app --reload`)
     - Descripción de funcionalidades
   - PDF con:
     - Nombres de integrantes
     - Diagrama de clases
     - Diagrama ER de la base de datos
     - Capturas de pantalla

---

## 🎤 Sustentación

**Duración:** 15 minutos por pareja

1. **Demostración (8 min):**
   - Ejecutar todas las operaciones CRUD
   - Mostrar transacciones funcionando
   - Demostrar reportes
   - Mostrar interactividad HTMX

2. **Preguntas técnicas (7 min):**
   - Explicar uso de SQLAlchemy ORM
   - Mostrar prevención de SQL Injection
   - Explicar manejo de transacciones
   - Explicar uso de Pydantic para validación

---

## 📏 Rúbrica

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **CRUD Productos** | 25 | Todas las operaciones |
| **Categorías/Proveedores** | 15 | CRUD completo |
| **Movimientos** | 25 | Con transacciones |
| **Reportes** | 20 | Al menos 3 reportes |
| **Arquitectura** | 15 | Repository pattern, capas |
| **TOTAL** | **100** | |

---

## ⚠️ Notas Importantes

- El código debe compilar y ejecutar sin errores
- La base de datos debe poder recrearse con `python init_db.py`
- Ambos integrantes deben poder explicar el código
- Sin sustentación = máximo 3.0
- Usar type hints en todo el código
- Incluir docstrings en español

---

## 💡 Recursos

- SQLAlchemy ORM: https://docs.sqlalchemy.org/orm/
- FastAPI: https://fastapi.tiangolo.com/
- Jinja2: https://jinja.palletsprojects.com/
- HTMX: https://htmx.org/

---

**Fecha límite:** Jueves 7 de mayo de 2026, 23:59
**Sustentación:** En clase del jueves 7 de mayo
**UNAULA - POO II - 2026-I**
