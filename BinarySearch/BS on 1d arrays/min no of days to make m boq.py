def minDays(bloomDay,m,k) -> int:
    def counts(bloomDay,mid):
        c,nb=0,0
        for i in bloomDay:
            if mid>=i:
                c+=1
            else:
                nb+= c//k
                c=0
        nb+= c//k
        return nb>=m
    v=m*k
    if v>len(bloomDay):
        return -1       
    i,j=min(bloomDay),max(bloomDay)
    while i<=j:
        mid=(i+j)//2
        if counts(bloomDay,mid):
            j=mid-1
        else:
            i=mid+1
    return i

        