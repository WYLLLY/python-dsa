from copy import deepcopy

import pytest

from python_dsa.dynamic_programming.climbing_stairs import climbing_stairs


@pytest.mark.parametrize(
    "args, expected", [((0,), 1), ((1,), 1), ((2,), 2), ((5,), 8), ((10,), 89)]
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert climbing_stairs(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [(-1,)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        climbing_stairs(*args)
