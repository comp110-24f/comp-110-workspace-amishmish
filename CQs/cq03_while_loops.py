""" While Loops Challenge Question"""

__author__ = "730740543"


def num_instances(phrase: str, search_char: str) -> int:
    """Checking the amount of times that a character appears in a phrase"""

    i: int = 0  # initializing the variable
    instances: int = 0

    while i < len(phrase):

        if (
            phrase[i] == search_char
        ):  # if the letter we r checking right now is the character
            instances += 1  # add one to the instances

        i += 1

    return instances
