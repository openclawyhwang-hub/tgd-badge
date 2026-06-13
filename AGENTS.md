# tgd-badge — AI Agent Guide

## Overview

tgd-badge is a CLI tool that generates high-quality SVG badge images for tGD ecosystem projects. It produces badges like shields.io but tailored for the tGD framework — "powered by tGD", "tGD v1.0", "tGD-compatible", "status: active" etc.

## Tech Stack

- **Language**: Python 3.10+
- **Build**: No external dependencies (pure Python SVG generation)
- **Test**: pytest
- **Distribution**: pip (private PyPI or direct install)

## Key Files

- `src/tgd_badge/__init__.py` — Package init
- `src/tgd_badge/cli.py` — CLI entrypoint
- `src/tgd_badge/badge.py` — SVG badge generation logic
- `tests/test_badge.py` — Tests
- `README.md` — User documentation
- `PRD.md` — Product requirements
- `SPEC.md` — Technical specification
- `TASKS.md` — Task breakdown
