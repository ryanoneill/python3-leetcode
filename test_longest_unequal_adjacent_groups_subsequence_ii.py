from longest_unequal_adjacent_groups_subsequence_ii import Solution

def test_ex1():
    words = ["bab", "dab", "cab"]
    groups = [1,2,2]
    solution = Solution()
    result = solution.getWordsInLongestSubsequence(words, groups)
    assert result == ["bab","dab"]

def test_ex2():
    words = ["a", "b", "c", "d"]
    groups = [0,1,2,3]
    solution = Solution()
    result = solution.getWordsInLongestSubsequence(words, groups)
    assert result == ["a", "b", "c", "d"]
