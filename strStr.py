class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle: return 0
        
        for start in range(len(haystack) - len(needle) + 1):
            print(haystack[start: start + len(needle)])
            if haystack[start: start + len(needle)] == needle: return start
        
        return -1
                