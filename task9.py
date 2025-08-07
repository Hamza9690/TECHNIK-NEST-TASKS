students = ["Ali", "Sara", "John", "Ayesha", "Zain"]

print("Student Names:")
for student in students:
    print(student)

print("\nReversed List:")
for i in range(len(students)-1, -1, -1):
    print(students[i])