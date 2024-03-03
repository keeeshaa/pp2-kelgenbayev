def count(str):
    upper = sum(1 for char in str if char.isupper())
    lower = sum(1 for char in str if char.islower())
    return upper, lower

str = input()
upper, lower = count(str)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
