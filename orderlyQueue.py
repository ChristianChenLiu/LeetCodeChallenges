class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # if k == 1, then we can only shift and see which one gives us the best lexical order
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        #if k>1, then we can always get the lexical order
        return ''.join(sorted(s))