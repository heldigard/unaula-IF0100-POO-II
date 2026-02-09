# Teoría - Formularios, Validación y Sesiones

**IF0100 - Lenguaje de Programación OO II**

---

## 1. Validaciones con Flask-WTF

```python
# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Range


class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[
        DataRequired(message='El nombre es requerido'),
        Length(min=3, max=100, message='El nombre debe tener entre 3 y 100 caracteres')
    ])
    
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Email no válido')
    ])
    
    clave = PasswordField('Clave', validators=[
        DataRequired(),
        Length(min=6, max=100, message='La clave debe tener al menos 6 caracteres')
    ])
    
    confirmar_clave = PasswordField('Confirmar Clave', validators=[
        DataRequired(),
        EqualTo('clave', message='Las claves no coinciden')
    ])
    
    edad = IntegerField('Edad', validators=[
        Range(min=18, max=120, message='La edad debe estar entre 18 y 120')
    ])
    
    submit = SubmitField('Registrarse')
```

### Uso en Rutas

```python
from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistroForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta'


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    
    if form.validate_on_submit():
        # Datos válidos, procesar registro
        usuario = Usuario(
            nombre=form.nombre.data,
            email=form.email.data,
            clave=form.clave.data,
            edad=form.edad.data
        )
        db.session.add(usuario)
        db.session.commit()
        
        flash('¡Registro exitoso!', 'success')
        return redirect(url_for('login'))
    
    # GET o validación fallida
    return render_template('registro.html', form=form)
```

### Template con Formulario

```html
<!-- templates/registro.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Registro</title>
</head>
<body>
    <h1>Registro de Usuario</h1>
    
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">
                    {{ message }}
                </div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <form method="POST" action="">
        {{ form.hidden_tag() }}
        
        <div>
            {{ form.nombre.label }}<br>
            {{ form.nombre(size=32) }}<br>
            {% for error in form.nombre.errors %}
                <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        
        <div>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}<br>
            {% for error in form.email.errors %}
                <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        
        <div>
            {{ form.clave.label }}<br>
            {{ form.clave() }}<br>
            {% for error in form.clave.errors %}
                <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        
        <div>
            {{ form.confirmar_clave.label }}<br>
            {{ form.confirmar_clave() }}<br>
            {% for error in form.confirmar_clave.errors %}
                <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        
        <div>
            {{ form.edad.label }}<br>
            {{ form.edad() }}<br>
            {% for error in form.edad.errors %}
                <span style="color: red;">{{ error }}</span>
            {% endfor %}
        </div>
        
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

---

## 2. Estado y Sesiones

### Flask flash (Mensajes Temporales)

```python
from flask import flash, redirect, url_for

@app.route('/procesar', methods=['POST'])
def procesar():
    # Dura una redirección (usa sesiones internamente)
    flash('Operación exitosa', 'success')
    flash('Revisa tu correo', 'info')
    return redirect(url_for('index'))
```

### Session

```python
from flask import session

# Configurar clave secreta (requerido para sesiones)
app.config['SECRET_KEY'] = 'tu-clave-secreta-aqui'


@app.route('/login', methods=['POST'])
def login():
    # Verificar credenciales...
    
    # Guardar en sesión (dura toda la sesión del usuario)
    session['usuario'] = 'Juan'
    session['user_id'] = 123
    session['rol'] = 'admin'
    
    flash('Sesión iniciada', 'success')
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    # Leer de sesión
    usuario = session.get('usuario')
    if not usuario:
        flash('Debes iniciar sesión', 'error')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', usuario=usuario)


@app.route('/logout')
def logout():
    # Limpiar sesión
    session.clear()
    # o eliminar claves específicas
    # session.pop('usuario', None)
    
    flash('Sesión cerrada', 'info')
    return redirect(url_for('index'))
```

### Cookies Persistentes

```python
from flask import make_response, request

@app.route('/set_cookie')
def set_cookie():
    resp = make_response(redirect(url_for('index')))
    
    # Cookie persistente (30 días)
    from datetime import datetime, timedelta
    expiracion = datetime.now() + timedelta(days=30)
    
    resp.set_cookie(
        'ultima_visita', 
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        expires=expiracion
    )
    
    return resp


@app.route('/get_cookie')
def get_cookie():
    ultima_visita = request.cookies.get('ultima_visita')
    if ultima_visita:
        return f'Tu última visita fue: {ultima_visita}'
    return 'Primera visita'


@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response(redirect(url_for('index')))
    resp.delete_cookie('ultima_visita')
    return resp
```

---

**Última actualización:** 2026-02-01
