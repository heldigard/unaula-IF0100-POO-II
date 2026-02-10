# Ejercicios - pytest Avanzado

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Sistema de Inventario con Fixtures

### Requisitos

Implementar un sistema de inventario usando fixtures avanzados:

- [ ] `Inventario` class con productos
- [ ] Fixture con scope="module" para base de datos
- [ ] Fixture con scope="function" para inventario limpio
- [ ] Factory fixture para crear productos

### Entregable

```python
# tests/test_inventario_fixtures.py
import pytest
from src.inventario.inventario import Inventario
from src.inventario.producto import Producto


class TestInventarioFixtures:
    """Tests del sistema de inventario con fixtures."""

    @pytest.fixture
    def inventario_vacio(self, inv_modulo):
        """Inventario vacio."""
        inv_modulo.limpiar()
        return inv_modulo

    @pytest.fixture
    def inventario_con_productos(self, inv_modulo, producto_factory):
        """Inventario con productos."""
        inv_modulo.limpiar()
        inv_modulo.agregar(producto_factory.crear("P001", "Producto 1", 100))
        inv_modulo.agregar(producto_factory.crear("P002", "Producto 2", 200))
        return inv_modulo

    def test_agregar_producto(self, inventario_vacio):
        """Test agregar producto."""
        producto = Producto("P001", "Test", 100)
        inventario_vacio.agregar(producto)
        assert inventario_vacio.contar() == 1

    def test_eliminar_producto(self, inventario_con_productos):
        """Test eliminar producto."""
        inventario_con_productos.eliminar("P001")
        assert inventario_con_productos.contar() == 1

    def test_buscar_producto_existente(self, inventario_con_productos):
        """Test buscar producto existente."""
        producto = inventario_con_productos.buscar("P001")
        assert producto is not None
        assert producto.nombre == "Producto 1"

    def test_buscar_producto_inexistente(self, inventario_vacio):
        """Test buscar producto inexistente."""
        producto = inventario_vacio.buscar("P999")
        assert producto is None

    def test_listar_todos_productos(self, inventario_con_productos):
        """Test listar todos los productos."""
        productos = inventario_con_productos.listar_todos()
        assert len(productos) == 2

    def test_total_inventario(self, inventario_con_productos):
        """Test total del inventario."""
        total = inventario_con_productos.calcular_total()
        assert total == 300  # 100 + 200
```

---

## Ejercicio 2: Servicio de Pagos con Mocks

### Requisitos

Implementar y probar un servicio de pagos:

- [ ] `ServicioPagos` que llama a API externa
- [ ] Mock de processor de pagos
- [ ] Tests de exito y fracaso
- [ ] Verificacion de llamadas al mock

### Entregable

```python
# tests/test_pagos_mocks.py
import pytest
from unittest.mock import Mock, patch
from src.pagos.processor import Processor
from src.pagos.servicio_pagos import ServicioPagos


class TestServicioPagosMocks:
    """Tests del servicio de pagos con mocks."""

    @pytest.fixture
    def mock_processor(self, mocker):
        """Mock del processor de pagos."""
        mock = mocker.patch('src.pagos.processor.Processor')
        return mock

    def test_procesar_pago_exitoso(self, mock_processor):
        """Test de pago exitoso."""
        mock_processor.return_value.procesar.return_value = {
            "status": "success",
            "transaction_id": "TX123"
        }

        servicio = ServicioPagos()
        resultado = servicio.procesar_pago(100.00, "card-token")

        assert resultado["status"] == "success"
        mock_processor.return_value.procesar.assert_called_once()

    def test_procesar_pago_fallido(self, mock_processor):
        """Test de pago fallido."""
        mock_processor.return_value.procesar.return_value = {
            "status": "failed",
            "error": "Fondos insuficientes"
        }

        servicio = ServicioPagos()
        resultado = servicio.procesar_pago(100.00, "card-token")

        assert resultado["status"] == "failed"

    def test_reembolso(self, mock_processor):
        """Test de reembolso."""
        mock_processor.return_value.reembolsar.return_value = {
            "status": "refunded",
            "amount": 50.00
        }

        servicio = ServicioPagos()
        resultado = servicio.reembolsar("TX123", 50.00)

        assert resultado["status"] == "refunded"
        mock_processor.return_value.reembolsar.assert_called_once_with("TX123", 50.00)

    def test_error_conexion(self, mock_processor):
        """Test de error de conexion."""
        mock_processor.return_value.procesar.side_effect = ConnectionError("Sin conexion")

        servicio = ServicioPagos()

        with pytest.raises(ConnectionError):
            servicio.procesar_pago(100.00, "card-token")
```

