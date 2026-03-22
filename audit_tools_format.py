"""
audit_tools_format.py - scans all agents and reports every tools: format found
"""
import re
from pathlib import Path

agents_dir = Path('C:/laragon/www/pharmacy-system/.opencode/agents')
fmt = {'record': [], 'list': [], 'inline_string': [], 'missing': []}

for f in sorted(agents_dir.glob('*.md')):
    txt = f.read_text(encoding='utf-8', errors='ignore')
    fm = re.match(r'^---\n(.*?)---\n', txt, re.DOTALL)
    if not fm:
        fmt['missing'].append(f.name); continue
    front = fm.group(1)

    # Find tools: line
    m = re.search(r'^(tools:.*)$', front, re.MULTILINE)
    if not m:
        fmt['missing'].append(f.name); continue

    line = m.group(1)
    inline = line[len('tools:'):].strip()

    if inline:
        # tools: WebFetch, Read  OR  tools: read
        fmt['inline_string'].append((f.name, inline))
    else:
        # Multi-line — check next indented lines
        after = front[m.end():]
        sub = re.match(r'((?:  .+\n?)+)', after)
        if not sub:
            fmt['missing'].append(f.name); continue
        first = sub.group(1).splitlines()[0].strip()
        if first.startswith('- '):
            fmt['list'].append(f.name)
        elif ': true' in first or ': false' in first:
            fmt['record'].append(f.name)
        else:
            fmt['missing'].append(f.name)

print(f"record        : {len(fmt['record'])}")
print(f"list          : {len(fmt['list'])}")
print(f"inline_string : {len(fmt['inline_string'])}")
print(f"missing/other : {len(fmt['missing'])}")
print()
if fmt['inline_string']:
    print("=== inline_string samples ===")
    for name, val in fmt['inline_string'][:10]:
        print(f"  {name}: tools: {val}")
if fmt['list']:
    print(f"\n=== list samples ===")
    for name in fmt['list'][:5]:
        print(f"  {name}")
