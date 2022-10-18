class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tracked = -100000 # from constraints
        counter = 0 # to count how many we have seen of a number so far
        idx = 0 # to go through each index of nums
        
        while idx < len(nums):
            # if nums[idx] == tracked, then we increase counter + 1, and
            # might pop the nums[idx] if counter > 2
            if nums[idx] == tracked:
                counter += 1
                if counter > 2: 
                    nums.pop(idx)
                    idx -= 1
            # if nums[idx] > tracked, then we reset counter to 1 and tracked to nums[idx]
            elif nums[idx] > tracked:
                tracked = nums[idx] 
                counter = 1
            idx += 1
        
        # return the number of elements left in nums
        return len(nums)