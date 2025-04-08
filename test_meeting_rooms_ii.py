from meeting_rooms_ii import Solution

def test_ex1():
    intervals = [[0,30],[5,10],[15,20]]
    solution = Solution()
    result = solution.minMeetingRooms(intervals)
    assert result == 2

def test_ex2():
    intervals = [[7,10],[2,4]]
    solution = Solution()
    result = solution.minMeetingRooms(intervals)
    assert result == 1

def test_ex3():
    intervals = [[10,15],[8,12],[7,11],[6,8]]
    solution = Solution()
    result = solution.minMeetingRooms(intervals)
    assert result == 3
