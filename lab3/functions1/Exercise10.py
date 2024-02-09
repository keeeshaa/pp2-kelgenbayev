def unique(first):
    final = []
    for x in first:
        if x not in final:
            final.append(x)
    return final

first = input()
first = list(map(int,first.split()))
final = unique(first)
print(final)