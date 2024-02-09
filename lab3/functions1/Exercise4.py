def filter_prime(*numbers_list):
    for i in numbers_list:
        if i == 2:
            print(2)
            continue
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)
            


numbers_str = input("Enter numbers: ")
numbers_list = list(map(int, numbers_str.split()))

filter_prime(*numbers_list)
