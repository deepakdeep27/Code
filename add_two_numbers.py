def add_two_numbers(a: float, b: float) -> float:
    return a + b


def main() -> None:
    a = float(input("Enter first number: ").strip())
    b = float(input("Enter second number: ").strip())
    print(f"Sum: {add_two_numbers(a, b)}")


if __name__ == "__main__":
    main()
