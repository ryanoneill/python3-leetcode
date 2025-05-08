from find_minimum_time_to_reach_last_room_ii import Solution

def test_ex1():
    moveTime = [[0,4],[4,4]]
    solution = Solution()
    result = solution.minTimeToReach(moveTime)
    assert result == 7

def test_ex2():
    moveTime = [[0,0,0,0],[0,0,0,0]]
    solution = Solution()
    result = solution.minTimeToReach(moveTime)
    assert result == 6

def test_ex3():
    moveTime = [[0,1],[1,2]]
    solution = Solution()
    result = solution.minTimeToReach(moveTime)
    assert result == 4
