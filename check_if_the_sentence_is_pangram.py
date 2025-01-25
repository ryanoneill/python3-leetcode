from string import ascii_lowercase

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        result = True
        letters = set()
        for letter in sentence:
            letters.add(letter)
        for letter in ascii_lowercase:
            if letter not in letters:
                result = False
                break
        return result

