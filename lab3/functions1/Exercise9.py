def volume(radius):
    V=4*3.14*(radius**3)/3
    return V

radius = int(input("Enter radius: "))
V = volume(radius)
print("Volume of the sphere: ", V)
