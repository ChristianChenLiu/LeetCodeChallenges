class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        size = len(capacity)
        differenceRocks = []
        for i in range(size):
            differenceRocks.append(capacity[i] - rocks[i])
        differenceRocks.sort()

        count = 0
        index = 0
        while additionalRocks > 0 and index < size:
            if differenceRocks[index] == 0:
                count += 1
            elif differenceRocks[index] <= additionalRocks:
                additionalRocks -= differenceRocks[index]
                count += 1
            else:
                break
            index += 1

        return count
        
