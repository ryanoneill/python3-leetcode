from cheapest_flights_within_k_stops import Solution

def test_ex1():
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    solution = Solution()
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert result == 700

def test_ex2():
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    solution = Solution()
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert result == 200

def test_ex3():
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    solution = Solution()
    result = solution.findCheapestPrice(n, flights, src, dst, k)
    assert result == 500
