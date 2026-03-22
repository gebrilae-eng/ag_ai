"""
fix_all_tools.py
================
Fixes ALL tools formats in .opencode/agents/*.md to OpenCode-required record format.

Handles:
  1. Inline string:  tools: WebFetch, Read, Write
  2. YAML list:      tools:\n    - read\n    - write
  3. Already record: tools:\n    read: true   (skip)

Normalises tool names to lowercase.
"""
import re
from pathlib import Path

# Map common PascalCase / camelCase tool names -> opencode lowercase keys
TOOL_ALIASES = {
    'webfetch': 'webfetch', 'websearch': 'websearch',
    'read': 'read', 'write': 'write', 'edit': 'edit',
    'bash': 'bash', 'glob': 'glob', 'grep': 'grep',
    'task': 'task', 'computer': 'computer',
    'list': 'list', 'search': 'search',
}

def normalise(name: str) -> str:
    return TOOL_ALIASES.get(name.lower().strip(), name.lower().strip())

def tools_to_record(tool_names: list[str]) -> str:
    """Convert list of tool names to YAML record block."""
    lines = ['tools:']
    for t in tool_names:
        n = normalise(t)
        if n:
            lines.append(f'  {n}: true')
    return '\n'.join(lines)

def fix_frontmatter(content: str) -> tuple[str, str]:
    """
    Returns (new_content, status) where status is one of:
      'fixed_inline', 'fixed_list', 'already_record', 'no_tools', 'no_frontmatter'
    """
    fm = re.match(r'^(---\n)(.*?)(---\n)(.*)', content, re.DOTALL)
    if not fm:
        return content, 'no_frontmatter'

    open_fence  = fm.group(1)
    front       = fm.group(2)
    close_fence = fm.group(3)
    body        = fm.group(4)

    # ── Case 1: inline string  tools: WebFetch, Read, Write ──────────────────
    inline_m = re.search(r'^tools:[ \t]+([^\n]+)$', front, re.MULTILINE)
    if inline_m:
        raw    = inline_m.group(1).strip()
        names  = [t.strip() for t in raw.split(',') if t.strip()]
        record = tools_to_record(names)
        new_front = front[:inline_m.start()] + record + '\n' + front[inline_m.end()+1:]
        return open_fence + new_front + close_fence + body, 'fixed_inline'

    # ── Case 2: list block  tools:\n    - read ───────────────────────────────
    list_m = re.search(r'^tools:\n((?:[ \t]+-[ \t]+\S+\n?)+)', front, re.MULTILINE)
    if list_m:
        names  = re.findall(r'[ \t]+-[ \t]+(\S+)', list_m.group(1))
        record = tools_to_record(names)
        new_front = front[:list_m.start()] + record + '\n' + front[list_m.end():]
        return open_fence + new_front + close_fence + body, 'fixed_list'

    # ── Case 3: already record  tools:\n    read: true ──────────────────────
    record_m = re.search(r'^tools:\n(?:[ \t]+\w+:[ \t]+(?:true|false)\n?)+', front, re.MULTILINE)
    if record_m:
        return content, 'already_record'

    return content, 'no_tools'


def fix_directory(agents_dir: Path, dry_run: bool = False) -> dict:
    counts = {'fixed_inline': 0, 'fixed_list': 0,
              'already_record': 0, 'no_tools': 0,
              'no_frontmatter': 0, 'error': 0}

    for f in sorted(agents_dir.glob('*.md')):
        try:
            txt = f.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            print(f'  ERR {f.name}: {e}')
            counts['error'] += 1
            continue

        new_txt, status = fix_frontmatter(txt)
        counts[status] += 1

        if new_txt != txt and not dry_run:
            f.write_text(new_txt, encoding='utf-8')

    return counts


if __name__ == '__main__':
    import sys
    dry = '--dry-run' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]

    projects = args if args else [
        r'C:\ag_ai',
        r'C:\laragon\www\pharmacy-system',
        r'C:\laragon\www\mcp-server',
        r'C:\laragon\www\pharmacy_10min_2026-02-28_09-45-42',
        r'C:\laragon\www\test-project',
    ]

    if dry:
        print('DRY RUN — no files written\n')

    for proj in projects:
        agents_dir = Path(proj) / '.opencode' / 'agents'
        if not agents_dir.exists():
            print(f'  SKIP {proj}')
            continue
        c = fix_directory(agents_dir, dry_run=dry)
        total_fixed = c['fixed_inline'] + c['fixed_list']
        print(
            f"  {Path(proj).name:45s} "
            f"fixed={total_fixed:3d} "
            f"(inline={c['fixed_inline']} list={c['fixed_list']}) "
            f"ok={c['already_record']:3d}  no_tools={c['no_tools']}"
        )
