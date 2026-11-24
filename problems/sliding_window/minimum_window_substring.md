# Minimum Window Substring

**Sliding Window · Hard**

## Problem

Return the shortest contiguous substring of `text` covering every code point in `required`, including repetitions. Choose the leftmost result on equal length. Return `""` if impossible or if `required` is empty. Comparison is exact and case-sensitive.

```python
minimum_window_substring(text: str, required: str) -> str
```

`minimum_window_substring("ADOBECODEBANC", "ABC") == "BANC"`.

## Reasoning

Keep a deficit counter and a total number of missing occurrences. Expand right until all requirements are covered, then shrink left while coverage remains valid. Negative deficits represent surplus occurrences. Record only strictly shorter windows to preserve the leftmost tie rule.

## Complexity

**Time:** O(n + m) expected, including the final slice. **Auxiliary space:** O(u) for code points encountered in either string; **output space:** O(n) worst case.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/sliding_window/minimum_window_substring.py)
- [pytest tests](../../tests/sliding_window/test_minimum_window_substring.py)
- Run: `pytest tests/sliding_window/test_minimum_window_substring.py -v`

## Attribution

Problem inspiration: [LeetCode — Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
