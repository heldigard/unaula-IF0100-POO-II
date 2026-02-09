# Codigo - pytest Avanzado

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Proyecto con Fixtures

### Estructura

```
src/
├── db/
│   ├── __init__.py
│   └── cliente_db.py
├── api/
│   ├── __init__.py
│   └── servicio_api.py
└── usuarios/
    ├── __init__.py
    └── usuario.py
tests/
├── __init__.py
├── conftest.py
├── test_usuarios.py
└── test_api.py
```

### conftest.py con Fixtures Avanzados

```python
# tests/conftest.py
import pytest
from src.db.cliente_db import ClienteDB
from src.api.servicio_api import ServicioAPI
from src.usuarios.usuario import Usuario

@pytest.fixture(scope="module")
def base_datos():
    """Base de datos para todos los tests del modulo."""
    db = ClienteDB(":memory:")
    db.crear_tablas()
    yield db
    db.cerrar()

@pytest.fixture(scope="function")
def db_limpia(base_datos):
    """Base de datos vacia para cada test."""
    base_datos.limpiar_tablas()
    return base_datos

@pytest.fixture
def usuario_ejemplo(db_limpia):
    """Usuario de ejemplo."""
    usuario = Usuario("Juan", "juan@test.com")
    db_limpia.guardar(usuario)
    return usuario

@pytest.fixture
def usuarios_ejemplo(db_limpia):
    """Lista de usuarios de ejemplo."""
    usuarios = [
        Usuario("Usuario1", "u1@test.com"),
        Usuario("Usuario2", "u2@test.com"),
        Usuario("Usuario3", "u3@test.com"),
    ]
    for u in usuarios:
        db_limpia.guardar(u)
    return usuarios

@pytest.fixture
def mock_servicio_api(mocker):
    """Mock del servicio de API."""
    mock = mocker.patch('src.api.servicio_api.ServicioAPI.obtener_datos')
    mock.return_value = {"status": "ok", "data": [1, 2, 3]}
    return mock
```

---

## 2. Tests con Parametrizacion

### Test de Calculadora Parametrizada

```python
# tests/test_calculadora_parametrizada.py
import pytest
from src.calculadora.calculadora import Calculadora

class TestCalculadoraParametrizada:
    """Tests parametrizados para Calculadora."""

    @pytest.fixture
    def calc(self):
        """Fixture de calculadora."""
        return Calculadora()

    # Tests de suma parametrizados
    @pytest.mark.parametrize("a,b,esperado", [
        (1, 1, 2),
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (-5, -3, -8),
        (100, 200, 300),
    ])
    def test_suma(self, calc, a, b, esperado):
        """Test parametrizado de suma."""
        assert calc.sumar(a, b) == esperado

    # Tests de resta parametrizados
    @pytest.mark.parametrize("a,b,esperado", [
        (10, 5, 5),
        (5, 10, -5),
        (0, 0, 0),
        (-5, -3, -2),
    ])
    def test_resta(self, calc, a, b, esperado):
        """Test parametrizado de resta."""
        assert calc.restar(a, b) == esperado

    # Tests de multiplicacion parametrizados
    @pytest.mark.parametrize("a,b,esperado", [
        (3, 4, 12),
        (0, 100, 0),
        (-2, 5, -10),
        (-3, -3, 9),
    ])
    def test_multiplicacion(self, calc, a, b, esperado):
        """Test parametrizado de multiplicacion."""
        assert calc.multiplicar(a, b) == esperado

    # Tests de division parametrizados
    @pytest.mark.parametrize("a,b,esperado", [
        (10, 2, 5),
        (7, 2, 3.5),
        (0, 5, 0),
    ])
    def test_division(self, calc, a, b, esperado):
        """Test parametrizado de division."""
        assert calc.dividir(a, b) == pytest.approx(esperado)

    # Tests de division por cero (excepciones)
    @pytest.mark.parametrize("a", [10, 0, -5, 100])
    def test_division_por_cero(self, calc, a):
        """Test de excepciones para division por cero."""
        with pytest.raises(ZeroDivisionError):
            calc.dividir(a, 0)
```

### Tests de Validador Parametrizados

```python
# tests/test_validador_parametrizado.py
import pytest
from src.validador.validador import Validador

class TestValidadorParametrizado:
    """Tests parametrizados para Validador."""

    @pytest.fixture
    def validador(self):
        """Fixture de validador."""
        return Validador()

    @pytest.mark.parametrize("email,esperado", [
        ("test@test.com", True),
        ("usuario@dominio.com", True),
        ("sin@email", False),
        ("@dominio.com", False),
        ("email@", False),
        ("", False),
    ])
    def test_es_email_valido(self, validador, email, esperado):
        """Test parametrizado de validacion de email."""
        assert validador.es_email_valido(email) == esperado

    @pytest.mark.parametrize("password,esperado", [
        ("Secure123!", True),
        ("short1!", False),
        ("nouppercase123!", False),
        ("NOLOWERCASE123!", False),
        ("NoNumbers!!", False),
        ("Valid123", True),
    ])
    def test_es_password_seguro(self, validador, password, esperado):
        """Test parametrizado de validacion de password."""
        assert validador.es_password_seguro(password) == esperado
```

---

## 3. Tests con Mocks

### Tests de API con Mocks

