from copy import deepcopy

import pytest

from python_dsa.graphs.course_schedule import course_schedule


@pytest.mark.parametrize(
    "args, expected",
    [
        ((2, [(1, 0)]), True),
        ((2, [(1, 0), (0, 1)]), False),
        ((0, []), True),
        ((1, [(0, 0)]), False),
        ((4, [(1, 0), (2, 0), (3, 1), (3, 2)]), True),
        ((3, [(1, 0), (1, 0)]), True),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert course_schedule(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [(-1, []), (2, [(2, 0)]), (2, [(-1, 0)])])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        course_schedule(*args)
