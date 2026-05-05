"""Read a CSV file using UTF-8 encoding."""

import csv
import sys


def read_csv_utf(file_path, encoding="utf-8"):
    """Read a CSV file with the specified UTF encoding and return rows.

    Args:
        file_path: Path to the CSV file.
        encoding: Character encoding to use (default: utf-8).
                  Common options: utf-8, utf-16, utf-32.

    Returns:
        A list of rows, where each row is a list of field values.
    """
    rows = []
    with open(file_path, mode="r", encoding=encoding, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def main():
    if len(sys.argv) < 2:
        print("Usage: python read_csv_utf.py <file_path> [encoding]")
        print("  encoding: utf-8 (default), utf-16, utf-32")
        sys.exit(1)

    file_path = sys.argv[1]
    encoding = sys.argv[2] if len(sys.argv) > 2 else "utf-8"

    try:
        rows = read_csv_utf(file_path, encoding)
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
        sys.exit(1)
    except UnicodeDecodeError as exc:
        print(f"Error: unable to decode file with encoding '{encoding}': {exc}")
        sys.exit(1)

    if not rows:
        print("The CSV file is empty.")
        return

    header = rows[0]
    print(f"Columns ({len(header)}): {', '.join(header)}")
    print(f"Data rows: {len(rows) - 1}\n")

    for i, row in enumerate(rows):
        print(f"Row {i}: {row}")


if __name__ == "__main__":
    main()
