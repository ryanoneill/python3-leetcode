from time_needed_to_buy_tickets import Solution


def test_ex1():
    tickets = [2, 3, 2]
    k = 2
    solution = Solution()
    result = solution.timeRequiredToBuy(tickets, k)
    assert result == 6


def test_ex2():
    tickets = [5, 1, 1, 1]
    k = 0
    solution = Solution()
    result = solution.timeRequiredToBuy(tickets, k)
    assert result == 8
