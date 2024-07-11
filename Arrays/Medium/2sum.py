def twoSum( nums, target):
    n=len(nums)       
    maps={}        
    for i in range(n):
        if target-nums[i] in maps:
            return [i,maps[target-nums[i]]]
        maps[nums[i]]=i
    return []