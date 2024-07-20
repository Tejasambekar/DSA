def search(nums,target):
        # if target in nums:
        #     return True
        # else:
        #     return False
    i,j=0,len(nums)-1  # Initialize two pointers, i and j, to the start and end of the array respectively.
    while i<=j:  # Continue the loop until i is less than or equal to j.
        m=(i+j)//2  # Calculate the middle index of the array.
        if target==nums[m]:  # Check if the target element is equal to the middle element.
            return True  # If yes, return True as the target element is found.
        if nums[i]==nums[m] and nums[m]==nums[j]:  # Check if the elements at indices i, m, and j are equal.
            i+=1  # If yes, increment i by 1 and decrement j by 1 to skip duplicate elements.
            j-=1
            continue  # Continue to the next iteration of the loop.
        if nums[i]<=nums[m]:  # Check if the left half of the array is sorted.
            if nums[i]<=target<=nums[m]:  # Check if the target element lies between the left half of the array.
                j=m-1  # If yes, update j to m-1 to search in the left half of the array.
            else:
                i=m+1  # If no, update i to m+1 to search in the right half of the array.
        else:  # If the right half of the array is sorted.
            if nums[m]<=target<=nums[j]:  # Check if the target element lies between the right half of the array.
                i=m+1  # If yes, update i to m+1 to search in the right half of the array.
            else:
                j=m-1  # If no, update j to m-1 to search in the left half of the array.
    return False  # If the target element is not found, return False.