class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        p = range(n)
        def find(v):
            if p[v] != v:
                p[v] = find(p[v])
            return p[v]
        for v, w in edges:
            p[find(v)] = find(w)
        return len(set(map(find, p)))