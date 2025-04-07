from number_of_senior_citizens import Solution


def test_ex1():
    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    solution = Solution()
    result = solution.countSeniors(details)
    assert result == 2


def test_ex2():
    details = ["1313579440F2036", "2921522980M5644"]
    solution = Solution()
    result = solution.countSeniors(details)
    assert result == 0
