# Merge Two Sorted Lists

**Linked Lists · Easy**

## Problem

Merge two finite, acyclic, node-disjoint linked lists sorted in nondecreasing order. Return a sorted list reusing their nodes, taking nodes from the left list first on ties. Inputs are consumed: their links may change. Either head may be `None`. Sortedness, disjointness and acyclicity are preconditions, not validated at runtime.

```python
merge_sorted_lists(left: ListNode | None, right: ListNode | None) -> ListNode | None
```

`[1, 2, 4]` and `[1, 3, 4]` merge into `[1, 1, 2, 3, 4, 4]`.

## Reasoning

The next smallest remaining node must be one of the two heads. Attach the smaller one to the output tail and advance its chain. A temporary sentinel avoids a special first-node case. When one chain ends, its sorted counterpart can be attached whole.

## Complexity

**Time:** O(n + m). **Auxiliary space:** O(1); the sentinel is not included in the returned chain.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/linked_lists/merge_sorted_lists.py)
- [pytest tests](../../tests/linked_lists/test_merge_sorted_lists.py)
- Run: `pytest tests/linked_lists/test_merge_sorted_lists.py -v`

## Attribution

Problem inspiration: [LeetCode — Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
