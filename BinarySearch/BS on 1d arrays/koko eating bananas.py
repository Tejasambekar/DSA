def minEatingSpeed(piles,h):
    import math
    def ceils(nums,k):
        s=0
        for i in nums:
            s+=math.ceil(i/k)
        return s

    i,j=1,max(piles)
    n=len(piles)
    if n==h:
        return max(piles)
    while i<=j:
        mid=(i+j)//2
        s=ceils(piles,mid)
        if s<=h:
            j=mid-1
            # return mid
        else:
            i=mid+1
    return i
