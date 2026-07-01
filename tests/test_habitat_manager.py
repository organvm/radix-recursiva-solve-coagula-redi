#!/usr/bin/env python3
"""Focused tests for habitat_manager."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pytest

# Make the src package importable without installation.
ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from habitat import habitat_manager
from habitat.experimental_habitat_implementation import ExperimentalSystem, RecursiveMythEngine


class _NoopSpinner:
    """CLI spinner stub for deterministic, fast tests."""

    def __init__(self, *_: Any, **__: Any) -> None:
        return None

    def __enter__(self) -> "_NoopSpinner":
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        return None


@pytest.fixture
def manager(tmp_path, monkeypatch):
    # Keep tests fast and deterministic by removing spinner output/thread churn.
    monkeypatch.setattr(habitat_manager.habitat_ux, "Spinner", _NoopSpinner)

    config_path = tmp_path / "habitat_config.json"
    manager = habitat_manager.HabitatManager(config_file=str(config_path))
    yield manager

    for habitat in list(manager.habitats.values()):
        try:
            habitat.cleanup()
        except FileNotFoundError:
            pass


def test_init_creates_default_config(manager):
    config_file = Path(manager.config_file)
    assert config_file.exists()

    raw = json.loads(config_file.read_text(encoding="utf-8"))
    assert raw == manager.config
    assert "main" in manager.habitats
    assert manager.habitats["main"].name == "main_lab"
    assert manager.habitats["main"].isolation_level == 3
    assert raw["default_habitat"]["name"] == "main_lab"


def test_spawn_experiment_uses_recursive_myth_default(manager):
    exp_data = manager.spawn_experiment("myth_experiment")

    experiment = exp_data["experiment"]
    assert isinstance(experiment, RecursiveMythEngine)
    assert experiment.name == "myth_experiment"
    assert exp_data["status"] == "spawned"


def test_spawn_experiment_uses_generic_system_for_non_myth_type(manager):
    exp_data = manager.spawn_experiment(
        "generic_experiment", experiment_type="pattern_test"
    )

    experiment = exp_data["experiment"]
    assert isinstance(experiment, ExperimentalSystem)
    assert not isinstance(experiment, RecursiveMythEngine)


def test_run_experiment_happy_path(manager):
    manager.spawn_experiment("quick_test", experiment_type="recursive_myth")
    result = manager.run_experiment("quick_test")

    assert isinstance(result, dict)
    assert "myth" in result
    status = manager.habitats["main"].active_experiments["quick_test"]
    assert status["status"] == "completed"


def test_run_experiment_errors_for_unknown_habitat(manager):
    with pytest.raises(ValueError, match="Habitat 'missing' not found"):
        manager.run_experiment("quick_test", habitat_name="missing")


def test_get_status_returns_active_habitat_experiment_data(manager):
    manager.spawn_experiment("status_probe")
    status = manager.get_status("status_probe")

    assert status["Status"] == "spawning"
    assert status["Hypothesis"] == "Default experiment hypothesis"
    assert status["Boundary"] == "boundary_status_probe"


def test_get_status_returns_graduated_experiment_payload(manager):
    manager.spawn_experiment("grad_ready")
    manager.run_experiment("grad_ready")
    forge_package = manager.graduate_experiment("grad_ready")

    status = manager.get_status("grad_ready")
    assert status["name"] == forge_package["name"]
    assert "code_patterns" in status
    assert "symbolic_mappings" in status


def test_get_status_returns_composted_experiment_payload(manager):
    parent = manager.habitats["main"]

    class FailingExperiment(ExperimentalSystem):
        def _execute_experiment(self):
            raise RuntimeError("planned failure")

    failing = FailingExperiment("failing", "fail on demand")
    parent.spawn_experiment(failing, {"resources": {}})
    with pytest.raises(RuntimeError, match="planned failure"):
        parent.run_experiment("failing")

    lessons = manager.compost_experiment("failing", "intentional test failure")
    assert "what_failed" in lessons

    status = manager.get_status("failing")
    assert status["lessons"]["what_failed"] == "planned failure"


def test_get_status_returns_empty_for_unknown_experiment(manager):
    status = manager.get_status("does_not_exist")
    assert status == {}


def test_create_nested_habitat_registers_child_key(manager):
    manager.habitats["main"].spawn_experiment(
        ExperimentalSystem("parent", "for-nesting"),
        {"resources": {}},
    )

    nested = manager.create_nested_habitat("parent", "analysis")

    assert nested.name == "main_lab_nested_analysis"
    assert manager.habitats["main_analysis"] is nested
    assert nested.nesting_depth == 1


def test_list_habitats_prints_output(manager, capsys):
    manager.list_habitats()
    output = capsys.readouterr().out

    assert "Active Habitats" in output
    assert "Habitat: main" in output


def test_cleanup_all_respects_cancel_and_force_paths(manager, monkeypatch):
    calls = []

    def fake_cleanup() -> None:
        calls.append("cleanup")

    monkeypatch.setattr(manager.habitats["main"], "cleanup", fake_cleanup)

    monkeypatch.setattr("builtins.input", lambda _="": "n")
    manager.cleanup_all()
    assert calls == []

    manager.cleanup_all(force=True)
    assert calls == ["cleanup"]
