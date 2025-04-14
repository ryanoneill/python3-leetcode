from counting_words_with_a_given_prefix import Solution

def test_ex1():
    words = ["pay","attention","practice","attend"]
    pref = "at"
    solution = Solution()
    result = solution.prefixCount(words, pref)
    assert result == 2

def test_ex2():
    words = ["leetcode","win","loops","success"]
    pref = "code"
    solution = Solution()
    result = solution.prefixCount(words, pref)
    assert result == 0
