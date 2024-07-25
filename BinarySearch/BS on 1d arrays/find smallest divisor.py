def smallestDivisor(nums,threshold):
    import math
    mini=float('inf')
    if threshold==len(nums):
        return max(nums)
    def suma(nums,k):
        s=0
        for i in nums:
            s+= math.ceil(i/k)
        return s
    i,j=1,max(nums)
    while i<=j:
        mid=(i+j)//2
        s=suma(nums,mid)
        if s<=threshold:
            mini=min(mini,mid)
            j=mid-1
        else:
            i=mid+1
        
    return mini



        