from single_threaded_cpu import Solution

def test_ex1():
    tasks = [[1,2],[2,4],[3,2],[4,1]]
    solution = Solution()
    result = solution.getOrder(tasks)
    assert result == [0,2,3,1]

def test_ex2():
    tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
    solution = Solution()
    result = solution.getOrder(tasks)
    assert result == [4,3,2,0,1]
