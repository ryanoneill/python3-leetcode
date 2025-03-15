from house_robber_ii import Solution

def test_ex1():
    nums = [2,3,2]
    solution = Solution()
    result = solution.rob(nums)
    assert result == 3

def test_ex2():
    nums = [1,2,3,1]
    solution = Solution()
    result = solution.rob(nums)
    assert result == 4

def test_ex3():
    nums = [1,2,3]
    solution = Solution()
    result = solution.rob(nums)
    assert result == 3

def test_ex4():
    nums = [5]
    solution = Solution()
    result = solution.rob(nums)
    assert result == 5

def test_ex5():
    nums = [0,0]
    solution = Solution()
    result = solution.rob(nums)
    assert result == 0
