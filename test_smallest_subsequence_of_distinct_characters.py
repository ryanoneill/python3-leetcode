from smallest_subsequence_of_distinct_characters import Solution

def test_ex1():
    s = "bcabc"
    solution = Solution()
    result = solution.smallestSubsequence(s)
    assert result == "abc"

def test_ex2():
    s = "cbacdcbc"
    solution = Solution()
    result = solution.smallestSubsequence(s)
    assert result == "acdb"
