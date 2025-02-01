from special_array_i import Solution

def test_ex1():
    nums = [1]
    solution = Solution()
    result = solution.isArraySpecial(nums)
    assert result

def test_ex2():
    nums = [2,1,4]
    solution = Solution()
    result = solution.isArraySpecial(nums)
    assert result

def test_ex3():
    nums = [4,3,1,6]
    solution = Solution()
    result = solution.isArraySpecial(nums)
    assert not result
