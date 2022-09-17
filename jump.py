class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        l,r=1,nums[0]+1
        maxx=r-1
        count=1
        while maxx<len(nums)-1:
            for i in range(l,r):
                maxx=max(maxx,i+nums[i])
            l=r
            r=maxx+1
            count+=1
        return count