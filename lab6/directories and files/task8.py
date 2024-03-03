import os

path = input()

if os.access(path, os.W_OK) and os.path.exists(path):
    os.remove(path)
    print("successfully deleted")