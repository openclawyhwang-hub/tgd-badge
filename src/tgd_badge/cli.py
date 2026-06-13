"""CLI entrypoint for tgd-badge."""

import argparse
import sys

from . import __version__
from .badge import render_badge
from .colors import list_colors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments.

    Args:
        argv: Argument list (default: sys.argv[1:]).

    Returns:
        Parsed namespace.
    """
    parser = argparse.ArgumentParser(
        prog="tgd-badge",
        description="Generate SVG badges for tGD projects.",
    )
    parser.add_argument(
        "label",
        nargs="?",
        help="Left-side label text",
    )
    parser.add_argument(
        "message",
        nargs="?",
        help="Right-side message text",
    )
    parser.add_argument(
        "-c",
        "--color",
        default="green",
        help="Badge color (name or hex, default: green)",
    )
    parser.add_argument(
        "-s",
        "--style",
        default="flat",
        choices=["flat", "flat-square", "plastic"],
        help="Badge style (default: flat)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--list-colors",
        action="store_true",
        help="List available colors and exit",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version and exit",
    )

    args = parser.parse_args(argv)

    # Validate: label and message required unless a flag is set
    if not args.list_colors and not args.version:
        if not args.label or not args.message:
            parser.error("the following arguments are required: label, message")

    return args


def main(argv: list[str] | None = None) -> None:
    """Main entrypoint.

    Args:
        argv: Argument list (default: sys.argv[1:]).
    """
    if argv is None:
        argv = sys.argv[1:]

    args = parse_args(argv)

    # Handle flag-only commands
    if args.list_colors:
        print("Available colors:")
        print(list_colors())
        return

    if args.version:
        print(f"tgd-badge v{__version__}")
        return

    # Generate badge
    try:
        svg = render_badge(args.label, args.message, args.color, args.style)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Output
    if args.output:
        with open(args.output, "w") as f:
            f.write(svg)
            f.write("\n")
    else:
        print(svg)


if __name__ == "__main__":
    main()
