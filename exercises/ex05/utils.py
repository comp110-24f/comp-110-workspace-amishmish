"Creating more list functions!"

__author__ = "730740543"


def only_evens(input: list[int]) -> list[int]:
    return_list: list[int] = []  # making our output

    if len(input) == 0:  # if its empty
        return return_list  # return an empty list

    for x in input:  # loop through all the items
        if x % 2 == 0:  # if they are even
            return_list.append(x)  # add it to our output

    return return_list  # output


def sub(input: list[int], start: int, end: int) -> list[int]:
    return_list: list[int] = []  # output

    if len(input) == []:  # if empty
        return return_list  # return empty

    # editing our limits if they are not right
    if start < 0:  # if start negative
        start = 0  # make it 0

    if end >= len(input):  # if start is greater than we have indexes
        end = len(input)  # make it the last index

    i: int = start  # our index
    while i < end:  # looping in the indexes we want
        return_list.append(input[i])  # adding those items to output
        i += 1  # making sure loop ends

    return return_list  # returning this output


def add_at_index(input: list[int], num: int, index: int) -> None:
    if index > len(input) or index < 0:  # raising error if impossible
        raise IndexError("Index is out of bounds for the input list")

    if index == len(input):  # if we need to add at the end
        input.append(num)  # just append it on!

    else:  # if it is not just added at end
        temp: int = 0  # create a temporary variable
        input.append(temp)  # add it to our list so we have right amount of items

        # now we put everything into place
        i: int = len(input) - 1  # making it the last index
        while i > index:  # loop through items that need to be shifted up
            input[i] = input[i - 1]  # shifting it up one index
            i -= 1  # going down

        # now we add the number
        input[index] = num
