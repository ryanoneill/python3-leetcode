class Solution:
    def isVowel(self, letter: str) -> bool:
        return letter in {"a", "e", "i", "o", "u"}

    def atLeastK(self, word: str, k: int) -> int:
        result = 0

        vowels = {}
        consonants = 0

        left = 0
        right = 0

        for right, letter in enumerate(word):
            if self.isVowel(letter):
                vowels[letter] = vowels.get(letter, 0) + 1
            else:
                consonants += 1

            while len(vowels) == 5 and consonants >= k:
                result += len(word) - right
                previous = word[left]
                if self.isVowel(previous):
                    vowels[previous] -= 1
                    if vowels[previous] == 0:
                        del vowels[previous]
                else:
                    consonants -= 1
                left += 1

        return result

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.atLeastK(word, k) - self.atLeastK(word, k + 1)
