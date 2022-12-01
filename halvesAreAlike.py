class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return vowelCounter(s[:len(s)//2]) == vowelCounter(s[len(s)//2:])


def vowelCounter(s):
    vowels = {'a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"}
    counter = 0
    for ch in s: 
        if ch in vowels: counter += 1
    return counter