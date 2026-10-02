def cal(a, b):
    '''
    A python program, for basic arithmetic operations like addition, multiplication, division and subtraction.
    '''
    sum = a + b
    product = a * b
    div = a / b
    sub = a - b

    return sum, product, div, sub
s, p, d, sub = cal(20, 5)

print(f"Sum: {s}, Product: {p}, Division: {d}, Subtraction: {sub}")
print(cal.__doc__) 