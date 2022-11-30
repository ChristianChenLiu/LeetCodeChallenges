class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occurrences = set()
        for freq in count.values():
            if freq in occurrences:
                return False
            occurrences.add(freq)
        return True