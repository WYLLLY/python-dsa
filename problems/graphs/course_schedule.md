# Course Schedule

**Graphs · Medium**

## Problem

Courses are numbered `0` through `num_courses - 1`. Each pair `(course, prerequisite)` requires finishing the second before the first. Return whether all courses can be completed. Duplicate pairs are allowed. Zero courses is feasible. Raise `ValueError` for a negative count or any out-of-range course identifier.

```python
course_schedule(num_courses: int, prerequisites: list[tuple[int, int]]) -> bool
```

`course_schedule(2, [(1, 0)]) is True`; adding `(0, 1)` creates a cycle.

## Reasoning

Build prerequisite-to-course edges and incoming edge counts. Repeatedly process courses with no outstanding prerequisites, removing their outgoing edges. If every course is processed, this is a topological order; otherwise a directed cycle leaves some counts positive. Duplicate edges are counted and removed consistently.

## Complexity

For V courses and E prerequisite pairs, **time:** O(V + E). **Auxiliary space:** O(V + E).

Complexities count arithmetic and hash operations as constant time; Python's
arbitrary-size integer costs can grow with operand size. Input is not modified
unless the contract explicitly says otherwise.

## Implementation and tests

- [Typed solution](../../src/python_dsa/graphs/course_schedule.py)
- [pytest tests](../../tests/graphs/test_course_schedule.py)
- Run: `pytest tests/graphs/test_course_schedule.py -v`

## Attribution

Problem inspiration: [LeetCode — Course Schedule](https://leetcode.com/problems/course-schedule/).
Statement, explanation, code and tests were independently written for this
repository with Codex assistance; no external solution code was copied.
