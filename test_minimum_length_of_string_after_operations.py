from minimum_length_of_string_after_operations import Solution


def test_ex1():
    s = "abaacbcbb"
    solution = Solution()
    result = solution.minimumLength(s)
    assert result == 5


def test_ex2():
    s = "aa"
    solution = Solution()
    result = solution.minimumLength(s)
    assert result == 2
