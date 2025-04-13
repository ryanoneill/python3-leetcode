from minimum_string_length_after_removing_substrings import Solution

def test_ex1():
    s = "ABFCACDB"
    solution = Solution()
    result = solution.minLength(s)
    assert result == 2

def test_ex2():
    s = "ACBBD"
    solution = Solution()
    result = solution.minLength(s)
    assert result == 5
