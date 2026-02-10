"""Script to create 02-04-bdd-intro.ipynb"""
import json

# Create new BDD notebook
cells = []

# Cell 0: Title and objectives
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """# Clase 2.4 - Introduccion a BDD: Gherkin y behave

**Unidad:** 2 - Tecnicas de Desarrollo
**Duracion:** 2 horas
**Autor:** IF0100 - UNAULA

## Objetivos de Aprendizaje

Al finalizar esta clase, sera capaz de:
- [ ] Comprender que es Behavior Driven Development (BDD)
- [ ] Identificar diferencias entre TDD y BDD
- [ ] Escribir escenarios en lenguaje Gherkin (Given-When-Then)
- [ ] Implementar pasos (steps) de BDD con Python
- [ ] Usar behave para ejecutar tests BDD
- [ ] Conectar escenarios BDD con codigo Python

---

## 1. Conceptos Teoricos

### Que es BDD?

**Behavior Driven Development (BDD)** o Desarrollo Guiado por Comportamiento es una metodologia de desarrollo agil que busca:

- **Colaboracion:** Desarrolladores, QA y stakeholders hablando el mismo idioma
- **Valor de negocio:** Enfocarse en comportamientos que agregan valor
- **Documentacion viva:** Los escenarios son documentacion ejecutable
- **Testing comprensible:** Tests que todos pueden entender

**Idea clave:** BDD transforma especificaciones tecnicas en escenarios de negocio comprensibles para todos los stakeholders.

### TDD vs BDD

| Aspecto | TDD | BDD |
|---------|-----|-----|
| **Enfoque** | Tests unitarios tecnicos | Comportamiento del sistema |
| **Lenguaje** | Codigo (Python, Java, etc.) | Gherkin (lenguaje natural) |
| **Audiencia** | Desarrolladores | Todos: Dev, QA, Negocio |
| **Perspectiva** | Como funciona internamente | Como se comporta para el usuario |
| **Ejemplo** | `test_usuario_es_valido()` | `Given un usuario valido When se registra Then es exitoso` |"""
})

# Cell 1: Gherkin introduction
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """---

## 2. Lenguaje Gherkin

### Que es Gherkin?

**Gherkin** es un lenguaje especifico de dominio (DSL) que permite describir comportamientos del software en un lenguaje natural estructurado.

### Palabras Clave de Gherkin

| Palabra Clave | Proposito | Ejemplo |
|---------------|-----------|---------|
| `Feature` | Describe la funcionalidad | Feature: Registro de usuarios |
| `Scenario` | Describe un caso especifico | Scenario: Registro exitoso |
| `Given` | Contexto inicial (Dado) | Given un usuario no registrado |
| `When` | Accion (Cuando) | When se registra con datos validos |
| `Then` | Resultado esperado (Entonces) | Then el registro es exitoso |
| `And` | Y (adicional) | And recibe email de confirmacion |
| `But` | Pero (negacion) | But no puede acceder hasta verificar |

### Estructura de un Feature

**Ejemplo de Feature de Login en TaskFlow:**

```gherkin
Feature: Inicio de Sesion en TaskFlow
  Como usuario registrado
  Quiero poder iniciar sesion
  Para acceder a mis proyectos y tareas

  Scenario: Login exitoso con credenciales validas
    Given un usuario registrado con username "testuser" y password "pass123"
    When ingresa username "testuser" y password "pass123"
    Then el login es exitoso
    And es redirigido al dashboard

  Scenario: Login fallido con password incorrecto
    Given un usuario registrado con username "testuser" y password "pass123"
    When ingresa username "testuser" y password "incorrecto"
    Then el login falla
    And ve el mensaje "Credenciales invalidas"
```"""
})

# Cell 2: Gherkin Background and Scenario Outline
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """### Background: Contexto Compartido

El `Background` permite definir pasos comunes a todos los escenarios de un Feature:

```gherkin
Feature: Gestion de Proyectos

  Background:
    Given un usuario autenticado como "admin"
    And el usuario tiene permisos de creacion

  Scenario: Crear proyecto exitosamente
    When crea un proyecto con nombre "Mi Proyecto"
    Then el proyecto se crea exitosamente

  Scenario: Crear proyecto con nombre duplicado
    Given existe un proyecto con nombre "Mi Proyecto"
    When crea un proyecto con nombre "Mi Proyecto"
    Then ve el error "El proyecto ya existe"
```

### Scenario Outline: Datos Parametrizados

```gherkin
Scenario Outline: Validacion de nombres de proyecto
  Given un usuario autenticado
  When intenta crear un proyecto con nombre "<nombre>"
  Then el sistema responde "<resultado>"

  Examples: | nombre             | resultado                |
    | Valido             | Proyecto creado         |
    | P                  | Nombre muy corto        |
    |                    | Nombre es requerido     |
    | Proyecto Muy Largo Nombre Excedido | Nombre muy largo |
```"""
})

