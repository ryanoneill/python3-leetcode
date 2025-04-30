from paint_house_ii import Solution

def test_ex1():
    costs = [[1,5,3],[2,9,4]]
    solution = Solution()
    result = solution.minCostII(costs)
    assert result == 5

def test_ex2():
    costs = [[1,3],[2,4]]
    solution = Solution()
    result = solution.minCostII(costs)
    assert result == 5
