"""Simple utilities for subtracting two numbers."""

import argparse


def subtract(first: float, second: float) -> float:
    """Return the result of subtracting the second number from the first."""
    return first - second


def main() -> None:
    parser = argparse.ArgumentParser(description="Subtract two numbers.")
    parser.add_argument("first", type=float, help="The number to subtract from")
    parser.add_argument("second", type=float, help="The number to subtract")
    args = parser.parse_args()

    result = subtract(args.first, args.second)
    print(int(result) if result.is_integer() else result)


if __name__ == "__main__":
    main()
