def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(m,m+n):
        #     nums1[i]=nums2[i-m]
        # for i in range(1,m+n):
        #     key = nums1[i]        
        #     j = i-1
        #     while j >= 0 and key < nums1[j] :
        #             nums1[j + 1] = nums1[j]
        #             j -= 1
        #     nums1[j + 1] = key
        # return nums1
       
       
       
        # Merge the two sorted arrays nums1 and nums2 into nums1 in-place
        # Start from the end of nums1 and compare the elements from nums1 and nums2
        # Move the larger element to the end of nums1
        # Continue this process until all elements from nums2 are merged into nums1
        # Return the modified nums1 array

        ind = m + n - 1
        left = m - 1
        right = n - 1

        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[ind] = nums1[left]
                left -= 1
            else:
                nums1[ind] = nums2[right]
                right -= 1
            ind -= 1

        return nums1