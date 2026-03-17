def add_three_numbers(a, b, c):
    return a + b + c


if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = float(input("Enter third number: "))

    result = add_three_numbers(x, y, z)
    print("Sum:", result)
