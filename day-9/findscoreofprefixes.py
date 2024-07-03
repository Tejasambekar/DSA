def findPrefixScore(nums):
    maxx=0
    for i in range(len(nums)):            
        maxx=max(maxx,nums[i])
        nums[i]+=maxx       
    for i in range(1,len(nums)):            
        nums[i]=nums[i]+nums[i-1]
    return nums
nums=[int(x) for x in input().split()]
print(findPrefixScore(nums))