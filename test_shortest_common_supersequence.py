from shortest_common_supersequence import Solution


def test_ex1():
    str1 = "abac"
    str2 = "cab"
    solution = Solution()
    result = solution.shortestCommonSupersequence(str1, str2)
    assert result == "cabac"


def test_ex2():
    str1 = "aaaaaaaa"
    str2 = "aaaaaaaa"
    solution = Solution()
    result = solution.shortestCommonSupersequence(str1, str2)
    assert result == "aaaaaaaa"
