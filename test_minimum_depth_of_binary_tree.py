from tree_node import TreeNode
from minimum_depth_of_binary_tree import Solution
from serialize_and_deserialize_binary_tree import Codec

def test_ex1():
    root = "[3,9,20,null,null,15,7]"
    codec = Codec()
    head = codec.deserialize(root)

    solution = Solution()
    result = solution.minDepth(head)
    assert result == 2

def test_ex2():
    root = "[2,null,3,null,4,null,5,null,6]"
    codec = Codec()
    head = codec.deserialize(root)

    solution = Solution()
    result = solution.minDepth(head)
    assert result == 5

