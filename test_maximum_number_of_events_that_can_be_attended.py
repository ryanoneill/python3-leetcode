from maximum_number_of_events_that_can_be_attended import Solution

def test_ex1():
    events = [[1,2],[2,3],[3,4]]
    solution = Solution()
    result = solution.maxEvents(events)
    assert result == 3

def test_ex2():
    events = [[1,2],[2,3],[3,4],[1,2]]
    solution = Solution()
    result = solution.maxEvents(events)
    assert result == 4

def test_ex3():
    events = [[1,2],[2,2],[1,2],[2,3]]
    solution = Solution()
    result = solution.maxEvents(events)
    assert result == 3

def test_ex4():
    events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
    solution = Solution()
    result = solution.maxEvents(events)
    assert result == 5

def test_ex5():
    events = [[3,3],[1,3],[2,3],[3,4],[3,4]]
    solution = Solution()
    result = solution.maxEvents(events)
    assert result == 4
