def searchInsert(nums, target):
    n = len(nums)  # Get the length of the input list
    i, j = 0, n - 1  # Initialize two pointers, i and j, to the start and end of the list
    ans = n  # Initialize a variable ans to store the answer, initially set to the length of the list
    
    while i <= j:  # Perform binary search until i is less than or equal to j
        mid = (i + j) // 2  # Calculate the middle index
        
        if nums[mid] == target:  # If the middle element is equal to the target
            return mid  # Return the index of the middle element
        
        elif nums[mid] < target:  # If the middle element is less than the target
            i = mid + 1  # Update the start pointer to mid + 1, since the target is in the right half of the list
        
        else:  # If the middle element is greater than the target
            ans = mid  # Update the answer to the current middle index
            j = mid - 1  # Update the end pointer to mid - 1, since the target is in the left half of the list
    
    return ans  # Return the answer (index where the target should be inserted)