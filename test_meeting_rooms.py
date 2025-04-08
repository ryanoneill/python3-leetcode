from meeting_rooms import Solution

def test_ex1():
    intervals = [[0,30],[5,10],[15,20]]
    solution = Solution()
    result = solution.canAttendMeetings(intervals)
    assert not result

def test_ex2():
    intervals = [[7,10],[2,4]]
    solution = Solution()
    result = solution.canAttendMeetings(intervals)
    assert result
