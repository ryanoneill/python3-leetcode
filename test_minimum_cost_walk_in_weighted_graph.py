from minimum_cost_walk_in_weighted_graph import Solution

def test_ex1():
    n = 5
    edges = [[0,1,7],[1,3,7],[1,2,1]]
    query = [[0,3],[3,4]]
    solution = Solution()
    results = solution.minimumCost(n, edges, query)
    assert results == [1,-1]

def test_ex2():
    n = 3
    edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
    query = [[1,2]]
    solution = Solution()
    results = solution.minimumCost(n, edges, query)
    assert results == [0]
