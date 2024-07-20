def findMin(nums):
    i, j = 0, len(nums) - 1
    mini = float('inf')  # Initialize the minimum value as positive infinity
    while i <= j:
        mid = (i + j) // 2  # Calculate the middle index
        if nums[i] < nums[j]:  # If the array is already sorted, the minimum is at index i
            mini = min(mini, nums[i])  # Update the minimum value
            break  # Exit the loop
        if nums[i] <= nums[mid]:  # If the left half is sorted
            mini = min(mini, nums[i])  # Update the minimum value
            i = mid + 1  # Move the left pointer to mid + 1
        else:  # If the right half is sorted
            mini = min(mini, nums[mid])  # Update the minimum value
            j = mid - 1  # Move the right pointer to mid - 1

    return mini  # Return the minimum value
