def generate(numRows):
    # k=[]
    # def fact(n):
    #     if n==0 or n==1:
    #         return 1
    #     return n*fact(n-1)
    # def permu(n,r):
    #     return fact(n)/(fact(n-r)*fact(r))
    # for i in range(numRows):
    #     m=[]
    #     for j in range(i+1):
    #         m.append(int(permu(i,j)))
    #     k.append(m)
    # return k
    k=[]
    for i in range(numRows):
        cur=[]
        for j in range(i+1):
            if j==0 or j==i :
                cur.append(1)
            else:
                cur.append(cur[-1]*(i-j+1)//j)
        k.append(cur)
    return k