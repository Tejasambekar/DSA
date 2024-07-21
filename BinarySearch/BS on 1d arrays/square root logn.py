def floorSqrt(self, x):  # Function definition for finding the floor square root of a number 'x'
    if x==1:  # If the number is 1, return 1 (special case)
        return 1
    i,j=1,x//2  # Initialize variables 'i' and 'j' for binary search range
    while i<=j:  # Loop until 'i' is less than or equal to 'j'
        mid=(i+j)//2  # Calculate the middle element of the range
        if mid*mid==x:  # If the middle element squared is equal to 'x', return the middle element
            return mid
        elif mid*mid<x:  # If the middle element squared is less than 'x', update 'i' to mid+1
            i=mid+1
        else:  # If the middle element squared is greater than 'x', update 'j' to mid-1
            j=mid-1
    return j  # Return 'j' as the floor square root of 'x'