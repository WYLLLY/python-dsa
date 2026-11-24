from copy import deepcopy

import pytest

from python_dsa.hash_maps.group_anagrams import group_anagrams


@pytest.mark.parametrize(
    "args, expected",
    [
        (
            (["eat", "tea", "tan", "ate", "nat", "bat"],),
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (([],), []),
        ((["", ""],), [["", ""]]),
        ((["a", "A"],), [["a"], ["A"]]),
        ((["éa", "aé", "é"],), [["éa", "aé"], ["é"]]),
    ],
)
def test_examples_and_boundaries(args, expected):
    before = deepcopy(args)
    assert group_anagrams(*args) == expected
    assert args == before
