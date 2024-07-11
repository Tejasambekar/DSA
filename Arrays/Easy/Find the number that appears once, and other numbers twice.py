def singleNumber( nums) :
    s=sum(nums)
    k=sum(set(nums))*2
    ans=(k-s)
    return ans