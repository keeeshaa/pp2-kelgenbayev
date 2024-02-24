import math

def radian(deg):
    rad = deg * math.pi / 180
    return rad


deg = float(input("Input degree: "))
rad = radian(deg)
print("Output radian:", rad)
