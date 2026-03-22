"""
fix_tools_format.py
Converts YAML list tools to record format in .opencode/agents/*.md frontmatter.

Before:
  tools:
    - read
    - write

After:
  tools:
    read: true
    write: true
"""
import re
from pathlib import Path

def fix_tools_in_frontmatter(content: str) -> str:
    # Match frontmatter block
    fm_match = re.match(r'^(---\n)(.*?)(---\n)', content, re.DOTALL)
    if not fm_match:
        return content

    pre   = fm_match.group(1)
    front = fm_match.group(2)
    post  = fm_match.group(3)
    body  = content[fm_match.end():]

    # Find tools: block with list items
    tools_match = re.search(r'^tools:\n((?:  - \S+\n?)+)', front, re.MULTILINE)
    if not tools_match:
        return content

    # Parse list items
    items = re.findall(r'  - (\S+)', tools_match.group(1))
    if not items:
        return content

    # Build record format
    record_lines = 'tools:\n' + ''.join(f'  {item}: true\n' for item in items)

    # Replace in frontmatter
    new_front = front[:tools_match.start()] + record_lines + front[tools_match.end():]
    return pre + new_front + post + body


def fix_directory(agents_dir: Path) -> tuple[int, int]:
    fixed = skipped = 0
    for f in sorted(agents_dir.glob('*.md')):
        try:
            txt = f.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            print(f'  SKIP {f.name}: {e}')
            skipped += 1
            continue

        new_txt = fix_tools_in_frontmatter(txt)
        if new_txt != txt:
            f.write_text(new_txt, encoding='utf-8')
            fixed += 1

    return fixed, skipped


if __name__ == '__main__':
    import sys
    projects = sys.argv[1:] if len(sys.argv) > 1 else []

    if not projects:
        # Default: all known projects
        projects = [
            r'C:\ag_ai',
            r'C:\laragon\www\pharmacy-system',
            r'C:\laragon\www\mcp-server',
            r'C:\laragon\www\pharmacy_10min_2026-02-28_09-45-42',
            r'C:\laragon\www\test-project',
        ]

    for proj in projects:
        agents_dir = Path(proj) / '.opencode' / 'agents'
        if not agents_dir.exists():
            print(f'  SKIP (no agents dir): {proj}')
            continue
        fixed, skipped = fix_directory(agents_dir)
        print(f'  {Path(proj).name:45s} fixed={fixed}  skipped={skipped}')
