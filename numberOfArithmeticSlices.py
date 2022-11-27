class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [defaultdict(int) for _ in range(n)]
        
        for i,a in enumerate(nums):
            for j,b in enumerate(nums[:i]):
                cnt[i][a-b] += cnt[j][a-b] + 1
        
        subseq = sum(sum(cnt[i].values()) for i in range(n))        
        return subseq - n*(n-1)//2