# SPEC: tgd-badge

## Tech Stack

- **Language**: Python 3.10+ (no external dependencies)
- **Test Framework**: pytest
- **Build System**: setuptools / pyproject.toml
- **CLI**: Click-style (hand-rolled argparse, no dependency)

## Architecture

```
tgd-badge/
├── src/
│   └── tgd_badge/
│       ├── __init__.py    # version
│       ├── __main__.py    # python -m entry
│       ├── cli.py         # arg parsing, entrypoint
│       ├── badge.py       # SVG badge rendering
│       └── colors.py      # color definitions
├── tests/
│   ├── conftest.py
│   ├── test_badge.py
│   ├── test_cli.py
│   └── test_colors.py
├── pyproject.toml
├── PRD.md
├── SPEC.md
├── TASKS.md
└── README.md
```

## CLI Commands

```
usage: tgd-badge <label> <message> [-c COLOR] [-s STYLE] [-o OUTPUT] [--list-colors] [--version]

Generate SVG badges for tGD projects.

positional arguments:
  label                 Left-side label text
  message               Right-side message text

options:
  -c, --color           Badge color (name or hex, e.g. green, brightgreen, #ff6600)
  -s, --style           Badge style: flat, flat-square, plastic
  -o, --output          Output file path (default: stdout)
  --list-colors         List available color names and exit
  --version             Show version and exit
```

## Key Components

### `badge.py`

Core SVG generator. Creates responsive, clean badges:

```
Function: render_badge(label, message, color, style) → str
```

- `style='flat'`: Rounded rectangle, subtle shadow, default look
- `style='flat-square'`: Sharp corners, flat design
- `style='plastic'`: Slight gradient and border

### `colors.py`

Color mapping dictionary:

```python
COLORS = {
    'brightgreen': '#4c1',
    'green': '#97ca00',
    'yellow': '#dfb317',
    'orange': '#fe7d37',
    'red': '#e05d44',
    'blue': '#007ec6',
    'purple': '#a05dec',
    'grey': '#555',
}
```

### `cli.py`

- Uses `argparse` (stdlib)
- Handles stdin → piping
- Exits with code 1 on error

## Testing Strategy

- **Unit tests** for badge SVG output (validate XML structure, dimensions)
- **Unit tests** for color resolution (name → hex, hex passthrough, invalid)
- **Integration tests** for CLI (capture stdout, file output, error codes)
- **Edge case tests** (empty strings, unknown colors, missing args)

## Sign-off

- [x] **DEV**: [Auto] — Approved — 2025-06-13
- [ ] **QA**: [Pending] — —
