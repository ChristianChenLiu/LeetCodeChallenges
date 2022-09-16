class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        mul = multipliers
        dp = [0] * (len(mul) + 1)
        for m in range(len(mul) - 1, -1, -1):
            pd = [0] * (m + 1)
            for l in range(m, -1, -1):
                pd[l] = max(dp[l + 1] + mul[m] * nums[l], 
                            dp[l] + mul[m] * nums[~(m - l)])
            dp = pd
        return dp[0]