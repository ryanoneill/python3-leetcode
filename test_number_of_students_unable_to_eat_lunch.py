from number_of_students_unable_to_eat_lunch import Solution

def test_ex1():
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    solution = Solution()
    result = solution.countStudents(students, sandwiches)
    assert result == 0

def test_ex2():
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    solution = Solution()
    result = solution.countStudents(students, sandwiches)
    assert result == 3
