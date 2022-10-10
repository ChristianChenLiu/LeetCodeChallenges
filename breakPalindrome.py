class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p_len = len(palindrome)
        
        # only one char
        if p_len <= 1:
            return ""
        
        # check first half part is enough
        mid = p_len // 2
        for i in range(mid):
            # replace the first non 'a' char with 'a'
            if palindrome[i] != 'a':
                return palindrome[0:i] + 'a' + palindrome[i+1:]
        
        # replace the last char with 'b'
        return palindrome[0:p_len -1] + 'b'
        
        