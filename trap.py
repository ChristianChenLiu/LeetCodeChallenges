class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # a straight forward approach to iterative the list twice
        # essentially share the same idea with two pointers but easier to understand
        n = len(height)
        ans = 0
        # iterate from left to right
        # left_h: current max height starting from left
        # left_sum: suppose there is a "right_h" that bounds "left_h", how many rains are trapped in between [left_h, right_h] ?
        left_h, left_sum = 0, 0
        for h in(height:
            # "right_h" is found, add left_sum to ans, set "right_h" to the new "left_h"
            if h >= left_h:
                ans += left_sum
                left_h, left_sum = h, 0
            # otherwise, add water count from the current index
            else:
                left_sum += left_h - h
        
        # note that the above only calculate the water than is bounded with non-decreasing "right_bounds"
        # we now needs to calculate the water than is bounded with decreasing "right_bounds", i.e. increasing "left_bounds"
        
        # iterate from right to left
        # right_h: current max height starting from right
        # right_sum: suppose there is a "left_h" that bounds "right_h", how many rains are trapped in between [left_h, right_h] ?
        right_h, right_sum = 0, 0
        for h in(height[::-1]:
            # "left_h" is found, add right_sum to ans, set "left_h" to the new "right_h"
            if h > right_h:
                ans += right_sum
                right_h, right_sum = h, 0
            # otherwise, add water count from the current index
            else:
                right_sum += right_h - h
        return ans