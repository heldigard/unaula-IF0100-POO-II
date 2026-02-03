#!/usr/bin/env python3
"""
Apply syntax highlighting to HTML code blocks without tokens.
Adds <span class="token-xxx"> tags to Python code in <pre><code class="language-python"> blocks.
"""

import re
import html
from pathlib import Path

# Python keywords
KEYWORDS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
    'try', 'while', 'with', 'yield', 'match', 'case', 'super', 'self'
}

TYPES = {
    'int', 'float', 'str', 'bool', 'list', 'dict', 'tuple', 'set',
    'bytes', 'bytearray', 'type', 'object', 'Any', 'List', 'Dict',
    'Tuple', 'Set', 'Optional', 'Union', 'Callable', 'Iterable',
    'Iterator', 'Sequence', 'Mapping'
}

BUILTINS = {
    'print', 'len', 'range', 'str', 'int', 'float', 'list', 'dict',
    'tuple', 'set', 'bool', 'input', 'open', 'abs', 'min', 'max',
    'sum', 'sorted', 'enumerate', 'zip', 'map', 'filter', 'all',
    'any', 'isinstance', 'issubclass', 'hasattr', 'getattr',
    'setattr', 'delattr', 'property', 'staticmethod', 'classmethod',
    'Exception', 'ValueError', 'TypeError', 'IndexError', 'KeyError',
    'abstractmethod', 'dataclass', 'field'
}

def escape_html(text: str) -> str:
    """Escape HTML entities."""
    return html.escape(text)

def highlight_python(code: str) -> str:
    """Apply syntax highlighting to Python code."""
    # First, escape HTML
    code = escape_html(code)

    # Split into lines for processing
    lines = code.split('\n')
    result_lines = []

    for line in lines:
        # Skip comment lines (but process inline comments)
        stripped = line.strip()

        # Process the line
        processed = line

        # Strings (simple and double quotes) - handle them first
        # Triple-quoted strings
        processed = re.sub(
            r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')',
            r'<span class="token-string">\1</span>',
            processed
        )

        # Single/double quoted strings
        processed = re.sub(
            r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')',
            r'<span class="token-string">\1</span>',
            processed
        )

        # Comments (lines starting with #, but not inside strings)
        # Find # that's not inside a span
        def replace_comment(match):
            content = match.group(1)
            return f'<span class="token-comment">#{content}</span>'

        # Match # followed by comment content to end of line
        # But only if not already inside a span (string)
        if '<span' not in processed:
            # Simple comment - no spans yet
            processed = re.sub(r'#(.*)$', replace_comment, processed, count=1)
        else:
            # Need to handle comments after strings
            parts = processed.split('#', 1)
            if len(parts) > 1 and not parts[0].rstrip().endswith("'''") and not parts[0].rstrip().endswith('"""'):
                processed = parts[0] + '<span class="token-comment">#' + parts[1] + '</span>'

        # Keywords - use word boundaries
        for kw in sorted(KEYWORDS, key=len, reverse=True):
            pattern = r'\b(' + re.escape(kw) + r')\b'
            processed = re.sub(pattern, r'<span class="token-keyword">\1</span>', processed)

        # Types
        for tp in sorted(TYPES, key=len, reverse=True):
            pattern = r'\b(' + re.escape(tp) + r')\b'
            processed = re.sub(pattern, r'<span class="token-type">\1</span>', processed)

        # Builtins/methods
        for bi in sorted(BUILTINS, key=len, reverse=True):
            pattern = r'\b(' + re.escape(bi) + r')\b'
            processed = re.sub(pattern, r'<span class="token-method">\1</span>', processed)

        # Numbers
        processed = re.sub(
            r'\b(\d+\.?\d*|\d*\.?\d+)\b',
            r'<span class="token-number">\1</span>',
            processed
        )

        # Operators
        processed = re.sub(
            r'([=+\-*/%&|^<>!~:@]+)',
            r'<span class="token-operator">\1</span>',
            processed
        )

        # Decorator symbols (@)
        processed = re.sub(
            r'(@)(\w+)',
            r'<span class="token-operator">\1</span><span class="token-method">\2</span>',
            processed
        )

        result_lines.append(processed)

    return '\n'.join(result_lines)

def process_file(filepath: Path) -> int:
    """Process an HTML file and add syntax highlighting to code blocks."""
    content = filepath.read_text(encoding='utf-8')
    original = content

    # Find all <pre><code class="language-python"> blocks
    pattern = r'(<pre><code class="language-python">)(.*?)(</code></pre>)'

    def replace_block(match):
        opening = match.group(1)
        code_content = match.group(2)
        closing = match.group(3)

        # Check if already has tokens (has <span class="token-)
        if '<span class="token-' in code_content:
            return match.group(0)  # Skip, already highlighted

        # Decode HTML entities first
        from html import unescape
        decoded = unescape(code_content)

        # Apply highlighting
        highlighted = highlight_python(decoded)

        return opening + highlighted + closing

    content = re.sub(pattern, replace_block, content, flags=re.DOTALL)

    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return 1

    return 0

def main():
    """Process all class files that need syntax highlighting."""
    import sys
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    classes_dir = Path(r'F:\UNAULA\IF0100-POO-II\clases-html')
    files_to_fix = ['clase-01.html', 'clase-14.html', 'clase-15.html', 'clase-16.html', 'clase-17.html']

    for filename in files_to_fix:
        filepath = classes_dir / filename
        if filepath.exists():
            print(f"Processing {filename}...")
            changed = process_file(filepath)
            if changed:
                print(f"  [OK] Updated {filename}")
            else:
                print(f"  [INFO] No changes needed for {filename}")
        else:
            print(f"  [ERROR] File not found: {filename}")

if __name__ == '__main__':
    main()
