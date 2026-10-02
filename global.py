num = 67 

def namespace_test():
    age = 35  

    print(f"Value of local variable age is {age}")

    print(f"Value of global variable num accessed inside the function is {num}")

namespace_test()

print(f"Value of global variable num is {num}")