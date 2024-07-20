def findKRotation(self, arr):        
    i,j=0,len(arr)-1  # Initialize two pointers i and j to the start and end of the array
    ind=-1  # Initialize the index of the minimum element as -1
    ans=float('inf')  # Initialize the minimum element as positive infinity
    while i<=j:  # Loop until the pointers cross each other
        mid=(i+j)//2  # Calculate the middle index
        if arr[i]<=arr[mid]:  # If the left half of the array is sorted
            if arr[i]<ans:  # If the current element is smaller than the minimum element
                ind=i  # Update the index of the minimum element
                ans=arr[i]  # Update the minimum element
            i=mid+1  # Move the left pointer to the right half
        else:  # If the right half of the array is sorted
            if arr[mid]<arr[j]:  # If the current element is smaller than the minimum element
                ind=mid  # Update the index of the minimum element
                ans=arr[mid]  # Update the minimum element
            j=mid-1  # Move the right pointer to the left half
    return ind  # Return the index of the minimum element


# for i in range(len(arr)-1):
        #     if arr[i]>arr[i+1]:
        #         return i+1
        # return 0
