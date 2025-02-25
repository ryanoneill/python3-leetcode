from monotonic_array import Solution

def test_ex1():
    nums = [1,2,2,3]
    solution = Solution()
    result = solution.isMonotonic(nums)
    assert result

def test_ex2():
    nums = [6,5,4,4]
    solution = Solution()
    result = solution.isMonotonic(nums)
    assert result

def test_ex3():
    nums = [1,3,2]
    solution = Solution()
    result = solution.isMonotonic(nums)
    assert not result

def test_ex4():
    nums = [1,1,1,1]
    solution = Solution()
    result = solution.isMonotonic(nums)
    assert result
