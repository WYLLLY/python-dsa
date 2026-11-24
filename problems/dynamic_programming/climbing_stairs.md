# Climbing Stairs

**Dynamic Programming · Easy**

## Problem

Count ordered sequences of one-step and two-step moves that total n stairs. For n = 0 there is one way: the empty sequence. Raise `ValueError` for negative n. Return an exact Python integer.

```python
climbing_stairs(n: int) -> int
```

`climbing_stairs(3) == 3`: `(1, 1, 1)`, `(1, 2)`, `(2, 1)`.

## Reasoning

A sequence ending in a one-step move comes from n − 1 stairs; one ending in a two-step move comes from n − 2. These cases are disjoint, so their counts add. Starting from the two initial counts, retain just the last two rather than a whole table.

## Complexity

**Time:** O(n) arithmetic operations. **Auxiliary space:** O(1) integer slots. Counts have O(n) bits; bit-level addition work is O(n²) in total and stored integer bits are O(n).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/dynamic_programming/climbing_stairs.py)
- [pytest tests](../../tests/dynamic_programming/test_climbing_stairs.py)
- Run: `pytest tests/dynamic_programming/test_climbing_stairs.py -v`

## Attribution

Problem inspiration: [LeetCode — Climbing Stairs](https://leetcode.com/problems/climbing-stairs/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
