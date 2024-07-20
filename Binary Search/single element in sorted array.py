from collections import Counter

def singleNonDuplicate(nums):
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0]!=nums[1]:
        return nums[0]
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]
    i,j=1,n-2
    while i<=j:
        m=(i+j)//2
        if nums[m-1]!=nums[m] and nums[m]!=nums[m+1]:
            return nums[m]
        if (m%2==1 and nums[m]==nums[m-1]) or (m%2==0 and nums[m]==nums[m+1]):
            i=m+1
        else:
            j=m-1
        # return -1

        # x=Counter(nums)
        # for i in x:
        #     if x[i]==1:
        #         return i
