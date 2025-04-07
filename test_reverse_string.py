from reverse_string import Solution


def test_ex1():
    s = list("hello")
    solution = Solution()
    solution.reverseString(s)
    assert s == list("olleh")


def test_ex2():
    s = list("Hannah")
    solution = Solution()
    solution.reverseString(s)
    assert s == list("hannaH")
