# Codigo - Clases Abstractas e Interfaces

**IF0100 - Lenguaje de Programacion OO II**

---

## 1. Sistema de Figuras Geometricas (Completo)

```python
from abc import ABC, abstractmethod
from math import pi, sqrt
from typing import List


class Figura(ABC):
    """Clase abstracta base para figuras geometricas"""

    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, valor: str) -> None:
        self._color = valor

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def escalar(self, factor: float) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (color: {self._color})"


class Rectangulo(Figura):
    """Rectangulo con lados diferentes"""

    def __init__(self, ancho: float, alto: float, color: str = "azul"):
        super().__init__(color)
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self) -> float:
        return self._ancho

    @property
    def alto(self) -> float:
        return self._alto

    def area(self) -> float:
        return self._ancho * self._alto

    def perimetro(self) -> float:
        return 2 * (self._ancho + self._alto)

    def escalar(self, factor: float) -> None:
        self._ancho *= factor
        self._alto *= factor

    def __str__(self) -> str:
        return f"Rectangulo {self._ancho}x{self._alto} ({self._color})"


class Cuadrado(Rectangulo):
    """Cuadrado especial (hereda de Rectangulo)"""

    def __init__(self, lado: float, color: str = "amarillo"):
        super().__init__(lado, lado, color)

    def __str__(self) -> str:
        return f"Cuadrado {self._ancho}x{self._alto} ({self._color})"


class Circulo(Figura):
    """Circulo con radio"""

    def __init__(self, radio: float, color: str = "rojo"):
        super().__init__(color)
        self._radio = radio

    @property
    def radio(self) -> float:
        return self._radio

    def area(self) -> float:
        return pi * self._radio ** 2

    def perimetro(self) -> float:
        return 2 * pi * self._radio

    def escalar(self, factor: float) -> None:
        self._radio *= factor

    def __str__(self) -> str:
        return f"Circulo r={self._radio:.2f} ({self._color})"


class Triangulo(Figura):
    """Triangulo equilatero"""

    def __init__(self, lado: float, color: str = "verde"):
        super().__init__(color)
        self._lado = lado

    @property
    def lado(self) -> float:
        return self._lado

    def area(self) -> float:
        return (self._lado ** 2 * sqrt(3)) / 4

    def perimetro(self) -> float:
        return 3 * self._lado

    def escalar(self, factor: float) -> None:
        self._lado *= factor

    def __str__(self) -> str:
        return f"Triangulo lado={self._lado:.2f} ({self._color})"


if __name__ == "__main__":
    figuras: List[Figura] = [
        Rectangulo(5, 3, "azul"),
        Cuadrado(4, "amarillo"),
        Circulo(3, "rojo"),
        Triangulo(6, "verde")
    ]

    print("=== FIGURAS GEOMETRICAS ===\n")

    for figura in figuras:
        print(figura)
        print(f"  Area: {figura.area():.2f}")
        print(f"  Perimetro: {figura.perimetro():.2f}\n")

    # Escalar todas al 150%
    print("Escalando figuras al 150%...")
    for figura in figuras:
        figura.escalar(1.5)
        print(f"{figura}: Area={figura.area():.2f}")
```

---

## 2. Sistema de Empleados con Clases Abstractas

