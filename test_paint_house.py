from paint_house import Solution

def test_ex1():
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    solution = Solution()
    result = solution.minCost(costs)
    assert result == 10

def test_ex2():
    costs = [[7,6,2]]
    solution = Solution()
    result = solution.minCost(costs)
    assert result == 2
