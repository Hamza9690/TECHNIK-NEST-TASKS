number = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table of {number}")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

limit = int(input("Enter the limit: "))
sum_div_by_3 = 0

for i in range(1, limit + 1):
    if i % 3 == 0:
        sum_div_by_3 += i

print(f"\nSum of numbers divisible by 3 from 1 to {limit} is: {sum_div_by_3}")
