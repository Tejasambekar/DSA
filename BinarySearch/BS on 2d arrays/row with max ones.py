def rowWithMax1s(arr):
    def rowtraversal(row):
        m=len(row)
        occ=m
        i,j=0,m-1
        while i<=j:
            mid=(i+j)//2
            if row[mid]>=1:
                occ=mid
                j=mid-1
            else:
                i=mid+1
        return occ
    maxi=0
    ind=-1
    for i in range(len(arr)):
        k=len(arr[0])-rowtraversal(arr[i])
        if k>maxi:
            maxi=k
            ind=i
    return ind
	       
	       
	   #ind=-1
	   #maxi=0
	   #for i in range(len(arr)):
	   #    c=0
	   #    for j in range(len(arr[0])):
	   #        c+=arr[i][j]
	   #    if c>maxi:
	           
	   #        maxi=c
	   #        ind=i
	   #return ind
	       