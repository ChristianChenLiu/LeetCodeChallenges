class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) - 1
        
        while index >= 0:
            if digits[index] + 1 >= 10:
                digits[index] = 0
            else:
                digits[index] = digits[index] + 1
                return digits
            index -=1
            
        digits.insert(0, 1)
        return digits