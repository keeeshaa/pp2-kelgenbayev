import math

def area(b, h):
    A = b * h
    return A

b = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))

A = area(b, h)
print("Expected Output:", A)