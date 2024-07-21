import math

def minEatingSpeed(piles, h):

    def ceils(nums, k):
        s = 0
        for i in nums:
            s += math.ceil(i / k)
        return s

    i, j = 1, max(piles)  # Initialize the lower and upper bounds for binary search
    n = len(piles)

    if n == h:  # If the number of piles is equal to the number of hours, return the maximum pile size
        return max(piles)

    while i <= j:
        mid = (i + j) // 2  # Calculate the middle value for binary search
        s = ceils(piles, mid)  # Calculate the total number of hours required to eat all piles with the current eating speed

        if s <= h:  # If the total number of hours is less than or equal to the given hours, adjust the upper bound
            j = mid - 1
        else:  # If the total number of hours is greater than the given hours, adjust the lower bound
            i = mid + 1

    return i  # Return the minimum eating speed that satisfies the given hours
