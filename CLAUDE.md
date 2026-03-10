# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

4_S0VRC3 (read: "A Source") is a hybrid creative/technical system combining an Obsidian knowledge vault with Python automation. It implements RE:GE:OS (Recursive Generative Operating System) - a symbolic operating system using consonant-only UIDs, mythic archetypes, and experimental containment.

**Zero external dependencies** for core functionality - uses only Python standard library.

## Commands

### Setup
```bash
pip install -e .                    # Install package
pip install -e ".[dev]"             # Install with dev dependencies (pytest, black, flake8)
```

### Testing
```bash
pytest tests/                       # Run all tests
pytest tests/test_habitat_system.py # Run specific test file
python -m pytest -v                 # Verbose output
```

### Entry Points (after install)
```bash
habitat-manager      # Experimental Habitat containment system
habitat-interactive  # Interactive habitat interface
habitat-demo         # Simple demonstration
habitat-workflow     # Complete workflow demo
```

### Vault Utilities
```bash
python scripts/vault_utils/generate_uid.py     # Generate symbolic UIDs
python scripts/vault_utils/uid_indexer.py      # Generate master UID index
python scripts/vault_utils/uid_check.py        # Validate UID compliance
python scripts/vault_utils/initialize_vault.py # Bootstrap folder structure
python scripts/vault_utils/vault_freeze.py     # Create archival snapshots
python scripts/vault_utils/sort_router.py      # Route files to domain folders
```

### Validation
```bash
python scripts/validate_containment.py  # Check containment policy compliance
python scripts/metadata_guard.py        # Validate YAML frontmatter
python scripts/check_env_vars.py        # Verify environment variables
```

## Architecture

### Folder Structure

The vault uses a simplified naming convention with 4-letter suffix codes:

| Folder | Purpose |
|--------|---------|
| `src/habitat/` | Python package for Experimental Habitat System |
| `REGEOS_RG01/` | Core RE:GE:OS logic, symbolic laws, 22 organizational bodies |
| `ARCHIVE_RK01/` | Long-term archival storage (gitignored), distributions |
| `MIRROR_MR01/` | Shadow self, reflection systems |
| `TEMPLATES_TP01/` | Seed files, note templates |
| `TAGS_TA01/` | Tag and symbol management |
| `SYSTEM_MAP_SM01/` | System architecture maps, experiments |
| `ARCHIVAL_STACK/` | Project thread digests |
| `DOCUMENTATION/` | Vault guides, SOPs, policies, standards, reference docs |
| `PROJECT_MANAGEMENT/` | Manifests, changelogs, meta-operations, reports |
| `CATALOGS_AND_INDEXES/` | Master indexes, observation logs, UIDs |
| `Users/` | User-specific content |
| `GATEWAY_GT01/` | External ingestion points |
| `ANOMALIES_FL01/` | Anomaly tracking |
| `FRAGMENTS_FR01/` | Fragment and memory collection |
| `NARRATIVES_NR01/` | Narrative content |
| `GAMEDESIGN_GD01/` | Game design materials |
| `WORKSHOPS_WR01/` | Workshop content |
| `scripts/` | Python automation (CLI entry points, utils, analysis) |
| `tests/` | Test suite (pytest integration) |
| `security/` | Recovery keys (sensitive, isolated) |

### Experimental Habitat System

Safe, isolated containment for experimental code with resource limits:

```python
from habitat import ExperimentalHabitat, ExperimentalSystem

habitat = ExperimentalHabitat("lab_name", isolation_level=3)
experiment = ExperimentalSystem("test_name", "hypothesis")
habitat.spawn_experiment(experiment, {'resources': {'cpu': '50%'}})
result = habitat.run_experiment("test_name")
habitat.cleanup()
```

**Lifecycle:** Spawn → Run → Graduate (to production) or Compost (extract lessons)

### Key Files

- `src/habitat/experimental_habitat_implementation.py` - Core containment system
- `src/habitat/habitat_manager.py` - CLI management interface
- `DOCUMENTATION/sops/SOP_SYSTEM_OVERVIEW.md` - Complete operations manual
- `CATALOGS_AND_INDEXES/uids/UIDS_MASTER_INDEX.md` - Master UID lookup
- `DOCUMENTATION/guides/GLOSSARY.md` - Symbolic terminology

## Working with Special Characters

Some older symbolic folder names may contain special characters. Always use quotes:

```bash
ls -la "MIRROR_MR01/"
cat "path/with spaces/file.md"
```

## GitHub Workflows

