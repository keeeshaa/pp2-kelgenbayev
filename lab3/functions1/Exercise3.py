def solve(numheads, numlegs):
    count_chicken = 1
    count_rabbit = numheads - count_chicken
    for i in range(numheads):
        if count_chicken*2+count_rabbit*4==numlegs:
            break
        else:
            count_chicken +=1
            count_rabbit = numheads - count_chicken
    print("Chicken: ", count_chicken)
    print("Rabbit: ", count_rabbit)
    

solve(35,94)