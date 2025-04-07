from typing import Set, List


class Solution:
    def digit_to_letters(self, digit: str) -> Set[str]:
        if digit == "2":
            return {"a", "b", "c"}
        elif digit == "3":
            return {"d", "e", "f"}
        elif digit == "4":
            return {"g", "h", "i"}
        elif digit == "5":
            return {"j", "k", "l"}
        elif digit == "6":
            return {"m", "n", "o"}
        elif digit == "7":
            return {"p", "q", "r", "s"}
        elif digit == "8":
            return {"t", "u", "v"}
        elif digit == "9":
            return {"w", "x", "y", "z"}
        return set()

    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        for digit in digits:
            letters = self.digit_to_letters(digit)
            if results == []:
                results = list(letters)
            else:
                original = results
                results = []
                for letter in letters:
                    for orig in original:
                        results.append(orig + letter)

        return results
