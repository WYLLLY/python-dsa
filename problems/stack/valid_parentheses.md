# Valid Parentheses

**Stack · Easy**

## Problem

Return whether a string consists only of properly paired and nested `()`, `[]` and `{}`. Reject any other character. The empty string is valid.

```python
valid_parentheses(text: str) -> bool
```

`valid_parentheses("([{}])") is True`; `valid_parentheses("([)]") is False`.

## Reasoning

A closing bracket must match the latest unmatched opening bracket. Push openings and pop on a matching closing bracket; reject underflow, mismatches or unknown symbols. At the end, no opening may remain.

## Complexity

**Time:** O(n). **Auxiliary space:** O(n) for unmatched openings.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/stack/valid_parentheses.py)
- [pytest tests](../../tests/stack/test_valid_parentheses.py)
- Run: `pytest tests/stack/test_valid_parentheses.py -v`

## Attribution

Problem inspiration: [LeetCode — Valid Parentheses](https://leetcode.com/problems/valid-parentheses/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
