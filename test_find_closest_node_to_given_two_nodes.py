from find_closest_node_to_given_two_nodes import Solution

def test_ex1():
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
    solution = Solution()
    result = solution.closestMeetingNode(edges, node1, node2)
    assert result == 2

def test_ex2():
    edges = [1,2,-1]
    node1 = 0
    node2 = 2
    solution = Solution()
    result = solution.closestMeetingNode(edges, node1, node2)
    assert result == 2

def test_ex3():
    edges = [4,4,8,-1,9,8,4,4,1,1]
    node1 = 5
    node2 = 6
    solution = Solution()
    result = solution.closestMeetingNode(edges, node1, node2)
    assert result == 1
