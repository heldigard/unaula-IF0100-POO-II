# Kaboom Clase IF0100 - POO II

Juego de preguntas por tiempo para clase:
**una pregunta a la vez, tiempo límite por pregunta, puntaje por rapidez y ranking local**.

Este archivo reemplaza la modalidad de plataformas anterior y deja el juego listo para repaso rápido en GitHub Pages.

## Funcionalidad

- Selección de unidad (`u0` a `u5`) por tema.
- 20 segundos por pregunta.
- Puntuación por respuesta correcta + bonus de tiempo restante.
- Penalización en respuesta incorrecta o timeout.
- Podio local en `localStorage` (sin servidor).
- En modo clase, el podio se guarda por código de sala para decidir ganadores de la sesión.
- Modo clase: genera link con `unidad` y `sala` para compartir.
- Sala lista con código QR para acceso rápido desde celular.

## Preguntas y contenido

Las preguntas están por unidad:

- `u0`: Fundamentos de Python
- `u1`: POO
- `u2`: TDD / BDD / DDD
- `u3`: FastAPI
- `u4`: SQLAlchemy
- `u5`: Clean Architecture

## Ejecutar localmente

```bash
git clone https://github.com/Eldigardo/IF0100-POO-II.git
cd IF0100-POO-II/juego-kaboom
# Abre index.html en cualquier navegador moderno
```

## GitHub Pages

1. En Settings > Pages, rama `main` y carpeta `/ (root)`.
2. URL esperada:
   `https://Eldigardo.github.io/IF0100-POO-II/juego-kaboom/`

## Flujo de juego

1. En menú, escribes tu nombre y seleccionas **Jugar** o **Modo Clase**.
2. Elegir unidad.
3. En cada pregunta:
   - tienes 20 segundos,
   - seleccionas una opción,
   - pasa a la siguiente pregunta automáticamente.
4. Al terminar, se muestra score final y se guarda el resultado en el podio de la sesión.

### Modo clase desde celular

1. Entra al **Modo Clase** y elige unidad.
2. Copia el link o enseña el QR generado a los estudiantes.
3. El link de la sala se ve como `index.html?unidad=uX&sala=XXXX`.
4. Cada estudiante abre el QR/link y responde desde su móvil como en navegador desktop.

Nota importante:
- El podio de sala se guarda en el navegador de cada dispositivo (localStorage).
- Para competir en vivo en muchos dispositivos, usa un método de recolección (por ejemplo que cada alumno comparta su texto de resultado) y consolida en una pantalla de clase.

## Reglas de puntaje por ronda

- Correcta: `80 + (segundos restantes * 4)`
- Incorrecta: `-15`
- Timeout: `-10`

## Link de sala

Ejemplo de link compartible:

`index.html?unidad=u3&sala=AB12`

`unidad` determina la temática y `sala` identifica la sesión de clase.