```python
# tests/test_api_mocks.py
import pytest
from unittest.mock import Mock, patch, MagicMock
from src.api.servicio_api import ServicioAPI
from src.usuarios.servicio_usuarios import ServicioUsuarios

class TestServicioAPIConMocks:
    """Tests del servicio API usando mocks."""

    def test_obtener_usuarios_desde_api(self, mocker):
        """Test de obtencion de usuarios con mock."""
        # Mock de la respuesta HTTP
        mock_response = mocker.patch('requests.get')
        mock_response.return_value.json.return_value = [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "Maria"},
        ]
        mock_response.return_value.status_code = 200

        servicio = ServicioAPI()
        usuarios = servicio.obtener_usuarios()

        assert len(usuarios) == 2
        assert usuarios[0]["nombre"] == "Juan"

    def test_error_conexion_api(self, mocker):
        """Test de manejo de errores de conexion."""
        mock_response = mocker.patch('requests.get')
        mock_response.return_value.raise_for_status.side_effect = ConnectionError("Sin conexion")

        servicio = ServicioAPI()

        with pytest.raises(ConnectionError):
            servicio.obtener_usuarios()

    def test_llamadas_multiple_apis(self, mocker):
        """Test con multiple llamadas a APIs."""
        mock_get = mocker.patch('requests.get')

        # Configurar diferentes respuestas
        mock_get.side_effect = [
            Mock(status_code=200, json=lambda: {"data": "usuarios"}),
            Mock(status_code=200, json=lambda: {"data": "productos"}),
        ]

        servicio = ServicioAPI()

        resultado1 = servicio.obtener_datos("usuarios")
        resultado2 = servicio.obtener_datos("productos")

        assert mock_get.call_count == 2
```

### Tests de Base de Datos con Mocks

```python
# tests/test_db_mocks.py
import pytest
from unittest.mock import Mock, patch
from src.db.cliente_db import ClienteDB
from src.usuarios.servicio_usuarios import ServicioUsuarios

class TestServicioUsuariosConMocks:
    """Tests del servicio de usuarios con mocks de BD."""

    def test_crear_usuario(self, mocker):
        """Test de creacion de usuario con mock de BD."""
        mock_db = mocker.patch('src.db.cliente_db.ClienteDB')
        mock_instance = MagicMock()
        mock_db.return_value = mock_instance

        servicio = ServicioUsuarios()
        resultado = servicio.crear_usuario("Juan", "juan@test.com")

        assert resultado is True
        mock_instance.guardar.assert_called_once()

    def test_buscar_usuario_por_id(self, mocker):
        """Test de busqueda de usuario por ID."""
        mock_db = mocker.patch('src.db.cliente_db.ClienteDB')
        mock_instance = MagicMock()
        mock_instance.buscar_por_id.return_value = {"id": 1, "nombre": "Juan"}
        mock_db.return_value = mock_instance

        servicio = ServicioUsuarios()
        usuario = servicio.buscar_usuario(1)

        assert usuario["nombre"] == "Juan"
        mock_instance.buscar_por_id.assert_called_once_with(1)

    def test_listar_todos_usuarios(self, mocker):
        """Test de listado de usuarios."""
        mock_db = mocker.patch('src.db.cliente_db.ClienteDB')
        mock_instance = MagicMock()
        mock_instance.listar_todos.return_value = [
            {"id": 1, "nombre": "Juan"},
            {"id": 2, "nombre": "Maria"},
        ]
        mock_db.return_value = mock_instance

        servicio = ServicioUsuarios()
        usuarios = servicio.listar_todos()

        assert len(usuarios) == 2

    def test_eliminar_usuario(self, mocker):
        """Test de eliminacion de usuario."""
        mock_db = mocker.patch('src.db.cliente_db.ClienteDB')
        mock_instance = MagicMock()
        mock_instance.eliminar.return_value = True
        mock_db.return_value = mock_instance

        servicio = ServicioUsuarios()
        resultado = servicio.eliminar_usuario(1)

        assert resultado is True
        mock_instance.eliminar.assert_called_once_with(1)
```

---

## 4. Tests de Integracion

```python
# tests/test_integration.py
import pytest
from src.db.cliente_db import ClienteDB
from src.usuarios.usuario import Usuario

class TestIntegracionDB:
    """Tests de integracion con base de datos real."""

    @pytest.fixture
    def db(self):
        """Fixture de base de datos real en memoria."""
        db = ClienteDB(":memory:")
        db.crear_tablas()
        yield db
        db.cerrar()

    def test_guardar_y_recuperar_usuario(self, db):
        """Test de guardado y recuperacion de usuario."""
        usuario = Usuario("Juan", "juan@test.com")
        db.guardar(usuario)

        resultado = db.buscar_por_id(1)

        assert resultado["nombre"] == "Juan"
        assert resultado["email"] == "juan@test.com"

    def test_listar_usuarios_vacios(self, db):
        """Test de listado de usuarios vacios."""
        usuarios = db.listar_todos()
        assert usuarios == []

    def test_actualizar_usuario(self, db):
        """Test de actualizacion de usuario."""
        usuario = Usuario("Juan", "juan@test.com")
        db.guardar(usuario)

        db.actualizar(1, {"nombre": "Juan Updated"})
        resultado = db.buscar_por_id(1)

        assert resultado["nombre"] == "Juan Updated"

    def test_eliminar_usuario(self, db):
        """Test de eliminacion de usuario."""
        usuario = Usuario("Juan", "juan@test.com")
        db.guardar(usuario)
        db.eliminar(1)

        usuarios = db.listar_todos()
        assert usuarios == []
```

---

## 5. Ejecucion de Tests

```bash
# Ejecutar todos los tests
pytest

# Con coverage
pytest --cov=src --cov-report=html

# Tests especificos por patron
pytest -k "test_suma"

# Tests de archivo especifico
pytest tests/test_calculadora_parametrizada.py

# Con verbosidad
pytest -v

# Detener en primer fallo
pytest -x

# Coverage minimo requerido (falla si < 80%)
pytest --cov=src --cov-fail-under=80
```

---

**Ultima actualizacion:** 2026-02-08
