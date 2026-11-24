# Kth Largest Element

**Heaps · Medium**

## Problem

Return the kth largest value, counting duplicate occurrences separately. Require `1 <= k <= len(nums)`, otherwise raise `ValueError`. Do not sort or mutate the caller list.

```python
kth_largest(nums: list[int], k: int) -> int
```

`kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4`.

## Reasoning

Keep a min-heap containing the k largest values encountered so far. Once full, values no larger than its smallest entry cannot enter the top k. Replace the root when a larger value arrives. The final root is exactly the kth largest value.

## Complexity

**Time:** O(n log(k + 1)), including k = 1. **Auxiliary space:** O(k).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/heaps/kth_largest.py)
- [pytest tests](../../tests/heaps/test_kth_largest.py)
- Run: `pytest tests/heaps/test_kth_largest.py -v`

## Attribution

Problem inspiration: [LeetCode — Kth Largest Element](https://leetcode.com/problems/kth-largest-element-in-an-array/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
