"""Interface for providing answers to crossword puzzles.

This module provides an interface for providing answers to crossword puzzles.
This interface describes the methods that must be implemented by a class that
provides answers to crossword puzzles.
"""


class ProvideAnswers(object):
    """Interface for providing answers to crossword puzzles."""
    
    def get_answer_from_position(self, number : int, direction : str) -> str:
        """Get answer from number and direction (i.e position) on board.
        
        Parameters
        ----------
        number : int
            Number corresponding to position on board.
            
        direction : str
            Direction corresponding to position on board. Must be one of
            'across' or 'down'.
        
        Returns
        -------
        str
            Answer corresponding to position on board.
        """
        pass

    def get_answer_from_clue(self, clue : str) -> str:
        """Get answer from clue.
        
        Parameters
        ----------
        clue : str 
            Clue corresponding to answer.
        
        Returns
        -------
        str
            Answer corresponding to clue.
        """
        pass

