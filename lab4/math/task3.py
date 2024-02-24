import math

def area(n, s):
    A = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return A


n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

A = area(n, s)
print("The area of the polygon is:", A)
