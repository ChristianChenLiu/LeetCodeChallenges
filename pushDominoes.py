class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = list(dominoes)
        active = set([i for i, d in enumerate(dominoes) if d != '.'])
        while active:
            nxt_active = set()
            for i in active:
                if dominoes[i] == 'L':
                    if i > 0:
                        if dominoes[i-1] == '.':
                            dominoes[i-1] = 'L'
                            nxt_active.add(i-1)
                        elif dominoes[i-1] == 'R':
                            if i-1 not in active:
                                dominoes[i-1] = '.'
                                nxt_active.remove(i-1)
                else:
                    if i < len(dominoes) - 1:
                        if dominoes[i+1] == '.':
                            dominoes[i+1] = 'R'
                            nxt_active.add(i+1)
                        elif dominoes[i+1] == 'L':
                            if i+1 not in active:
                                dominoes[i+1] = '.'
                                nxt_active.remove(i+1)
            active = nxt_active
        return "".join(dominoes)