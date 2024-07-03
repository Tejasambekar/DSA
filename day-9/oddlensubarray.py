def sumOddLengthSubarrays( arr):
    res=0
    n=len(arr)
    for i in range(len(arr)):
        start=n-i
        end=i+1
        tot=start*end
        odd=int(tot/2)
        if tot%2!=0:
            odd+=1
        res+=odd*arr[i]
    return res
arr=[1,2,4,5,6]
print(sumOddLengthSubarrays(arr))