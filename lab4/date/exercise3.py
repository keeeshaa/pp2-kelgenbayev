import datetime

date = datetime.datetime.now()
x = date.replace(microsecond=0)
print(x)