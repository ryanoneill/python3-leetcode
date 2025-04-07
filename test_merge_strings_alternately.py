from merge_strings_alternately import Solution


def test_ex1():
    word1 = "abc"
    word2 = "pqr"
    solution = Solution()
    result = solution.mergeAlternately(word1, word2)
    assert result == "apbqcr"


def test_ex2():
    word1 = "ab"
    word2 = "pqrs"
    solution = Solution()
    result = solution.mergeAlternately(word1, word2)
    assert result == "apbqrs"


def test_ex3():
    word1 = "abcd"
    word2 = "pq"
    solution = Solution()
    result = solution.mergeAlternately(word1, word2)
    assert result == "apbqcd"
