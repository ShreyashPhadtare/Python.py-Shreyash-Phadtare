num_students = int(input("Enter number of students: "))

total_class_score = 0

for i in range(1, num_students + 1):
    print("\nStudent", i)
    
    total = 0
    
    for j in range(1, 6):
        score = float(input("Enter score for Test " + str(j) + ": "))
        total += score
    
    average = total / 5
    print("Average score of Student", i, ":", average)
    
    total_class_score += average

class_average = total_class_score / num_students

print("\nOverall class average:", class_average)