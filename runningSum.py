class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        summed = 0
        lis = []
        
        for num in nums:
            summed += num
            lis.append(summed)
            
        return lis