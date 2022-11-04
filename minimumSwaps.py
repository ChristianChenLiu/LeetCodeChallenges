class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        #We find the smallest leftmost and largest rightmost element index
        min_num = 1000000
        max_num = -1
        min_num_idx = -1
        max_num_idx = -1
        for i, num in enumerate(nums):
            if num >= max_num:
                max_num_idx = i
                max_num = num

            if num < min_num:
                min_num_idx = i
                min_num = num
        
        #Two cases:
        #1. Smallest rightmost element is to the left of the largest rightmost element
        #Then, when we either start moving the smallest or largest element to their
        #desired position in the extremes, they will cross over, thus moving the 
        #other element 1 position closer to its respective extreme. Hence, we just
        #need to calculate the number of steps they need to take to reach the extremes
        #minus 1 from the help in the cross over.
        if min_num_idx > max_num_idx:
            return min_num_idx + (len(nums) - 1 - max_num_idx) - 1

        #2. Smallest rightmost element is to the right of the largest rightmost element
        #Then, they would never cross over when moving either one to their desired
        #position in the extremes. Hence we just calculate the number of steps they
        #need to take to reach the extremes.
        return min_num_idx + (len(nums) - 1 - max_num_idx)


