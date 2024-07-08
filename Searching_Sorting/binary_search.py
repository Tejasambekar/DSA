def binary_search(a,target):
    n=len(a)
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2        
        if target==a[mid]:
            return mid
        elif target<a[mid]:
            right=mid-1            
        else:
            left=mid+1
    return -1
a=[1,2,3,4,5,6]
k=1
print(binary_search(a,k))

