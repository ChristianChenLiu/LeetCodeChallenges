class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans