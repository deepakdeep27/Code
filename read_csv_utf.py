"""Read a CSV file encoded in UTF-8 and display its contents."""

import csv
import sys


def read_csv_utf(file_path: str) -> list[dict[str, str]]:
    """Read a UTF-8 encoded CSV file and return rows as a list of dicts.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A list of dictionaries, one per row, keyed by column headers.
    """
    rows: list[dict[str, str]] = []
    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python read_csv_utf.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    rows = read_csv_utf(file_path)

    if not rows:
        print("The CSV file is empty or has no data rows.")
        return

    # Print header
    headers = list(rows[0].keys())
    print(" | ".join(headers))
    print("-" * (sum(len(h) for h in headers) + 3 * (len(headers) - 1)))

    # Print rows
    for row in rows:
        print(" | ".join(row.get(h, "") for h in headers))

    print(f"\nTotal rows: {len(rows)}")


if __name__ == "__main__":
    main()
