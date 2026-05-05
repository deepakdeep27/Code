"""
Read a CSV file in UTF-8 format and display its contents in black color.

Usage:
    python read_csv_utf8.py <csv_file_path>

If no file path is provided, the script uses a built-in sample CSV for demo.
"""

import csv
import sys
import os

# ANSI escape code for black text on default background
BLACK = "\033[30m"
RESET = "\033[0m"


def read_csv_utf8(file_path: str) -> None:
    """Read a CSV file encoded in UTF-8 and print each row in black color."""
    if not os.path.isfile(file_path):
        print(f"Error: file '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            line = ", ".join(row)
            print(f"{BLACK}{line}{RESET}")


def create_sample_csv(path: str) -> None:
    """Create a small sample CSV file for demonstration purposes."""
    with open(path, mode="w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", "30", "New York"])
        writer.writerow(["Bob", "25", "London"])
        writer.writerow(["Charlie", "35", "Tokyo"])
        writer.writerow(["Déjà", "28", "Paris"])  # UTF-8 accented characters


if __name__ == "__main__":
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
    else:
        csv_path = "sample.csv"
        print("No file provided. Creating a sample CSV for demo...\n")
        create_sample_csv(csv_path)

    read_csv_utf8(csv_path)
