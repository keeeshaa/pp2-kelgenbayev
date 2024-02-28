import re

txtfile = input()

result = re.findall(r'[A-Z][a-z]+', txtfile)
print(result)