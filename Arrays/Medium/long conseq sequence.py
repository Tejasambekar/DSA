def longestConsecutive(nums):
    if len(nums)==0:
        return 0
    nums=set(nums)
    # c=0
    longest=1
    for i in nums:
        if i-1 not in nums:
            c=1
            x=i
            while x+1 in nums:
                x+=1
                c+=1
            longest=max(longest,c)
    return longest