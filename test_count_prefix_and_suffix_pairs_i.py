from count_prefix_and_suffix_pairs_i import Solution

def test_ex1():
    words = ["a","aba","ababa","aa"]
    solution = Solution()
    result = solution.countPrefixSuffixPairs(words)
    assert result == 4

def test_ex2():
    words = ["pa","papa","ma","mama"]
    solution = Solution()
    result = solution.countPrefixSuffixPairs(words)
    assert result == 2

def test_ex3():
    words = ["abab","ab"]
    solution = Solution()
    result = solution.countPrefixSuffixPairs(words)
    assert result == 0
