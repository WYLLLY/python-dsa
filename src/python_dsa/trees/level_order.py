"""Binary Tree Level Order. See problems/trees/level_order.md."""

from collections import deque

from python_dsa.structures import TreeNode


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return binary-tree values by level, left to right."""
    if root is None:
        return []
    pending = deque([root])
    result: list[list[int]] = []
    while pending:
        level: list[int] = []
        for _ in range(len(pending)):
            node = pending.popleft()
            level.append(node.val)
            if node.left is not None:
                pending.append(node.left)
            if node.right is not None:
                pending.append(node.right)
        result.append(level)
    return result
