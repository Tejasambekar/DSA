def rotate(nums,k):
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        k=k%len(nums)
        nums[:]=nums[n-k:]+nums[:n-k]
        return nums
nums=[1,2,3,4,5]
k=1
print(rotate(nums,k))