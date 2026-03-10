def add_three_numbers(a: float, b: float, c: float) -> float:
    numbers = (a, b, c)

    if not all(number < 100 for number in numbers):
        raise ValueError("All three numbers must be less than 100.")

    return sum(numbers)


if __name__ == "__main__":
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    third = float(input("Enter the third number: "))

    total = add_three_numbers(first, second, third)
    print(f"The sum is: {total}")
