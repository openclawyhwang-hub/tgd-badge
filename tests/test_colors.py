# RED: Write failing tests for colors module

import pytest
from tgd_badge.colors import resolve_color, COLORS, list_colors
import re


class TestResolveColor:
    """resolve_color(name_or_hex) → hex string"""

    def test_known_color_name_returns_hex(self):
        """Known color name returns its hex value"""
        result = resolve_color("green")
        assert result == "#97ca00"

    def test_brightgreen(self):
        """brightgreen returns correct hex"""
        assert resolve_color("brightgreen") == "#4c1"

    def test_blue(self):
        """blue returns correct hex"""
        assert resolve_color("blue") == "#007ec6"

    def test_purple(self):
        """purple returns correct hex"""
        assert resolve_color("purple") == "#a05dec"

    def test_grey(self):
        """grey returns correct hex"""
        assert resolve_color("grey") == "#555"

    def test_hex_passthrough_with_hash(self):
        """Hex string with # is returned as-is"""
        result = resolve_color("#ff6600")
        assert result == "#ff6600"

    def test_hex_passthrough_6_chars(self):
        """6-char hex without # gets # prepended"""
        result = resolve_color("ff6600")
        assert result == "#ff6600"

    def test_hex_passthrough_3_chars(self):
        """3-char hex without # gets # prepended"""
        result = resolve_color("f60")
        assert result == "#f60"

    def test_unknown_color_raises_valueerror(self):
        """Unknown color name raises ValueError"""
        with pytest.raises(ValueError, match="Unknown color"):
            resolve_color("nonexistent")

    def test_case_insensitive(self):
        """Color names are case-insensitive"""
        assert resolve_color("GREEN") == "#97ca00"
        assert resolve_color("Blue") == "#007ec6"


class TestListColors:
    """list_colors() returns formatted string"""

    def test_list_colors_returns_formatted_output(self):
        """list_colors returns lines of name + hex"""
        output = list_colors()
        assert "#97ca00" in output
        assert "#007ec6" in output
        assert "#a05dec" in output
        assert "green" in output


class TestColorsModule:
    def test_all_colors_are_valid_hex(self):
        """All COLORS entries are valid 3- or 6-digit hex"""
        hex_pattern = re.compile(r'^#[0-9a-fA-F]{3,6}$')
        for name, hex_val in COLORS.items():
            assert hex_pattern.match(hex_val), f"{name}: {hex_val}"

    def test_colors_are_lowercase_keys(self):
        """All color name keys are lowercase"""
        for name in COLORS:
            assert name == name.lower(), f"{name} is not lowercase"
