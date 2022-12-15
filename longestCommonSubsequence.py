class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                s1_sub = s1[:j]
                s2_sub = s2[:i]
                if s1_sub[-1] == s2_sub[-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
        