def findFloor(A,N,X):
        #Your code here
    def findFloor(A, N, X):
        # Initialize variables
        i, j = 0, N-1
        ans = -1
        
        # Binary search
        while i <= j:
            mid = (i + j) // 2
            if A[mid] <= X:
                ans = mid
                i = mid + 1
            else:
                j = mid - 1
        
        return ans
            