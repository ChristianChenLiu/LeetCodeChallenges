class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Fibonacci
        ans = [0, 1]
        for i in range(n):
            ans.append(ans[-1] + ans[-2])
        return ans[-1]