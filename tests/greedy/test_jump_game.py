from copy import deepcopy

import pytest

from python_dsa.greedy.jump_game import jump_game


@pytest.mark.parametrize(
    "args, expected",
    [
        (([2, 3, 1, 1, 4],), True),
        (([3, 2, 1, 0, 4],), False),
        (([],), False),
        (([0],), True),
        (([1, 0],), True),
        (([0, 1],), False),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert jump_game(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([1, -1],)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        jump_game(*args)


def test_matches_reachability_oracle():
    from itertools import product

    for size in range(1, 7):
        for jumps in product(range(3), repeat=size):
            reachable = {0}
            for i in range(size):
                if i in reachable:
                    reachable.update(range(i + 1, min(size, i + jumps[i] + 1)))
            assert jump_game(list(jumps)) == (size - 1 in reachable)
