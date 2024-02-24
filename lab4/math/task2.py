def area(b1, b2, h):
    area = (b1 + b2) * h / 2
    return area


h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))

A = area(b1, b2, h)
print("Expected Output:", A)
