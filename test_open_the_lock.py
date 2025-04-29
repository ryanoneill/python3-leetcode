from open_the_lock import Solution

def test_ex1():
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    solution = Solution()
    result = solution.openLock(deadends, target)
    assert result == 6

def test_ex2():
    deadends = ["8888"]
    target = "0009"
    solution = Solution()
    result = solution.openLock(deadends, target)
    assert result == 1

def test_ex3():
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"
    solution = Solution()
    result = solution.openLock(deadends, target)
    assert result == -1
