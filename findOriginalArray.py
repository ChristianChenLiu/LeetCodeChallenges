class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        hashmap, res = defaultdict(int), []
        for n in sorted(changed, reverse=True):
            if hashmap[n * 2]:
                hashmap[n * 2] -= 1
                res.append(n)
            else:
                hashmap[n] += 1
        if any(hashmap.values()): return []
        return res