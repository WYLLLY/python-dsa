from copy import deepcopy

import pytest

from python_dsa.stack.daily_temperatures import daily_temperatures


@pytest.mark.parametrize(
    "args, expected",
    [
        (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
        (([],), []),
        (([5, 5, 5],), [0, 0, 0]),
        (([3, 2, 1],), [0, 0, 0]),
        (([-3, -1, 0],), [1, 1, 0]),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert daily_temperatures(*args) == expected
    assert args == before
