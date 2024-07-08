#Linear Search
def linear_search(a,k):
    n=len(a)
    for i in range(n):
        if k==a[i]:
            return i 
    return -1
a=[1,2,2,24,1,1]
k=24
print(linear_search(a,k)) 