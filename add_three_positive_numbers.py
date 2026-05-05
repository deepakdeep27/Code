def add_three_positive_numbers(a, b, c):
    """Add three numbers, ensuring all are positive."""
    for i, val in enumerate((a, b, c), start=1):
        if val < 0:
            raise ValueError(f"Number {i} ({val}) is not positive.")
    return a + b + c


if __name__ == "__main__":
    num1 = float(input("Enter first positive number: "))
    num2 = float(input("Enter second positive number: "))
    num3 = float(input("Enter third positive number: "))

    result = add_three_positive_numbers(num1, num2, num3)
    print(f"The sum of {num1}, {num2}, and {num3} is: {result}")
