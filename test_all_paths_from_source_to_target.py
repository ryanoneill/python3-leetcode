from all_paths_from_source_to_target import Solution


def test_ex1():
    graph = [[1, 2], [3], [3], []]
    solution = Solution()
    result = solution.allPathsSourceTarget(graph)
    result.sort()
    expected = [[0, 1, 3], [0, 2, 3]]
    expected.sort()
    assert result == expected


def test_ex2():
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    solution = Solution()
    result = solution.allPathsSourceTarget(graph)
    result.sort()
    expected = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    expected.sort()
    assert result == expected
