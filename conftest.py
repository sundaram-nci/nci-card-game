import pytest

from nci.card_game import CardGame as CG


DEFAULT_COLORS = ["green", "red", "yellow", "blue"]

DEFAULT_NUMBERS = [0, 1, 2, 3, 4, 5]


@pytest.fixture
def card_game():
    return CG(colors=DEFAULT_COLORS, numbers=DEFAULT_NUMBERS, seed="testing")
