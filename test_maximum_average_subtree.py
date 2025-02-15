from maximum_average_subtree import Solution
from serialize_and_deserialize_binary_tree import Codec

def test_ex1():
    root = "[5,6,1]"
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.maximumAverageSubtree(head)
    assert result == 6.000

def test_ex2():
    root = "[0,null,1]"
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.maximumAverageSubtree(head)
    assert result == 1.000

