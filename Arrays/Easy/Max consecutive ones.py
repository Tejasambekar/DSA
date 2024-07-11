def findMaxConsecutiveOnes(nums) :
    c1=c2=0
    for j in nums:
        if j==1:
            c1+=1
        elif j==0:
            c1=0
        if c1>c2:
            c2=c1
    return c2