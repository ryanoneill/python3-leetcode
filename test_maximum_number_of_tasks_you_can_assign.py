from maximum_number_of_tasks_you_can_assign import Solution

def test_ex1():
    tasks = [3,2,1]
    workers = [0,3,3]
    pills = 1
    strength = 1
    solution = Solution()
    result = solution.maxTaskAssign(tasks, workers, pills, strength)
    assert result == 3

def test_ex2():
    tasks = [5,4]
    workers = [0,0,0]
    pills = 1
    strength = 5
    solution = Solution()
    result = solution.maxTaskAssign(tasks, workers, pills, strength)
    assert result == 1

def test_ex3():
    tasks = [10,15,30]
    workers = [0,10,10,10,10]
    pills = 3
    strength = 10
    solution = Solution()
    result = solution.maxTaskAssign(tasks, workers, pills, strength)
    assert result == 2

def test_ex4():
    tasks = [5,9,8,5,9]       # 5,5,8,9,9
    workers = [1,6,4,2,6]     # 1,2,4,6,6
    pills = 1
    strength = 5
    solution = Solution()
    result = solution.maxTaskAssign(tasks, workers, pills, strength)
    assert result == 3
