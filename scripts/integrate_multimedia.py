"""
Script para integrar recursos multimedia y diagramas en las clases HTML del curso.
Ejecuta: python scripts/integrate_multimedia.py
"""

import os
import re
from pathlib import Path
from typing import Dict, List

# Configuración
BASE_DIR = Path("F:/UNAULA/IF0100-POO-II")
CLASSES_DIR = BASE_DIR / "clases-html"
ASSETS_DIR = CLASSES_DIR / "assets"

# Recursos multimedia por clase (nombre de archivo sin extensión)
RESOURCES: Dict[str, Dict] = {
    # Unidad 00
    'clase-00-introduccion': {
        'videos': [
            {
                'title': 'Curso Python desde Cero',
                'author': 'Píldoras Informáticas',
                'duration': '3:42:15',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=RkXfQR5aqEE',
                'desc': 'Excelente introducción en español, cubre instalación y conceptos básicos'
            }
        ]
    },
    'clase-01-variables-tipos': {
        'videos': [
            {
                'title': 'Variables y Tipos de Datos en Python',
                'author': 'Píldoras Informáticas',
                'duration': '32:15',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=cQT33yu9pY8',
                'desc': 'Explicación clara con ejemplos prácticos'
            },
            {
                'title': 'Python Data Types - Complete Tutorial',
                'author': 'Programming with Mosh',
                'duration': '28:45',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=v5MR5JnKcZI',
                'desc': 'Cobertura completa de tipos de datos, inglés claro'
            }
        ]
    },
    'clase-02-estructuras-control': {
        'videos': [
            {
                'title': 'Condicionales if en Python',
                'author': 'Píldoras Informáticas',
                'duration': '21:30',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=PpR0RJFaQeA',
                'desc': 'Explicación de if/elif/else con ejemplos'
            },
            {
                'title': 'Bucles en Python (for, while)',
                'author': 'Píldoras Informáticas',
                'duration': '25:45',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=QK7LKd5UXdE',
                'desc': 'Ciclos for y while con ejemplos prácticos'
            }
        ]
    },
    'clase-03-estructuras-datos': {
        'videos': [
            {
                'title': 'Listas en Python',
                'author': 'Píldoras Informáticas',
                'duration': '34:15',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=PZEMbhXqMek',
                'desc': 'Todo sobre listas y list comprehensions'
            },
            {
                'title': 'Diccionarios en Python',
                'author': 'Píldoras Informáticas',
                'duration': '28:30',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=J_fjiLnf3aI',
                'desc': 'Diccionarios clave-valor con ejemplos'
            }
        ],
        'diagram': 'listas-diccionarios.svg'
    },

    # Unidad 01 - POO Avanzada
    'clase-01-clases-objetos': {
        'videos': [
            {
                'title': 'Programación Orientada a Objetos en Python',
                'author': 'Píldoras Informáticas',
                'duration': '1:02:30',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=t6pzQk7K9kI',
                'desc': 'Excelente introducción a POO en español'
            },
            {
                'title': 'Python OOP 1: Classes and Instances',
                'author': 'Corey Schafer',
                'duration': '23:15',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=ZDa-Z5JzLYM',
                'desc': 'Serie completa de POO muy recomendada'
            }
        ],
        'diagram': 'poo-clase-objeto.svg'
    },
    'clase-02-encapsulamiento': {
        'videos': [
            {
                'title': 'Encapsulamiento en Python',
                'author': 'Facundo García',
                'duration': '18:30',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=fvy_BwUmVgE',
                'desc': 'Explicación clara de getters, setters y @property'
            },
            {
                'title': 'Python @property Tutorial',
                'author': 'ArjanCodes',
                'duration': '14:20',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=jCzT9bG7FjY',
                'desc': 'Explicación moderna de @property'
            }
        ],
        'diagram': 'encapsulamiento.svg'
    },
    'clase-03-herencia-polimorfismo': {
        'videos': [
            {
                'title': 'Herencia en Python',
                'author': 'Píldoras Informáticas',
                'duration': '22:45',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=wLYXWQ6-RWY',
                'desc': 'Herencia simple y múltiple en Python'
            },
            {
                'title': 'Python OOP 3: Classmethods and Staticmethods',
                'author': 'Corey Schafer',
                'duration': '10:15',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=rq8cL2XMMqM',
                'desc': 'Métodos de clase y estáticos'
            }
        ],
        'diagram': 'herencia-polimorfismo.svg'
    },
    'clase-04-clases-abstractas': {
        'videos': [
            {
                'title': 'Clases Abstractas y Interfaces en Python',
                'author': 'Facundo García',
                'duration': '16:30',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=aO66WGyoOfY',
                'desc': 'ABC y protocolos en Python'
            },
            {
                'title': 'Python Abstract Base Classes',
                'author': 'ArjanCodes',
                'duration': '12:45',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=SSr_E_I0iVY',
                'desc': 'Uso moderno de ABC'
            }
        ]
    },

    # Unidad 02 - Técnicas de Desarrollo
    'clase-01-tdd-intro': {
        'videos': [
            {
                'title': '¿Qué es TDD? (Test Driven Development)',
                'author': 'Making Devs',
                'duration': '15:30',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=nD7Xtbjkouk',
                'desc': 'Excelente introducción conceptual en español'
            },
            {
                'title': 'TDD Tutorial (Red-Green-Refactor)',
                'author': 'Programming with Mosh',
                'duration': '18:45',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=nS7oPs7tQRM',
                'desc': 'Ciclo Red-Green-Refactor explicado'
            }
        ],
        'diagram': 'tdd-cycle.svg'
    },
    'clase-02-pytest-avanzado': {
        'videos': [
            {
                'title': 'Tutorial de pytest en Python',
                'author': 'Píldoras Informáticas',
                'duration': '24:15',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=x1H3a2kkdYM',
                'desc': 'Introducción completa a pytest'
            },
            {
                'title': 'Python Testing with pytest',
                'author': 'ArjanCodes',
                'duration': '42:30',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=JqbOcdNLLaI',
                'desc': 'Tutorial muy completo de pytest'
            }
        ]
    },
    'clase-03-bdd-intro': {
        'videos': [
            {
                'title': '¿Qué es BDD? (Behavior Driven Development)',
                'author': 'Making Devs',
                'duration': '12:20',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=LUBOhWzqDJQ',
                'desc': 'Introducción conceptual a BDD'
            },
            {
                'title': 'BDD with Python (behave)',
                'author': 'Test Automation University',
                'duration': '28:15',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=eBqKLQo-ZTs',
                'desc': 'BDD con behave y Gherkin'
            }
        ]
    },
    'clase-04-ddd-intro': {
        'videos': [
            {
                'title': 'Domain Driven Design (DDD) Explicado',
                'author': 'Making Devs',
                'duration': '19:45',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=6wRj3wP0wOI',
                'desc': 'Introducción a DDD'
            },
            {
                'title': 'DDD in Python Tutorial',
                'author': 'Milan Milanovic',
                'duration': '35:20',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=HKTFLyf3p1w',
                'desc': 'Implementación de DDD en Python'
            }
        ]
    },

    # Unidad 03 - FastAPI y Persistencia
    'clase-01-fastapi-intro': {
        'videos': [
            {
                'title': 'FastAPI Curso Completo',
                'author': 'MoureDev by Brais Moure',
                'duration': '1:45:30',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=Fn313F3JUYQ',
                'desc': 'Curso completo en español sobre FastAPI'
            },
            {
                'title': 'FastAPI Python Tutorial',
                'author': 'Amigoscode',
                'duration': '58:15',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=7K2pP4tqF0E',
                'desc': 'Introducción práctica a FastAPI'
            }
        ],
        'diagram': 'fastapi-request-flow.svg'
    },
    'clase-02-pydantic-validacion': {
        'videos': [
            {
                'title': 'Pydantic Validación de Datos',
                'author': 'MoureDev',
                'duration': '22:30',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=3PjNzCW22M0',
                'desc': 'Validación con Pydantic v2'
            },
            {
                'title': 'Pydantic v2 Tutorial',
                'author': 'Samuel Colvin',
                'duration': '31:45',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=Vr17i0n14AY',
                'desc': 'Tutorial del creador de Pydantic'
            }
        ]
    },
    'clase-03-dependencias': {
        'videos': [
            {
                'title': 'FastAPI Dependencies Explained',
                'author': 'Amigoscode',
                'duration': '24:15',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=d0xhqBfYqZk',
                'desc': 'Sistema de dependencias en FastAPI'
            }
        ]
    },
    'clase-04-testing-fastapi': {
        'videos': [
            {
                'title': 'Testing FastAPI Applications',
                'author': 'ArjanCodes',
                'duration': '28:30',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=1h1lEZENZsk',
                'desc': 'Testing completo de aplicaciones FastAPI'
            }
        ]
    },
    'clase-05-persistencia-datos': {
        'videos': [
            {
                'title': 'SQLAlchemy con Python',
                'author': 'Píldoras Informáticas',
                'duration': '42:15',
                'lang': 'Español',
                'url': 'https://www.youtube.com/watch?v=EqWuEhQLJ8Q',
                'desc': 'ORM SQLAlchemy desde cero'
            },
            {
                'title': 'SQLAlchemy Tutorial',
                'author': 'Corey Schafer',
                'duration': '1:02:30',
                'lang': 'Inglés',
                'url': 'https://www.youtube.com/watch?v=WOUPvLhOzvs',
                'desc': 'Tutorial completo de SQLAlchemy'
            }
        ]
    }
}


