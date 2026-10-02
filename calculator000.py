num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
op = int(input("Enter the operation to be performed 1.Addition 2.Subtraction 3.Multiplication 4.Division: "))

if op == 1:
    result = num1 + num2
    print("The sum of",num1,"and",num2,"is:",result)    
elif op == 2:
    result = num1 - num2
    print("The difference of",num1,"and",num2,"is:",result)
elif op == 3:
    result = num1 * num2
    print("The product of",num1,"and",num2,"is:",result)
elif op == 4:
    if num2 != 0:
        result = num1 / num2
        print("The quotient of",num1,"and",num2,"is:",result)
    else:
        print("Error: Division by zero is not allowed.")