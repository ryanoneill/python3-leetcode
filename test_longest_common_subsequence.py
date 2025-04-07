from longest_common_subsequence import Solution


def test_ex1():
    text1 = "abcde"
    text2 = "ace"
    solution = Solution()
    result = solution.longestCommonSubsequence(text1, text2)
    assert result == 3


def test_ex2():
    text1 = "abc"
    text2 = "abc"
    solution = Solution()
    result = solution.longestCommonSubsequence(text1, text2)
    assert result == 3
