"""Gets the Daily Crossword from the New York Times website.

This script generates a CrosswordBoard object from the New York Times
website.
"""

import requests
from CrosswordBoard import CrosswordBoard as Board


class NYTimesScraper(object):
    """Scrapes the New York Times website for the Daily Crossword."""

    def __init__(self) -> None:
        """Initialize the NYTimesScraper."""
        self._session = requests.Session()
        self._session.headers.update({'User-Agent': 'Mozilla/5.0'})
        self._url = "https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json"

    def get_dimensions(self, response) -> tuple:
        """Get the dimensions of the crossword board.

        Parameters
        ----------
        response : requests.Response
            Response from the New York Times website.

        Returns
        -------
        tuple
            Dimensions of the crossword board.
        """
        data = response.json()
        return (data['body'][0]['dimensions']['width'],
                data['body'][0]['dimensions']['height'])

    def get_crossword_board(self) -> Board:
        """Get the crossword board from the New York Times website.

        Returns
        -------
        CrosswordBoard
            Crossword board from the New York Times website.
        """
        board = Board()

        response = self._session.get(self._url)
        response.raise_for_status()

        data = response.json()
        board.set_dimensions(self.get_dimensions(response))
        for cell_no, cell in enumerate(data['body'][0]['cells']):
            answer = cell['answer'] if 'answer' in cell else ''
            board.set_cell(cell_no, answer)
        
        for clue in data['body'][0]['clues']:
            clue_cells = clue['cells']
            clue_direction = clue['direction'].lower()
            clue_number = int(clue['label'])
            clue_text = clue['text'][0]['plain']
            board.add_clue_position(clue_cells, clue_number, clue_direction)
            board.add_clue(clue_number, clue_direction, clue_text)

            # This isn't great design. 
            answer = board.get_answer_from_cells(clue_cells)
            board.add_answer(clue_number, clue_direction, answer)


        return board


if __name__ == '__main__':
    scraper = NYTimesScraper()
    board = scraper.get_crossword_board()
    print(board)
