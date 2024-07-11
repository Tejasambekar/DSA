def majorityElement(nums):
    n=len(nums)
    k=set(nums)
    # nums=sorted(nums)
    for i in k:
        if nums.count(i)>n/2:
            return i