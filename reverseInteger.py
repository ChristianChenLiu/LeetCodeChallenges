class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        
        if x >= 0:
            inverted = str(x)[::-1]
        else:
            inverted = str(x*-1)[::-1]
            neg = True
            
        if len(bin(abs(int(inverted)))[2:]) >= 32:
            return 0
        
        if neg:
            return int(inverted)*-1
        else:
            return int(inverted)
    