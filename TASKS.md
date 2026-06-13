# TASKS: tgd-badge

## Task Dependencies

```
task-1 (init/struct) ← task-3 (cli)
task-2 (colors) ← task-3 (cli)
task-2 (colors) ← task-4 (badge)
task-4 (badge) ← task-5 (render tests)
task-3 (cli) ← task-6 (cli tests)
```

## Tasks

### Task 1: Project scaffold + pyproject.toml

- **Files**: `pyproject.toml`, `src/tgd_badge/__init__.py`, `src/tgd_badge/__main__.py`
- **Do**: Set up Python package structure with setuptools, define version
- **Verify**: `pip install -e .` succeeds, `python -m tgd_badge` prints version

### Task 2: Colors module

- **Files**: `src/tgd_badge/colors.py`, `tests/test_colors.py`
- **Do**: Define color map + resolution function
- **Verify**: Tests pass for name→hex, hex passthrough, invalid colors

### Task 3: CLI entrypoint

- **Files**: `src/tgd_badge/cli.py`, `tests/test_cli.py`
- **Do**: Argparse-based CLI with all options
- **Verify**: `tgd-badge --help` works, `--list-colors` prints colors, errors on missing args

### Task 4: Badge SVG renderer

- **Files**: `src/tgd_badge/badge.py`, `tests/test_badge.py`
- **Do**: SVG generation for flat, flat-square, plastic styles
- **Verify**: Tests pass for SVG structure, dimensions, styles

### Task 5: Badge rendering tests

- **Files**: `tests/test_badge.py` (extend)
- **Do**: Validate SVG content — XML tags, colors, text, dimensions
- **Verify**: All rendering tests pass

### Task 6: CLI integration tests

- **Files**: `tests/test_cli.py` (extend)
- **Do**: Test CLI end-to-end — stdout, file output, error codes
- **Verify**: CLI integration tests pass

### Task 7: End-to-end verification

- **Files**: (no new files)
- **Do**: Run full test suite, generate example badges, verify SVG renders
- **Verify**: All tests pass, SVG files open in browser correctly

## Sign-off

- [ ] **DEV**: [Pending] — —  
- [ ] **QA**: [Pending] — —
