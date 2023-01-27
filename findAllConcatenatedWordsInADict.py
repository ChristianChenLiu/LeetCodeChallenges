class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set()
        concatenateWords = []
        for word in words:
            s.add(word)
        for word in words:
            if self.checkConcatenate(word, s) == True:
                concatenateWords.append(word)
        return concatenateWords
    def checkConcatenate(self, word: str, s: set) -> bool:
        for i in range(1, len(word)):
            prefixWord = word[:i]
            suffixWord = word[i:]
            if prefixWord in s and (suffixWord in s or self.checkConcatenate(suffixWord, s)):
                return True
        return False