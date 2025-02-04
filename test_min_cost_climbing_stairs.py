from min_cost_climbing_stairs import Solution

def test_ex1():
    cost = [10,15,20]
    solution = Solution()
    result = solution.minCostClimbingStairs(cost)
    assert result == 15

def test_ex2():
    cost = [1,100,1,1,1,100,1,1,100,1]
    solution = Solution()
    result = solution.minCostClimbingStairs(cost)
    assert result == 6
