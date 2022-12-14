class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank, v, q = set(bank), {start}, [(start, 0)]
        for g,k in q:
            for s in (g[:i] + cc + g[i+1:] for i,c in enumerate(g) for cc in 'ACGT'):
                if s in bank and s not in v:
                    if s==end:
                        return k+1
                    q.append((s, k+1))
                    v.add(s)
        return -1