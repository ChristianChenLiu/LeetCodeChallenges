class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = -1
        res = 0
        lis = [["I", 1], ["V", 5], ["X", 10], ["L", 50], ["C", 100], ["D", 500], ["M", 1000]]
        
        dic = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}
        
        for char in s[::-1]:
            if dic[char] >= last: 
                last = dic[char]
                res += lis[dic[char]][1]
            else:
                res -= lis[dic[char]][1]
                
        return res