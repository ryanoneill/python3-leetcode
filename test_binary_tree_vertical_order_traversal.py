from binary_tree_vertical_order_traversal import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    data = "[3,9,20,null,null,15,7]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.verticalOrder(root)
    assert result == [[9], [3, 15], [20], [7]]


def test_ex2():
    data = "[3,9,8,4,0,1,7]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.verticalOrder(root)
    assert result == [[4], [9], [3, 0, 1], [8], [7]]


def test_ex3():
    data = "[1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    result = solution.verticalOrder(root)
    assert result == [[4], [2, 5], [1, 10, 9, 6], [3], [11]]
