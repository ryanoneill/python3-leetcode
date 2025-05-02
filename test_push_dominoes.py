from push_dominoes import Solution

def test_ex1():
    dominoes = "RR.L"
    solution = Solution()
    result = solution.pushDominoes(dominoes)
    assert result == "RR.L"

def test_ex2():
    dominoes = ".L.R...LR..L.."
    solution = Solution()
    result = solution.pushDominoes(dominoes)
    assert result == "LL.RR.LLRRLL.."

def test_ex3():
    dominoes = "..R.."
    solution = Solution()
    result = solution.pushDominoes(dominoes)
    assert result == "..RRR"
