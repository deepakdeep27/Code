def add_three_positive_numbers(a, b, c):
    """Add three numbers, ensuring all are positive."""
    if a < 0 or b < 0 or c < 0:
        raise ValueError("All three numbers must be positive.")
    return a + b + c


def main():
    print("Addition of 3 Positive Numbers")
    print("-" * 30)

    try:
        num1 = float(input("Enter the first positive number: "))
        num2 = float(input("Enter the second positive number: "))
        num3 = float(input("Enter the third positive number: "))

        result = add_three_positive_numbers(num1, num2, num3)
        print(f"\nThe sum of {num1}, {num2}, and {num3} is: {result}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
