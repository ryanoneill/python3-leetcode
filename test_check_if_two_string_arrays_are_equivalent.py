from check_if_two_string_arrays_are_equivalent import Solution


def test_ex1():
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    solution = Solution()
    result = solution.arrayStringsAreEqual(word1, word2)
    assert result


def test_ex2():
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    solution = Solution()
    result = solution.arrayStringsAreEqual(word1, word2)
    assert not result


def test_ex3():
    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    solution = Solution()
    result = solution.arrayStringsAreEqual(word1, word2)
    assert result


def test_ex4():
    word1 = ["a"]
    word2 = ["a", "b"]
    solution = Solution()
    result = solution.arrayStringsAreEqual(word1, word2)
    assert not result
