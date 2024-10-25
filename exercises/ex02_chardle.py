"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730740543"


def input_word() -> str:
    """Asking our user their guest!"""
    user_word = str(input("Enter a 5-character word: "))

    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()

    return user_word
    print(user_word)


def input_letter() -> str:
    """Getting our user's guess letter"""

    user_letter = str(input("Enter a single character: "))

    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()

    return user_letter
    print(user_letter)


def contains_char(word: str, letter: str) -> None:
    """Checking whether our letter is in the word!!!"""

    print("Searching for " + letter.lower() + " in " + word)

    matches = 0

    if letter == word[0]:
        print(letter + " found at index 0")
        matches += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        matches += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        matches += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        matches += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        matches += 1

    if matches == 0:
        print("No instances of " + letter + " found in " + word)
    elif matches == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(matches) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
