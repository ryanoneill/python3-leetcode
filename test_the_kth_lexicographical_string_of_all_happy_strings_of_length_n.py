from the_kth_lexicographical_string_of_all_happy_strings_of_length_n import Solution

def test_ex1():
    n = 1
    k = 3
    solution = Solution()
    result = solution.getHappyString(n, k)
    assert result == "c"

def test_ex2():
    n = 1
    k = 4
    solution = Solution()
    result = solution.getHappyString(n, k)
    assert result == ""

def test_ex3():
    n = 3
    k = 9
    solution = Solution()
    result = solution.getHappyString(n, k)
    assert result == "cab"
