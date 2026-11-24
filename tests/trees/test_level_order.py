from python_dsa.structures import TreeNode
from python_dsa.trees.level_order import level_order


def test_empty_tree():
    assert level_order(None) == []


def test_singleton():
    assert level_order(TreeNode(4)) == [[4]]


def test_sparse_tree_preserves_left_to_right_order_and_links():
    left = TreeNode(9)
    lower_left, lower_right = TreeNode(15), TreeNode(7)
    right = TreeNode(20, lower_left, lower_right)
    root = TreeNode(3, left, right)
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    assert root.left is left and root.right is right
    assert right.left is lower_left and right.right is lower_right


def test_deep_tree():
    root = TreeNode(0)
    node = root
    for i in range(1, 2000):
        node.right = TreeNode(i)
        node = node.right
    assert level_order(root) == [[i] for i in range(2000)]
