def subarraySum(nums,k):
    c=0
    ps=0
    d={0:1}
    for num in nums:
        ps+=num
        if ps-k in d:
            c+=d[ps-k]
        if ps  in d:
            d[ps]+=1
        else:
            d[ps]=1
    return c