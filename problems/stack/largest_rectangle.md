# Largest Rectangle in Histogram

**Stack · Hard**

## Problem

Given nonnegative unit-width histogram bars, return the area of the largest rectangle entirely beneath the profile. Empty input gives zero. Negative heights raise `ValueError`.

```python
largest_rectangle(heights: list[int]) -> int
```

`largest_rectangle([2, 1, 5, 6, 2, 3]) == 10`.

## Reasoning

Keep increasing heights with their earliest usable start indices. A shorter bar ends all taller rectangles on the stack; compute their areas and carry their earliest start forward. Equal heights share the earlier start. A final virtual zero flushes all remaining positive heights without modifying the input.

## Complexity

**Time:** O(n), since each stack entry is pushed and popped once. **Auxiliary space:** O(n).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/stack/largest_rectangle.py)
- [pytest tests](../../tests/stack/test_largest_rectangle.py)
- Run: `pytest tests/stack/test_largest_rectangle.py -v`

## Attribution

Problem inspiration: [LeetCode — Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
