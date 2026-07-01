# DISCOVERY - organvm/radix-recursiva-solve-coagula-redi

**Verdict:** VALUE FOUND - promote into the ranked tier.
**Date:** 2026-07-01 (auto-discovery)

## Value Thesis

`radix-recursiva-solve-coagula-redi` is not merely an archival theory vault: its highest latent value is a reusable zero-dependency experiment-containment and knowledge-governance substrate for the rest of ORGANVM. The repo already ships an installable Python package, `experimental-habitat`, with real console entry points (`habitat-manager`, `habitat-interactive`, `habitat-demo`, `habitat-workflow`), an importable lifecycle API (`ExperimentalHabitat`, `ExperimentalSystem`, `ContainmentBoundary`, `RecursiveMythEngine`, `HabitatManager`), path-traversal hardening around experiment workspaces, and tests covering spawn, run, nested habitat creation, graduation, composting, CLI manager behavior, and terminal sanitization. Its reusable asset is the "habitat" pattern: a standard-library sandbox contract for taking risky ideas from hypothesis to contained execution to either promoted pattern or composted lesson, which Limen and the wider estate can use as the local/free floor for experimental work, prompt-agent trials, code-pattern incubation, and audit-friendly failure learning. The honest revenue path is indirect but concrete: package the habitat as the estate's trusted experiment ledger and containment CLI, then use it inside higher-value repos to reduce failed-build waste and create receipts for paid automation work. This is build-out-worthy infrastructure, not a finished product and not an archive.

## Single Best Concrete First Task

Add a persisted experiment ledger: every `spawn`, `run`, `graduate`, and `compost` operation should append a JSONL event under a configurable habitat state directory, and `habitat-manager` should gain `ledger` / `export` commands that print or write the lifecycle history for a habitat. Keep it standard-library-only, add focused tests around the event schema and CLI output, and wire the test command into the documented verification path.
