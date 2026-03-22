import re
from pathlib import Path

COLOR_MAP = {
    'red': '#ef4444', 'blue': '#3b82f6', 'green': '#22c55e',
    'purple': '#a855f7', 'orange': '#f97316', 'teal': '#14b8a6',
    'cyan': '#06b6d4', 'pink': '#ec4899', 'yellow': '#eab308',
    'amber': '#f59e0b', 'indigo': '#6366f1', 'gold': '#f59e0b',
    'metallic-blue': '#4a7fa5', 'neon-cyan': '#00ffff',
    'neon-green': '#39ff14',
}

VALID_HEX  = re.compile(r'^#[0-9a-fA-F]{3,6}$')
COLOR_LINE = re.compile(r'^(color:\s*)(.+)$', re.MULTILINE)

def fix_agent_colors(agents_dir: Path) -> int:
    fixed = 0
    for f in agents_dir.glob('*.md'):
        try:
            txt = f.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
        if 'color:' not in txt:
            continue

        def replacer(m):
            prefix = m.group(1)
            raw = m.group(2).strip().strip('"').strip("'")
            if VALID_HEX.match(raw):
                return f'{prefix}"{raw}"'
            mapped = COLOR_MAP.get(raw.lower(), '#6366f1')
            return f'{prefix}"{mapped}"'

        new_txt = COLOR_LINE.sub(replacer, txt)
        if new_txt != txt:
            f.write_text(new_txt, encoding='utf-8')
            fixed += 1
    return fixed

if __name__ == '__main__':
    import sys
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    agents_dir = target / '.opencode' / 'agents'
    if not agents_dir.exists():
        print(f'No agents dir: {agents_dir}')
        sys.exit(1)
    n = fix_agent_colors(agents_dir)
    print(f'Fixed {n} files in {agents_dir}')
