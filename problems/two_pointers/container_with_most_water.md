# Container With Most Water

**Two Pointers · Medium**

## Problem

At integer positions, choose two nonnegative vertical line heights to maximize width times the smaller height. Fewer than two lines gives zero. Raise `ValueError` for negative heights.

```python
container_with_most_water(heights: list[int]) -> int
```

`container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49`.

## Reasoning

Start with the widest pair. Keeping the shorter line while reducing width cannot improve area, so discard that endpoint. This rules out only pairs that cannot beat the current pair; the best area seen remains a candidate.

## Complexity

**Time:** O(n). **Auxiliary space:** O(1).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/two_pointers/container_with_most_water.py)
- [pytest tests](../../tests/two_pointers/test_container_with_most_water.py)
- Run: `pytest tests/two_pointers/test_container_with_most_water.py -v`

## Attribution

Problem inspiration: [LeetCode — Container With Most Water](https://leetcode.com/problems/container-with-most-water/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
