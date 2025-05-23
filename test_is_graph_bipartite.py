from is_graph_bipartite import Solution

def test_ex1():
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    solution = Solution()
    result = solution.isBipartite(graph)
    assert not result

def test_ex2():
    graph = [[1,3],[0,2],[1,3],[0,2]]
    solution = Solution()
    result = solution.isBipartite(graph)
    assert result

def test_ex3():
    graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    solution = Solution()
    result = solution.isBipartite(graph)
    assert not result

def test_ex4():
    graph = [[4],[],[4],[4],[0,2,3]]
    solution = Solution()
    result = solution.isBipartite(graph)
    assert result
