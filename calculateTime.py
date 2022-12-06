class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        startIndex = 0
        charToIndex = {}
        for i, char in enumerate(keyboard):
            charToIndex[char] = i
        totalTime = 0
        for char in word:
            totalTime += abs(startIndex - charToIndex[char]) 
            startIndex = charToIndex[char]
        return totalTime