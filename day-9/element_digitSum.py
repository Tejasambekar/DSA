def differenceOfSum(nums):
    ele_sum=sum(nums)
    b=sum([int(digit) for num in nums for digit in str(num)])
    return abs(b-ele_sum)
nums=[1,2,3,34]
print(differenceOfSum(nums))