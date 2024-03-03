import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("Path exists.")
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("Path does not exist.")
