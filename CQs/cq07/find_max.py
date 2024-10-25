__author__ = "730740543"


def find_and_remove_max(list: list[int]) -> int:

    if list == []:
        return -1

    max: int = list[0]

    for x in list:  # checking all items
        if max < x:  # if max is less than item right now
            max = x  # x is the new max
    # we should have correct max now

    i: int = 0
    while i < len(list):  # using indexes to loop through so we can pop correct indexes
        if list[i] == max:  # if item at i is max
            list.pop(i)  # get rid of it
        else:
            i += 1
    return max
