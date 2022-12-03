class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        return "".join(sorted(list(s), key = lambda x: (counter[x], x), reverse = True))