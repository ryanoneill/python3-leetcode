from find_bottom_left_tree_value import Solution
from serialize_and_deserialize_binary_tree import Codec

def test_ex1():
    items = "[2,1,3]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.findBottomLeftValue(root)
    assert result == 1
    
def test_ex2():
    items = "[1,2,3,4,null,5,6,null,null,7]"
    codec = Codec()
    root = codec.deserialize(items)
    solution = Solution()
    result = solution.findBottomLeftValue(root)
    assert result == 7
