from minimum_time_to_repair_cars import Solution

def test_ex1():
    ranks = [4,2,3,1]
    cars = 10
    solution = Solution()
    result = solution.repairCars(ranks, cars)
    assert result == 16

def test_ex2():
    ranks = [5,1,8]
    cars = 6
    solution = Solution()
    result = solution.repairCars(ranks, cars)
    assert result == 16
