# Valid Anagram

**Hash Maps · Easy**

## Problem

Determine whether two strings have exactly the same character multiplicities. Comparison is case-sensitive and uses Unicode code points without normalization; spaces and punctuation count.

```python
valid_anagram(left: str, right: str) -> bool
```

`valid_anagram("anagram", "nagaram") is True`.

## Reasoning

An ordering change preserves every character count. Comparing frequency maps is therefore both necessary and sufficient; it also handles repeated characters and empty strings.

## Complexity

**Time:** O(n + m) expected. **Auxiliary space:** O(u), for distinct characters across both strings.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/hash_maps/valid_anagram.py)
- [pytest tests](../../tests/hash_maps/test_valid_anagram.py)
- Run: `pytest tests/hash_maps/test_valid_anagram.py -v`

## Attribution

Problem inspiration: [LeetCode — Valid Anagram](https://leetcode.com/problems/valid-anagram/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
