def largestAltitude(gain):
    nums=[0]*(len(gain)+1)
    # nums.append(0)
    
    for i in range(len(nums)-1):
        nums[i+1]=gain[i]+nums[i]
        # nums[i]=0
        
    return max(nums)
gain=[-5,1,2,3,-9]
print(largestAltitude(gain))
