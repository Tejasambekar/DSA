'''Given an array nums, return true if the array was 
originally sorted in non-decreasing order,
then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length
 such that A[i] == B[(i+x) % A.length], where % is the modulo operation.'''

def check( nums):
    c=0
    for i in range(len(nums)):
        if nums[i]>(nums[(i+1)%len(nums)]):
            c+=1
        if c>1:
            return False
    return c<=1
nums=[3,4,5,6,2,7]
print(check(nums))