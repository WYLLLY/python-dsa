# Trapping Rain Water

**Arrays · Hard**

## Problem

Bars of unit width have nonnegative integer heights. Return the volume retained after rain. Empty or short profiles hold no water. Raise `ValueError` for any negative height.

```python
trapping_rain_water(heights: list[int]) -> int
```

`trapping_rain_water([4, 2, 0, 3, 2, 5]) == 9`.

## Reasoning

Water above a bar is limited by the smaller boundary maximum. Maintain maxima from both ends. When the left maximum is smaller, the known right boundary is sufficient to settle the next left bar; otherwise settle the next right bar. Each bar is processed once.

## Complexity

**Time:** O(n). **Auxiliary space:** O(1).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/arrays/trapping_rain_water.py)
- [pytest tests](../../tests/arrays/test_trapping_rain_water.py)
- Run: `pytest tests/arrays/test_trapping_rain_water.py -v`

## Attribution

Problem inspiration: [LeetCode — Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
