class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        h = []
    
        for n in arr:
            if len(h) < k:
                heapq.heappush(h, n)
            elif abs(n-x) < abs(h[0]-x):
                heapq.heappushpop(h, n)

        return sorted(h)