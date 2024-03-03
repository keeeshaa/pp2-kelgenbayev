import os

def dir(path):
    dir = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return dir

def files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def all(path):
    dir = dir(path)
    files = files(path)
    return dir + files


path = input("Enter the path: ")

print(dir(path))
print(files(path))
print(all(path))

