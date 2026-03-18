# Changelog

---

## [2.3.0] - 2025-03

### Changed (restructure — no behavior changes)

**Flat .ai/ structure:**
- `.ai/agents/ecc/` + `.ai/sub-agents/` merged into `.ai/agents/` (one folder, 18 files)
- `.ai/rules/common/security.md` + `.ai/rules/common/coding-style.md` → `.ai/rules/common.md`
- `.ai/rules/php/security.md` + `.ai/rules/php/patterns.md` + `.ai/rules/php/testing.md` → `.ai/rules/php.md`
- `.ai/spec/commands/` (6 files) → `.ai/spec/commands.md` (one file)

**Scripts:**
- `agent.bat` regrouped into Planning / Development / Review / Specialists
- `agent.ps1` rewritten with ordered hashtable, same grouping
- `setup_ai.py` updated to reflect flat structure (removed ecc/sub-agents/rules-php/rules-common paths)
- `make_dirs()` updated — no longer creates obsolete sub-folders

**Docs:**
- `orchestrator.md` updated — removed old ecc/sub-agents path references
- `spec-workflow.md` updated — references `commands.md` not `commands/`
- `CLAUDE.md` template updated — reflects new flat layout
- `README.md` updated — repo structure + project structure sections

### Removed
- `.ai/agents/ecc/` directory (contents moved to `.ai/agents/`)
- `.ai/sub-agents/` directory (contents moved to `.ai/agents/`)
- `.ai/rules/common/` directory (merged into `.ai/rules/common.md`)
- `.ai/rules/php/` directory (merged into `.ai/rules/php.md`)
- `.ai/spec/commands/` directory (merged into `.ai/spec/commands.md`)

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
- Models updated to `claude-sonnet-4-6`

---

## [2.0.0] - 2025-01
- 18 OpenCode YAML agents, wizard.py, AGENTS.md, Spec Kit, ECC agents

## [1.0.0] - 2024-11
- Initial release
