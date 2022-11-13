"""Implements the CrosswordBoard class.

This class is used to represent a crossword board. It is used to
represent the state of a crossword board. Including information
about the clues, positions of the clues on the Board, and answers.
"""


class CrosswordBoard(object):
    """Represents a crossword board."""

    def __init__(self) -> None:
        """Initialize a crossword board."""
        # Board is a list of strings. Each string is a single character.
        self._board = []

        # Dictionary of clue positions. Key is (number, direction) and value
        # is a list of cells that the clue occupies.
        self._clue_positions = {}

        # Dictionary of clue answers. Key is (number, direction) and value
        # is the clue.
        self._clues = {}
        
        # Dictionary of clues and their corresponding positions. Key is
        # clue and value is a list of (number, direction) tuples.
        self._positions = {}

        # Dictionary of answers. Key is (number, direction) and value is
        # the answer.
        self._answers = {}
        self._allow_empty_clues = False
        self.dimensions = (0, 0)

    def __str__(self) -> str:
        """Get string representation of board.

        Returns
        -------
        str
            String representation of board.
        """
        width, height = self.get_dimensions()
        out = ''

        out += f'Board ({width}: {height}):\n'
        out += str('-' * (width + 2)) + '\n'
        for x in range(width):
            out += '|'
            for y in range(height):
                cell = self.get_cell(x * height + y)
                out += cell if cell else ' '
            out += '|\n'
        out += str('-' * (height + 2)) + '\n\n'


        out += f'Allow Empty Clues: {str(self._allow_empty_clues)}\n\n'

        out += 'Clue Positions:\n'
        for key, value in self._clue_positions.items():
            out += f'({key[0]}: {key[1]}): {value}\n'
        out += '\n'

        out += 'Clues:\n'
        for key, value in self._clues.items():
            out += f'({key[0]}: {key[1]}): {value}\n'
        out += '\n'

        out += 'Positions:\n'
        for key, value in self._positions.items():
            out += f'{key}: {value}\n'
        out += '\n'

        out += 'Answers:\n'
        for key, value in self._answers.items():
            out += f'({key[0]}: {key[1]}): {value}\n'
        out += '\n'

        return out

    def __repr__(self) -> str:
        """Get string representation of board.

        Returns
        -------
        str
            String representation of board.
        """
        return self.__str__()

    

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

    def get_dimensions(self) -> tuple:
        """Get dimension of board.

        Returns
        -------
        tuple
            Dimension of board.
        """
        return self.dimensions

    def set_dimensions(self, dimension: tuple) -> None:
        """Set dimension of board to (width, height).

        Sets the dimensions of the board. Whenever this is called,
        the board is reset.

        Parameters
        ----------
        dimension : tuple
            Dimension of board.
        """
        if not isinstance(dimension, tuple):
            raise ValueError('Dimension must be a tuple.')
        if len(dimension) != 2:
            raise ValueError('Dimension must be a tuple of length 2.')
        if not isinstance(dimension[0], int) or dimension[0] < 1:
            raise ValueError('Dimension[0] must be a positive integer.')
        if not isinstance(dimension[1], int) or dimension[1] < 1:
            raise ValueError('Dimension[1] must be a positive integer.')
        
        self._board = [''] * (dimension[0] * dimension[1])
        self.dimensions = dimension

    def get_cell(self, index: int) -> str:
        """Get cell from board.

        Parameters
        ----------
        index : int
            Index of cell to get.

        Returns
        -------
        str
            Cell at index.
        """
        if not isinstance(index, int) or index < 0:
            raise ValueError('Index must be a positive integer.')
        if index >= len(self._board):
            raise ValueError('Index out of range.')

        return self._board[index]

    def set_cell(self, index: int, cell: str) -> None:
        """Set board cell.

        Parameters
        ----------
        index : int
            Index of cell to set.

        cell : str
            Cell to set.
        """
        if not isinstance(index, int) or index < 0:
            raise ValueError('Index must be a positive integer.')
        if not isinstance(cell, str):
            raise ValueError('Cell must be a string.')
        if len(cell) > 1:
            raise ValueError('Cell must be a string of length 1 or 0.')
        if index >= len(self._board):
            raise ValueError('Index out of range.')
            
        self._board[index] = cell

    def remove_cell(self, index: int) -> None:
        """Remove cell from board.

        Parameters
        ----------
        index : int
            Index of cell to remove.
        """
        if not isinstance(index, int) or index < 0:
            raise ValueError('Index must be a positive integer.')
        if index >= len(self._board):
            raise ValueError('Index out of range.')

        self._board[index] = ''

    def get_answer_from_cells(self, cells: list) -> str:
        """Get answer from cells.

        Parameters
        ----------
        cells : list
            List of cells to get answer from.

        Returns
        -------
        str
            Answer from cells.
        """
        answer = ''
        for cell in cells:
            answer += self.get_cell(cell)
        return answer
    
    def add_clue_position(self, cells: list, number: int, direction: str) -> None:
        """Add clue position to board.

        Parameters
        ----------
        cells : list
            List of cells that the clue occupies.

        number : int
            Number corresponding to position on board.

        direction : str
            Direction corresponding to position on board. Must be one of
            'across' or 'down'.
        """
        self.__validate_position(number, direction)
        if (number, direction) in self._clue_positions:
            raise ValueError("Clue position already exists.")
        self._clue_positions[(number, direction)] = cells

    def get_clue_position(self, number: int, direction: str) -> list:
        """Get clue position.

        Parameters
        ----------
        number : int
            Number corresponding to position on board.

        direction : str
            Direction corresponding to position on board. Must be one of
            'across' or 'down'.

        Returns
        -------
        list
            List of cells that the clue occupies.
        """
        self.__validate_position(number, direction)
        if (number, direction) not in self._clue_positions:
            raise ValueError("Clue position does not exist.")

        return self._clue_positions[(number, direction)]

    def remove_clue_position(self, number: int, direction: str) -> None:
        """Remove clue position from number and direction (i.e position) on board.

        Parameters
        ----------
        number : int
            Number corresponding to position on board.

        direction : str
            Direction corresponding to position on board. Must be one of
            'across' or 'down'.
        """
        self.__validate_position(number, direction)
        if (number, direction) not in self._clue_positions:
            raise ValueError("Clue position does not exist.")

        del self._clue_positions[(number, direction)]

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
        if not isinstance(allow, bool):
            raise TypeError("allow must be a boolean.")
        
        self._allow_empty_clues = allow


if __name__ == '__main__':
    import doctest
    doctest.testmod()