from split_a_string_into_the_max_number_of_unique_substrings import Solution

def test_ex1():
    s = "ababccc"
    solution = Solution()
    result = solution.maxUniqueSplit(s)
    assert result == 5

def test_ex2():
    s = "aba"
    solution = Solution()
    result = solution.maxUniqueSplit(s)
    assert result == 2

def test_ex3():
    s = "aa"
    solution = Solution()
    result = solution.maxUniqueSplit(s)
    assert result == 1
