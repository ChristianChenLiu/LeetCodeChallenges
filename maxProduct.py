class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            current_minimum = min(prev_max * num, prev_min * num, num)
            current_maximum = max(prev_max * num, prev_min * num, num)
            global_max = max(global_max, current_maximum)
            prev_min = current_minimum
            prev_max = current_maximum
        return global_max