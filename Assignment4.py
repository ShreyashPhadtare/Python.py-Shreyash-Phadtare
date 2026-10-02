assignments = ["Python", "DBMS", "DSA"]

print("Original assignments:", assignments)

# Add a new assignment
new_assignment = input("Enter a new assignment: ")
assignments.append(new_assignment)

# Remove completed assignment
completed = input("Enter completed assignment to remove: ")

if completed in assignments:
    assignments.remove(completed)
    print("Assignment removed successfully.")
else:
    print("Assignment not found.")

# Display updated list
print("\nUpdated assignments:")
for assignment in assignments:
    print("-", assignment)