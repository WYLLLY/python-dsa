from copy import deepcopy

import pytest

from python_dsa.two_pointers.container_with_most_water import container_with_most_water


@pytest.mark.parametrize(
    "args, expected",
    [
        (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
        (([],), 0),
        (([1],), 0),
        (([1, 1],), 1),
        (([0, 0, 0],), 0),
        (([4, 3, 2, 1, 4],), 16),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert container_with_most_water(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([1, -1],)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        container_with_most_water(*args)


def test_matches_brute_force():
    from itertools import product

    for size in range(6):
        for values in product(range(3), repeat=size):
            expected = max(
                (
                    min(values[i], values[j]) * (j - i)
                    for i in range(size)
                    for j in range(i + 1, size)
                ),
                default=0,
            )
            assert container_with_most_water(list(values)) == expected
