def has_33(nums):
    check = False
    for x in range(len(nums)):
        if(nums[x]==3):
            if(nums[x+1]==3):
                check = True
                break
    if check:
        print("Pass")
    else:
        print("Fail")


nums=input("Enter numbers: ")
nums=list(map(int,nums.split()))
has_33(nums)