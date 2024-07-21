def NthRoot(n, m):
    # Function to calculate the nth root of m.
    # Parameters:
    #   - n: the root value
    #   - m: the number to calculate the root of

    if n == 1:
        # If n is 1, the result is always m.
        return m

    if m == 1:
        # If m is 1, the result is always 1.
        return 1

    i, j = 1, m // n
    # Initialize i as 1 and j as the integer division of m by n.
    # These variables will be used to define the search range.

    while i <= j:
        # Perform a binary search until i is greater than j.

        mid = (i + j) // 2
        # Calculate the middle value between i and j.

        if mid ** n == m:
            # If the middle value raised to the power of n is equal to m,
            # we have found the nth root of m.
            return mid

        if mid ** n < m:
            # If the middle value raised to the power of n is less than m,
            # update the lower bound i to mid + 1.
            i = mid + 1
        else:
            # If the middle value raised to the power of n is greater than m,
            # update the upper bound j to mid - 1.
            j = mid - 1

    # If the loop ends without finding the nth root of m, return -1.
    return -1