Active CI/CD in `.github/workflows/`:
- `ai-review.yml` - AI-assisted PR reviews
- `jules-branch-guard.yml` - Branch lifecycle (bolt-*/sentinel-*/palette-* prefixes)
- `codeql.yml` / `semgrep.yml` - Security analysis
- `documentation-quality.yml` - Doc validation

## AI Handoff Protocol

AI-generated documents use envelope notation:
```
<<<AI-Handoff:BEGIN::Agent={Name}::Timestamp={ISO-8601}>>>
...content...
<<<AI-Handoff:END>>>
```

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-I (Theory) | **Tier:** standard | **Status:** PUBLIC_PROCESS
**Org:** `organvm-i-theoria` | **Repo:** `radix-recursiva-solve-coagula-redi`

### Edges
- *No inter-repo edges declared in seed.yaml*

### Siblings in Theory
`recursive-engine--generative-entity`, `organon-noumenon--ontogenetic-morphe`, `auto-revision-epistemic-engine`, `narratological-algorithmic-lenses`, `call-function--ontological`, `sema-metra--alchemica-mundi`, `system-governance-framework`, `cognitive-archaelogy-tribunal`, `a-recursive-root`, `.github`, `nexus--babel-alexandria-`, `reverse-engine-recursive-run`, `4-ivi374-F0Rivi4`, `cog-init-1-0-`, `collective-persona-operations` ... and 4 more

### Governance
- Foundational theory layer. No upstream dependencies.

*Last synced: 2026-03-08T20:11:34Z*

## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`
4. Run `organvm prompts distill --dry-run` to detect uncovered operational patterns

Transcripts are on-demand (never committed):
- `organvm session transcript <id>` — conversation summary
- `organvm session transcript <id> --unabridged` — full audit trail
- `organvm session prompts <id>` — human prompts only


## Active Directives

| Scope | Phase | Name | Description |
|-------|-------|------|-------------|
| system | any | prompting-standards | Prompting Standards |
| system | any | research-standards-bibliography | APPENDIX: Research Standards Bibliography |
| system | any | research-standards | METADOC: Architectural Typology & Research Standards |
| system | any | sop-ecosystem | METADOC: SOP Ecosystem — Taxonomy, Inventory & Coverage |
| system | any | autopoietic-systems-diagnostics | SOP: Autopoietic Systems Diagnostics (The Mirror of Eternity) |
| system | any | cicd-resilience-and-recovery | SOP: CI/CD Pipeline Resilience & Recovery |
| system | any | cross-agent-handoff | SOP: Cross-Agent Session Handoff |
| system | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction |
| system | any | essay-publishing-and-distribution | SOP: Essay Publishing & Distribution |
| system | any | market-gap-analysis | SOP: Full-Breath Market-Gap Analysis & Defensive Parrying |
| system | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |
| system | any | promotion-and-state-transitions | SOP: Promotion & State Transitions |
| system | any | repo-onboarding-and-habitat-creation | SOP: Repo Onboarding & Habitat Creation |
| system | any | research-to-implementation-pipeline | SOP: Research-to-Implementation Pipeline (The Gold Path) |
| system | any | security-and-accessibility-audit | SOP: Security & Accessibility Audit |
| system | any | session-self-critique | session-self-critique |
| system | any | source-evaluation-and-bibliography | SOP: Source Evaluation & Annotated Bibliography (The Refinery) |
| system | any | stranger-test-protocol | SOP: Stranger Test Protocol |
| system | any | strategic-foresight-and-futures | SOP: Strategic Foresight & Futures (The Telescope) |
| system | any | typological-hermeneutic-analysis | SOP: Typological & Hermeneutic Analysis (The Archaeology) |
| unknown | any | gpt-to-os | SOP_GPT_TO_OS.md |
| unknown | any | index | SOP_INDEX.md |
| unknown | any | obsidian-sync | SOP_OBSIDIAN_SYNC.md |

Linked skills: evaluation-to-growth


**Prompting (Anthropic)**: context 200K tokens, format: XML tags, thinking: extended thinking (budget_tokens)

<!-- ORGANVM:AUTO:END -->


## ⚡ Conductor OS Integration
This repository is a managed component of the ORGANVM meta-workspace.
- **Orchestration:** Use `conductor patch` for system status and work queue.
- **Lifecycle:** Follow the `FRAME -> SHAPE -> BUILD -> PROVE` workflow.
- **Governance:** Promotions are managed via `conductor wip promote`.
- **Intelligence:** Conductor MCP tools are available for routing and mission synthesis.
