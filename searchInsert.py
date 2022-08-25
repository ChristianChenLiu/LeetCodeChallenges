class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = binarySearch(nums,target, 0)
        
        if result >= len(nums):
            return result
        
        if nums[result] == target:
            return result
        elif nums[result] > target:
            return result
        else:
            return result + 1

def binarySearch(nums, target, index):
    if len(nums) <= 1:
        return index
    
    mid = len(nums)//2
        
    if nums[mid] == target:
        return index + mid
    elif nums[mid] > target:
        return binarySearch(nums[:mid], target, index)
    else:
        return binarySearch(nums[mid+1:], target, index + mid + 1)