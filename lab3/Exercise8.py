def spy_game(nums):
    li = [0,0,7]
    for x in nums:
        if(nums[x] == li[0]):
            for j in range(x,len(nums)):
                if(nums[j] == li[1]):
                    for s in range(j,len(nums)):
                        if(nums[s] == li[2]):
                            return True
                            
                

nums = input("Enter numbers: ")
nums = list(map(int,nums.split()))
if(spy_game(nums)):
    print("Pass")
else:
    print("Fail")

#NOT SOLVED!!!!!!!!!!!!!!!!