```python
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Empleado(ABC):
    """Clase abstracta para empleados"""

    def __init__(self, nombre: str, identificacion: str):
        self._nombre = nombre
        self._id = identificacion
        self._fecha_ingreso = datetime.now()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def identificacion(self) -> str:
        return self._id

    @abstractmethod
    def calcular_salario(self) -> float:
        """Metodo abstracto - cada tipo lo implementa diferente"""
        pass

    @abstractmethod
    def obtener_bonificaciones(self) -> float:
        """Metodo abstracto para bonificaciones"""
        pass

    def tiempo_servicio(self) -> int:
        """Metodo concreto - coman a todos"""
        return datetime.now().year - self._fecha_ingreso.year

    def __str__(self) -> str:
        return f"{self._nombre} ({self._id}) - Salario: ${self.calcular_salario():,.2f}"


class EmpleadoTiempoCompleto(Empleado):
    """Empleado con salario fijo mensual"""

    def __init__(self, nombre: str, identificacion: str,
                 salario_mensual: float, bono_asistencia: float = 0):
        super().__init__(nombre, identificacion)
        self._salario_mensual = salario_mensual
        _bono_asistencia = bono_asistencia

    def calcular_salario(self) -> float:
        return self._salario_mensual + self._bono_asistencia

    def obtener_bonificaciones(self) -> float:
        return self._bono_asistencia


class EmpleadoPorHoras(Empleado):
    """Empleado que cobra por horas trabajadas"""

    def __init__(self, nombre: str, identificacion: str,
                 horas_trabajadas: float, tarifa_hora: float):
        super().__init__(nombre, identificacion)
        self._horas = horas_trabajadas
        self._tarifa = tarifa_hora

    def calcular_salario(self) -> float:
        return self._horas * self._tarifa

    def obtener_bonificaciones(self) -> float:
        return 0  # No tiene bonificaciones


class EmpleadoComisionista(Empleado):
    """Empleado con salario base + comision"""

    def __init__(self, nombre: str, identificacion: str,
                 salario_base: float, total_ventas: float, porcentaje_comision: float):
        super().__init__(nombre, identificacion)
        self._salario_base = salario_base
        self._ventas = total_ventas
        self._porcentaje = porcentaje_comision

    def calcular_salario(self) -> float:
        return self._salario_base + (self._ventas * self._porcentaje / 100)

    def obtener_bonificaciones(self) -> float:
        return self._ventas * self._porcentaje / 100


class EmpleadoPorProyecto(Empleado):
    """Empleado con pago por proyecto completado"""

    def __init__(self, nombre: str, identificacion: str,
                 valor_proyecto: float, porcentaje_avance: float):
        super().__init__(nombre, identificacion)
        self._valor = valor_proyecto
        self._avance = porcentaje_avance

    def calcular_salario(self) -> float:
        return self._valor * (self._avance / 100)

    def obtener_bonificaciones(self) -> float:
        return self._valor * 0.05 if self._avance >= 100 else 0


def procesar_nomina(empleados: List[Empleado]) -> None:
    """Procesa nomina con polimorfismo"""
    print("=== PROCESO DE NOMINA ===\n")

    total = 0
    for emp in empleados:
        salario = emp.calcular_salario()
        bono = emp.obtener_bonificaciones()
        total += salario

        print(f"Empleado: {emp.nombre}")
        print(f"  ID: {emp.identificacion}")
        print(f"  Tiempo de servicio: {emp.tiempo_servicio()} años")
        print(f"  Salario base: ${salario:,.2f}")
        print(f"  Bonificaciones: ${bono:,.2f}")
        print(f"  Total: ${salario + bono:,.2f}\n")

    print(f"Total nomina: ${total:,.2f}")


if __name__ == "__main__":
    empleados = [
        EmpleadoTiempoCompleto("Ana Garcia", "001", 2500000, 200000),
        EmpleadoPorHoras("Carlos Rodriguez", "002", 160, 25000),
        EmpleadoComisionista("Maria Lopez", "003", 1500000, 50000000, 5),
        EmpleadoPorProyecto("Pedro Martinez", "004", 10000000, 75)
    ]

    procesar_nomina(empleados)
```

---

## 3. Sistema de Repositorios (Interface Pattern)

```python
from abc import ABC, abstractmethod
from typing import List, Optional


class IRepositorio(ABC):
    """Interface base para repositorios"""

    @abstractmethod
    def guardar(self, entidad) -> None: ...

    @abstractmethod
    def buscar_por_id(self, id: int): ...

    @abstractmethod
    def listar_todos(self) -> List: ...

    @abstractmethod
    def eliminar(self, id: int) -> None: ...

    @abstractmethod
    def contar(self) -> int: ...


class Usuario:
    """Entidad Usuario"""

    def __init__(self, id: int, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __str__(self) -> str:
        return f"Usuario({self.id}): {self.nombre} <{self.email}>"


class UsuarioRepositorio(IRepositorio):
    """Implementacion en memoria"""

    def __init__(self):
        self._usuarios = {}
        self._contador = 0

    def guardar(self, usuario: Usuario) -> None:
        if usuario.id is None:
            self._contador += 1
            usuario.id = self._contador
        self._usuarios[usuario.id] = usuario

    def buscar_por_id(self, id: int) -> Optional[Usuario]:
        return self._usuarios.get(id)

    def listar_todos(self) -> List[Usuario]:
        return list(self._usuarios.values())

    def eliminar(self, id: int) -> None:
        if id in self._usuarios:
            del self._usuarios[id]

    def contar(self) -> int:
        return len(self._usuarios)


class Producto:
    """Entidad Producto"""

    def __init__(self, id: int, nombre: str, precio: float):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f"Producto({self.id}): {self.nombre} - ${self.precio:,.2f}"


class ProductoRepositorio(IRepositorio):
    """Implementacion para productos"""

    def __init__(self):
        self._productos = {}

    def guardar(self, producto: Producto) -> None:
        self._productos[producto.id] = producto

    def buscar_por_id(self, id: int) -> Optional[Producto]:
        return self._productos.get(id)

    def listar_todos(self) -> List[Producto]:
        return list(self._productos.values())

    def eliminar(self, id: int) -> None:
        if id in self._productos:
            del self._productos[id]

    def contar(self) -> int:
        return len(self._productos)


# Uso con polimorfismo
def operaciones_basicas(repo: IRepositorio) -> None:
    """Demo que funciona con cualquier repositorio"""
    print(f"\n=== Operando con {repo.__class__.__name__} ===")
    print(f"Total registros: {repo.contar()}")


if __name__ == "__main__":
    # Repositorio de usuarios
    repo_usuarios = UsuarioRepositorio()
    repo_usuarios.guardar(Usuario(None, "Ana", "ana@email.com"))
    repo_usuarios.guardar(Usuario(None, "Carlos", "carlos@email.com"))

    # Repositorio de productos
    repo_productos = ProductoRepositorio()
    repo_productos.guardar(Producto(1, "Laptop", 1500000))
    repo_productos.guardar(Producto(2, "Mouse", 50000))

    # Polimorfismo
    operaciones_basicas(repo_usuarios)
    operaciones_basicas(repo_productos)

    # Listar todos
    print("\nUsuarios:")
    for u in repo_usuarios.listar_todos():
        print(f"  {u}")

    print("\nProductos:")
    for p in repo_productos.listar_todos():
        print(f"  {p}")
```

