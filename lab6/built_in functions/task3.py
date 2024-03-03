def palindrome(s):
    return s == ''.join(reversed(s))

str = input()
if palindrome(str):
    print("yes")
else:
    print("no")
