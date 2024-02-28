import re

txtfile = input()

result = re.findall(r'ab*', txtfile)
print(result)