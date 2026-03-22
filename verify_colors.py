import re
from pathlib import Path

VALID = re.compile(r'^\"#[0-9a-fA-F]{3,6}\"$')
COLOR_LINE = re.compile(r'^color:\s*(.+)$', re.MULTILINE)

agents_dir = Path('C:/laragon/www/pharmacy-system/.opencode/agents')
bad = []
total_with_color = 0

for f in sorted(agents_dir.glob('*.md')):
    txt = f.read_text(encoding='utf-8', errors='ignore')
    for m in COLOR_LINE.finditer(txt):
        total_with_color += 1
        val = m.group(1).strip()
        if not VALID.match(val):
            bad.append((f.name, val))

if bad:
    print(f'Still invalid: {len(bad)}')
    for n, v in bad:
        print(f'  {n}: {v}')
else:
    print(f'All {total_with_color} color fields are valid hex format')
