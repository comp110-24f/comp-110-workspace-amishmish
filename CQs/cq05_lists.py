"""Mutating functions."""

__author__ = "730740543"


def manual_append(list: list[int], num: int) -> None:
    """Manually appends an integer to a list"""
    list.append(num)  # just added it on the end


def double(list: list[int]) -> None:
    """Doubles all items"""
    i: int = 0
    while i < len(list):  # looping through all items
        new = list[i] * 2  # doubling the item
        list[i] = new  # making this the item at that index
