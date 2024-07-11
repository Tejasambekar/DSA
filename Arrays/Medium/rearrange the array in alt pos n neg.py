def rearrangeArray(nums):
       
    ans = [0] * len(nums)
    pos, neg = 0, 1

    for num in nums:
        if num < 0:
            ans[neg] = num
            neg += 2

        else:
            ans[pos] = num
            pos += 2

    return ans


