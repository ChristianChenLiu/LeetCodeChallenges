class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        long_str = ''
        max_len = 0
        #iterate through every char. and find max_substring where ith element is at center
        for i in range(len(s)): 
            # for odd substring
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if max_len < r-l+1:
                    max_len = r-l+1
                    long_str = s[l:r+1]
                l -=1
                r += 1
            
            # for even substring
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if max_len < r-l+1:
                    max_len = r-l+1
                    long_str = s[l:r+1]
                l -=1
                r += 1
        
        return long_str