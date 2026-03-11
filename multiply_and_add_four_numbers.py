def multiply_pairs_and_add(first: int, second: int, third: int, fourth: int) -> int:
    return (first * second) + (third * fourth)


def main() -> None:
    first_number = int(input("Enter first number: ").strip())
    second_number = int(input("Enter second number: ").strip())
    third_number = int(input("Enter third number: ").strip())
    fourth_number = int(input("Enter fourth number: ").strip())

    result = multiply_pairs_and_add(first_number, second_number, third_number, fourth_number)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
