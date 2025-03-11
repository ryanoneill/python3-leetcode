from number_of_substrings_containing_all_three_characters import Solution

def test_ex1():
    s = "abcabc"
    solution = Solution()
    result = solution.numberOfSubstrings(s)
    assert result == 10

def test_ex2():
    s = "aaacb"
    solution = Solution()
    result = solution.numberOfSubstrings(s)
    assert result == 3

def test_ex3():
    s = "abc"
    solution = Solution()
    result = solution.numberOfSubstrings(s)
    assert result == 1
