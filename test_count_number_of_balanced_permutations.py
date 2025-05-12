from count_number_of_balanced_permutations import Solution

def test_ex1():
    num = "123"
    solution = Solution()
    result = solution.countBalancedPermutations(num)
    assert result == 2

def test_ex2():
    num = "112"
    solution = Solution()
    result = solution.countBalancedPermutations(num)
    assert result == 1

def test_ex3():
    num = "12345"
    solution = Solution()
    result = solution.countBalancedPermutations(num)
    assert result == 0
