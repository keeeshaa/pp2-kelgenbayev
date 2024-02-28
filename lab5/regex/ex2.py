import re

txtfile = input()

result = re.findall(r'ab{2,3}', txtfile)
print(result)