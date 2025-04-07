from count_substrings_with_only_one_distinct_letter import Solution


def test_ex1():
    s = "aaaba"
    solution = Solution()
    result = solution.countLetters(s)
    assert result == 8


def test_ex2():
    s = "aaaaaaaaaa"
    solution = Solution()
    result = solution.countLetters(s)
    assert result == 55
