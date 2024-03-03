filename = input("Filename: ")
with open(filename) as file:
             print(sum(1 for line in file))

