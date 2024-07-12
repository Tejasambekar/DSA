
def threeSum(nums):
    # n=len(nums)
    # # m=[]
    # b=set()
    # nums.sort()
    # for i in range(n-2):
    #     if i>0 and nums[i]==nums[i-1]:
    #         continue
    #     j=i+1
    #     k=n-1
    #     while j<k:
    #         s=nums[i]+nums[j]+nums[k]
            
    #         if s==0:
    #             b.add((nums[i],nums[j],nums[k]))
    #             j,k=i+1,k-1
    #             while j<k and nums[j]==nums[j-1]:
    #                 j+=1
    #             while j<k and nums[k]==nums[k+1]:
    #                 k-=1
    #         elif s>0:                        
    #             k-=1
    #         else:
    #             j+=1
    # return b
    b=set()
    n,p,z=[],[],[]
    for num in nums:
        if num>0:
            p.append(num)
        elif num<0:
            n.append(num)
        else:
            z.append(num)
    N,P=set(n),set(p)
    if z:
        for num in P:
            if -num in N:
                b.add((-num,0,num))
    if len(z)>=3:
        b.add((0,0,0))
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            target=-1*(n[i]+n[j])
            if target in P:
                b.add(tuple(sorted([n[i],n[j],target])))
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            target=-1*(p[i]+p[j])
            if target in N:
                b.add(tuple(sorted([p[i],p[j],target])))
    return b

                    
            





    

    