"""Making list functions for practice!"""

__author__ = "730740543"


def all(list: list[int], num: int) -> bool:
    """Checking whether all the integers in a list are one num"""
    if len(list) == 0:
        return False

    i: int = 0
    while i < len(list):  # checking through all items
        if list[i] != num:  # if an item in our list is NOT the num
            return False  # FALSE!!
        i += 1

    return True  # if we make it out the loop, then its true


def max(list: list[int]) -> int:
    """Manually finds the maximum"""

    if len(list) == 0:
        raise ValueError("max() arg is an empty List")

    i: int = 0
    maximum: int = list[0]  # we will assing the max to this
    while i < len(list):  # looping through all items
        if list[i] > maximum:
            maximum = list[i]
        i += 1

    return maximum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Finds whether two lists are exactly the same"""

    if len(list1) != len(list2):  # i its not the same length
        return False  # they cant be the same

    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:  # if at the same index they arent the same
            return False  # it is also false
        i += 1

    return True  # if all that wasn't able to get it to be false it must be true


def extend(list1: list[int], list2: list[int]) -> None:
    i: int = 0
    while i < len(list2):  # looping through list 2 items
        list1.append(list2[i])  # adding them onto our return list
        i += 1