---

## Ejercicio 3: API REST con Parametrizacion

### Requisitos

Probar endpoints de API REST con tests parametrizados:

- [ ] Endpoints: GET, POST, PUT, DELETE
- [ ] Parametrizar diferentes inputs
- [ ] Verificar respuestas y codigos de estado

### Entregable

```python
# tests/test_api_parametrizada.py
import pytest
from src.api.cliente import APIClient


class TestAPIUsuariosParametrizada:
    """Tests parametrizados de API de usuarios."""

    @pytest.fixture
    def api_client(self):
        """Fixture de API client."""
        return APIClient(base_url="https://api.test.com")

    # GET Tests
    @pytest.mark.parametrize("user_id,esperado", [
        (1, {"id": 1, "nombre": "Juan"}),
        (2, {"id": 2, "nombre": "Maria"}),
    ])
    def test_obtener_usuario(self, api_client, mocker, user_id, esperado):
        """Test de obtencion de usuario."""
        mocker.patch('requests.get')
        api_client.get.return_value.json.return_value = esperado
        api_client.get.return_value.status_code = 200

        resultado = api_client.get(f"/usuarios/{user_id}")

        assert resultado.json() == esperado
        assert resultado.status_code == 200

    # POST Tests
    @pytest.mark.parametrize("datos,esperado_codigo", [
        ({"nombre": "Nuevo", "email": "nuevo@test.com"}, 201),
        ({"nombre": "Test"}, 400),  # Email requerido
    ])
    def test_crear_usuario(self, api_client, mocker, datos, esperado_codigo):
        """Test de creacion de usuario."""
        mocker.patch('requests.post')
        api_client.post.return_value.status_code = esperado_codigo

        resultado = api_client.post("/usuarios", json=datos)

        assert resultado.status_code == esperado_codigo

    # PUT Tests
    @pytest.mark.parametrize("user_id,datos,esperado_codigo", [
        (1, {"nombre": "Actualizado"}, 200),
        (999, {"nombre": "Test"}, 404),
    ])
    def test_actualizar_usuario(self, api_client, mocker, user_id, datos, esperado_codigo):
        """Test de actualizacion de usuario."""
        mocker.patch('requests.put')
        api_client.put.return_value.status_code = esperado_codigo

        resultado = api_client.put(f"/usuarios/{user_id}", json=datos)

        assert resultado.status_code == esperado_codigo

    # DELETE Tests
    @pytest.mark.parametrize("user_id,esperado_codigo", [
        (1, 204),
        (999, 404),
    ])
    def test_eliminar_usuario(self, api_client, mocker, user_id, esperado_codigo):
        """Test de eliminacion de usuario."""
        mocker.patch('requests.delete')
        api_client.delete.return_value.status_code = esperado_codigo

        resultado = api_client.delete(f"/usuarios/{user_id}")

        assert resultado.status_code == esperado_codigo
```

---

## Ejercicio 4: Coverage Challenge

### Requisitos

Alcanzar coverage del 90%:

- [ ] Implementar todas las funciones requeridas
- [ ] Escribir tests que cubran todos los casos
- [ ] Verificar coverage con `pytest --cov`

### Verificacion

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=90
```

---

## Rubrica de Evaluacion

| Criterio | Peso | Descripcion |
|----------|------|-------------|
| Coverage | 25% | Porcentaje de coverage alcanzado |
| Fixtures avanzados | 25% | Uso correcto de scopes y autouse |
| Mocks | 20% | Implementacion correcta de mocks |
| Parametrizacion | 20% | Tests bien parametrizados |
| Organizacion | 10% | Estructura y limpieza del codigo |

---

**Ultima actualizacion:** 2026-02-08