---

## 4. Plugins con Interfaces

```python
from abc import ABC, abstractmethod
from typing import Dict, List


class IPlugin(ABC):
    """Interface base para plugins"""

    @property
    @abstractmethod
    def nombre(self) -> str: ...

    @property
    @abstractmethod
    def version(self) -> str: ...

    @abstractmethod
    def inicializar(self) -> None: ...

    @abstractmethod
    def ejecutar(self, datos: Dict) -> Dict: ...


class PluginLogger(IPlugin):
    """Plugin para logging"""

    @property
    def nombre(self) -> str:
        return "Logger Plugin"

    @property
    def version(self) -> str:
        return "1.0.0"

    def inicializar(self) -> None:
        print("[Logger] Inicializado")

    def ejecutar(self, datos: Dict) -> Dict:
        print(f"[Logger] Registrando: {datos}")
        datos["log"] = True
        return datos


class PluginValidador(IPlugin):
    """Plugin para validacion de datos"""

    @property
    def nombre(self) -> str:
        return "Validador Plugin"

    @property
    def version(self) -> str:
        return "2.0.1"

    def inicializar(self) -> None:
        print("[Validador] Inicializado")

    def ejecutar(self, datos: Dict) -> Dict:
        datos["validado"] = "email" in datos
        print(f"[Validador] Datos validados: {datos['validado']}")
        return datos


class PluginCalculadora(IPlugin):
    """Plugin para calculos"""

    @property
    def nombre(self) -> str:
        return "Calculadora Plugin"

    @property
    def version(self) -> str:
        return "1.2.0"

    def inicializar(self) -> None:
        print("[Calculadora] Inicializada")

    def ejecutar(self, datos: Dict) -> Dict:
        if "a" in datos and "b" in datos:
            datos["suma"] = datos["a"] + datos["b"]
            datos["producto"] = datos["a"] * datos["b"]
        return datos


class GestorPlugins:
    """Gestiona la ejecucion de plugins"""

    def __init__(self):
        self._plugins: List[IPlugin] = []

    def registrar_plugin(self, plugin: IPlugin) -> None:
        self._plugins.append(plugin)
        print(f"Registrado: {plugin.nombre} v{plugin.version}")

    def inicializar_todos(self) -> None:
        print("=== INICIALIZANDO PLUGINS ===")
        for plugin in self._plugins:
            plugin.inicializar()

    def ejecutar_pipeline(self, datos: Dict) -> Dict:
        print("\n=== EJECUTANDO PIPELINE ===")
        resultado = datos
        for plugin in self._plugins:
            resultado = plugin.ejecutar(resultado)
        return resultado


if __name__ == "__main__":
    gestor = GestorPlugins()

    # Registrar plugins
    gestor.registrar_plugin(PluginLogger())
    gestor.registrar_plugin(PluginValidador())
    gestor.registrar_plugin(PluginCalculadora())

    # Inicializar y ejecutar
    gestor.inicializar_todos()

    datos_entrada = {
        "email": "test@email.com",
        "a": 10,
        "b": 5
    }

    resultado = gestor.ejecutar_pipeline(datos_entrada)
    print(f"\nResultado final: {resultado}")
```

---

**Ultima actualizacion:** 2026-02-08
