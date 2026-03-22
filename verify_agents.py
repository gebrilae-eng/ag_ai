from pathlib import Path
import os

os.chdir('C:/ag_ai')
agents = list(Path('.opencode/agents').glob('*.md'))
ok = broken = 0
for f in sorted(agents):
    txt = f.read_text(encoding='utf-8')
    parts = txt.split('---')
    has_front = txt.startswith('---') and len(parts) >= 3
    front     = parts[1] if len(parts) >= 3 else ''
    has_name  = 'name:' in front
    has_tools = 'tools:' in front
    has_body  = parts[2].strip() != '' if len(parts) >= 3 else False
    broken_ref = '.ai/sub-agents/' in txt
    if has_front and has_name and has_tools and has_body and not broken_ref:
        ok += 1
    else:
        broken += 1
        print(f'  BROKEN: {f.name}')

print(f'\nAgents .md : {ok} OK / {broken} broken')
print(f'YML remaining : {len(list(Path(".opencode/agents").glob("*.yml")))}')
print(f'opencode.json : {Path("opencode.json").exists()}')
print(f'.git/COMMIT_EDITMSG_MANUAL cleanup...')
tmp = Path('.git/COMMIT_EDITMSG_MANUAL')
if tmp.exists(): tmp.unlink(); print('  cleaned')
