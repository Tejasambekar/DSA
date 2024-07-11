def spiralOrder( matrix):
    n=len(matrix)
    m=len(matrix[0])
    visited=[[False]*m for _ in range(n)]
    k=[]
    
    j=-1
    i=0
    c=0
    while c<(m*n):
        j+=1
        while j<m and not (visited[i][j]):    
            k.append(matrix[i][j])
            c+=1
            visited[i][j]=True
            j+=1
        
        j-=1
        i+=1
        while i<n and not visited[i][j]:
            k.append(matrix[i][j])
            c+=1
            visited[i][j]=True
            i+=1
        j-=1
        i-=1
        while j>=0 and not visited[i][j]:
            k.append(matrix[i][j])
            c+=1
            visited[i][j]=True
            j-=1
        j+=1
        i-=1
        while i>=0 and not visited[i][j]:
            k.append(matrix[i][j])  
            c+=1
            visited[i][j]=True
            i-=1
        i+=1
    return k