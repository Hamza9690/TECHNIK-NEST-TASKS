def convert_length():
    print("\nLength Converter")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = input("Choose (1/2): ")
    value = float(input("Enter the value: "))
    if choice == '1':
        print(f"{value} meters = {value * 3.281:.2f} feet")
    elif choice == '2':
        print(f"{value} feet = {value / 3.281:.2f} meters")
    else:
        print("Invalid choice!")

def convert_weight():
    print("\nWeight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose (1/2): ")
    value = float(input("Enter the value: "))
    if choice == '1':
        print(f"{value} kg = {value * 2.205:.2f} pounds")
    elif choice == '2':
        print(f"{value} pounds = {value / 2.205:.2f} kg")
    else:
        print("Invalid choice!")

def convert_temperature():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose (1/2): ")
    value = float(input("Enter the temperature: "))
    if choice == '1':
        print(f"{value}°C = {value * 9/5 + 32:.2f}°F")
    elif choice == '2':
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    else:
        print("Invalid choice!")

while True:
    print("\n=== CLI Unit Converter ===")
    print("1. Convert Length")
    print("2. Convert Weight")
    print("3. Convert Temperature")
    print("4. Exit")

    option = input("Select an option (1-4): ")

    if option == '1':
        convert_length()
    elif option == '2':
        convert_weight()
    elif option == '3':
        convert_temperature()
    elif option == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
