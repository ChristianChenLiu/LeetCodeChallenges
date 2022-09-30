class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for L, R, H in buildings:
            # append start point of building
            events.append((L, -H, R))
            # append end point of building
            events.append((R, 0, 0))
            
        # sort the event
        events.sort()
        
        # init for result and heap
        res = [[0, 0]]
        hp = [(0, float("inf"))]
        
        for pos, negH, R in events:
            # pop out building which is end
            while hp[0][1] <= pos:
                heapq.heappop(hp)
            
            # if it is a start of building, push it into heap as current building
            if negH != 0:
                heapq.heappush(hp, (negH, R))
            
            # if change in height with previous key point, append to result
            if res[-1][1] != -hp[0][0]:
                res.append([pos, -hp[0][0]])
        
        return res[1:]