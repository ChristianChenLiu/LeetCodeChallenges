class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        if len(colors) <= 1: return 0
        
        last_color, max_time, time_accumulated = colors[0], neededTime[0], neededTime[0]
        
        for i, color in enumerate(colors[1:], start = 1):
            if last_color == color:
                if neededTime[i] > max_time: max_time = neededTime[i]
            else: #next color is not equal
                time_accumulated -= max_time #remove the max_time to get min time
                last_color, max_time = color, neededTime[i]
            time_accumulated += neededTime[i]
            
        return time_accumulated - max_time