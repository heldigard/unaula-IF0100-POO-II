# Teoría - Flask Framework

**IF0100 - Lenguaje de Programación OO II**

---

## 1. ¿Qué es Flask?

Framework web **ligero y flexible** para Python, ideal para aplicaciones web y APIs.

### Arquitectura

```
┌─────────────────────────────────┐
│       FLASK APPLICATION         │
├─────────────────────────────────┤
│  Request/Response Cycle         │
│  ┌─────────────────────────────┐│
│  │ Before Request              ││
│  │ URL Routing                 ││
│  │ View Function               ││
│  │ Template Rendering          ││
│  │ After Request               ││
│  └─────────────────────────────┘│
├─────────────────────────────────┤
│  Werkzeug WSGI + Jinja2        │
└─────────────────────────────────┘
```

### Instalación

```bash
pip install flask
```

### Aplicación Mínima

```python
# app.py
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '¡Hola, Mundo!'


if __name__ == '__main__':
    app.run(debug=True)
```

---

## 2. Routing y Vistas

```python
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# Ruta básica
@app.route('/')
def index():
    return render_template('index.html')


# Ruta con parámetro
@app.route('/usuario/<nombre>')
def saludar_usuario(nombre):
    return f'¡Hola, {nombre}!'


# Ruta con tipo de dato
@app.route('/producto/<int:id>')
def obtener_producto(id):
    return f'Producto ID: {id}'


# Múltiples métodos HTTP
@app.route('/api/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'GET':
        return jsonify({'usuarios': []})
    elif request.method == 'POST':
        datos = request.get_json()
        return jsonify({'creado': datos}), 201


# API REST completa
@app.route('/api/productos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def producto(id):
    if request.method == 'GET':
        return jsonify({'id': id, 'nombre': 'Producto'})
    elif request.method == 'PUT':
        datos = request.get_json()
        return jsonify({'actualizado': id, 'datos': datos})
    elif request.method == 'DELETE':
        return jsonify({'eliminado': id}), 204
```

---

## 3. Templates con Jinja2

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/productos')
def listar_productos():
    productos = [
        {'id': 1, 'nombre': 'Laptop', 'precio': 1200},
        {'id': 2, 'nombre': 'Mouse', 'precio': 25},
    ]
    return render_template('productos.html', 
                         productos=productos, 
                         titulo='Catálogo')
```

```html
<!-- templates/productos.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ titulo }}</title>
</head>
<body>
    <h1>{{ titulo }}</h1>
    
    {% if productos %}
        <ul>
        {% for producto in productos %}
            <li>
                {{ producto.nombre }} - 
                ${{ "%.2f"|format(producto.precio) }}
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No hay productos disponibles.</p>
    {% endif %}
</body>
</html>
```

---

## 4. Crear Proyecto

```bash
# Crear estructura de proyecto
mkdir mi_app_flask
cd mi_app_flask
mkdir -p app/templates app/static/css app/static/js

# Instalar dependencias
pip install flask flask-sqlalchemy flask-wtf
```

### Estructura Recomendada

```
mi_app_flask/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   └── static/
│       ├── css/
│       └── js/
├── config.py
├── run.py
└── requirements.txt
```

### Ejemplo: Configuración Completa

```python
# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app


# app/models.py
from app import db


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio
        }


# run.py
from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

**Última actualización:** 2026-02-01
