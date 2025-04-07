from longest_substring_without_repeating_characters import Solution


def test_ex1():
    s = "abcabcbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    assert result == 3


def test_ex2():
    s = "bbbbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    assert result == 1


def test_ex3():
    s = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    assert result == 3
