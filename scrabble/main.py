"""Scrabble Game"""

from random import randint

LETTER_SCORES = {"E": 1, "A": 1, "I": 1, "O": 1,
                 "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
                 "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}

BAG = "EEEEEEEEEEEEAAAAAAAAAIIIIIIIIIOOOOOOOONNNNNNRRRRRRTTTTTTLLLLUUUUSSSSDDDDGGGBBCCMMPPFFHHVVWWYKJXQZ"


def score_for_word(word: list[str], letter_scores: dict) -> int:
    """Returns and integer score for a given word as a list"""

    if not (word or letter_scores):
        raise ValueError("Input word or score dictionary missing")

    score = 0

    for letter in word:
        score += letter_scores[letter.upper()]

    return score


def get_seven_random_letters(bag: str) -> list[str]:
    """Returns list of strings from a given bag string"""

    hand = []

    for _ in range(0, 7):
        index = randint(0, 25)

        letter = bag[index]
        hand.append(letter)

    return hand


def get_hand_from_bag(bag: str) -> list[str]:
    """Returns list of strings from a given bag."""

    hand = []

    for _ in range(0, 7):
        index = randint(0, len(bag))

        letter = bag[index]
        bag.replace(letter, "")
        hand.append(letter)

    return hand


def find_valid_word_from_hand(hand: list[str]) -> list[str]:
    """Return list of valid words from dictionary from a given hand"""

    with open("dictionary.txt", "r") as f:
        dictionary = f.readlines()

    for word in dictionary:
        word.replace("\n", "")

    # for word in dictionary:
    #    for

    """For each word check if a character in in the hand list, if any character is not I would move the the next word.
        For a single valid word I would return the first word that meets the criteria, for a list of words I would add them to a list
        and return that."""


if __name__ == "__main__":

    find_valid_word_from_hand(["g", "u", "a", "r", "d", "i",
                               "a"])
