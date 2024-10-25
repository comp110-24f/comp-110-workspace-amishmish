"""Summing the elements of a list using different loops"""

__author__ = "730740543"


def w_sum(vals: list[float]) -> float:
    if len(vals) == 0:  # if theres no values
        return 0.0  # sume is 0

    sum: float = 0
    i: int = 0
    while i < len(vals):  # while i < num of val
        sum += vals[i]  # add the val at i to our sum
        i += 1  # preventing infinnite loop

    return sum  # return the sum from that


def f_sum(vals: list[float]) -> float:
    if len(vals) == 0:  # if no vals
        return 0.0  # sum is 0

    sum: float = 0
    for val in vals:  # taking every value in vals
        sum += val  # and then adding it to our sum

    return sum  # return that sum


def f_range_sum(vals: list[float]) -> float:
    if len(vals) == 0:  # if there are no vals
        return 0.0  # there is no sum

    sum: float = 0
    for i in range(0, len(vals)):  # for i in a range of values from 0 to the len val
        sum += vals[i]  # add the value at i to the sum

    return sum  # return that sum
