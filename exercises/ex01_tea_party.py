"""Calculating the costs and materials for a tea party!"""

__author__: str = "730740543"


def main_planner(guests: int) -> None:
    "Function to plan out EVERYTHING!"

    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # I kept forgetting to close parantheses here!

    return None


def tea_bags(people: int) -> int:
    """Figuring out how many tea bags we need!"""

    return people * 2


def treats(people: int) -> int:
    """Tells us how many treats we need"""

    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Gives us the total cost of the items we need!"""

    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
