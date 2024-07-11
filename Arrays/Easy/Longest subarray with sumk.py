def lenOfLongSubarr (a, n, k) :
    maa={}
    maxlen=0
    s=0
    for i in range(n):
        s+=a[i]
        if s==k:
            maxlen=max(maxlen,i+1)
        rem=s-k
        if rem in maa:
            length=i-maa[rem]
            maxlen=max(length,maxlen)
        if s not in maa:
            maa[s]=i
    return maxlen