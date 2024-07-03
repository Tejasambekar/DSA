def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c=0
        left=0
        t=threshold*k
        subsum=sum(arr[:k])
        if subsum>=t:
            c+=1        
        for right in range(k,len(arr)):
            # if right-left+1>k:
            subsum-=arr[left]
            left+=1
            subsum+=arr[right]
            if subsum>=t:
                c+=1
        return c