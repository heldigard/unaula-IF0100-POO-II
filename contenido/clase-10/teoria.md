# Teoria - pytest Avanzado

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Fixtures de pytest

### Concepto de Fixture

Los fixtures son funciones que proporcionan datos o recursos de prueba. Se usan para configurar estados de prueba comunes.

```python
# conftest.py
import pytest

@pytest.fixture
def usuario_basico():
    """Fixture que retorna un usuario de prueba."""
    return {"nombre": "Juan", "email": "juan@test.com"}

@pytest.fixture
def usuario_admin():
    """Fixture que retorna un usuario administrador."""
    return {"nombre": "Admin", "email": "admin@test.com", "rol": "admin"}

@pytest.fixture
def base_datos_vacia():
    """Fixture que crea una base de datos vacia para testing."""
    db = BaseDatosMock()
    yield db  # El codigo de test se ejecuta aqui
    db.limpiar()  # Cleanup despues del test
```

### Uso de Fixtures en Tests

```python
# tests/test_usuarios.py
import pytest
from src.usuarios.usuario import Usuario

class TestUsuario:
    """Tests para la clase Usuario."""

    def test_crear_usuario(self, usuario_basico):
        """Test usando fixture usuario_basico."""
        usuario = Usuario(**usuario_basico)
        assert usuario.nombre == "Juan"
        assert usuario.email == "juan@test.com"

    def test_usuario_admin_tiene_rol(self, usuario_admin):
        """Test usando fixture usuario_admin."""
        assert usuario_admin["rol"] == "admin"
```

### Scopes de Fixtures

| Scope | Descripcion | Cuando se ejecuta |
|-------|-------------|-------------------|
| `function` | (default) Cada funcion de test | Una vez por test |
| `class` | Una vez por clase | Una vez por clase |
| `module` | Una vez por modulo | Una vez por modulo |
| `session` | Una vez por sesion | Una vez por sesion |

```python
# conftest.py
import pytest

@pytest.fixture(scope="function")
def dato_funcional():
    """Se crea para cada test individual."""
    print("\n[Setup function]")
    yield "dato function"
    print("\n[Teardown function]")

@pytest.fixture(scope="class")
def dato_clase():
    """Se crea una vez por clase de test."""
    print("\n[Setup class]")
    yield "dato class"
    print("\n[Teardown class]")

@pytest.fixture(scope="module")
def dato_modulo():
    """Se crea una vez por modulo completo."""
    print("\n[Setup module]")
    yield "dato module"
    print("\n[Teardown module]")
```

### Fixture con Dependencias

```python
# conftest.py
@pytest.fixture
def cliente_db():
    """Cliente de base de datos configurado."""
    return ClienteDB("localhost", 5432)

@pytest.fixture
def db_con_datos(cliente_db):
    """Base de datos con datos de prueba."""
    cliente_db.insertar("usuarios", {"nombre": "Juan"})
    cliente_db.insertar("usuarios", {"nombre": "Maria"})
    return cliente_db
```

### Fixture con Autouse

```python
# conftest.py
import pytest

@pytest.fixture(autouse=True)
def setup_logging():
    """Se ejecuta automaticamente para cada test."""
    print("\n=== Inicio de test ===")
    yield
    print("\n=== Fin de test ===")
```

---

## 2. Parametrizacion de Tests

### pytest.mark.parametrize

```python
import pytest

@pytest.mark.parametrize("a,b,esperado", [
    (1, 1, 2),
    (2, 3, 5),
    (10, -5, 5),
    (0, 0, 0),
    (-1, -1, -2),
])
def test_suma(a, b, esperado):
    """Test parametrizado para suma."""
    assert a + b == esperado
```

### Multiple Parametrizacion

```python
@pytest.mark.parametrize("numero,esperado", [
    (0, "cero"),
    (1, "positivo"),
    (-1, "negativo"),
])
def test_clasificar_numero(numero, esperado):
    """Test parametrizado para clasificacion."""
    assert clasificar(numero) == esperado
```

### Parametrizar con IDs Personalizadas

```python
@pytest.mark.parametrize("entrada,esperado", [
    ("hola", 4),
    ("mundo", 5),
    ("", 0),
], ids=["string_normal", "string_largo", "string_vacio"])
def test_longitud(entrada, esperado):
    """Test con IDs personalizadas."""
    assert len(entrada) == esperado
```

### Parametrizar Clases

```python
import pytest

class TestCalculadoraParametrizada:
    """Clase con tests parametrizados."""

    @pytest.mark.parametrize("a,b,esperado", [
        (2, 3, 5),
        (10, 5, 15),
        (-1, 1, 0),
    ])
    def test_suma_parametrizada(self, a, b, esperado):
        """Suma con parametros."""
        assert a + b == esperado

    @pytest.mark.parametrize("a,b,esperado", [
        (6, 3, 2),
        (10, 2, 5),
        (7, 1, 7),
    ])
    def test_division_parametrizada(self, a, b, esperado):
        """Division con parametros."""
        assert a / b == pytest.approx(esperado)
```

---

## 3. Mocks y Patching

### unittest.mock

```python
from unittest.mock import Mock, patch, MagicMock

# Crear un mock basico
mock_db = Mock()
mock_db.guardar.return_value = True
mock_db.buscar.return_value = {"nombre": "Juan"}

# Usar el mock
resultado = mock_db.guardar({"nombre": "Maria"})
assert resultado is True
assert mock_db.guardar.called
assert mock_db.guardar.call_count == 1
```

