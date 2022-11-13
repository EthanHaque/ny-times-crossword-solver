"""Solves the New York Times crossword puzzle.

This program solves the New York Times crossword puzzle. It scrapes
the puzzle from the New York Times website, and then sends input to
the New York Times crossword website to solve the puzzle.
"""

import requests
from datetime import date
from NYTimesScraper import NYTimesScraper


class NYTimesSolver(object):
    """Solves the New York Times crossword puzzle.

    This class solves the New York Times crossword puzzle. It scrapes
    the puzzle from the New York Times website, and then sends input to
    the New York Times crossword website to solve the puzzle.
    """

    def __init__(self):
        """Initializes the NYTimesSolver object."""
        self._scraper = NYTimesScraper()

    def solve(self, board_type):
        """Solves the puzzle.

        This method solves the puzzle. It sends input to the New York
        Times crossword website to solve the puzzle.

        Parameters
        ----------  
        board_type : str
            Type of crossword board to get. Options are 'mini' and
            'daily'.
        """
        board = self._scraper.get_crossword_board(board_type, date.today())
        print(board)


if __name__ == '__main__':
    solver = NYTimesSolver()
    print(solver.solve('mini'))
