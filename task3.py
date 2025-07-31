name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\n--- Profile Summary ---")
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"City: {city} (Type: {type(city)})")


a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
