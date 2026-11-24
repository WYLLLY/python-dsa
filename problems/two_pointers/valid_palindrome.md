# Valid Palindrome

**Two Pointers · Easy**

## Problem

Return whether the alphanumeric characters read identically from either end, ignoring case via per-character `str.lower()`. Use `str.isalnum()` for Unicode characters. This is not Unicode normalization or full case folding. Empty strings and punctuation-only strings are palindromes.

```python
valid_palindrome(text: str) -> bool
```

`valid_palindrome("A man, a plan, a canal: Panama") is True`.

## Reasoning

Move two pointers inward, skipping non-alphanumeric characters. Every surviving pair must match after lowercase conversion. Once all pairs match, zero or one middle character cannot break the palindrome.

## Complexity

**Time:** O(n). **Auxiliary space:** O(1).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/two_pointers/valid_palindrome.py)
- [pytest tests](../../tests/two_pointers/test_valid_palindrome.py)
- Run: `pytest tests/two_pointers/test_valid_palindrome.py -v`

## Attribution

Problem inspiration: [LeetCode — Valid Palindrome](https://leetcode.com/problems/valid-palindrome/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
