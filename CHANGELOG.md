# Changelog

---

## [2.6.0] - 2026-03

### Added
- `prd.py` — auto-generates `PRD.md` from wizard answers (product overview,
  tech stack, business rules, agent routing, reading chain, file map)
- `prd-template.md` — manual PRD template in `.ai/spec/templates/`
- `prd` command in `run.bat` menu (option 5) and direct mode
- PRD.md optional check in `validate.py`
- Standardized reading chain: `PRD.md → AGENTS.md → STACK.md → RULES.md`

### Changed
- `wizard.py` — now auto-calls `prd.py` after context file generation
- `CLAUDE.md` — reading chain at top, PRD.md in file map
- `run.bat` — bumped to v2.6, renumbered menu (1-8)
- `README.md` — added `prd.py` to scripts table, updated menu
- 4 key agent YAMLs (`orchestrator`, `coder`, `architect`, `spec-workflow`)
  now read PRD.md first in their instructions

### Fixed
- 8 YAML agents had stale `ecc/` path references → fixed to `.ai/agents/`
- 3 agent MDs had stale `sub-agents/` references → fixed to `.ai/agents/`
- `wizard.py` was creating obsolete `.ai/sub-agents/` directory → removed
- `run.bat` referenced non-existent `scripts/update.bat` and
  `scripts/new-project.bat` → replaced with inline commands

---

## [2.4.0] - 2025-03

### Added
- `run.bat` — single entry-point menu: new-project / install / wizard /
  validate / update / update-project / agent. All scripts now accessible
  from one command.

### Changed
- `validate.py` — added flat structure checks (warns if old ecc/sub-agents
  dirs still present, verifies common.md + php.md + commands.md exist)
- `validate.py` — added recommended structure section in output
- `agent.bat` / `agent.ps1` — regrouped into Planning / Development /
  Review / Specialists for clarity

### Removed
- `GUIDE.md` — content was already in README.md since v2.1

---

## [2.3.0] - 2025-03

### Changed (flat structure — no behavior changes)
- `.ai/agents/ecc/` + `.ai/sub-agents/` merged into `.ai/agents/`
- `rules/common/` (2 files) → `rules/common.md`
- `rules/php/` (3 files) → `rules/php.md`
- `spec/commands/` (6 files) → `spec/commands.md`
- `setup_ai.py` updated for new paths
- `orchestrator.md` + `spec-workflow.md` references updated

---

## [2.2.0] - 2025-03
### Added
- `.config/opencode/opencode.json` — global OpenCode config, all 18 agents as primary

---

## [2.1.0] - 2025-03
### Added
- `validate.py` / `validate.bat`, `update-project.bat`
- `--dry-run` and `--update-agents` flags in `setup_ai.py`
- Confirmation summary + overwrite-all prompt in `wizard.py`
### Changed
- All 18 agents → `mode: primary`, orchestrator delegates only
- `install.bat` — removed `git reset --hard`

---

## [2.0.0] - 2025-01
- 18 OpenCode YAML agents, wizard.py, AGENTS.md, Spec Kit, ECC agents

## [1.0.0] - 2024-11
- Initial release
