# Group Anagrams

**Hash Maps · Medium**

## Problem

Partition words into groups with equal Unicode character multiplicities. Preserve input order inside each group and order groups by their first appearance. Comparison is case-sensitive; no normalization is performed.

```python
group_anagrams(words: list[str]) -> list[list[str]]
```

`group_anagrams(["tea", "eat", "bat"]) == [["tea", "eat"], ["bat"]]`.

## Reasoning

Sorting a word produces a canonical key for its multiset of characters. Append each word to the group for that key. Python dictionaries retain insertion order, providing deterministic group order.

## Complexity

Let W be the number of words and L the longest word. **Time:** O(W · L log L) as an upper bound (plus O(W) for empty words). **Auxiliary space:** O(W · L) for keys and references in groups, including the O(W) output references.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/hash_maps/group_anagrams.py)
- [pytest tests](../../tests/hash_maps/test_group_anagrams.py)
- Run: `pytest tests/hash_maps/test_group_anagrams.py -v`

## Attribution

Problem inspiration: [LeetCode — Group Anagrams](https://leetcode.com/problems/group-anagrams/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
