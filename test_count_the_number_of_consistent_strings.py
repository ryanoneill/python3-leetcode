from count_the_number_of_consistent_strings import Solution

def test_ex1():
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    solution = Solution()
    result = solution.countConsistentStrings(allowed, words)
    assert result == 2

def test_ex2():
    allowed = "abc"
    words = ["a","b","c","ab","ac","bc","abc"]
    solution = Solution()
    result = solution.countConsistentStrings(allowed, words)
    assert result == 7

def test_ex3():
    allowed = "cad"
    words = ["cc","acd","b","ba","bac","bad","ac","d"]
    solution = Solution()
    result = solution.countConsistentStrings(allowed, words)
    assert result == 4
