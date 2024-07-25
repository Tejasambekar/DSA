def findKthPositive(arr,k):
    i=0
    j=1
    while i<len(arr) and k>0:
        if arr[i]==j:
            i+=1
        else:
            k-=1
        j+=1
    if k>0:
        return j+k-1
    return j-1

        # def missing(arr):
        #     a = []
        #     for i in range(1, max(arr) + 1):
        #         if i in arr:
        #             pass
        #         else:
        #             a.append(i)            
        #     return a
        # ab = missing(arr)
        # print(ab)
        # if ab:
        #     if k > len(ab):
        #         return arr[-1] + k - len(ab)
        #     else:
        #         return ab[k - 1]
        # else:
        #     return arr[-1] + k

        
