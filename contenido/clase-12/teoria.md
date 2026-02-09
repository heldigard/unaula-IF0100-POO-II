# Teoría - Acceso a Bases de Datos en Python

**IF0100 - Lenguaje de Programación OO II**

---

## 1. DB-API 2.0 (sqlite3)

Librería estándar de Python para acceso a bases de datos SQLite.

### Arquitectura

```
┌─────────────────────────────────────┐
│      APLICACIÓN PYTHON              │
├─────────────────────────────────────┤
│  DB-API 2.0 (PEP 249)               │
│  ┌───────────────────────────────┐ │
│  │ Connection                    │ │
│  │ Cursor                        │ │
│  │ execute() / executemany()     │ │
│  │ fetchone() / fetchall()       │ │
│  └───────────────────────────────┘ │
├─────────────────────────────────────┤
│  sqlite3 / psycopg2 / pymysql      │
├─────────────────────────────────────┤
│  SQLite / PostgreSQL / MySQL        │
└─────────────────────────────────────┘
```

### Objetos Principales

| Objeto | Propósito |
|--------|-----------|
| **Connection** | Conexión a la base de datos |
| **Cursor** | Ejecutar consultas SQL |
| **execute()** | Ejecutar una sentencia SQL |
| **fetchone()** | Obtener una fila |
| **fetchall()** | Obtener todas las filas |

---

## 2. SQLite3 - Ejemplos

```python
import sqlite3
from datetime import datetime


# Conectar a la base de datos (crea si no existe)
conn = sqlite3.connect('mi_base.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insertar datos
cursor.execute('''
    INSERT INTO usuarios (nombre, email) 
    VALUES (?, ?)
''', ('Juan Pérez', 'juan@email.com'))

# Insertar múltiples registros
usuarios = [
    ('María García', 'maria@email.com'),
    ('Pedro López', 'pedro@email.com'),
]
cursor.executemany('''
    INSERT INTO usuarios (nombre, email) 
    VALUES (?, ?)
''', usuarios)

# Confirmar cambios
conn.commit()

# Consultar datos
cursor.execute('SELECT * FROM usuarios WHERE nombre LIKE ?', ('%Juan%',))
resultados = cursor.fetchall()

for fila in resultados:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Email: {fila[2]}")

# Consultar un solo registro
cursor.execute('SELECT * FROM usuarios WHERE id = ?', (1,))
usuario = cursor.fetchone()

if usuario:
    print(f"Usuario encontrado: {usuario}")

# Actualizar
cursor.execute('''
    UPDATE usuarios 
    SET email = ? 
    WHERE id = ?
''', ('juan.nuevo@email.com', 1))

# Eliminar
cursor.execute('DELETE FROM usuarios WHERE id = ?', (2,))

conn.commit()

# Cerrar conexión
cursor.close()
conn.close()
```

### Uso con Context Manager (recomendado)

```python
import sqlite3


def obtener_usuario_por_id(user_id):
    with sqlite3.connect('mi_base.db') as conn:
        conn.row_factory = sqlite3.Row  # Acceso por nombre de columna
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM usuarios WHERE id = ?', (user_id,))
        fila = cursor.fetchone()
        
        if fila:
            return {
                'id': fila['id'],
                'nombre': fila['nombre'],
                'email': fila['email'],
                'fecha_registro': fila['fecha_registro']
            }
        return None


def listar_todos_los_usuarios():
    with sqlite3.connect('mi_base.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM usuarios ORDER BY nombre')
        return [dict(fila) for fila in cursor.fetchall()]
```

---

## 3. SQLAlchemy (ORM)

ORM más popular para Python.

### Instalación

```bash
pip install sqlalchemy
```

### Configuración Básica

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}')>"


# Configurar conexión
engine = create_engine('sqlite:///app.db', echo=True)
Base.metadata.create_all(engine)

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()
```

### CRUD con SQLAlchemy

```python
# CREATE - Crear
nuevo_usuario = Usuario(nombre='Ana Torres', email='ana@email.com')
session.add(nuevo_usuario)
session.commit()

# READ - Leer
todos = session.query(Usuario).all()
uno = session.query(Usuario).filter_by(id=1).first()
filtrados = session.query(Usuario).filter(Usuario.nombre.like('%Torres%')).all()

# UPDATE - Actualizar
usuario = session.query(Usuario).filter_by(id=1).first()
usuario.email = 'nuevo@email.com'
session.commit()

# DELETE - Eliminar
usuario = session.query(Usuario).filter_by(id=1).first()
session.delete(usuario)
session.commit()
```

### Relaciones

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Pedido(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    total = Column(Integer)
    
    # Relación
    usuario = relationship("Usuario", back_populates="pedidos")


# Agregar relación inversa a Usuario
Usuario.pedidos = relationship("Pedido", back_populates="usuario")

# Uso
usuario = session.query(Usuario).filter_by(id=1).first()
for pedido in usuario.pedidos:
    print(pedido.total)
```

---

## 4. Connection String

```python
# SQLite
sqlite:///app.db                    # Archivo
sqlite:///:memory:                  # En memoria

# PostgreSQL
postgresql://usuario:password@localhost:5432/midb

# MySQL
mysql+pymysql://usuario:password@localhost:3306/midb
```

### Configuración con variables de entorno

```python
import os

DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
engine = create_engine(DATABASE_URL)
```

---

**Última actualización:** 2026-02-01
