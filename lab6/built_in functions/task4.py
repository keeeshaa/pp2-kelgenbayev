import time
import math

def func(num, ms):
    time.sleep(ms / 1000)
    return math.sqrt(num)

num = int(input("Number: "))
ms = int(input("Time: "))

sqrt = func(num, ms)
print(f"Square root of {num} after {ms} milliseconds is {sqrt}")