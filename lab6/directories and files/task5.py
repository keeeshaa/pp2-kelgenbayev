li = ["for","example"]
filename = "example.txt"

with open(filename, 'w') as file:
    file.write(' '.join(li))

print("List has been written to", filename)
