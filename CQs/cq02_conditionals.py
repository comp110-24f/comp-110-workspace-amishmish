""" Practice with Conditionals! """

__author__ = "730740543"


# functions


def guess_a_number() -> None:
    """Lets the user guess a number"""

    secret: int = 7  # shhh
    guess: int = int(input("Guess a number: "))

    print("Your guess was " + str(guess) + ".")

    # conditionals!!!
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


# main
if __name__ == "__main__":
    guess_a_number()
