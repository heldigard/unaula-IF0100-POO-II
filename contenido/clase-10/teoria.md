# Teoría - MVC con Flask

**IF0100 - Lenguaje de Programación OO II**

---

## MVC con Flask

| Aspecto | Descripción |
|---------|-------------|
| **Organización** | Blueprints + Templates + Models |
| **Complejidad** | Flexible (desde simple hasta complejo) |
| **Uso ideal** | APIs, apps web, CRUD |

---

## MVC Pattern

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Browser  │────▶│  Route   │────▶│  Model   │
└──────────┘     └────┬─────┘     └──────────┘
                      │
                      ▼
                 ┌──────────┐
                 │ Template │
                 └────┬─────┘
                      │
                      ▼
                 ┌──────────┐
                 │ Browser  │
                 └──────────┘
```

### Blueprint (Controller)

```python
# app/routes.py (o app/controllers/productos.py)
from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import Producto
from app import db

# Crear Blueprint
main = Blueprint('main', __name__)


# LISTAR (Index)
@main.route('/productos')
def productos_index():
    productos = Producto.query.all()
    return render_template('productos/index.html', productos=productos)


# DETALLE (Details)
@main.route('/productos/<int:id>')
def productos_details(id):
    producto = Producto.query.get_or_404(id)
    return render_template('productos/details.html', producto=producto)


# CREAR - Formulario (GET)
@main.route('/productos/nuevo', methods=['GET'])
def productos_create_get():
    return render_template('productos/create.html')


# CREAR - Procesar (POST)
@main.route('/productos/nuevo', methods=['POST'])
def productos_create_post():
    nombre = request.form.get('nombre')
    precio = request.form.get('precio', type=float)
    
    producto = Producto(nombre=nombre, precio=precio)
    db.session.add(producto)
    db.session.commit()
    
    flash('Producto creado exitosamente', 'success')
    return redirect(url_for('main.productos_index'))


# ACTUALIZAR
@main.route('/productos/<int:id>/editar', methods=['GET', 'POST'])
def productos_edit(id):
    producto = Producto.query.get_or_404(id)
    
    if request.method == 'POST':
        producto.nombre = request.form.get('nombre')
        producto.precio = request.form.get('precio', type=float)
        db.session.commit()
        flash('Producto actualizado', 'success')
        return redirect(url_for('main.productos_details', id=id))
    
    return render_template('productos/edit.html', producto=producto)


# ELIMINAR
@main.route('/productos/<int:id>/eliminar', methods=['POST'])
def productos_delete(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado', 'success')
    return redirect(url_for('main.productos_index'))
```

---

## Organización con Blueprints

```
aplicacion/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── producto.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── productos_controller.py
│   └── templates/
│       └── productos/
│           ├── index.html
│           ├── create.html
│           ├── edit.html
│           └── details.html
└── run.py
```

```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SECRET_KEY'] = 'clave-secreta'
    
    db.init_app(app)
    
    # Registrar blueprints
    from app.controllers.productos_controller import productos_bp
    app.register_blueprint(productos_bp, url_prefix='/productos')
    
    return app
```

---

## Alternativa: Flask-RESTful para APIs

```python
from flask_restful import Api, Resource

api = Api(app)


class ProductoResource(Resource):
    def get(self, id):
        producto = Producto.query.get_or_404(id)
        return producto.to_dict()

    def put(self, id):
        producto = Producto.query.get_or_404(id)
        datos = request.get_json()
        producto.nombre = datos.get('nombre', producto.nombre)
        producto.precio = datos.get('precio', producto.precio)
        db.session.commit()
        return producto.to_dict()

    def delete(self, id):
        producto = Producto.query.get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return '', 204


class ProductosListResource(Resource):
    def get(self):
        productos = Producto.query.all()
        return [p.to_dict() for p in productos]

    def post(self):
        datos = request.get_json()
        producto = Producto(nombre=datos['nombre'], precio=datos['precio'])
        db.session.add(producto)
        db.session.commit()
        return producto.to_dict(), 201


# Registrar rutas API
api.add_resource(ProductosListResource, '/api/productos')
api.add_resource(ProductoResource, '/api/productos/<int:id>')
```

---

**Última actualización:** 2026-02-01
