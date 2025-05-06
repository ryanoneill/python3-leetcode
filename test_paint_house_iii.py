from paint_house_iii import Solution

def test_ex1():
    houses = [0,0,0,0,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3
    solution = Solution()
    result = solution.minCost(houses, cost, m, n, target)
    assert result == 9

def test_ex2():
    houses = [0,2,1,2,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
    m = 5
    n = 2
    target = 3
    solution = Solution()
    result = solution.minCost(houses, cost, m, n, target)
    assert result == 11

def test_ex3():
    houses = [3,1,2,3]
    cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
    m = 4
    n = 3
    target = 3
    solution = Solution()
    result = solution.minCost(houses, cost, m, n, target)
    assert result == -1
