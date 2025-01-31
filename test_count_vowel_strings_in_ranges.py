from count_vowel_strings_in_ranges import Solution

def test_ex1():
    words = ["aba", "bcb", "ece", "aa", "e"]
    queries = [[0,2],[1,4],[1,1]]
    solution = Solution()
    result = solution.vowelStrings(words, queries)
    assert result == [2,3,0]

def test_ex2():
    words = ["a", "e", "i"]
    queries = [[0,2],[0,1],[2,2]]
    solution = Solution()
    result = solution.vowelStrings(words, queries)
    assert result == [3,2,1]
