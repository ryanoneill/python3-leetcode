from typing import List


class Solution:

    def findWords(self, words: List[str]) -> List[str]:
        results = []

        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        for word in words:
            found = -1
            result = True
            for letter in word:
                letter = letter.lower()
                if found == -1:
                    if letter in first_row:
                        found = 1
                    elif letter in second_row:
                        found = 2
                    elif letter in third_row:
                        found = 3
                    else:
                        result = False
                        break
                elif found == 1 and letter in first_row:
                    pass
                elif found == 2 and letter in second_row:
                    pass
                elif found == 3 and letter in third_row:
                    pass
                else:
                    # Doesn't match
                    result = False
                    break

            if result:
                results.append(word)

        return results
