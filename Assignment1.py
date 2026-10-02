print("===== CALCULATOR =====")
print("1. Basic Calculations")
print("2. Hard Calculations")

try:
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        print("\nBasic Operations:")
        print("+ Addition")
        print("- Subtraction")
        print("* Multiplication")
        print("/ Division")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            print("Invalid operator!")
            exit()

        print("\nResult =", result)

    elif choice == 2:
        print("\nHard Operations:")
        print("1. Exponentiation (**)")
        print("2. Modulus (%)")

        hard_choice = int(input("Enter your choice (1 or 2): "))

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if hard_choice == 1:
            result = num1 ** num2
            print("\nExponentiation Result =", result)

        elif hard_choice == 2:
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 % num2
            print("\nModulus Result =", result)

        else:
            print("Invalid hard calculation choice!")

    else:
        print("Invalid choice! Please enter 1 or 2.")

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("An unexpected error occurred:", e)