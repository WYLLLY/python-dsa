# Merge Intervals

**Greedy · Medium**

## Problem

Given closed integer intervals `(start, end)`, return their union as sorted disjoint intervals. Overlap and touching endpoints merge. Empty input gives `[]`. Raise `ValueError` when start exceeds end. Do not modify the original list.

```python
merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]
```

`merge_intervals([(1, 4), (4, 5), (8, 9)]) == [(1, 5), (8, 9)]`.

## Reasoning

Sort a copy by start. The next interval can overlap only the last accumulated interval: earlier ones end before it starts. Extend that last interval when they touch or overlap; otherwise append a new disjoint interval. This greedily preserves the union at every step.

## Complexity

**Time:** O(n log n). **Auxiliary space:** O(n) for the sorted copy and sorting workspace, plus O(n) output.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/greedy/merge_intervals.py)
- [pytest tests](../../tests/greedy/test_merge_intervals.py)
- Run: `pytest tests/greedy/test_merge_intervals.py -v`

## Attribution

Problem inspiration: [LeetCode — Merge Intervals](https://leetcode.com/problems/merge-intervals/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
