from palindrome_permutation import Solution


def test_ex1():
    s = "code"
    solution = Solution()
    result = solution.canPermutePalindrome(s)
    assert not result


def test_ex2():
    s = "aab"
    solution = Solution()
    result = solution.canPermutePalindrome(s)
    assert result


def test_ex3():
    s = "carerac"
    solution = Solution()
    result = solution.canPermutePalindrome(s)
    assert result
