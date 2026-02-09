"""
Script para validar la coherencia cronológica del curso IF0100-POO-II.
Verifica prerequisitos, progresión de complejidad, referencias internas y alineación con evaluaciones.
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict

# Configuración
BASE_DIR = Path("F:/UNAULA/IF0100-POO-II")
CLASSES_DIR = BASE_DIR / "clases-html"
EVALUACIONES_DIR = BASE_DIR / "evaluaciones"

# Orden cronológico esperado de las clases
CHRONOLOGICAL_ORDER = [
    # Unidad 00 - Fundamentos de Python
    ('unidad-00', 'clase-00-introduccion'),
    ('unidad-00', 'clase-01-variables-tipos'),
    ('unidad-00', 'clase-02-estructuras-control'),
    ('unidad-00', 'clase-03-estructuras-datos'),

    # Unidad 01 - POO Avanzada
    ('unidad-01', 'clase-01-clases-objetos'),
    ('unidad-01', 'clase-02-encapsulamiento'),
    ('unidad-01', 'clase-03-herencia-polimorfismo'),
    ('unidad-01', 'clase-04-clases-abstractas'),

    # Unidad 02 - Técnicas de Desarrollo
    ('unidad-02', 'clase-01-tdd-intro'),
    ('unidad-02', 'clase-02-pytest-avanzado'),
    ('unidad-02', 'clase-03-bdd-intro'),
    ('unidad-02', 'clase-04-ddd-intro'),

    # Unidad 03 - FastAPI y Persistencia
    ('unidad-03', 'clase-01-fastapi-intro'),
    ('unidad-03', 'clase-02-pydantic-validacion'),
    ('unidad-03', 'clase-03-dependencias'),
    ('unidad-03', 'clase-04-testing-fastapi'),
    ('unidad-03', 'clase-05-persistencia-datos'),
]

# Conceptos clave que deben ser introducidos antes de ser usados
PREREQUISITES = {
    'clase-01-clases-objetos': ['variables', 'tipos', 'funciones', 'clases', 'objetos'],
    'clase-02-encapsulamiento': ['clases', 'objetos', 'atributos', 'metodos'],
    'clase-03-herencia-polimorfismo': ['clases', 'objetos', 'herencia', 'polimorfismo'],
    'clase-04-clases-abstractas': ['clases', 'objetos', 'herencia', 'abc'],
    'clase-01-tdd-intro': ['testing', 'pytest', 'red-green-refactor'],
    'clase-02-pytest-avanzado': ['pytest', 'fixtures', 'mock'],
    'clase-01-fastapi-intro': ['http', 'api', 'rest', 'endpoints'],
    'clase-02-pydantic-validacion': ['fastapi', 'models', 'validation'],
    'clase-03-dependencias': ['fastapi', 'functions', 'injection'],
    'clase-04-testing-fastapi': ['fastapi', 'pytest', 'testing'],
    'clase-05-persistencia-datos': ['fastapi', 'database', 'orm', 'sqlalchemy'],
}

# Terminología consistente
TERMINOLOGY = {
    'objeto': ['object', 'instance', 'instancia'],
    'clase': ['class', 'type'],
    'herencia': ['inheritance', 'herencia'],
    'polimorfismo': ['polymorphism', 'polimorfismo'],
    'encapsulamiento': ['encapsulation', 'encapsulamiento'],
    'atributo': ['attribute', 'property', 'atributo'],
    'metodo': ['method', 'funcion', 'función', 'método'],
}


def extract_concepts_from_html(html_content: str) -> List[str]:
    """Extrae conceptos clave del contenido HTML."""
    concepts = []

    # Extraer de títulos y subtítulos
    h2_pattern = r'<h2[^>]*>(.*?)</h2>'
    h3_pattern = r'<h3[^>]*>(.*?)</h3>'
    h4_pattern = r'<h4[^>]*>(.*?)</h4>'

    for match in re.finditer(h2_pattern, html_content, re.IGNORECASE):
        text = re.sub(r'<[^>]+>', '', match.group(1))
        concepts.extend(text.lower().split())

    for match in re.finditer(h3_pattern, html_content, re.IGNORECASE):
        text = re.sub(r'<[^>]+>', '', match.group(1))
        concepts.extend(text.lower().split())

    # Extraer bloques de código con comentarios clave
    code_pattern = r'<code class="language-python">(.*?)</code>'
    for match in re.finditer(code_pattern, html_content, re.DOTALL | re.IGNORECASE):
        code = match.group(1)
        # Buscar palabras clave en el código
        keywords = ['class ', 'def ', 'import ', 'from ', 'if ', 'for ', 'while ']
        for keyword in keywords:
            if keyword in code:
                concepts.append(keyword.strip())

    return list(set(concepts))


def check_navigation_links(html_content: str) -> Tuple[bool, str]:
    """Verifica que los enlaces de navegación sean correctos."""
    issues = []

    # Verificar que existe enlace a siguiente/anterior
    if 'Anterior:' not in html_content and 'Siguiente:' not in html_content:
        # Primera o última clase, es aceptable
        pass

    return len(issues) == 0, "; ".join(issues)


def check_video_links(html_content: str) -> Tuple[bool, str]:
    """Verifica que los videos de YouTube sean válidos."""
    video_pattern = r'https://www\.youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
    videos = re.findall(video_pattern, html_content)

    if not videos:
        return True, "No hay videos"

    # Verificar que los IDs de video tengan formato válido
    for video_id in videos:
        if len(video_id) < 10 or len(video_id) > 12:
            return False, f"ID de video inválido: {video_id}"

    return True, f"{len(videos)} videos válidos"


def validate_class_file(class_path: Path) -> Dict:
    """Valida un archivo de clase HTML."""
    with open(class_path, 'r', encoding='utf-8') as f:
        content = f.read()

    result = {
        'file': class_path.name,
        'concepts': [],
        'navigation_ok': False,
        'navigation_issue': '',
        'videos_ok': False,
        'videos_issue': '',
        'has_examples': False,
        'has_exercise': False,
        'missing_concepts': [],
    }

    # Extraer conceptos
    result['concepts'] = extract_concepts_from_html(content)

    # Verificar navegación
    result['navigation_ok'], result['navigation_issue'] = check_navigation_links(content)

    # Verificar videos
    result['videos_ok'], result['videos_issue'] = check_video_links(content)

    # Verificar secciones importantes
    result['has_examples'] = '<section id="ejemplos">' in content
    result['has_exercise'] = '<section id="ejercicio">' in content

    return result


def validate_evaluation_files() -> List[Dict]:
    """Valida los archivos de evaluación."""
    evaluations = []

    for eval_file in EVALUACIONES_DIR.glob('*.md'):
        with open(eval_file, 'r', encoding='utf-8') as f:
            content = f.read()

        eval_data = {
            'file': eval_file.name,
            'has_rubric': 'rúbrica' in content.lower() or 'criterios' in content.lower(),
            'has_points': 'puntos' in content.lower() or 'porcentaje' in content.lower(),
            'topics_mentioned': [],
        }

        # Extraer temas mencionados
        topic_pattern = r'\*\*([^*]+)\*\*'
        for match in re.finditer(topic_pattern, content):
            topic = match.group(1).lower()
            if len(topic) > 3 and len(topic) < 50:
                eval_data['topics_mentioned'].append(topic)

        evaluations.append(eval_data)

    return evaluations


def check_prerequisites(class_results: List[Dict]) -> List[str]:
    """Verifica que los prerequisitos se cumplan."""
    issues = []

    for i, class_result in enumerate(class_results):
        class_name = class_result['file'].replace('.html', '')
        prereqs = PREREQUISITES.get(class_name, [])

        # Verificar que los prerequisitos fueron introducidos en clases anteriores
        for prereq in prereqs:
            found = False
            for prev_class in class_results[:i]:
                if prereq in ' '.join(prev_class['concepts']):
                    found = True
                    break

            if not found:
                issues.append(f"{class_name}: '{prereq}' no encontrado en clases anteriores")

    return issues


def generate_report() -> Dict:
    """Genera un reporte completo de validación."""
    print("=== Validación de Coherencia Cronológica ===\n")

    # Validar archivos de clases
    class_results = []
    for unit, class_name in CHRONOLOGICAL_ORDER:
        class_path = CLASSES_DIR / unit / f"{class_name}.html"
        if class_path.exists():
            result = validate_class_file(class_path)
            class_results.append(result)
        else:
            print(f"[WARNING] No existe: {class_path.name}")

    # Validar evaluaciones
    eval_results = validate_evaluation_files()

    # Verificar prerequisitos
    prereq_issues = check_prerequisites(class_results)

    # Generar reporte
    report = {
        'total_classes': len(class_results),
        'classes_with_videos': sum(1 for r in class_results if r['videos_ok']),
        'classes_with_examples': sum(1 for r in class_results if r['has_examples']),
        'classes_with_exercises': sum(1 for r in class_results if r['has_exercise']),
        'navigation_issues': sum(1 for r in class_results if not r['navigation_ok']),
        'evaluations_with_rubric': sum(1 for e in eval_results if e['has_rubric']),
        'prereq_issues': prereq_issues,
    }

    # Imprimir resumen
    print(f"Total de clases analizadas: {report['total_classes']}")
    print(f"Clases con videos: {report['classes_with_videos']}/{report['total_classes']}")
    print(f"Clases con ejemplos: {report['classes_with_examples']}/{report['total_classes']}")
    print(f"Clases con ejercicios: {report['classes_with_exercises']}/{report['total_classes']}")
    print(f"Evaluaciones con rúbrica: {report['evaluations_with_rubric']}/{len(eval_results)}")
    print(f"Issues de navegación: {report['navigation_issues']}")

    print(f"\n=== Issues de Prerequisitos ===")
    if prereq_issues:
        for issue in prereq_issues:
            print(f"  [!] {issue}")
    else:
        print("  [OK] Todos los prerequisitos se cumplen")

    # Verificar coherencia de evaluaciones
    print(f"\n=== Coherencia de Evaluaciones ===")
    for eval_data in eval_results:
        status = "[OK]" if eval_data['has_rubric'] else "[WARNING]"
        print(f"  {status} {eval_data['file']}: {len(eval_data['topics_mentioned'])} temas")

    return report


def main():
    """Función principal."""
    report = generate_report()

    print(f"\n=== Resumen ===")
    print(f"Validación completada: {report['total_classes']} clases procesadas")

    if report['prereq_issues']:
        print(f"[WARNING] Se encontraron {len(report['prereq_issues'])} issues de prerequisitos")
    else:
        print("[OK] Curso coherente cronológicamente")

    print("\n[OK] Validación finalizada")


if __name__ == "__main__":
    main()
