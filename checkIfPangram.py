class Solution(object):
    def checkIfPangram(self, sentence):
        letters_dict = {}
        # we keep track of what letters have appeared with letters_dict
        for letter in sentence:
            if letter not in letters_dict:
                letters_dict[letter] = 1

        # there are 26 english characters, if  letters_dict has at least 26 keys, then its good
        return len(letters_dict) >= 26