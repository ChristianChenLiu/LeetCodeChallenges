from heapq import heapify, heappop, heappush
class Solution:
    def connectSticks(self, sticks):
        heapify(sticks)
        ret = 0
        while len(sticks) > 1:
            a = heappop(sticks)
            b = heappop(sticks)
            heappush(sticks, a+b)
            ret += a+b
        return ret