"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        """Making fish with age."""
        self.age = 0  # age starts zero
        return None

    def one_day(self):
        """What a fish does everyday."""
        self.age += 1  # add age
        return None
