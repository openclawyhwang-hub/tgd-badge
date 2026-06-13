"""SVG badge generation for tgd-badge."""

from .colors import resolve_color

# Style presets: each style defines SVG attributes
STYLES = {
    "flat": {
        "rect_rx": "3",
        "rect_ry": "3",
        "label_gradient": False,
        "message_gradient": False,
        "shadow": True,
    },
    "flat-square": {
        "rect_rx": "0",
        "rect_ry": "0",
        "label_gradient": False,
        "message_gradient": False,
        "shadow": False,
    },
    "plastic": {
        "rect_rx": "3",
        "rect_ry": "3",
        "label_gradient": True,
        "message_gradient": True,
        "shadow": True,
    },
}

# Default style
_DEFAULT_STYLE = "flat"

# Font metrics — approximate character width in pixels
_CHAR_WIDTH = 7
_PADDING_X = 5
_LABEL_BG = "#555"  # Dark grey for label side


def _get_width(text: str) -> int:
    """Calculate approximate width for text block."""
    return len(text) * _CHAR_WIDTH + _PADDING_X * 2


def _hex_to_rgb(hex_color: str) -> tuple:
    """Convert #rgb or #rrggbb to (r, g, b) tuple."""
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def _gradient_defs(bg_color: str, height: int, suffix: str = "") -> str:
    """Generate linear gradient SVG definition for plastic style."""
    r, g, b = _hex_to_rgb(bg_color)
    return f"""    <linearGradient id="b-{suffix}" x2="0" y2="1">
      <stop offset="0" stop-color="#{(min(255, r + 30)):02x}{(min(255, g + 30)):02x}{(min(255, b + 30)):02x}" stop-opacity="1"/>
      <stop offset="1" stop-color="{bg_color}" stop-opacity="1"/>
    </linearGradient>"""


def _shadow_filter() -> str:
    """SVG filter definition for drop shadow."""
    return """    <filter id="s">
      <feDropShadow dx="0" dy="1" stdDeviation="1" flood-opacity=".3"/>
    </filter>"""


def render_badge(
    label: str,
    message: str,
    color: str,
    style: str = "flat",
) -> str:
    """Generate an SVG badge.

    Args:
        label: Left-side label text.
        message: Right-side message text.
        color: Badge color (name or hex string).
        style: Badge style ("flat", "flat-square", "plastic").

    Returns:
        Complete SVG string.
    """
    hex_color = resolve_color(color)
    style_config = STYLES.get(style, STYLES[_DEFAULT_STYLE])

    height = 20
    label_w = _get_width(label)
    message_w = _get_width(message)
    total_w = label_w + message_w

    # Build SVG parts
    parts = []

    # XML + SVG open
    xmlns = 'xmlns="http://www.w3.org/2000/svg"'
    parts.append(f'<svg {xmlns} width="{total_w}" height="{height}" viewBox="0 0 {total_w} {height}">')

    # Defs (gradients + shadow)
    defs_parts = []
    if style_config.get("shadow"):
        defs_parts.append(_shadow_filter())
    if style_config.get("message_gradient"):
        defs_parts.append(_gradient_defs(hex_color, height, "msg"))
    if style_config.get("label_gradient"):
        defs_parts.append(_gradient_defs(_LABEL_BG, height, "lbl"))
    if defs_parts:
        parts.append("  <defs>")
        parts.extend("  " + d for d in defs_parts)
        parts.append("  </defs>")

    # Shadow box (if enabled)
    rx = style_config["rect_rx"]
    ry = style_config["rect_ry"]

    shadow_attr = ' filter="url(#s)"' if style_config.get("shadow") else ""

    # Label background
    label_bg_fill = 'url(#b-lbl)' if style_config.get("label_gradient") else _LABEL_BG
    parts.append(
        f'  <rect rx="{rx}" ry="{ry}" x="0" width="{label_w}" '
        f'height="{height}" fill="{label_bg_fill}"{shadow_attr}/>'
    )

    # Clip label side's right edge so text doesn't bleed into message
    parts.append(
        f'  <clipPath id="l-clip"><rect rx="{rx}" ry="{ry}" '
        f'x="0" width="{label_w}" height="{height}"/></clipPath>'
    )

    # Label text
    text_x = _PADDING_X
    text_y = height // 2 + 1
    parts.append(
        '  <g clip-path="url(#l-clip)" fill="#fff" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" '
        'font-size="11" font-weight="400">'
    )
    parts.append(
        f'    <text x="{text_x}" y="{text_y}" fill="#fff" '
        f'text-anchor="start" dominant-baseline="central">{_xml_escape(label)}</text>'
    )
    parts.append("  </g>")

    # Message background (right side)
    msg_bg_fill = 'url(#b-msg)' if style_config.get("message_gradient") else hex_color
    parts.append(
        f'  <rect rx="{rx}" ry="{ry}" x="{label_w}" width="{message_w}" '
        f'height="{height}" fill="{msg_bg_fill}"{shadow_attr}/>'
    )

    # Clip message side's left edge
    parts.append(
        f'  <clipPath id="r-clip"><rect rx="{rx}" ry="{ry}" '
        f'x="{label_w}" width="{message_w}" height="{height}"/></clipPath>'
    )

    # Message text
    msg_x = label_w + _PADDING_X
    parts.append(
        '  <g clip-path="url(#r-clip)" fill="#fff" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" '
        'font-size="11" font-weight="400">'
    )
    parts.append(
        f'    <text x="{msg_x}" y="{text_y}" fill="#fff" '
        f'text-anchor="start" dominant-baseline="central">{_xml_escape(message)}</text>'
    )
    parts.append("  </g>")

    parts.append("</svg>")

    return "\n".join(parts)


def _xml_escape(text: str) -> str:
    """Escape XML special characters."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )
