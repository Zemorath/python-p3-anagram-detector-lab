# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        matches = []
        for list_word in anagrams:
            if sorted(self.word) == sorted(list_word):
                matches.append(list_word)
            else:
                pass
        return matches

    