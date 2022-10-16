class Solution:
    def minDifficulty(self, J, d):
        if len(J) < d: return -1
        
        dp = {} # (index of day, index of the last finished job)
        for i,job in enumerate(J):
            # the base case, all jobs need to be finish in one day
            dp[0, i] = max(dp.get((0, i-1), 0), job)
            
        for i in range(1, d):
            for j in range(i, len(J)):
                mx = J[j]
                for k in range(j, i-1, -1):
                    mx = max(mx, J[k])
                    dp[i, j] = min(dp.get((i, j), float('inf')), mx + dp[i-1, k-1])
                
        return dp[d-1, len(J)-1]