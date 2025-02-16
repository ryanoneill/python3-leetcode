from convert_a_number_to_hexadecimal import Solution

def test_ex1():
    num = 26
    solution = Solution()
    result = solution.toHex(num)
    assert result == "1a"

def test_ex2():
    num = -1
    solution = Solution()
    result = solution.toHex(num)
    assert result == "ffffffff"

def test_ex3():
    num = 0
    solution = Solution()
    result = solution.toHex(num)
    assert result == "0"
