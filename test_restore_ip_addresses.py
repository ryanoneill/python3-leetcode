from restore_ip_addresses import Solution


def test_ex1():
    s = "25525511135"
    solution = Solution()
    results = solution.restoreIpAddresses(s)
    assert results == ["255.255.11.135", "255.255.111.35"]


def test_ex2():
    s = "0000"
    solution = Solution()
    results = solution.restoreIpAddresses(s)
    assert results == ["0.0.0.0"]


def test_ex3():
    s = "101023"
    solution = Solution()
    results = solution.restoreIpAddresses(s)
    assert results == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
