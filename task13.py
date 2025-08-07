import random
from datetime import datetime

random_number = random.randint(1, 100)
print(f"Random number: {random_number}")

now = datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")



def add(a, b):
    return a + b

def square(n):
    return n * n

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

import math_utils

print("Addition:", math_utils.add(3, 5))        
print("Square:", math_utils.square(4))          
print("Factorial:", math_utils.factorial(5))    
