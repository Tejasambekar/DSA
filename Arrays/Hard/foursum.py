def fourSum(nums,target) :
    nums.sort()
    b=[]
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,len(nums)):
            if j>i+1 and nums[j]==nums[j-1]:
                continue

            m,k=j+1,len(nums)-1
            while m<k:
                s=nums[i]+nums[j]+nums[k]+nums[m]
                if s==target:
                    b.append([nums[i],nums[j],nums[m],nums[k]])                        
                    m+=1
                    k-=1
                    
                    while m<k and nums[m]==nums[m-1]:
                        m+=1
                    while m<k and nums[k]==nums[k+1]:                        
                        k-=1
                elif s>target:
                    k-=1
                else:
                    m+=1
    return b