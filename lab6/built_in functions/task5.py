def true(tup):
    return all(tup)

tuple = (True, False, True, True)

if true(tuple):
    print("Yes")
else:
    print("No")

