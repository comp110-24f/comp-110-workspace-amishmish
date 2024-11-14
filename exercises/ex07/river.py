"""File to define River class."""

__author__ = "730740543"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks whether the fish and bears will die."""
        glubs = []
        for i in range(0, len(self.fish)):  # for every fish
            glub = self.fish[i]  # just naming this fish
            if glub.age <= 3:  # if the age is too high
                glubs.append(glub)

        # doing same thing for bear
        rawrs = []  # :3
        for i in range(0, len(self.bears)):
            rawr = self.bears[i]  # current bear
            if rawr.age <= 5:
                rawrs.append(rawr)

        # making them the attribute fish and bear
        self.fish = glubs
        self.bears = rawrs  # :3

        return None

    def remove_fish(self, amount: int):
        """Getting rid of fish."""
        glubs = []  # lists to store the fish left
        for i in range(0, len(self.fish)):  # checking all fish
            if i >= amount:  # if fish index is not the ones we are removing
                glubs.append(self.fish[i])  # add it to list

        self.fish = glubs  # make this list the one in attribute

        return None

    def bears_eating(self):
        """Let the bears FEAST!"""
        for bear in self.bears:  # for each bear
            if len(self.fish) >= 5:  # if there are enough fish
                self.remove_fish(3)  # EAT THEM
                bear.eat(3)

        return None

    def check_hunger(self):
        """Checks whether the bear is too hungry to live."""
        # essentially copying this from the other function BUT
        rawrs = []  # :3
        for i in range(0, len(self.bears)):
            rawr = self.bears[i]  # current bear
            if rawr.hunger_score >= 0:  # the condition is that the hunger is too low
                rawrs.append(rawr)

        self.bears = rawrs  # puting that back in the river
        return None

    def repopulate_fish(self):
        """Making new fishies."""
        num = (len(self.fish) // 2) * 4  # finding how many
        for _ in range(0, num):  # making range of that many
            self.fish.append(Fish())  # appending
        return None

    def repopulate_bears(self):
        """Making new cubs."""
        # copy from fish
        num = len(self.bears) // 2
        for _ in range(0, num):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Find out information about the bears and fish in river."""
        print("~~~ Day " + str(self.day) + ": ~~~\n")  # the exact string
        print(
            "Fish Population: " + str(len(self.fish))
        )  # had to str() it to let it add
        print("Bear Population: " + str(len(self.bears)))

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one entire week!"""
        for _ in range(0, 7):  # repeats it 7 times
            self.one_river_day()
