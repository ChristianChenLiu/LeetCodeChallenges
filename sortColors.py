class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        mid=0
        r=len(nums)-1
        while(mid<=r):
            if nums[mid] == 0:
                nums[mid], nums[l] = nums[l], nums[mid]
                mid+=1
                l+=1
            elif nums[mid] == 2:
                nums[mid], nums[r] = nums[r], nums[mid]
                r-=1
            else:
                mid+=1