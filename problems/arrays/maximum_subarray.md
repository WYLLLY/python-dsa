# Maximum Subarray

**Arrays · Medium**

## Problem

Given a nonempty list of integers, return the largest sum among all nonempty contiguous slices. Raise `ValueError` for an empty list.

```python
maximum_subarray(nums: list[int]) -> int
```

`maximum_subarray([-2, 1, -3, 4, -1, 2, 1]) == 6` (slice `[4, -1, 2, 1]`).

## Reasoning

At each position, the best slice ending here either starts at this value or extends the best slice ending immediately before it. Keep the larger choice and update the overall best. Initializing from the first value preserves the all-negative case.

## Complexity

**Time:** O(n). **Auxiliary space:** O(1). An iterator avoids copying a slice.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/arrays/maximum_subarray.py)
- [pytest tests](../../tests/arrays/test_maximum_subarray.py)
- Run: `pytest tests/arrays/test_maximum_subarray.py -v`

## Attribution

Problem inspiration: [LeetCode — Maximum Subarray](https://leetcode.com/problems/maximum-subarray/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
