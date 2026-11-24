# Longest Unique Substring

**Sliding Window · Medium**

## Problem

Return the length of the longest contiguous substring containing no repeated Unicode code point. Empty input gives zero. Spaces, case and punctuation are significant.

```python
longest_unique_substring(text: str) -> int
```

`longest_unique_substring("abba") == 2`.

## Reasoning

Maintain a window with distinct characters. On a repeated character, move the left edge past its last occurrence, but never backward. Store the last index of each character and update the longest valid window.

## Complexity

**Time:** O(n) expected. **Auxiliary space:** O(u), where u is the number of distinct code points.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/sliding_window/longest_unique_substring.py)
- [pytest tests](../../tests/sliding_window/test_longest_unique_substring.py)
- Run: `pytest tests/sliding_window/test_longest_unique_substring.py -v`

## Attribution

Problem inspiration: [LeetCode — Longest Unique Substring](https://leetcode.com/problems/longest-substring-without-repeating-characters/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
