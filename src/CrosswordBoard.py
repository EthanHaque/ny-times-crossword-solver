"""Implements the CrosswordBoard class.

This class is used to represent a crossword board. It is used to
represent the state of a crossword board. Including information
about the clues, positions of the clues on the Board, and answers.
"""


class CrosswordBoard(object):
    """Represents a crossword board."""

    def __init__(self) -> None:
        """Initialize a crossword board."""
        self._clues = {}
        self._positions = {}
        self._answers = {}
        self._allow_empty_clues = False

    def __validate_direction(self, direction: str) -> None:
        """Validate direction.

        Parameters
        ----------
        direction : str
            Direction to validate.

        Raises
        ------
        ValueError
            If direction is not 'across' or 'down'.
        """
        if direction not in ['across', 'down']:
            raise ValueError('Direction must be \'across\' or \'down\'.')

    def __validate_position(self, number: int, direction: str) -> None:
        """Validate position.

        Parameters
        ----------
        number : int
            Number to validate.

        direction : str
            Direction to validate.

        Raises
        ------
        ValueError
            If number is not a positive integer.
        """
        if not isinstance(number, int) or number < 1:
            raise ValueError('Number must be a positive integer.')
        self.__validate_direction(direction)

    def add_clue(self, number: int, direction: str, clue: str) -> None:
        """Add a clue to the board.

        Parameters
        ----------
        number : int
            Number corresponding to position on board.

        direction : str
            Direction corresponding to position on board. Must be one of
            'across' or 'down'.

        clue : str
            Clue corresponding to position on board.
        """
        self.__validate_position(number, direction)
        if (number, direction) in self._clues:
            raise ValueError("Clue already exists.")
        if clue == '' and not self._allow_empty_clues:
            raise ValueError("Clue cannot be empty.")

        self._clues[(number, direction)] = clue
        self._positions[clue] = (number, direction)

    def get_clue(self, number: int, direction: str) -> str:
        """Get clue from number and direction (i.e position) on board.

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
            Clue corresponding to position on board.
        """
        self.__validate_position(number, direction)
        if (number, direction) not in self._clues:
            raise ValueError("Clue does not exist.")

        return self._clues[(number, direction)]

    def remove_clue(self, number: int, direction: str) -> None:
        """Remove clue from number and direction (i.e position) on board.

        Parameters
        ----------
        number : int
            Number corresponding to position on board.

        direction : str
            Direction corresponding to position on board. Must be one of
            'across' or 'down'.
        """
        self.__validate_position(number, direction)
        if (number, direction) not in self._clues:
            raise ValueError("Clue does not exist.")

        del self._clues[(number, direction)]
        del self._positions[self._clues[(number, direction)]]

    def add_answer(self, number: int, direction: str, answer: str) -> None:
        """Add an answer to the board.

        Parameters
        ----------
        number : int
            Number corresponding to position on board.

        direction : str
            Direction corresponding to position on board. Must be one of
            'across' or 'down'.

        answer : str
            Answer corresponding to position on board.
        """
        self.__validate_position(number, direction)
        if (number, direction) in self._answers:
            raise ValueError("Answer already exists.")
        self._answers[(number, direction)] = answer

    def get_answer(self, number: int, direction: str) -> str:
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
        self.__validate_position(number, direction)
        if (number, direction) not in self._answers:
            raise ValueError("Answer does not exist.")
        return self._answers[(number, direction)]

    def remove_answer(self, number: int, direction: str) -> None:
        """Remove answer from number and direction (i.e position) on board.

        Parameters
        ----------
        number : int
            Number corresponding to position on board.

        direction : str
            Direction corresponding to position on board. Must be one of
            'across' or 'down'.
        """
        self.__validate_position(number, direction)
        if (number, direction) not in self._answers:
            raise ValueError("Answer does not exist.")
        del self._answers[(number, direction)]

    def get_clues(self) -> list:
        """Get list of clues.

        Returns
        -------
        list
            List of clues.
        """
        return list(self._clues.items())

    def get_answers(self) -> list:
        """Get list of answers.

        Returns
        -------
        list
            List of answers.
        """
        return list(self._answers.items())

    def get_answer_from_clue(self, clue: str) -> str:
        """Get answer from clue.

        Parameters
        ----------
        clue : str
            Clue to get answer for.

        Returns
        -------
        str
            Answer corresponding to clue.
        """
        if clue not in self._positions:
            raise ValueError("Clue does not exist.")
        return self.get_answer(*self._positions[clue])
    
    def allows_empty_clues(self) -> bool:
        """Check if board allows empty clues.

        Returns
        -------
        bool
            True if board allows empty clues, False otherwise.
        """
        return self._allow_empty_clues

    def set_allow_empty_clues(self, allow: bool) -> None:
        """Set whether board allows empty clues.

        Parameters
        ----------
        allow : bool
            Whether to allow empty clues.
        """
        self._allow_empty_clues = allow