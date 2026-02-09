# Ejercicios - Clases Abstractas e Interfaces

**IF0100 - Lenguaje de Programacion OO II**

---

## Ejercicio 1: Sistema de Formas de Pago

**Objetivo:** Practicar interfaces y polimorfismo

### Clases requeridas:
- `MetodoPago` (interface)
  - `procesar_pago(monto: float) -> bool`
  - `reembolsar(monto: float) -> bool`

- Implementaciones concretas:
  - `TarjetaCredito`
  - `PayPal`
  - `TransferenciaBancaria`
  - `Efectivo`

### Requisitos:
1. Cada metodo procesa y reembolsa de forma diferente
2. Simular procesamiento real
3. Calcular total de pagos procesados

---

## Ejercicio 2: Sistema de Notificaciones

**Objetivo:** Implementar estrategia de notificaciones

### Clases:
- `INotificable` (interface)
  - `enviar(mensaje: str, destinatario: str) -> bool`

- Implementaciones:
  - `EmailNotificacion`
  - `SMSNotificacion`
  - `PushNotificacion`
  - `WhatsappNotificacion`

### Requisitos:
1. Cada canal tiene formato diferente
2. Validar destinatario antes de enviar
3. Simular envio y registrar exitosos/fallidos

---

## Ejercicio 3: Editor de Documentos

**Objetivo:** Sistema de exportacion con interfaces

### Interface:
- `IExportable`
  - `exportar(formato: str) -> bytes`

### Clases:
- `Documento`
- `Presentacion`
- `HojaCalculo`

### Formatos:
- PDF
- DOCX
- HTML
- CSV

### Requisitos:
1. Cada documento puede exportar en ciertos formatos
2. Lanzar excepcion si formato no soportado
3. Contar exportaciones exitosas

---

## Ejercicio 4: Juego de Cartas (Polimorfismo)

**Objetivo:** Cartas con comportamientos diferentes

### Clases:
- `Carta` (abstracta)
  - `valor: int`
  - `color: str`

- `CartaAccion`: Roba cartas, cambia turno
- `CartaPuntuacion`: Puntos al final
- `CartaComodin`: Efecto especial

### Metodos:
- `jugar(jugador: Jugador, mesa: Mesa) -> bool`
- `__str__()`

---

## Ejercicio 5: Framework de Validadores

**Objetivo:** Sistema de validacion con interfaces

### Interface:
- `IValidador`
  - `validar(dato: any) -> tuple[bool, str]`

### Validadores:
- `ValidadorLongitud(min, max)`
- `ValidadorEmail()`
- `ValidadorNumero(min, max)`
- `ValidadorExpresion(regex)`
- `ValidadorPersonalizado(func)`

### Requisitos:
1. Encadenar validaciones
2. Devolver primer error encontrado
3. Todos deben pasar

---

## Solucion Ejercicio 1 (Referencia)

```python
from abc import ABC, abstractmethod
from typing import List


class MetodoPago(ABC):
    """Interface para metodos de pago"""

    @property
    @abstractmethod
    def nombre(self) -> str: ...

    @abstractmethod
    def procesar_pago(self, monto: float) -> bool: ...

    @abstractmethod
    def reembolsar(self, monto: float) -> bool: ...


class TarjetaCredito(MetodoPago):
    def __init__(self, numero: str, banco: str):
        self._numero = numero[-4:]  # Solo ultimos 4 digitos
        self._banco = banco

    @property
    def nombre(self) -> str:
        return f"Tarjeta {self._banco} ****{self._numero}"

    def procesar_pago(self, monto: float) -> bool:
        print(f"[Tarjeta] Procesando ${monto:,.2f}")
        return monto > 0

    def reembolsar(self, monto: float) -> bool:
        print(f"[Tarjeta] Reembolsando ${monto:,.2f}")
        return monto > 0


class PayPal(MetodoPago):
    def __init__(self, email: str):
        self._email = email

    @property
    def nombre(self) -> str:
        return f"PayPal ({self._email})"

    def procesar_pago(self, monto: float) -> bool:
        print(f"[PayPal] Procesando ${monto:,.2f}")
        return monto > 0

    def reembolsar(self, monto: float) -> bool:
        print(f"[PayPal] Reembolsando ${monto:,.2f}")
        return monto > 0


# Continuara...
```

---

**Ultima actualizacion:** 2026-02-08
