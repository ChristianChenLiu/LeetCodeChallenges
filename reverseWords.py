class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #split is a method for strings that splits a string given a separator
        words = s.split(" ")
        res = ""
        for word in words:
            res += word[::-1] + " "
        #remove extra last white space
        res = res[:len(res) - 1]
        return res