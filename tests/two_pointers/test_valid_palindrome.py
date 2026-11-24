from copy import deepcopy

import pytest

from python_dsa.two_pointers.valid_palindrome import valid_palindrome


@pytest.mark.parametrize(
    "args, expected",
    [
        (("A man, a plan, a canal: Panama",), True),
        (("race a car",), False),
        (("",), True),
        ((".,",), True),
        (("Été",), True),
        (("0P",), False),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert valid_palindrome(*args) == expected
    assert args == before
