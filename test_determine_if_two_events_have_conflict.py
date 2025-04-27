from determine_if_two_events_have_conflict import Solution

def test_ex1():
    event1 = ["01:15", "02:00"]
    event2 = ["02:00", "03:00"]
    solution = Solution()
    result = solution.haveConflict(event1, event2)
    assert result

def test_ex2():
    event1 = ["01:00", "02:00"]
    event2 = ["01:20", "03:00"]
    solution = Solution()
    result = solution.haveConflict(event1, event2)
    assert result

def test_ex3():
    event1 = ["10:00", "11:00"]
    event2 = ["14:00", "15:00"]
    solution = Solution()
    result = solution.haveConflict(event1, event2)
    assert not result

def test_ex4():
    event1 = ["10:00", "16:00"]
    event2 = ["14:00", "15:00"]
    solution = Solution()
    result = solution.haveConflict(event1, event2)
    assert result

def test_ex5():
    event1 = ["02:00", "03:00"]
    event2 = ["01:00", "02:00"]
    solution = Solution()
    result = solution.haveConflict(event1, event2)
    assert result
