from copy import deepcopy

import pytest

from python_dsa.graphs.number_of_islands import number_of_islands


@pytest.mark.parametrize(
    "args, expected",
    [
        (([["1", "1", "0"], ["0", "1", "0"], ["1", "0", "1"]],), 3),
        (([],), 0),
        (([[]],), 0),
        (([["0"]],), 0),
        (([["1"]],), 1),
        (([["1", "0"], ["0", "1"]],), 2),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert number_of_islands(*args) == expected
    assert args == before


@pytest.mark.parametrize("args", [([["1"], []],), ([["x"]],)])
def test_invalid_input(args):
    with pytest.raises(ValueError):
        number_of_islands(*args)
