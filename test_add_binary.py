from add_binary import Solution


def test_ex1():
    a = "11"
    b = "1"
    solution = Solution()
    result = solution.addBinary(a, b)
    assert result == "100"


def test_ex2():
    a = "1010"
    b = "1011"
    solution = Solution()
    result = solution.addBinary(a, b)
    assert result == "10101"
