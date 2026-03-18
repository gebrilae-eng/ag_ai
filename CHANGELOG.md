# Changelog

All notable changes to ag_ai are documented here.

---

## [2.2.0] - 2025-03

### Added
- `.config/opencode/opencode.json` — global OpenCode config with all 18 agents
  as `mode: primary` with correct tool permissions. Copy to
  `C:\Users\%USERNAME%\.config\opencode\opencode.json` to enable agents
  globally across every project without needing `.opencode/agents/` in each one.

### Changed
- `README.md` — added Global OpenCode Config section with copy instruction

---

## [2.1.0] - 2025-03

### Added
- `validate.py` / `validate.bat` — checks context files for unfilled
  placeholders and verifies all 18 agents are installed
- `update-project.bat` — updates agents only, preserves user context files
- `--dry-run` flag in `setup_ai.py` — preview all changes before applying
- `--update-agents` flag in `setup_ai.py` — agents-only update mode
- Confirmation summary step in `wizard.py` before writing any files
- Single overwrite-all prompt in `wizard.py` instead of per-file prompts
- `CHANGELOG.md` shown after `update.bat` / `update.ps1` runs

### Changed
- `install.bat` / `install.ps1` — removed git reset --hard (belongs in
  update only, never in install)
- `update.ps1` — switched Write-Host to Write-Output for pipe/redirect
- `new-project.bat` — checks if project already exists before overwriting
- `wizard.py` — overwrite protection on all generated files
- `wizard.py` — CLAUDE.md built via list join, no blank lines from conditions
- All 18 OpenCode agents upgraded to mode: primary with full tool access
- `orchestrator.yml` — delegation/management only, never writes code or
  executes tasks itself
- All former sub-agents promoted to mode: primary
- Models updated to anthropic/claude-sonnet-4-6 (architect on opus-4-6)
- Context file templates — removed FILL THIS FILE noise

### Fixed
- `setup_ai.py` — make_dirs() now respects install_ecc and install_sub
- `agent.ps1` — replaced Write-Host with Write-Output throughout
- `new-project.bat` — no longer silently overwrites existing projects

---

## [2.0.0] - 2025-01

### Added
- 18 OpenCode YAML agents in .opencode/agents/
- wizard.py interactive project setup
- AGENTS.md generation for OpenCode
- Spec Kit integration (speckit.* commands)
- ECC agents: architect, tdd-guide, security-reviewer, and more
- new-project.bat one-shot project creation
- agent.bat / agent.ps1 launcher menus

---

## [1.0.0] - 2024-11

### Added
- Initial release: orchestrator, coder, db-agent, api-agent
- Basic context files: PROJECT.md, STACK.md, RULES.md
- Claude Code slash commands
- install.bat / wizard.bat scripts
