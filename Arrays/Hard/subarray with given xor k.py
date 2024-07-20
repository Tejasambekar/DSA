from collections import defaultdict

def solve(A, k):

    n = len(A)  # Get the length of the array A
    xr = 0  # Initialize the XOR variable to 0
    mpp = defaultdict(int)  # Create a defaultdict to store XOR values and their frequencies
    mpp[xr] = 1  # Initialize the frequency of XOR 0 to 1
    cnt = 0  # Initialize the count variable to 0

    for i in range(n):  # Iterate through each element in the array
        xr = xr ^ A[i]  # Calculate the XOR of current element with previous XOR value
        x = xr ^ k  # Calculate the XOR value that should be present to get k
        cnt += mpp[x]  # Add the frequency of XOR value x to the count
        mpp[xr] += 1  # Increment the frequency of current XOR value

    return cnt  # Return the final count
