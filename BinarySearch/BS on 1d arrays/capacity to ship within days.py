def shipWithinDays(weights,days) :
    def check(weights,cap):
        l=0
        n=len(weights)
        d=1
        for i in range(n):
            if l+weights[i]>cap:
                d+=1
                l=weights[i]
            else:
                l+=weights[i]
        return d
    i,j=max(weights),sum(weights)        
    while i<=j:
        m=(i+j)//2
        d=check(weights,m)
        if d<=days:
            j=m-1
        else:
            i=m+1
    return i