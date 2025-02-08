from design_task_manager import TaskManager

def test_ex1():
    tm = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
    tm.add(4, 104, 5)
    tm.edit(102, 8)
    result = tm.execTop()
    assert result == 3
    tm.rmv(101)
    tm.add(5, 105, 15)
    result = tm.execTop()
    assert result == 5

def test_ex2():
    tm = TaskManager([[10,26,25]])
    tm.rmv(26)
    result = tm.execTop()
    assert result == -1
