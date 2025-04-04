from lowest_common_ancestor_of_deepest_leaves import Solution
from serialize_and_deserialize_binary_tree import Codec

# def test_ex1():
#     items = "[3,5,1,6,2,0,8,null,null,7,4]"
#     codec = Codec()
#     root = codec.deserialize(items)
#     solution = Solution()
#     result = solution.lcaDeepestLeaves(root)
#     s = codec.serialize(result)
#     assert s == "[2,7,4]"
#
# def test_ex2():
#     items = "[1]"
#     codec = Codec()
#     root = codec.deserialize(items)
#     solution = Solution()
#     result = solution.lcaDeepestLeaves(root)
#     s = codec.serialize(result)
#     assert s == "[1]"
    
def test_ex3():
    items = "[0,1,3,null,2]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.lcaDeepestLeaves(root)
    s = codec.serialize(result)
    assert s == "[2]"


