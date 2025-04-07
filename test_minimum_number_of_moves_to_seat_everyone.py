from minimum_number_of_moves_to_seat_everyone import Solution


def test_ex1():
    seats = [3, 1, 5]
    students = [2, 7, 4]
    solution = Solution()
    result = solution.minMovesToSeat(seats, students)
    assert result == 4


def test_ex2():
    seats = [4, 1, 5, 9]
    students = [1, 3, 2, 6]
    solution = Solution()
    result = solution.minMovesToSeat(seats, students)
    assert result == 7


def test_ex3():
    seats = [2, 2, 6, 6]
    students = [1, 3, 2, 6]
    solution = Solution()
    result = solution.minMovesToSeat(seats, students)
    assert result == 4


def test_ex4():
    seats = [12, 14, 19, 19, 12]
    students = [19, 2, 17, 20, 7]
    solution = Solution()
    result = solution.minMovesToSeat(seats, students)
    assert result == 19
