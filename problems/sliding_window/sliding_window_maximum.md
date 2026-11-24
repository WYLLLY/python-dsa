# Sliding Window Maximum

**Sliding Window · Hard**

## Problem

Return the maximum value in every contiguous window of exactly `k` entries. Require `1 <= k <= len(nums)`, otherwise raise `ValueError` (including empty input). Negative and repeated values are valid.

```python
sliding_window_maximum(nums: list[int], k: int) -> list[int]
```

`sliding_window_maximum([1, 3, -1, -3, 5], 3) == [3, 3, 5]`.

## Reasoning

Maintain indices in decreasing value order. Remove expired indices from the front. A new value dominates earlier smaller or equal values because it expires later, so remove those from the back. The front then identifies the current maximum. Every index enters and leaves at most once.

## Complexity

**Time:** O(n). **Auxiliary space:** O(k), excluding the O(n − k + 1) output.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/sliding_window/sliding_window_maximum.py)
- [pytest tests](../../tests/sliding_window/test_sliding_window_maximum.py)
- Run: `pytest tests/sliding_window/test_sliding_window_maximum.py -v`

## Attribution

Problem inspiration: [LeetCode — Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
