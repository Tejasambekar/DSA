def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n=len(nums)
    
    for i in range(n):
        min1=i
        for j in range(i+1,n):
            if nums[j]<nums[min1]:
                min1=j
        nums[i],nums[min1]=nums[min1],nums[i]
    return nums