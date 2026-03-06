#!/usr/bin/env python3
"""Simple utility to read and print CSV files."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def read_csv_file(file_path: Path, delimiter: str = ",", encoding: str = "utf-8") -> None:
    """Read a CSV file and print its rows as dictionaries."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with file_path.open("r", newline="", encoding=encoding) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        if reader.fieldnames is None:
            print("CSV file appears to be empty or missing a header row.")
            return

        print(f"Columns: {', '.join(reader.fieldnames)}")
        print("-" * 40)

        row_count = 0
        for row_count, row in enumerate(reader, start=1):
            print(f"Row {row_count}: {row}")

        print("-" * 40)
        print(f"Total rows read: {row_count}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read and print a CSV file.")
    parser.add_argument("path", type=Path, help="Path to the CSV file")
    parser.add_argument("--delimiter", default=",", help="CSV delimiter (default: ',')")
    parser.add_argument("--encoding", default="utf-8", help="File encoding (default: utf-8)")

    args = parser.parse_args()

    try:
        read_csv_file(args.path, delimiter=args.delimiter, encoding=args.encoding)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except UnicodeDecodeError as exc:
        print(f"Encoding error: {exc}", file=sys.stderr)
        return 1
    except csv.Error as exc:
        print(f"CSV parsing error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
