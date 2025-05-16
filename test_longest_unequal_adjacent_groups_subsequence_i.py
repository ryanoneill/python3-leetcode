from longest_unequal_adjacent_groups_subsequence_i import Solution

def test_ex1():
    words = ["e", "a", "b"]
    groups = [0, 0, 1]
    solution = Solution()
    result = solution.getLongestSubsequence(words, groups)
    assert result == ["e", "b"]

def test_ex2():
    words = ["a","b","c","d"]
    groups = [1,0,1,1]
    solution = Solution()
    result = solution.getLongestSubsequence(words, groups)
    assert result == ["a", "b", "c"]
