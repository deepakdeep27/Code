"""Script to add three positive numbers."""


def add_three_positive_numbers(a, b, c):
    """Add three positive numbers and return the result.

    Args:
        a: First positive number.
        b: Second positive number.
        c: Third positive number.

    Returns:
        The sum of the three numbers.

    Raises:
        ValueError: If any of the numbers is not positive.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All numbers must be positive.")
    return a + b + c


if __name__ == "__main__":
    num1 = float(input("Enter the first positive number: "))
    num2 = float(input("Enter the second positive number: "))
    num3 = float(input("Enter the third positive number: "))

    result = add_three_positive_numbers(num1, num2, num3)
    print(f"The sum of {num1}, {num2}, and {num3} is: {result}")
