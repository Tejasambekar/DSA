def searchMatrix( matrix, target):
    #O(log(n*m))
    n=len(matrix)
    m=len(matrix[0])
    i,j=0,m*n-1
    while i<=j:
        mid=(i+j)//2
        row=mid//m
        col=mid%m
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            i=mid+1
        else:
            j=mid-1
    return False

#O(n2)
 
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==target:
        #             return True
        # return False

#O(m+log(n))

        # def search(row,target):
        #     m=len(row)
        #     i,j=0,m-1
        #     while i<=j:
        #         mid=(i+j)//2
        #         if row[mid]==target:
        #             return True
        #         elif row[mid]<target:
        #             i=mid+1
        #         else:
        #             j=mid-1
        #     return False
        # for i in range(len(matrix)):
        #     if matrix[i][0]<=target<=matrix[i][len(matrix[0])-1]:
        #         return search(matrix[i],target)
        # return False
        
