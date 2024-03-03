first = input()
final = input()

with open(first, 'r') as first1:
    with open(final, 'w') as final2:
        final2.write(first1.read())