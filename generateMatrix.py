class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        r1 = 0
        r2 = n -1 
        c1 = 0
        c2 = n -1
        
        res = [[0 for i in range(n)] for i in range(n)]
        print(res)
        k = 1
        while(r1<=r2 and c1 <= c2):
            for i in range(r1,r2+1):
                res[r1][i] = k
                k+=1

            for i in range(c1+1,c2+1):
                res[i][c2]=k
                k+=1

            for i in range(r2-1,r1-1,-1):
                res[c2][i] = k
                k+=1

            for i in range(c2-1,c1,-1):
                res[i][c1] = k
                k+=1

            r1+=1
            c1+=1
            c2-=1
            r2-=1
            
        return res