class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s2 = " ".join(s.split())
        counter = 0
        max_counter = 0
        for char in s2:
            if char == " ":
                counter = 0
            else:
                counter += 1
                if counter > max_counter:
                    max_counter = counter
        
        return max_counter