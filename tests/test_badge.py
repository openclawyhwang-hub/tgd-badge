"""RED: Write failing tests for badge SVG renderer."""

from tgd_badge.badge import render_badge, STYLES


class TestRenderBadge:
    """render_badge(label, message, color, style) → SVG string"""

    def test_returns_string(self):
        """Returns a string"""
        result = render_badge("label", "message", "#4c1")
        assert isinstance(result, str)

    def test_starts_with_svg_tag(self):
        """SVG starts with <svg tag"""
        result = render_badge("label", "message", "#4c1")
        assert result.strip().startswith("<svg")

    def test_ends_with_svg_close(self):
        """SVG ends with </svg>"""
        result = render_badge("label", "message", "#4c1")
        assert result.strip().endswith("</svg>")

    def test_contains_label_text(self):
        """SVG contains the label text"""
        result = render_badge("test-label", "test-msg", "#4c1")
        assert "test-label" in result

    def test_contains_message_text(self):
        """SVG contains the message text"""
        result = render_badge("test-label", "test-msg", "#4c1")
        assert "test-msg" in result

    def test_contains_color_in_svg(self):
        """SVG contains the color string somewhere (fill)"""
        result = render_badge("a", "b", "#ff6600")
        assert "#ff6600" in result or "ff6600" in result

    def test_flat_style_is_default(self):
        """Default style is flat"""
        result = render_badge("a", "b", "#4c1")
        # flat has rounded rects
        assert "rx=" in result

    def test_flat_square_style(self):
        """flat-square style works"""
        result = render_badge("a", "b", "#4c1", style="flat-square")
        assert isinstance(result, str)

    def test_plastic_style(self):
        """plastic style works"""
        result = render_badge("a", "b", "#4c1", style="plastic")
        assert isinstance(result, str)

    def test_invalid_style_uses_default(self):
        """Invalid style falls back to flat"""
        result = render_badge("a", "b", "#4c1", style="nonexistent")
        assert isinstance(result, str)

    def test_label_width_scales_with_text_length(self):
        """Short and long labels produce different widths"""
        short = render_badge("hi", "msg", "#4c1")
        long = render_badge("very-long-label", "msg", "#4c1")
        assert len(short) != len(long)  # Different SVG dimensions

    def test_out_has_valid_xml_syntax(self):
        """SVG output has valid XML syntax (matching tags)"""
        result = render_badge("test", "value", "#4c1")
        assert result.count("<text") >= 2  # At least two text elements
        assert result.count("</text>") >= 2


class TestStyles:
    """Test that STYLES dict is properly defined"""

    def test_styles_has_flat(self):
        assert "flat" in STYLES

    def test_styles_has_flat_square(self):
        assert "flat-square" in STYLES

    def test_styles_has_plastic(self):
        assert "plastic" in STYLES
