"""Course Schedule. See problems/graphs/course_schedule.md."""

from collections import deque


def course_schedule(num_courses: int, prerequisites: list[tuple[int, int]]) -> bool:
    """Return whether every course can be completed (no directed cycle)."""
    if num_courses < 0:
        raise ValueError("num_courses must be nonnegative")
    outgoing: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prerequisite in prerequisites:
        if not (0 <= course < num_courses and 0 <= prerequisite < num_courses):
            raise ValueError("course indices must be in range")
        outgoing[prerequisite].append(course)
        indegree[course] += 1
    ready = deque(i for i, degree in enumerate(indegree) if degree == 0)
    completed = 0
    while ready:
        prerequisite = ready.popleft()
        completed += 1
        for course in outgoing[prerequisite]:
            indegree[course] -= 1
            if indegree[course] == 0:
                ready.append(course)
    return completed == num_courses
