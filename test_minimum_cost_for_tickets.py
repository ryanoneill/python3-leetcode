from minimum_cost_for_tickets import Solution

def test_ex1():
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    solution = Solution()
    result = solution.mincostTickets(days, costs)
    assert result == 11

def test_ex2():
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2,7,15]
    solution = Solution()
    result = solution.mincostTickets(days, costs)
    assert result == 17
