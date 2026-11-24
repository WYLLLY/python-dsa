# Longest Increasing Subsequence

**Dynamic Programming · Medium**

## Problem

Return the length of the longest strictly increasing subsequence. Chosen entries preserve their original order but need not be contiguous. Equal values cannot extend a subsequence. Empty input gives zero. Do not modify input.

```python
longest_increasing_subsequence(nums: list[int]) -> int
```

`longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4`.

## Reasoning

Use a compressed dynamic-programming frontier: `tails[i]` is the smallest possible last value of an increasing subsequence of length i + 1 in the prefix processed. Binary search finds the first tail at least as large as the new value. Replace it to improve future extension opportunities, or append if every tail is smaller. The frontier length is optimal; its entries are not necessarily one actual subsequence.

## Complexity

**Time:** O(n log(n + 1)). **Auxiliary space:** O(n).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/dynamic_programming/longest_increasing_subsequence.py)
- [pytest tests](../../tests/dynamic_programming/test_longest_increasing_subsequence.py)
- Run: `pytest tests/dynamic_programming/test_longest_increasing_subsequence.py -v`

## Attribution

Problem inspiration: [LeetCode — Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
