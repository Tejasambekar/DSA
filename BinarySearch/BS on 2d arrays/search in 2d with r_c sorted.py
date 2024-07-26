
def searchMatrix( matrix, target):
    # n=len(matrix)
    # m=len(matrix[0])
    # def eachrow(arr,target):
    #     k=len(arr)
    #     i,j=0,k-1
    #     while i<=j:
    #         mid=(i+j)//2
    #         if arr[mid]==target:
    #             return True
    #         elif arr[mid]<target:
    #             i=mid+1
    #         else:
    #             j=mid-1
    #     return False
    # def eachcol(arr,target):
    #     k=len(arr)
    #     i,j=0,k-1
    #     while i<=j:
    #         mid=(i+j)//2
    #         if arr[mid]==target:
    #             return True
    #         elif arr[mid]<target:
    #             i=mid+1
    #         else:
    #             j=mid-1
    #     return False

    # for i in range(len(matrix)):
    #     h=eachrow(matrix[i],target)
    #     h=eachcol(matrix[:][i],target)
    #     if h:
    #         return True
    
    # return False
    row,col=0,len(matrix[0])-1
    while (row<=(len(matrix)-1) and col>=0):
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            row+=1
        else:
            col-=1
    return False


       
       