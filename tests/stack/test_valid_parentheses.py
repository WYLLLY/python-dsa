from copy import deepcopy

import pytest

from python_dsa.stack.valid_parentheses import valid_parentheses


@pytest.mark.parametrize(
    "args, expected",
    [
        (("()[]{}",), True),
        (("([{}])",), True),
        (("(]",), False),
        (("([)]",), False),
        (("(",), False),
        (("",), True),
        (("a",), False),
        (("]",), False),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert valid_parentheses(*args) == expected
    assert args == before
