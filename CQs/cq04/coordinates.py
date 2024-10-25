"""Challenge Question 4"""

__author__ = "730740543"


def get_coords(xs: str, ys: str) -> None:
    """Finds all the possible ways to combine a string"""

    i = 0
    while i < len(xs):  # while the integer i is less than all letters in xs
        j = 0
        while j < len(ys):  # while integer j is less than letter in ys
            # print the letter in xs at index i and the letter in ys at index j
            print("(" + xs[i] + "," + ys[j] + ")")
            j += 1  # adding 1 to j to make sure loop breaks

        i += 1  # adding 1 to i to make sure loop breaks
