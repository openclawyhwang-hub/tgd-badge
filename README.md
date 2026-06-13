<div align="center">
  <h1>🎨 tgd-badge</h1>
  <p><strong>SVG badge generator for the tGD ecosystem</strong></p>
  <p>Generate shields.io-style badges locally — zero dependencies, pure Python.</p>
  <p>
    <a href="https://github.com/openclawyhwang-hub/tgd-badge/releases">
      <img src="https://img.shields.io/github/v/release/openclawyhwang-hub/tgd-badge" alt="Release">
    </a>
    <a href="https://github.com/openclawyhwang-hub/tgd-badge">
      <img src="https://img.shields.io/github/license/openclawyhwang-hub/tgd-badge" alt="License">
    </a>
  </p>
</div>

---

## ✨ Features

- **Zero dependencies** — pure Python SVG generation, no npm, no HTTP calls
- **Three styles** — `flat`, `flat-square`, `plastic`
- **Named colors** — 9 built-in colors + custom hex support
- **CLI-first** — pipe-friendly, CI/CD ready
- **tGD branding** — consistent badges for your tGD ecosystem projects

## 📦 Installation

```bash
pip install tgd-badge
```

Or from source:

```bash
git clone https://github.com/openclawyhwang-hub/tgd-badge.git
cd tgd-badge
pip install -e .
```

## 🚀 Usage

### Basic

```bash
tgd-badge "tGD" "v1.0"
```

Outputs SVG to stdout:

<p align="center">
  <img src="https://img.shields.io/badge/tGD-v1.0-brightgreen" alt="tGD v1.0 badge">
</p>

### With color

```bash
tgd-badge "status" "active" --color blue
tgd-badge "tGD" "compatible" --color brightgreen
tgd-badge "build" "passing" --color green
tgd-badge "version" "2.0.0" --color purple
```

### With style

```bash
tgd-badge "tGD" "v1.0" --style flat           # rounded corners (default)
tgd-badge "tGD" "v1.0" --style flat-square     # sharp corners
tgd-badge "tGD" "v1.0" --style plastic         # gradient + shadow
```

### Save to file

```bash
tgd-badge "tGD" "v1.0" --color green -o badge.svg
```

### Custom hex colors

```bash
tgd-badge "custom" "#ff6600" --color "#ff6600"
```

### List available colors

```bash
tgd-badge --list-colors
```

### Pipe to clipboard

```bash
tgd-badge "tGD" "v1.0" | pbcopy  # macOS
tgd-badge "tGD" "v1.0" | xclip   # Linux
```

## 🎨 Colors

| Name | Hex |
|------|-----|
| `brightgreen` | `#4c1` |
| `green` | `#97ca00` |
| `yellow` | `#dfb317` |
| `orange` | `#fe7d37` |
| `red` | `#e05d44` |
| `blue` | `#007ec6` |
| `purple` | `#a05dec` |
| `grey` | `#555` |
| `lightgrey` | `#9f9f9f` |

## 🧪 Development

```bash
# Clone and install
git clone https://github.com/openclawyhwang-hub/tgd-badge.git
cd tgd-badge
pip install -e .

# Run tests
pytest tests/ -v

# Lint
ruff check src/ tests/
```

### Project Structure

```
tgd-badge/
├── src/tgd_badge/
│   ├── __init__.py    # Version
│   ├── __main__.py    # python -m entry
│   ├── badge.py       # SVG badge rendering
│   ├── cli.py         # CLI entrypoint
│   └── colors.py      # Color definitions
├── tests/
│   ├── test_badge.py  # Badge rendering tests (15)
│   ├── test_cli.py    # CLI integration tests (17)
│   └── test_colors.py # Color resolution tests (13)
├── PRD.md             # Product requirements
├── SPEC.md            # Technical specification
├── TASKS.md           # Task breakdown
├── TEST-REPORT.md     # Test results
└── REVIEW.md           # Code review
```

## 🤝 Contributing

PRs welcome! This is a tGD ecosystem project — all new features should follow tGD development lifecycle.

## 📄 License

MIT
