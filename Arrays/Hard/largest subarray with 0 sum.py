def maxLen(n, a):
    mpp={}
    s=0
    maxi=0
    for i in range(n):
        s+=a[i]
        if s==0:
            maxi=i+1
        else:
            if s in mpp:
                maxi=max(maxi,i-mpp[s])
            else:
                mpp[s]=i
    return maxi