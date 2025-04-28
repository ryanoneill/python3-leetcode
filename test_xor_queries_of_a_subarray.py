from xor_queries_of_a_subarray import Solution

def test_ex1():
    arr = [1,3,4,8]
    queries = [[0,1],[1,2],[0,3],[3,3]]
    solution = Solution()
    result = solution.xorQueries(arr, queries)
    assert result == [2,7,14,8]

def test_ex2():
    arr = [4,8,2,10]
    queries = [[2,3],[1,3],[0,0],[0,3]]
    solution = Solution()
    result = solution.xorQueries(arr, queries)
    assert result == [8,0,4,4]
