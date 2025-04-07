from vertical_order_traversal_of_a_binary_tree import Solution
from serialize_and_deserialize_binary_tree import Codec


def test_ex1():
    data = "[3,9,20,null,null,15,7]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    results = solution.verticalTraversal(root)
    assert results == [[9], [3, 15], [20], [7]]


def test_ex2():
    data = "[1,2,3,4,5,6,7]"
    codec = Codec()
    root = codec.deserialize(data)
    solution = Solution()
    results = solution.verticalTraversal(root)
    assert results == [[4], [2], [1, 5, 6], [3], [7]]
