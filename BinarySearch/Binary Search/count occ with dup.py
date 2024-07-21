def count(nums, n, target):
    def search(nums, n, left):
        i, j = 0, len(nums) - 1
        hehe = -1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                hehe = mid
                if left:
                    j = mid - 1
                else:
                    i = mid + 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return hehe

    # Find the first occurrence of the target
    first = search(nums, target, True)

    # Find the last occurrence of the target
    last = search(nums, target, False)

    if first == -1:
        return 0

    # Return the count of occurrences of the target
    return last - first + 1


	   # def fsoc(arr,n,x):
	   #     i,j=0,len(arr)-1
    # 	    c=0
    # 	    fs=-1
    # 	    while i<=j:
    # 	        m=(i+j)//2
    # 	        if arr[m]==x:
    # 	            fs=m
    # 	            j=m-1
    # 	        elif arr[m]<x:
    # 	            i=m+1
    # 	        else:
    # 	            j=m-1
    # 	    return fs
    # 	def lsoc(arr,n,x):
	   #     i,j=0,len(arr)-1
    # 	    c=0
    # 	    ls=-1
    # 	    while i<=j:
    # 	        m=(i+j)//2
    # 	        if arr[m]==x:
    # 	            ls=m
    # 	            i=m+1
    # 	        elif arr[m]<x:
    # 	            i=m+1
    # 	        else:
    # 	            j=m-1
    # 	    return ls
    # 	def firstAndLastPosition(arr, n, x):
    #         first = fsoc(arr, n, x)
    #         if first == -1:
    #             return (-1, -1)
    #         last = lsoc(arr, n, x)
    #         return (first, last)
    #     first, last = firstAndLastPosition(arr, n, x)
    #     if first == -1:
    #         return 0
    #     return last - first + 1
    
    	    
	   # a=Counter(arr)
	   # return a[x]