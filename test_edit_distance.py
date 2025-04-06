from edit_distance import Solution

def test_ex1():
    word1 = "horse"
    word2 = "ros"
    solution = Solution()
    result = solution.minDistance(word1, word2)
    assert result == 3

def test_ex2():
    word1 = "intention"
    word2 = "execution"
    solution = Solution()
    result = solution.minDistance(word1, word2)
    assert result == 5
