def add_three_positive_numbers(a, b, c):
    """Add three numbers after ensuring they are positive."""
    for name, value in [("a", a), ("b", b), ("c", c)]:
        if value < 0:
            raise ValueError(f"{name} must be a positive number, got {value}")
    return a + b + c


def main():
    print("Addition of 3 Positive Numbers")
    print("-" * 30)

    numbers = []
    for i in range(1, 4):
        while True:
            try:
                num = float(input(f"Enter positive number {i}: "))
                if num < 0:
                    print("Please enter a positive number.")
                    continue
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    result = add_three_positive_numbers(*numbers)
    print(f"\nThe sum of {numbers[0]}, {numbers[1]}, and {numbers[2]} is: {result}")


if __name__ == "__main__":
    main()