# Cell 3: behave introduction
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """---

## 3. behave Framework en Python

### Que es behave?

**behave** es un framework BDD para Python que permite ejecutar escenarios Gherkin como tests automatizados. Es similar a Cucumber en Java.

### Instalacion

```bash
# Instalar behave
pip install behave

# Instalar con dependencias utiles
pip install behave pytest-bdd
```

### Estructura de Directorios

```
proyecto/
├── features/                  # Archivos .feature con escenarios Gherkin
│   ├── __init__.py
│   ├── login.feature        # Escenarios de login
│   ├── registro.feature     # Escenarios de registro
│   └── steps/               # Implementacion de pasos (steps)
│       ├── __init__.py
│       ├── login_steps.py   # Pasos de login
│       └── registro_steps.py
├── tests/                    # Tests unitarios tradicionales
└── src/                      # Codigo de produccion
```"""
})

# Cell 4: Implement steps example
cells.append({
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': '''# Ejemplo 1: Implementar Pasos (Steps) para Login

# features/steps/login_steps.py

from behave import given, when, then

# Simulacion de servicio para el ejemplo
class AuthService:
    def __init__(self):
        self.usuarios = {}

    def registrar(self, username, password):
        self.usuarios[username] = password

    def login(self, username, password):
        if username in self.usuarios and self.usuarios[username] == password:
            return {'exitoso': True, 'redirect': '/dashboard'}
        return {'exitoso': False, 'mensaje': 'Credenciales invalidas'}

# Servicio para testing
auth_service = AuthService()

@given('un usuario registrado con username "{username}" y password "{password}"')
def step_given_usuario_registrado(context, username, password):
    """Paso que registra un usuario para el test."""
    # Crear usuario en contexto para usar en pasos siguientes
    context.username = username
    context.password = password

    # Guardar en BD de prueba
    auth_service.registrar(username, password)
    print(f"Usuario registrado: {username}")

@when('ingresa username "{username}" y password "{password}"')
def step_when_ingresa_credenciales(context, username, password):
    """Paso que intenta login."""
    context.resultado = auth_service.login(username, password)
    print(f"Intento de login: {username}")

@then('el login es exitoso')
def step_then_login_exitoso(context):
    """Verifica que el login fue exitoso."""
    assert context.resultado['exitoso'] == True
    print("Login exitoso - PASSED")

@then('es redirigido al dashboard')
def step_then_redirigido_dashboard(context):
    """Verifica redireccion al dashboard."""
    assert context.resultado['redirect'] == '/dashboard'
    print("Redireccion correcta - PASSED")

@then('el login falla')
def step_then_login_falla(context):
    """Verifica que el login fallo."""
    assert context.resultado['exitoso'] == False
    print("Login fallido - PASSED")

@then('ve el mensaje "{mensaje}"')
def step_then_ve_mensaje(context, mensaje):
    """Verifica el mensaje de error."""
    assert mensaje in context.resultado['mensaje']
    print(f"Mensaje correcto: {mensaje} - PASSED")

# Simulacion de ejecucion
print("=== Simulacion: Login exitoso ===")
context_mock = type('Context', (), {})()
step_given_usuario_registrado(context_mock, "testuser", "pass123")
step_when_ingresa_credenciales(context_mock, "testuser", "pass123")
step_then_login_exitoso(context_mock)
step_then_redirigido_dashboard(context_mock)

print("\\n=== Simulacion: Login fallido ===")
context_mock2 = type('Context', (), {})()
step_given_usuario_registrado(context_mock2, "testuser", "pass123")
step_when_ingresa_credenciales(context_mock2, "testuser", "incorrecto")
step_then_login_falla(context_mock2)
step_then_ve_mensaje(context_mock2, "Credenciales invalidas")'''
})

# Cell 5: Context in behave
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """### Contexto en behave

El objeto `context` permite compartir datos entre pasos:

```python
@given('un producto con precio {precio:d}')
def step_given_producto(context, precio):
    \"\"\"Crea un producto y lo guarda en context.\"\"\"
    context.producto = {'nombre': 'Test', 'precio': precio}

@when('aplico un descuento del {descuento:d}%')
def step_when_descuento(context, descuento):
    \"\"\"Usa el producto del context.\"\"\"
    context.precio_final = context.producto['precio'] * (1 - descuento/100)

@then('el precio final es {esperado:d}')
def step_then_precio_final(context, esperado):
    \"\"\"Verifica el resultado.\"\"\"
    assert context.precio_final == esperado
```"""
})

# Cell 6: Execute behave and pytest-bdd
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """### Ejecutar behave

```bash
# Ejecutar todos los features
behave

# Ejecutar un feature especifico
behave features/login.feature

# Ejecutar con formato bonito
behave --format pretty

# Ejecutar con colores
behave --color

# Mostrar ayuda
behave --help
```

### pytest-bdd: Alternativa a behave

**pytest-bdd** integra BDD con pytest, permitiendo usar las fixtures de pytest con escenarios Gherkin.

```python
# tests/test_bdd/test_login.py

from pytest_bdd import scenario, given, when, then
from pytest import fixture

# Escenario definido en features/login.feature
@scenario('features/login.feature', 'Login exitoso')
def test_login_exitoso():
    \"\"\"Test que ejecuta el escenario BDD.\"\"\"
    pass

@given('un usuario registrado con username "testuser"')
def usuario_registrado():
    \"\"\"Fixture que crea usuario.\"\"\"
    return Usuario(username="testuser", email="test@example.com")

@when('ingresa credenciales validas')
def ingresa_credenciales(usuario_registrado):
    \"\"\"Intenta login.\"\"\"
    return AuthService().login(usuario_registrado.username, "pass123")

@then('el login es exitoso')
def login_exitoso(ingresa_credenciales):
    \"\"\"Verifica login exitoso.\"\"\"
    assert ingresa_credenciales['exitoso'] == True
```"""
})

# Cell 7: Registration feature example
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """---

## 4. Ejemplos Practicos

### Ejemplo 1: Feature de Registro de Usuario

```gherkin
Feature: Registro de Usuarios
  Como usuario no registrado
  Quiero poder crear una cuenta
  Para poder usar TaskFlow

  Background:
    Given el sistema esta configurado
    And la pagina de registro es accesible

  Scenario: Registro exitoso con datos validos
    Given estoy en la pagina de registro
    When completo el formulario con:
      | campo           | valor            |
      | username        | newuser          |
      | email           | new@example.com  |
      | password        | pass123          |
      | confirm_password | pass123          |
    And hago clic en "Registrarse"
    Then veo "Registro exitoso"
    And soy redirigido al login

  Scenario: Registro falla con password corto
    Given estoy en la pagina de registro
    When completo el formulario con:
      | campo           | valor            |
      | username        | newuser          |
      | email           | new@example.com  |
      | password        | abc              |
      | confirm_password | abc              |
    And hago clic en "Registrarse"
    Then veo "Password muy corto"
    And permanezco en la pagina de registro
```"""
})

# Cell 8: Steps for registration
cells.append({
    'cell_type': 'code',
    'execution_count': None,
    'metadata': {},
    'outputs': [],
    'source': '''# Ejemplo 2: Steps para Registro

# features/steps/registro_steps.py

from behave import given, when, then

# Simulacion de servicio de registro
class UsuarioService:
    def __init__(self):
        self.usuarios = []

    def registrar(self, username, email, password):
        # Validar password
        if len(password) < 6:
            return {'exitoso': False, 'mensaje': 'Password muy corto'}

        # Verificar duplicados
        for u in self.usuarios:
            if u['username'] == username:
                return {'exitoso': False, 'mensaje': 'Usuario ya existe'}

        # Registrar
        self.usuarios.append({
            'username': username,
            'email': email,
            'password': password
        })
        return {'exitoso': True, 'mensaje': 'Registro exitoso'}

usuario_service = UsuarioService()

@given('estoy en la pagina de registro')
def step_pagina_registro(context):
    """Navega a la pagina de registro."""
    context.pagina_actual = 'registro'
    print("Navegado a pagina de registro")

@when('completo el formulario con:')
def step_completar_formulario(context):
    """Completa el formulario con los datos de la tabla."""
    tabla = context.table
    context.datos_form = {row['campo']: row['valor'] for row in tabla}
    print(f"Formulario completado: {context.datos_form}")

@when('hago clic en "{boton}"')
def step_hacer_clic(context, boton):
    """Envia el formulario."""
    context.response = usuario_service.registrar(
        context.datos_form.get('username'),
        context.datos_form.get('email'),
        context.datos_form.get('password')
    )

@then('veo "{mensaje}"')
def step_ver_mensaje(context, mensaje):
    """Verifica que el mensaje este en la respuesta."""
    assert mensaje in context.response['mensaje']
    print(f"Mensaje verificado: {mensaje}")

@then('soy redirigido al login')
def step_redirigido_login(context):
    """Verifica redireccion."""
    assert context.response['exitoso'] == True
    print("Redirigido a login - PASSED")

@then('permanezco en la pagina de registro')
def step_permanecer_registro(context):
    """Verifica que NO hubo redireccion."""
    assert context.response['exitoso'] == False
    print("Permanece en registro - PASSED")

# Simulacion de ejecucion
print("=== Test 1: Registro exitoso ===")
class Row:
    def __init__(self, campo, valor):
        self['campo'] = campo
        self['valor'] = valor
    def __getitem__(self, key):
        return getattr(self, key)

context_mock = type('Context', (), {
    'table': [
        type('Row', (), {'campo': 'username', 'valor': 'newuser'})(),
        type('Row', (), {'campo': 'email', 'valor': 'new@example.com'})(),
        type('Row', (), {'campo': 'password', 'valor': 'pass123'})(),
        type('Row', (), {'campo': 'confirm_password', 'valor': 'pass123'})()
    ]
})()
step_pagina_registro(context_mock)
step_completar_formulario(context_mock)
step_hacer_clic(context_mock, "Registrarse")
step_ver_mensaje(context_mock, "Registro exitoso")
step_redirigido_login(context_mock)

print("\\n=== Test 2: Registro fallido (password corto) ===")
context_mock2 = type('Context', (), {
    'table': [
        type('Row', (), {'campo': 'username', 'valor': 'newuser2'})(),
        type('Row', (), {'campo': 'email', 'valor': 'new2@example.com'})(),
        type('Row', (), {'campo': 'password', 'valor': 'abc'})(),
        type('Row', (), {'campo': 'confirm_password', 'valor': 'abc'})()
    ]
})()
step_pagina_registro(context_mock2)
step_completar_formulario(context_mock2)
step_hacer_clic(context_mock2, "Registrarse")
step_ver_mensaje(context_mock2, "Password muy corto")
step_permanecer_registro(context_mock2)'''
})

# Cell 9: Best practices
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """---

## 5. Buenas Practicas

### Escribiendo Buenos Escenarios

**❌ Mal:**
```gherkin
Scenario: Registro
  Given completo el formulario
  When hago clic
  Then veo "OK"
```
*Demasiado vago, no documenta el comportamiento real.*

**✅ Bien:**
```gherkin
Scenario: Registro exitoso
  Given un usuario nuevo en la pagina de registro
  When completa todos los campos validos
  Then recibe confirmacion por email
```
*Claro, especifico, describe el valor de negocio.*

### Organizacion de Features

- **Un feature por archivo:** features/login.feature, features/registro.feature
- **Nombre descriptivo:** Describe la capacidad de negocio
- **Escenarios independientes:** Cada escenario debe ser autonomo
- **Uso de Background:** Para contexto compartido entre escenarios

### Nomenclatura de Steps

- **Ser descriptivo:** step_when_usuario_selecciona_proyecto (no step_cuando)
- **Usar parametros:** 'Cuando crea "{nombre}"' en vez de 'Cuando crea proyecto'
- **Reutilizar steps:** Un mismo step puede usarse en multiples escenarios
- **Evitar duplicacion:** Extraer logica compartida a funciones auxiliares

### Tests BDD vs Tests Unitarios

| Cuándo usar BDD | Cuándo usar Tests Unitarios |
|-----------------|-----------------------------|
| Flujos de usuario completos | Logica de negocio aislada |
| Integracion entre componentes | Algoritmos y calculos |
| Casos de uso del negocio | Validaciones tecnicas |
| Documentacion para stakeholders | Cobertura de codigo |

### Integracion BDD + TDD

**Enfoque Hibrido:**

No es TDD vs BDD, sino TDD + BDD. Usa BDD para escenarios de usuario y TDD para la implementacion detallada de cada componente.

- **BDD:** Escenarios Gherkin definen el "que"
- **TDD:** Tests unitarios definen el "como"
- **Resultado:** Codigo documentado y probado en multiples niveles"""
})

# Cell 10: Exercise
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """---

## 6. Ejercicio Practico: Escenario BDD para Login

### Objetivo

Crear un escenario BDD completo para el flujo de login en TaskFlow, desde el feature Gherkin hasta la implementacion de pasos.

### Pasos del Ejercicio

**Paso 1: Crear Directorio de Features**
```bash
mkdir -p features/steps
touch features/__init__.py
touch features/steps/__init__.py
```

**Paso 2: Escribir Feature (features/login.feature)**
```gherkin
Feature: Login de Usuarios en TaskFlow
  Como usuario registrado
  Quiero poder iniciar sesion
  Para acceder a mis proyectos y tareas

  Scenario: Login exitoso
    Given un usuario registrado con username "testuser" y password "pass123"
    When ingresa username "testuser" y password "pass123"
    Then el login es exitoso
    And recibe un token de autenticacion

  Scenario: Login fallido con password incorrecto
    Given un usuario registrado con username "testuser" y password "pass123"
    When ingresa username "testuser" y password "incorrecto"
    Then el login falla
    And ve el error "Credenciales invalidas"
```

**Paso 3: Implementar Steps (features/steps/login_steps.py)**
```python
from behave import given, when, then

@given('un usuario registrado con username "{username}" y password "{password}"')
def step_usuario_registrado(context, username, password):
    \"\"\"Crea un usuario de prueba.\"\"\"
    context.usuario = {'username': username, 'password': password}

@when('ingresa username "{username}" y password "{password}"')
def step_ingresa_credenciales(context, username, password):
    \"\"\"Intenta login con las credenciales.\"\"\"
    # Aqui iria la logica de login real
    if username == context.usuario['username'] and password == context.usuario['password']:
        context.resultado = {'exitoso': True, 'token': 'abc123'}
    else:
        context.resultado = {'exitoso': False, 'error': 'Credenciales invalidas'}

@then('el login es exitoso')
def step_login_exitoso(context):
    \"\"\"Verifica que el login fue exitoso.\"\"\"
    assert context.resultado['exitoso'] == True

@then('recibe un token de autenticacion')
def step_token_autenticacion(context):
    \"\"\"Verifica que recibio token.\"\"\"
    assert 'token' in context.resultado
```

**Paso 4: Ejecutar behave**
```bash
behave features/login.feature
```"""
})

# Cell 11: Summary
cells.append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': """---

## Resumen

### Conceptos Clave

| Concepto | Sintaxis | Uso |
|----------|----------|-----|
| Feature | `Feature: Nombre` | Describe la funcionalidad |
| Scenario | `Scenario: Caso` | Describe un caso especifico |
| Given | `Given contexto` | Estado inicial |
| When | `When accion` | Accion a ejecutar |
| Then | `Then resultado` | Resultado esperado |
| Background | `Background:` | Contexto compartido |
| Scenario Outline | `Scenario Outline:` | Datos parametrizados |

### Checklist de Aprendizaje

- [ ] Entiendo que es BDD y cuando usarlo
- [ ] Puedo escribir escenarios en Gherkin
- [ ] Se usar behave para ejecutar tests BDD
- [ ] Puedo implementar pasos (steps) en Python
- [ ] Conozco las diferencias entre TDD y BDD
- [ ] Puedo integrar BDD con TDD

### Para Profundizar

- [behave Documentation](https://behave.readthedocs.io/)
- [Gherkin Reference - Cucumber Docs](https://cucumber.io/docs/gherkin/)
- [pytest-bdd Documentation](https://pytest-bdd.readthedocs.io/)
- [BDD con Python y behave - Video](https://www.youtube.com/watch?v=uE0e3G4d8IU)

---

**¡Siguiente clase:** Introduccion a DDD (Domain Driven Design)

**Tarea para casa:** Crear escenarios BDD para el flujo de registro en TaskFlow"""
})

# Create the notebook
notebook = {
    'cells': cells,
    'metadata': {
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'codemirror_mode': {'name': 'ipython', 'version': 3},
            'file_extension': '.py',
            'mimetype': 'text/x-python',
            'name': 'python',
            'nbconvert_exporter': 'python',
            'pygments_lexer': 'ipython3',
            'version': '3.8.0'
        }
    },
    'nbformat': 4,
    'nbformat_minor': 4
}

# Write the notebook
with open('notebooks/unidad-02/02-04-bdd-intro.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print('Notebook 02-04-bdd-intro.ipynb creado exitosamente!')
print(f'Total de celdas: {len(cells)}')
