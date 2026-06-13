"""RED: Write failing tests for CLI."""

import pytest
from tgd_badge.cli import parse_args, main


class TestParseArgs:
    """parse_args() returns parsed namespace"""

    def test_label_and_message_positional(self):
        """Parses label and message from positional args"""
        args = parse_args(["hello", "world"])
        assert args.label == "hello"
        assert args.message == "world"

    def test_default_color(self):
        """Default color is green"""
        args = parse_args(["a", "b"])
        assert args.color == "green"

    def test_custom_color_flag(self):
        """--color sets the color"""
        args = parse_args(["a", "b", "--color", "blue"])
        assert args.color == "blue"

    def test_custom_color_short(self):
        """-c sets the color"""
        args = parse_args(["a", "b", "-c", "#ff6600"])
        assert args.color == "#ff6600"

    def test_default_style(self):
        """Default style is flat"""
        args = parse_args(["a", "b"])
        assert args.style == "flat"

    def test_custom_style(self):
        """--style sets the style"""
        args = parse_args(["a", "b", "--style", "plastic"])
        assert args.style == "plastic"

    def test_style_short(self):
        """-s sets the style"""
        args = parse_args(["a", "b", "-s", "flat-square"])
        assert args.style == "flat-square"

    def test_output_flag(self):
        """--output sets output path"""
        args = parse_args(["a", "b", "--output", "badge.svg"])
        assert args.output == "badge.svg"

    def test_output_short(self):
        """-o sets output path"""
        args = parse_args(["a", "b", "-o", "out.svg"])
        assert args.output == "out.svg"

    def test_list_colors(self):
        """--list-colors returns True"""
        args = parse_args(["--list-colors"])
        assert args.list_colors is True

    def test_version(self):
        """--version returns True"""
        args = parse_args(["--version"])
        assert args.version is True

    def test_no_args_raises_systemexit(self):
        """No args should exit with error"""
        with pytest.raises(SystemExit):
            parse_args([])

    def test_missing_message_raises_systemexit(self):
        """Only label without message should exit"""
        with pytest.raises(SystemExit):
            parse_args(["label"])


class TestMainFunction:
    """Integration-level tests for main()"""

    def test_main_prints_svg_to_stdout(self, capsys):
        """main() with valid args prints SVG to stdout"""
        main(["test", "value"])
        captured = capsys.readouterr()
        assert captured.out.strip().startswith("<svg")

    def test_main_no_args_prints_error(self, capsys):
        """main() with no args prints usage error"""
        with pytest.raises(SystemExit):
            main([])

    def test_main_list_colors(self, capsys):
        """main() --list-colors prints colors to stdout"""
        main(["--list-colors"])
        captured = capsys.readouterr()
        assert "#97ca00" in captured.out

    def test_main_version(self, capsys):
        """main() --version prints version"""
        main(["--version"])
        captured = capsys.readouterr()
        assert "tgd-badge" in captured.out
        assert "1.0.0" in captured.out
