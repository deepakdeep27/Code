#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Iterable


def iter_rows(
    csv_path: Path,
    *,
    delimiter: str = ",",
    encoding: str = "utf-8",
    has_header: bool = True,
) -> Iterable[dict[str, str] | list[str]]:
    with csv_path.open("r", encoding=encoding, newline="") as f:
        if has_header:
            reader = csv.DictReader(f, delimiter=delimiter)
            yield from reader
        else:
            reader = csv.reader(f, delimiter=delimiter)
            yield from reader


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Read a CSV file and print rows.")
    p.add_argument("path", type=Path, help="Path to the CSV file")
    p.add_argument("--delimiter", default=",", help="CSV delimiter (default: ',')")
    p.add_argument("--encoding", default="utf-8", help="File encoding (default: utf-8)")
    p.add_argument(
        "--no-header",
        action="store_true",
        help="Treat the first row as data (not a header)",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum rows to print (default: 10). Use 0 for all rows.",
    )
    args = p.parse_args(argv)

    if not args.path.exists():
        print(f"File not found: {args.path}", file=sys.stderr)
        return 2

    count = 0
    for row in iter_rows(
        args.path,
        delimiter=args.delimiter,
        encoding=args.encoding,
        has_header=not args.no_header,
    ):
        print(row)
        count += 1
        if args.limit and count >= args.limit:
            break

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
