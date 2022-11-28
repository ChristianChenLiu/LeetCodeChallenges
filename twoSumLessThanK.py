class Solution:
    def twoSumLessThanK(self, nums, k, m = -1):
        
        nums.sort()
		
        l, r = 0, len(nums)-1
        while l < r:
            s = nums[l] + nums[r]               # compute the sum and compare it to the target 'k':
            if s >= k : r -= 1                  # - if larger or equal, try a smaller element from the right;
            else      : l, m = l+1, max(m, s)   # - if smaller, update max & try a larger element from the left.
            
        return m