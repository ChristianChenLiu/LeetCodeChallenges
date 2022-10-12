class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # sort the array in descending order
        nums.sort(reverse = True)
        
        # start from begining to length of nums - 2
        for i in range(len(nums) - 2):
            
            # if current element is less than sum of its +2 neighbour element 
            # then return sum of these three element
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return sum(nums[i:i+3])
            
        # if the loop is complete then triangle cannot be formed so return 0
        return 0