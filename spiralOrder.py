class Solution:
    def spiralOrder(self, matrix):
        arr = []
        m, n = len(matrix), len(matrix[0])
        
        def traverse(d, r1,r2,c1,c2):   
            if len(arr) == m*n:
                return 
            
            if d == "r":
                for c in range(c1,c2):
                    arr.append(matrix[r1][c])
                traverse("d",r1+1,r2,c1,c2)             # update row (lower bound)
            elif d == "d":
                for r in range(r1,r2):
                    arr.append(matrix[r][c2-1])
                traverse("l",r1,r2,c1,c2-1)             # update col (upper bound)
            elif d == "l":
                for c in range(c2-1,c1-1,-1):
                    arr.append(matrix[r2-1][c])
                traverse("u",r1,r2-1,c1,c2)           # update row (lower bound)
            else:
                for r in range(r2-1,r1-1,-1):
                    arr.append(matrix[r][c1])
                traverse("r",r1,r2,c1+1,c2)        # update col (lower bound)
                
        traverse("r",0,m,0,n)
        return arr