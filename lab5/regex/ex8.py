import re

txtfile = input()

result = re.split(r'[A-Z]', txtfile)
print(result)