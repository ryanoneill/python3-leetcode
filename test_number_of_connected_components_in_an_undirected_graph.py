from number_of_connected_components_in_an_undirected_graph import Solution

def test_ex1():
    solution = Solution()
    n = 5
    edges = [[0,1],[1,2],[3,4]]
    result = solution.countComponents(n, edges)
    assert result == 2

def test_ex2():
    solution = Solution()
    n = 5
    edges = [[0,1],[1,2],[2,3],[3,4]]
    result = solution.countComponents(n, edges)
    assert result == 1

