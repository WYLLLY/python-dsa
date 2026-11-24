"""Validate Binary Search Tree. See problems/trees/validate_bst.md."""

from python_dsa.structures import TreeNode


def validate_bst(root: TreeNode | None) -> bool:
    """Check strict global BST ordering with an iterative inorder walk."""
    stack: list[TreeNode] = []
    current = root
    previous: int | None = None
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if previous is not None and current.val <= previous:
            return False
        previous = current.val
        current = current.right
    return True
