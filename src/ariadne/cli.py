from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ariadne",
        description="Ariadne — your beginner-to-LLM Python project CLI.",
    )
    parser.add_argument(
        "--name",
        default="World",
        help="Name to greet (default: World).",
    )
    return parser


def run(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    print(f"Hello, {args.name}! I'm Ariadne.")
    return 0


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
