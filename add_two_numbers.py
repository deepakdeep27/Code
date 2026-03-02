def add_three_numbers(a: float, b: float, c: float) -> float:
    return a + b + c


def main() -> None:
    a = float(input("Enter first number: ").strip())
    b = float(input("Enter second number: ").strip())
    c = float(input("Enter third number: ").strip())
    print(f"Sum: {add_three_numbers(a, b, c)}")


if __name__ == "__main__":
    main()
