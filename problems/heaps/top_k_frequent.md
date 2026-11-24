# Top K Frequent Elements

**Heaps · Medium**

## Problem

Return exactly k distinct values ordered by decreasing frequency, then increasing numeric value on ties. Allow k = 0, including empty input. Raise `ValueError` unless `0 <= k <= number of distinct values`. Leave input unchanged.

```python
top_k_frequent(nums: list[int], k: int) -> list[int]
```

`top_k_frequent([4, 4, 2, 2, 1], 2) == [2, 4]`.

## Reasoning

Count occurrences, then select the k smallest priority keys `(-frequency, value)` with a heap. Negating the frequency reverses that ordering, while the value makes ties deterministic. `heapq.nsmallest` returns its selections in key order.

## Complexity

For n entries and u distinct values, **time:** O(n + u log(k + 1)) expected, with O(n) for k = 0. **Auxiliary space:** O(u + k), including the O(k) output.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/heaps/top_k_frequent.py)
- [pytest tests](../../tests/heaps/test_top_k_frequent.py)
- Run: `pytest tests/heaps/test_top_k_frequent.py -v`

## Attribution

Problem inspiration: [LeetCode — Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
