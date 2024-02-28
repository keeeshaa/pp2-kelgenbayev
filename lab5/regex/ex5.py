import re

txtfile = input()

result = re.findall(r'a.*b', txtfile)
print(result)