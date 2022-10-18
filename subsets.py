class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def recursion(index, path):
            if index == len(nums):
                ans.append(path)
                return
            
            recursion(index + 1, path)
            recursion(index + 1, path + [nums[index]])
        
        recursion(0,[])
        return ans