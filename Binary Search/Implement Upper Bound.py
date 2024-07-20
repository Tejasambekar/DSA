def getFloorAndCeil(A, n, x):
    A.sort()  # Sort the array in ascending order
    i, j = 0, n-1  # Initialize two pointers, i and j, to the start and end of the array
    floor, ceil = -1, -1  # Initialize floor and ceil variables to -1
    while i <= j:  # Loop until i is less than or equal to j
        mid = (i + j) // 2  # Calculate the middle index
        if A[mid] == x:  # If the middle element is equal to x
            return [arr[mid], arr[mid]]  # Return a list with the middle element as both floor and ceil
        if A[mid] < x:  # If the middle element is less than x
            floor = A[mid]  # Update the floor variable to the middle element
            i = mid + 1  # Move the left pointer to mid + 1
        else:  # If the middle element is greater than x
            ceil = A[mid]  # Update the ceil variable to the middle element
            j = mid - 1  # Move the right pointer to mid - 1
    return [floor, ceil]  # Return a list with the floor and ceil values