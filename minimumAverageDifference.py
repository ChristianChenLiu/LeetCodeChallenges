class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        l_n = len(nums)
        front, back = 0, sum(nums)
        minn, min_idx = float('inf'), -1
        for i in range(len(nums)):
            x = nums[i]
            front += x
            back -= x
            if i < l_n - 1:
                x = front // (i + 1)
                y = back // (l_n - i - 1)
                val = x - y
            else:
                val = front // (i + 1)
            val = abs(val)
            if val < minn:
                minn = val
                min_idx = i
        return min_idx