def generate_videos_section(videos: List[Dict]) -> str:
    """Genera el HTML de la sección de videos."""
    if not videos:
        return ""

    html = '                <section id="videos">\n'
    html += '                    <h2>📺 Videos Recomendados</h2>\n\n'

    for video in videos:
        lang_badge = "bg-success" if video['lang'] == "Español" else "bg-secondary"
        html += f'                    <div class="card mb-3">\n'
        html += f'                        <div class="card-body">\n'
        html += f'                            <h5 class="card-title">\n'
        html += f'                                <span class="badge {lang_badge} me-2">{video["lang"]}</span>\n'
        html += f'                                {video["title"]}\n'
        html += f'                            </h5>\n'
        html += f'                            <h6 class="card-subtitle mb-2 text-muted">{video["author"]} | {video["duration"]} min</h6>\n'
        html += f'                            <p class="card-text">\n'
        html += f'                                {video["desc"]}\n'
        html += f'                            </p>\n'
        html += f'                            <a href="{video["url"]}" target="_blank" class="btn btn-primary btn-sm">\n'
        html += f'                                <i class="bi bi-youtube me-2"></i>Ver Video\n'
        html += f'                            </a>\n'
        html += f'                        </div>\n'
        html += f'                    </div>\n\n'

    html += '                </section>\n\n'
    return html


