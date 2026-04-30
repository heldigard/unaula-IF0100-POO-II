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
git clone https://github.com/heldigard/unaula-IF0100-POO-II.git
cd IF0100-POO-II/juego-kaboom
# Abre index.html en cualquier navegador moderno
```

## Modo Clase en vivo (servidor + túnel)

1. Levanta el backend local desde la raíz del repo:

```bash
cd IF0100-POO-II
python -m pip install -r requirements.txt
python -m uvicorn backend.main:app --app-dir juego-kaboom --host 0.0.0.0 --port 8000
```

2. En el frontend (`index.html`) agrega en **Servidor de sala**:

```text
http://localhost:8000
```

3. Entra a **Modo Clase**, crea una unidad y comparte el link/QR con tus alumnos.

### Exponer el backend para celulares en otra red (gratis)

- **Cloudflare Tunnel (recomendado)**:

```bash
cloudflared tunnel --url http://localhost:8000
```

Copia la URL pública (`https://xxxxx.trycloudflare.com`) y configúrala en el campo `Servidor de sala`.

- También puedes usar `npx localtunnel --port 8000` (gratis, sin registro).  
  Copia la URL HTTPS que te entrega y configúrala en el campo `Servidor de sala`.

- `ngrok` también funciona, pero revisa sus límites por plan.

## GitHub Pages

1. En Settings > Pages, rama `main` y carpeta `/ (root)`.
2. URL esperada:
   `https://heldigard.github.io/unaula-IF0100-POO-II/juego-kaboom/`

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
4. Si la sala es en vivo, también incluye backend:

`index.html?unidad=uX&sala=XXXX&backend=https://xxxxx.trycloudflare.com`
5. Cada estudiante abre el QR/link y responde desde su móvil como en navegador desktop.

Nota importante:
- El podio de sala en vivo se sincroniza desde servidor por código de sala.
- También se mantiene el podio local como respaldo en tu navegador.

## Reglas de puntaje por ronda

- Correcta: `80 + (segundos restantes * 4)`
- Incorrecta: `-15`
- Timeout: `-10`

## Link de sala

Ejemplo de link compartible:

`index.html?unidad=u3&sala=AB12`  
`index.html?unidad=u3&sala=AB12&backend=https://xxxxx.trycloudflare.com`

`unidad` determina la temática y `sala` identifica la sesión de clase.
