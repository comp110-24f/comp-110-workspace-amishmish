"""Creating wordle in python!"""

__author__ = "730740543"


def input_guess(num_chars: int) -> str:
    """Gets our input"""

    guess: str = str(input("Enter a " + str(num_chars) + " character word: "))
    # give me a word with num_chars letter

    while len(guess) != num_chars:  # if length of guess is not num_chars
        guess = str(input("That wasn't " + str(num_chars) + " chars! Try again: "))
        # try again loser!!!

    return guess
    # returns the guess


def contains_char(searched: str, letter: str) -> bool:
    """Finds the whether the letter is in searched"""

    assert len(letter) == 1

    i: int = 0  # counter!!
    while i < len(searched):  # while the index exists

        # if the letter in searched at i is letter
        if searched[i] == letter:
            return True  # then we can return true

        i += 1  # making sure the while loop can break

    return False  # if it wasn't already true, then we can assume false


def emojified(guess: str, correct: str) -> str:
    """Gives a string of emojis that represents the correcttness"""
    assert len(guess) == len(correct)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    output: str = str()  # our output

    i: int = 0  # counter for guess
    while i < len(guess):  # checking every letter
        # characters contained list
        if contains_char(searched=correct, letter=guess[i]):
            # if the letter is in searched then
            if correct[i] == guess[i]:
                # checking whether its at the same spot
                output += GREEN_BOX  # if so add green
            else:  # otherwise we add yellow
                output += YELLOW_BOX
        else:  # if it isnt there then we can add white box
            output = output + WHITE_BOX
        i += 1  # making sure loop ends

    return output


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    # defining game state variables
    turn: int = 1
    won: bool = False

    # game loop
    while turn <= 6 and not (won):
        # while we have turns left and we have not won

        # printing game information
        print("=== Turn " + str(turn) + "/6 ===")
        uguess: str = input_guess(len(secret))
        print(emojified(secret, uguess))  # printing results of they guess

        # checking if they won
        if uguess == secret:
            won = True
            print("You won in " + str(turn) + "/6 turns!")

        # checking whether they lost
        if turn == 6 and not (won):
            print("X/6 - Sorry, try again tomorrow!")

        turn += 1


if __name__ == "__main__":
    main(secret="codes")
