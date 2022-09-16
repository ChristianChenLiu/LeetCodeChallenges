class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        def recur_div(a, b):
            if a < b: 
                return 0
            n = 1
            cur = b
            while cur + cur <= a:
                cur += cur
                n += n
            return n + recur_div(a-cur, b)
        
        n = recur_div(dividend, divisor)
            
        if sign: 
            return -min(2147483648, n)
        else: 
            return min(2147483647, n)