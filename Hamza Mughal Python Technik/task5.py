weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))


principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest is:", round(simple_interest, 2))
