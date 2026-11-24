# Reverse Linked List

**Linked Lists · Easy**

## Problem

Given the head of a finite acyclic singly linked list, reverse its links in place and return the new head. `None` remains `None`. Reuse every node and preserve its value. The caller must not rely on the old link direction afterward; cycles are outside the contract.

```python
reverse_list(head: ListNode | None) -> ListNode | None
```

`1 -> 2 -> 3 -> None` becomes `3 -> 2 -> 1 -> None`, using the same nodes.

## Reasoning

Before each iteration, `previous` heads the reversed prefix and `current` heads the untouched suffix. Save the next link, reverse the current link, and advance both pointers. Saving the link first prevents losing the suffix. Once exhausted, the reversed prefix is the whole chain.

## Complexity

**Time:** O(n). **Auxiliary space:** O(1).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/linked_lists/reverse_list.py)
- [pytest tests](../../tests/linked_lists/test_reverse_list.py)
- Run: `pytest tests/linked_lists/test_reverse_list.py -v`

## Attribution

Problem inspiration: [LeetCode — Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
