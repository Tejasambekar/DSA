def searchRange(nums,target):
        # if target in nums:
        #     n=len(nums)
        #     m=nums.index(target)
        #     nums[:]=nums[::-1]
        #     k=nums.index(target)
        #     return [m,n-k-1]
        # else:
        #     return [-1,-1]
        
        # def frst(nums,target):
        #     i,j=0,len(nums)-1
        #     frst=-1
        #     while i<=j:
        #         mid=(i+j)//2
        #         if nums[mid]==target:
        #             frst=mid
        #             j=mid-1
        #         elif nums[mid]<target:
        #             i=mid+1
        #         else:
        #             j=mid-1
        #     return frst
        # def last(nums,target):
        #     # n=len(nums)
        #     i,j=0,len(nums)-1
        #     last=-1
        #     while i<=j:
        #         mid=(i+j)//2
        #         if nums[mid]==target:
        #             last=mid
        #             i=mid+1
        #         elif nums[mid]<target:
        #             i=mid+1
        #         else:
        #             j=mid-1
        #     return last
        # first=frst(nums,target)
        # last=last(nums,target)
        # return [first,last]
    def seach(nums,target,left):
        i,j=0,len(nums)-1
        hehe=-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                hehe=mid
                if left:
                    j=mid-1
                else:
                    i=mid+1
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return hehe
    first=seach(nums,target,True)  # Find the first occurrence of the target element in the nums list.
    last=seach(nums,target,False)  # Find the last occurrence of the target element in the nums list.
    return [first,last]  # Return the indices of the first and last occurrence of the target element in the nums list.