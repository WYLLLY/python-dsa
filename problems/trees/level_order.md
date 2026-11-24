# Binary Tree Level Order

**Trees · Medium**

## Problem

Return one list of values per depth, from root down and from left to right within each depth. An empty tree gives `[]`. Assume a finite acyclic binary tree with no shared child nodes. Do not modify it.

```python
level_order(root: TreeNode | None) -> list[list[int]]
```

A tree rooted at 3 with children 9 and 20, where 20 has children 15 and 7, gives `[[3], [9, 20], [15, 7]]`.

## Reasoning

Breadth-first search processes shallower nodes first. At each outer iteration, the current queue length counts exactly the current level. Process that many nodes and enqueue left children before right children to preserve horizontal order.

## Complexity

**Time:** O(n). **Auxiliary space:** O(w), where w is the largest level width; **output space:** O(n).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/trees/level_order.py)
- [pytest tests](../../tests/trees/test_level_order.py)
- Run: `pytest tests/trees/test_level_order.py -v`

## Attribution

Problem inspiration: [LeetCode — Binary Tree Level Order](https://leetcode.com/problems/binary-tree-level-order-traversal/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
