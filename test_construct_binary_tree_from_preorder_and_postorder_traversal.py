from construct_binary_tree_from_preorder_and_postorder_traversal import Solution
from serialize_and_deserialize_binary_tree import Codec

def test_ex1():
    preorder = [1,2,4,5,3,6,7]
    postorder = [4,5,2,6,7,3,1]
    solution = Solution()
    root = solution.constructFromPrePost(preorder, postorder)
    codec = Codec()
    result = codec.serialize(root)
    assert result == "[1,2,3,4,5,6,7]"

def test_ex2():
    preorder = [1]
    postorder = [1]
    solution = Solution()
    root = solution.constructFromPrePost(preorder, postorder)
    codec = Codec()
    result = codec.serialize(root)
    assert result == "[1]"
