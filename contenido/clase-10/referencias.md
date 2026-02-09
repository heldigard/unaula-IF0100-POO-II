# Referencias - Clase 10

**IF0100 - Lenguaje de Programacion OO II**

---

## Documentacion Oficial

| Recurso | Enlace |
|---------|--------|
| pytest Fixtures | https://docs.pytest.org/en/stable/fixture.html |
| pytest Parametrize | https://docs.pytest.org/en/stable/example/parametrize.html |
| unittest.mock | https://docs.python.org/3/library/unittest.mock.html |
| pytest-mock | https://pytest-mock.readthedocs.io/ |
| pytest-cov | https://pytest-cov.readthedocs.io/ |

---

## Recursos de Mocks

| Recurso | Enlace |
|---------|--------|
| Python Mocking 101 | https://realpython.com/python-mock-library/ |
| Getting Started with Mocks | https://docs.python.org/3/library/unittest.mock.html#quick-guide |
| pytest-mock Tutorial | https://pytest-mock.readthedocs.io/en/latest/ |

---

## Recursos de Coverage

| Recurso | Enlace |
|---------|--------|
| Coverage.py Documentacion | https://coverage.readthedocs.io/ |
| Coverage Configuration | https://coverage.readthedocs.io/en/latest/config.html |

---

## Cheat Sheets

```bash
# Fixtures
@pytest.fixture(scope="function")
def mi_fixture():
    yield "dato"
    # cleanup

# Parametrizacion
@pytest.mark.parametrize("a,b,esperado", [(1,1,2), (2,3,5)])
def test_suma(a, b, esperado):
    assert a + b == esperado

# Mocks
mocker.patch('modulo.funcion')
mocker.patch.object(Clase, 'metodo')
mocker.spy(Obj, 'metodo')

# Coverage
pytest --cov=src --cov-report=html
pytest --cov=src --cov-fail-under=90
```

---

**Ultima actualizacion:** 2026-02-08
