import pytest


from nci.card_game import CardGame as CG



def test_shuffle_deck(card_game):
    """Test the shuffle_deck method
    """
    cg = card_game
    cards = cg.shuffle_deck()

    assert cards[0] == ('green', 2), "shuffle_deck test 2 failed"
    assert cards[2] == ('blue', 4), "shuffle_deck test 1 failed"
    assert cards[4] == ('green', 5), "shuffle_deck test 3 failed"


def test_get_card(card_game):
    """Test the get_card method
    """
    cg = card_game

    # Shuffling the deck in order to get cards to a specific state
    # Can discuss alternative approach.
    cards = cg.shuffle_deck()

    assert cg.get_card() == ('yellow', 0), "get_card test 1 failed"
    assert cg.get_card() == ('yellow', 4), "get_card test 2 failed"
    assert cg.get_card() == ('yellow', 5), "get_card test 3 failed"
    assert cg.get_card() == ('blue', 0), "get_card test 4 failed"
    assert cg.get_card() == ('red', 0), "get_card test 5 failed"


def test_sort_colors(card_game):
    """Test the sort_colors method
    """
    expected_count = 14
    cg = card_game

    # Shuffling the deck in order to get cards to a specific state
    # Can discuss alternative approach.
    cards = cg.shuffle_deck()

    # Getting cards in order to get cards to a specific state.
    # Can discuss alternative approach.
    for _ in range(5):
        cg.get_card()

    cards = cg.sort_cards(['green', 'yellow', 'red'])
    assert len(cards) == expected_count, f"sort_colors test 1 failed, expected '{expected_count}' got '{len(cards)}''"
    
    assert cards[0] == ('green', 0), "sort_colors test 2 failed"
    assert cards[1] == ('green', 1), "sort_colors test 3 failed"
    assert cards[2] == ('green', 2), "sort_colors test 4 failed"
    assert cards[3] == ('green', 3), "sort_colors test 5 failed"
    assert cards[4] == ('green', 4), "sort_colors test 6 failed"
    assert cards[5] == ('green', 5), "sort_colors test 7 failed"
    assert cards[6] == ('yellow', 1), "sort_colors test 8 failed"
    assert cards[7] == ('yellow', 2), "sort_colors test 9 failed"
    assert cards[8] == ('yellow', 3), "sort_colors test 10 failed"
    assert cards[9] == ('red', 1), "sort_colors test 11 failed"
    assert cards[10] == ('red', 2), "sort_colors test 12 failed"
    assert cards[11] == ('red', 3), "sort_colors test 13 failed"
    assert cards[12] == ('red', 4), "sort_colors test 14 failed"
    assert cards[13] == ('red', 5), "sort_colors test 15 failed"
