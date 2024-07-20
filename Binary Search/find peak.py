def findPeakElement(nums):
    n = len(nums)  # Get the length of the input list

    if n == 1:  # If the list has only one element, it is the peak
        return 0

    if nums[0] > nums[1]:  # If the first element is greater than the second, it is a peak
        return 0

    if nums[n - 1] > nums[n - 2]:  # If the last element is greater than the second-to-last, it is a peak
        return n - 1

    i, j = 1, n - 2  # Set the left and right pointers for binary search

    while i <= j:  # Perform binary search until the pointers meet
        m = (i + j) // 2  # Calculate the middle index

        if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:  # If the middle element is greater than its neighbors, it is a peak
            return m

        if nums[m] > nums[m - 1]:  # If the middle element is greater than its left neighbor, move the left pointer
            i = m + 1
        else:  # If the middle element is smaller than its left neighbor, move the right pointer
            j = m - 1

    return -1  # If no peak is found, return -1


# if len(nums)<3:
        #     return nums.index(max(nums))
            
        # for i in range(1,len(nums)-1):
        #     if nums[i-1]<nums[i]>nums[i+1]:
        #         return i

            
        # return nums.index(max(nums))
