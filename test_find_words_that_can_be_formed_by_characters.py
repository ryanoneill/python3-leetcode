from find_words_that_can_be_formed_by_characters import Solution


def test_ex1():
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    solution = Solution()
    result = solution.countCharacters(words, chars)
    assert result == 6


def test_ex2():
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    solution = Solution()
    result = solution.countCharacters(words, chars)
    assert result == 10
