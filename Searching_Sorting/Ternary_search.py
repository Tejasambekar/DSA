def ternary_search(ar,target,left,right):
    if left<=right:
        mid1=left+((right-left)//3)
        mid2=right-((right-left)//3)
        if target==ar[mid1]:
            return mid1
        elif target==ar[mid2]:
            return mid2
        else:
            if target<ar[mid1]:
                return ternary_search(ar,target,left,mid1-1)
            elif target>ar[mid2]:
                return ternary_search(ar,target,mid2+1,right)
            else:
                return ternary_search(ar,target,mid1+1,mid2-1)
    return -1
n=10
ar=[1,3,5,7,9,11,13,15,17,19]
target=17
print(ternary_search(ar,target,0,n-1))



