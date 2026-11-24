# Search Rotated Sorted Array

**Binary Search · Medium**

## Problem

Return the index of a target in an integer array obtained by rotating a strictly increasing array; return `-1` when absent. An unrotated or empty array is allowed. Duplicate values and arbitrary unsorted inputs are outside the contract; the precondition is not checked.

```python
search_rotated(nums: list[int], target: int) -> int
```

`search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4`.

## Reasoning

At every midpoint, at least one half is sorted because there is at most one rotation break. Use its endpoints to decide whether the target lies inside it. Keep that half if it does, otherwise search the other half. Distinct values make the decision unambiguous.

## Complexity

**Time:** O(log n) for nonempty input. **Auxiliary space:** O(1).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/binary_search/search_rotated.py)
- [pytest tests](../../tests/binary_search/test_search_rotated.py)
- Run: `pytest tests/binary_search/test_search_rotated.py -v`

## Attribution

Problem inspiration: [LeetCode — Search Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
