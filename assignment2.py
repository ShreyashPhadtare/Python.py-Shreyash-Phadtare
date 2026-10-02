try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nBasic Calculations:")
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
        print("Modulus:", num1 % num2)
    else:
        print("Division and modulus not possible (division by zero).")

    print("\nOptional Calculations:")
    print("Exponentiation:", num1 ** num2)

except ValueError:
    print("Invalid input! Please enter numbers only.")