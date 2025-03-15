from house_robber_iv import Solution

def test_ex1():
    nums = [2,3,5,9]
    k = 2
    solution = Solution()
    result = solution.minCapability(nums, k)
    assert result == 5

def test_ex2():
    nums = [2,7,9,3,1]
    k = 2
    solution = Solution()
    result = solution.minCapability(nums, k)
    assert result == 2
