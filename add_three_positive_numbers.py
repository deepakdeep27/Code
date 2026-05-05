def add_three_positive_numbers(a: float, b: float, c: float) -> float:
    """Return the sum of three positive numbers.

    Args:
        a: First positive number.
        b: Second positive number.
        c: Third positive number.

    Returns:
        The sum of a, b, and c.

    Raises:
        ValueError: If any argument is not positive.
    """
    for name, value in [("a", a), ("b", b), ("c", c)]:
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}")
    return a + b + c


if __name__ == "__main__":
    x = float(input("Enter first positive number: "))
    y = float(input("Enter second positive number: "))
    z = float(input("Enter third positive number: "))
    print(f"Sum: {add_three_positive_numbers(x, y, z)}")
