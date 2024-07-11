def rotate(matrix):
        
    n=len(matrix)
    for i in range(n):
        for j in range(0,i+1):
            if i!=j:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for i in range(n):
        matrix[i]=reversed(matrix[i])
    return matrix