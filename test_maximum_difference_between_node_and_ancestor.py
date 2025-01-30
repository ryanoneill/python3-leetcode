from maximum_difference_between_node_and_ancestor import Solution
from serialize_and_deserialize_binary_tree import Codec

def test_ex1():
    root = "[8,3,10,1,6,null,14,null,null,4,7,13]"
    codec = Codec()
    head = codec.deserialize(root)
    solution = Solution()
    result = solution.maxAncestorDiff(head)
    assert result == 7

