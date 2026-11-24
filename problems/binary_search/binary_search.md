# Binary Search

**Binary Search · Easy**

## Problem

Given a strictly increasing integer list, return the index of `target`, or `-1` when absent. Empty input is allowed. Sortedness and distinctness are preconditions and are not checked, preserving logarithmic time.

```python
binary_search(nums: list[int], target: int) -> int
```

`binary_search([-1, 0, 3, 5, 9, 12], 9) == 4`.

## Reasoning

Maintain the half-open candidate range `[left, right)`. Comparing the middle value with the target rules out half of that range. Exact equality returns the index; an empty candidate range proves absence.

## Complexity

**Time:** O(log n) for nonempty input, O(1) for empty input. **Auxiliary space:** O(1).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/binary_search/binary_search.py)
- [pytest tests](../../tests/binary_search/test_binary_search.py)
- Run: `pytest tests/binary_search/test_binary_search.py -v`

## Attribution

Problem inspiration: [LeetCode — Binary Search](https://leetcode.com/problems/binary-search/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
