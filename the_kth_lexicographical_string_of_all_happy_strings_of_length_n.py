from typing import List

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def worker(items: List[str], index: int, found: int) -> (bool, List[str], int):
            if index == n:
                return (True, items, found + 1)
            else:
                for letter in "abc":
                    if index == 0 or items[index-1] != letter:
                        items.append(letter)
                        (result, response, found) = worker(items, index+1, found)
                        if result and found == k:
                            return (result, response, found)
                        items.pop()

            return (False, "", found)

        (result, response, found) = worker([], 0, 0)
        return "".join(response)
