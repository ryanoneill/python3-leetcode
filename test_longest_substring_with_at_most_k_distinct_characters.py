from longest_substring_with_at_most_k_distinct_characters import Solution


def test_ex1():
    s = "eceba"
    k = 2
    solution = Solution()
    result = solution.lengthOfLongestSubstringKDistinct(s, k)
    assert result == 3


def test_ex2():
    s = "aa"
    k = 1
    solution = Solution()
    result = solution.lengthOfLongestSubstringKDistinct(s, k)
    assert result == 2
