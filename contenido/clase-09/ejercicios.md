# Ejercicios - TDD y pytest Basico

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Calculadora Basica TDD

### Requisitos

Implementar una calculadora usando TDD:

- [ ] suma(a, b)
- [ ] resta(a, b)
- [ ] multiplicacion(a, b)
- [ ] division(a, b)
- [ ] potencia(base, exponente)
- [ ] raiz_cuadrada(numero)

### Entregable

```python
# tests/test_calculadora_completa.py
import pytest
from src.calculadora.calculadora import Calculadora


class TestCalculadoraCompleta:
    """Tests para calculadora completa."""

    def setup_method(self):
        self.calc = Calculadora()

    # Tests de suma
    def test_suma_enteros(self):
        assert self.calc.sumar(5, 3) == 8

    def test_suma_decimales(self):
        assert self.calc.sumar(2.5, 1.5) == 4.0

    # Tests de division
    def test_division_exacta(self):
        assert self.calc.dividir(10, 2) == 5

    def test_division_decimal(self):
        assert self.calc.dividir(7, 2) == 3.5

    def test_division_por_cero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.dividir(10, 0)

    # Tests de potencia
    def test_potencia_base_positiva(self):
        assert self.calc.potencia(2, 3) == 8

    def test_potencia_exponente_cero(self):
        assert self.calc.potencia(5, 0) == 1

    def test_potencia_exponente_negativo(self):
        assert self.calc.potencia(2, -2) == 0.25

    # Tests de raiz cuadrada
    def test_raiz_cuadrada_numero_perfecto(self):
        assert self.calc.raiz_cuadrada(16) == 4

    def test_raiz_cuadrada_numero_decimal(self):
        assert self.calc.raiz_cuadrada(2) == pytest.approx(1.4142, rel=1e-3)

    def test_raiz_cuadrada_numero_negativo(self):
        with pytest.raises(ValueError):
            self.calc.raiz_cuadrada(-4)
```

---

## Ejercicio 2: Validador de Contraseñas TDD

### Requisitos

Implementar un validador de contraseñas:

- [ ] debe tener_minimo_8_caracteres(contrasena)
- [ ] debe_tener_mayuscula(contrasena)
- [ ] debe_tener_minuscula(contrasena)
- [ ] debe_tener_numero(contrasena)
- [ ] debe_tener_caracter_especial(contrasena)
- [ ] es_valida(contrasena)

### Entregable

```python
# tests/test_validador_contrasena.py
import pytest
from src.validador.validador import ValidadorContrasena


class TestValidadorContrasena:
    """Tests para validador de contraseñas."""

    def setup_method(self):
        self.validador = ValidadorContrasena()

    def test_contrasena_valida(self):
        assert self.validador.es_valida("Secure123!") is True

    def test_contrasena_corta(self):
        assert self.validador.es_valida("Ab1!") is False

    def test_sin_mayuscula(self):
        assert self.validador.es_valida("secure123!") is False

    def test_sin_minuscula(self):
        assert self.validador.es_valida("SECURE123!") is False

    def test_sin_numero(self):
        assert self.validador.es_valida("SecurePass!") is False

    def test_sin_caracter_especial(self):
        assert self.validador.es_valida("SecurePass123") is False

    def test_contrasena_vacia(self):
        assert self.validador.es_valida("") is False
```

---

## Ejercicio 3: Lista de Tareas TDD

### Requisitos

Implementar un gestor de tareas:

- [ ] agregar_tarea(lista, tarea)
- [ ] eliminar_tarea(lista, indice)
- [ ] marcar_completada(lista, indice)
- [ ] tareas_pendientes(lista)
- [ ] tareas_completadas(lista)

### Entregable

```python
# tests/test_lista_tareas.py
import pytest
from src.tareas.gestor_tareas import GestorTareas


class TestGestorTareas:
    """Tests para gestor de tareas."""

    def setup_method(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Comprar leche")
        assert self.gestor.obtener_tareas() == ["Comprar leche"]

    def test_agregar_multiples_tareas(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.agregar_tarea("Tarea 2")
        assert len(self.gestor.obtener_tareas()) == 2

    def test_eliminar_tarea(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.agregar_tarea("Tarea 2")
        self.gestor.eliminar_tarea(0)
        assert len(self.gestor.obtener_tareas()) == 1

    def test_marcar_completada(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.marcar_completada(0)
        assert self.gestor.esta_completada(0) is True

    def test_tareas_pendientes(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.agregar_tarea("Tarea 2")
        self.gestor.marcar_completada(0)
        assert len(self.gestor.tareas_pendientes()) == 1
```

---

## Ejercicio 4: Registro de Estudiantes TDD

### Requisitos

Implementar un sistema de registro:

- [ ] agregar_estudiante(estudiante)
- [ ] buscar_por_codigo(codigo)
- [ ] buscar_por_nombre(nombre)
- [ ] obtener_todos()
- [ ] eliminar_estudiante(codigo)

### Entregable

```python
# tests/test_registro_estudiantes.py
import pytest
from src.estudiantes.registro import RegistroEstudiantes


class TestRegistroEstudiantes:
    """Tests para registro de estudiantes."""

    def setup_method(self):
        self.registro = RegistroEstudiantes()

    def test_agregar_estudiante(self):
        self.registro.agregar_estudiante("E001", "Juan Perez")
        assert self.registro.obtener_todos() == [{"codigo": "E001", "nombre": "Juan Perez"}]

    def test_buscar_por_codigo_existente(self):
        self.registro.agregar_estudiante("E001", "Juan Perez")
        resultado = self.registro.buscar_por_codigo("E001")
        assert resultado == {"codigo": "E001", "nombre": "Juan Perez"}

    def test_buscar_por_codigo_inexistente(self):
        resultado = self.registro.buscar_por_codigo("E999")
        assert resultado is None

    def test_buscar_por_nombre(self):
        self.registro.agregar_estudiante("E001", "Juan Perez")
        self.registro.agregar_estudiante("E002", "Maria Garcia")
        resultados = self.registro.buscar_por_nombre("Juan")
        assert len(resultados) == 1
        assert resultados[0]["nombre"] == "Juan Perez"

    def test_eliminar_estudiante(self):
        self.registro.agregar_estudiante("E001", "Juan Perez")
        self.registro.eliminar_estudiante("E001")
        assert self.registro.obtener_todos() == []
```

---

## Rubrica de Evaluacion

| Criterio | Peso | Descripcion |
|----------|------|-------------|
| Coverage tests | 30% | Porcentaje de codigo probado |
| TDD aplicado | 25% | Ciclo Rojo-Verde-Refactor seguido |
| Nombres descriptivos | 15% | Tests con nombres claros |
| Assertions correctos | 15% | Uso adecuado de assert |
| Organizacion | 15% | Estructura de archivos |

---

**Ultima actualizacion:** 2026-02-08
