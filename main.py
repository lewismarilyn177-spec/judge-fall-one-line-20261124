import os
import sys
from pathlib import Path


def read_entry() -> str:
    content = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    return content.rstrip("\r\n")


def choose_output_directory() -> Path:
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured == "":
        raise ValueError("MAKEFUN_OUTPUT_DIR must not be empty")
    return Path(configured or "/output")


def write_entry(destination: Path, line: str) -> None:
    if not 1 <= len(line) <= 240 or "\n" in line or "\r" in line:
        raise ValueError("entry.txt must contain one line of 1 to 240 characters")
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_text(line, encoding="utf-8")


def main() -> int:
    try:
        write_entry(choose_output_directory(), read_entry())
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
