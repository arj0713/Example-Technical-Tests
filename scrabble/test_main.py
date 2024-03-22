import pytest

from main import score_for_word, get_seven_random_letters, get_hand_from_bag, find_valid_word_from_hand

LETTER_SCORES = {"E": 1, "A": 1, "I": 1, "O": 1,
                 "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
                 "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}

BAG = "EEEEEEEEEEEEAAAAAAAAAIIIIIIIIIOOOOOOOONNNNNNRRRRRRTTTTTTLLLLUUUUSSSSDDDDGGGBBCCMMPPFFHHVVWWYKJXQZ"


def test_score_for_guardian_equals_10():

    assert score_for_word(["g", "u", "a", "r", "d", "i",
                          "a", "n"], LETTER_SCORES) == 10


def test_score_for_sat_equals_3():

    assert score_for_word(["s", "a", "t"], LETTER_SCORES) == 3


def test_missing_word_raises_error():

    with pytest.raises(ValueError):
        score_for_word([], {})


def test_hand_is_correct_size():

    assert len(get_seven_random_letters(BAG)) == 7


def test_hand_is_list_of_str():

    hand = get_seven_random_letters(BAG)

    assert isinstance(hand[1], str)


def test_hand_from_proper_bag_is_correct_size():

    assert len(get_hand_from_bag(BAG)) == 7


def test_hand_from_proper_bag_is_list_of_str():

    hand = get_hand_from_bag(BAG)

    assert isinstance(hand[1], str)


def test_find_valid_word_returns_list():

    words = find_valid_word_from_hand(["g", "u", "a", "r", "d", "i",
                                       "a"])

    assert isinstance(words, list)


def test_find_valid_word_returns_list_of_str():

    words = find_valid_word_from_hand(["g", "u", "a", "r", "d", "i",
                                       "a"])

    assert isinstance(words[0], str)
