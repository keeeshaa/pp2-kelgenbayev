def to_centigrade(F):
    C = (5 / 9) * (F - 32)
    print("In centigrade: ", C)


F = int(input("In Fahrenheit: "))
to_centigrade(F)