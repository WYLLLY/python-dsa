# Maximum Tree Depth

**Trees · Easy**

## Problem

Return the maximum number of nodes on a root-to-leaf path in a finite binary tree. The empty tree has depth zero. The tree must be acyclic with no shared child nodes. Do not modify nodes or links.

```python
maximum_depth(root: TreeNode | None) -> int
```

A root with two leaf children has depth 2; `maximum_depth(None) == 0`.

## Reasoning

Use an explicit depth-first stack of `(node, depth)` pairs. Every child has its parent depth plus one. Recording the greatest encountered depth gives the deepest path without relying on Python recursion limits.

## Complexity

**Time:** O(n). **Auxiliary space:** O(h), where h is tree height, O(n) worst case.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/trees/maximum_depth.py)
- [pytest tests](../../tests/trees/test_maximum_depth.py)
- Run: `pytest tests/trees/test_maximum_depth.py -v`

## Attribution

Problem inspiration: [LeetCode — Maximum Tree Depth](https://leetcode.com/problems/maximum-depth-of-binary-tree/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
