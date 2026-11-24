from copy import deepcopy

import pytest

from python_dsa.greedy.merge_intervals import merge_intervals


@pytest.mark.parametrize(
    "args, expected",
    [
        (([(1, 3), (2, 6), (8, 10), (15, 18)],), [(1, 6), (8, 10), (15, 18)]),
        (([],), []),
        (([(1, 4), (4, 5)],), [(1, 5)]),
        (([(5, 5), (1, 10), (2, 3)],), [(1, 10)]),
        (([(-3, -1), (-2, 2)],), [(-3, 2)]),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert merge_intervals(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([(2, 1)],)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        merge_intervals(*args)
