import re

txtfile = input()

result = re.findall(r'\b[a-z]+_[a-z]+\b', txtfile)
print(result)