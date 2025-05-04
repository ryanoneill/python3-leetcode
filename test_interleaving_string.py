from interleaving_string import Solution

def test_ex1():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    solution = Solution()
    result = solution.isInterleave(s1, s2, s3)
    assert result

def test_ex2():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    solution = Solution()
    result = solution.isInterleave(s1, s2, s3)
    assert not result

def test_ex3():
    s1 = ""
    s2 = ""
    s3 = ""
    solution = Solution()
    result = solution.isInterleave(s1, s2, s3)
    assert result

