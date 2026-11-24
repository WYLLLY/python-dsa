# Number of Islands

**Graphs · Medium**

## Problem

Count connected components of land (`"1"`) in a rectangular grid of `"0"` and `"1"` strings, using up/down/left/right adjacency. Diagonals are not adjacent. Empty grids and zero-column rows give zero. Raise `ValueError` for ragged rows or invalid cells. Leave the grid unchanged.

```python
number_of_islands(grid: list[list[str]]) -> int
```

`number_of_islands([["1", "0"], ["0", "1"]]) == 2`.

## Reasoning

Scan every cell. An unseen land cell starts one new island; traverse its component with an explicit DFS stack. Mark neighbors when pushing them so no cell is scheduled twice. Each later scan position in that component is already visited.

## Complexity

For R rows and C columns, **time:** O(R + R·C), including validation of zero-column rows. **Auxiliary space:** O(R·C) for visited land and the stack.

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/graphs/number_of_islands.py)
- [pytest tests](../../tests/graphs/test_number_of_islands.py)
- Run: `pytest tests/graphs/test_number_of_islands.py -v`

## Attribution

Problem inspiration: [LeetCode — Number of Islands](https://leetcode.com/problems/number-of-islands/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
