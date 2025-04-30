from filling_bookcase_shelves import Solution

def test_ex1():
    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelfWidth = 4
    solution = Solution()
    result = solution.minHeightShelves(books, shelfWidth)
    assert result == 6

def test_ex2():
    books = [[1,3],[2,4],[3,2]]
    shelfWidth = 6
    solution = Solution()
    result = solution.minHeightShelves(books, shelfWidth)
    assert result == 4
