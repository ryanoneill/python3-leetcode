from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        cache = {}
        def worker(i: int) -> int:
            if i == n:
                return 0           
            else:
                if i not in cache:
                    result = 2**32

                    current_width = 0
                    max_height = 0

                    for j in range(i, n):
                        book_width, book_height = books[j]

                        current_width += book_width
                        if current_width > shelfWidth:
                            break

                        max_height = max(max_height, book_height)
                        next_shelf = max_height + worker(j + 1)

                        result = min(result, next_shelf)
                    cache[i] = result
                return cache[i]

        return worker(0)
