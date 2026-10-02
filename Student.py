##  Accept student name, enrollment number, course, and fee amount and display them as a formatted fee receipt.
student_name = input("Enter the student name")
enrollment_number = input("Enter the enrollment number")
course_name = input("Enter the course name")
fee_amount = input("Enter the fee amount")

print("\n+------------------------------------------------------------------------------------------+")
print("|                    fee receipt                             |")
print("+-------------------------------------------------------------------------------------------+")
print(f"| student name : {student_name:<30} |")
print(f"| enrollment number : {enrollment_number:<30} |")
print(f"| course name : {course_name:<30} |")
print(f"| fee amount : {fee_amount:<30} |")

print('+-----------------------------------------------------------------------------------------+')