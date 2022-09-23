class Solution(object):
    def countBits(self,x):
        ab = 0
        while x:
            x >>= 1
            ab += 1
        return ab
    def concatenatedBinary(self, n):
        res = 0
        mod = 10**9 + 7
        for i in range(1, n+1):
            res = ((res << self.countBits(i)) + i) % mod
        return res