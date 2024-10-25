__author__ = "730740543"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max1() -> None:
    a: list[int] = [1, 2, 3]
    assert find_and_remove_max(list=a) == 3


def test_find_and_remove_max2() -> None:
    a: list[int] = [1, 2, 3]
    max: int = find_and_remove_max(list=a)
    assert a == [1, 2]


def test_find_and_remove_max3() -> None:
    a: list[int] = [3, 3, 3]
    assert find_and_remove_max(list=a) == 3
