# Changelog

---

## [3.0.0] - 2026-03

### Changed (breaking -- wizard.py rewritten)
- `wizard.py` rewritten as a standalone all-in-one generator.
  One file, one command, zero external dependencies.
  Replaces `wizard.py` + `prd.py` + separate generator scripts.

### Added
- **Hooks generator** (inside wizard.py) -- generates `.claude/settings.json`
  with stack-aware hooks: PHP, Python, Node.js, MySQL/PostgreSQL, n8n, Telegram.
  Hooks auto-trigger on Edit/Write/Bash without any manual configuration.
- **Skills generator** (inside wizard.py) -- generates SKILL.md files matched
  to the project stack. Claude Code reads these automatically.
  Included skills: security-core, git-workflow, tdd-workflow, sql-patterns,
  n8n-patterns, telegram-bot, api-design (selected based on stack).
- **Security audit generator** (inside wizard.py) -- generates
  `.claude/security/security-audit.js` with checks for the detected stack.
  Run: `node ~/.claude/security/security-audit.js [project-path]`
- **6 slash commands** installed globally and per-project:
  `/learn`, `/instinct-status`, `/evolve`, `/checkpoint`, `/verify`, `/security`
- **session-observer.js** -- async background hook that silently logs patterns
  to `~/.claude/sessions/observations.jsonl` for `/learn` to process.
- **Continuous Learning loop**:
  Session -> `/learn` -> `/instinct-status` -> `/evolve` -> new SKILL.md
- **Cross-platform**: generates `.cursor/rules/` and `.codex/AGENTS.md`
  alongside standard Claude Code / OpenCode output.

### Fixed
- `prd.py` functionality merged into `wizard.py` -- no separate script needed.
- `wizard.py` no longer requires `subprocess` call to `prd.py`.

---

## [2.6.0] - 2026-03

### Added
- `prd.py` -- auto-generates PRD.md from wizard-answers.json
- `prd-template.md` in `.ai/spec/templates/`
- `prd` command in `run.bat` menu (option 5)
- PRD.md optional check in `validate.py`
- Standardized reading chain: PRD.md -> AGENTS.md -> STACK.md -> RULES.md

### Changed
- `wizard.py` -- now auto-calls `prd.py` after context file generation
- `CLAUDE.md` -- reading chain at top, PRD.md in file map
- `run.bat` -- bumped to v2.6, renumbered menu (1-8)
- 4 key agent YAMLs now read PRD.md first in their instructions

### Fixed
- 8 YAML agents had stale `ecc/` path references -> fixed to `.ai/agents/`
- 3 agent MDs had stale `sub-agents/` references -> fixed to `.ai/agents/`
- `wizard.py` was creating obsolete `.ai/sub-agents/` directory -> removed

---

## [2.4.0] - 2025-03

### Added
- `run.bat` -- single entry-point menu for all operations

### Changed
- `validate.py` -- flat structure checks, recommended structure section
- `agent.bat` -- regrouped into Planning / Development / Review / Specialists

### Removed
- `GUIDE.md` -- content moved to README.md in v2.1

---

## [2.3.0] - 2025-03

### Changed (flat structure)
- `.ai/agents/ecc/` + `.ai/sub-agents/` merged into `.ai/agents/`
- `rules/common/` -> `rules/common.md`
- `rules/php/` -> `rules/php.md`
- `spec/commands/` -> `spec/commands.md`

---

## [2.2.0] - 2025-03
### Added
- `.config/opencode/opencode.json` -- global OpenCode config, 18 agents as primary

---

## [2.1.0] - 2025-03
### Added
- `validate.py`, `--dry-run`, `--update-agents` flags in `setup_ai.py`
### Changed
- All 18 agents -> `mode: primary`, orchestrator delegates only

---

## [2.0.0] - 2025-01
- 18 OpenCode YAML agents, wizard.py, AGENTS.md, Spec Kit

## [1.0.0] - 2024-11
- Initial release
