def multiply_two_integers(a: int, b: int) -> int:
    return a * b


def main() -> None:
    first_number = int(input("Enter first integer: ").strip())
    second_number = int(input("Enter second integer: ").strip())
    print(f"Product: {multiply_two_integers(first_number, second_number)}")


if __name__ == "__main__":
    main()
