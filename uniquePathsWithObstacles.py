class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # Purpose: find # ways to go from top-left to bottom-right (with obstacles)
        # Formula: dp[j] + dp[j - 1] if no obstacle
        
        # init
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # cc
        if obstacleGrid[0][0] == 1:
            return 0
        
        # build
        dp = [0] * n
        dp[0] = 1
        
        # find 
        for i in range(m):
            
            for j in range(n):
                
                # obstacle -> no solution
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                
                # no obstacle -> like we did in Unique Path
                elif j >= 1:
                    dp[j] += dp[j - 1]
        
        # return 
        return dp[-1]