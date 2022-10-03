class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0]) #row and column lengths
        l, r = 0, n*m #left and right pointers
        while l<r:
            mid = (l+r)//2 #middle
            row = mid//n #use the middle to get a row
            col = mid%n #use the middle to get a column
            num = matrix[mid//n][mid%n] #corresponding element
            if num == target: #we found the target
                return True
            elif num < target: #we need to look at bigger elements
                l = mid+1
            else: #we need to look at smaller elements
                r = mid
        return False #didn't find the target