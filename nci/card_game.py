import random
import logging



DEFAULT_COLORS = ['green', 'red', 'yellow', 'blue']

# Explicitly providing comma-separated list as opposed to 
# using range inside list comprehension in case need to 
# support different use cases.
DEFAULT_NUMBERS = [0, 1, 2, 3, 4, 5]


# Could have used singleton support.  
# Need more specifications to understand use cases.
class CardGame():
    """A Card Game class to support some operations.
    """
    def __init__(self, **kwargs) -> None:
        """Class constructor.
        Will allow override of the default colors and numbers during
        instantiation of this class.
        """
        self._deck = []
        
        if 'colors' in kwargs:
            self._colors = kwargs['colors']
        else:
            logging.info("Assigning default colors")
            self._colors = DEFAULT_COLORS

        if 'numbers' in kwargs:
            self._numbers = kwargs['numbers']
        else:
            logging.info("Assigning default numbers")
            self._numbers = DEFAULT_NUMBERS

        self._card_count = 0
        self._seed = None
        if 'seed' in kwargs:
            random.seed(kwargs['seed'])
        
        self._initialize_deck()
        logging.info("Initialized CardGame")

    def _initialize_deck(self) -> None:
        """Initialize the deck of cards.  The colors and numbers have
        been hardcoded in this class.  Alternatively, these could be 
        specified via a configuration file.  Another option would be 
        to read the cards in from a file.
        """
        
        for color in self._colors:
            color = color.lower()
            for number in self._numbers:
                if number != int(number):
                    raise Exception(f"Found non-integer value '{number}'")
                card = (color, number)
                logging.info(f"card {card}")
                self._deck.append(card)
                self._card_count += 1
        logging.info(f"Initialized deck with {self._card_count} cards")

    def shuffle_deck(self) -> list:
        """Shuffle the cards in the deck: randomly mix the cards in the card deck,
        and return the whole deck of cards with a mixed order
        :returns deck: {list}
        """
        
        logging.info("Going to shuffle the deck")
        # if self._seed is not None:
            # Seed the random generator for testing purposes
            # pass
        # self._deck = random.shuffle(self._deck)
        random.shuffle(self._deck)
        return self._deck

    def get_card(self) -> tuple:
        """Get a card from the top of the deck: get one card from
        top of the card deck, return a card, and if there is no card left 
        in the deck return error or exception
        :returns card: {tuple}
        """
        
        if len(self._deck) > 0:
            # The end of the list considered the top of the deck 
            card = self._deck.pop()
            logging.info(f"Got card with color {card[0]} and number {card[1]}")
            return card
        else:
            logging.error("No more cards in the deck")
            raise Exception("No more cards in the deck")

    def sort_cards(self, colors: list = None) -> list:
        """Sort the cards: take a list of colors as parameter and sort the
        cards in that color order.  Numbers should be in ascending order.
        :returns sorted_deck: {list}
        """

        sorted_deck = []       

        if len(self._deck) > 0:
            # Only attempt to sort if there even any cards left in the deck

            if colors is None:
                logging.error("colors was not defined")
                raise Exception("colors was not defined")

            # Create a dict to use to qualify the cards by color
            qualified_color_lookup = {}
            for color in colors:
                color = color.lower()
                logging.info(f"Will sort cards for color '{color}'")
                qualified_color_lookup[color] = True

            # Collect all of the cards by their color for qualified colors
            color_card_lookup = {}
            for card in self._deck:
                logging.info(f"Processing card {card}")
                if card[0] in qualified_color_lookup:
                    if card[0] not in color_card_lookup:
                        color_card_lookup[card[0]] = []
                    color_card_lookup[card[0]].append(card)
                else:
                    logging.info(f"Ignoring card with color '{card[0]}'")

            # For each color, sort the cards
            for color in colors:
                if color in color_card_lookup:            
                    color_cards = color_card_lookup[color]
                    # color_cards = color_cards.sort(key=lambda x:x[1])
                    color_cards.sort(key=lambda x:x[1])
                    for card in color_cards:
                        sorted_deck.append(card)
                else:
                    logging.warning(f"There are no cards with color '{color}' remaining in the deck")
        else:
            logging.info("There are no cards left in the deck to be sorted")

        return sorted_deck
            
