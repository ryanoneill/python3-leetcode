from count_largest_group import Solution

def test_ex1():
    n = 13
    solution = Solution()
    result = solution.countLargestGroup(n)
    assert result == 4

def test_ex2():
    n = 2
    solution = Solution()
    result = solution.countLargestGroup(n)
    assert result == 2
