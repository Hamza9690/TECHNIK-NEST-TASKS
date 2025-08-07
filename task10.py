coordinates = (5, 10, 15)
x, y, z = coordinates  

print("Unpacked Coordinates:")
print("x =", x)
print("y =", y)
print("z =", z)

a = 7
b = 3

print("\nBefore Swap:")
print("a =", a, "b =", b)

a, b = b, a  
print("After Swap:")
print("a =", a, "b =", b)