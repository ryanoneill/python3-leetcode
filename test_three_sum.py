from three_sum import Solution

def test_ex1():
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum(nums)
    assert result == [[-1,-1,2], [-1,0,1]]

def test_ex2():
    nums = [0, 1, 1]
    solution = Solution()
    result = solution.threeSum(nums)
    assert result == []

def test_ex3():
    nums = [0, 0, 0]
    solution = Solution()
    result = solution.threeSum(nums)
    assert result == [[0,0,0]]

def test_ex4():
    nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    solution = Solution()
    result = solution.threeSum(nums)
    assert result == [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]
