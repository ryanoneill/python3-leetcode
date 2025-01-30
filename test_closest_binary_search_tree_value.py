from closest_binary_search_tree_value import Solution
from serialize_and_deserialize_binary_tree import Codec
from tree_node import TreeNode

def test_ex1():
    root = "[4,2,5,1,3]"
    target = 3.714286
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.closestValue(head, target)
    assert result == 4

def test_ex2():
    root = "[1]"
    target = 4.428571
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.closestValue(head, target)
    assert result == 1
