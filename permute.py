class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[nums[0]]]
        for num in nums[1:]:
            length = len(res[0])
            res = [returnAfterInsert(arr, i, num) for arr in res for i in range(length + 1)]
        
        return res

def returnAfterInsert(arr, i, num):
    new_array = list(arr)
    new_array.insert(i, num)
    return new_array