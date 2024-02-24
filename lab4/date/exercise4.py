from datetime import datetime

date1 = input("Format (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Format (YYYY-MM-DD HH:MM:SS): ")

try:
    date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    delta = date1 - date2
    x = abs(delta.total_seconds())
    print(x)
except:
    print("Invalid date format")