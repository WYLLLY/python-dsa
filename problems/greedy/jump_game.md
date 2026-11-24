# Jump Game

**Greedy · Medium**

## Problem

At each position, a nonnegative integer specifies the maximum forward jump length; any smaller forward jump is allowed. Starting at index zero, can you reach the final index? Empty input gives `False`; a singleton is already reached. Raise `ValueError` for any negative jump.

```python
jump_game(jumps: list[int]) -> bool
```

`jump_game([2, 3, 1, 1, 4]) is True`; `jump_game([3, 2, 1, 0, 4]) is False`.

## Reasoning

Reachable positions form a prefix, because all shorter jumps are allowed. Track the farthest reachable index. A scan position beyond that boundary proves a gap no later position can bridge. Otherwise extend the boundary with its jump, and finish once it covers the last index.

## Complexity

**Time:** O(n), including full input validation before early success. **Auxiliary space:** O(1).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/greedy/jump_game.py)
- [pytest tests](../../tests/greedy/test_jump_game.py)
- Run: `pytest tests/greedy/test_jump_game.py -v`

## Attribution

Problem inspiration: [LeetCode — Jump Game](https://leetcode.com/problems/jump-game/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
