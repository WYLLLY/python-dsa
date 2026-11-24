from copy import deepcopy

import pytest

from python_dsa.stack.largest_rectangle import largest_rectangle


@pytest.mark.parametrize(
    "args, expected",
    [
        (([2, 1, 5, 6, 2, 3],), 10),
        (([],), 0),
        (([2, 2],), 4),
        (([1, 2, 3, 4],), 6),
        (([4, 3, 2, 1],), 6),
        (([0, 0],), 0),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert largest_rectangle(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([2, -1],)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        largest_rectangle(*args)


def test_matches_brute_force():
    from itertools import product

    for size in range(6):
        for values in product(range(3), repeat=size):
            expected = max(
                (min(values[i:j]) * (j - i) for i in range(size) for j in range(i + 1, size + 1)),
                default=0,
            )
            assert largest_rectangle(list(values)) == expected
