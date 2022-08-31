class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        to_delete = []
        for i in range(len(nums)):
            if nums[i] == val:
                to_delete += [i]
        for index in to_delete[::-1]:
            nums.pop(index)
        return len(nums)