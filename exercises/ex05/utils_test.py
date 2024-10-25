"Testing our list functions"

__author__ = "730740543"

# imports
from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


# only_evens tests
def test_only_evens_normal() -> None:
    in_list: list[int] = [104, 15548, 427, 4158, 4333]
    assert only_evens(in_list) == [104, 15548, 4158]
    # filtering out numbers that are not even


def test_only_evens_all_odds() -> None:
    in_list: list[int] = [3, 5, 7, 9, 11]
    assert only_evens(in_list) == []
    # should be empty since no evens


def test_only_evens_all_evens_with_zero() -> None:
    in_list: list[int] = [0, 2, 4, 6, 8]
    assert only_evens(in_list) == [0, 2, 4, 6, 8]
    # should be the same since 0 also has no remainder when divided by 2


# sub tests
def test_sub_unusual_end() -> None:
    in_list: list[int] = [1, 2, 3, 4]  # input
    assert sub(in_list, 2, 52) == [3, 4]  # it should change the 52 to last index


def test_sub_unusual_start() -> None:
    in_list: list[int] = [1, 2, 3, 4]  # input
    assert sub(in_list, -2, 2) == [1, 2]  # should change -2 to 0


def test_sub_normal() -> None:
    in_list: list[int] = [1, 2, 3, 4]  # regular list
    assert sub(in_list, 1, 3) == [2, 3]  # takes items at 1 and 2


# add_at_index tests
def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    in_list: list[int] = [1, 2, 3]  # input
    with pytest.raises(IndexError):
        add_at_index(in_list, 5738, 457724)
        # an IndexError is raised for the case when the add_at_index is given an 5738
        # that is greater than the length of our <list_object>


def test_add_at_index_empty_list() -> None:
    # checks whether it can mutate an empty list
    in_list: list[int] = []  # empty!
    add_at_index(in_list, 1, 0)  # add 1 at index 0 please!
    assert in_list == [1]  # this checks that it worked


def test_add_at_index_regular() -> None:
    # checks whether it can mutate an regular list
    in_list: list[int] = [1, 2, 4]  # input
    add_at_index(in_list, 3, 2)  # add 3 at index 2 please!
    assert in_list == [1, 2, 3, 4]  # did it work?
