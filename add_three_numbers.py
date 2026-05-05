def add_three_positive_numbers(a, b, c):
    """Add three positive numbers and return their sum.

    Args:
        a: First positive number.
        b: Second positive number.
        c: Third positive number.

    Returns:
        The sum of the three numbers.

    Raises:
        ValueError: If any of the numbers is not positive.
    """
    for name, value in [("a", a), ("b", b), ("c", c)]:
        if value <= 0:
            raise ValueError(f"{name} must be a positive number, got {value}")
    return a + b + c


if __name__ == "__main__":
    num1 = float(input("Enter the first positive number: "))
    num2 = float(input("Enter the second positive number: "))
    num3 = float(input("Enter the third positive number: "))

    result = add_three_positive_numbers(num1, num2, num3)
    print(f"The sum of {num1}, {num2}, and {num3} is: {result}")
