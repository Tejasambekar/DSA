def longestSubarray(nums):
    left=right=0
    zc=0
    maxlen=0
    while right <len(nums):
        if nums[right]==0:
            zc+=1
        if zc>1:
            if nums[left]==0:
                zc-=1
            left+=1
        maxlen=max(maxlen,right-left)
        right+=1
    return maxlen
nums=[int(x) for x in input().split()]
print(longestSubarray(nums))