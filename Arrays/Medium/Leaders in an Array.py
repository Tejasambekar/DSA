def leaders(n, arr):
    k=[]
    m=[]
    maxi= arr[-1]
    k.append(arr[n-1])
    for i in range(n-2,-1,-1):
        if arr[i]>=maxi:
            k.append(arr[i])
            maxi=arr[i]
    return reversed(k)