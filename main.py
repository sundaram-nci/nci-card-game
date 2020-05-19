'''
Main module -- implement core logic here.


Invocation should be:
python main.py
Try python main.py --help to see options

I am using python 3.6.9 on Ubuntu 18.04

'''
import os
import sys
import click
import pathlib
import logging
import calendar
import time
import pathlib
from colorama import Fore, Style
from datetime import datetime
from datetime import date

import pprint
import os
from datetime import datetime
import logging

from nci.card_game import CardGame as CG

SHUFFLE_DECK = True
RETRIEVE_CARDS = True
SORT_COLOR_CARDS = True

DEFAULT_OUTDIR = "/tmp/" + os.path.basename(__file__) + '/' + str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))

LOGGING_FORMAT = "%(levelname)s : %(asctime)s : %(pathname)s : %(lineno)d : %(message)s"

DEFAULT_LOGFILE = DEFAULT_OUTDIR + '/' + os.path.basename(__file__) + '.log'

LOG_LEVEL = logging.INFO

DEFAULT_RETRIEVE_COUNT = 5
DEFAULT_SORT_COLORS = 'green, yellow, red'

@click.command()
@click.option('--outdir', help=f"The output directory - default is '{DEFAULT_OUTDIR}'")
@click.option('--logfile', help=f"The log file - default is '{DEFAULT_LOGFILE}'")
@click.option('--retrieve_count', help=f"The number of cards to retrieve - default is '{DEFAULT_RETRIEVE_COUNT}'")
@click.option('--sort_colors', help=f"The colors of cards to be sorted - default is '{DEFAULT_SORT_COLORS}'")
@click.option('--seed', help="The seed to pass to the random function to force pseudo random results")
def main(outdir, logfile, retrieve_count, seed, sort_colors):
    """Template command-line executable
    """

    error_ctr = 0

    if error_ctr > 0:
        sys.exit(1)

    if outdir is None:
        outdir = DEFAULT_OUTDIR
        print(Fore.YELLOW + f"--outdir was not specified and therefore was set to '{outdir}'")
        print(Style.RESET_ALL + '', end='')

    assert isinstance(outdir, str)

    if not os.path.exists(outdir):
        pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)
        print(Fore.YELLOW + f"Created output directory '{outdir}'")
        print(Style.RESET_ALL + '', end='')

    if logfile is None:
        logfile = outdir + '/' + os.path.basename(__file__) + '.log'
        print(Fore.YELLOW + f"--logfile was not specified and therefore was set to '{logfile}'")
        print(Style.RESET_ALL + '', end='')

    assert isinstance(logfile, str)

    if retrieve_count is None:
        retrieve_count = DEFAULT_RETRIEVE_COUNT
        print(Fore.YELLOW + f"--retrieve_count was not specified and therefore was set to '{retrieve_count}'")
        print(Style.RESET_ALL + '', end='')
    else:
        retrieve_count = int(retrieve_count)
        
    assert isinstance(retrieve_count, int)

    if sort_colors is None:
        sort_colors = DEFAULT_SORT_COLORS
        print(Fore.YELLOW + f"--sort_colors was not specified and therefore was set to '{sort_colors}'")
        print(Style.RESET_ALL + '', end='')

    assert isinstance(sort_colors, str)

    logging.basicConfig(filename=logfile, format=LOGGING_FORMAT, level=LOG_LEVEL)

    # Convert the comma-separated list into a proper list
    sort_color_list = []
    for color in sort_colors.split(','):
        sort_color_list.append(color.strip())

    # Instantiate the CardGame class
    if seed is not None:
        cg = CG(seed=seed)
    else:
        cg = CG()

    if SHUFFLE_DECK:
        # Shuffle the deck and display to STDOUT
        deck = cg.shuffle_deck()
        print("Here is the initialized deck:")
        pprint.pprint(deck)

    if RETRIEVE_CARDS:
        # Test the get_card method
        print(f"Going to retrieve {retrieve_count} cards from the deck")
        for i in range(retrieve_count):
            try:
                card = cg.get_card()
                print(f"Got card number {i}: {card}")
            except Exception as e:
                print(f"Caught exception while attempting to retrieve card number {i}: {e}")
                break

    if SORT_COLOR_CARDS:
        # Test the sort_cards method and display
        # results to STDOUT
        print(f"Here are the sorted cards by colors: {sort_color_list}")
        logging.info(f"Here are the sorted cards by colors: {sort_color_list}")
        sorted_cards = cg.sort_cards(sort_color_list)
        if len(sorted_cards) > 0:
            for card in sorted_cards:
                print(f"{card}")
        else:
            print(f"No cards for sorted colors {sort_color_list}")
            logging.warning(f"No cards for sorted colors {sort_color_list}")

    print(f"The log file is {logfile}")


if __name__ == '__main__':
    main()