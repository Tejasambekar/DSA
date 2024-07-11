def maxSubArray( nums):
    s=0
    maxi = float('-inf')
    for i in nums:
        s+=i
        if s>maxi:
            maxi = s
        if s<0:
            s=0
    return maxi