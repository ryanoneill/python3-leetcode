from minimum_changes_to_make_alternating_binary_string import Solution

def test_ex1():
    s = "0100"
    solution = Solution()
    result = solution.minOperations(s)
    assert result == 1

def test_ex2():
    s = "10"
    solution = Solution()
    result = solution.minOperations(s)
    assert result == 0

def test_ex3():
    s = "1111"
    solution = Solution()
    result = solution.minOperations(s)
    assert result == 2
