# TaskFlow Quest - Juego Educativo

Juego de plataformas 2D educativo para reforzar conceptos del curso **IF0100 Programación Orientada a Objetos II**.

## Descripción

- **Motor:** [KAPLAY.js](https://kaplayjs.com/) v3001.0.0
- **Estilo:** Retro oscuro, pixel-art
- **Objetivo:** Recolectar ítems, evitar bugs, responder preguntas de opción múltiple y completar 6 niveles temáticos.

## Cómo ejecutar localmente

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Eldigardo/IF0100-POO-II.git
   ```
2. Abre `juego-kaboom/index.html` directamente en tu navegador.

No requiere servidor ni dependencias externas (KAPLAY carga vía CDN).

## Despliegue en GitHub Pages

1. Ve a **Settings > Pages** del repositorio.
2. Selecciona el branch `main` y la carpeta `/ (root)`.
3. Guarda. El juego estará disponible en:
   ```
   https://Eldigardo.github.io/IF0100-POO-II/juego-kaboom/
   ```

## Controles

| Tecla | Acción |
|-------|--------|
| ← → | Moverse |
| ↑ / Espacio | Saltar |
| P | Pausar |

## Puntuación

| Acción | Puntos |
|--------|--------|
| Recolectar ítem | +50 |
| Respuesta correcta | +100 |
| Respuesta incorrecta | -50 |
| Sin errores en el nivel | x2 bonus |
| Tiempo restante | +10 pts/s |

## Datos persistentes

- **Podio:** Top 10 guardado en `localStorage` (clave `tfq_leaderboard`).
- **Último jugador:** Nombre recordado entre sesiones.
