class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 1
        num = nums[0]
        length = len(nums)
        while (index < length):
            if nums[index] <= num:
                del nums[index]
                length -= 1
            else:
                num = nums[index]
                index += 1
        
        return length