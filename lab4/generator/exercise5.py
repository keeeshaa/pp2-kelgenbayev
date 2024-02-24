def decreasing(n):
    while n!=-1:
        yield n
        n -= 1

n = int(input())
print(*decreasing(n), sep = ', ')