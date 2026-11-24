from copy import deepcopy

import pytest

from python_dsa.arrays.trapping_rain_water import trapping_rain_water


@pytest.mark.parametrize(
    "args, expected",
    [
        (([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), 6),
        (([4, 2, 0, 3, 2, 5],), 9),
        (([],), 0),
        (([2],), 0),
        (([3, 3, 3],), 0),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert trapping_rain_water(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([-1],)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        trapping_rain_water(*args)


def test_matches_brute_force():
    from itertools import product

    for size in range(6):
        for values in product(range(3), repeat=size):
            expected = sum(
                min(max(values[: i + 1]), max(values[i:])) - h for i, h in enumerate(values)
            )
            assert trapping_rain_water(list(values)) == expected