### Patching con patch()

```python
from unittest.mock import patch

# Patchear una funcion o metodo
class Calculadora:
    def obtener_precio(self, producto):
        # Llama a una API externa
        return obtener_precio_api(producto)

# Test con mock de la API externa
@patch('src.calculadora.calculadora.obtener_precio_api')
def test_precio_producto(mock_api):
    """Test que mockea la API externa."""
    mock_api.return_value = 99.99

    calc = Calculadora()
    precio = calc.obtener_precio("producto-1")

    assert precio == 99.99
    mock_api.assert_called_once_with("producto-1")
```

### patch como Context Manager

```python
from unittest.mock import patch

def test_contexto_bd():
    """Test usando patch como context manager."""
    with patch('src.db.cliente_db.Guardar') as mock_guardar:
        mock_guardar.return_value = True

        resultado = guardar_usuario("Juan")

        assert resultado is True
        mock_guardar.assert_called_once()
```

### MagicMock para Objetos Complejos

```python
from unittest.mock import MagicMock

# Crear un mock complejo
mock_usuario = MagicMock()
mock_usuario.nombre = "Juan"
mock_usuario.email = "juan@test.com"
mock_usuario.guardar.return_value = True
mock_usuario.eliminar.return_value = True

# Verificar llamadas
mock_usuario.guardar()
mock_usuario.guardar.assert_called_once()

# Llamadas con argumentos
mock_usuario.actualizar("email", "nuevo@test.com")
mock_usuario.actualizar.assert_called_with("email", "nuevo@test.com")
```

---

## 4. pytest-mock

### Instalacion

```bash
pip install pytest-mock
```

### Uso de mocker

```python
import pytest

class TestConPytestMocker:
    """Tests usando pytest-mock."""

    def test_mock_basico(self, mocker):
        """Mock basico con mocker."""
        mock_funcion = mocker.patch('mi_modulo.mi_funcion')
        mock_funcion.return_value = 42

        resultado = llamada_externa()

        assert resultado == 42
        mock_funcion.assert_called_once()

    def test_mock_metodo_clase(self, mocker):
        """Mock de metodo de clase."""
        mock_guardar = mocker.patch.object(Usuario, 'guardar')
        mock_guardar.return_value = True

        usuario = Usuario("Juan")
        resultado = usuario.guardar()

        assert resultado is True

    def test_mock_api_externa(self, mocker):
        """Mock de llamada API."""
        mock_peticion = mocker.patch('requests.get')
        mock_peticion.return_value.json.return_value = {"precio": 100}

        precio = obtener_precio_bitcoin()

        assert precio == 100

    def test_spy(self, mocker):
        """Spy que mantiene el comportamiento original."""
        spy = mocker.spy(ListaTareas, 'agregar')

        tareas = ListaTareas()
        tareas.agregar("Tarea 1")

        spy.assert_called_once_with("Tarea 1")
```

---

## 5. Coverage y Reportes

### Instalar pytest-cov

```bash
pip install pytest-cov
```

### Ejecutar con Coverage

```bash
# Coverage basico
pytest --cov=src

# Coverage con reporte HTML
pytest --cov=src --cov-report=html

# Coverage con reporte en terminal
pytest --cov=src --cov-report=term-missing

# Coverage de modulo especifico
pytest --cov=src.calculadora --cov-report=html

# Coverage con minimum threshold
pytest --cov=src --cov-fail-under=80
```

### Configurar Coverage en pytest.ini

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py

[tool:pytest_cov]
cov = src
cov-report = term-missing
cov-report = html
cov-fail-under = 80
```

---

## 6. Patrones de Testing Avanzado

### Factory Pattern con Fixtures

```python
# conftest.py
import pytest

class UsuarioFactory:
    """Factory para crear usuarios de prueba."""

    def crear(self, nombre="Test", email=None, rol="user"):
        if email is None:
            email = f"{nombre.lower()}@test.com"
        return {"nombre": nombre, "email": email, "rol": rol}

    def admin(self):
        return self.crear(nombre="Admin", rol="admin")

@pytest.fixture
def usuario_factory():
    """Fixture que retorna la factory."""
    return UsuarioFactory()

@pytest.fixture
def usuario_test(usuario_factory):
    """Usuario de prueba estandar."""
    return usuario_factory.crear()

@pytest.fixture
def usuarios_multiple(usuario_factory):
    """Lista de usuarios de prueba."""
    return [
        usuario_factory.crear("Usuario1"),
        usuario_factory.crear("Usuario2"),
        usuario_factory.crear("Usuario3"),
    ]
```

### Test de Excepciones

```python
import pytest

def test_lanza_excepcion(mocker):
    """Test que verifica excepciones."""
    mock_guardar = mocker.patch('src.db.guardar')
    mock_guardar.side_effect = ValueError("Error de validacion")

    with pytest.raises(ValueError) as excinfo:
        guardar_usuario({"nombre": ""})

    assert "Error de validacion" in str(excinfo.value)

def test_excepcion_con_mensaje():
    """Test con raise de ValueError."""
    with pytest.raises(ValueError, match="no puede estar vacio"):
        validar_campo("")
```

---

**Ultima actualizacion:** 2026-02-08
