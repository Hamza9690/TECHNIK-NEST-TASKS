marks = float(input("Enter your marks (0 - 100): "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")


password = input("Enter your password: ")
length = len(password)

if length < 6:
    print("Password strength: Weak")
elif length < 10:
    print("Password strength: Moderate")
else:
    print("Password strength: Strong")
