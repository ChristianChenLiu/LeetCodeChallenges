class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ["" for _ in range(numRows)]
        i, j = 0, 0
        down = -1
        while i < len(s):
            if i % (numRows - 1) == 0:
                down *= -1
            zigzag[j] += s[i]
            i += 1
            j += down
        return "".join(zigzag)