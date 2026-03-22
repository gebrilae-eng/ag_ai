import os
from pathlib import Path

www = Path('C:/laragon/www')
projects = []
if www.exists():
    for d in sorted(www.iterdir()):
        if d.is_dir() and not d.name.startswith('.'):
            projects.append(d)

print('=== Projects in C:\\laragon\\www ===\n')
for proj in projects:
    oc = proj / '.opencode' / 'agents'
    yml = list(oc.glob('*.yml')) if oc.exists() else []
    md  = list(oc.glob('*.md'))  if oc.exists() else []
    agents_md = (proj / 'AGENTS.md').exists()
    has_ai = (proj / '.ai').exists()
    total = len(yml) + len(md)
    status = 'installed' if total > 0 else 'NOT installed'
    print(f'  {proj.name}')
    print(f'    agents: {len(yml)} yml + {len(md)} md = {total} ({status})')
    print(f'    AGENTS.md: {"YES" if agents_md else "NO"}  |  .ai/: {"YES" if has_ai else "NO"}')
    print()
