def findTwoElement( arr, n): 
        
        # Calculate the sum of numbers from 1 to n
        sn = n * (n + 1) // 2

        # Calculate the sum of squares of numbers from 1 to n
        s2n = (n * (2 * n + 1) * (n + 1)) // 6

        # Initialize variables for sum and sum of squares
        s, s2 = 0, 0

        # Calculate the sum and sum of squares of the given array
        for i in range(n):
            s += arr[i]
            s2 += arr[i] * arr[i]

        # Calculate the missing numbers
        v1 = s - sn
        v2 = s2 - s2n
        v2 = v2 // v1
        x = (v1 + v2) // 2
        y = (v2 - v1) // 2

        # Return the missing numbers as a list
        return [x, y]
        
        # count=Counter(arr)
        # for i in count:
        #     if count[i]==2:
        #         v=i
        #         break
                
            
        # n=len(arr)    
        # sol=n*(n+1)//2
        # arr=set(arr)
        # sol=sol-sum(arr)

        # return v,sol