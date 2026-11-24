# Two Sum

**Hash Maps · Easy**

## Problem

Return distinct indices `(i, j)` with `i < j` whose values sum to the target, or `None`. Choose the earliest possible `j`, then the earliest matching `i`. Empty input is allowed.

```python
two_sum(nums: list[int], target: int) -> tuple[int, int] | None
```

`two_sum([3, 3], 6) == (0, 1)`.

## Reasoning

Scan left to right and remember the first index of every seen value. Check for the complement before inserting the current value, so one element cannot be used twice. The scan and first-index map enforce the tie rule.

## Complexity

**Time:** O(n) expected with hash-table operations. **Auxiliary space:** O(n).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/hash_maps/two_sum.py)
- [pytest tests](../../tests/hash_maps/test_two_sum.py)
- Run: `pytest tests/hash_maps/test_two_sum.py -v`

## Attribution

Problem inspiration: [LeetCode — Two Sum](https://leetcode.com/problems/two-sum/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
