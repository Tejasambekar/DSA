def missing(nums):
    n=len(nums)
    s=(n*(n+1)/2)
    k=sum(nums)
    return s-k 
print(missing([1,2,0,3]))