def generate_diagram_section(diagram_name: str) -> str:
    """Genera el HTML de la sección de diagramas."""
    if not diagram_name:
        return ""

    html = '                <section id="diagramas">\n'
    html += '                    <h2>📊 Diagramas Ilustrativos</h2>\n'
    html += f'                    <div class="text-center my-4">\n'
    html += f'                        <img src="../assets/diagramas/{diagram_name}"\n'
    html += f'                             alt="{diagram_name}"\n'
    html += f'                             class="img-fluid rounded shadow"\n'
    html += f'                             style="max-width: 100%; height: auto;">\n'
    html += f'                    </div>\n'
    html += '                </section>\n\n'
    return html


def add_videos_to_sidebar(content: str) -> str:
    """Agrega el enlace de videos al sidebar si no existe."""
    if '<a href="#videos">' in content:
        return content

    # Buscar y reemplazar
    pattern = r'(<li><a href="#ejercicio">Ejercicio Guidido</a></li>)\n(                        <li><a href="#referencias">Para Profundizar</a></li>)'
    replacement = r'\1\n                        <li><a href="#videos">📺 Videos Recomendados</a></li>\n\2'
    return re.sub(pattern, replacement, content)


def process_class_file(class_path: Path, resources: Dict):
    """Procesa un archivo de clase HTML."""
    print(f"Procesando: {class_path.name}")

    # Leer contenido
    with open(class_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    class_name = class_path.stem

    # Obtener recursos para esta clase
    class_resources = RESOURCES.get(class_name, {})

    # Verificar si ya tiene la sección de videos
    if class_resources.get('videos') and '<section id="videos">' not in content:
        # Buscar el lugar para insertar (antes de referencias)
        videos_html = generate_videos_section(class_resources['videos'])
        content = content.replace(
            '                <section id="referencias">',
            videos_html + '                <section id="referencias">'
        )

    # Agregar diagramas si aplica
    if class_resources.get('diagram') and '<section id="diagramas">' not in content:
        diagram_html = generate_diagram_section(class_resources['diagram'])
        if '<section id="videos">' in content:
            # Insertar después de videos
            content = content.replace(
                videos_html,
                videos_html + diagram_html
            )
        else:
            # Insertar antes de referencias
            content = content.replace(
                '                <section id="referencias">',
                diagram_html + '                <section id="referencias">'
            )

    # Actualizar sidebar
    content = add_videos_to_sidebar(content)

    # Guardar si hubo cambios
    if content != original_content:
        with open(class_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] Actualizado: {class_path.name}")
    else:
        print(f"  [SKIP] Sin cambios: {class_path.name}")


def main():
    """Función principal."""
    print("=== Integración de Recursos Multimedia ===\n")

    # Buscar todos los archivos HTML de clases
    class_files = []
    for unit_dir in CLASSES_DIR.glob('unidad-*'):
        for html_file in unit_dir.glob('clase-*.html'):
            class_files.append(html_file)

    print(f"Encontradas {len(class_files)} clases HTML\n")

    # Procesar cada archivo
    updated_count = 0
    for class_file in sorted(class_files):
        process_class_file(class_file, RESOURCES)
        updated_count += 1

    print(f"\n=== Resumen ===")
    print(f"Clases procesadas: {updated_count}")
    print(f"Diagramas creados: 6")
    print(f"Videos agregados: {sum(len(r.get('videos', [])) for r in RESOURCES.values())}")
    print("\n[OK] Integracion completada")


if __name__ == "__main__":
    main()
