from count_vowels_permutation import Solution

def test_ex1():
    n = 1
    solution = Solution()
    result = solution.countVowelPermutation(n)
    assert result == 5

def test_ex2():
    n = 2
    solution = Solution()
    result = solution.countVowelPermutation(n)
    assert result == 10

def test_ex3():
    n = 5
    solution = Solution()
    result = solution.countVowelPermutation(n)
    assert result == 68


