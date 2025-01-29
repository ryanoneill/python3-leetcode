from tree_node import TreeNode
from binary_tree_level_order_traversal import Solution

def test_ex1():
    head = TreeNode(3)
    nine = TreeNode(9)
    head.left = nine
    twenty = TreeNode(20)
    head.right = twenty
    fifteen = TreeNode(15)
    twenty.left = fifteen
    seven = TreeNode(7)
    twenty.right = seven

    solution = Solution()
    result = solution.levelOrder(head)
    assert result == [[3],[9,20],[15,7]]

def test_ex2():
    head = TreeNode(1)
    
    solution = Solution()
    result = solution.levelOrder(head)
    assert result == [[1]]

def test_ex3():
    head = None

    solution = Solution()
    result = solution.levelOrder(head)
    assert result == []
