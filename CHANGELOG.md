# Changelog

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
