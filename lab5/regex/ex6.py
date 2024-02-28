import re

txtfile = input()

result = re.sub(r'[,. ]', ':', txtfile)
print(result)