"""Color definitions and resolution for tgd-badge."""

# Shields.io-inspired color palette
COLORS = {
    "brightgreen": "#4c1",
    "green": "#97ca00",
    "yellow": "#dfb317",
    "orange": "#fe7d37",
    "red": "#e05d44",
    "blue": "#007ec6",
    "purple": "#a05dec",
    "grey": "#555",
    "lightgrey": "#9f9f9f",
}


def resolve_color(color_str: str) -> str:
    """Resolve a color name or hex string to a #hex value.

    Args:
        color_str: Color name (case-insensitive) or hex string (with or without #).

    Returns:
        Hex color string with leading #.

    Raises:
        ValueError: If the color name is unknown and not a valid hex.
    """
    if color_str.startswith("#"):
        return color_str

    # Check if it's a hex string (3 or 6 chars, hex digits only)
    stripped = color_str.lstrip("#")
    if all(c in "0123456789abcdefABCDEF" for c in stripped) and len(stripped) in (3, 6):
        return f"#{stripped}"

    # Check color name (case-insensitive)
    lower = color_str.lower()
    if lower in COLORS:
        return COLORS[lower]

    raise ValueError(f"Unknown color: {color_str!r}")


def list_colors() -> str:
    """Return formatted list of available colors."""
    max_name_len = max(len(n) for n in COLORS)
    lines = []
    for name, hex_val in sorted(COLORS.items()):
        lines.append(f"  {name:<{max_name_len}}  {hex_val}")
    return "\n".join(lines)
