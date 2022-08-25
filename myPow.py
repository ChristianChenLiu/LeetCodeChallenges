class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n
        
        #TAKES TOO LONG
        if n == 0:
            return 1
        
        result = 1
        counter = 0
        
        if n < 0:
            while counter > n:
                result /= x
                counter -= 1
        else:
            while counter < n:
                result *= x
                counter += 1
        
        return result