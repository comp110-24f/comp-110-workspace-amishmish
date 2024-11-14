"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a bear with an age and hunger."""
        self.age: int = 0
        self.hunger_score: int = 0  # initializing as 0
        return None

    def one_day(self):
        """What a bear does in a day."""
        self.age += 1  # adding one
        self.hunger_score -= 1  # decreasing
        return None

    def eat(self, num_fish):
        """'nom nom' - bear."""
        self.hunger_score += num_fish  # increasing accordingly
