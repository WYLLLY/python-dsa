# Validate Binary Search Tree

**Trees · Medium**

## Problem

Determine whether a finite binary tree is a strict binary search tree: every left descendant is smaller and every right descendant is larger. Duplicates are invalid. Empty input is valid. Assume an acyclic tree without shared children. Values are arbitrary Python integers; input is not modified.

```python
validate_bst(root: TreeNode | None) -> bool
```

A root 5 with right child 6 whose left child is 4 is invalid: 4 violates the ancestor bound.

## Reasoning

An inorder traversal of a strict BST is strictly increasing, and conversely that ordering enforces the descendant constraints. Compare each visited value with the previous one. Use `None` for the initial absence of a previous value rather than a finite numeric sentinel.

## Complexity

**Time:** O(n). **Auxiliary space:** O(h), where h is height, O(n) worst case.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/trees/validate_bst.py)
- [pytest tests](../../tests/trees/test_validate_bst.py)
- Run: `pytest tests/trees/test_validate_bst.py -v`

## Attribution

Problem inspiration: [LeetCode — Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
