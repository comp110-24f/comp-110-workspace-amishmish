"""Practice with dictionaries"""

__author__ = "730740543"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """inverting the keys and values"""
    new: dict[str, str] = dict()  # creating the output

    values: list[str] = list()
    for x in dictionary:  # making a list of values
        values.append(dictionary[x])  # appending the values

    for i in range(0, len(values) - 1):  # looping through values
        for j in range(0, i - 1):  # looping through values before that
            if values[i] == values[j]:
                # if there is a list before that one that is
                # the same as the one at i
                raise IndexError("There are two of the same keys!")  # ERROR!

    # now that we KNOW there is no way that we can have an error,
    # lets swip swap :p

    for x in dictionary:
        new[dictionary[x]] = x

    return new


def favorite_color(favs: dict[str, str]) -> str:
    """Checking the most liked color"""

    count: dict[str, int] = dict()  # dictionary of counts of color
    for x in favs:  # doing this for all elements
        if x in count:  # if its already in here
            count[x] += 1  # just add one
        else:  # otherwise
            count[x] = 1  # initialize it with one count

    # placeholder value added so we can compare
    count["fake"] = 0

    max: str = "fake"
    for x in count:  # making a list of values
        if count[x] > count[max]:  # if current values coutn is greater
            max = x  # thats our new max

    return max


def count(input: list[str]) -> dict[str, int]:
    """Checking the count of every item"""

    count: dict[str, int] = dict()  # dictionary of counts of color
    for x in input:  # doing this for all elements
        if x in count:  # if its already in here
            count[x] += 1  # just add one
        else:  # otherwise
            count[x] = 1  # initialize it with one count

    return count


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """organizing all words by the beginning letter"""

    alphabet: dict[str, list[str]] = dict()  # our output

    for x in input:  # looping through all elements in lsit
        first = x.lower()[0]  # making it lowercase for easy checking
        if first in alphabet:  #
            alphabet[first].append(x)
        else:
            alphabet[first] = [x]

    return alphabet


def update_attendance(dictionary: dict[str, list[str]], day: str, name: str) -> None:
    """Updating the attendance dictionary"""
    if day in dictionary:
        dictionary[day].append(name)
    else:
        dictionary[day] = [name]