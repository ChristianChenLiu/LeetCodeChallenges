class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        target = sum(nums) / 2
        l, r = nums[:n], nums[n:]
        ans = float('inf')
        for k in range(n):
            right_sums = sorted(set(map(sum, combinations(r, n - k))))
            for left_sum in set(map(sum, combinations(l, k))):
                i = bisect_left(right_sums, target - left_sum)
                if i != len(right_sums):
                    ans = min(ans, abs(target - left_sum - right_sums[i]))
        return int(2 * ans)